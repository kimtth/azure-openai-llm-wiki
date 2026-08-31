"""Update citation counts for papers in the Ranked by cite count sections."""

from __future__ import annotations

import argparse
import re
import sys
import time
from pathlib import Path

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

def extract_papers_from_ranked_section(content: str, section_name: str) -> list[tuple[str, str, int, str, str]]:
    """Extract papers from a ranked section."""
    section_pattern = f'### \\*\\*{re.escape(section_name)}\\*\\*'
    section_match = re.search(section_pattern, content)
    if not section_match:
        return []
    
    start = section_match.end()
    next_section = re.search(r'\n(?:###|---)', content[start:])
    section_content = content[start:start + next_section.start()] if next_section else content[start:]
    
    paper_pattern = r'^-\s+\[([^\]]*?)📑(?:💡)?\]\(https://arxiv\.org/abs/(\d{4}\.\d{4,5})\):[^\n]+\(Citations:\s*([\d,]+)\)'
    
    return [
        (
            match.group(1),
            match.group(2),
            int(match.group(3).replace(",", "")),
            match.group(3),
            match.group(0),
        )
        for match in re.finditer(paper_pattern, section_content, re.MULTILINE)
    ]

def sort_ranked_section(content: str, section_name: str) -> str:
    """Sort a ranked section in descending citation-count order."""
    section_pattern = f'### \\*\\*{re.escape(section_name)}\\*\\*'
    section_match = re.search(section_pattern, content)
    if not section_match:
        return content

    start = section_match.end()
    next_section = re.search(r'\n(?:###|---)', content[start:])
    end = start + next_section.start() if next_section else len(content)
    section_lines = content[start:end].splitlines(keepends=True)
    citation_lines = [
        line for line in section_lines
        if re.search(r'\(Citations:\s*[\d,]+\)', line)
    ]
    sorted_citation_lines = sorted(
        citation_lines,
        key=lambda line: int(re.search(r'\(Citations:\s*([\d,]+)\)', line).group(1).replace(",", "")),
        reverse=True,
    )
    citation_line_iter = iter(sorted_citation_lines)
    sorted_section = "".join(
        next(citation_line_iter) if line in citation_lines else line
        for line in section_lines
    )
    return content[:start] + sorted_section + content[end:]

def update_ranked_sections(
    file_path: Path,
    *,
    timeout: int,
    max_retries: int,
    sleep_s: float,
    dry_run: bool,
    sort_only: bool,
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

        if sort_only:
            continue

        for idx, (title, arxiv_id, current_citations, current_citations_text, original_text) in enumerate(papers, 1):
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
                    f'(Citations: {current_citations_text})',
                    f'(Citations: {new_citations:,})'
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
    
    if not sort_only:
        print(f"\nProcessed {total_papers} papers")

    updated_content = content
    if replacements:
        print("\nUpdates needed:")
        for i, r in enumerate(replacements, 1):
            print(f"{i}. {r['title'][:50]}... ({r['arxiv_id']}): {r['old_count']} → {r['new_count']}")
        
        for r in replacements:
            updated_content = updated_content.replace(r['old'], r['new'])

    for section_name in sections:
        updated_content = sort_ranked_section(updated_content, section_name)

    if updated_content == content:
        print("✓ All up to date")
    elif dry_run:
        print("\nDRY RUN: No files written.")
    else:
        file_path.write_text(updated_content, encoding="utf-8")
        print(f"\n✓ Updated {len(replacements)} papers and re-sorted ranked sections")

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
    parser.add_argument("--sort-only", action="store_true", help="Re-sort ranked sections without calling the API.")
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
        sort_only=args.sort_only,
    )


if __name__ == "__main__":
    main()
