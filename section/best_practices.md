# Best Practices and Resources

This file curates blogs (✍️), best practices, architectural guidance, and implementation tips from across all LLM topics.

### **Contents**

- [RAG Best Practices](#rag-best-practices)
  - [The Problem with RAG](#the-problem-with-rag)
  - [RAG Solution Design](#rag-solution-design)
  - [RAG Research](#rag-research)
- [Agent Best Practices](#agent-best-practices)
  - [Agent Design Patterns](#agent-design-patterns)
  - [Tool Use: LLM to Master APIs](#tool-use-llm-to-master-apis)
- [Proposals & Glossary](#proposals--glossary)

## **RAG Best Practices**

### **The Problem with RAG**

- [Seven Failure Points When Engineering a Retrieval Augmented Generation System📑](https://alphaxiv.org/abs/2401.05856): 1. Missing Content, 2. Missed the Top Ranked Documents, 3. Not in Context, 4. Not Extracted, 5. Wrong Format, 6. Incorrect Specificity, 7. Lack of Thorough Testing [11 Jan 2024]
- Solving the core challenges of Retrieval-Augmented Generation [✍️](https://towardsdatascience.com/12-rag-pain-points-and-proposed-solutions-43709939a28c) [Feb 2024] <br/>
  <img src="../files/rag-12-pain-points-solutions.jpg" width="500">
- The Problem with RAG
  - A question is not semantically similar to its answers. Cosine similarity may favor semantically similar texts that do not contain the answer.
  - Semantic similarity gets diluted if the document is too long. Cosine similarity may favor short documents with only the relevant information.
  - The information needs to be contained in one or a few documents. Information that requires aggregations by scanning the whole data.

### **RAG Solution Design**

  - [Advanced RAG with Azure AI Search and LlamaIndex✍️](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/advanced-rag-with-azure-ai-search-and-llamaindex/ba-p/4115007)
  - [Announcing cost-effective RAG at scale with Azure AI Search✍️](https://aka.ms/AAqfqla)
  - [Azure OpenAI chat baseline architecture in an Azure landing zone](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/azure-openai-baseline-landing-zone)
  - [GPT-RAG✨](https://github.com/Azure/GPT-RAG): Enterprise RAG Solution Accelerator [Jun 2023]
![**github stars**](https://img.shields.io/github/stars/Azure/GPT-RAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [bRAG✨](https://github.com/bRAGAI/bRAG-langchain/): Everything you need to know to build your own RAG application [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/bRAGAI/bRAG-langchain?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Evaluating LLMs and RAG Systems✍️](https://dzone.com/articles/evaluating-llms-and-rag-systems): Best Practices for Evaluating LLMs and RAG Systems [27 Jan 2025]
- [From Zero to Hero: Proven Methods to Optimize RAG for Production✍️](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/from-zero-to-hero-proven-methods-to-optimize-rag-for-production/4450040): ColBERT (Token-level embedding), [CoPali](https://huggingface.co/vidore/colpali-v1.2)(Extends ColBERT's multi-vector retrieval and late interaction from text to vision), RAPTOR, HyDE, Re-Ranking and Fusion [Sep 2025]
- [Galileo eBook](https://www.rungalileo.io/mastering-rag): 200 pages content. Mastering RAG. [🗄️](../files/archive/Mastering%20RAG-compressed.pdf) [Sep 2024]
- [Genie: Uber's Gen AI On-Call Copilot✍️](https://www.uber.com/blog/genie-ubers-gen-ai-on-call-copilot/) [10 Oct 2024]
- [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/information-retrieval-book.html): The official website for the classic textbook (free to read online) "Introduction to Information Retrieval" by Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze.
- [Introduction to Large-Scale Similarity Search: HNSW, IVF, LSH✍️](https://blog.gopenai.com/introduction-to-large-scale-similarity-search-part-one-hnsw-ivf-lsh-677bf193ab07) [28 Sep 2024]
- [LangChain RAG from scratch✨](https://github.com/langchain-ai/rag-from-scratch) [📺](https://youtube.com/playlist?list=PLfaIDFEXuae2LXbO1_PKyVJiQ23ZztA0x&feature=shared) [Jan 2024]
![**github stars**](https://img.shields.io/github/stars/langchain-ai/rag-from-scratch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLM Twin Course: Building Your Production-Ready AI Replica✨](https://github.com/decodingml/llm-twin-course): Learn to Build a Production-Ready LLM & RAG System with LLMOps [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/decodingml/llm-twin-course?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LlamIndex Building Performant RAG Applications for Production](https://docs.llamaindex.ai/en/stable/optimizing/production_rag/#building-performant-rag-applications-for-production)
- [Papers with code](https://paperswithcode.com/method/rag): RAG
- [RAG at scale✍️](https://medium.com/@neum_ai/retrieval-augmented-generation-at-scale-building-a-distributed-system-for-synchronizing-and-eaa29162521): Building a distributed system for synchronizing and ingesting billions of text embeddings [28 Sep 2023]
- RAG context relevancy metric: Ragas, TruLens, DeepEval [✍️](https://towardsdatascience.com/the-challenges-of-retrieving-and-evaluating-relevant-context-for-rag-e362f6eaed34) [Jun 2024]
  - `Context Relevancy (in Ragas) = S / Total number of sentences in retrieved context`
  - `Contextual Relevancy (in DeepEval) = Number of Relevant Statements / Total Number of Statements`
- [RAG-driven Generative AI✨](https://github.com/Denis2054/RAG-Driven-Generative-AI): Retrieval Augmented Generation (RAG) code for Generative AI with LlamaIndex, Deep Lake, and Pinecone [Apr 2024] ![**github stars**](https://img.shields.io/github/stars/Denis2054/RAG-Driven-Generative-AI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [What AI Engineers Should Know about Search](https://softwaredoug.com/blog/2024/06/25/what-ai-engineers-need-to-know-search) [25 Jun 2024]

### **RAG Research**

- [A Survey on Retrieval-Augmented Text Generation📑](https://alphaxiv.org/abs/2202.01110): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2202.01110)]: This paper conducts a survey on retrieval-augmented text generation, highlighting its advantages and state-of-the-art performance in many NLP tasks. These tasks include Dialogue response generation, Machine translation, Summarization, Paraphrase generation, Text style transfer, and Data-to-text generation. [2 Feb 2022]
- [Adaptive-RAG📑](https://alphaxiv.org/abs/2403.14403): Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity [✨](https://github.com/starsuzi/Adaptive-RAG) [21 Mar 2024]
 ![**github stars**](https://img.shields.io/github/stars/starsuzi/Adaptive-RAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Active Retrieval Augmented Generation📑](https://alphaxiv.org/abs/2305.06983) : [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.06983)]: Forward-Looking Active REtrieval augmented generation (FLARE): FLARE iteratively generates a temporary next sentence and check whether it contains low-probability tokens. If so, the system retrieves relevant documents and regenerates the sentence. Determine low-probability tokens by `token_logprobs in OpenAI API response`. [✨](https://github.com/jzbjyb/FLARE/blob/main/src/templates.py) [11 May 2023]
- [ARAG📑](https://alphaxiv.org/abs/2506.21931): Agentic Retrieval Augmented Generation for Personalized Recommendation [27 Jun 2025]
- [Astute RAG📑](https://alphaxiv.org/abs/2410.07176): adaptively extracts essential information from LLMs, consolidates internal and external knowledge with source awareness, and finalizes answers based on reliability. [9 Oct 2024]
- [Benchmarking Large Language Models in Retrieval-Augmented Generation📑](https://alphaxiv.org/abs/2309.01431): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.01431)]: Retrieval-Augmented Generation Benchmark (RGB) is proposed to assess LLMs on 4 key abilities [4 Sep 2023]:
  - <details>
    <summary>Expand</summary>

    1. Noise robustness (External documents contain noises, struggled with noise above 80%)  
    1. Negative rejection (External documents are all noises, Highest rejection rate was only 45%)  
    1. Information integration (Difficulty in summarizing across multiple documents, Highest accuracy was 60-67%)  
    1. Counterfactual robustness (Failed to detect factual errors in counterfactual external documents.)  
    </details>
- [CAG: Cache-Augmented Generation📑](https://alphaxiv.org/abs/2412.15605): Preloading Information and Pre-computed KV cache for low latency and minimizing retrieval errors [20 Dec 2024] [✨](https://github.com/hhhuang/CAG) ![**github stars**](https://img.shields.io/github/stars/hhhuang/CAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [CoRAG📑](https://alphaxiv.org/abs/2501.14342): Chain-of-Retrieval Augmented Generation. RAG: single search -> CoRAG: Iterative search and reasoning [24 Jan 2025]
- [Corrective Retrieval Augmented Generation (CRAG)📑](https://alphaxiv.org/abs/2401.15884): Retrieval Evaluator assesses the retrieved documents and categorizes them as Correct, Ambiguous, or Incorrect. For Ambiguous and Incorrect documents, the method uses Web Search to improve the quality of the information. The refined and distilled documents are then used to generate the final output. [29 Jan 2024] CRAG implementation by LangGraph [✨](https://github.com/langchain-ai/langgraph/blob/main/examples/rag/langgraph_crag.ipynb)
- [CRAG: Comprehensive RAG Benchmark📑](https://alphaxiv.org/abs/2406.04744): a factual question answering benchmark of 4,409 question-answer pairs and mock APIs to simulate web and Knowledge Graph (KG) search [✍️](https://www.aicrowd.com/challenges/meta-comprehensive-rag-benchmark-kdd-cup-2024) [7 Jun 2024]
- [Discuss-RAG📑](https://alphaxiv.org/abs/2504.21252): Agent-Led Discussions for Better RAG in Medical QA [30 Apr 2025]
- [FreshLLMs📑](https://alphaxiv.org/abs/2310.03214): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.03214)]: Fresh Prompt, Google search first, then use results in prompt. Our experiments show that FreshPrompt outperforms both competing search engine-augmented prompting methods such as Self-Ask (Press et al., 2022) as well as commercial systems such as Perplexity.AI. [✨](https://github.com/freshllms/freshqa) [5 Oct 2023] ![**github stars**](https://img.shields.io/github/stars/freshllms/freshqa?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Graph Retrieval-Augmented Generation: A Survey📑](https://alphaxiv.org/abs/2408.08921) [15 Aug 2024]
- [HIRAG: Hierarchical-Thought Instruction-Tuning Retrieval-Augmented Generation📑](https://alphaxiv.org/abs/2507.05714): fine-tunes LLMs to learn a three-level hierarchical reasoning process — Filtering: select relevant information; Combination: synthesize across documents; RAG-specific reasoning: infer using retrieved documents plus internal knowledge. [8 Jul 2025]
- [HippoRAG📑](https://alphaxiv.org/abs/2405.14831): RAG + Long-Term Memory (Knowledge Graphs) + Personalized PageRank. [23 May 2024]
- [Hyde📑](https://alphaxiv.org/abs/2212.10496): Hypothetical Document Embeddings. `zero-shot (generate a hypothetical document) -> embedding -> avg vectors -> retrieval` [20 Dec 2022]
- [INTERS: Unlocking the Power of Large Language Models in Search with Instruction Tuning📑](https://alphaxiv.org/abs/2401.06532): INTERS covers 21 search tasks across three categories: query understanding, document understanding, and query-document relationship understanding. The dataset is designed for instruction tuning, a method that fine-tunes LLMs on natural language instructions. [✨](https://github.com/DaoD/INTERS) [12 Jan 2024]
 ![**github stars**](https://img.shields.io/github/stars/DaoD/INTERS?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [OP-RAG: Order-preserve RAG📑](https://alphaxiv.org/abs/2409.01666): Unlike traditional RAG, which sorts retrieved chunks by relevance, we keep them in their original order from the text.  [3 Sep 2024]
- [PlanRAG📑](https://alphaxiv.org/abs/2406.12430): Decision Making. Decision QA benchmark, DQA. Plan -> Retrieve -> Make a decision (PlanRAG) [✨](https://github.com/myeon9h/PlanRAG) [18 Jun 2024]
 ![**github stars**](https://img.shields.io/github/stars/myeon9h/PlanRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [RAG for LLMs📑](https://alphaxiv.org/abs/2312.10997): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2312.10997)] 🏆Retrieval-Augmented Generation for Large Language Models: A Survey: `Three paradigms of RAG Naive RAG > Advanced RAG > Modular RAG` [18 Dec 2023]
- [RAG vs Fine-tuning📑](https://alphaxiv.org/abs/2401.08406): Pipelines, Tradeoffs, and a Case Study on Agriculture. [16 Jan 2024]
- [RARE: Retrieval-Augmented Reasoning Modeling 📑](https://alphaxiv.org/abs/2503.23513): LLM Training from static knowledge storage (memorization) to reasoning-focused. Combining domain knowledge and thinking (Knowledge Remembering & Contextualized Reasoning). 20% increase in accuracy on tasks like PubMedQA and CoVERT. [30 Mar 2025]
- [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval📑](https://alphaxiv.org/abs/2401.18059): Introduce a novel approach to retrieval-augmented language models by constructing a recursive tree structure from documents. [✨](https://github.com/run-llama/llama_index/blob/main/llama-index-packs/llama-index-packs-raptor/README.md) `pip install llama-index-packs-raptor` / [✨](https://github.com/profintegra/raptor-rag) [31 Jan 2024] ![**github stars**](https://img.shields.io/github/stars/profintegra/raptor-rag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [RECOMP: Improving Retrieval-Augmented LMs with Compressors📑](https://alphaxiv.org/abs/2310.04408): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.04408)]: 1. We propose RECOMP (Retrieve, Compress, Prepend), an intermediate step which compresses retrieved documents into a textual summary prior to prepending them to improve retrieval-augmented language models (RALMs). 2. We present two compressors – an `extractive compressor` which selects useful sentences from retrieved documents and an `abstractive compressor` which generates summaries by synthesizing information from multiple documents. 3. Both compressors are trained. [6 Oct 2023]
- [REFRAG: Rethinking RAG based Decoding📑](https://alphaxiv.org/abs/2509.01092): Meta. Compress (chunk → single embedding) → Sense/Select (RL policy picks relevant chunks) → Expand (Selective expansion). 16× Longer Contexts and Up to 31× Faster RAG Decoding. [1 Sep 2025] [✍️](https://x.com/_avichawla/status/1977260787027919209)
- [Retrieval Augmented Generation (RAG) and Beyond📑](https://alphaxiv.org/abs/2409.14924):🏆The paper classifies user queries into four levels—`explicit, implicit, interpretable rationale, and hidden rationale`—and highlights the need for external data integration and fine-tuning LLMs for specialized tasks. [23 Sep 2024]
- [Retrieval Augmented Generation or Long-Context LLMs?📑](https://alphaxiv.org/abs/2407.16833): Long-Context consistently outperforms RAG in terms of average performance. However, RAG's significantly lower cost remains a distinct advantage. [23 Jul 2024]
- [Retrieval meets Long Context LLMs📑](https://alphaxiv.org/abs/2310.03025): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.03025)]: We demonstrate that retrieval-augmentation significantly improves the performance of 4K context LLMs. Perhaps surprisingly, we find this simple retrieval-augmented baseline can perform comparable to 16K long context LLMs. [4 Oct 2023]
- [Retrieval-Augmentation for Long-form Question Answering📑](https://alphaxiv.org/abs/2310.12150): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.12150)]: 1. The order of evidence documents affects the order of generated answers 2. the last sentence of the answer is more likely to be unsupported by evidence. 3. Automatic methods for detecting attribution can achieve reasonable performance, but still lag behind human agreement. `Attribution in the paper assesses how well answers are based on provided evidence and avoid creating non-existent information.` [18 Oct 2023]
- [Searching for Best Practices in Retrieval-Augmented Generation📑](https://alphaxiv.org/abs/2407.01219): `Best Performance Practice`: Query Classification, Hybrid with HyDE (retrieval), monoT5 (reranking), Reverse (repacking), Recomp (summarization). `Balanced Efficiency Practice`: Query Classification, Hybrid (retrieval), TILDEv2 (reranking), Reverse (repacking), Recomp (summarization). [1 Jul 2024]
- [Self-RAG](https://alphaxiv.org/pdf/2310.11511.pdf): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.11511)] 1. `Critic model C`: Generates reflection tokens (IsREL (relevant,irrelevant), IsSUP (fullysupported,partially supported,nosupport), IsUse (is useful: 5,4,3,2,1)). It is pretrained on data labeled by GPT-4. 2. `Generator model M`: The main language model that generates task outputs and reflection tokens. It leverages the data labeled by the critic model during training. 3. `Retriever model R`: Retrieves relevant passages. The LM decides if external passages (retriever) are needed for text generation. [✨](https://github.com/AkariAsai/self-rag) [17 Oct 2023]
 ![**github stars**](https://img.shields.io/github/stars/AkariAsai/self-rag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Sufficient Context: A New Lens on Retrieval Augmented Generation Systems📑](https://alphaxiv.org/abs/2411.06037): Use Gemini 1.5 Pro (1-shot) as a `Sufficient Context AutoRater` to verify if enough context is provided. Larger models perform well with sufficient context but often make wrong guesses when information is missing. Accuracy improves by combining `Model Self-Rated Confidence` with the `Sufficient Context AutoRater`. [9 Nov 2024]
- [The Power of Noise: Redefining Retrieval for RAG Systems📑](https://alphaxiv.org/abs/2401.14887): No more than 2-5 relevant docs + some amount of random noise to the LLM context maximizes the accuracy of the RAG. [26 Jan 2024]
- [Towards AI Search Paradigm📑](https://alphaxiv.org/abs/2506.17188): Baidu. A modular, 4-agent LLM system: master (coordinator), planner (task decomposition), executor (tool use & retrieval), writer (answer synthesis), leveraging DAG for agentic AI search. [20 Jun 2025]
- [UniversalRAG📑](https://alphaxiv.org/abs/2504.20734): A framework for modality-aware routing across image, text, and video. It features granularity-aware routing (e.g., paragraphs, documents for text, video clips) and supports flexible routing methods (zero-shot vs trained). [29 Apr 2025]

## **Agent Best Practices**

- [AIAgentToolkit.xyz](https://www.aiagenttoolkit.xyz): A curated list of AI agent frameworks, launchpads, tools, tutorials, & resources.
- [Agent Leaderboard🤗](https://huggingface.co/spaces/galileo-ai/agent-leaderboard)
- [Agent Leaderboard v2✨](https://github.com/rungalileo/agent-leaderboard) ![**github stars**](https://img.shields.io/github/stars/rungalileo/agent-leaderboard?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **Agent Design Patterns**

- [10 Lessons to Get Started Building AI Agents✨](https://github.com/microsoft/ai-agents-for-beginners): 💡Microsoft. [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [5 Agentic AI Design Patterns✍️](https://blog.dailydoseofds.com/p/5-agentic-ai-design-patterns): Reflection, Tool use, ReAct, Planning, Multi-agent pattern [24 Jan 2025]
- [A Practical Approach for Building Production-Grade Conversational Agents with Workflow Graphs📑](https://alphaxiv.org/abs/2505.23006): 1. DAG-based workflows for e-commerce tasks. 2. A prototype agent generates responses, with human annotations used to build the dataset. 3. Response and loss masking isolate node outputs and losses to prevent conflicts between nodes. [29 May 2025]
- [A Practical Guide to Building AI Agents✍️](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf): 💡OpenAI. [11 Mar 2025]
- [Advances and Challenges in Foundation Agents📑](https://alphaxiv.org/abs/2504.01990):💡From Brain-Inspired Intelligence to Evolutionary, Collaborative, and Safe Systems [✨](https://github.com/FoundationAgents/awesome-foundation-agents) [31 Mar 2025]
- [Agent Factory: The new era of agentic AI—common use cases and design patterns✍️](https://azure.microsoft.com/en-us/blog/agent-factory-the-new-era-of-agentic-ai-common-use-cases-and-design-patterns/):💡Tool use, Reflection, Planning,  Multi-agent, ReAct (Reason + Act) Patterns [13 Aug 2025]
- [Agent-as-a-Judge📑](https://alphaxiv.org/abs/2410.10934): Evaluate Agents with Agents. DevAI, a new benchmark of 55 realistic automated AI development tasks. `Agent-as-a-Judge > LLM-as-a-Judge > Human-as-a-Judge` [14 Oct 2024]
- [AgentBench📑](https://alphaxiv.org/abs/2308.03688) Evaluating LLMs as Agents: Assess LLM-as Agent's reasoning and decision-making abilities. [7 Aug 2023]
- [Agentic AI Architecture Framework for Enterprises ✍️](https://www.infoq.com/articles/agentic-ai-architecture-framework/):💡Tier 1: Foundation: Establishing Controlled Intelligence, Tier 2: Workflow, Tier 3: Autonomous (experimental) [11 Jul 2025]
- [Agentic Architectures for Retrieval-intensive Applications](https://weaviate.io/ebooks/agentic-architectures): Published by Weviate [Mar 2025]
- [Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models📑](https://alphaxiv.org/abs/2510.04618): Agentic Context Engineering (ACE) lets language models self-improve by evolving their contexts without any fine-tuning. [6 Oct 2025]
- [Agentic Design Patterns✍️](https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0#heading=h.pxcur8v2qagu): Google Docs. A Hands-On Guide to Building Intelligent Systems. [🗄️](../files/archive/Agentic_Design_Patterns.docx) [May 2025]
- [Agents](https://huyenchip.com/2025/01/07/agents.html):💡Chip Huyen [7 Jan 2025]
- [Agents Are Not Enough📑](https://alphaxiv.org/abs/2412.16241): Proposes an ecosystem comprising agents (task executors), sims (user preferences and behavior), and assistants (human-in-the-loop). [19 Dec 2024]
- [AI agent orchestration patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns):💡Sequential, Concurrent, Group chat, Handoff, Magentic orchestration [17 Jun 2025]
- [AI Agents That Matter📑](https://alphaxiv.org/abs/2407.01502): AI agent evaluations for optimizing both accuracy and cost. Focusing solely on accuracy can lead to overfitting and high costs. `retry, warming, escalation` [1 Jul 2024]
- [AI Agents vs. Agentic AI📑](https://alphaxiv.org/abs/2505.10468): `TL;DR` AI Agents are tool-like and task-specific; Agentic AI is goal-directed, autonomous, and capable of planning, reacting, and learning. [15 May 2025]
- [Automated Design of Agentic Systems📑](https://alphaxiv.org/abs/2408.08435): Automated Design of Agentic Systems (ADAS), which aims to automatically create powerful agentic system designs, including inventing novel building blocks and/or combining them. [15 Aug 2024]
- [Azure AI Foundry Agent Ochestration Patterns ](https://aifoundry.app/patterns): Prompt Chaining, Routing, Parallelization, Orchestrator, Evaluator-optimizer
- [Beyond the Gang of Four: Practical Design Patterns for Modern AI Systems✍️](https://www.infoq.com/articles/practical-design-patterns-modern-ai-systems/): **Prompting & Context:** Few-Shot Prompting, Role Prompting, Chain-of-Thought, RAG; **Responsible AI:** Output Guardrails, Model Critic; **UX:** Contextual Guidance, Editable Output, Iterative Exploration; **AI-Ops:** Metrics-Driven AI-Ops, Prompt-Model-Config Versioning; **Optimization:** Prompt Caching, Dynamic Batching, Intelligent Model Routing. [15 My 2025]
- [Building effective agents✍️](https://www.anthropic.com/engineering/building-effective-agents):💡Anthrophic. Prompt Chaining, Sequential LLM calls, Routing, Input classification, Parallelization, Concurrent execution, Orchestrator-Workers, Delegation, Evaluator-Optimizer, Feedback loops, Iterative refinement [19 Dec 2024]
- [Cognitive Architectures for Language Agents📑](https://alphaxiv.org/abs/2309.02427): Cognitive Architectures for Language Agents (CoALA). Procedural (how to perform tasks), Semantic (long-term store of knowledge), Episodic Memory (recall specific past events) [✍️](https://blog.langchain.dev/memory-for-agents/) [5 Sep 2023]
- [Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents📑](https://alphaxiv.org/abs/2505.22954): Darwin Gödel Machine (DGM) iteratively self-modifies its code, with improvements validated by SWE-bench and Polyglot. It uses frozen foundation models to enable coding agents that read, write, and execute code via tools. Starting from a single agent, DGM evolves by branching multiple improved agents, boosting SWE-bench scores from 20% to 50% and Polyglot from 14% to 31%. [29 May 2025]
- [Exploring Generative AI (martinfowler.com)](https://martinfowler.com/articles/exploring-gen-ai.html): Memos on how LLMs are being used to enhance software delivery practices, including Toochain, Test-Driven Development (TDD) with GitHub Copilot, pair programming, and multi-file editing. [26 Jul 2023 ~ ]
- Generate the code [✍️](https://www.deeplearning.ai/the-batch/issue-254/) [Jun 2024]
  - [AgentCoder: Multiagent-Code Generation with Iterative Testing and Optimisation📑](https://alphaxiv.org/abs/2312.13010) [20 Dec 2023]
  - [LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step📑](https://alphaxiv.org/abs/2402.16906) [25 Feb 2024]
  - [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering📑](https://alphaxiv.org/abs/2405.15793) [6 May 2024]
- [Generative Agent Simulations of 1,000 People📑](https://alphaxiv.org/abs/2411.10109): a generative agent architecture that simulates more than 1,000 real individuals using two-hour qualitative interviews. 85% accuracy in General Social Survey. [15 Nov 2024]
- [Generative AI Design Patterns for Agentic AI Systems✨](https://github.com/microsoft/azure-genai-design-patterns): Design Patterns for Agentic solutions in Azure [May 2023]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/azure-genai-design-patterns?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Google AI Agents Whitepaper](https://www.kaggle.com/whitepaper-agents) [12 Nov 2024]
- [How Anthropic Built a Multi-Agent Research System✍️](https://blog.bytebytego.com/p/how-anthropic-built-a-multi-agent): Lead Researcher agent to coordinate specialized subagents, enabling dynamic, parallelized research and citation verification [17 Sep 2025]
- [How to write a great agents.md: Lessons from over 2,500 repositories✍️](https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/): How to write effective agents.md files for GitHub Copilot with practical tips [19 Nov 2025]
- [How we built our multi-agent research system✍️](https://www.anthropic.com/engineering/built-multi-agent-research-system): Anthrophic. [13 Jun 2025]
- [Hugging Face Agents Course✨](https://github.com/huggingface/agents-course) 🤗 Hugging Face Agents Course. [Jan 2025]
- [Language Agent Tree Search Method (LATS)✨](https://github.com/lapisrocks/LanguageAgentTreeSearch): LATS leverages an external environment and an MCTS (Monte Carlo Tree Search)-based search [6 Oct 2023] ![**github stars**](https://img.shields.io/github/stars/lapisrocks/LanguageAgentTreeSearch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Solving a Million-Step LLM Task with Zero Errors📑](https://arxiv.org/abs/2511.09030): MDAP framework: MAKER (for Maximal Agentic decomposition, first-to-ahead-by-K Error correction, and Red-flagging) [12 Nov 2025] [✨](https://github.com/mpesce/MDAP) ![**github stars**](https://img.shields.io/github/stars/mpesce/MDAP?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Taxonomy of failure modes in AI agents ✍️](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents): Microsoft AI Red Team (AIRT) has categorized identified failure modes into two types: novel and existing, under the pillars of safety and security. [24 Apr 2025]
- [The Different Ochestration Frameworks](https://newsletter.theaiedge.io/p/implementing-a-language-agent-tree):💡Orchestration frameworks for LLM applications: Micro-orchestration / Macro-orchestration / Agentic Design Frameworks / Optimizer frameworks [11 Oct 2024]
- [The Last Mile Problem: Why Your AI Models Stumble Before the Finish Line](https://solutionsreview.com/data-management/the-last-mile-problem-why-your-ai-models-stumble-before-the-finish-line/): According to Gartner, by 2025, at least 30 percent of GenAI projects will be abandoned after the POC stage. [25 Oct 2024]
- [The Rise and Potential of Large Language Model Based Agents: A Survey📑](https://alphaxiv.org/abs/2309.07864): The papers list for LLM-based agents [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.07864)] / [✨](https://github.com/WooooDyy/LLM-Agent-Paper-List) [14 Sep 2023]
 ![**github stars**](https://img.shields.io/github/stars/WooooDyy/LLM-Agent-Paper-List?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [When One AI Agent Isn't Enough - Building Multi-Agent Systems✍️](https://diamantai.substack.com/p/when-one-ai-agent-isnt-enough-building): When Multi-Agent Systems Make Sense: Complex subtasks, diverse expertise, parallel speed, easy scaling, and multi-entity problems. [Jul 14]
- [Zero to One: Learning Agentic Patterns](https://www.philschmid.de/agentic-pattern):💡Structured `workflows` follow fixed paths, while `agentic patterns` allow autonomous, dynamic decision-making. Sample code using Gemini. [5 May 2025]

### **Reflection, Tool Use, Planning and Multi-agent collaboration**

- Agentic Design Patterns [✍️](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/) [Mar 2024]
  - Reflection: LLM self-evaluates to improve.
    - [Self-Refine📑](https://alphaxiv.org/abs/2303.17651) [30 Mar 2023]
    - [Reflexion📑](https://alphaxiv.org/abs/2303.11366) [20 Mar 2023]
    - [CRITIC📑](https://alphaxiv.org/abs/2305.11738) [19 May 2023]
  - Tool use: LLM uses tools for information gathering, action, or data processing.
    - [Gorilla📑](https://alphaxiv.org/abs/2305.15334) [24 May 2023]
    - [MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action📑](https://alphaxiv.org/abs/2303.11381) [20 Mar 2023]
    - [Efficient Tool Use with Chain-of-Abstraction Reasoning📑](https://alphaxiv.org/abs/2401.17464) [30 Jan 2024]
    - [Executable Code Actions Elicit Better LLM Agents📑](https://alphaxiv.org/abs/2402.01030): CodeAct. Unlike fixed-format outputs such as JSON or text, CodeAct enables LLMs to produce executable Python code as actions. [1 Feb 2024]
  - Planning: LLM devises and executes multistep plans to reach goals.
    - [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models📑](https://alphaxiv.org/abs/2201.11903) [28 Jan 2022]
    - [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face📑](https://alphaxiv.org/abs/2303.17580) [30 Mar 2023]
    - [Understanding the planning of LLM agents: A survey📑](https://alphaxiv.org/abs/2402.02716) [5 Feb 2024]
  - Multi-agent collaboration: Multiple AI agents collaborate for better solutions.
    - [Communicative Agents for Software Development📑](https://alphaxiv.org/abs/2307.07924) [16 Jul 2023]
    - [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation📑](https://alphaxiv.org/abs/2308.08155) [16 Aug 2023]
    - [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework📑](https://alphaxiv.org/abs/2308.00352) [1 Aug 2023]

### **Tool Use: LLM to Master APIs**

- [APIGen📑](https://alphaxiv.org/abs/2406.18518): Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets [26 Jun 2024]
- [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard_live.html) V2 [Aug 2024]
- [Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models📑](https://alphaxiv.org/abs/2304.09842): Different tasks require different tools, and different models show different tool preferences—e.g., ChatGPT favors image captioning, while GPT-4 leans toward knowledge retrieval. [Tool transition](https://chameleon-llm.github.io/) [19 Apr 2023]
- [Gorilla: An API store for LLMs📑](https://alphaxiv.org/abs/2305.15334): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.15334)]: Gorilla: Large Language Model Connected with Massive APIs. 1,645 APIs. [✨](https://github.com/ShishirPatil/gorilla) [24 May 2023] ![**github stars**](https://img.shields.io/github/stars/ShishirPatil/gorilla?style=flat-square&label=%20&color=blue&cacheSeconds=36000)  
  - Used GPT-4 to generate a dataset of instruction-api pairs for fine-tuning Gorilla.  
  - Used the abstract syntax tree (AST) of the generated code to match with APIs in the database and test set for evaluation purposes.  
  > Another user asked how Gorilla compared to LangChain; Patil replied: LangChain is a terrific project that tries to teach agents how to use tools using prompting. Our take on this is that prompting is not scalable if you want to pick between 1000s of APIs. So Gorilla is a LLM that can pick and write the semantically and syntactically correct API for you to call! A drop in replacement into LangChain! [cite✍️](https://www.infoq.com/news/2023/07/microsoft-gorilla/) [04 Jul 2023]  
- [Toolformer📑](https://alphaxiv.org/abs/2302.04761): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2302.04761)]: Language Models That Can Use Tools, by MetaAI. Finetuned GPT-J to learn 5 tools. [✨](https://github.com/lucidrains/toolformer-pytorch) [9 Feb 2023]
 ![**github stars**](https://img.shields.io/github/stars/lucidrains/toolformer-pytorch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [ToolLLM📑](https://alphaxiv.org/abs/2307.16789): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.16789)]: : Facilitating Large Language Models to Master 16000+ Real-world APIs [✨](https://github.com/OpenBMB/ToolBench) [31 Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/OpenBMB/ToolBench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [ToolShed📑](https://alphaxiv.org/abs/2410.14594): Toolshed Knowledge Bases & Advanced RAG-Tool Fusion, optimized for storing and retrieving tools in a vector database for large-scale agents. To address the limitations of primary methods, two approaches are: 1. tuning-based tool calling via LLM fine-tuning, and 2. retriever-based tool selection and planning. [18 Oct 2024]
- [Voyager: An Open-Ended Embodied Agent with Large Language Models📑](https://alphaxiv.org/abs/2305.16291): The 'Skill Library' in Voyager functions like a skill manager, storing and organizing learned behaviors or code snippets that the agent can reuse and combine to solve various tasks in the Minecraft environment. [25 May 2023]

### **Proposals & Glossary**

- [A2A✨](https://github.com/google/A2A): Google. Agent2Agent (A2A) protocol. Agent Card (metadata: self-description). Task (a unit of work). Artifact (output). Streaming (Long-running tasks). Leverages HTTP, SSE, and JSON-RPC. Multi-modality incl. interacting with UI components [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/google/A2A?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Agent Payments Protocol (AP2)✨](https://github.com/google-agentic-commerce/AP2): an open-source protocol developed by Google to enable secure, interoperable AI-driven payments between agents [May 2025] ![**github stars**](https://img.shields.io/github/stars/google-agentic-commerce/AP2?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Agentic Commerce Protocol (ACP)✨](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol): an interaction model and open standard for connecting buyers, their AI agents [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/agentic-commerce-protocol/agentic-commerce-protocol?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Context Engineering: [tweet from Shopify CEO Tobi Lutke](https://x.com/tobi/status/1935533422589399127), [tweet from Andrej Karpathy](https://x.com/karpathy/status/1937902205765607626), [The New Skill in AI is Not Prompting, It's Context Engineering](https://www.philschmid.de/context-engineering) [Jun 2025]
- [AGENTS.md](https://agents.md/): AGENTS.md as a README for agents. [✨](https://github.com/openai/agents.md) [Aug 2025]
- Defensive UX: A design strategy that aims to prevent and handle errors in user interactions with machine learning or LLM-based products. Why defensive UX?: Machine learning and LLMs can produce inaccurate or inconsistent output, which can affect user trust and satisfaction. Defensive UX can help by increasing accessibility, trust, and UX quality.
- [Guidelines for Human-AI Interaction✍️](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/): Microsoft: Based on a survey of 168 potential guidelines from various sources, they narrowed it down to 18 action rules organized by user interaction stages.
- [Human Interface Guidelines for Machine Learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning): Apple: Based on practitioner knowledge and experience, emphasizing aspects of UI rather than model functionality4.
- [/llms.txt](https://llmstxt.org/): Proposal for an `/llms.txt` file to guide LLMs in using websites during inference. [✨](https://github.com/answerdotai/llms-txt) [3 Sep 2024]
 ![**github stars**](https://img.shields.io/github/stars/answerdotai/llms-txt?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Model Context Protocol (MCP)✍️](https://www.anthropic.com/news/model-context-protocol): Anthropic proposes an open protocol for seamless LLM integration with external data and tools. [✨](https://github.com/modelcontextprotocol/servers) [26 Nov 2024]
 ![**github stars**](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
- [People + AI Guidebook](https://pair.withgoogle.com/guidebook/): Google: Google's product teams and academic research, they provide 23 patterns grouped by common questions during the product development process.
- [Spec-Driven Development✨](https://github.com/github/spec-kit): Unlike conventional coding where specs are just guides, it makes specifications executable, directly producing working implementations. [Aug 2025] ![**github stars**](https://img.shields.io/github/stars/github/spec-kit?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [The future of AI agents—and why OAuth must evolve✍️](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/the-future-of-ai-agents%E2%80%94and-why-oauth-must-evolve/3827391): OAuth 2.0 wasn’t built for autonomous AI agents—Microsoft proposes evolving it with agent identities, dynamic permissions, and cross-agent trust. [28 May 2025]
- [Unmetered Intelligence](https://www.zackkass.com/publications): Always-on, unlimited, adaptive intelligence — not bound by usage limits or fixed capacities.
- [Vibe Coding](https://en.wikipedia.org/wiki/Vibe_coding): a method where programmers explain their goals in simple language, and AI creates the code. Suggested by Andrej Karpathy in February 2025, it changes the programmer's role to guiding, testing, and improving the AI's work. [Feb 2025]

