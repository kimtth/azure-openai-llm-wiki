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
import os
import random
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Callable, Dict, List, Optional, Tuple

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

from utils.http_utils import create_session, get_json  # noqa: E402
from utils.path_utils import get_repo_root  # noqa: E402


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
    "LLM Memory & Personalization": [
        "memory mechanism large language model agents",
        "long-term memory LLM agents",
        "personalized large language models memory",
        "conversation memory large language models agents",
        "agent memory large language models",
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


STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "based", "by", "for", "from", "in", "is", "it", "model",
    "models", "large", "language", "llm", "llms", "of", "on", "or", "the", "to", "towards", "using",
    "via", "with",
}

CORE_RELEVANCE_TERMS = (
    "large language model", "large language models", "llm", "llms", "language model", "language models",
    "chatgpt", "gpt-4", "gpt4", "foundation model", "foundation models", "transformer",
    "transformers", "pretrained language", "pre-trained language", "instruction tuning", "prompt tuning",
    "retrieval-augmented", "retrieval augmented", "vision-language", "multimodal", "tool use",
    "agent", "agents", "text-to-sql", "code generation", "mixture-of-experts", "mixture of experts",
    "lora", "quantization", "embedding", "state space model", "mamba", "rlhf", "alignment",
)

TOPIC_KEYWORDS: Dict[str, Tuple[str, ...]] = {
    "Reasoning in LLMs": (
        "reasoning", "chain-of-thought", "chain of thought", "tree of thoughts", "math reasoning",
        "logical reasoning", "test-time compute", "process reward", "verifiable reward",
    ),
    "LLM Agents": ("agent", "agents", "autonomous", "planning", "multi-agent", "agentic"),
    "Retrieval-Augmented Generation (RAG)": ("retrieval-augmented", "retrieval augmented", "rag", "dense retrieval"),
    "GUI Agents": ("gui", "computer use", "web agent", "screen", "ui agent"),
    "Hallucination in LLMs": ("hallucination", "hallucinations", "factuality", "faithfulness", "sycophancy"),
    "Prompt Engineering & In-Context Learning": (
        "prompt", "prompting", "in-context", "few-shot", "demonstrations", "prompt engineering",
    ),
    "Context Engineering": ("long context", "context window", "context engineering", "prompt compression"),
    "LLM Memory & Personalization": (
        "memory", "long-term memory", "conversation memory", "personalized", "personalization",
        "user preference", "agent memory",
    ),
    "Efficient LLMs: Training & Inference": (
        "efficient", "inference", "serving", "compression", "quantization", "pruning", "distillation",
        "speculative decoding", "flashattention", "pagedattention",
    ),
    "Alignment & RLHF": ("alignment", "rlhf", "human feedback", "preference", "reward model", "dpo"),
    "Evaluation of LLMs & Agents": ("evaluation", "benchmark", "bench", "leaderboard", "judge"),
    "Multimodal LLMs": ("multimodal", "vision-language", "vision language", "video", "image", "audio"),
    "Small Language Models": ("small language", "slm", "mobilellm", "phi", "on-device"),
    "Mixture of Experts": ("mixture of experts", "mixture-of-experts", "moe", "routing"),
    "LLMs for Healthcare & Science": ("healthcare", "clinical", "medical", "medicine", "science", "chemistry", "biology"),
    "LLMs for Code": ("code", "program synthesis", "code generation", "software engineering", "verilog"),
    "Tabular Data & NL2SQL": ("tabular", "table", "text-to-sql", "nl2sql", "sql"),
    "Data for LLMs": ("data", "dataset", "pretraining data", "synthetic data", "data curation"),
    "Trustworthy & Secure LLMs": (
        "trustworthy", "security", "safety", "jailbreak", "red-teaming", "adversarial", "privacy",
    ),
    "LLM Overview & History": ("survey", "overview", "history", "foundation models", "aigc", "chatgpt"),
    "AIOps & Observability": ("aiops", "observability", "monitoring", "logs", "anomaly"),
    "Federated & Personalized AI": ("federated", "personalized", "personalization", "private data"),
    "Self-Supervised & Representation Learning": (
        "self-supervised", "self supervised", "representation learning", "contrastive", "masked language",
    ),
    "GraphRAG & Knowledge Graphs": ("graphrag", "knowledge graph", "graph rag", "graph retrieval"),
    "Embeddings & Vector Search": ("embedding", "embeddings", "vector", "semantic similarity", "dense retrieval"),
    "Function Calling & Tool Use": ("tool", "tools", "function calling", "api", "tool learning"),
    "LLM for Robotics & Embodied AI": (
        "robot", "robotics", "embodied", "vision-language-action", "vla", "physical world",
        "grounded language", "parse and perceive",
    ),
    "LLMOps & Model Serving": ("llmops", "serving", "deployment", "continuous batching", "pagedattention"),
    "PEFT & LoRA": ("lora", "qlora", "adapter", "parameter-efficient", "peft", "prefix tuning"),
    "Instruction Tuning & SFT": ("instruction tuning", "instruction following", "sft", "self-instruct", "alpaca"),
    "RLAIF & Constitutional AI": ("rlaif", "constitutional ai", "ai feedback", "harmless"),
    "RLVR & Process Reward Models": ("rlvr", "process reward", "verifiable reward", "grpo", "reward shaping"),
    "Inference-Time Scaling & Test-Time Compute": (
        "test-time", "inference-time", "thinking", "best-of-n", "self-consistency", "verifier",
    ),
    "Scaling Laws": ("scaling law", "scaling laws", "compute-optimal", "chinchilla", "emergent abilities"),
    "LLM Architecture Innovations": (
        "architecture", "attention", "mamba", "rwkv", "rope", "gqa", "state space", "retnet", "kv cache",
    ),
    "Continual Learning & Model Merging": (
        "continual", "catastrophic forgetting", "model merging", "model soup", "knowledge editing", "lifelong",
    ),
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


def _paper_text(paper: Dict) -> str:
    return " ".join(
        str(paper.get(key) or "") for key in ("title", "abstract", "venue")
    ).lower()


def _contains_term(text: str, term: str) -> bool:
    term = term.lower()
    if len(term) <= 4 and term.isalnum():
        return bool(re.search(rf"\b{re.escape(term)}\b", text))
    return term in text


def _has_core_relevance(paper: Dict) -> bool:
    text = _paper_text(paper)
    return any(_contains_term(text, term) for term in CORE_RELEVANCE_TERMS)


def _topic_score(paper: Dict, topic: str) -> float:
    text = _paper_text(paper)
    score = 0.0

    for keyword in TOPIC_KEYWORDS.get(topic, ()):
        if _contains_term(text, keyword):
            score += 3.0 if " " in keyword or "-" in keyword else 1.5

    for query in TOPICS.get(topic, []):
        tokens = [t for t in re.findall(r"[a-z0-9]+", query.lower()) if t not in STOPWORDS and len(t) > 2]
        if not tokens:
            continue
        hits = sum(1 for token in tokens if _contains_term(text, token))
        if hits >= min(2, len(tokens)):
            score += hits / len(tokens)

    return score


def infer_paper_topics(paper: Dict, max_topics: int = 3) -> List[str]:
    """Infer likely topic tags from title/abstract text for compact output."""
    existing = paper.get("topics") or []
    if existing:
        return list(dict.fromkeys(existing))[:max_topics]

    scored = [
        (topic, _topic_score(paper, topic))
        for topic in TOPICS
    ]
    topics = [topic for topic, score in sorted(scored, key=lambda item: item[1], reverse=True) if score > 0]
    if not topics and _has_core_relevance(paper):
        topics = ["LLM Overview & History"]
    return topics[:max_topics]


def _is_relevant_paper(paper: Dict, topic: str) -> bool:
    """Keep broad Semantic Scholar searches from drifting away from the LLM landscape."""
    fields = paper.get("fieldsOfStudy") or []
    if "Computer Science" not in fields:
        return False
    if not _has_core_relevance(paper):
        return False
    return _topic_score(paper, topic) > 0


class QueryFetchError(RuntimeError):
    """Raised when a Semantic Scholar query cannot be fetched after retries."""


class TopicFetchIncomplete(RuntimeError):
    """Raised when a topic has partial results but one or more queries failed."""

    def __init__(self, topic: str, papers: List[Dict], failed_queries: List[str]) -> None:
        super().__init__(f"{topic}: {len(failed_queries)} query/query(s) failed")
        self.topic = topic
        self.papers = papers
        self.failed_queries = failed_queries


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
        api_key: Optional[str],
        timeout: int,
        max_retries: int,
        backoff: float,
        request_delay: float,
        jitter: float,
    ) -> None:
        self.session = create_session(user_agent)
        if api_key:
            self.session.headers.update({"x-api-key": api_key})
        self.timeout = timeout
        self.max_retries = max_retries
        self.backoff = backoff
        self.request_delay = request_delay
        self.jitter = jitter

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
        if self.request_delay > 0:
            time.sleep(self.request_delay + random.uniform(0, max(self.jitter, 0)))
        if not data:
            raise QueryFetchError(f"Semantic Scholar query failed after retries: {query}")
        return data.get("data", [])

    def fetch_topic(
        self,
        topic: str,
        queries: List[str],
        top_n: int,
        min_citations: int,
        query_cache: Dict[str, List[Dict]],
        cache_updated: Optional[Callable[[], None]] = None,
    ) -> List[Dict]:
        """Aggregate results for multiple queries, deduplicate, filter, sort."""
        seen: set = set()
        papers: List[Dict] = []
        failed_queries: List[str] = []

        for query in queries:
            cache_key = query.strip().lower()
            if cache_key in query_cache:
                search_results = query_cache[cache_key]
                print(f"  [cache] {query}")
            else:
                try:
                    search_results = self.search_papers(query)
                except QueryFetchError as exc:
                    print(f"  [WARN] {exc}")
                    failed_queries.append(query)
                    break
                query_cache[cache_key] = search_results
                if cache_updated:
                    cache_updated()

            for paper in search_results:
                pid = paper.get("paperId")
                if pid and pid not in seen:
                    seen.add(pid)
                    papers.append(paper)

        filtered = [
            p for p in papers
            if p.get("citationCount", 0) >= min_citations
            and _is_relevant_paper(p, topic)
        ]
        filtered.sort(key=lambda p: p.get("citationCount", 0), reverse=True)

        for paper in filtered:
            paper["topics"] = list(dict.fromkeys([*(paper.get("topics") or []), topic]))

        if failed_queries:
            raise TopicFetchIncomplete(topic, filtered[:top_n], failed_queries)

        return filtered[:top_n]


