---
name: add-temp-entries-to-sections
description: "Classification guidelines for entries in temp_entries.md. Each entry has a title containing the markdown file name and section name. USE FOR: Classifying new entries in temp_entries.md into *.md section files. DO NOT USE FOR: Adding entries to temp_entries.md or moving entries between sections."
---

## Workflow: Classifying Entries in temp_entries.md

`temp_entries.md` is the staging file where new entries from `temp.md` are formatted before being inserted into the section files. Each entry in `temp_entries.md` should have a title indicating the target markdown file and section name for clarity.

**Steps for classification:**

1. **Identify the target section** — Based on the title of each entry, determine which markdown file under `section/` it belongs to and use the exact current heading from that file's `Contents` block or heading text.
2. **Insert into sections** — Once classified, entries should be moved from `temp_entries.md` to the appropriate section files (`azure.md`, `applications.md`, `models_research.md`, `best_practices.md`, `tools_extra.md`) under the correct live section headings.
3. **Maintain organization** — Ensure entries are placed in the correct order within each section, following the existing formatting and structure. Entries are ordered alphabetically by name within each section.
4. **Update temp_entries.md** — After classification and insertion, add Check emoji ✅ to the entry in `temp_entries.md` to keep it clean and track which entries have been processed.

Do not classify hand-curated entries into generated index files such as `section/x_llm_apps.md`, `section/x_llm_papers.md`, or `section/x_popular_papers.md`. Use the generator-specific skills for those files.
