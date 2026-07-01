from __future__ import annotations

import argparse
import os
import random
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import requests

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from utils.http_utils import create_session  # noqa: E402
from utils.path_utils import get_repo_root  # noqa: E402


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

    def __init__(
        self,
        *,
        user_agent: Optional[str],
        api_key: Optional[str],
        timeout: int,
        max_retries: int,
        backoff: float,
        request_delay: float,
        jitter: float,
    ):
        self.session = create_session(user_agent)
        if api_key:
            self.session.headers.update({"x-api-key": api_key})
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff = backoff
        self.request_delay = request_delay
        self.jitter = jitter

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

        url = f"{self.BASE_URL}/paper/search"
        backoff = self.backoff
        last_error = "no response"

        for attempt in range(self.max_retries):
            try:
                response = self.session.get(url, params=params, timeout=self.timeout)
            except requests.RequestException as exc:
                last_error = f"{type(exc).__name__}: {exc}"
            else:
                if response.status_code == 200:
                    if self.request_delay > 0:
                        time.sleep(self.request_delay + random.uniform(0, max(self.jitter, 0)))
                    return response.json().get("data", [])

                message = ""
                try:
                    payload = response.json()
                    message = str(payload.get("message") or payload.get("error") or "").strip()
                except ValueError:
                    message = response.text[:200].strip()
                last_error = f"HTTP {response.status_code}"
                if message:
                    last_error += f": {message}"

                if response.status_code not in {429, 500, 502, 503, 504}:
                    break

                retry_after = response.headers.get("Retry-After")
                if retry_after:
                    try:
                        backoff = max(backoff, float(retry_after))
                    except ValueError:
                        pass
                elif response.status_code == 429:
                    backoff = max(backoff, 60.0)

            if attempt < self.max_retries - 1:
                time.sleep(backoff)
                backoff = min(backoff * 2, 300.0)

        if self.request_delay > 0:
            time.sleep(self.request_delay + random.uniform(0, max(self.jitter, 0)))
        raise RuntimeError(f"Semantic Scholar query failed after retries ({last_error}): {query}")

    def batch_papers(self, ids: List[str], fields: List[str] | None = None) -> List[Dict | None]:
        """Fetch papers by stable IDs in one low-volume API request."""
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

        url = f"{self.BASE_URL}/paper/batch"
        params = {"fields": ",".join(fields)}
        backoff = self.backoff
        last_error = "no response"

        for attempt in range(self.max_retries):
            try:
                response = self.session.post(url, params=params, json={"ids": ids}, timeout=self.timeout)
            except requests.RequestException as exc:
                last_error = f"{type(exc).__name__}: {exc}"
            else:
                if response.status_code == 200:
                    if self.request_delay > 0:
                        time.sleep(self.request_delay + random.uniform(0, max(self.jitter, 0)))
                    return response.json()

                message = ""
                try:
                    payload = response.json()
                    message = str(payload.get("message") or payload.get("error") or "").strip()
                except ValueError:
                    message = response.text[:200].strip()
                last_error = f"HTTP {response.status_code}"
                if message:
                    last_error += f": {message}"

                if response.status_code not in {429, 500, 502, 503, 504}:
                    break

                retry_after = response.headers.get("Retry-After")
                if retry_after:
                    try:
                        backoff = max(backoff, float(retry_after))
                    except ValueError:
                        pass
                elif response.status_code == 429:
                    backoff = max(backoff, 60.0)

            if attempt < self.max_retries - 1:
                time.sleep(backoff)
                backoff = min(backoff * 2, 300.0)

        if self.request_delay > 0:
            time.sleep(self.request_delay + random.uniform(0, max(self.jitter, 0)))
        raise RuntimeError(f"Semantic Scholar batch fetch failed after retries ({last_error})")

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


def paper_lookup_id(paper: Dict) -> Optional[str]:
    external_ids = paper.get("externalIds") or {}
    arxiv_id = external_ids.get("ArXiv")
    if arxiv_id:
        return f"ARXIV:{arxiv_id}"
    url = paper.get("url") or ""
    if "arxiv.org/abs/" in url:
        return "ARXIV:" + url.rsplit("/abs/", 1)[1].strip()
    if "semanticscholar.org/paper/" in url:
        return url.rsplit("/paper/", 1)[1].split("/", 1)[0].strip()
    return None


