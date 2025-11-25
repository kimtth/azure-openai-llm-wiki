import re
from pathlib import Path

DATE_PATTERN = re.compile(r"(\[[0-9]{1,2}\s\w+\s[0-9]{4}\]|\[\w+\s[0-9]{4}\]|\([0-9]{1,2}\s\w+\s[0-9]{4}\)|\(\w+\s[0-9]{4}\))")
LINK_PATTERN = re.compile(r"\[([^\]]+)\]\((https?[^)]+)\)")

root = Path(__file__).resolve().parent.parent
old_path = root / "snapshot" / "azure_old.md"
new_path = root / "section" / "azure.md"

old_text = old_path.read_text(encoding="utf-8")
new_text = new_path.read_text(encoding="utf-8")

mapping = {}
for line in old_text.splitlines():
    m = DATE_PATTERN.search(line)
    if not m:
        continue
    date_token = m.group(0)
    # Normalize stored date tokens to parentheses format.
    if date_token.startswith("[") and date_token.endswith("]"):
        date_token = "(" + date_token[1:-1].strip() + ")"
    for _title, url in LINK_PATTERN.findall(line):
        mapping[url] = date_token

lines = new_text.splitlines()
changed = 0
for i, line in enumerate(lines):
    # Convert bracket date tokens to parentheses in target file.
    norm = re.sub(r"\[(\d{1,2}\s\w+\s\d{4}|\w+\s\d{4})\]", r"(\1)", line)
    if norm != line:
        lines[i] = norm
        line = norm
    # Skip adding if a date already exists after normalization.
    if DATE_PATTERN.search(line):
        continue
    urls = [u for _t, u in LINK_PATTERN.findall(line)]
    for url in urls:
        if url in mapping:
            lines[i] = f"{line} {mapping[url]}".rstrip()
            changed += 1
            break

if changed:
    new_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Updated {changed} lines with dates.")
else:
    print("No date updates applied.")