# ---------------------------------------------------------------------------
# Formatting
# ---------------------------------------------------------------------------

def _paper_arxiv_url(paper: Dict) -> Optional[str]:
    ext = paper.get("externalIds") or {}
    arxiv_id = ext.get("ArXiv")
    return f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else None


def _paper_link(paper: Dict) -> str:
    return _paper_arxiv_url(paper) or paper.get("link") or paper.get("url") or "#"


def _paper_date_str(paper: Dict) -> str:
    if paper.get("date_str"):
        return paper["date_str"]
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
    if paper.get("description"):
        return paper["description"].strip()
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
    link = _paper_link(paper)
    desc = _short_description(paper)
    date_str = _paper_date_str(paper)
    citations = paper.get("citationCount", 0)
    topics = infer_paper_topics(paper)

    prefix = f"{rank}." if rank > 0 else "1."
    entry = f"{prefix} [{title}📑]({link})"
    if desc:
        entry += f": {desc}"
    if date_str:
        entry += f" {date_str}"
    topic_str = f"; Topics: {', '.join(topics)}" if topics else ""
    entry += f" (Citations: {citations:,}{topic_str})"
    return entry


def _parse_compact_entry(line: str) -> Optional[Dict]:
    if not re.match(r"^\d+\. ", line):
        return None

    citation_match = re.search(r" \(Citations: ([\d,]+)(?:; Topics: (.*))?\)$", line)
    if not citation_match:
        return None

    body = line[: citation_match.start()]
    link_match = re.match(r"^\d+\. \[(.+?)\]\(([^)]+)\)(.*)$", body)
    if not link_match:
        return None

    title, link, remainder = link_match.groups()
    title = re.sub(r"(?:📑|≡ƒôæ)$", "", title).strip()
    date_str = ""
    date_match = re.search(r" (\[[A-Z][a-z]{2} \d{4}\])$", remainder)
    if date_match:
        date_str = date_match.group(1)
        remainder = remainder[: date_match.start()]

    abstract = remainder[2:].strip() if remainder.startswith(": ") else ""
    topics = []
    if citation_match.group(2):
        topics = [topic.strip() for topic in citation_match.group(2).split(",") if topic.strip()]

    paper = {
        "paperId": link,
        "title": title,
        "link": link,
        "url": link,
        "abstract": abstract,
        "description": abstract,
        "date_str": date_str,
        "citationCount": int(citation_match.group(1).replace(",", "")),
        "topics": topics,
    }
    if not topics:
        paper["topics"] = infer_paper_topics(paper)
    return paper


