from __future__ import annotations

import argparse
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from utils.github_api import get_repo_description
from utils.http_utils import create_session
from utils.io_utils import read_text_input, write_text_output
from utils.markdown_utils import GITHUB_REPO_URL_WITH_COLON_PATTERN, clean_repo_name

# Fetch repository descriptions from GitHub API
# Extracts clean, informative descriptions from GitHub repos


def process_text_with_descriptions(text: str, *, session, timeout: int, max_retries: int) -> str:
    """
    Process markdown text and add GitHub repository descriptions after links.
    Preserves existing descriptions if present.
    
    Example input: "- [ ] [Agent-R1✨](https://github.com/0russwest0/Agent-R1):"
    Example output: "- [ ] [Agent-R1✨](https://github.com/0russwest0/Agent-R1): End-to-End reinforcement learning..."
    """
    lines = text.strip().split('\n')
    output = []
    
    # Pattern to match GitHub links and check if description already exists
    link_pattern = GITHUB_REPO_URL_WITH_COLON_PATTERN

    for line in lines:
        match = link_pattern.search(line)
        
        if not match:
            output.append(line)
            continue
        
        owner, repo = match.group(1), clean_repo_name(match.group(2))
        
        # Check if description already exists (after the colon)
        after_link = line[match.end():].strip()
        if after_link and not after_link.startswith('['):  # Has description
            output.append(line)
            continue
        
        # Fetch description
        print(f"Fetching description for: {owner}/{repo}", file=sys.stderr)
        description = get_repo_description(owner, repo, session=session, timeout=timeout, max_retries=max_retries)
        
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
    
    return "\n".join(output)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Append GitHub repository descriptions to markdown lines.")
    parser.add_argument("--input", help="Input markdown file path (or '-' for stdin).")
    parser.add_argument("--output", help="Output file path (or '-' for stdout).")
    parser.add_argument("--in-place", action="store_true", help="Overwrite the input file.")
    parser.add_argument("--timeout", type=int, default=10, help="Request timeout in seconds.")
    parser.add_argument("--max-retries", type=int, default=3, help="Max retries for API calls.")
    parser.add_argument("--user-agent", default="awesome-azure-openai-llm/1.0", help="Custom User-Agent for GitHub API.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    text = read_text_input(args.input)

    session = create_session(args.user_agent)
    result = process_text_with_descriptions(text, session=session, timeout=args.timeout, max_retries=args.max_retries)

    if args.in_place:
        if not args.input or args.input == "-":
            parser.error("--in-place requires --input with a file path.")
        Path(args.input).write_text(result, encoding="utf-8")
    else:
        write_text_output(result, args.output)


if __name__ == "__main__":
    main()
