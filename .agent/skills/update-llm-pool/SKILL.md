---
name: update-llm-pool
description: "Workflow for updating the LLM landscape paper pool (section/x_llm_papers.md) using fetch_llm_papers.py. Covers full re-fetch, resume from checkpoint, and adding new topics. USE FOR: Refreshing citation counts, expanding topic coverage. DO NOT USE FOR: Adding hand-curated entries to section files (use add-new-entry), updating RAG/Agent citation sections in best_practices.md (use update-cite-count)."
---

## Overview

The pool file `section/x_llm_papers.md` is a flat list of high-citation CS papers covering the LLM landscape, fetched from the Semantic Scholar API and ranked by citation count. It is generated and maintained by `code/fetch_llm_papers.py`.

The section `### **LLM Research (Ranked by cite count >=100)**` in `section/models_research.md` links to this file with a single descriptive line.

---

## Script Reference

**Script:** `code/fetch_llm_papers.py`  
**Python env:** `.venv\Scripts\python.exe`

### Key CLI Arguments

| Argument | Default | Purpose |
|----------|---------|---------|
| `--output` | `section/x_llm_papers.md` | Output markdown file for the paper pool |
| `--min-citations` | `150` | Minimum citation count filter |
| `--top-n` | `50` | Max papers returned per topic query |
| `--reset` | *(flag)* | Delete existing checkpoint and start from scratch |
| `--topics` | *(all)* | Limit run to matching topic names (substring, case-insensitive) |

---

## Workflow

### 1. Full re-fetch (refresh everything)

Use when topics have been added/modified or citation counts are stale.

```powershell
.venv\Scripts\python.exe code/fetch_llm_papers.py `
    --reset `
    --min-citations 150 `
    --top-n 50
```

- `--reset` deletes any existing checkpoint so all 35 topics are re-queried.
- On success the checkpoint is automatically deleted.
- `section/x_llm_papers.md` is rewritten with sequential numbering sorted by citation count.

### 2. Resume after API interruption

The script saves a checkpoint (`section/x_llm_papers.checkpoint.json`) after each topic completes. If the run is interrupted by a rate-limit (HTTP 429), simply re-run **without** `--reset`:

```powershell
.venv\Scripts\python.exe code/fetch_llm_papers.py `
    --min-citations 150 `
    --top-n 50
```

The script prints `[resume] Loaded N papers, M completed topics from checkpoint.` and skips already-finished topics.

### 3. Refresh only specific topics

```powershell
.venv\Scripts\python.exe code/fetch_llm_papers.py `
    --topics "PEFT" "Reasoning" `
    --min-citations 150 `
    --top-n 50
```

Matches topic names by substring (case-insensitive). New papers for matched topics are merged into the existing pool if a checkpoint exists; otherwise starts fresh for those topics only.

---

## Adding or Modifying Topics

Topics are defined in the `TOPICS` dict at the top of `fetch_llm_papers.py`. Each key is a topic label; the value is a list of Semantic Scholar search query strings.

**Rules:**
- Queries should be descriptive phrases, not single keywords — Semantic Scholar full-text search works best with 4–8 word phrases.
- Avoid the word "survey" to capture research papers, benchmarks, and position papers, not just surveys.
- Aim for 3–10 queries per topic. Overlapping queries are fine — deduplication is handled automatically by `paperId`.
- After adding topics, run with `--reset` to re-fetch from scratch (checkpoint is stale once `TOPICS` changes).

**Current topic areas (35 total):**

| Category | Topics |
|----------|--------|
| Core LLM | Reasoning in LLMs, LLM Overview & History, Scaling Laws, LLM Architecture Innovations |
| Training | Alignment & RLHF, RLAIF & Constitutional AI, RLVR & Process Reward Models, Instruction Tuning & SFT, PEFT & LoRA, Self-Supervised & Representation Learning |
| Inference | Efficient LLMs: Training & Inference, Inference-Time Scaling & Test-Time Compute, LLMOps & Model Serving |
| Applications | LLM Agents, Retrieval-Augmented Generation (RAG), GraphRAG & Knowledge Graphs, LLMs for Code, LLMs for Healthcare & Science, LLM for Robotics & Embodied AI, Function Calling & Tool Use, GUI Agents, Tabular Data & NL2SQL |
| Multimodal | Multimodal LLMs, Small Language Models, Mixture of Experts |
| Evaluation | Evaluation of LLMs & Agents, Hallucination in LLMs, Trustworthy & Secure LLMs |
| Other | Prompt Engineering & In-Context Learning, Context Engineering, Embeddings & Vector Search, Data for LLMs, AIOps & Observability, Federated & Personalized AI, Continual Learning & Model Merging |

---

## Output Format

Each entry in `section/x_llm_papers.md`:

```
N. [Title📑](https://arxiv.org/abs/XXXX.XXXXX): First sentence of abstract. [Mon YYYY] (Citations: N,NNN)
```

- Numbered sequentially (`1.`, `2.`, ...) by citation count descending.
- Link target is the arXiv URL if available, otherwise the Semantic Scholar URL.
- Date is derived from the arXiv ID prefix (e.g. `2305.xxxxx` → `[May 2023]`).
- Only Computer Science papers with `fieldsOfStudy` containing `"Computer Science"` are included.

---

## Checkpoint File

`section/x_llm_papers.checkpoint.json` — JSON with two keys:

```json
{
  "completed_topics": ["Reasoning in LLMs", "LLM Agents", ...],
  "papers": [ { "paperId": "...", "title": "...", "citationCount": 123, ... } ]
}
```

- Created/updated after every topic completes.
- Deleted automatically on successful full run.
- If corrupted, delete manually and re-run with `--reset`.
- To inspect: `python -c "import json; cp=json.load(open('section/x_llm_papers.checkpoint.json', encoding='utf-8')); print(len(cp['papers']), 'papers,', len(cp['completed_topics']), 'topics done')"`

---

## Common Pitfalls

1. **Modified TOPICS but not using `--reset`:** The checkpoint from a previous run skips topics that already completed. After editing `TOPICS`, always use `--reset` to re-fetch all topics.

2. **API rate limits (HTTP 429):** Semantic Scholar enforces per-IP rate limits. The script adds a 1-second polite delay between queries and retries with backoff. If repeatedly rate-limited, wait a few minutes and resume (no `--reset`). Increase `--backoff` (e.g. `--backoff 2.0`) to slow down between retries.

3. **Non-CS papers in results:** The filter requires `"Computer Science"` in `fieldsOfStudy`. Some highly cited ML papers may not be tagged as CS by Semantic Scholar and will be excluded. This is intentional.