def _compact_entry_blocks(markdown_text: str) -> List[str]:
    blocks: List[str] = []
    current: List[str] = []

    for line in markdown_text.splitlines():
        if re.match(r"^\d+\. ", line):
            if current:
                blocks.append(" ".join(part.strip() for part in current if part.strip()))
            current = [line]
        elif current and not line.startswith("#") and line.strip():
            current.append(line)

    if current:
        blocks.append(" ".join(part.strip() for part in current if part.strip()))
    return blocks


def _load_existing_markdown(output_file: str, source_file: Optional[str] = None) -> List[Dict]:
    if source_file == "-":
        markdown_text = sys.stdin.read()
    elif source_file and source_file.startswith("git:"):
        repo_root = get_repo_root(__file__)
        markdown_bytes = subprocess.check_output(
            ["git", "show", source_file.removeprefix("git:")],
            cwd=repo_root,
        )
        markdown_text = markdown_bytes.decode("utf-8")
    else:
        path = Path(source_file or output_file)
        if not path.exists():
            return []
        markdown_text = path.read_text(encoding="utf-8")

    papers = []
    for line in _compact_entry_blocks(markdown_text):
        paper = _parse_compact_entry(line)
        if paper:
            papers.append(paper)
    return papers


def _topic_counts(papers: List[Dict]) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for paper in papers:
        for topic in infer_paper_topics(paper):
            counts[topic] = counts.get(topic, 0) + 1
    return dict(sorted(counts.items(), key=lambda item: (-item[1], item[0])))


