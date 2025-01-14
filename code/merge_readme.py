
# merge the md files under section for one README.md file
# the order of the files is the order of the sections in the README.md

import os
import re

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
    if content.find("[x-ref]") != -1:
        for x in section_files:
            content = content.replace(f'{x}/', '')
    # 3. Replace "../files" with "./files"
    content = content.replace("../files", "./files")
    return content

def merge_markdowns(section_dir, existing_readme, output_file):
    section_files = [
        "rag.md",
        "aoai.md",
        "app.md",
        "agent.md",
        "sk_dspy.md",
        "langchain.md",
        "prompt.md",
        "ft.md",
        "chab.md",
        "llm.md",
        "survey_ref.md",
        "ai_tool.md",
        "dataset.md",
        "eval.md"
    ]
    with open(output_file, "w", encoding="utf-8") as outfile:
        if os.path.exists(existing_readme):
            with open(existing_readme, "r", encoding="utf-8") as r:
                existing_content = r.read()
                existing_content = replace_section_links(existing_content, section_files)
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

if __name__ == "__main__":
    merge_markdowns("section", "README.md", "README_all_in_one.md")