"""Fetch high-citation papers covering the LLM landscape and derived technologies from Semantic Scholar.

Captures survey, research, and position papers across all major LLM topic areas derived
from the curated hint list in the awesome-azure-openai-llm knowledge base.
Only Computer Science papers with >= --min-citations citations are included.

Usage:
    python code/fetch_llm_papers.py
    python code/fetch_llm_papers.py --min-citations 200 --top-n 20
    python code/fetch_llm_papers.py --output files/llm_papers.md
    python code/fetch_llm_papers.py --topics "Reasoning" "Agents"
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from utils.http_utils import create_session, get_json
from utils.path_utils import get_repo_root


# ---------------------------------------------------------------------------
# Topic → query mapping
# Each entry maps a section name to a list of Semantic Scholar search queries.
# Queries intentionally omit "survey" to capture ALL high-citation papers
# (research contributions, position papers, benchmarks, overviews) in each area.
# ---------------------------------------------------------------------------
TOPICS: Dict[str, List[str]] = {
    "Reasoning in LLMs": [
        "advancing reasoning large language models methods approaches",
        "chain-of-thought reasoning LLM prompting",
        "agentic reasoning large language models",
        "thinking machines LLM reasoning strategies",
        "efficient reasoning large language models",
        "stop overthinking efficient reasoning LLM",
        "harnessing reasoning economy efficient LLM",
        "mathematical reasoning large language models benchmark",
        "tree of thoughts deliberate problem solving LLM",
        "reinforcement learning verifiable rewards reasoning LLM",
        "DeepSeek-R1 incentivizing reasoning reinforcement learning",
        "process reward model mathematical reasoning step-by-step",
        "test-time compute scaling reasoning language model",
        "logical reasoning commonsense large language models",
    ],
    "LLM Agents": [
        "LLM-based autonomous agents",
        "large language model based agents",
        "AI agents large language models",
        "agent AI towards holistic intelligence position paper",
        "evaluation LLM-based agents benchmark",
        "AI agent protocols communication",
        "LLM agent communication protocols security countermeasures",
        "rise potential large language model based agents",
        "autonomous agents language model planning tool use",
    ],
    "Retrieval-Augmented Generation (RAG)": [
        "retrieval-augmented generation large language models",
        "agentic retrieval-augmented generation RAG",
        "retrieval augmented text generation LLM",
        "retrieval structuring augmented generation LLM",
        "dense passage retrieval open-domain question answering",
    ],
    "GUI Agents": [
        "GUI agents large language models",
        "large language model brained GUI agents",
        "web agent GUI automation LLM",
    ],
    "Hallucination in LLMs": [
        "hallucination large language models taxonomy",
        "mitigating hallucination large language models techniques",
        "hallucination natural language generation",
        "factuality large language models overview",
        "sycophancy LLM faithfulness factual accuracy",
    ],
    "Prompt Engineering & In-Context Learning": [
        "prompt engineering large language models NLP tasks",
        "automatic prompt optimization techniques LLM",
        "in-context learning large language models",
        "few-shot prompting large language models",
        "chain-of-thought prompting elicits reasoning",
    ],
    "Context Engineering": [
        "context engineering large language models",
        "long context large language models",
        "retrieval augmented generation context window",
    ],
    "Efficient LLMs: Training & Inference": [
        "efficient training transformers",
        "model compression large language models",
        "compression algorithms language models quantization pruning",
        "efficient guided generation large language models",
        "transformer inference optimization techniques",
        "efficient generative large language model serving systems",
        "efficient architectures large language models speed",
        "speculative decoding language model inference",
        "knowledge distillation language models",
        "flash attention fast memory efficient exact attention IO-awareness",
        "quantization INT4 INT8 LLM weight-only",
        "AWQ activation-aware weight quantization LLM",
    ],
    "Alignment & RLHF": [
        "aligned large language models human feedback",
        "reinforcement learning from human feedback open problems limitations",
        "post-training large language models alignment",
        "direct preference optimization language models",
        "constitutional AI harmless helpful language model",
        "PPO proximal policy optimization language model fine-tuning",
        "GRPO group relative policy optimization language model",
        "reward hacking alignment language models",
        "scalable oversight alignment language models",
        "value alignment large language models safety",
    ],
    "Evaluation of LLMs & Agents": [
        "evaluation large language models comprehensive",
        "evaluating large language models benchmark",
        "LLM-as-a-Judge evaluation framework",
        "SEED-Bench benchmarking multimodal LLMs comprehension",
        "evaluation LLM-based agents benchmark",
        "LLM benchmark leaderboard evaluation methodology",
    ],
    "Multimodal LLMs": [
        "multimodal large language models",
        "foundation models vision language",
        "multimodal deep learning vision language",
        "mathematical reasoning multimodal large language models challenges",
        "vision language model image understanding",
    ],
    "Small Language Models": [
        "small language models measurements insights",
        "small language models era large language models",
        "role small models LLM era",
        "phi language model small efficient",
    ],
    "Mixture of Experts": [
        "mixture of experts large language models",
        "sparse mixture of experts transformer",
        "MoE language model routing",
    ],
    "LLMs for Healthcare & Science": [
        "large language models healthcare clinical NLP",
        "medical reasoning large language models",
        "autonomous scientific discovery AI agentic science",
        "large language models biology chemistry science",
    ],
    "LLMs for Code": [
        "code foundation models agents applications",
        "code intelligence large language models",
        "code generation large language models",
        "LLM program synthesis code completion",
    ],
    "Tabular Data & NL2SQL": [
        "NL2SQL large language models text-to-SQL",
        "tabular data understanding large language models",
        "table question answering language model",
    ],
    "Data for LLMs": [
        "data management large language models",
        "data synthesis augmentation large language models",
        "pretraining data curation large language models",
    ],
    "Trustworthy & Secure LLMs": [
        "trustworthy large language models safety",
        "adversarial attacks aligned language models universal",
        "jailbreak attacks large language models",
        "red-teaming large language models safety",
    ],
    "LLM Overview & History": [
        "AI-generated content AIGC history generative AI GAN ChatGPT",
        "large language models ChatGPT GPT-4 research perspective",
        "open-source large language models ChatGPT benchmarks performance",
        "language models recent developments outlook",
        "challenges applications large language models NLP",
        "harnessing power LLMs in practice ChatGPT beyond",
        "Google Gemini OpenAI GPT reshaping generative AI research",
        "foundation models opportunities risks",
    ],
    "AIOps & Observability": [
        "AIOps large language models era",
        "LLM operations observability monitoring",
        "log anomaly detection large language model",
    ],
    "Federated & Personalized AI": [
        "personalized federated intelligence foundation model",
        "federated learning large language models",
        "towards artificial general personalized intelligence",
    ],
    "Self-Supervised & Representation Learning": [
        "self-supervised learning cookbook methods",
        "self-supervised representation learning transformers",
        "contrastive learning language model pretraining",
    ],
    "GraphRAG & Knowledge Graphs": [
        "graph retrieval-augmented generation knowledge graph LLM",
        "GraphRAG knowledge graph large language models",
        "knowledge graph question answering large language models",
        "graph neural networks language models",
        "knowledge-enhanced large language models",
    ],
    "Embeddings & Vector Search": [
        "text embeddings large language models dense retrieval",
        "sentence embeddings semantic similarity",
        "vector databases approximate nearest neighbor search",
        "dense retrieval neural information retrieval",
        "embedding models language representation MTEB",
    ],
    "Function Calling & Tool Use": [
        "tool learning large language models API",
        "function calling language models external tools",
        "LLM tool augmented generation external knowledge",
        "language models API calling tool use",
        "plan and execute LLM tools agents",
    ],
    "LLM for Robotics & Embodied AI": [
        "large language models robotics embodied AI",
        "foundation models for robotic manipulation",
        "LLM robot planning grounding",
        "vision language models robotics",
        "embodied intelligence large language models",
    ],
    "LLMOps & Model Serving": [
        "LLMOps large language model operations deployment",
        "efficient serving large language models inference",
        "continuous batching language model serving",
        "AI model deployment monitoring production",
        "vLLM PagedAttention efficient LLM serving",
    ],
    "PEFT & LoRA": [
        "LoRA low-rank adaptation large language models",
        "parameter-efficient fine-tuning methods survey",
        "QLoRA efficient finetuning quantized LLMs",
        "adapter methods parameter-efficient transfer learning",
        "prefix tuning prompt tuning parameter efficient",
        "AdaLoRA adaptive budget allocation parameter efficient fine-tuning",
        "LoftQ LoRA fine-tuning quantization initializing language models",
        "DoRA weight-decomposed low-rank adaptation",
    ],
    "Instruction Tuning & SFT": [
        "instruction tuning large language models",
        "supervised fine-tuning language models instruction following",
        "self-instruct aligning language models instruction self-generated",
        "finetuned language models zero-shot learners",
        "LIMA less is more alignment data instruction tuning",
        "open instruction following evaluation benchmark",
        "alpaca instruction-following fine-tuning language model",
        "distilabel synthetic data instruction tuning pipeline",
    ],
    "RLAIF & Constitutional AI": [
        "reinforcement learning AI feedback RLAIF",
        "constitutional AI training harmless assistant AI feedback",
        "AI feedback preference learning language models",
        "self-rewarding language models AI feedback alignment",
        "scalable AI feedback language model alignment",
        "weak-to-strong generalization superalignment",
        "reward model AI preference language model",
    ],
    "RLVR & Process Reward Models": [
        "reinforcement learning verifiable rewards language model RLVR",
        "process reward model step-level feedback math reasoning",
        "outcome reward model ORM process reward PRM comparison",
        "DeepSeek GRPO reinforcement learning reasoning",
        "let's verify step by step process reward model",
        "math olympiad problem solving reinforcement learning LLM",
        "reward shaping language model reasoning verifiable",
        "STILL thinking slower language model reinforcement learning",
    ],
    "Inference-Time Scaling & Test-Time Compute": [
        "inference time scaling test-time compute language model",
        "scaling LLM test-time compute verifier reranking",
        "o1 OpenAI reasoning model thinking tokens",
        "chain-of-thought test time reasoning scaling",
        "best-of-n sampling language model inference compute",
        "self-consistency chain of thought reasoning LLM decoding",
        "compute-optimal inference language models",
        "thinking longer test-time reasoning scaling laws",
    ],
    "Scaling Laws": [
        "scaling laws neural language models",
        "Chinchilla training compute optimal large language models",
        "emergent abilities large language models scaling",
        "scaling data model size language model performance",
        "neural scaling laws data model compute",
        "grokking generalization beyond overfitting neural networks",
        "scaling language models methods analysis insights",
    ],
    "LLM Architecture Innovations": [
        "flash attention efficient exact attention IO-awareness",
        "Mamba linear time sequence modeling selective state spaces",
        "RWKV parallelizable RNN language models transformer",
        "rotary position embedding RoPE transformer",
        "grouped query attention GQA multi-query attention inference",
        "RetNet retentive network successor transformer",
        "state space model SSM sequence modeling language",
        "transformer architecture improvements efficiency",
        "sparse attention transformer long sequences",
        "multi-head latent attention KV cache compression",
    ],
    "Continual Learning & Model Merging": [
        "continual learning large language models catastrophic forgetting",
        "model merging task vectors weight interpolation language models",
        "model soup averaging weights fine-tuning",
        "ties-merging resolving interference model merging",
        "knowledge editing large language models",
        "lifelong learning language models forgetting",
        "catastrophic forgetting neural networks continual learning",
        "parameter merging multi-task language models",
    ],
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def infer_arxiv_date(arxiv_id: str) -> Optional[Tuple[int, int]]:
    """Infer (year, month) from arXiv ID (YYMM.NNNNN format)."""
    match = re.match(r"(\d{2})(\d{2})\.(\d{4,5})", arxiv_id)
    if not match:
        return None
    yy, mm = int(match.group(1)), int(match.group(2))
    year = 2000 + yy
    if not (1 <= mm <= 12 and 2000 <= year <= datetime.now().year + 1):
        return None
    return year, mm


def format_month_year(year: int, month: int) -> str:
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return f"[{months[month - 1]} {year}]"


# ---------------------------------------------------------------------------
# Fetcher
# ---------------------------------------------------------------------------

class SemanticScholarFetcher:
    BASE_URL = "https://api.semanticscholar.org/graph/v1"

    _FIELDS = [
        "paperId",
        "title",
        "authors",
        "year",
        "citationCount",
        "abstract",
        "venue",
        "url",
        "externalIds",
        "fieldsOfStudy",
    ]

    def __init__(
        self,
        *,
        user_agent: Optional[str],
        timeout: int,
        max_retries: int,
        backoff: float,
    ) -> None:
        self.session = create_session(user_agent)
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff = backoff

    def search_papers(self, query: str, limit: int = 100) -> List[Dict]:
        params = {
            "query": query,
            "limit": min(limit, 100),
            "fields": ",".join(self._FIELDS),
        }
        data = get_json(
            self.session,
            f"{self.BASE_URL}/paper/search",
            params=params,
            timeout=self.timeout,
            max_retries=self.max_retries,
            backoff=self.backoff,
        )
        time.sleep(1)  # be polite to the API
        if not data:
            return []
        return data.get("data", [])

    def fetch_topic(
        self, queries: List[str], top_n: int, min_citations: int
    ) -> List[Dict]:
        """Aggregate results for multiple queries, deduplicate, filter, sort."""
        seen: set = set()
        papers: List[Dict] = []

        for query in queries:
            for paper in self.search_papers(query):
                pid = paper.get("paperId")
                if pid and pid not in seen:
                    seen.add(pid)
                    papers.append(paper)

        filtered = [
            p for p in papers
            if p.get("citationCount", 0) >= min_citations
            and p.get("fieldsOfStudy")
            and "Computer Science" in p.get("fieldsOfStudy", [])
        ]
        filtered.sort(key=lambda p: p.get("citationCount", 0), reverse=True)
        return filtered[:top_n]


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def _paper_arxiv_url(paper: Dict) -> Optional[str]:
    ext = paper.get("externalIds") or {}
    arxiv_id = ext.get("ArXiv")
    return f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None


def _paper_date_str(paper: Dict) -> str:
    ext = paper.get("externalIds") or {}
    arxiv_id = ext.get("ArXiv")
    if arxiv_id:
        ym = infer_arxiv_date(arxiv_id)
        if ym:
            return format_month_year(ym[0], ym[1])
    return ""


def _author_str(paper: Dict) -> str:
    authors = paper.get("authors", [])
    names = [a.get("name", "") for a in authors[:3]]
    suffix = ", et al." if len(authors) > 3 else ""
    return ", ".join(names) + suffix


def format_paper_console(paper: Dict, rank: int) -> str:
    lines = [
        f"\n{rank}. {paper.get('title', 'No title')}",
        f"   Authors: {_author_str(paper)}",
        f"   Year: {paper.get('year', 'N/A')} | Citations: {paper.get('citationCount', 0):,}"
        f" | Venue: {paper.get('venue', 'N/A')}",
    ]
    date_str = _paper_date_str(paper)
    if date_str:
        lines.append(f"   Date: {date_str}")
    arxiv_url = _paper_arxiv_url(paper)
    if arxiv_url:
        lines.append(f"   arXiv: {arxiv_url}")
    else:
        lines.append(f"   URL: {paper.get('url', 'N/A')}")
    return "\n".join(lines) + "\n"


def _short_description(paper: Dict) -> str:
    """Return a short description from the abstract (first sentence, max 200 chars)."""
    abstract = (paper.get("abstract") or "").strip()
    if not abstract:
        return ""
    # Take up to the first sentence-ending punctuation
    for end in (".", "!", "?"):
        idx = abstract.find(end)
        if 30 < idx < 200:
            return abstract[: idx + 1]
    # Fallback: truncate at 200 chars on a word boundary
    if len(abstract) > 200:
        cut = abstract[:200].rsplit(" ", 1)[0]
        return cut.rstrip(",;:") + " ..."
    return abstract


def format_compact_entry(paper: Dict, rank: int = 0) -> str:
    """Format: N. [Title📑](url): description. [Mon YYYY] (Citations: NNN)"""
    title = paper.get("title", "No title")
    arxiv_url = _paper_arxiv_url(paper)
    link = arxiv_url or paper.get("url", "#")
    desc = _short_description(paper)
    date_str = _paper_date_str(paper)
    citations = paper.get("citationCount", 0)

    prefix = f"{rank}." if rank > 0 else "1."
    entry = f"{prefix} [{title}📑]({link})"
    if desc:
        entry += f": {desc}"
    if date_str:
        entry += f" {date_str}"
    entry += f" (Citations: {citations:,})"
    return entry


def _load_checkpoint(checkpoint_file: str) -> tuple[List[Dict], set, List[str]]:
    """Load checkpoint: returns (papers, seen_ids, completed_topics)."""
    path = Path(checkpoint_file)
    if not path.exists():
        return [], set(), []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        papers = data.get("papers", [])
        completed = data.get("completed_topics", [])
        seen = {p["paperId"] for p in papers if p.get("paperId")}
        print(f"  [resume] Loaded {len(papers)} papers, {len(completed)} completed topics from checkpoint.")
        return papers, seen, completed
    except Exception as exc:
        print(f"  [WARN] Could not read checkpoint ({exc}); starting fresh.")
        return [], set(), []


def _save_checkpoint(checkpoint_file: str, papers: List[Dict], completed_topics: List[str]) -> None:
    """Persist current state to checkpoint JSON."""
    data = {"completed_topics": completed_topics, "papers": papers}
    Path(checkpoint_file).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def _flush_output(output_file: str, papers: List[Dict], min_citations: int) -> List[str]:
    """Sort papers by citation count and rewrite the output markdown. Returns compact lines."""
    sorted_papers = sorted(papers, key=lambda p: p.get("citationCount", 0), reverse=True)
    compact_lines = [format_compact_entry(p, rank=i + 1) for i, p in enumerate(sorted_papers)]
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# LLM Landscape Papers (Citation \u2265 {})\n\n".format(min_citations))
        f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*  \n")
        f.write("*Source: Semantic Scholar API \u2014 Computer Science papers only*  \n")
        f.write(f"*Total papers: {len(sorted_papers)}*\n\n")
        f.write("\n".join(compact_lines) + "\n")
    return compact_lines


def write_markdown_section(f, topic: str, papers: List[Dict]) -> None:
    f.write(f"\n## {topic}\n\n")
    f.write(f"*Retrieved: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*  \n")
    f.write(f"*Papers shown: {len(papers)}*\n\n")

    if not papers:
        f.write("*No papers found meeting the criteria.*\n\n")
        return

    for idx, paper in enumerate(papers, 1):
        title = paper.get("title", "No title")
        url = paper.get("url", "")
        arxiv_url = _paper_arxiv_url(paper)
        link = arxiv_url or url

        f.write(f"### {idx}. [{title}]({link})\n\n")
        f.write(f"**Authors:** {_author_str(paper)}  \n")
        f.write(
            f"**Year:** {paper.get('year', 'N/A')} | "
            f"**Citations:** {paper.get('citationCount', 0):,} | "
            f"**Venue:** {paper.get('venue', 'N/A')}  \n"
        )
        date_str = _paper_date_str(paper)
        if date_str:
            f.write(f"**Month:** {date_str}  \n")
        fields = paper.get("fieldsOfStudy") or []
        if fields:
            f.write(f"**Fields:** {', '.join(fields)}  \n")
        if arxiv_url:
            f.write(f"**arXiv:** [{arxiv_url}]({arxiv_url})  \n")

        abstract = paper.get("abstract", "")
        if abstract:
            # Truncate very long abstracts for readability
            if len(abstract) > 600:
                abstract = abstract[:600].rstrip() + " ..."
            f.write(f"\n> {abstract}\n")
        f.write("\n---\n\n")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Fetch high-citation LLM landscape papers (research, surveys, benchmarks) from Semantic Scholar."
    )
    parser.add_argument("--output", help="Output markdown file path.")
    parser.add_argument(
        "--min-citations", type=int, default=150,
        help="Minimum citation count (default: 150)."
    )
    parser.add_argument(
        "--top-n", type=int, default=50,
        help="Top N papers per topic (default: 50)."
    )
    parser.add_argument("--timeout", type=int, default=30)
    parser.add_argument("--max-retries", type=int, default=5)
    parser.add_argument("--backoff", type=float, default=1.0)
    parser.add_argument(
        "--user-agent", default="Academic-Research-Tool/1.0",
        help="HTTP User-Agent header."
    )
    parser.add_argument(
        "--topics", nargs="*",
        help="Limit to specific topic names (substring match, case-insensitive)."
    )
    parser.add_argument(
        "--reset", action="store_true",
        help="Ignore any existing checkpoint and start from scratch."
    )
    args = parser.parse_args()

    fetcher = SemanticScholarFetcher(
        user_agent=args.user_agent,
        timeout=args.timeout,
        max_retries=args.max_retries,
        backoff=args.backoff,
    )

    # Optionally filter topics
    topics_to_run = TOPICS
    if args.topics:
        filters = [t.lower() for t in args.topics]
        topics_to_run = {
            k: v for k, v in TOPICS.items()
            if any(f in k.lower() for f in filters)
        }
        if not topics_to_run:
            print("No matching topics found. Available topics:")
            for t in TOPICS:
                print(f"  {t}")
            return

    root_dir = get_repo_root(__file__)
    output_file = args.output or str(root_dir / "section" / "x_llm_papers.md")
    checkpoint_file = str(Path(output_file).with_suffix(".checkpoint.json"))

    # Load or reset checkpoint
    if args.reset and Path(checkpoint_file).exists():
        Path(checkpoint_file).unlink()
        print("  [reset] Checkpoint deleted.")

    global_papers, global_seen, completed_topics = _load_checkpoint(checkpoint_file)

    # Collect all papers across every topic into a single deduplicated pool
    for topic_name, queries in topics_to_run.items():
        if topic_name in completed_topics:
            print(f"\n[{topic_name}] Already done (skipping).")
            continue

        print(f"\n[{topic_name}] Querying {len(queries)} search term(s)...")
        papers = fetcher.fetch_topic(queries, top_n=args.top_n, min_citations=args.min_citations)
        for paper in papers:
            pid = paper.get("paperId")
            if pid and pid not in global_seen:
                global_seen.add(pid)
                global_papers.append(paper)
        completed_topics.append(topic_name)
        print(f"  -> {len(papers)} papers (pool size: {len(global_papers)})")

        # Persist progress after every topic so we can resume on interruption
        _save_checkpoint(checkpoint_file, global_papers, completed_topics)
        _flush_output(output_file, global_papers, args.min_citations)

    # Final flush (updates timestamp)
    compact_lines = _flush_output(output_file, global_papers, args.min_citations)

    # Print to console
    sorted_papers = sorted(global_papers, key=lambda p: p.get("citationCount", 0), reverse=True)
    for idx, paper in enumerate(sorted_papers, 1):
        print(format_paper_console(paper, idx))

    print(f"\nDone. {len(global_papers)} unique papers saved to: {output_file}")

    # Remove checkpoint on successful completion
    if Path(checkpoint_file).exists():
        Path(checkpoint_file).unlink()
        print("  [done] Checkpoint removed.")


if __name__ == "__main__":
    main()
