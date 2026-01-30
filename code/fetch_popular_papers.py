from __future__ import annotations

import argparse
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from utils.http_utils import create_session, get_json
from utils.path_utils import get_repo_root


def infer_arxiv_date(arxiv_id: str) -> Optional[Tuple[int, int]]:
    """Infer (year, month) from arXiv ID (YYMM.NNNNN format)."""
    match = re.match(r'(\d{2})(\d{2})\.(\d{4,5})', arxiv_id)
    if not match:
        return None
    yy, mm = int(match.group(1)), int(match.group(2))
    year = 2000 + yy if yy <= 99 else yy
    if not (1 <= mm <= 12 and 1991 <= year <= datetime.now().year + 1):
        return None
    return year, mm

def format_month_year(year: int, month: int) -> str:
    """Format as [Mon YYYY]"""
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    return f"[{months[month-1]} {year}]"

class SemanticScholarFetcher:
    """Fetch popular papers from Semantic Scholar API."""

    BASE_URL = "https://api.semanticscholar.org/graph/v1"

    def __init__(self, *, user_agent: Optional[str], timeout: int, max_retries: int, backoff: float):
        self.session = create_session(user_agent)
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff = backoff

    def search_papers(self, query: str, limit: int = 50, fields: List[str] | None = None) -> List[Dict]:
        """Search papers by query and return results."""
        if fields is None:
            fields = [
                "paperId",
                "title",
                "authors",
                "year",
                "citationCount",
                "abstract",
                "venue",
                "url",
                "externalIds",
                "fieldsOfStudy",
            ]

        params = {
            "query": query,
            "limit": min(limit, 100),
            "fields": ",".join(fields),
        }

        data = get_json(
            self.session,
            f"{self.BASE_URL}/paper/search",
            params=params,
            timeout=self.timeout,
            max_retries=self.max_retries,
            backoff=self.backoff,
        )
        if not data:
            return []
        return data.get("data", [])

    def get_papers_sorted_by_citations(self, query: str, top_n: int = 30, min_citations: int = 100) -> List[Dict]:
        """Get top N papers sorted by citation count."""
        papers = self.search_papers(query, limit=100)

        cs_papers = [
            p
            for p in papers
            if p.get("fieldsOfStudy")
            and "Computer Science" in p.get("fieldsOfStudy", [])
            and p.get("citationCount", 0) >= min_citations
        ]

        sorted_papers = sorted(cs_papers, key=lambda x: x.get("citationCount", 0), reverse=True)
        time.sleep(1)
        return sorted_papers[:top_n]


def format_paper_info(paper: Dict, rank: int) -> str:
    """Format paper information for display"""
    authors = paper.get('authors', [])
    author_names = ', '.join([a.get('name', '') for a in authors[:3]])
    if len(authors) > 3:
        author_names += ', et al.'
    
    external_ids = paper.get('externalIds', {})
    arxiv_id = external_ids.get('ArXiv') if external_ids else None
    arxiv_url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None
    
    year_month_str = ""
    if arxiv_id:
        ym = infer_arxiv_date(arxiv_id)
        if ym:
            year_month_str = format_month_year(ym[0], ym[1])
    
    lines = [
        f"\n{rank}. {paper.get('title', 'No title')}",
        f"   Authors: {author_names}",
        f"   Year: {paper.get('year', 'N/A')} | Citations: {paper.get('citationCount', 0):,} | Venue: {paper.get('venue', 'N/A')}"
    ]
    
    if year_month_str:
        lines.append(f"   Year Month: {year_month_str}")
    if paper.get('fieldsOfStudy'):
        lines.append(f"   Fields: {', '.join(paper['fieldsOfStudy'])}")
    lines.append(f"   URL: {paper.get('url', 'N/A')}")
    if arxiv_url:
        lines.append(f"   arXiv: {arxiv_url}")
    
    return '\n'.join(lines) + '\n'