def _load_checkpoint(checkpoint_file: str) -> tuple[List[Dict], set, List[str], Dict[str, List[Dict]], List[str]]:
    """Load checkpoint with backward compatibility for older checkpoint files."""
    path = Path(checkpoint_file)
    if not path.exists():
        return [], set(), [], {}, []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        papers = data.get("papers", [])
        completed = data.get("completed_topics", [])
        query_cache = data.get("query_cache", {})
        failed_queries = data.get("failed_queries", [])
        seen = {p["paperId"] for p in papers if p.get("paperId")}
        print(
            f"  [resume] Loaded {len(papers)} papers, {len(completed)} completed topics, "
            f"{len(query_cache)} cached queries from checkpoint."
        )
        return papers, seen, completed, query_cache, failed_queries
    except Exception as exc:
        print(f"  [WARN] Could not read checkpoint ({exc}); starting fresh.")
        return [], set(), [], {}, []


def _save_checkpoint(
    checkpoint_file: str,
    papers: List[Dict],
    completed_topics: List[str],
    query_cache: Dict[str, List[Dict]],
    failed_queries: List[str],
) -> None:
    """Persist current state to checkpoint JSON."""
    data = {
        "completed_topics": completed_topics,
        "failed_queries": failed_queries,
        "query_cache": query_cache,
        "papers": papers,
    }
    Path(checkpoint_file).write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")


