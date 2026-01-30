
from __future__ import annotations

# merge the md files under section for one README.md file
# the order of the files is the order of the sections in the README.md

import argparse
import os
import re
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

def replace_section_links(content, section_files):
    # 1. Update the regex to include an optional slash before the anchor
    # for example, # (section/intro.md#getting-started) -> # (intro.md#installation)
    pattern = re.compile(
        r'\(section/(' + '|'.join([f.replace('.md', '') for f in section_files]) + r')\.md/?#([^)]+)\)'
    )
    content = pattern.sub(r'(#\2)', content)
    # 2. Add a replacement pattern such as [x-ref](sk_dspy.md/#code-recipes) -> [x-ref](#code-recipes)
    # Check whether text contains [x-ref].
    # If it does, replace the link.
    if content.find("[🔗]") != -1:
        for x in section_files:
            content = content.replace(f'{x}/', '')
    # 3. Replace "../files" with "./files"
    content = content.replace("../files", "./files")
    return content


def strip_agent_tools_comment(content: str) -> str:
    pattern = re.compile(r"<!--\s*AGENT_TOOLS_START[\s\S]*?AGENT_TOOLS_END\s*-->", re.MULTILINE)
    return pattern.sub("", content)

def merge_markdowns(section_dir, existing_readme, output_file, *, keep_agent_comment: bool = False):
    section_files = [
        "applications.md",
        "azure.md",
        "models_research.md",
        "tools_extra.md",
        "best_practices.md"
    ]
    with open(output_file, "w", encoding="utf-8") as outfile:
        if os.path.exists(existing_readme):
            with open(existing_readme, "r", encoding="utf-8") as r:
                existing_content = r.read()
                existing_content = replace_section_links(existing_content, section_files)
                if not keep_agent_comment:
                    existing_content = strip_agent_tools_comment(existing_content)
                outfile.write(existing_content)
                outfile.write("\n\n")

        for f in section_files:
            path = os.path.join(section_dir, f)
            if os.path.exists(path):
                with open(path, "r", encoding="utf-8") as infile:
                    content = infile.read()
                    content = replace_section_links(content, section_files)
                    outfile.write(content)
                    outfile.write("\n\n")

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Merge README with section markdown files.")
    parser.add_argument("--section-dir", default="section", help="Directory containing section markdown files.")
    parser.add_argument("--readme", default="README.md", help="Base README file.")
    parser.add_argument("--output", default="README_all_in_one.md", help="Output merged markdown file.")
    parser.add_argument("--keep-agent-comment", action="store_true", help="Keep agent tool comment block.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    merge_markdowns(args.section_dir, args.readme, args.output, keep_agent_comment=args.keep_agent_comment)


if __name__ == "__main__":
    main()