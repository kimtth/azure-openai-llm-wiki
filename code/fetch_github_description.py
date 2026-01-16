import re
import requests

# Fetch repository descriptions from GitHub API
# Extracts clean, informative descriptions from GitHub repos

def get_repo_description(owner, repo):
    """
    Fetch GitHub repository description via API.
    Returns the description string or a fallback message if unavailable.
    """
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code != 200:
            print(f"  Failed to fetch {owner}/{repo}: HTTP {response.status_code}")
            return None
        
        data = response.json()
        description = data.get('description')
        
        if not description:
            # Try to use the name or topics as fallback
            topics = data.get('topics', [])
            if topics:
                return f"Repository for {', '.join(topics)}"
            return None
        
        # Clean up description: remove URLs, extra whitespace
        description = description.strip()
        # Limit to first sentence or 150 chars
        if len(description) > 150:
            description = description[:150].rsplit(' ', 1)[0] + '.'
        
        return description
    
    except Exception as e:
        print(f"  Error fetching {owner}/{repo}: {e}")
        return None


def process_text_with_descriptions(text):
    """
    Process markdown text and add GitHub repository descriptions after links.
    Preserves existing descriptions if present.
    
    Example input: "- [ ] [Agent-R1✨](https://github.com/0russwest0/Agent-R1):"
    Example output: "- [ ] [Agent-R1✨](https://github.com/0russwest0/Agent-R1): End-to-End reinforcement learning..."
    """
    lines = text.strip().split('\n')
    output = []
    
    # Pattern to match GitHub links and check if description already exists
    link_pattern = re.compile(r'\(https://github\.com/([^/\s]+)/([^/\s)]+)\):?\s*')
    
    for line in lines:
        match = link_pattern.search(line)
        
        if not match:
            output.append(line)
            continue
        
        owner, repo = match.group(1), match.group(2)
        repo = repo.rstrip('.')  # Remove trailing punctuation
        
        # Check if description already exists (after the colon)
        after_link = line[match.end():].strip()
        if after_link and not after_link.startswith('['):  # Has description
            output.append(line)
            continue
        
        # Fetch description
        print(f"Fetching description for: {owner}/{repo}")
        description = get_repo_description(owner, repo)
        
        if description:
            # Insert description after the link
            line_before_link = line[:match.start()] + match.group(0)
            new_line = line_before_link + description
            # Add remaining content if any
            remaining = line[match.end():]
            if remaining.strip() and not remaining.startswith(description):
                new_line += " " + remaining
            output.append(new_line)
        else:
            output.append(line)
    
    return '\n'.join(output)


if __name__ == "__main__":
    # Test with sample input
    test_input = """- [ ] [Agent-R1✨](https://github.com/0russwest0/Agent-R1):
- [ ] [ralph✨](https://github.com/snarktank/ralph):
- [ ] [SciSciGPT✨](https://github.com/Northwestern-CSSI/SciSciGPT):
- [ ] [superpowers✨](https://github.com/obra/superpowers):
- [ ] [Universal-Commerce-Protocol/ucp✨](https://github.com/Universal-Commerce-Protocol/ucp):
- [ ] [ART✨](https://github.com/OpenPipe/ART):"""
    
    print("Fetching repository descriptions...\n")
    result = process_text_with_descriptions(test_input)
    print("\n" + "="*80)
    print("Result:")
    print("="*80)
    print(result)