def _flush_output(output_file: str, papers: List[Dict], min_citations: int) -> List[str]:
    """Sort papers by citation count and rewrite the output markdown. Returns compact lines."""
    sorted_papers = sorted(papers, key=lambda p: p.get("citationCount", 0), reverse=True)
    compact_lines = [format_compact_entry(p, rank=i + 1) for i, p in enumerate(sorted_papers)]
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# LLM Landscape Papers (Citation \u2265 {})\n\n".format(min_citations))
        f.write(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*  \n")
        f.write("*Source: Semantic Scholar API and local topic inference \u2014 Computer Science papers only*  \n")
        f.write(f"*Total papers: {len(sorted_papers)}*\n\n")
        counts = _topic_counts(sorted_papers)
        if counts:
            f.write("## Topic Coverage\n\n")
            for topic, count in counts.items():
                f.write(f"- {topic}: {count}\n")
            f.write("\n## Papers\n\n")
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
        "--request-delay", type=float, default=2.0,
        help="Delay between Semantic Scholar requests in seconds (default: 2.0)."
    )
    parser.add_argument(
        "--jitter", type=float, default=0.5,
        help="Random extra delay between requests in seconds (default: 0.5)."
    )
    parser.add_argument(
        "--api-key-env", default="S2_API_KEY",
        help="Environment variable containing a Semantic Scholar API key, if available."
    )
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
    parser.add_argument(
        "--annotate-existing", action="store_true",
        help="Rewrite the existing output with inferred topic tags and coverage without calling the API."
    )
    parser.add_argument(
        "--annotate-source",
        help="Optional markdown source for --annotate-existing; use '-' for stdin or 'git:<rev>:<path>'."
    )
    args = parser.parse_args()

    root_dir = get_repo_root(__file__)
    output_file = args.output or str(root_dir / "section" / "x_llm_papers.md")

    if args.annotate_existing:
        existing_papers = _load_existing_markdown(output_file, args.annotate_source)
        if not existing_papers:
            print(f"No compact paper entries found in: {output_file}")
            return
        _flush_output(output_file, existing_papers, args.min_citations)
        print(f"Annotated {len(existing_papers)} existing papers with inferred topics: {output_file}")
        return

    fetcher = SemanticScholarFetcher(
        user_agent=args.user_agent,
        api_key=os.environ.get(args.api_key_env),
        timeout=args.timeout,
        max_retries=args.max_retries,
        backoff=args.backoff,
        request_delay=args.request_delay,
        jitter=args.jitter,
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

    checkpoint_file = str(Path(output_file).with_suffix(".checkpoint.json"))

    # Load or reset checkpoint
    if args.reset and Path(checkpoint_file).exists():
        Path(checkpoint_file).unlink()
        print("  [reset] Checkpoint deleted.")

    global_papers, global_seen, completed_topics, query_cache, failed_queries = _load_checkpoint(checkpoint_file)

    def persist_progress() -> None:
        _save_checkpoint(checkpoint_file, global_papers, completed_topics, query_cache, failed_queries)

    def merge_papers(papers: List[Dict], topic_name: str) -> int:
        added = 0
        by_id = {paper.get("paperId"): paper for paper in global_papers if paper.get("paperId")}
        for paper in papers:
            pid = paper.get("paperId")
            if not pid:
                continue
            if pid in by_id:
                existing_topics = by_id[pid].get("topics") or []
                by_id[pid]["topics"] = list(dict.fromkeys([*existing_topics, topic_name]))
            elif pid not in global_seen:
                paper["topics"] = list(dict.fromkeys([*(paper.get("topics") or []), topic_name]))
                global_seen.add(pid)
                global_papers.append(paper)
                added += 1
        return added

    # Collect all papers across every topic into a single deduplicated pool
    for topic_name, queries in topics_to_run.items():
        if topic_name in completed_topics:
            print(f"\n[{topic_name}] Already done (skipping).")
            continue

        print(f"\n[{topic_name}] Querying {len(queries)} search term(s)...")
        try:
            papers = fetcher.fetch_topic(
                topic_name,
                queries,
                top_n=args.top_n,
                min_citations=args.min_citations,
                query_cache=query_cache,
                cache_updated=persist_progress,
            )
        except TopicFetchIncomplete as exc:
            added = merge_papers(exc.papers, topic_name)
            failed_queries.extend(exc.failed_queries)
            persist_progress()
            _flush_output(output_file, global_papers, args.min_citations)
            print(
                f"  [pause] {topic_name} incomplete: {len(exc.failed_queries)} failed query/query(s), "
                f"{added} partial paper(s) added. Re-run without --reset to resume."
            )
            return

        added = merge_papers(papers, topic_name)
        completed_topics.append(topic_name)
        failed_queries = []
        print(f"  -> {len(papers)} papers, {added} new (pool size: {len(global_papers)})")

        # Persist progress after every topic so we can resume on interruption
        persist_progress()
        _flush_output(output_file, global_papers, args.min_citations)

    # Final flush (updates timestamp)
    _flush_output(output_file, global_papers, args.min_citations)

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