def parse_existing_markdown(filename: str) -> List[Tuple[str, List[Dict]]]:
    text = Path(filename).read_text(encoding="utf-8")
    sections: List[Tuple[str, List[Dict]]] = []
    section_re = re.compile(r"^## (.+?)\n\n\*Retrieved: [^*]+\*\n\n(.*?)(?=^## |\Z)", re.S | re.M)
    entry_re = re.compile(r"^### \d+\. (.+?)\n\n(.*?)(?=^### \d+\. |\Z)", re.S | re.M)

    for section_match in section_re.finditer(text):
        topic_name = section_match.group(1)
        papers: List[Dict] = []
        for entry_match in entry_re.finditer(section_match.group(2)):
            title = entry_match.group(1).strip()
            block = entry_match.group(2)
            citation_match = re.search(r"\*\*Citations:\*\* ([\d,]+)", block)
            year_match = re.search(r"\*\*Year:\*\* (\d{4}|N/A)", block)
            venue_match = re.search(r"\| \*\*Venue:\*\*([^\n]+)", block)
            fields_match = re.search(r"\*\*Fields:\*\*([^\n]+)", block)
            url_match = re.search(r"\*\*URL:\*\* \[([^\]]+)\]", block)
            arxiv_match = re.search(r"\*\*arXiv:\*\* \[https://arxiv\.org/abs/([^\]]+)\]", block)
            abstract_match = re.search(r"\*\*Abstract:\*\* (.*?)(?:\n\n---|\Z)", block, re.S)
            authors_match = re.search(r"\*\*Authors:\*\*([^\n]+)", block)

            external_ids = {"ArXiv": arxiv_match.group(1)} if arxiv_match else {}
            papers.append({
                "title": title,
                "authors": [{"name": name.strip()} for name in (authors_match.group(1).split(",") if authors_match else [])],
                "year": None if not year_match or year_match.group(1) == "N/A" else int(year_match.group(1)),
                "citationCount": int(citation_match.group(1).replace(",", "")) if citation_match else 0,
                "venue": venue_match.group(1).strip() if venue_match else "",
                "url": url_match.group(1).strip() if url_match else "",
                "externalIds": external_ids,
                "fieldsOfStudy": [field.strip() for field in fields_match.group(1).split(",")] if fields_match else [],
                "abstract": " ".join(abstract_match.group(1).split()) if abstract_match else "",
            })
        sections.append((topic_name, papers))
    return sections


