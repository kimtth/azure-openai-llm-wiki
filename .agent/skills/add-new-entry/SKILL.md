---
name: add-new-entry
description: "Workflow and tools for adding new entries from temp.md to the section files. Includes legend format, section reference, code tools, and common pitfalls. USE FOR: Adding new resources to the knowledge base. DO NOT USE FOR: Editing existing entries or restructuring sections."
---


## Workflow: Adding New Entries from temp.md

`temp.md` is the raw input — an unformatted checklist of URLs and short notes. The goal is to produce `temp_entries.md` as a properly formatted staging file ready to paste into the target section files.

**Steps in order:**

1. **Classify each URL** → determine which section file (`azure.md`, `applications.md`, `models_research.md`, `best_practices.md`, `tools_extra.md`) and which current section heading it belongs to.
2. **Fetch descriptions** — use `code/fetch_github_description.py` for GitHub repos. For arXiv papers and blog/web links, use `fetch_webpage` to extract a one-sentence description.
3. **Fetch creation dates** — use `code/get_github_dates.py` for GitHub repos. For arXiv, derive the date from the ID prefix (e.g., `2602.xxxxx` → Feb 2026). For blog posts, read from the page.
4. **Add star badges** — use `code/add_github_stars.py` for all GitHub links.
5. **Apply legend symbols** — see the **Legend Format** section below. `azure.md` should not use emoji markers.
6. **Shorten descriptions** — keep each description to ≤15 words. One punchy sentence. Do not repeat the link name.

---

## Legend Format

### `azure.md` — dash-bullet, no emojis

```
- [Name](url) - Description. (Mon YYYY) ![stars](...)
```

- Do not use emoji markers in `azure.md` (no link-prefix emojis and no description-prefix emojis).
- Date is in `(Mon YYYY)` parentheses format with no brackets.
- Star badge goes at the end of the line, after the date.

**Examples:**

```markdown
- [Azure ML Prompt Flow](https://learn.microsoft.com/...) - Visual designer for prompt orchestration and evaluation. (Jun 2023)
- [APIM-Sample](https://github.com/Azure-Samples/APIM-Sample) - Single APIM endpoint for multiple models. (Jan 2026) ![**github stars**](...)
```

### `applications.md`, `models_research.md`, `best_practices.md` — numbered list (or dash), symbol appended to link text

```
1. [Name](url): Description. [Mon YYYY] ![stars](...)
```
or (for entries that use dash bullets in that section):
```
- [Name](url): Description. [Mon YYYY]
```

- The legend symbol is appended **inside the link text**, immediately after the name (no space before the symbol).
- Date is in `[Mon YYYY]` square-bracket format.
- Star badge goes at the end of the line, after the date.
- Use numbered list (`1.`) when the surrounding section uses numbered lists; dash (`-`) when not.

**Examples:**

```markdown
1. [Auto-Claude](https://github.com/AndyMik90/Auto-Claude): Autonomous multi-session AI coding. [Dec 2025] ![**github stars**](...)
1. [Towards AI Search Paradigm📑](https://arxiv.org/abs/2506.17188): Modular 4-agent system using DAGs for retrieval-intensive search. [Jun 2025]
- [Claude Code Security](https://www.anthropic.com/news/claude-code-security): Claude Code on the web for scanning codebases. [Feb 2026]
```

### Legend Symbols

| Symbol | Meaning |
|--------|---------|
|  | Blog post / documentation / web page |
| 📑 | Academic paper (arXiv) |
| 📺 | Video content |
| 🤗 | Hugging Face resource |

---

## Section Reference

Use **exact** heading names when labeling entries in `temp_entries.md`. Format: `## <filename> - <Section Name>:`.

### `azure.md`
- Azure OpenAI & Foundry Overview
- Orchestration Frameworks
- Prompt Engineering & Tooling
- Agent Frameworks
- Model Training & Inference
- Safety, Security & LLMOps
- Data Processing & Memory
- Dev Tools, MCP & Extensions
- Copilot Product Catalog
- Microsoft Foundry & AI Services
- Azure AI Search
- Agent Development
- Microsoft 365 Agent Development
- Learning Resources & Workshops
- Microsoft Research
- Sample Applications
- Solution Accelerators
- Code Samples & Workshops
- Architecture Patterns & Use Cases

