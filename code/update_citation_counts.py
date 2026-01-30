"""Update citation counts for papers in the Ranked by cite count sections."""

from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path
from typing import List, Tuple

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from utils.http_utils import create_session, get_json
from utils.path_utils import get_repo_root


def get_citation_count(
    arxiv_id: str,
    *,
    session,
    timeout: int,
    max_retries: int,
    backoff: float,
) -> int | None:
    """Fetch citation count from Semantic Scholar API."""
    url = f"https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}"
    params = {"fields": "citationCount"}

    data = get_json(
        session,
        url,
        params=params,
        timeout=timeout,
        max_retries=max_retries,
        backoff=backoff,
    )
    if not data:
        return None
    return data.get("citationCount", 0)

def extract_papers_from_ranked_section(content: str, section_name: str) -> List[Tuple[str, str, int, str]]:
    """Extract papers from a ranked section."""
    section_pattern = f'### \\*\\*{re.escape(section_name)}\\*\\*'
    section_match = re.search(section_pattern, content)
    if not section_match:
        return []
    
    start = section_match.end()
    next_section = re.search(r'\n(?:###|---)', content[start:])
    section_content = content[start:start + next_section.start()] if next_section else content[start:]
    
    paper_pattern = r'(\d+)\.\s+\[([^\]]+)📑💡?\]\(https://arxiv\.org/abs/(\d{4}\.\d{4,5})\):[^\n]+\(Citations:\s*(\d+)\)'
    
    return [
        (match.group(1), match.group(2), match.group(3), int(match.group(4)), match.group(0))
        for match in re.finditer(paper_pattern, section_content)
    ]

def update_ranked_sections(
    file_path: Path,
    *,
    timeout: int,
    max_retries: int,
    sleep_s: float,
    dry_run: bool,
) -> int:
    """Update citation counts in ranked sections."""

    content = file_path.read_text(encoding="utf-8")
    
    sections = [
        'RAG Research (Ranked by cite count >=100)',
        'Agent Research (Ranked by cite count >=100)'
    ]
    
    replacements = []
    total_papers = 0
    
    session = create_session("awesome-azure-openai-llm/1.0")

    for section_name in sections:
        papers = extract_papers_from_ranked_section(content, section_name)
        total_papers += len(papers)
        
        for idx, (_, title, arxiv_id, current_citations, original_text) in enumerate(papers, 1):
            print(f"[{idx}/{len(papers)}] Checking {arxiv_id}...", end='\r')
            new_citations = get_citation_count(
                arxiv_id,
                session=session,
                timeout=timeout,
                max_retries=max_retries,
                backoff=max(1.0, sleep_s),
            )
            
            if new_citations is not None and new_citations != current_citations:
                new_text = original_text.replace(
                    f'(Citations: {current_citations})',
                    f'(Citations: {new_citations})'
                )
                
                replacements.append({
                    'old': original_text,
                    'new': new_text,
                    'title': title,
                    'arxiv_id': arxiv_id,
                    'old_count': current_citations,
                    'new_count': new_citations
                })
                print(f"[{idx}/{len(papers)}] {arxiv_id}: {current_citations} → {new_citations}")
            
            time.sleep(sleep_s)
    
    print(f"\nProcessed {total_papers} papers")
    
    if replacements:
        print("\nUpdates needed:")
        for i, r in enumerate(replacements, 1):
            print(f"{i}. {r['title'][:50]}... ({r['arxiv_id']}): {r['old_count']} → {r['new_count']}")
        
        updated_content = content
        for r in replacements:
            updated_content = updated_content.replace(r['old'], r['new'])
        
        if dry_run:
            print("\nDRY RUN: No files written.")
        else:
            file_path.write_text(updated_content, encoding="utf-8")
            print(f"\n✓ Updated {len(replacements)} papers")
    else:
        print("✓ All up to date")

    return len(replacements)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Update citation counts in ranked paper sections.")
    parser.add_argument(
        "--file",
        help="Target markdown file (default: section/best_practices.md).",
    )
    parser.add_argument("--timeout", type=int, default=10, help="Request timeout in seconds.")
    parser.add_argument("--max-retries", type=int, default=3, help="Max retries for API calls.")
    parser.add_argument("--sleep", type=float, default=0.5, help="Sleep between API calls in seconds.")
    parser.add_argument("--dry-run", action="store_true", help="Preview updates without writing.")
    return parser

def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    root = get_repo_root(__file__)
    file_path = Path(args.file) if args.file else root / "section" / "best_practices.md"
    update_ranked_sections(
        file_path,
        timeout=args.timeout,
        max_retries=args.max_retries,
        sleep_s=args.sleep,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
