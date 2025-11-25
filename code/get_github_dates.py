import re
import requests
from datetime import datetime

# Process markdown text with GitHub links and append creation dates
# Example input: "- [ ] [Agent-R1✨](https://github.com/0russwest0/Agent-R1): Description"
# Example output: "- [ ] [Agent-R1✨](https://github.com/0russwest0/Agent-R1): Description [Mar 2025]"

def get_repo_created_date(owner, repo):
    """
    Fetch GitHub repository creation date via API.
    Returns formatted date string like [Mar 2025] or None if failed.
    """
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    
    try:
        response = requests.get(api_url, timeout=10)
        if response.status_code != 200:
            print(f"  Failed to fetch {owner}/{repo}: HTTP {response.status_code}")
            return None
        
        data = response.json()
        created_at = data.get('created_at')
        
        if not created_at:
            return None
        
        # Parse ISO 8601 date and format as [Mon YYYY]
        dt = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
        return f"[{dt.strftime('%b %Y')}]"
    
    except Exception as e:
        print(f"  Error fetching {owner}/{repo}: {e}")
        return None


def process_text(text):
    """
    Process markdown text and append creation dates to lines with GitHub URLs.
    """
    lines = text.strip().split('\n')
    output = []
    link_pattern = re.compile(r'\(https://github\.com/([^/\s]+)/([^/\s)]+)\)')
    date_pattern = re.compile(r'\[([A-Z][a-z]{2} \d{4})\]')
    
    for line in lines:
        # Check if line already has a date
        if date_pattern.search(line):
            output.append(line)
            continue
        
        match = link_pattern.search(line)
        if match:
            owner, repo = match.group(1), match.group(2)
            print(f"Fetching: {owner}/{repo}")
            date = get_repo_created_date(owner, repo)
            if date:
                # Append date at the end of the line
                line = line.rstrip() + f" {date}"
        
        output.append(line)
    
    return '\n'.join(output)


if __name__ == "__main__":
    # Test with provided input
    test_input = """- [ ] [Agent-R1✨](https://github.com/0russwest0/Agent-R1): End-to-End reinforcement learning to train agents in specific environments.
- [ ] [Tinker Cookbook✨](https://github.com/thinking-machines-lab/tinker-cookbook): Thinking Machines Lab. Training SDK to fine-tune language models. 
- [ ] [verl✨](https://github.com/volcengine/verl): ByteDance. RL training library for LLMs
- [ ] [RLinf✨](https://github.com/RLinf/RLinf): Post-training foundation models (LLMs, VLMs, VLAs) via reinforcement learning.
- [ ] [MineContext✨](https://github.com/volcengine/MineContext): a context-aware AI agent desktop application.
- [ ] [NocoBase✨](https://github.com/nocobase/nocobase): Data model-driven. AI-powered no-code platform.
- [ ] [PaddleOCR✨](https://github.com/PaddlePaddle/PaddleOCR): Turn any PDF or image document into structured data.
- [ ] [EmbedAnything✨](https://github.com/StarlightSearch/EmbedAnything): Built by Rust. Supports BERT, CLIP, Jina, ColPali, ColBERT, ModernBERT, Reranker, Qwen. Mutilmodality.
- [ ] [FalkorDB✨](https://github.com/FalkorDB/FalkorDB): Graph Database. Knowledge Graph for LLM (GraphRAG)."""
    
    print("Processing text...\n")
    result = process_text(test_input)
    print("\n" + "="*80)
    print("Result:")
    print("="*80)
    print(result)
