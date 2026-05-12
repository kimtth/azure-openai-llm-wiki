---
name: update-llm-pool
description: "Workflow for updating the LLM landscape paper pool (section/x_llm_papers.md) using fetch_llm_papers.py. Covers full re-fetch, resume from checkpoint, and adding new topics. USE FOR: Refreshing citation counts, expanding topic coverage. DO NOT USE FOR: Adding hand-curated entries to section files (use add-new-entry), updating RAG/Agent citation sections in best_practices.md (use update-cite-count)."
---

## Overview

The pool file `section/x_llm_papers.md` is a compact list of high-citation CS papers covering the LLM landscape, fetched from the Semantic Scholar API and ranked by citation count. It includes a topic coverage summary and per-paper topic tags. It is generated and maintained by `code/fetch_llm_papers.py`.

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
| `--request-delay` | `2.0` | Delay between Semantic Scholar requests |
| `--jitter` | `0.5` | Random extra delay between requests |
| `--api-key-env` | `S2_API_KEY` | Env var containing a Semantic Scholar API key |
| `--reset` | *(flag)* | Delete existing checkpoint and start from scratch |
| `--topics` | *(all)* | Limit run to matching topic names (substring, case-insensitive) |
| `--annotate-existing` | *(flag)* | Rewrite the existing markdown with inferred topic tags without API calls |
| `--annotate-source` | *(output file)* | Optional source for annotation; supports `git:<rev>:<path>` |

---

## Workflow

### 1. Full re-fetch (refresh everything)

Use when topics have been added/modified or citation counts are stale.

```powershell
.venv\Scripts\python.exe code/fetch_llm_papers.py `
    --reset `
    --min-citations 150 `
    --top-n 50 `
    --request-delay 2.0 `
    --jitter 0.5
```

- `--reset` deletes any existing checkpoint so all 36 topics are re-queried.
- On success the checkpoint is automatically deleted.
- `section/x_llm_papers.md` is rewritten with topic coverage, topic tags, and sequential numbering sorted by citation count.
- If a Semantic Scholar API key is available, set `$env:S2_API_KEY` before running. The script sends it as the `x-api-key` header.

### 2. Resume after API interruption

The script saves a checkpoint (`section/x_llm_papers.checkpoint.json`) after each successful query and after each completed topic. If the run is interrupted by a rate-limit (HTTP 429), simply re-run **without** `--reset`:

```powershell
.venv\Scripts\python.exe code/fetch_llm_papers.py `
    --min-citations 150 `
    --top-n 50
```

The script prints `[resume] Loaded N papers, M completed topics, Q cached queries from checkpoint.` and skips already-finished topics. Query-level cache entries prevent successful queries from being reissued during resume.

If a query fails after retries, the script writes partial progress, keeps the current topic incomplete, and exits with a `[pause]` message. Re-run later without `--reset`.

### 3. Local annotation only (no API calls)

Use this when the paper pool already exists and you only need topic coverage or tag extraction refreshed:

```powershell
.venv\Scripts\python.exe code/fetch_llm_papers.py `
    --annotate-existing `
    --min-citations 150
```

To rebuild annotations from the committed version of the file, useful after a partial write or parser change:

```powershell
.venv\Scripts\python.exe code/fetch_llm_papers.py `
    --annotate-existing `
    --annotate-source git:HEAD:section/x_llm_papers.md `
    --min-citations 150
```

### 4. Refresh only specific topics

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
- Keep broad queries paired with relevance terms such as LLM, language model, transformer, foundation model, agent, RAG, or tool use. The script filters broad Semantic Scholar drift using topic keywords plus core LLM relevance terms.

**Current topic areas (36 total):**

| Category | Topics |
|----------|--------|
| Core LLM | Reasoning in LLMs, LLM Overview & History, Scaling Laws, LLM Architecture Innovations |
| Training | Alignment & RLHF, RLAIF & Constitutional AI, RLVR & Process Reward Models, Instruction Tuning & SFT, PEFT & LoRA, Self-Supervised & Representation Learning |
| Inference | Efficient LLMs: Training & Inference, Inference-Time Scaling & Test-Time Compute, LLMOps & Model Serving |
| Applications | LLM Agents, Retrieval-Augmented Generation (RAG), GraphRAG & Knowledge Graphs, LLMs for Code, LLMs for Healthcare & Science, LLM for Robotics & Embodied AI, Function Calling & Tool Use, GUI Agents, Tabular Data & NL2SQL |
| Multimodal | Multimodal LLMs, Small Language Models, Mixture of Experts |
| Evaluation | Evaluation of LLMs & Agents, Hallucination in LLMs, Trustworthy & Secure LLMs |
| Other | Prompt Engineering & In-Context Learning, Context Engineering, LLM Memory & Personalization, Embeddings & Vector Search, Data for LLMs, AIOps & Observability, Federated & Personalized AI, Continual Learning & Model Merging |

---

## Output Format

Each entry in `section/x_llm_papers.md`:

```
N. [Title📑](https://arxiv.org/abs/XXXX.XXXXX): First sentence of abstract. [Mon YYYY] (Citations: N,NNN; Topics: Topic A, Topic B)
```

- The file begins with `## Topic Coverage`, a count of inferred topic tags across all papers.
- Numbered sequentially (`1.`, `2.`, ...) by citation count descending.
- Link target is the arXiv URL if available, otherwise the Semantic Scholar URL.
- Date is derived from the arXiv ID prefix (e.g. `2305.xxxxx` → `[May 2023]`).
- Only Computer Science papers with `fieldsOfStudy` containing `"Computer Science"` are included.
- Topic tags come from the API topic that found the paper when fetched, or local keyword inference when running `--annotate-existing`.

---

## Checkpoint File

`section/x_llm_papers.checkpoint.json` — JSON with these keys:

```json
{
  "completed_topics": ["Reasoning in LLMs", "LLM Agents", ...],
    "failed_queries": ["..."],
    "query_cache": { "normalized query": [ ... ] },
  "papers": [ { "paperId": "...", "title": "...", "citationCount": 123, ... } ]
}
```

- Created/updated after each successful query and every topic completion.
- Deleted automatically on successful full run.
- If corrupted, delete manually and re-run with `--reset`.
- To inspect: `python -c "import json; cp=json.load(open('section/x_llm_papers.checkpoint.json', encoding='utf-8')); print(len(cp['papers']), 'papers,', len(cp['completed_topics']), 'topics done,', len(cp.get('query_cache', {})), 'cached queries')"`

---

## Common Pitfalls

1. **Modified TOPICS but not using `--reset`:** The checkpoint from a previous run skips topics that already completed. After editing `TOPICS`, always use `--reset` to re-fetch all topics.

2. **API rate limits (HTTP 429):** Semantic Scholar enforces per-IP rate limits. The script adds a default 2-second delay plus jitter between queries and retries with backoff. If repeatedly rate-limited, wait a few minutes and resume (no `--reset`). Increase `--request-delay` or `--backoff` to slow down further.

3. **Failed queries marked as complete:** Do not manually add a topic to `completed_topics` after a 429 or timeout. The script intentionally leaves incomplete topics out of `completed_topics` so resume can retry only the missing query work.

4. **Non-CS or off-topic papers in results:** The filter requires `"Computer Science"` in `fieldsOfStudy` and a topic/core LLM relevance match. Some highly cited ML papers may be excluded if they drift too far from the LLM landscape. This is intentional.