### `applications.md`
- RAG (Retrieval-Augmented Generation)
- GraphRAG
- RAG Application
- Vector Database & Embedding
- Top Agent Frameworks
- Additional Agent Framework
- Cache
- Data & Analytics Agents
- Data Processing & OCR
- Desktop AI assistant
- Memory
- Model Gateway
- Model Serving & Local Runtimes
- Observability & LLMOps
- SDKs, Integration & ML Libraries
- Training & Fine-tuning
- UI & No-Code Tool
- A2A
- Computer use
- Model Context Protocol (MCP)
- Coding
- Deep Research
- Domain-Specific Agents
- Skill
- Harness

> **Tip:** Do not add hand-curated entries to generated index sections such as `Popular LLM Applications (GitHub Stars >= 1000)`; update the generator skill instead.

### `models_research.md`
- Large Language Model Landscape
- Large Language Model Comparison
- Taxonomy of Natural Language Processing
- LLM Evolution and Model Timelines
- NLP Taxonomy and Research Fields
- Large Language Model Collection
- Architecture Comparisons
- Foundation Model Providers
- Domain-Specific and Specialized LLMs
- Multimodal Models
- Prompt Engineering and Visual Prompts
- Prompt Engineering
- Adversarial Prompting
- Prompt Tuner and Optimizer
- Prompt Guides and Prompt Libraries
- Visual Prompting and Visual Grounding
- Large Language Model Training and Optimization
- Pre-training and Data Preparation
- Architecture and Inference Patterns
- Architecture Variants, Attention, and Sparse Computation
- Context and Long-Context Limits
- Tokenization and LLM Numbers
- Capabilities and Evaluation
- Reasoning
- Post-training and Fine-Tuning
- Model Merging and Continual Adaptation
- Parameter-Efficient Fine-Tuning
- LoRA: Low-Rank Adaptation
- Alignment and Preference Optimization
- Quantization Techniques
- Pruning and Sparsification
- Knowledge Distillation
- Memory Optimization
- AI Adoption, Impact, and Society
- AGI, Society, and Long-Term Impact
- Trust, Safety, and Security
- Business Adoption and Use Cases
- Model Roadmaps and Products
- OpenAI Products
- Anthropic AI Products
- Google AI Products
- Survey on Large Language Models
- Additional Topics: A Survey of LLMs
- LLM Research (Ranked by cite count >=150)
- Learning Resources, Implementations, and Regional Materials
- Build LLMs from Scratch
- Japanese and Korean-Language Materials
- General Learning and Supplementary Materials

### `best_practices.md`
- The Problem with RAG
- RAG Solution Design
- Agent Research → `### **Agent Research**`
- RAG Research → `### **RAG Research**`
- Agent Design Patterns → `### **Agent Design Patterns**`
- Tool Use
- Tool Use: LLM to Master APIs
- Proposals & Glossary

### `tools_extra.md`
- LLM for Robotics
- Awesome demo
- Datasets for LLM Training
- Evaluating Large Language Models
- LLM Evalution Benchmarks
- Evaluation Metrics
- LLMOps: Large Language Model Operations

---

## Code Tools Reference

All tools are in `code/`. Run with `python code/<script>.py`.

| Script | Purpose |
|--------|---------|
| `fetch_github_description.py` | Fetch GitHub repo descriptions; appends after the link colon. Skips lines that already have a description. |
| `get_github_dates.py` | Fetch GitHub repo creation date; appends `[Mon YYYY]` or `(Mon YYYY)`. Skips lines already dated. |
| `add_github_stars.py` | Append star badge to lines with GitHub links. Skips duplicates. |
| `fetch_popular_papers.py` | Query Semantic Scholar for review-only RAG/agent paper candidates; not part of normal entry insertion. |
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

1. **Wrong legend placement:** In `azure.md`, do not use emoji markers at all. In all other files, the symbol is appended to the link name inside `[Name]`. Never mix these two formats.

2. **Wrong section names:** Section labels in `temp_entries.md` must match the actual heading text in the target file exactly. Check the file before assigning. Do not invent new section names.

3. **Missing descriptions for non-GitHub links:** `fetch_github_description.py` only works for `github.com` URLs. For arXiv, blog, and product pages, you must fetch the page and write a description manually.

4. **Verbose descriptions:** Keep descriptions to ≤15 words. Do not repeat the name. No trailing "for use with", "that helps you", or similar filler.

5. **Date format mismatch:** `azure.md` uses `(Mon YYYY)` parentheses. All other section files use `[Mon YYYY]` square brackets.

6. **emoji stripping via heredoc:** Writing file content via PowerShell heredoc strips emoji characters. Use `replace_string_in_file` or `multi_replace_string_in_file` to patch emoji symbols back in if they are lost.

7. **Star badges on non-GitHub links:** Only add star badges to `github.com` links. Blog posts, arXiv papers, and product pages must not have a star badge.
