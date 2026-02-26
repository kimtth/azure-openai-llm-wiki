---
name: update-cite-count
description: "Guidelines for updating citation counts for papers in the section files using the `update_citation_counts.py` tool. USE FOR: Updating citation counts for papers listed in the section files to keep information current. DO NOT USE FOR: 1) Adding new papers to the section files; 2) Classifying entries into sections."
---

## Workflow: Updating Citation Counts for Papers

To keep the citation counts for papers in the section files up to date, follow these guidelines when using the `update_citation_counts.py` tool.

1. The ouput count will be used for updating the citation counts for papers in the section files. the section file is for `best_practices.md` and the sections are `RAG Research (Ranked by cite count >=100)` and `Agent Research (Ranked by cite count >=100)`.
2. Run the `fetch_popular_papers.py` script first to ensure that the section files are populated with the latest papers and their current citation counts. This will provide a baseline for the `update_citation_counts.py` script to work with.
3. Run the `update_citation_counts.py` script to fetch the latest citation counts from Semantic Scholar for the papers listed in the specified sections of `best_practices.md`.
4. The script will automatically update the citation counts in the section files based on the latest data retrieved. Ensure that the updated counts are accurate and reflect the current citation status of each paper.
5. After updating, review the section files to confirm that the citation counts have been correctly updated and that the papers are still ranked appropriately based on their citation counts. If any discrepancies are found, manually verify the counts and make necessary adjustments.