def refresh_existing_markdown(fetcher: SemanticScholarFetcher, filename: str, min_citations: int) -> None:
    sections = parse_existing_markdown(filename)
    lookup_ids = [paper_lookup_id(paper) for _, papers in sections for paper in papers]
    live_by_id: Dict[str, Dict | None] = {}

    for start in range(0, len(lookup_ids), 450):
        chunk = [paper_id for paper_id in lookup_ids[start:start + 450] if paper_id]
        if not chunk:
            continue
        print(f"[batch] Fetching {len(chunk)} papers ({start + 1}-{start + len(chunk)})")
        live_by_id.update(zip(chunk, fetcher.batch_papers(chunk)))

    refreshed_sections: List[Tuple[str, List[Dict]]] = []
    changed = 0
    missing = 0
    for topic_name, papers in sections:
        refreshed = []
        for paper in papers:
            lookup_id = paper_lookup_id(paper)
            live = live_by_id.get(lookup_id or "")
            if live:
                if live.get("citationCount") != paper.get("citationCount"):
                    changed += 1
                refreshed.append(live)
            else:
                missing += 1
                refreshed.append(paper)
        filtered = [
            paper for paper in refreshed
            if paper.get("citationCount", 0) >= min_citations
            and "Computer Science" in (paper.get("fieldsOfStudy") or [])
        ]
        filtered.sort(key=lambda paper: paper.get("citationCount", 0), reverse=True)
        refreshed_sections.append((topic_name, filtered))

    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Popular Papers on RAG & AI Agents (Computer Science)\n\n")
        f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
        f.write("*Source: Semantic Scholar batch API refresh of existing paper IDs*\n")
        f.write("*Filtered for Computer Science papers only*\n")

    for topic_name, papers in refreshed_sections:
        save_to_markdown(topic_name, papers, filename)

    print(
        f"Refreshed {sum(len(papers) for _, papers in refreshed_sections)} existing papers from Semantic Scholar batch API: "
        f"{changed} citation count(s) changed, {missing} missing response(s)."
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Fetch top-cited RAG/agent papers from Semantic Scholar.")
    parser.add_argument("--output", help="Output markdown file path.")
    parser.add_argument("--min-citations", type=int, default=100, help="Minimum citation threshold.")
    parser.add_argument("--top-n", type=int, default=30, help="Top N papers per query.")
    parser.add_argument("--timeout", type=int, default=30, help="Request timeout in seconds.")
    parser.add_argument("--max-retries", type=int, default=5, help="Max retries for API calls.")
    parser.add_argument("--backoff", type=float, default=1.0, help="Initial backoff in seconds.")
    parser.add_argument(
        "--request-delay", type=float, default=2.0,
        help="Delay between Semantic Scholar requests in seconds."
    )
    parser.add_argument(
        "--jitter", type=float, default=0.5,
        help="Random extra delay between requests in seconds."
    )
    parser.add_argument(
        "--api-key-env", default="S2_API_KEY",
        help="Environment variable containing a Semantic Scholar API key, if available."
    )
    parser.add_argument(
        "--refresh-existing", action="store_true",
        help="Refresh existing output entries from Semantic Scholar batch API without running search queries."
    )
    parser.add_argument("--user-agent", default="Academic-Research-Tool/1.0", help="Custom User-Agent.")
    args = parser.parse_args()

    fetcher = SemanticScholarFetcher(
        user_agent=args.user_agent,
        api_key=os.environ.get(args.api_key_env),
        timeout=args.timeout,
        max_retries=args.max_retries,
        backoff=args.backoff,
        request_delay=args.request_delay,
        jitter=args.jitter,
    )

    root_dir = get_repo_root(__file__)
    output_file = args.output or str(root_dir / "section" / "x_popular_papers.md")

    if args.refresh_existing:
        refresh_existing_markdown(fetcher, output_file, args.min_citations)
        return

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
    
    topic_papers = []
    for topic_name, queries in topics.items():
        print(f"\nTopic: {topic_name}")
        
        all_papers = []
        seen_ids = set()
        failed_queries = []
        for query in queries:
            try:
                query_papers = fetcher.get_papers_sorted_by_citations(query, top_n=args.top_n, min_citations=args.min_citations)
            except RuntimeError as exc:
                failed_queries.append(str(exc))
                print(f"  [WARN] {exc}")
                continue

            for paper in query_papers:
                paper_id = paper.get('paperId')
                if paper_id and paper_id not in seen_ids:
                    seen_ids.add(paper_id)
                    all_papers.append(paper)
            if len(all_papers) >= args.top_n:
                break
        
        # Filter and sort
        filtered_papers = [p for p in all_papers if p.get('citationCount', 0) >= args.min_citations]
        filtered_papers.sort(key=lambda x: x.get('citationCount', 0), reverse=True)
        if not filtered_papers:
            if failed_queries:
                print("\n".join(f"  [ERROR] {error}" for error in failed_queries))
            raise RuntimeError(
                f"No papers found for {topic_name}. The API may be unavailable or rate limited; "
                "leaving the existing output file unchanged."
            )
        topic_papers.append((topic_name, filtered_papers))
        
        for idx, paper in enumerate(filtered_papers, 1):
            print(format_paper_info(paper, idx))
        
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Popular Papers on RAG & AI Agents (Computer Science)\n\n")
        f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n")
        f.write("*Filtered for Computer Science papers only*\n")
    
    for topic_name, filtered_papers in topic_papers:
        save_to_markdown(topic_name, filtered_papers, output_file)
        print(f"Saved {len(filtered_papers)} papers")
    
    print(f"\nResults saved to: {output_file}")


if __name__ == "__main__":
    main()
