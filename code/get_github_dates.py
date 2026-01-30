from __future__ import annotations

import argparse
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from utils.github_api import get_repo_created_date
from utils.http_utils import create_session
from utils.io_utils import read_text_input, write_text_output
from utils.markdown_utils import DATE_TOKEN_PATTERN, GITHUB_REPO_URL_PATTERN, clean_repo_name

# Process markdown text with GitHub links and append creation dates


def process_text(text: str, *, session, timeout: int, max_retries: int) -> str:
    """
    Process markdown text and append creation dates to lines with GitHub URLs.
    """
    lines = text.strip().split('\n')
    output = []
    link_pattern = GITHUB_REPO_URL_PATTERN
    date_pattern = DATE_TOKEN_PATTERN
    
    for line in lines:
        # Check if line already has a date
        if date_pattern.search(line):
            output.append(line)
            continue
        
        match = link_pattern.search(line)
        if match:
            owner, repo = match.group(1), clean_repo_name(match.group(2))
            print(f"Fetching: {owner}/{repo}", file=sys.stderr)
            date = get_repo_created_date(owner, repo, session=session, timeout=timeout, max_retries=max_retries)
            if date:
                # Append date at the end of the line
                line = line.rstrip() + f" {date}"
        
        output.append(line)
    
    return "\n".join(output)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Append GitHub repo creation dates to markdown lines.")
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
    result = process_text(text, session=session, timeout=args.timeout, max_retries=args.max_retries)

    if args.in_place:
        if not args.input or args.input == "-":
            parser.error("--in-place requires --input with a file path.")
        Path(args.input).write_text(result, encoding="utf-8")
    else:
        write_text_output(result, args.output)


if __name__ == "__main__":
    main()
