---
name: add-new-entry
description: "Workflow and tools for adding new entries from temp.md to the section files. Includes legend format, section reference, code tools, and common pitfalls. USE FOR: Adding new resources to the knowledge base. DO NOT USE FOR: Editing existing entries or restructuring sections."
---


## Workflow: Adding New Entries from temp.md

`temp.md` is the raw input — an unformatted checklist of URLs and short notes. The goal is to produce `temp_entries.md` as a properly formatted staging file ready to paste into the target section files.

**Steps in order:**

1. **Classify each URL** → determine which section file (`azure.md`, `applications.md`, `models_research.md`, `best_practices.md`) and which section heading it belongs to.
2. **Fetch descriptions** — use `code/fetch_github_description.py` for GitHub repos. For arXiv papers and blog/web links, use `fetch_webpage` to extract a one-sentence description.
3. **Fetch creation dates** — use `code/get_github_dates.py` for GitHub repos. For arXiv, derive the date from the ID prefix (e.g., `2602.xxxxx` → Feb 2026). For blog posts, read from the page.
4. **Add star badges** — use `code/add_github_stars.py` for all GitHub links.
5. **Apply legend symbols** — see the **Legend Format** section below. The format differs between `azure.md` and all other files.
6. **Shorten descriptions** — keep each description to ≤15 words. One punchy sentence. Do not repeat the link name.

---

## Legend Format

### `azure.md` — dash-bullet, symbol before description

```
- [OPTIONAL_PREFIX][Name](url) - SYMBOL_Description. (Mon YYYY) ![stars](...)
```

- The legend symbol (✨, ✍️, etc.) is placed **before the description**, separated by a space from the dash.
- Optional prefix emoji (🏛️ for Microsoft OSS, 🏬 for Azure-Samples) goes **before the link text**, outside the brackets.
- Date is in `(Mon YYYY)` parentheses format with no brackets.
- Star badge goes at the end of the line, after the date.

**Examples:**

```markdown
- [Azure ML Prompt Flow](https://learn.microsoft.com/...) - ✍️Visual designer for prompt orchestration and evaluation. (Jun 2023)
- 🏬[APIM-Sample](https://github.com/Azure-Samples/APIM-Sample) - ✨Single APIM endpoint for multiple models. (Jan 2026) ![**github stars**](...)
```

### `applications.md`, `models_research.md`, `best_practices.md` — numbered list (or dash), symbol appended to link text

```
1. [Name✨](url): Description. [Mon YYYY] ![stars](...)
```
or (for entries that use dash bullets in that section):
```
- [Name✍️](url): Description. [Mon YYYY]
```

- The legend symbol is appended **inside the link text**, immediately after the name (no space before the symbol).
- Date is in `[Mon YYYY]` square-bracket format.
- Star badge goes at the end of the line, after the date.
- Use numbered list (`1.`) when the surrounding section uses numbered lists; dash (`-`) when not.

**Examples:**

```markdown
1. [Auto-Claude✨](https://github.com/AndyMik90/Auto-Claude): Autonomous multi-session AI coding. [Dec 2025] ![**github stars**](...)
1. [Towards AI Search Paradigm📑](https://arxiv.org/abs/2506.17188): Modular 4-agent system using DAGs for retrieval-intensive search. [Jun 2025]
- [Claude Code Security✍️](https://www.anthropic.com/news/claude-code-security): Claude Code on the web for scanning codebases. [Feb 2026]
```

### Legend Symbols

| Symbol | Meaning |
|--------|---------|
| ✨ | GitHub repository (OSS) |
| ✍️ | Blog post / documentation / web page |
| 📑 | Academic paper (arXiv) |
| 📺 | Video content |
| 🤗 | Hugging Face resource |
| 🏛️ | Microsoft official OSS (azure.md prefix only) |
| 🏬 | Azure-Samples org (azure.md prefix only) |

---

## Section Reference

Use **exact** heading names when labeling entries in `temp_entries.md`. Format: `## <filename> - <Section Name>:`.

