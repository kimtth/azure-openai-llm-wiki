---
name: update-cite-count
description: "Guidelines for updating citation counts for papers in the section files using the `update_citation_counts.py` tool. USE FOR: Updating citation counts for papers listed in the section files to keep information current. DO NOT USE FOR: 1) Adding new papers to the section files; 2) Classifying entries into sections."
---

## Workflow: Updating Citation Counts for Papers

To keep the citation counts for papers in the section files up to date, follow these guidelines when using the `update_citation_counts.py` tool.

1. The output count is used for the inline ranked sections in `section/best_practices.md`: `RAG Research (Ranked by cite count >=100)` and `Agent Research (Ranked by cite count >=100)`.
2. Run `update_citation_counts.py` directly to fetch the latest Semantic Scholar citation counts for papers already listed in those two sections.
3. The script updates citation counts in place when counts changed. It does not add new papers, rebuild section indexes, or update generated pool files.
4. After updating, review `section/best_practices.md` to confirm the counts changed correctly and the ranked order is still accurate. If counts change enough to affect ordering, manually reorder the entries.