def save_to_markdown(topic: str, papers: List[Dict], filename: str):
    """Save papers to a markdown file"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(f"\n## {topic}\n\n*Retrieved: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n")
        
        for idx, paper in enumerate(papers, 1):
            authors = paper.get('authors', [])
            author_names = ', '.join([a.get('name', '') for a in authors[:3]])
            if len(authors) > 3:
                author_names += ', et al.'
            
            external_ids = paper.get('externalIds', {})
            arxiv_id = external_ids.get('ArXiv') if external_ids else None
            arxiv_url = f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None
            
            year_month_str = ""
            if arxiv_id:
                ym = infer_arxiv_date(arxiv_id)
                if ym:
                    year_month_str = format_month_year(ym[0], ym[1])
            
            f.write(f"### {idx}. {paper.get('title', 'No title')}\n\n")
            f.write(f"**Authors:** {author_names}  \n")
            f.write(f"**Year:** {paper.get('year', 'N/A')} | **Citations:** {paper.get('citationCount', 0):,} | **Venue:** {paper.get('venue', 'N/A')}  \n")
            
            if year_month_str:
                f.write(f"**Year Month:** {year_month_str}  \n")
            if paper.get('fieldsOfStudy'):
                f.write(f"**Fields:** {', '.join(paper['fieldsOfStudy'])}  \n")
            
            url = paper.get('url', 'N/A')
            f.write(f"**URL:** [{url}]({url})  \n")
            if arxiv_url:
                f.write(f"**arXiv:** [{arxiv_url}]({arxiv_url})  \n")
            
            if paper.get('abstract'):
                f.write(f"\n**Abstract:** {paper['abstract']}\n\n")
            f.write("---\n\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch top-cited RAG/agent papers from Semantic Scholar.")
    parser.add_argument("--output", help="Output markdown file path.")
    parser.add_argument("--min-citations", type=int, default=100, help="Minimum citation threshold.")
    parser.add_argument("--top-n", type=int, default=30, help="Top N papers per query.")
    parser.add_argument("--timeout", type=int, default=30, help="Request timeout in seconds.")
    parser.add_argument("--max-retries", type=int, default=5, help="Max retries for API calls.")
    parser.add_argument("--backoff", type=float, default=1.0, help="Initial backoff in seconds.")
    parser.add_argument("--user-agent", default="Academic-Research-Tool/1.0", help="Custom User-Agent.")
    args = parser.parse_args()

    fetcher = SemanticScholarFetcher(
        user_agent=args.user_agent,
        timeout=args.timeout,
        max_retries=args.max_retries,
        backoff=args.backoff,
    )

    topics = {
        "RAG (Retrieval-Augmented Generation)": [
            "Retrieval-Augmented Generation",
            "RAG language models",
            "retrieval augmented generation",
            "RAG"
        ],
        "AI Agents": [
            "AI agents",
            "LLM agents",
            "LM Agents",
            "LLM agent"
        ]
    }
    
    root_dir = get_repo_root(__file__)
    output_file = args.output or str(root_dir / "section" / "x_popular_papers.md")
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Popular Papers on RAG & AI Agents (Computer Science)\n\n")
        f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
        f.write("*Filtered for Computer Science papers only*\n")
    
    for topic_name, queries in topics.items():
        print(f"\nTopic: {topic_name}")
        
        all_papers = []
        for query in queries:
            all_papers.extend(fetcher.get_papers_sorted_by_citations(query, top_n=args.top_n, min_citations=args.min_citations))
        
        # Remove duplicates
        seen_ids = set()
        unique_papers = []
        for paper in all_papers:
            paper_id = paper.get('paperId')
            if paper_id and paper_id not in seen_ids:
                seen_ids.add(paper_id)
                unique_papers.append(paper)
        
        # Filter and sort
        filtered_papers = [p for p in unique_papers if p.get('citationCount', 0) >= args.min_citations]
        filtered_papers.sort(key=lambda x: x.get('citationCount', 0), reverse=True)
        
        for idx, paper in enumerate(filtered_papers, 1):
            print(format_paper_info(paper, idx))
        
        save_to_markdown(topic_name, filtered_papers, output_file)
        print(f"Saved {len(filtered_papers)} papers")
    
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    main()
