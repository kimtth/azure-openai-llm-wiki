import re

# Process text and add GitHub star badge lines after repository links
# Supports both file input and direct text input

badge_template = "![**github stars**](https://img.shields.io/github/stars/{owner}/{repo}?style=flat-square&label=%20&color=blue&cacheSeconds=36000)"


def add_github_stars(text):
    """
    Add GitHub star badges after lines containing GitHub repository links.
    Returns the modified text and count of added badges.
    """
    link_pattern = re.compile(r"\(https://github\.com/([^/\s]+)/([^/\s)]+)\)")
    existing_badge_pattern = re.compile(r"img\.shields\.io/github/stars/([^/]+)/([^/?\s]+)")
    
    lines = text.strip().split('\n')
    
    # Collect existing badges to avoid duplicates
    existing = set()
    for line in lines:
        for m in existing_badge_pattern.finditer(line):
            existing.add((m.group(1), m.group(2)))
    
    added = 0
    output = []
    seen_repo_for_badge = set(existing)
    
    for line in lines:
        matches = list(link_pattern.finditer(line))
        if not matches:
            output.append(line)
            continue
        
        # Extract candidate repos
        to_add = []
        for m in matches:
            owner, repo = m.group(1), m.group(2)
            repo = repo.rstrip(').')  # Strip trailing punctuation
            key = (owner, repo)
            
            if key in seen_repo_for_badge or not repo:
                continue
            
            to_add.append(key)
        
        # Append badges to the same line
        modified_line = line
        for owner, repo in to_add:
            badge = " " + badge_template.format(owner=owner, repo=repo)
            modified_line += badge
            seen_repo_for_badge.add((owner, repo))
            added += 1
        
        output.append(modified_line)
    
    return '\n'.join(output), added


if __name__ == "__main__":
    # Test with sample text
    test_text = """
- [ ] [Kimi K2 Thinking✍️](https://moonshotai.github.io/Kimi-K2/thinking.html): The first open-source model beats GPT-5 in Agent benchmark. [7 Nov 2025]
- [ ] [GPT 5.1✍️](https://openai.com/index/gpt-5-1/): GPT-5.1 Auto, GPT-5.1 Instant, and GPT-5.1 Thinking. Better instruction-following, More customization for tone and style. [12 Nov 2025]
- [ ] [Nested Learning: A new ML paradigm for continual learning✍️](https://research.google/blog/introducing-nested-learning-a-new-ml-paradigm-for-continual-learning/): A self-modifying architecture. Nested Learning (HOPE) views a model and its training as multiple nested, multi-level optimization problems, each with its own “context flow,” pairing deep optimizers + continuum memory systems for continual, human-like learning. [7 Nov 2025]
- [ ] [PageIndex✨](https://github.com/VectifyAI/PageIndex): a vectorless, reasoning-based RAG system that builds a hierarchical tree index [Apr 2025]
- [ ] [LEANN✨](https://github.com/yichuan-w/LEANN): The smallest vector database. 97% less storage. [Jun 2025]
- [ ] [Memori✨](https://github.com/GibsonAI/Memori): a SQL native memory engine (SQLite, PostgreSQL, MySQL) [Jul 2025]
- [ ] [Grok 4.1✍️](https://x.ai/news/grok-4-1) [17 Nov 2025]
- [ ] [Gemini 3 Pro✍️](https://blog.google/products/gemini/gemini-3/): Deep Think reasoning, Advanced multimodal understanding, spatial reasoning, and agentic capabilities up 30% from 2.5 Pro — reaching 37.5% on Humanity’s Last Exam (41% in Deep Think mode). [18 Nov 2025]
- [ ] [Vibe Hacking✍️](https://www.anthropic.com/news/disrupting-AI-espionage): Anthropic reports vibe-hacking attempts. [14 Nov 2025]
- [ ] [Gemini Memory✍️](https://www.shloked.com/writing/gemini-memory): Gemini uses a structured, typed “user_context” summary with timestamps, accessed only when you explicitly ask. simpler and more unified than ChatGPT or Claude, and it rarely uses data from the Google ecosystem. [19 Nov 2025]
- [ ] [Google Antigravity✍️](https://antigravity.google/): A VSCode‑forked IDE with an artifacts concept, similar to Claude. [18 Nov 2025]
- [ ] [ModelScope-Agent✨](https://github.com/modelscope/ms-agent): Lightweight Framework for Agents with Autonomous Exploration [Aug 2023]
- [ ] [Solving a Million-Step LLM Task with Zero Errors📑](https://arxiv.org/abs/2511.09030): MDAP framework: MAKER (for Maximal Agentic decomposition, first-to-ahead-by-K Error correction, and Red-flagging) [12 Nov 2025] [✨](https://github.com/mpesce/MDAP)
- [ ] [mgrep✨](https://github.com/mixedbread-ai/mgrep): Natural-language based semantic search as grep.
- [ ] [OLMo 3✍️](https://allenai.org/blog/olmo3): Fully open models including the entire flow.
- [ ] https://github.com/rlresearch/DR-Tulu
- [ ] [GPT-5.1 Codex Max✍️](https://openai.com/index/gpt-5-1-codex-max/): agentic coding model for long-running, detailed work. [19 Nov 2025]
- [ ] [Google CodeWiki](https://codewiki.google/): AI-powered documentation platform that automatically transforms any GitHub repository into comprehensive documentation. [13 Nov 2025]
- [ ] [Agent-R1✨](https://github.com/0russwest0/Agent-R1): End-to-End reinforcement learning to train agents in specific environments. [Mar 2025]
- [ ] [Tinker Cookbook✨](https://github.com/thinking-machines-lab/tinker-cookbook): Thinking Machines Lab. Training SDK to fine-tune language models. [Jul 2025]
- [ ] [verl✨](https://github.com/volcengine/verl): ByteDance. RL training library for LLMs [Oct 2024]
- [ ] [RLinf✨](https://github.com/RLinf/RLinf): Post-training foundation models (LLMs, VLMs, VLAs) via reinforcement learning. [Aug 2025]
- [ ] [MineContext✨](https://github.com/volcengine/MineContext): a context-aware AI agent desktop application. [Jun 2025]
- [ ] [NocoBase✨](https://github.com/nocobase/nocobase): Data model-driven. AI-powered no-code platform. [Oct 2020]
- [ ] [PaddleOCR✨](https://github.com/PaddlePaddle/PaddleOCR): Turn any PDF or image document into structured data. [May 2020]
- [ ] [EmbedAnything✨](https://github.com/StarlightSearch/EmbedAnything): Built by Rust. Supports BERT, CLIP, Jina, ColPali, ColBERT, ModernBERT, Reranker, Qwen. Mutilmodality. [Mar 2024]
- [ ] [FalkorDB✨](https://github.com/FalkorDB/FalkorDB): Graph Database. Knowledge Graph for LLM (GraphRAG). OpenCypher (query language in Neo4j). For a sparse matrix, the graph can be queried with linear algebra instead of traversal, boosting performance.  [Jul 2023]
- [ ] [Verbalized Sampling📑](https://arxiv.org/abs/2510.01171): "Generate 5 jokes about coffee and their corresponding probabilities" [1 Oct 2025]
"""
    
    result, count = add_github_stars(test_text)
    print(f"Added {count} GitHub star badge lines.\n")
    print("Result:")
    print("="*80)
    print(result)