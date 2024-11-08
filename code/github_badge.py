import os
import re

# Function to add a GitHub repo badge link if not already added
def add_github_badge(line, added_badges):
    # Search for GitHub repo URLs in markdown format [text](https://github.com/user/repo)
    matches = re.findall(r"\[([^\]]+)\]\((https://github\.com/([a-zA-Z0-9_\-\.]+)/([a-zA-Z0-9_\-\.]+))\)", line)
    
    for match in matches:
        label, url, user, repo = match
        unique_key = f"{user}/{repo}"
        
        # Add badge if it hasn't been added for this repo
        if unique_key not in added_badges:
            badge = f"![GitHub Repo stars](https://img.shields.io/github/stars/{user}/{repo}?style=flat-square&label=%20&color=gray)"
            line += f" {badge}"
            added_badges.add(unique_key)  # Track added badges to avoid duplicates
    
    return line

# Function to process files in the specified directory
def process_markdown_files(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    for filename in os.listdir(input_dir):
        if filename.endswith(".md"):
            print(f"Processing file: {filename}")  # Debugging log
            process_file(input_dir, output_dir, filename)

# Function to process a single markdown file, adding badges
def process_file(input_dir, output_dir, filename):
    input_path = os.path.join(input_dir, filename)
    output_path = os.path.join(output_dir, filename)
    added_badges = set()  # Track added badges for this file

    with open(input_path, "r", encoding="utf-8") as infile, open(output_path, "w", encoding="utf-8") as outfile:
        for line in infile:
            updated_line = add_github_badge(line, added_badges)
            outfile.write(updated_line + "\n")

if __name__ == "__main__":
    input_directory = "section"  # Input directory path
    output_directory = "out"     # Output directory path

    process_markdown_files(input_directory, output_directory)