### `azure.md`
- Developer Tooling
- Agent Frameworks
- Agent Development
- Microsoft Copilot Products
- Azure OpenAI Samples
- Azure OpenAI Application
- Azure OpenAI Accelerator & Samples
- LLM Frameworks
- Prompt Tooling
- Microsoft Copilot Products
- Copilot Development
- Azure AI Search / Azure AI Services
- Microsoft Research
- Risk & LLMOps

### `applications.md`
- AI Application → `### **AI Application**` (contains `#### Agent & Application`, `#### Skill`, `#### Coding`, `#### Deep Research`, `#### Memory`, `#### Gateway`, `#### Caching`, `#### Data Processing`)
- Agent Protocol → `### **Agent Protocol**` (contains `#### Model Context Protocol (MCP)`, `#### A2A`, `#### Computer use`)
- Vector Database & Embedding → `### **Vector Database & Embedding**`
- RAG (Retrieval-Augmented Generation) → `## **RAG ...`

> **Tip:** The sub-sections under `AI Application` (Agent & Application, Skill, Coding, Deep Research) are `####` headings. Use the exact name, e.g., `applications.md - Skill`, `applications.md - Coding`, `applications.md - Agent & Application`, `applications.md - Deep Research`, `applications.md - Model Context Protocol (MCP)`.

### `models_research.md`
- OpenAI Products → `### **OpenAI Products**`
- Anthropic AI Products → `### **Anthropic AI Products**`
- Google AI Products → `### **Google AI Products**`
- AGI Discussion and Social Impact (no explicit heading — look for related entries near end of file)
- Large Language Model Collection
- Reasoning

### `best_practices.md`
- Agent Research → `### **Agent Research**`
- RAG Research → `### **RAG Research**`
- Agent Design Patterns → `### **Agent Design Patterns**`
- Reflection, Tool Use, Planning and Multi-agent collaboration

---

## Code Tools Reference

All tools are in `code/`. Run with `python code/<script>.py`.

| Script | Purpose |
|--------|---------|
| `fetch_github_description.py` | Fetch GitHub repo descriptions; appends after the link colon. Skips lines that already have a description. |
| `get_github_dates.py` | Fetch GitHub repo creation date; appends `[Mon YYYY]` or `(Mon YYYY)`. Skips lines already dated. |
| `add_github_stars.py` | Append star badge to lines with GitHub links. Skips duplicates. |
| `fetch_popular_papers.py` | Query Semantic Scholar for top-cited papers; writes `section/x_popular_papers.md`. |
| `update_citation_counts.py` | Update citation counts for ranked paper sections via Semantic Scholar. |
| `check_unused_files.py` | Scan markdown for file refs; move unreferenced files to `files/_bak/`. |

**For arXiv papers and blog posts, `fetch_github_description.py` does not apply.** Use `fetch_webpage` (agent tool) to retrieve a description from the URL.

**Common CLI pattern:**
```powershell
python code/fetch_github_description.py --input temp.md --output temp_with_desc.md
python code/get_github_dates.py --input temp_with_desc.md --in-place
python code/add_github_stars.py --input temp_with_desc.md --in-place
```

---

## Common Pitfalls (Lessons Learned)

1. **Wrong legend placement:** In `azure.md` the symbol (✨, ✍️) precedes the description text after ` - `. In all other files the symbol is appended to the link name inside `[Name✨]`. Never mix these two formats.

2. **Wrong section names:** Section labels in `temp_entries.md` must match the actual heading text in the target file exactly. Check the file before assigning. Do not invent new section names.

3. **Missing descriptions for non-GitHub links:** `fetch_github_description.py` only works for `github.com` URLs. For arXiv, blog, and product pages, you must fetch the page and write a description manually.

4. **Verbose descriptions:** Keep descriptions to ≤15 words. Do not repeat the name. No trailing "for use with", "that helps you", or similar filler.

5. **Date format mismatch:** `azure.md` uses `(Mon YYYY)` parentheses. All other section files use `[Mon YYYY]` square brackets.

6. **emoji stripping via heredoc:** Writing file content via PowerShell heredoc strips emoji characters. Use `replace_string_in_file` or `multi_replace_string_in_file` to patch emoji symbols back in if they are lost.

7. **Star badges on non-GitHub links:** Only add star badges to `github.com` links. Blog posts, arXiv papers, and product pages must not have a star badge.
