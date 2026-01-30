from __future__ import annotations

import argparse
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from utils.io_utils import read_text_input, write_text_output
from utils.markdown_utils import (
    GITHUB_BADGE_PATTERN,
    GITHUB_REPO_URL_PATTERN,
    clean_repo_name,
)

# Process text and add GitHub star badge lines after repository links
BADGE_TEMPLATE = "![**github stars**](https://img.shields.io/github/stars/{owner}/{repo}?style=flat-square&label=%20&color=blue&cacheSeconds=36000)"


def add_github_stars(text: str) -> tuple[str, int]:
    """
    Add GitHub star badges after lines containing GitHub repository links.
    Returns the modified text and count of added badges.
    """
    lines = text.strip().split("\n")

    # Collect existing badges to avoid duplicates
    existing = set()
    for line in lines:
        for m in GITHUB_BADGE_PATTERN.finditer(line):
            existing.add((m.group(1), m.group(2)))

    added = 0
    output = []
    seen_repo_for_badge = set(existing)

    for line in lines:
        matches = list(GITHUB_REPO_URL_PATTERN.finditer(line))
        if not matches:
            output.append(line)
            continue

        # Extract candidate repos
        to_add = []
        for m in matches:
            owner, repo = m.group(1), clean_repo_name(m.group(2))
            key = (owner, repo)

            if key in seen_repo_for_badge or not repo:
                continue

            to_add.append(key)

        # Append badges to the same line
        modified_line = line
        for owner, repo in to_add:
            badge = " " + BADGE_TEMPLATE.format(owner=owner, repo=repo)
            modified_line += badge
            seen_repo_for_badge.add((owner, repo))
            added += 1

        output.append(modified_line)

    return "\n".join(output), added


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Append GitHub star badges to markdown lines.")
    parser.add_argument("--input", help="Input markdown file path (or '-' for stdin).")
    parser.add_argument("--output", help="Output file path (or '-' for stdout).")
    parser.add_argument("--in-place", action="store_true", help="Overwrite the input file.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    text = read_text_input(args.input)

    result, count = add_github_stars(text)

    if args.in_place:
        if not args.input or args.input == "-":
            parser.error("--in-place requires --input with a file path.")
        Path(args.input).write_text(result, encoding="utf-8")
    else:
        write_text_output(result, args.output)

    print(f"Added {count} GitHub star badge lines.", file=sys.stderr)


if __name__ == "__main__":
    main()