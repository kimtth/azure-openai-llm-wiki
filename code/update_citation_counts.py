"""
Update citation counts for papers in the Ranked by cite count sections.
Uses Semantic Scholar API to fetch real-time citation counts.
"""

import re
import time
import requests
from typing import Tuple, List

def get_citation_count(arxiv_id: str) -> int:
    """Fetch citation count from Semantic Scholar API."""
    url = f'https://api.semanticscholar.org/graph/v1/paper/arXiv:{arxiv_id}'
    params = {'fields': 'citationCount'}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            return response.json().get('citationCount', 0)
        elif response.status_code == 429:
            time.sleep(60)
            return get_citation_count(arxiv_id)
        return None
    except Exception:
        return None

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

def update_ranked_sections(file_path: str):
    """Update citation counts in ranked sections."""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    sections = [
        'RAG Research (Ranked by cite count >=100)',
        'Agent Research (Ranked by cite count >=100)'
    ]
    
    replacements = []
    total_papers = 0
    
    for section_name in sections:
        papers = extract_papers_from_ranked_section(content, section_name)
        total_papers += len(papers)
        
        for idx, (_, title, arxiv_id, current_citations, original_text) in enumerate(papers, 1):
            print(f"[{idx}/{len(papers)}] Checking {arxiv_id}...", end='\r')
            new_citations = get_citation_count(arxiv_id)
            
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
            
            time.sleep(0.5)
    
    print(f"\nProcessed {total_papers} papers")
    
    if replacements:
        print(f"\nUpdates needed:")
        for i, r in enumerate(replacements, 1):
            print(f"{i}. {r['title'][:50]}... ({r['arxiv_id']}): {r['old_count']} → {r['new_count']}")
        
        updated_content = content
        for r in replacements:
            updated_content = updated_content.replace(r['old'], r['new'])
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        
        print(f"\n✓ Updated {len(replacements)} papers")
    else:
        print("✓ All up to date")

if __name__ == '__main__':
    update_ranked_sections('section/best_practices.md')
