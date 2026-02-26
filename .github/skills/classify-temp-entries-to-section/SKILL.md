---
name: classify-temp-entries-to-section
description: "Classification guidelines for entries in temp_entries.md. Each entry have its own title with the markdown file name and section name in temp_entries.md. USE FOR: Classifying new entries in temp_entries.md into *.md in the section files. DO NOT USE FOR: 1) Adding new entries to temp_entries.md; 2) Moving entries between sections."
---

## Workflow: Classifying Entries in temp_entries.md

`temp_entries.md` is the staging file where new entries from `temp.md` are formatted before being inserted into the section files. Each entry in `temp_entries.md` should have a title indicating the target markdown file and section name for clarity.

**Steps for classification:**

1. **Identify the target section** — Based on the title of each entry determine which section file it belongs to mark down files under `section/` and the specific section heading within that file.
2. **Insert into sections** — Once classified, entries should be moved from `temp_entries.md` to the appropriate section files (`azure.md`, `applications.md`, `models_research.md`, `best_practices.md`, `tools_extra.md`) under the correct section headings.
3. **Maintain organization** — Ensure that entries are placed in the correct order within each section, following any existing formatting and structure. The entry are ordered by alphabetical order of the entry name under each section.
4. **Update temp_entries.md** — After classification and insertion, add Check emoji ✅ to the entry in `temp_entries.md` to keep it clean and track which entries have been processed.
