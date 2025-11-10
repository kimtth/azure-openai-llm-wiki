# Azure OpenAI + LLM

![GitHub last commit](https://img.shields.io/github/last-commit/kimtth/awesome-azure-openai-llm?label=commit&color=hotpink&style=flat-square)
![Azure OpenAI](https://img.shields.io/badge/llm-azure_openai-blue?style=flat-square)
![GitHub Created At](https://img.shields.io/github/created-at/kimtth/awesome-azure-openai-llm?style=flat-square)

> A comprehensive, curated collection of resources for Azure OpenAI, Large Language Models (LLMs), and their applications.

This repository serves as a comprehensive guide to the rapidly evolving field of LLMs and Azure OpenAI services. Key features:

🔹Concise Summaries: Each resource is briefly described for quick understanding  
🔹Chronological Organization: Resources appended with date (first commit, publication, or paper release)  
🔹Active Tracking: Regular updates to capture the latest developments  

> Note: Some content may become outdated due to the rapid pace of development in this field.

## Quick Navigation

| Application | LLM | Tools |
|------------|-------------------|----------------------|
| [1. RAG Systems](#1rag-systems) | [5. Prompt & Finetuning](#5prompt-engineering-and-finetuning) | [8. AI Tools & Extensions](#8ai-tools-and-extensions) |
| [2. Azure OpenAI](#2azure-openai) | [6. Challenges & Abilities](#6challenges-and-abilities) | [9. Datasets](#9datasets) |
| [3. LLM Applications](#3llm-applications) | [7. LLM Landscape](#7llm-landscape) | [10. Evaluation Methods](#10evaluation-methods) |
| [4. Agent Development](#4agent-development) | [11. Research & Surveys](#11research-and-surveys) | [Frameworks](#semantic-kernel-and-dspy) |

---

## Core Topics

### 1.🎯RAG Systems
Retrieval-Augmented Generation - Enhancing LLMs with External Knowledge

- [RAG Fundamentals](#rag-retrieval-augmented-generation) - Core concepts and implementation strategies
- [RAG Architecture Design](#rag-solution-design) - System design patterns and best practices
- [RAG Applications](#rag-development) - Real-world implementations and use cases
  - [GraphRAG](#graphrag) - Graph-based retrieval approaches
- [Vector Databases](#vector-database-comparison) - Comparison and selection guide

### 2.🌌Azure OpenAI
Microsoft's Cloud-Based AI Platform and Services

- [Azure OpenAI vs OpenAI](#azure-openai-vs-openai) - Azure OpenAI vs OpenAI
- [Microsoft LLM Framework](#microsoft-azure-openai-llm-framework) - Official frameworks and SDKs
- [Microsoft Copilot](#microsoft-copilot) - Copilot products overview
- [Azure AI Services](#azure-ai-search) - Azure AI Search, AI services
- [Microsoft Research](#microsoft-research) - Research publications and findings
- [Reference Architectures](#azure-reference-architectures) - Proven architectural patterns and samples

### 3.🤖LLM Applications
Building Real-World Applications with Large Language Models

- [Development Frameworks](#applications-frameworks-and-user-interface-uiux) - Tools for building LLM applications
- [Application Development](#llm-application-development) - Implementation guides and best practices
  - [Code Development Tools](#code-editor--agent) - AI-powered coding assistants and editors
  - [Memory Systems](#llm-memory) - Persistent memory and context management
- [Performance Optimization](#caching) - Caching strategies and UX improvements
- [Emerging Concepts](#proposals--glossary) - New paradigms like Vibe Coding and Context Engineering
- [Robotics Integration](#llm-for-robotics) - LLMs in robotic systems
- [Demonstration Projects](#awesome-demo) - Inspiring examples and showcases

### 4.🤖Agent Development
Building Autonomous AI Agents and Multi-Agent Systems

- [Design Patterns](#agent-design-patterns) - Proven architectural approaches for agent systems
- [Development Frameworks](#agent-framework) - Tools and libraries for building agents
- [Agent Applications](#agent-application) - Real-world agent implementations
  - [Code Interpreters](#oss-alternatives-for-openai-code-interpreter-aka-advanced-data-analytics) - Open-source alternatives to OpenAI's Code Interpreter
  - [Model Context Protocol](#model-context-protocol-mcp-a2a-computer-use) - MCP, Agent-to-Agent communication, and computer interaction
  - [Research Agents](#deep-research) - AI systems for deep research and analysis

### 5.🧠Prompt Engineering and Finetuning
Optimizing Model Performance and Behavior

- [Prompt Engineering](#prompt-engineering) - Techniques for effective prompt design
- [Model Finetuning](#finetuning) - PEFT (LoRA), RLHF, and supervised fine-tuning
- [Model Optimization](#quantization-techniques) - Quantization and performance optimization
- [Advanced Techniques](#other-techniques-and-llm-patterns) - Mixture of Experts (MoE) and other patterns
- [Visual Prompting](#visual-prompting--visual-grounding) - Working with multimodal inputs

### 6.⚡Challenges and Abilities
Understanding LLM Capabilities and Limitations

- [AGI and Social Impact](#agi-discussion-and-social-impact) - Discussions on artificial general intelligence
- [OpenAI Ecosystem](#openais-roadmap-and-products) - Product roadmaps and strategic direction
- [Technical Constraints](#context-constraints) - Context limitations and solutions (e.g., RoPE)
- [Safety and Security](#trustworthy-safe-and-secure-llm) - Building trustworthy AI systems
- [LLM Capabilities](#large-language-model-is-abilities) - Understanding what LLMs can and cannot do
  - [Reasoning Abilities](#reasoning) - Logical reasoning and problem-solving

### 7.🌍LLM Landscape
Overview of Available Models and Technologies

- [Model Taxonomy](#large-language-models-in-2023) - Classification and comparison of LLMs
- [Model Collection](#large-language-model-collection) - Comprehensive list of available models
- [Domain-Specific Models](#llm-for-domain-specific) - Specialized models for software development and other domains
- [Multimodal Models](#mllm-multimodal-large-language-model) - Models handling text, image, audio, and video

---

## 🏗️Frameworks

### Semantic Kernel and DSPy
Microsoft's Orchestration Framework and Optimization Tools

- [Semantic Kernel](#semantic-kernel) - Microsoft's micro-orchestration framework for AI applications
- [DSPy](#dspy) - Optimizer frameworks for systematic prompt and model optimization

### LangChain and LlamaIndex
Popular Open-Source Frameworks for LLM Applications

- [LangChain Features](#langchain-feature-matrix--cheetsheet) - Comprehensive feature overview and cheat sheets
- [LangChain Agents](#langchain-chain-type-chains--summarizer) - Agent implementations and critical analysis
- [Framework Comparisons](#langchain-vs-competitors) - LangChain vs. alternative frameworks
- [LlamaIndex](#llamaindex) - Micro-orchestration and RAG-focused framework

---

## Tools

### 8.📚AI Tools and Extensions
Practical Tools and Browser Extensions

- [AI Tools & Extensions](#general-ai-tools-and-extensions)

### 9.📊Datasets
Training and Evaluation Data Resources

- [Training Datasets](#datasets-for-llm-training) - High-quality datasets for model training and fine-tuning

### 10.📝Evaluation Methods
Measuring and Improving LLM Performance

- [Evaluation Frameworks](#evaluating-large-language-models) - Methods and metrics for LLM assessment
- [LLMOps](#llmops-large-language-model-operations) - Operations and lifecycle management for LLM systems

---

### 11.🧠Research and Surveys
Comprehensive Surveys and Learning Materials

- [LLM Surveys](#survey-on-large-language-models) - Academic surveys and systematic reviews
- [Business Applications](#business-use-cases) - Industry use cases and implementation strategies
- [Building from Scratch](#build-an-llms-from-scratch-picogpt-and-lit-gpt) - Educational resources for understanding LLM internals
- [Multilingual Resources](#llm-materials-for-east-asian-languages) - LLM resources for Korean, Japanese, and other languages
- [Learning Materials](#learning-and-supplementary-materials) - Tutorials, courses, and supplementary resources

---

## Legend & Notation

| Symbol | Meaning | Symbol | Meaning |
|--------|---------|--------|---------|
| ✍️ | Blog post / Documentation | ✨ | GitHub repository |
| 🗄️ | Archived files | 🔗 | Cross reference |
| 🗣️ | Source citation | 📺 | Video content |
| 🔢 | Citation count | 💡🏆 | Recommend |
| 📑 |  Academic paper | 🤗 | Huggingface |

<!-- 
All rights reserved © `kimtth` 
-->
<!-- 
https://shields.io/badges/git-hub-created-at
-->

**[`^        back to top        ^`](#azure-openai--llm)**

## **RAG (Retrieval-Augmented Generation)**

### **RAG (Retrieval-Augmented Generation)**

- RAG (Retrieval-Augmented Generation) : Integrates the retrieval (searching) into LLM text generation. RAG helps the model to “look up” external information to improve its responses. [✍️](https://towardsdatascience.com/rag-vs-finetuning-which-is-the-best-tool-to-boost-your-llm-application-94654b1eaba7) [25 Aug 2023]

  <!-- <img src="./files/RAG.png" alt="sk" width="400"/> -->

- In a 2020 paper, Meta (Facebook) came up with a framework called retrieval-augmented generation to give LLMs access to information beyond their training data. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks📑](https://alphaxiv.org/abs/2005.11401): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2005.11401)] [22 May 2020]

  1. RAG-sequence — We retrieve k documents, and use them to generate all the output tokens that answer a user query.
  1. RAG-token— We retrieve k documents, use them to generate the next token, then retrieve k more documents, use them to generate the next token, and so on. This means that we could end up retrieving several different sets of documents in the generation of a single answer to a user’s query.
  1. Of the two approaches proposed in the paper, the RAG-sequence implementation is pretty much always used in the industry. It’s cheaper and simpler to run than the alternative, and it produces great results. [✍️](https://towardsdatascience.com/add-your-own-data-to-an-llm-using-retrieval-augmented-generation-rag-b1958bf56a5a) [30 Sep 2023]

### **Research**

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

### **Advanced RAG**

- [9 Effective Techniques To Boost Retrieval Augmented Generation (RAG) Systems✍️](https://towardsdatascience.com/9-effective-techniques-to-boost-retrieval-augmented-generation-rag-systems-210ace375049) [🗄️](9-effective-rag-techniques.png): ReRank, Prompt Compression, Hypothetical Document Embedding (HyDE), Query Rewrite and Expansion, Enhance Data Quality, Optimize Index Structure, Add Metadata, Align Query with Documents, Mixed Retrieval (Hybrid Search) [2 Jan 2024]
- Advanced RAG Patterns: How to improve RAG peformance [✍️](https://cloudatlas.me/why-do-rag-pipelines-fail-advanced-rag-patterns-part1-841faad8b3c2) / [✍️](https://cloudatlas.me/how-to-improve-rag-peformance-advanced-rag-patterns-part2-0c84e2df66e6) [17 Oct 2023]
  1. Data quality: Clean, standardize, deduplicate, segment, annotate, augment, and update data to make it clear, consistent, and context-rich.
  2. Embeddings fine-tuning: Fine-tune embeddings to domain specifics, adjust them according to context, and refresh them periodically to capture evolving semantics.
  3. Retrieval optimization: Refine chunking, embed metadata, use query routing, multi-vector retrieval, re-ranking, hybrid search, recursive retrieval, query engine, [HyDE📑](https://alphaxiv.org/abs/2212.10496) [20 Dec 2022], and vector search algorithms to improve retrieval efficiency and relevance.
  4. Synthesis techniques: Query transformations, prompt templating, prompt conditioning, function calling, and fine-tuning the generator to refine the generation step.
  - HyDE: Implemented in [LangChain: HypotheticalDocumentEmbedder✨](https://github.com/langchain-ai/langchain/blob/master/cookbook/hypothetical_document_embeddings.ipynb). A query generates hypothetical documents, which are then embedded and retrieved to provide the most relevant results. `query -> generate n hypothetical documents -> documents embedding - (avg of embeddings) -> retrieve -> final result.` [✍️](https://www.jiang.jp/posts/20230510_hyde_detailed/index.html)
- [🗣️](https://twitter.com/yi_ding/status/1721728060876300461) [7 Nov 2023] `OpenAI has put together a pretty good roadmap for building a production RAG system.` Naive RAG -> Tune Chunks -> Rerank & Classify -> Prompt Engineering. In `llama_index`... [📺](https://www.youtube.com/watch?v=ahnGLM-RC1Y)  <br/>
  <img src="./files/oai-rag-success-story.jpg" width="500">
- [Contextual Retrieval✍️](https://www.anthropic.com/news/contextual-retrieval): Contextual Retrieval enhances traditional RAG by using Contextual Embeddings and Contextual BM25 to maintain context during retrieval. [19 Sep 2024]
- Demystifying Advanced RAG Pipelines: An LLM-powered advanced RAG pipeline built from scratch [✨](https://github.com/pchunduri6/rag-demystified) [19 Oct 2023]
 ![**github stars**](https://img.shields.io/github/stars/pchunduri6/rag-demystified?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Evaluation with Ragas✍️](https://towardsdatascience.com/visualize-your-rag-data-evaluate-your-retrieval-augmented-generation-system-with-ragas-fc2486308557): UMAP (often used to reduce the dimensionality of embeddings) with Ragas metrics for visualizing RAG results. [Mar 2024] / `Ragas provides metrics`: Context Precision, Context Relevancy, Context Recall, Faithfulness, Answer Relevance, Answer Semantic Similarity, Answer Correctness, Aspect Critique [✨](https://github.com/explodinggradients/ragas) [May 2023]
 ![**github stars**](https://img.shields.io/github/stars/explodinggradients/ragas?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [How to improve RAG Piplines](https://www.linkedin.com/posts/damienbenveniste_how-to-improve-rag-pipelines-activity-7241497046631776256-vwOc?utm_source=li_share&utm_content=feedcontent&utm_medium=g_dt_web&utm_campaign=copy): LangGraph implementation with Self-RAG, Adaptive-RAG, Corrective RAG. [Oct 2024]
- How to optimize RAG pipeline: [Indexing optimization](https://newsletter.theaiedge.io/p/how-to-optimize-your-rag-pipelines) [24 Oct 2023]
- [RAG Hallucination Detection Techniques✍️](https://machinelearningmastery.com/rag-hallucination-detection-techniques/): Hallucination metrics using the DeepEval, G-Eval. [10 Jan 2025] 
- RAG Pipeline: 1. Indexing Stage – prepare knowledge base; 2. Querying Stage – retrieve relevant data; 3. Responding Stage – generate responses [✍️](https://learn.microsoft.com/en-us/azure/machine-learning/concept-retrieval-augmented-generation)

#### Agentic RAG

- [Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG📑](https://alphaxiv.org/abs/2501.09136) [15 Jan 2025]
- From Simple to Advanced RAG (LlamaIndex) [✍️](https://twitter.com/jerryjliu0/status/1711419232314065288) / [🗄️](./files/archive/LlamaIndexTalk_PyDataGlobal.pdf) /💡[✍️](https://aiconference.com/speakers/jerry-liu-2023/) [10 Oct 2023] <br/>
  <img src="./files/advanced-rag.png" width="430">
- [What is Agentic RAG](https://weaviate.io/blog/what-is-agentic-rag): The article published by Weaviate. [5 Nov 2024]

#### Multi-modal RAG (Vision RAG)

- [Azure RAG with Vision Application Framework✨](https://github.com/Azure-Samples/rag-as-a-service-with-vision) [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/rag-as-a-service-with-vision?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Enhancing Ultra High Resolution Remote Sensing Imagery Analysis with ImageRAG📑](https://alphaxiv.org/abs/2411.07688): Ultra High Resolution (UHR) remote sensing imagery, such as satellite imagery and medical imaging. [12 Nov 2024]
- [localGPT-Vision✨](https://github.com/PromtEngineer/localGPT-Vision): an end-to-end vision-based Retrieval-Augmented Generation (RAG) system. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/PromtEngineer/localGPT-Vision?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Multi-Modal RAG System✍️](https://machinelearningmastery.com/implementing-multi-modal-rag-systems/): Building a knowledge base with both image and audio data. [12 Feb 2025]
- [Path-RAG: Knowledge-Guided Key Region Retrieval for Open-ended Pathology Visual Question Answering📑](https://alphaxiv.org/abs/2411.17073): Using HistoCartography to improve pathology image analysis and boost PathVQA-Open performance. [26 Nov 2024]
- [UniversalRAG✨](https://github.com/wgcyeo/UniversalRAG): [🔗](#research) [29 Apr 2025]  ![**github stars**](https://img.shields.io/github/stars/wgcyeo/UniversalRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [VideoRAG📑](https://alphaxiv.org/abs/2501.05874): Not only does it retrieve relevant videos from a large video corpus, but it also integrates both the visual and textual elements of videos into the answer-generation process using Large Video Language Models (LVLMs). [10 Jan 2025]
- [Visual RAG over PDFs with Vespa✍️](https://blog.vespa.ai/visual-rag-in-practice/): a demo showcasing Visual RAG over PDFs using ColPali embeddings in Vespa [✨](https://github.com/vespa-engine/sample-apps/tree/master/visual-retrieval-colpali) [19 Nov 2024]

#### GraphRAG

- [Fast GraphRAG✨](https://github.com/circlemind-ai/fast-graphrag): 6x cost savings compared to `graphrag`, with 20% higher accuracy. Combines PageRank and GraphRAG. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/circlemind-ai/fast-graphrag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Graph RAG (by NebulaGraph)](https://medium.com/@nebulagraph/graph-rag-the-new-llm-stack-with-knowledge-graphs-e1e902c504ed): NebulaGraph proposes the concept of Graph RAG, which is a retrieval enhancement technique based on knowledge graphs. [demo](https://www.nebula-graph.io/demo) [8 Sep 2023]
- [GraphRAG (by Microsoft)📑](https://alphaxiv.org/abs/2404.16130):🏆1. Global search: Original Documents -> Knowledge Graph (Community Summaries generated by LLM) -> Partial Responses -> Final Response. 2. Local Search: Utilizes vector-based search to find the nearest entities and relevant information.
[✍️](https://microsoft.github.io/graphrag) / [✨](https://github.com/microsoft/graphrag) [24 Apr 2024]
![**github stars**](https://img.shields.io/github/stars/microsoft/graphrag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - [DRIFT Search✍️](https://www.microsoft.com/en-us/research/blog/introducing-drift-search-combining-global-and-local-search-methods-to-improve-quality-and-efficiency/): DRIFT search (Dynamic Reasoning and Inference with Flexible Traversal) combines global and local search methods to improve query relevance by generating sub-questions and refining the context using HyDE (Hypothetical Document Embeddings). [31 Oct 2024]
  - ["From Local to Global" GraphRAG with Neo4j and LangChain](https://neo4j.com/developer-blog/global-graphrag-neo4j-langchain/) [09 Jul 2024]
  - [GraphRAG Implementation with LlamaIndex✨](https://github.com/run-llama/llama_index/blob/main/docs/docs/examples/cookbooks/GraphRAG_v1.ipynb) [15 Jul 2024]
  - [Improving global search via dynamic community selection✍️](https://www.microsoft.com/en-us/research/blog/graphrag-improving-global-search-via-dynamic-community-selection/): Dynamic Community Selection narrows the scope by selecting the most relevant communities based on query relevance, utilizing Map-reduce search, reducing costs by 77% without sacrificing output quality [15 Nov 2024]
  - [LazyGraphRAG✍️](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/): Reduces costs to 0.1% of full GraphRAG through efficient use of best-first (vector-based) and breadth-first (global search) retrieval and deferred LLM calls [25 Nov 2024]
  - [LightRAG✨](https://github.com/HKUDS/LightRAG): Utilizing graph structures for text indexing and retrieval processes. [8 Oct 2024] ![**github stars**](https://img.shields.io/github/stars/HKUDS/LightRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - [nano-graphrag✨](https://github.com/gusye1234/nano-graphrag): A simple, easy-to-hack GraphRAG implementation [Jul 2024]
![**github stars**](https://img.shields.io/github/stars/gusye1234/nano-graphrag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Graphiti✨](https://github.com/getzep/graphiti): [🔗](#llm-memory)
- [HippoRAG✨](https://github.com/OSU-NLP-Group/HippoRAG):💡RAG + Knowledge Graphs + Personalized PageRank. [23 May 2024] ![**github stars**](https://img.shields.io/github/stars/OSU-NLP-Group/HippoRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [How to Build a Graph RAG App✍️](https://towardsdatascience.com/how-to-build-a-graph-rag-app-b323fc33ba06): Using knowledge graphs and AI to retrieve, filter, and summarize medical journal articles [30 Dec 2024]
- [HybridRAG📑](https://alphaxiv.org/abs/2408.04948): Integrating VectorRAG and GraphRAG with financial earnings call transcripts in Q&A format. [9 Aug 2024]
- [Neo4j GraphRAG Package for Python✨](https://github.com/neo4j/neo4j-graphrag-python) [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/neo4j/neo4j-graphrag-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **The Problem with RAG**

- [Seven Failure Points When Engineering a Retrieval Augmented Generation System📑](https://alphaxiv.org/abs/2401.05856): 1. Missing Content, 2. Missed the Top Ranked Documents, 3. Not in Context, 4. Not Extracted, 5. Wrong Format, 6. Incorrect Specificity, 7. Lack of Thorough Testing [11 Jan 2024]
- Solving the core challenges of Retrieval-Augmented Generation [✍️](https://towardsdatascience.com/12-rag-pain-points-and-proposed-solutions-43709939a28c) [Feb 2024] <br/>
  <img src="./files/rag-12-pain-points-solutions.jpg" width="500">
- The Problem with RAG
  1. A question is not semantically similar to its answers. Cosine similarity may favor semantically similar texts that do not contain the answer.
  1. Semantic similarity gets diluted if the document is too long. Cosine similarity may favor short documents with only the relevant information.
  1. The information needs to be contained in one or a few documents. Information that requires aggregations by scanning the whole data.

### **RAG Solution Design**

- [5 Chunking Strategies For RAG✍️](https://blog.dailydoseofds.com/p/5-chunking-strategies-for-rag) [19 Oct 2024]
- [8 RAG Architectures for AI Engineers✍️](https://blog.dailydoseofds.com/p/8-rag-architectures-for-ai-engineers) [16 Aug 2025]
- [A Practical Approach to Retrieval Augmented Generation (RAG) Systems✨](https://github.com/mallahyari/rag-ebook): Online book [Dec 2023]
![**github stars**](https://img.shields.io/github/stars/mallahyari/rag-ebook?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Advanced RAG on Hugging Face documentation using LangChain🤗](https://huggingface.co/learn/cookbook/advanced_rag)
- [Advanced RAG Techniques✨](https://github.com/NirDiamant/RAG_Techniques):🏆Showcases various advanced techniques for Retrieval-Augmented Generation (RAG) [Jul 2024]
![**github stars**](https://img.shields.io/github/stars/NirDiamant/RAG_Techniques?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure: Designing and developing a RAG solution](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide)
  - [Advanced RAG with Azure AI Search and LlamaIndex✍️](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/advanced-rag-with-azure-ai-search-and-llamaindex/ba-p/4115007)
  - [Announcing cost-effective RAG at scale with Azure AI Search✍️](https://aka.ms/AAqfqla)
  - [Azure OpenAI chat baseline architecture in an Azure landing zone](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/azure-openai-baseline-landing-zone)
  - Azure Reference Architectures: [🔗](#azure-reference-architectures)
  - [GPT-RAG✨](https://github.com/Azure/GPT-RAG): Enterprise RAG Solution Accelerator [Jun 2023]
![**github stars**](https://img.shields.io/github/stars/Azure/GPT-RAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [bRAG✨](https://github.com/bRAGAI/bRAG-langchain/): Everything you need to know to build your own RAG application [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/bRAGAI/bRAG-langchain?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Evaluating LLMs and RAG Systems✍️](https://dzone.com/articles/evaluating-llms-and-rag-systems): Best Practices for Evaluating LLMs and RAG Systems [27 Jan 2025]
- [From Zero to Hero: Proven Methods to Optimize RAG for Production✍️](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/from-zero-to-hero-proven-methods-to-optimize-rag-for-production/4450040): ColBERT (Token-level embedding), [CoPali](https://huggingface.co/vidore/colpali-v1.2)(Extends ColBERT’s multi-vector retrieval and late interaction from text to vision), RAPTOR, HyDE, Re-Ranking and Fusion [Sep 2025]
- [Galileo eBook](https://www.rungalileo.io/mastering-rag): 200 pages content. Mastering RAG. [🗄️](./files/archive/Mastering%20RAG-compressed.pdf) [Sep 2024]
- [Genie: Uber’s Gen AI On-Call Copilot✍️](https://www.uber.com/blog/genie-ubers-gen-ai-on-call-copilot/) [10 Oct 2024]
- [Introduction to Information Retrieval](https://nlp.stanford.edu/IR-book/information-retrieval-book.html): The official website for the classic textbook (free to read online) “Introduction to Information Retrieval” by Christopher D. Manning, Prabhakar Raghavan, and Hinrich Schütze.
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

### **RAG Development**

1. Applications, Frameworks, and User Interface (UI/UX): [🔗](#applications-frameworks-and-user-interface-uiux)
1. [AutoRAG✨](https://github.com/Marker-Inc-Korea/AutoRAG): RAG AutoML tool for automatically finds an optimal RAG pipeline for your data. [Jan 2024]
![**github stars**](https://img.shields.io/github/stars/Marker-Inc-Korea/AutoRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Canopy✨](https://github.com/pinecone-io/canopy): open-source RAG framework and context engine built on top of the Pinecone vector database. [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/pinecone-io/canopy?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Chonkie✨](https://github.com/SecludedCoder/chonkie): RAG chunking library [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/SecludedCoder/chonkie?style=flat-square&label=%20&color=blue&cacheSeconds=36000) <!--old: https://github.com/chonkie-ai/chonkie -->
1. [Cognita✨](https://github.com/truefoundry/cognita): RAG (Retrieval Augmented Generation) Framework for building modular, open-source applications [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/truefoundry/cognita?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Haystack✨](https://github.com/deepset-ai/haystack): LLM orchestration framework to build customizable, production-ready LLM applications. [5 May 2020] ![**github stars**](https://img.shields.io/github/stars/deepset-ai/haystack?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [llmware✨](https://github.com/llmware-ai/llmware): Building Enterprise RAG Pipelines with Small, Specialized Models [Sep 2023] ![**github stars**](https://img.shields.io/github/stars/llmware-ai/llmware?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MindSearch✨](https://github.com/InternLM/MindSearch): An open-source AI Search Engine Framework [Jul 2024]
![**github stars**](https://img.shields.io/github/stars/InternLM/MindSearch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MiniRAG✨](https://github.com/HKUDS/MiniRAG): RAG through heterogeneous graph indexing and lightweight topology-enhanced retrieval. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/HKUDS/MiniRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Pyversity✨](https://github.com/Pringled/pyversity): A rerank library for search results [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/Pringled/pyversity?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAGApp✨](https://github.com/ragapp/ragapp): Agentic RAG. Custom GPTs, but deployable in your own cloud infrastructure using Docker. [Apr 2024]
![**github stars**](https://img.shields.io/github/stars/ragapp/ragapp?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAG Builder✨](https://github.com/KruxAI/ragbuilder): Automatically create an optimal production-ready Retrieval-Augmented Generation (RAG) setup for your data. [Jun 2024] 
![**github stars**](https://img.shields.io/github/stars/KruxAI/ragbuilder?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAGChecker📑](https://alphaxiv.org/abs/2408.08067): A Fine-grained Framework For Diagnosing RAG [✨](https://github.com/amazon-science/RAGChecker) [15 Aug 2024]
![**github stars**](https://img.shields.io/github/stars/amazon-science/RAGChecker?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAGflow✨](https://github.com/infiniflow/ragflow):💡Streamlined RAG workflow. Focusing on Deep document understanding [Dec 2023] 
![**github stars**](https://img.shields.io/github/stars/infiniflow/ragflow?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAGFoundry✨](https://github.com/IntelLabs/RAGFoundry): A library designed to improve LLMs ability to use external information by fine-tuning models on specially created RAG-augmented datasets. [5 Aug 2024]
![**github stars**](https://img.shields.io/github/stars/IntelLabs/RAGFoundry?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **RAG Application**

1. Applications, Frameworks, and User Interface (UI/UX): [🔗](#applications-frameworks-and-user-interface-uiux)
1. [Danswer✨](https://github.com/danswer-ai/danswer): Ask Questions in natural language and get Answers backed by private sources: Slack, GitHub, Confluence, etc. [Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/danswer-ai/danswer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Fireplexity✨](https://github.com/mendableai/fireplexity): AI search engine by Firecrawl's search API ![**github stars**](https://img.shields.io/github/stars/mendableai/fireplexity?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [Jun 2025]
1. [FlashRAG✨](https://github.com/RUC-NLPIR/FlashRAG): A Python Toolkit for Efficient RAG Research [Mar 2024]
![**github stars**](https://img.shields.io/github/stars/RUC-NLPIR/FlashRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Gemini-Search✨](https://github.com/ammaarreshi/Gemini-Search): Perplexity style AI Search engine clone built with Gemini [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/ammaarreshi/Gemini-Search?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [KAG✨](https://github.com/OpenSPG/KAG): Knowledge Augmented Generation. a logical reasoning and Q&A framework based on the OpenSPG(Semantic-enhanced Programmable Graph). By Ant Group. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/OpenSPG/KAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [kotaemon✨](https://github.com/Cinnamon/kotaemon): Open-source clean & customizable RAG UI for chatting with your documents. [Mar 2024]
![**github stars**](https://img.shields.io/github/stars/Cinnamon/kotaemon?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Khoj✨](https://github.com/khoj-ai/khoj): Open-source, personal AI agents. Cloud or Self-Host, Multiple Interfaces. Python Django based [Aug 2021] ![**github stars**](https://img.shields.io/github/stars/khoj-ai/khoj?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [llm-answer-engine✨](https://github.com/developersdigest/llm-answer-engine): Build a Perplexity-Inspired Answer Engine Using Next.js, Groq, Mixtral, LangChain, OpenAI, Brave & Serper [Mar 2024]
![**github stars**](https://img.shields.io/github/stars/developersdigest/llm-answer-engine?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MedGraphRAG📑](https://alphaxiv.org/abs/2408.04187): MedGraphRAG outperforms the previous SOTA model, [Medprompt📑](https://alphaxiv.org/abs/2311.16452), by 1.1%. [✨](https://github.com/medicinetoken/medical-graph-rag) [8 Aug 2024]
![**github stars**](https://img.shields.io/github/stars/medicinetoken/medical-graph-rag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Meilisearch](https://github.com/meilisearch/meilisearch): A lightning-fast search engine API bringing AI-powered hybrid search to your sites and applications. [Apr 2018] ![**github stars**](https://img.shields.io/github/stars/meilisearch/meilisearch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MemFree✨](https://github.com/memfreeme/memfree): Hybrid AI Search Engine + AI Page Generator. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/memfreeme/memfree?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PaperQA2✨](https://github.com/Future-House/paper-qa): High accuracy RAG for answering questions from scientific documents with citations [Feb 2023]
![**github stars**](https://img.shields.io/github/stars/Future-House/paper-qa?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Perplexica✨](https://github.com/ItzCrazyKns/Perplexica):💡Open source alternative to Perplexity AI [Apr 2024] / [Marqo✨](https://github.com/marqo-ai/marqo) [Aug 2022] / [txtai✨](https://github.com/neuml/txtai) [Aug 2020] / [Typesense✨](https://github.com/typesense/typesense) [Jan 2017] / [Morphic✨](https://github.com/miurla/morphic) [Apr 2024]
 ![**github stars**](https://img.shields.io/github/stars/ItzCrazyKns/Perplexica?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/marqo-ai/marqo?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/neuml/txtai?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/typesense/typesense?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/miurla/morphic?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PrivateGPT✨](https://github.com/imartinez/privateGPT): 100% privately, no data leaks. The API is built using FastAPI and follows OpenAI's API scheme. [May 2023]
![**github stars**](https://img.shields.io/github/stars/imartinez/privateGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [quivr✨](https://github.com/QuivrHQ/quivr): A personal productivity assistant (RAG). Chat with your docs (PDF, CSV, ...) [May 2023]
 ![**github stars**](https://img.shields.io/github/stars/QuivrHQ/quivr?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [R2R (Reason to Retrieve)✨](https://github.com/SciPhi-AI/R2R): Agentic Retrieval-Augmented Generation (RAG) with a RESTful API. [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/SciPhi-AI/R2R?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAG capabilities of LlamaIndex to QA about SEC 10-K & 10-Q documents✨](https://github.com/run-llama/sec-insights): A real world full-stack application using LlamaIndex [Sep 2023]
![**github stars**](https://img.shields.io/github/stars/run-llama/sec-insights?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAG-Anything✨](https://github.com/HKUDS/RAG-Anything): "RAG-Anything: All-in-One RAG System". [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/HKUDS/RAG-Anything?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAGLite✨](https://github.com/superlinear-ai/raglite): a Python toolkit for Retrieval-Augmented Generation (RAG) with PostgreSQL or SQLite [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/superlinear-ai/raglite?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAGxplorer✨](https://github.com/gabrielchua/RAGxplorer): Visualizing document chunks and the queries in the embedding space. [Jan 2024]
![**github stars**](https://img.shields.io/github/stars/gabrielchua/RAGxplorer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Renumics RAG✨](https://github.com/Renumics/renumics-rag): Visualization for a Retrieval-Augmented Generation (RAG) Data [**github stars**](https://img.shields.io/github/stars/Renumics/renumics-rag?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [Jan 2024]
1. [Scira (Formerly MiniPerplx)✨](https://github.com/zaidmukaddam/scira): A minimalistic AI-powered search engine [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/zaidmukaddam/scira?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Semantra✨](https://github.com/freedmand/semantra): Multi-tool for semantic search [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/freedmand/semantra?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Simba✨](https://github.com/GitHamza0206/simba): Portable KMS (knowledge management system) designed to integrate seamlessly with any Retrieval-Augmented Generation (RAG) system [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/GitHamza0206/simba?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [smartrag✨](https://github.com/aymenfurter/smartrag): Deep Research through Multi-Agents, using GraphRAG. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/aymenfurter/smartrag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SWIRL AI Connect✨](https://github.com/swirlai/swirl-search): SWIRL AI Connect enables you to perform Unified Search and bring in a secure AI Co-Pilot. [Apr 2022]
![**github stars**](https://img.shields.io/github/stars/swirlai/swirl-search?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [turboseek✨](https://github.com/Nutlope/turboseek): An AI search engine inspired by Perplexity [May 2024]
![**github stars**](https://img.shields.io/github/stars/Nutlope/turboseek?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Verba✨](https://github.com/weaviate/Verba): Retrieval Augmented Generation (RAG) chatbot powered by Weaviate [Jul 2023]
![**github stars**](https://img.shields.io/github/stars/weaviate/Verba?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [WeKnora✨](https://github.com/Tencent/WeKnora): LLM-powered framework for deep document understanding, semantic retrieval, and context-aware answers using RAG paradigm. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/Tencent/WeKnora?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Xyne✨](https://github.com/xynehq/xyne): an AI-first Search & Answer Engine for work. We’re an OSS alternative to Glean, Gemini and MS Copilot. [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/xynehq/xyne?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **Vector Database Comparison**

- [A Comprehensive Survey on Vector Database📑](https://alphaxiv.org/abs/2310.11703): Categorizes search algorithms by their approach, such as hash-based, tree-based, graph-based, and quantization-based. [18 Oct 2023]
- [A SQLite extension for efficient vector search, based on Faiss!✨](https://github.com/asg017/sqlite-vss) [Jan 2023]
 ![**github stars**](https://img.shields.io/github/stars/asg017/sqlite-vss?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Chroma✨](https://github.com/chroma-core/chroma): Open-source embedding database [Oct 2022]
 ![**github stars**](https://img.shields.io/github/stars/chroma-core/chroma?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Faiss](https://faiss.ai/): Facebook AI Similarity Search (Faiss) is a library for efficient similarity search and clustering of dense vectors. It is used as an alternative to a vector database in the development and library of algorithms for a vector database. It is developed by Facebook AI Research. [✨](https://github.com/facebookresearch/faiss) [Feb 2017]
 ![**github stars**](https://img.shields.io/github/stars/facebookresearch/faiss?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [lancedb✨](https://github.com/lancedb/lancedb): LanceDB's core is written in Rust and is built using Lance, an open-source columnar format.  [Feb 2023] ![**github stars**](https://img.shields.io/github/stars/lancedb/lancedb?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Milvus (A cloud-native vector database) Embedded [✨](https://github.com/milvus-io/milvus) [Sep 2019]: Alternative option to replace PineCone and Redis Search in OSS. It offers support for multiple languages, addresses the limitations of RedisSearch, and provides cloud scalability and high reliability with Kubernetes.
 ![**github stars**](https://img.shields.io/github/stars/milvus-io/milvus?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [MongoDB's GenAI Showcase✨](https://github.com/mongodb-developer/GenAI-Showcase): Step-by-step Jupyter Notebook examples on how to use MongoDB as a vector database, data store, memory provider [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/mongodb-developer/GenAI-Showcase?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Not All Vector Databases Are Made Equal✍️](https://towardsdatascience.com/milvus-pinecone-vespa-weaviate-vald-gsi-what-unites-these-buzz-words-and-what-makes-each-9c65a3bd0696): Printed version for "Medium" limits. [🗄️](./files/vector-dbs.pdf) [2 Oct 2021]
- [pgvector✨](https://github.com/pgvector/pgvector): Open-source vector similarity search for Postgres [Apr 2021] / [pgvectorscale✨](https://github.com/timescale/pgvectorscale): 75% cheaper than pinecone [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/pgvector/pgvector?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/timescale/pgvectorscale?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Pinecone](https://docs.pinecone.io): A fully managed cloud Vector Database. Commercial Product [Jan 2021]
- [Qdrant✨](https://github.com/qdrant/qdrant): Written in Rust. Qdrant (read: quadrant) [May 2020]
 ![**github stars**](https://img.shields.io/github/stars/qdrant/qdrant?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Redis extension for vector search, RedisVL✨](https://github.com/redis/redis-vl-python): Redis Vector Library (RedisVL) [Nov 2022]
 ![**github stars**](https://img.shields.io/github/stars/redis/redis-vl-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [The Semantic Galaxy🤗](https://huggingface.co/spaces/webml-community/semantic-galaxy): Visualize embeddings in 3D space, powered by EmbeddingGemma and Transformers.js [Sep 2025]
- [Weaviate✨](https://github.com/weaviate/weaviate): Store both vectors and data objects. [Jan 2021]
 ![**github stars**](https://img.shields.io/github/stars/weaviate/weaviate?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **Vector Database Options for Azure**

- [Azure Cache for Redis Enterprise✍️](https://techcommunity.microsoft.com/t5/azure-developer-community-blog/introducing-vector-search-similarity-capabilities-in-azure-cache/ba-p/3827512): Enterprise [Redis Vector Search Demo](https://ecommerce.redisventures.com/) [22 May 2023 ]
- [Azure SQL's support for natively storing and querying vectors✍️](https://devblogs.microsoft.com/azure-sql/announcing-eap-native-vector-support-in-azure-sql-database/) [21 May 2024]
- [DiskANN✨](https://github.com/microsoft/DiskANN), a state-of-the-art suite of algorithms for low-latency, highly scalable vector search, is now generally available in [Azure Cosmos DB✍️](https://aka.ms/ignite24/cosmosdb/blog1) and in preview for Azure Database for PostgreSQL. [19 Nov 2024]
- [Exact Nearest Neighbor (ENN)✍️](https://devblogs.microsoft.com/cosmosdb/exact-nearest-neighbor-enn-vector-search/):  vCore-based Azure Cosmos DB for MongoDB. Slower, high accuracy, and designed for small data sets. [1 Apr 2025]
- GraphRAG, available in preview in [Azure Database for PostgreSQL✍️](https://aka.ms/Ignite24/PostgreSQLAI) [19 Nov 2024]
- [Pgvector extension on Azure Cosmos DB for PostgreSQL✍️](https://azure.microsoft.com/en-us/updates/generally-available-pgvector-extension-on-azure-cosmos-db-for-postgresql/): [✍️](https://python.langchain.com/docs/modules/data_connection/vectorstores/integrations/pgvector) [13 Jun 2023]
- [Vector search - Azure AI Search✨](https://github.com/Azure/azure-search-vector-samples): [✍️](https://python.langchain.com/docs/modules/data_connection/vectorstores/integrations/azuresearch) Rebranded from Azure Cognitive Search [Oct 2019] to Azure AI Search [Nov 2023]
 ![**github stars**](https://img.shields.io/github/stars/Azure/azure-search-vector-samples?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Vector Search in Azure Cosmos DB for MongoDB vCore✍️](https://devblogs.microsoft.com/cosmosdb/introducing-vector-search-in-azure-cosmos-db-for-mongodb-vcore/) [23 May 2023]

**Note**: Azure Cache for Redis Enterprise: Enterprise Sku series are not able to deploy by a template such as Bicep and ARM.

[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fkimtth%2Fazure-openai-elastic-vector-langchain%2Fmain%2Finfra%2Fdeployment.json)

#### **Embedding**

- [A Gentle Introduction to Word Embedding and Text Vectorization✍️](https://machinelearningmastery.com/a-gentle-introduction-to-word-embedding-and-text-vectorization/): Word embedding, Text vectorization, One-hot encoding, Bag-of-words, TF-IDF, word2vec, GloVe, FastText. | [Tokenizers in Language Models✍️](https://machinelearningmastery.com/tokenizers-in-language-models/): Stemming, Lemmatization, Byte Pair Encoding (BPE), WordPiece, SentencePiece, Unigram [23 May 2025]
- Azure Open AI Embedding API, `text-embedding-ada-002`, supports 1536 dimensions. Elastic search, Lucene based engine, supports 1024 dimensions as a max. Open search can insert 16,000 dimensions as a vector storage. Open search is available to use as a vector database with Azure Open AI Embedding API.
- [Contextual Document Embedding (CDE)📑](https://alphaxiv.org/abs/2410.02525): Improve document retrieval by embedding both queries and documents within the context of the broader document corpus. [✍️](https://pub.aimind.so/unlocking-the-power-of-contextual-document-embeddings-enhancing-search-relevance-01abfa814c76) [3 Oct 2024]
- [Contextualized Chunk Embedding Model✍️](https://blog.voyageai.com/2025/07/23/voyage-context-3/): Rather than embedding each chunk separately, a contextualized chunk embedding model uses the whole document to create chunk embeddings that reflect the document’s overall context. [✍️](https://blog.dailydoseofds.com/p/contextualized-chunk-embedding-model) [23 Jul 2025]
- [Embedding Atlas✨](https://github.com/apple/embedding-atlas): Apple. a tool that provides interactive visualizations for large embeddings. [May 2025]
- [Fine-tuning Embeddings for Specific Domains✍️](https://blog.gopenai.com/fine-tuning-embeddings-for-specific-domains-a-comprehensive-guide-5e4298b42185): The guide discusses fine-tuning embeddings for domain-specific tasks using `sentence-transformers` [1 Oct 2024]
- However, one exception to this is that the maximum dimension count for the Lucene engine is 1,024, compared with
  16,000 for the other engines. [✍️](https://opensearch.org/docs/latest/search-plugins/knn/approximate-knn/)
- [Is Cosine-Similarity of Embeddings Really About Similarity?📑](https://alphaxiv.org/abs/2403.05440): Regularization in linear matrix factorization can distort cosine similarity. L2-norm regularization on (1) the product of matrices (like dropout) and (2) individual matrices (like weight decay) may lead to arbitrary similarities.  [8 Mar 2024]
- OpenAI Embedding models: `text-embedding-3` [🔗](#openai-products) > `New embedding models`
- [text-embedding-ada-002✍️](https://openai.com/blog/new-and-improved-embedding-model):
  Smaller embedding size. The new embeddings have only 1536 dimensions, one-eighth the size of davinci-001 embeddings,
  making the new embeddings more cost effective in working with vector databases. [15 Dec 2022]
- [Vector Search with OpenAI Embeddings: Lucene Is All You Need📑](https://alphaxiv.org/abs/2308.14963): For vector search applications, Lucene’s HNSW implementation is a resilient and extensible solution with performance comparable to specialized vector databases like FAISS. Our experiments used Lucene 9.5.0, which limits vectors to 1024 dimensions—insufficient for OpenAI’s 1536-dimensional embeddings. A fix to make vector dimensions configurable per codec has been merged to Lucene’s source [here✨](https://github.com/apache/lucene/pull/12436) but was not yet released as of August 2023. [29 Aug 2023]



## **Azure OpenAI and Reference Architecture**

### **Azure OpenAI vs OpenAI**

1. OpenAI offers the latest features and models, while Azure OpenAI provides a reliable, secure, and compliant environment with seamless integration into other Azure services.
2. Azure OpenAI supports `private networking`, `role-based authentication`, and `responsible AI content filtering`.
3. Azure OpenAI does not use user input as training data for other customers. [Data, privacy, and security for Azure OpenAI✍️](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy). Azure OpenAI does not share user data, including prompts and responses, with OpenAI.

- [What is Azure OpenAI Service?✍️](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview)
- [Azure OpenAI Models](https://ai.azure.com/explore/models) | [Open AI Models](https://platform.openai.com/docs/models)
- [Abuse Monitoring✍️](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy): To detect and mitigate abuse, Azure OpenAI stores all prompts and generated content securely for up to thirty (30) days. (No prompts or completions are stored if the customer chooses to turn off abuse monitoring.)
- 🏆[Data Science Toolkit](https://www.ds-toolkit.com/)
- 🏆`github organizations`: 🌐[Azure](https://github.com/Azure) | 🏬[Azure-samples](https://github.com/Azure-Samples) | 🏛️[Microsoft](https://github.com/Microsoft) | 👥[MSUSAzureAccelerators](https://github.com/MSUSAzureAccelerators)

### **Microsoft Azure OpenAI LLM Framework**

#### LLM Integration Frameworks

1. [Artificial Intelligence Controller Interface (AICI)✨](https://github.com/microsoft/aici): a framework that enhances real-time control of Large Language Model outputs using secure, sandboxed controllers written in various languages like Rust and Python. [Sep 2023] ![**github stars**](https://img.shields.io/github/stars/microsoft/aici?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Azure ML Prompt Flow✍️](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/overview-what-is-prompt-flow) (Jun 2023): A visual designer for prompt crafting using Jinja as a prompt template language. / [✍️](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/harness-the-power-of-large-language-models-with-azure-machine/ba-p/3828459) / [✨](https://github.com/microsoft/promptflow)
 ![**github stars**](https://img.shields.io/github/stars/microsoft/promptflow?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Kernel Memory✨](https://github.com/microsoft/kernel-memory) (Jul 2023): An open-source service and plugin for efficient dataset indexing through custom continuous data hybrid pipelines.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/kernel-memory?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Microsoft Agent Framework✨](https://github.com/microsoft/agent-framework):🏆Unified SDK (Semantic Kernel & AutoGen), Graph-based Workflows, DevUI, Built-in connectors, MCP + A2A + OpenAPI [Apr 2025] / [Blog✍️](https://devblogs.microsoft.com/foundry/introducing-microsoft-agent-framework-the-open-source-engine-for-agentic-ai-apps/) ![**github stars**](https://img.shields.io/github/stars/microsoft/agent-framework?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Semantic Kernel✍️](https://devblogs.microsoft.com/semantic-kernel/) (Feb 2023): An open-source SDK for integrating AI services like OpenAI, Azure OpenAI, and Hugging Face with conventional programming languages such as C# and Python. It's an LLM orchestrator, similar to LangChain. / [✨](https://github.com/microsoft/semantic-kernel) / [🔗](#semantic-kernel)
 ![**github stars**](https://img.shields.io/github/stars/microsoft/semantic-kernel?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

- A Memory in Semantic Kernel vs Kernel Memory (formerly Semantic Memory) is designed to handle large datasets and extended conversations, with the memory pipeline deployed as a separate service. [✨](https://github.com/microsoft/chat-copilot/tree/main/memorypipeline)

#### Prompt

1. [GenAIScript✨](https://github.com/microsoft/genaiscript) (Aug 2023): Orchestrate LLMs, tools, and data in a single JavaScript. ![**github stars**](https://img.shields.io/github/stars/microsoft/genaiscript?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [guidance✨](https://github.com/microsoft/guidance) (Nov 2022): A domain-specific language (DSL) for controlling large language models, focusing on model interaction and implementing the "Chain of Thought" technique.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/guidance?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LMOps✨](https://github.com/microsoft/LMOps) (Dec 2022): A toolkit for improving text prompts used in generative AI models, including tools like Promptist for text-to-image generation and Structured Prompting.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/LMOps?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LLMLingua✨](https://github.com/microsoft/LLMLingua) (Jul 2023): A tool for compressing prompts and KV-Cache, achieving up to 20x compression with minimal performance loss. LLMLingua-2 was released in Mar 2024.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/LLMLingua?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Prompty✨](https://github.com/microsoft/prompty) (Apr 2024): A template language for integrating prompts with LLMs and frameworks, enhancing prompt management and evaluation.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/prompty?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PromptBench✨](https://github.com/microsoft/promptbench) (Jun 2023): A unified evaluation framework for large language models.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/promptbench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Prompt Engine✨](https://github.com/microsoft/prompt-engine) (Jun 2022): A tool for crafting prompts for large language models in Python. / [Python✨](https://github.com/microsoft/prompt-engine-py)
 ![**github stars**](https://img.shields.io/github/stars/microsoft/prompt-engine?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/microsoft/prompt-engine-py?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SAMMO✨](https://github.com/microsoft/sammo) (Apr 2024): A general-purpose framework for prompt optimization. / [✍️](https://www.microsoft.com/en-us/research/blog/sammo-a-general-purpose-framework-for-prompt-optimization/)
 ![**github stars**](https://img.shields.io/github/stars/microsoft/sammo?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [TypeChat](https://microsoft.github.io/TypeChat/blog/introducing-typechat) (Apr 2023): A tool that replaces prompt engineering with schema engineering, designed to build natural language interfaces using types. / [✨](https://github.com/microsoft/Typechat)
 ![**github stars**](https://img.shields.io/github/stars/microsoft/Typechat?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### Agent

1. [Agent Lightning✍️](https://github.com/microsoft/agent-lightning): Train and optimize agents (including RL, prompt‑optimization, multi‑agent workflows) [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/microsoft/agent-lightning?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AIOpsLab✍️](https://www.microsoft.com/en-us/research/blog/aiopslab-building-ai-agents-for-autonomous-clouds/): Building AI agents for autonomous clouds. AI agents for incident root cause analysis (RCA) [✨](https://github.com/microsoft/AIOpsLab/
) [20 Dec 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/AIOpsLab?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Autogen✨](https://github.com/microsoft/autogen) (Mar 2023): A customizable and conversable agent framework. / [✍️](https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-generation-large-language-model-applications/) / [Autogen Studio✍️](https://www.microsoft.com/en-us/research/blog/introducing-autogen-studio-a-low-code-interface-for-building-multi-agent-workflows/) (June 2024) ![**github stars**](https://img.shields.io/github/stars/microsoft/autogen?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
    - **Autogen** has two variants: **Community-driven (AG2)** — available via `pyautogen` (or its aliases `autogen` or `ag2`) [ag2✨](https://github.com/ag2ai/ag2) ![**github stars**](https://img.shields.io/github/stars/ag2ai/ag2?style=flat-square\&label=%20\&color=blue\&cacheSeconds=36000) **Microsoft-driven (autogen)** — from v0.4, install using `pip install autogen-agentchat`
1. [ExACT✨](https://github.com/microsoft/ExACT): An open-source project enabling agents to learn from past interactions and improve search efficiency dynamically. Monte Carlo Tree Search (MCTS). ![**github stars**](https://img.shields.io/github/stars/microsoft/ExACT?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [Dec 2024]
1. [JARVIS✨](https://github.com/microsoft/JARVIS) (Mar 2023): An interface for LLMs to connect numerous AI models for solving complex AI tasks.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/JARVIS?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Magentic-One✍️](https://aka.ms/magentic-one): Built on AutoGen. A Generalist Multi-Agent System for Solving Complex Tasks [Nov 2024]
1. [OmniParser✨](https://github.com/microsoft/OmniParser) (Sep 2024): A simple screen parsing tool towards pure vision based GUI agent.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/OmniParser?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [qlib✨](https://github.com/microsoft/qlib): Qlib is an AI-driven quantitative investment platform that supports diverse machine learning models—from research to production—including supervised learning, market dynamics, and reinforcement learning. [Aug 2020] ![**github stars**](https://img.shields.io/github/stars/microsoft/qlib?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RD-Agent✨](https://github.com/microsoft/RD-Agent): open source R&D automation tool [✍️](https://rdagent.azurewebsites.net/) [Apr 2024]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/RD-Agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Semantic Workbench✨](https://github.com/microsoft/semanticworkbench) (Aug 2024): A development tool for creating intelligent agents. / [✍️](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/introducing-semantic-workbench-your-gateway-to-agentic-ai/ba-p/4212695)
 ![**github stars**](https://img.shields.io/github/stars/microsoft/semanticworkbench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [TaskWeaver✨](https://github.com/microsoft/TaskWeaver) (Sep 2023): A code-first agent framework for converting natural language requests into executable code with support for rich data structures and domain-adapted planning.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/TaskWeaver?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [TinyTroupe✨](https://github.com/microsoft/TinyTroupe): LLM-powered multiagent persona simulation for imagination enhancement and business insights. [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/TinyTroupe?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [UFO✨](https://github.com/microsoft/UFO) (Mar 2024): A UI-focused agent for Windows OS interaction.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/UFO?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Vanilla AI Agents✨](https://github.com/Azure-Samples/vanilla-aiagents): Lightweight library demonstrating how to create agenting application without using any specific framework. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/vanilla-aiagents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Windows Agent Arena (WAA)✨](https://github.com/microsoft/WindowsAgentArena): a scalable Windows AI agent platform for testing and benchmarking multi-modal, desktop AI agents. [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/WindowsAgentArena?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

- [Understanding Microsoft's Latest Multi-Agent Systems✍️](https://techcommunity.microsoft.com/blog/machinelearningblog/the-evolution-of-ai-frameworks-understanding-microsofts-latest-multi-agent-syste/4339739): AutoGen 0.4 vs Magentic-One vs and TinyTroupe [27 Nov 2024]

#### Deep learning

1. [BitNet✨](https://github.com/microsoft/BitNet): Official inference framework for 1-bit LLMs [Aug 2024]
![**github stars**](https://img.shields.io/github/stars/microsoft/BitNet?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DeepSpeed✨](https://github.com/microsoft/DeepSpeed) (May 2020): A deep learning optimization library for easy, efficient, and effective distributed training and inference, featuring the Zero Redundancy Optimizer.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/DeepSpeed?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [FLAML✨](https://github.com/microsoft/FLAML) (Dec 2020): A lightweight Python library for efficient automation of machine learning and AI operations, offering interfaces for AutoGen, AutoML, and hyperparameter tuning.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/FLAML?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Foundation Models (aka large-scale pre-trained models)✨](https://github.com/microsoft/unilm): Foundation Models & Foundation Architectures [Mar 2020]

#### Risk Identification & LLMOPs

1. [AI Central✨](https://github.com/microsoft/AICentral) (Oct 2023): An AI Control Center for monitoring, authenticating, and providing resilient access to multiple OpenAI services.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/AICentral?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Azure AI Evaluation SDK✍️](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/develop/evaluate-sdk) (Oct 2024): Evaluate with the prompt flow SDK has been retired and replaced with Azure AI Evaluation SDK.
1. [PyRIT✨](https://github.com/Azure/PyRIT) (Dec 2023): Python Risk Identification Tool for generative AI, focusing on LLM robustness against issues like hallucination, bias, and harassment.
 ![**github stars**](https://img.shields.io/github/stars/Azure/PyRIT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### Data processing

- [markitdown✨](https://github.com/microsoft/markitdown):💡Python tool for converting files and office documents to Markdown. [14 Nov 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/markitdown?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Microsoft Fabric✍️](https://learn.microsoft.com/en-us/fabric/): Fabric integrates technologies like Azure Data Factory, Azure Synapse Analytics, and Power BI into a single unified product [May 2023]
- [NLWeb✨](https://github.com/microsoft/NLWeb):💡Conversational Interfaces for the Web. Support MCP, Schema.org, and RSS. [📺](https://youtu.be/EF6uywH-Yzo) [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/microsoft/NLWeb?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Presidio✨](https://github.com/microsoft/presidio): Presidio (Origin from Latin praesidium ‘protection, garrison’). Context aware, pluggable and customizable data protection and de-identification SDK for text and images. [Oct 2019]

#### Dev Toolkit

- [Data Formulator✨](https://github.com/microsoft/data-formulator): Create Rich Visualizations with AI [28 Aug 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/data-formulator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Document: AI Toolkit for Visual Studio Code✨](https://github.com/microsoft/vscode-ai-toolkit): AI Toolkit for Visual Studio Code extension [Dec 2023] ![**github stars**](https://img.shields.io/github/stars/microsoft/vscode-ai-toolkit?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Github Copilot Chat extension for VS Code✨](https://github.com/microsoft/vscode-copilot-chat):💡Copilot Chat extension for VS Code [June 2025] ![**github stars**](https://img.shields.io/github/stars/microsoft/vscode-copilot-chat?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Powershell: AIShell✨](https://github.com/PowerShell/AIShell): An interactive shell to work with AI-powered assistance providers [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/PowerShell/AIShell?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **Microsoft Copilot**

#### **Copilot Products**

- [An AI companion for everyone✍️](https://blogs.microsoft.com/blog/2024/10/01/an-ai-companion-for-everyone/): Copilot’s next phase (Copilot Voice, Copilot Daily, Copilot Vision, CoT, and others.) [1 Oct 2024]
- [Copilot Scenario Library](https://adoption.microsoft.com/en-us/copilot-scenario-library/)
- [Copilot Vision✍️](https://www.microsoft.com/en-us/microsoft-copilot/blog/2024/12/05/copilot-vision-now-in-preview-a-new-way-to-browse/): Available only on Microsoft Edge: See the page, read along, and solve problems together. [05 Dec 2024]
- `Microsoft Copilot in Windows` vs `Microsoft Copilot` (= Copilot in Windows + Bing + Commercial Data Protection; formerly Bing Chat) vs `Microsoft 365 Copilot` (= Microsoft Copilot + Microsoft 365 Integration) [Nov 2023]
- [Microsoft 365 Copilot Chat✍️](https://aka.ms/copilotchat): Chat experience (Free tier) + Pay-as-you-go agents [15 Jan 2025]
- [Microsoft 365 Copilot Wave 2 Spring✍️](https://www.microsoft.com/en-us/microsoft-365/blog/2025/04/23/microsoft-365-copilot-built-for-the-era-of-human-agent-collaboration/): Researcher and Analyst agent, Copilot Notebooks, Copilot Search, Copilot Control System, Memory and personalization, Create, Skills agent [23 Apr 2025]
- **Azure**
  - [Copilot in Azure Quantum✍️](https://learn.microsoft.com/en-us/azure/quantum/get-started-azure-quantum) [June 2023]
  - [Microsoft Copilot for Azure✍️](https://learn.microsoft.com/en-us/azure/copilot) / [✍️](https://techcommunity.microsoft.com/t5/azure-infrastructure-blog/simplify-it-management-with-microsoft-copilot-for-azure-save/ba-p/3981106) [Nov 2023]
  - [Security Copilot✍️](https://learn.microsoft.com/en-us/security-copilot/microsoft-security-copilot) / [✍️](https://blogs.microsoft.com/blog/2023/03/28/introducing-microsoft-security-copilot-empowering-defenders-at-the-speed-of-ai/) [March 2023]
- **Microsoft 365 (Incl. Dynamics 365 and Power Platform)**
  - [Copilot Pages✍️](https://techcommunity.microsoft.com/en-us/microsoft-365-copilot/announcing-copilot-pages-for-multiplayer-collaboration/ba-p/4242701): Copilot Pages is a dynamic, persistent canvas in Copilot chat designed for multiplayer AI collaboration [16 Sep 2024]
  - [Copilot Pro✍️](https://support.microsoft.com/en-us/copilot-pro): Copilot Pro offers all the features of Copilot, plus faster responses, priority access to advanced models, personalized GPTs, integration with Microsoft 365 apps, and enhanced AI image creation. [Jan 2024]
  - Copilot in Power Platform: [Power App AI Copilot✍️](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/ai-overview) [March 2023] / [Power Automate✍️](https://powerautomate.microsoft.com/en-us/blog/copilot-in-power-automate-new-time-saving-experiences-announced-at-microsoft-ignite-2023/): [Copilot in cloud flows✍️](https://learn.microsoft.com/en-us/power-automate/get-started-with-copilot), [Copilot in Process Mining ingestion✍️](https://learn.microsoft.com/en-us/power-automate/process-mining-copilot-in-ingestion), [Copilot in Power Automate for desktop✍️](https://learn.microsoft.com/en-us/power-automate/desktop-flows/copilot-in-power-automate-for-desktop) ... [Nov 2023]
  - [Dynamics 365 Copilot✍️](https://learn.microsoft.com/en-us/microsoft-cloud/dev/copilot/copilot-for-dynamics365) / [✍️](https://blogs.microsoft.com/blog/2023/03/06/introducing-microsoft-dynamics-365-copilot/) [March 2023]
    - [10 new autonomous agents in Microsoft Dynamics 365✍️](https://www.microsoft.com/en-us/dynamics-365/blog/business-leader/2024/10/21/transform-work-with-autonomous-agents-across-your-business-processes/) [21 Oct 2024] | [Sales Copilot✍️](https://learn.microsoft.com/en-us/microsoft-sales-copilot) | [Service Copilot](https://cloudblogs.microsoft.com/dynamics365/it/2023/11/15/announcing-microsoft-copilot-for-service/)
  - [Microsoft 365 Copilot✍️](https://learn.microsoft.com/en-us/microsoft-365-copilot/microsoft-365-copilot-overview) / [✍️](https://blogs.microsoft.com/blog/2023/03/16/introducing-microsoft-365-copilot-your-copilot-for-work/) [Nov 2023]
  - Microsoft Fabric and Power BI: [✍️](https://powerbi.microsoft.com/en-us/blog/empower-power-bi-users-with-microsoft-fabric-and-copilot/) / [Fabric Copilot✍️](https://learn.microsoft.com/en-us/fabric/get-started/copilot-fabric-overview) / [PowerBI Copilot✍️](https://learn.microsoft.com/en-us/power-bi/create-reports/copilot-introduction) [March 2024]
  - Microsoft Viva Copilot [✍️](https://www.microsoft.com/en-us/microsoft-365/blog/2023/04/20/introducing-copilot-in-microsoft-viva-a-new-way-to-boost-employee-engagement-and-performance/) [April 2023]
  - [Team Copilot✍️](https://www.microsoft.com/en-us/microsoft-365/blog/2024/05/21/new-agent-capabilities-in-microsoft-copilot-unlock-business-value/): Act as a valuable team member (Meeting facilitator, Group collaborator, Project manager) [May 2024]
- **Windows, Bing and so on**
  - [Copilot+ PC✍️](https://blogs.microsoft.com/blog/2024/05/20/introducing-copilot-pcs/): AI-powered and NPU-equipped Windows PCs [May 2024]
  - [Github Copilot](https://docs.github.com/en/copilot/getting-started-with-github-copilot) [Oct 2021]
  - [Microsoft Clarity Copilot✍️](https://learn.microsoft.com/en-us/clarity/copilot/clarity-copilot): [✍️](https://clarity.microsoft.com/blog/clarity-copilot/) [March 2023]
  - [Microsoft Copilot](https://copilot.microsoft.com/): FKA. Bing Chat Enterprise [Nov 2023]
  - [Microsoft Copilot in Windows✍️](https://learn.microsoft.com/en-us/copilot/copilot) [Sep 2023]
  - [Nuance DAX Copilot](https://www.nuance.com/healthcare/dragon-ai-clinical-solutions/dax-copilot.html): AI assistant for automated clinical documentation [18 Jan 2024]
  - [Windows Copilot Runtime✍️](https://blogs.windows.com/windowsdeveloper/2024/05/21/unlock-a-new-era-of-innovation-with-windows-copilot-runtime-and-copilot-pcs/): The set of APIs powered by the 40+ on-device models, a new layer of Windows. [May 2024] -> [Windows AI Foundry✍️](https://developer.microsoft.com/en-us/windows/ai/): an evolution of Windows Copilot Runtime, a platform to streamline AI development on Windows. [May 2025]
- [Build 2025✍️](https://news.microsoft.com/build-2025-book-of-news/): Advancements in AI agents, Azure AI Foundry, Microsoft 365 Copilot APIs, MCP in Copilot Studio &  Dynamics 365, GitHub Copilot, Cosmos DB in Microsoft Fabric, and new capabilities in Windows for AI development. [May 2025]

#### **Agent Development**

1. [AI Agents for Beginners - A Course✨](https://github.com/microsoft/ai-agents-for-beginners): 10 Lessons to Get Started Building AI Agents [Jan 2025]
1. [Agents in Power Platform✍️](https://www.microsoft.com/en-us/power-platform/blog/2024/11/19/redefine-development-ai-first-innovation-with-agents-and-microsoft-copilot-in-power-platform/) [19 Nov 2024]
1. [Agent builder & Plan designer in Power Apps✍️](https://www.microsoft.com/en-us/power-platform/blog/power-apps/build-user-focused-intelligent-solutions-in-power-apps-start-with-a-plan/)
1. [Combine Copilot Agents with Office Add-ins✍️](https://devblogs.microsoft.com/microsoft365dev/office-addins-at-build-2025/): Developers can now enhance Copilot with Office add-in actions for natural language interaction with Office documents. [22 May 2025]
1. From Bots to Agents: The Evolution of Copilot Development [4 Jun 2025]  
    <img src="./files/ms-bot-agent.png" alt="bot2agent" width="600"/>
1. [Introducing Copilot Actions, new agents, Copilot Control System✍️](https://www.microsoft.com/en-us/microsoft-365/blog/2024/11/19/introducing-copilot-actions-new-agents-and-tools-to-empower-it-teams/)
    - Employee Self-Service Agent: Automates HR/IT tasks (in private preview).
    - Facilitator Agent: Summarizes meetings and takes notes, helping teams track discussions and action items.
    - Interpreter Agent: Real-time speech-to-speech translation in Microsoft Teams for multilingual meetings. (public preview in early 2025)
    - Project Manager agent: Planner app in Teams.
1. [SharePoint Agent✍️](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/ignite-2024-agents-in-sharepoint-now-in-general-availability/4298746): Turn SharePoint sites and documents into interactive agents.
1. [Microsoft 365 Agents SDK✍️](https://devblogs.microsoft.com/microsoft365dev/introducing-the-microsoft-365-agents-sdk/): The evolution of the Bot Framework [✨](https://github.com/microsoft/agents) [19 Nov 2024]
1. [Microsoft Discovery✍️](https://azure.microsoft.com/en-us/blog/transforming-rd-with-agentic-ai-introducing-microsoft-discovery/): Graph-based scientific co-reasoning. Specialized discovery agents for conducting research. ​[19 May 2025]
1. [Microsoft Entra Agent ID✍️](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/announcing-microsoft-entra-agent-id-secure-and-manage-your-ai-agents/3827392): Automatically registers AI agents from Copilot Studio and Azure AI Foundry in Microsoft Entra admin center, enabling easy tracking, governance, and lifecycle management. [20 May 2025]

#### **Copilot Development**

1. [Community contributed samples for the Microsoft 365 Copilot✨](https://github.com/pnp/copilot-pro-dev-samples) [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/pnp/copilot-pro-dev-samples?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [Azure AI Agent Service✍️](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357): a fully managed platform for creating an agent on Azure AI Foundry [19 Nov 2024]
1. [Azure AI Foundry (rebranding of Azure AI Studio)✍️](https://learn.microsoft.com/en-us/azure/ai-studio/what-is-ai-studio): [Generative AI Developmet Hub✍️](https://azure.microsoft.com/en-us/products/ai-studio) + Promptflow + Azure AI Content safety / [📺](https://www.youtube.com/watch?v=Qes7p5w8Tz8) / [SDK and CLI✍️](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/sdk-generative-overview)
1. [Agent Evaluation in Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/build-smarter-test-smarter-agent-evaluation-in-microsoft-copilot-studio/): ✍️Structured, automated testing solution directly in Copilot Studio.
1. [Microsoft AI](http://microsoft.com/ai): The age of copilots: [✍️](https://www.linkedin.com/pulse/age-copilots-satya-nadella-2hllc) [Nov 2023]
1. [Copilot Tuning✍️](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-microsoft-365-copilot-tuning/4414762): Train models and create agents using company data in a simple, low-code way with Copilot Studio. [May 2025]
1. [Microsoft Copilot Dashboard](https://insights.cloud.microsoft/#/CopilotDashboard) / [✍️](https://techcommunity.microsoft.com/t5/microsoft-viva-blog/new-ways-microsoft-copilot-and-viva-are-transforming-the/ba-p/3982293)
1. [Microsoft Copilot Studio✍️](https://learn.microsoft.com/en-us/microsoft-copilot-studio/): Customize Copilot for Microsoft 365. FKA. Power Virtual Agents: [✍️](https://www.microsoft.com/en-us/copilot/microsoft-copilot-studio) [Nov 2023]
1. [Microsoft 365 Copilot - App Builder and Workflows](https://www.microsoft.com/en-us/microsoft-365/blog/2025/10/28/microsoft-365-copilot-now-enables-you-to-build-apps-and-workflows/): ✍️Build working apps & workflows using natural language.
1. The Copilot System: Explained by Microsoft [📺](https://www.youtube.com/watch?v=E5g20qmeKpg) [Mar 2023]
1. [Copilot Studio Monthly updates](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/cs-content-type/monthly-updates/)
1. [What’s new in Copilot Studio: March 2025✍️](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/whats-new-in-copilot-studio-march-2025/): Autonomous agents, deep reasoning, agent flows, generative orchestration, Model Context Protocol, tools/prompts in Copilot Studio, open web search, Microsoft-built agents in Copilot Studio, and private preview of GPT-4.5 now available. [31 Mar 2025]
1. Copilot Studio lite (formerly called the Microsoft 365 agent builder): [Sep 2025]

### **Azure AI Search**

- Azure AI Search (FKA Azure Cognitive Search) supports Hybrid Search, Pure Vector Search, Semantic Hybrid Search, and Text Search. doc:[✍️](https://learn.microsoft.com/en-us/azure/search/) / blog:[✍️](https://azure.microsoft.com/en-us/blog/product/azure-ai-search) / [✨](https://github.com/Azure-Samples/azureai-samples?tab=readme-ov-file#azure-ai-search)
- Azure Cognitive Search rebranding Azure AI Search, it supports Vector search and semantic ranker. [16 Nov 2023]
- A set of capabilities designed to improve relevance in these scenarios. We use a combination of hybrid retrieval (vector search + keyword search) + semantic ranking as the most effective approach for improved relevance out-of–the-box. `TL;DR: Retrieval Performance; Hybrid search + Semantic rank > Hybrid search > Vector only search > Keyword only` [✍️](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-outperforming-vector-search-with-hybrid/ba-p/3929167) [18 Sep 2023]  
  <img src="./files/acs-hybrid.png" alt="acs" width="300"/>
- [Agentic retrieval in Azure AI Search✍️](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-agentic-retrieval-in-azure-ai-search/4414677): An automated query engine that creates and runs its own retrieval plan for relevant results to complex questions. [20 May 2025]
- 🏬[Azure AI Search Demos using Jupyter Notebook✨](https://github.com/Azure-Samples/rag-with-azure-ai-search-notebooks): Jupyter notebooks that demonstrate vector search, hybrid search, image search, RAG, and evaluation. [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/rag-with-azure-ai-search-notebooks?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[Azure AI Search OpenAI Purview Data Security Demo✨](https://github.com/Azure-Samples/azure-search-openai-demo-purviewdatasecurity): Demo integrating Azure Search, OpenAI, and Purview data security [Jun 2025]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-search-openai-demo-purviewdatasecurity?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure AI Search Python Playground✨](https://github.com/farzad528/azure-ai-search-python-playground):  a collection of Jupyter notebooks designed to explore the various capabilities of Azure AI Search. [Feb 2024]
- 🏬[Azure AI Search Multimodal Sample✨](https://github.com/Azure-Samples/azure-ai-search-multimodal-sample) [May 2025] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-ai-search-multimodal-sample?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[Azure AI Search Power Skills✨](https://github.com/Azure-Samples/azure-search-power-skills): Custom skills for Azure AI Search [Jun 2019] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-search-power-skills?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[ChatGPT + Enterprise data RAG (Retrieval-Augmented Generation)✨](https://github.com/Azure-Samples/azure-search-openai-demo) [Feb 2023]
  ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-search-openai-demo?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Document-level access control✍️](https://learn.microsoft.com/en-us/azure/search/search-document-level-access-overview): Document-level access helps restrict content visibility to authorized users, based on predefined access rules. [20 May 2025]
- Hybrid search using Reciprocal Rank Fusion (RRF): Reciprocal Rank Fusion (RRF) is an algorithm that evaluates the search scores from multiple, previously ranked results to produce a unified result set. In Azure Cognitive Search, RRF is used whenever there are two or more queries that execute in parallel. [✍️](https://learn.microsoft.com/en-us/azure/search/hybrid-search-ranking)  
  <img src="https://learn.microsoft.com/en-us/azure/search/media/scoring-profiles/scoring-over-ranked-results.png" alt="rrf" width="300"/>
- In the vector databases category within Azure, several alternative solutions are available. However, the only option that provides a range of choices, including a conventional Lucene-based search engine and a hybrid search incorporating vector search capabilities.
- [Integrated vectorization✍️](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/integrated-vectorization-with-azure-openai-for-azure-ai-search/ba-p/4206836): Automatically splits documents into chunks, creates embeddings with Azure OpenAI, maps them to an Azure AI Search index, and automates query vectorization. [24 Aug 2024]
- 🏬[Python samples for Azure AI Search✨](https://github.com/Azure-Samples/azure-search-python-samples) [Apr 2019] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-search-python-samples?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [RAG-Knowledge✨](https://github.com/microsoft/RAG-Knowledge):💡Sample code for Data Preprocessing, Chunking, Index Design, Query Optimization [Jun 2024]
- Vector Search Sample Code: [✨](https://github.com/Azure/azure-search-vector-samples) [Apr 2023]
  ![**github stars**](https://img.shields.io/github/stars/Azure/azure-search-vector-samples?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[REST examples for Azure AI Search✨](https://github.com/Azure-Samples/azure-search-rest-samples) [Apr 2019] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-search-rest-samples?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **Azure AI Services**

- [Artificial intelligence (AI) architecture design✍️](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/):💡Overview Azure AI services, AI development platforms and tools
- [Assistants API✍️](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-openai-service-announces-assistants-api-new-models-for/ba-p/4049940): Code Interpreter, Function calling, Knowledge retrieval tool, and Threads (Truncated and optimized conversation history for the model's context length) in Azure [06 Feb 2024]
- [Azure AI Foundry](https://ai.azure.com/): Azure AI Foundry portal (formerly Azure AI Studio), and the [Azure AI Foundry SDK✍️](https://aka.ms/aifoundrysdk/reference), our unified SDK with pre-built app templates. `Rebranding for Enhancement: Azure Machine Learning Studio > Azure AI Studio > Azure AI Foundry.` [✍️](https://azure.microsoft.com/en-us/blog/the-next-wave-of-azure-innovation-azure-ai-foundry-intelligent-data-and-more/) / [✍️](https://learn.microsoft.com/en-us/azure/ai-studio/): Documentation [19 Nov 2024]
  - [Azure AI Agent Service✍️](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/introducing-azure-ai-agent-service/4298357): Public-preview
  - [Azure AI Content Understanding✍️](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-azure-ai-content-understanding-transforming-multimodal-data-into-insi/4297196)
  - [Azure AI Foundry Agent Service✍️](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/announcing-general-availability-of-azure-ai-foundry-agent-service/4414352): General Availability [20 May 2025]
  - [Azure AI Foundry Fine Tuning✍️](https://techcommunity.microsoft.com/blog/aiplatformblog/what%E2%80%99s-new-in-azure-ai-foundry-fine-tuning/4413873): SFT: non-reasoning models, DPO: GPT-4o, RFT: supported by reasoning models, GPT o4-mini [20 May 2025]
  - [Introducing Deep Research in Azure AI Foundry Agent Service✍️](https://azure.microsoft.com/en-us/blog/introducing-deep-research-in-azure-ai-foundry-agent-service): API and software development kit (SDK)-based offering of OpenAI’s advanced agentic research [7 Jul 2025]
  - [Weights & Biases with Azure✍️](https://aka.ms/WBFineTuningPartnership)
- Azure OpenAI Service Offerings
  1. Offering: Standard (Default), Batch (Low-cost, Huge workload), Provisioned (High performance)
  1. Offering Region types: Global (World wide), Data_zones (Zone based), Regional (Region based)
- Customer Copyright Commitment: protects customers from certain IP claims related to AI-generated content. [✍️](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/customer-copyright-commitment) [16 Nov 2023]
- [Models as a Service (MaaS)✍️](https://www.linkedin.com/pulse/model-service-maas-revolutionizing-ai-azure-shibu-kt): A cloud-based AI approach that provides developers and businesses with access to pre-built, pre-trained machine learning models. [Jul 2023]

<!-- 
#### .old
- Azure OpenAI Service On Your Data in Public Preview [✍️](https://techcommunity.microsoft.com/t5/ai-cognitive-services-blog/introducing-azure-openai-service-on-your-data-in-public-preview/ba-p/3847000) [19 Jun 2023]
- Copilot (FKA. Bing Chat Enterprise) [18 Jul 2023] [Privacy and Protection✍️](https://learn.microsoft.com/en-us/bing-chat-enterprise/privacy-and-protections#protected-by-default)
  1. Doesn't have plugin support
  1. Only content provided in the chat by users is accessible to Bing Chat Enterprise. 
- Azure OpenAI Finetuning: Babbage-002 is $34/hour, Davinci-002 is $68/hour, and Turbo is $102/hour. [✍️](https://techcommunity.microsoft.com/t5/azure-ai-services-blog/fine-tuning-now-available-with-azure-openai-service/ba-p/3954693) [16 Oct 2023]
-->

#### **Vector Database Options for Azure**

- [🔗](#vector-database-options-for-azure)

### **Microsoft Research**

1. [AutoGen Studio📑](https://alphaxiv.org/abs/2408.15247): A No-Code Developer Tool for Building and Debugging Multi-Agent Systems [9 Aug 2024]
1. [Azure AI Foundry Labs](https://ai.azure.com/labs/):💡Research driven tools and experimental projects.
1. [Data Formulator📑](https://alphaxiv.org/abs/2309.10094) [18 Sep 2023] | [Data Formulator 2📑](https://alphaxiv.org/abs/2408.16119):💡Iterative Creation of Data Visualizations, with AI Transforming Data Along the Way [✨](https://github.com/microsoft/data-formulator) [21 Feb 2025]
1. [GraphRAG (by Microsoft)📑](https://alphaxiv.org/abs/2404.16130):💡RAG with a graph-based approach to efficiently answer both specific and broad questions over large text corpora1. [✍️](https://microsoft.github.io/graphrag) / [✨](https://github.com/microsoft/graphrag) / [🔗](#graphrag) [24 Apr 2024]
![**github stars**](https://img.shields.io/github/stars/microsoft/graphrag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Knowledge-Augmented Large Language Models for Personalized Contextual Query Suggestion📑](https://alphaxiv.org/abs/2311.06318): K-LaMP. Contextual memory layer for LLM application [10 Nov 2023]
1. [Magentic-One✍️](https://aka.ms/magentic-one): A Generalist Multi-Agent System for Solving Complex Tasks [Nov 2024]
    - [Magentic-UI](www.microsoft.com/en-us/research/blog/magentic-ui-an-experimental-human-centered-web-agent/): Magentic-UI, built on Magentic-One, can browse the web, run Python and shell code, and process files. [19 May 2025 ]
1. [MarS: A Financial Market Simulation Engine Powered by Generative Foundation Model✨](https://github.com/microsoft/MarS) [4 Sep 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/MarS?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MatterGen✍️](https://www.microsoft.com/en-us/research/blog/mattergen-a-new-paradigm-of-materials-design-with-generative-ai/): a generative model for inorganic materials design [✨](https://github.com/microsoft/mattergen) [13 May 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/mattergen?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Microsoft AI Diagnostic Orchestrator (MAI-DxO)📑](https://alphaxiv.org/abs/2506.22405): Multi-Agent System. Accurately diagnoses up to 85% of NEJM case proceedings, which is over four times the rate achieved by a group of experienced physicians [30 June 2025 ]
1. [Microsoft Office Copilot: Natural Language Commanding via Program Synthesis📑](https://alphaxiv.org/abs/2306.03460): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2306.03460)]:💡Semantic Interpreter, a natural language-friendly AI system for productivity software such as Microsoft Office that leverages large language models (LLMs) to execute user intent across application features. [6 Jun 2023]
1. [NL2KQL📑](https://alphaxiv.org/abs/2404.02933): From Natural Language to Kusto Query [3 Apr 2024]
1. [Optimizing Model Selection for Compound AI Systems📑](https://alphaxiv.org/abs/2502.14815): a framework that automatically optimizes model selection for compound AI systems [20 Feb 2025] [✨](https://github.com/LLMSELECTOR/LLMSELECTOR) ![**github stars**](https://img.shields.io/github/stars/LLMSELECTOR/LLMSELECTOR?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PromptWizard✍️](https://www.microsoft.com/en-us/research/blog/promptwizard-the-future-of-prompt-optimization-through-feedback-driven-self-evolving-prompts/): The future of prompt optimization through feedback-driven self-evolving prompts [17 Dec 2024]
1. [R&D-Agent-Quant📑](https://alphaxiv.org/abs/2505.15155): R&D-Agent for Quantitative Finance, in short RD-Agent(Q), the first data-centric multi-agent framework designed to automate the full-stack research and development of quantitative strategies via coordinated factor-model co-optimization. [21 May 2025]
1. [SpreadsheetLLM📑](https://alphaxiv.org/abs/2407.09025): Introduces an efficient method to encode Excel sheets, outperforming previous approaches with 25 times fewer tokens.[12 Jul 2024]
1. [VibeVoice📑](https://alphaxiv.org/abs/2508.19205): Open-Source Text-to-Speech [26 Aug 2025]

### **Azure Reference Architectures**

#### Azure OpenAI Application

- 🏛️[AI Dev Gallery✨](https://github.com/microsoft/ai-dev-gallery):💡Windows application featuring interactive samples powered by local AI models. [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/ai-dev-gallery?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [An open-source template gallery✍️](https://azure.github.io/awesome-azd/?tags=aicollection): 🏆AI template collection
- 🏬[ARGUS✨](https://github.com/Azure-Samples/ARGUS): Hybrid approach with Azure Document Intelligence combined and GPT4-Vision to get better results without any pre-training. [Jun 2024]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/ARGUS?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🌐[Azure AI CLI✨](https://github.com/Azure/azure-ai-cli): Interactive command-line tool for ai [Jul 2023]
![**github stars**](https://img.shields.io/github/stars/Azure/azure-ai-cli?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure Cosmos DB + OpenAI ChatGPT✨](https://github.com/AzureCosmosDB/cosmosdb-nosql-copilot) [Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/AzureCosmosDB/cosmosdb-nosql-copilot?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[Azure OpenAI Embeddings QnA✨](https://github.com/Azure-Samples/azure-open-ai-embeddings-qna) [Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-open-ai-embeddings-qna?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure Video Indexer demo✨](https://aka.ms/viopenaidemo) [Apr 2023]
- 🏬[C# Implementation (ChatGPT + Enterprise data)✨](https://github.com/Azure-Samples/azure-search-openai-demo-csharp) [Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-search-openai-demo-csharp?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬ChatGPT + Enterprise data RAG (Retrieval-Augmented Generation) Demo [✨](https://github.com/Azure-Samples/azure-search-openai-demo) 🏆/ [📺](https://www.youtube.com/watch?v=tW2EA4aZ_YQ): Can ChatGPT work with your enterprise data? [06 Apr 2023] [8 Feb 2023]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-search-openai-demo?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬ChatGPT Plugin Quickstart using Python and FastAPI: [✨](https://github.com/Azure-Samples/openai-plugin-fastapi) [May 2023]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/openai-plugin-fastapi?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[Chat with your data - Solution accelerator✨](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) [Jun 2023]
 ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/chat-with-your-data-solution-accelerator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [eShopSupport✨](https://github.com/dotnet/eshopsupport):💡A reference .NET application using AI for a customer support ticketing system [✍️](https://devblogs.microsoft.com/semantic-kernel/eshop-infused-with-ai-a-comprehensive-intelligent-app-sample-with-semantic-kernel/) [Apr 2024]
![**github stars**](https://img.shields.io/github/stars/dotnet/eshopsupport?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- GPT-Azure-Search-Engine: [✨](https://github.com/pablomarin/GPT-Azure-Search-Engine)💡`Integration of Azure Bot Service with LangChain` [Feb 2023]
![**github stars**](https://img.shields.io/github/stars/pablomarin/GPT-Azure-Search-Engine?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Miyagi (Integration demo for multiple LangChain libraries)✨](https://github.com/Azure-Samples/miyagi) [Feb 2023]
 ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/miyagi?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Prompt Buddy✨](https://github.com/stuartridout/promptbuddy): 🏆Share and upvote favorite AI prompts. free Microsoft Teams Power App using Dataverse for Teams. [Mar 2024]
![**github stars**](https://img.shields.io/github/stars/stuartridout/promptbuddy?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Semantic Kernel sample application [🔗](#code-recipes)
- 🌐[Simple ChatGPT UI application✨](https://github.com/Azure/openai-at-scale) [Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/Azure/openai-at-scale?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Smart Components✨](https://github.com/dotnet-smartcomponents/smartcomponents): Experimental, end-to-end AI features for .NET apps [Mar 2024]
![**github stars**](https://img.shields.io/github/stars/dotnet-smartcomponents/smartcomponents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[VoiceRAG✨](https://github.com/Azure-Samples/aisearch-openai-rag-audio):💡Voice Using Azure AI Search and the GPT-4o Realtime API for Audio [✍️](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/voicerag-an-app-pattern-for-rag-voice-using-azure-ai-search-and/ba-p/4259116) [Sep 2024]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/aisearch-openai-rag-audio?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### Azure OpenAI Accelerator / Samples

##### Accelerator 💡

1. [🏛️AI Agents for Beginners - A Course✨](https://github.com/microsoft/ai-agents-for-beginners) ![**github stars**](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [Nov 2024]
1. [🌐Azure: Accelerator Collection✨](https://github.com/orgs/Azure/repositories?q=accelerator+sort%3Astars)
1. [Azure-Cognitive-Search-Azure-OpenAI-Accelerator✨](https://github.com/MSUSAzureAccelerators/Azure-Cognitive-Search-Azure-OpenAI-Accelerator) [May 2023]
![**github stars**](https://img.shields.io/github/stars/MSUSAzureAccelerators/Azure-Cognitive-Search-Azure-OpenAI-Accelerator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [🏬Azure-samples: Accelerator Collection✨](https://github.com/orgs/Azure-samples/repositories?q=accelerator+sort%3Astars)
1. [Conversational-Azure-OpenAI-Accelerator✨](https://github.com/MSUSAzureAccelerators/Conversational-Azure-OpenAI-Accelerator) [Feb 2022]
![**github stars**](https://img.shields.io/github/stars/MSUSAzureAccelerators/Conversational-Azure-OpenAI-Accelerator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [GPT-RAG✨](https://github.com/Azure/GPT-RAG):💡Enterprise RAG Solution Accelerator (GPT-RAG). Retrieval-Augmented Generation pattern running in Azure. [Jun 2023] ![**github stars**](https://img.shields.io/github/stars/Azure/GPT-RAG?style=flat-square&color=blue&cacheSeconds=36000&label=%20)  
1. [🏛️Microsoft: Accelerator Collection✨](https://github.com/orgs/Microsoft/repositories?q=accelerator+sort%3Astars)
1. [🏛️Model Context Protocol (MCP) Curriculum for Beginners✨](https://github.com/microsoft/mcp-for-beginners) ![**github stars**](https://img.shields.io/github/stars/microsoft/mcp-for-beginners?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [Apr 2025]
1. [👥MSUSAzureAccelerators: Accelerator Collection✨](https://github.com/MSUSAzureAccelerators):
1. [Solution Accelerator Portal✍️](https://accelerators.ms): 🏆

##### Samples

- 🏬[AgenticShop✨](https://github.com/azure-samples/postgres-agentic-shop): AgenticShop is a GenAI-powered e-commerce demo that showcases how multi-agent workflows, powered by LlamaIndex [May 2025] ![**github stars**](https://img.shields.io/github/stars/azure-samples/postgres-agentic-shop?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [AI Samples for .NET✨](https://github.com/dotnet/ai-samples):  official .NET samples demonstrating how to use AI. `Evaluating a LLM with .NET` [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/dotnet/ai-samples?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏛️[AI-Sentry✨](https://github.com/microsoft/ai-sentry): A lightweight, pluggable facade layer for AOAI [Jun 2024]
![**github stars**](https://img.shields.io/github/stars/microsoft/ai-sentry?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🌐[AI-in-a-Box✨](https://github.com/Azure/AI-in-a-Box): AI-in-a-Box aims to provide an "Azure AI/ML Easy Button" for common scenarios [Sep 2023]
![**github stars**](https://img.shields.io/github/stars/Azure/AI-in-a-Box?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[AI-in-a-Box - Generative AI Bot Quickstart✨](https://github.com/Azure-Samples/gen-ai-bot-in-a-box): A template deploys a Generative AI Virtual Assistant using Azure OpenAI and Bot Framework. [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/gen-ai-bot-in-a-box?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[AI Hub Gateway Landing Zone✨](https://github.com/Azure-Samples/ai-hub-gateway-solution-accelerator): Enterprise-ready solution accelerator for implementing a centralized AI API gateway. [May 2024] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/ai-hub-gateway-solution-accelerator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[Azure AI Foundry Baseline✨](https://github.com/Azure-Samples/azure-ai-foundry-baseline): Baseline setup for Azure AI Foundry projects [Jan 2024]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-ai-foundry-baseline?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[Azure OpenAI RAFT✨](https://github.com/Azure-Samples/azure-openai-raft ): RAFT Fine-Tuning for RAG Using Azure OpenAI [Sep 2024]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-openai-raft?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🌐[Azure Functions (C#) bindings for OpenAI✨](https://github.com/Azure/azure-functions-openai-extension) [Nov 2023]
![**github stars**](https://img.shields.io/github/stars/Azure/azure-functions-openai-extension?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🌐[Azure Multimodal AI + LLM Processing Accelerator✨](https://github.com/Azure/multimodal-ai-llm-processing-accelerator): Build multimodal data processing pipelines with Azure AI Services + LLMs [Aug 2024]
![**github stars**](https://img.shields.io/github/stars/Azure/multimodal-ai-llm-processing-accelerator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[Azure OpenAI cookbook✨](https://github.com/Azure-Samples/openai): The repository for all Azure OpenAI Samples complementing the OpenAI cookbook. [Apr 2023]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/openai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Azure OpenAI Network Latency Test Script
: [✨](https://github.com/wloryo/networkchatgpt/blob/dc76f2264ff8c2a83392e6ae9ee2aaa55ca86f0e/openai_network_latencytest_nocsv_pub_v1.1.py) [Jun 2023]  
- 🏬Azure OpenAI with AKS by Terraform (simple version): [✨](https://github.com/Azure-Samples/azure-openai-terraform-deployment-sample) [May 2023]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-openai-terraform-deployment-sample?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬Azure OpenAI with AKS By Bicep: [✨](https://github.com/Azure-Samples/aks-openai) [May 2023]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/aks-openai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬Azure OpenAI with AKS By Terraform: [✨](https://github.com/Azure-Samples/aks-openai-terraform) [Jun 2023]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/aks-openai-terraform?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬Azure-Samples [✨](https://github.com/Azure-Samples)
- 🏬[Azure SQL DB + AOAI✨](https://github.com/Azure-Samples/SQL-AI-samples): AI applications built on data from an Azure SQL Database [Oct 2023]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/SQL-AI-samples?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏛️[Build Your Own Copilot Solution Accelerator✨](https://github.com/microsoft/Build-your-own-copilot-Solution-Accelerator): Solution Accelerator to show how to build your own copilot [Mar 2024]
![**github stars**](https://img.shields.io/github/stars/microsoft/Build-your-own-copilot-Solution-Accelerator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬Create an Azure OpenAI, LangChain, ChromaDB, and Chainlit ChatGPT-like application in Azure Container Apps using Terraform [✨](https://github.com/Azure-Samples/container-apps-openai/) [Jul 2023]
- 🏬[Design and Evaluation of RAG Solutions✨](https://github.com/Azure-Samples/Design-and-evaluation-of-RAG-solutions): Resources for designing and evaluating RAG solutions [Sep 2024]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/Design-and-evaluation-of-RAG-solutions?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏛️[Document generation solution accelerator✨](https://github.com/microsoft/document-generation-solution-accelerator):  AI assistant for document generation [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/document-generation-solution-accelerator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[Document Processing with Azure AI Samples✨](https://github.com/Azure-Samples/azure-ai-document-processing-samples): Demonstrates how to use Azure AI Document Intelligence, Azure OpenAIS [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-ai-document-processing-samples?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[Enterprise Logging✨](https://github.com/Azure-Samples/openai-python-enterprise-logging): Comprehensive logging of Azure OpenAI model execution [Feb 2023]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/openai-python-enterprise-logging?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
- 🌐[Enterprise RAG Avatar✨](https://github.com/Azure/gpt-rag-avatar): GPT-RAG Avatar integrates Generative AI responses, real-time streaming into a dynamic avatar interface [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/Azure/gpt-rag-avatar?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
- 🏬[Evaluating a RAG Chat App✨](https://github.com/Azure-Samples/ai-rag-chat-evaluator): Tools for evaluation of RAG Chat Apps using Azure AI Evaluate SDK [Nov 2023]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/ai-rag-chat-evaluator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏛️[Fabric notebooks for analyzing chat history stored in CosmosDB✨](https://github.com/microsoft/fabric-cosmosdb-chat-analytics) [Sep 2024]
![**github stars**](https://img.shields.io/github/stars/microsoft/fabric-cosmosdb-chat-analytics?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🌐[Generate Synthetic QnAs from Real-world Data✨](https://github.com/Azure/synthetic-qa-generation): Demonstrating how to create/augment a QnA dataset from complex unstructured data. ![**github stars**](https://img.shields.io/github/stars/Azure/synthetic-qa-generation?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏛️[Generic accelerator for Build your own copilot✨](https://github.com/microsoft/Generic-Build-your-own-copilot-Solution-Accelerator): Chat with your own data, generate a document template using your own data, and exporting the document in a docx format. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/Generic-Build-your-own-copilot-Solution-Accelerator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🌐[GPT RAG Ingestion✨](https://github.com/Azure/gpt-rag-ingestion): GPT-based RAG ingestion utilities [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/Azure/gpt-rag-ingestion?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🌐[GPT-RAG Orchestrator✨](https://github.com/Azure/gpt-rag-orchestrator): an agentic orchestration layer built on Azure AI Foundry Agent Service and the Semantic Kernel framework. [June 2023] ![**github stars**](https://img.shields.io/github/stars/Azure/gpt-rag-orchestrator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[Healthcare Agent Orchestrator✨](https://github.com/Azure-Samples/healthcare-agent-orchestrator): A multi-agent accelerator that coordinates modular specialized agents to assist multi-disciplinary healthcare workflows. [May 2025] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/healthcare-agent-orchestrator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[M365 Custom Engine Agent✨](https://github.com/Azure-Samples/m365-custom-engine-agents): Proxy Agent demo to handle Copilot activities and forward a simple request to your existing backend [Aug 2025] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/m365-custom-engine-agents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏛️[Microsoft Copilot Studio Samples✨](https://github.com/microsoft/CopilotStudioSamples): Samples and artifacts for Microsoft Copilot Studio [Oct 2019] ![**github stars**](https://img.shields.io/github/stars/microsoft/CopilotStudioSamples?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Microsoft.Extensions.AI✍️](https://devblogs.microsoft.com/dotnet/introducing-microsoft-extensions-ai-preview/): a unified layer of C# abstractions for interacting with AI services, such as small and large language models (SLMs and LLMs), embeddings, and middleware. [8 Oct 2024]
- 🏬[OpenAI Chat Application with Microsoft Entra Authentication✨](https://github.com/Azure-Samples/openai-chat-app-entra-auth-builtin): Microsoft Entra ID for user authentication [May 2024]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/openai-chat-app-entra-auth-builtin?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏛️[RAG for Azure Data✨](https://github.com/microsoft/AzureDataRetrievalAugmentedGenerationSamples): Retrieval Augmented Generation (RAG) for Azure Data [Jun 2023]
![**github stars**](https://img.shields.io/github/stars/microsoft/AzureDataRetrievalAugmentedGenerationSamples?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏛️[Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook) - ✨Semantic Kernel Cookbook for beginners. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/SemanticKernelCookBook?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🌐[Setting up Azure OpenAI with Azure API Management✨](https://github.com/Azure/enterprise-azureai): Setting up Azure API Management to serve Azure OpenAI [Jan 2024]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/openai-python-enterprise-logging?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/Azure/enterprise-azureai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🌐[SLM/LLM Fine-tuning on Azure✨](https://github.com/Azure/azure-llm-fine-tuning): SLM/LLM Fine-tuning on Azure [May 2024]
![**github stars**](https://img.shields.io/github/stars/Azure/azure-llm-fine-tuning?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[Smart load balancing for AOAI✨](https://github.com/Azure-Samples/openai-aca-lb): Smart load balancing for OpenAI endpoints [Jan 2024]
![**github stars**](https://img.shields.io/github/stars/Azure-Samples/openai-aca-lb?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- 🏬[Vector similarity search with Azure SQL & Azure OpenAI✨](https://github.com/Azure-Samples/azure-sql-db-openai): Samples on how to use Azure SQL database with Azure OpenAI [May 2023] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/azure-sql-db-openai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### Referece: Use Case and Architecture

- [AI Agent-Driven Auto Insurance Claims RAG Pipeline✍️](https://techcommunity.microsoft.com/t5/azure-architecture-blog/exploring-ai-agent-driven-auto-insurance-claims-rag-pipeline/ba-p/4233779) [09 Sep 2024]
- [AI decision tree✍️](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/scenarios/ai/strategy):💡Selecting the most suitable tools and platforms for your generative and nongenerative AI use cases.
- [AI Feed✍️](https://techcommunity.microsoft.com/t5/artificial-intelligence-and/ct-p/AI) | [AI Platform ✍️](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/bg-p/AIPlatformBlog)
- [AI gateway capabilities in Azure API Management✍️](https://techcommunity.microsoft.com/blog/integrationsonazureblog/ai-gateway-enhancements-llm-policies-real-time-api-support-content-safety-and-mo/4409828): 💡Semantic Caching. Azure AI Content Safety. LLM policies (llm-token-limit, llm-emit-metric, llm-content-safety) [01 May 2025]
- [An Introduction to LLMOps✍️](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/an-introduction-to-llmops-operationalizing-and-managing-large/ba-p/3910996): Operationalizing and Managing Large Language Models using Azure ML [27 Aug 2023]
- [Authentication and Authorization in Generative AI applications with Entra ID and Azure AI Search✍️](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/authentication-and-authorization-in-generative-ai-applications/ba-p/4022277) [09 Jan 2024]
- [Azure AI Services Landing Zone✨](https://github.com/FreddyAyala/AzureAIServicesLandingZone) / [✍️](https://techcommunity.microsoft.com/t5/azure-architecture-blog/azure-openai-landing-zone-reference-architecture/ba-p/3882102) [24 Jul 2023]
![**github stars**](https://img.shields.io/github/stars/FreddyAyala/AzureAIServicesLandingZone?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure Command Companion✍️](https://techcommunity.microsoft.com/t5/analytics-on-azure-blog/azure-command-companion/ba-p/4005044): Harnessing the Power of OpenAI GPT-3.5 Turbo for Azure CLI Command Generation [10 Dec 2023]
- [Azure OpenAI and Call Center Modernization✍️](https://techcommunity.microsoft.com/t5/azure-architecture-blog/azure-openai-and-call-center-modernization/ba-p/4107070) [11 Apr 2024]
- [Azure OpenAI Best Practices Insights from Customer Journeys✍️](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-openai-best-practices-insights-from-customer-journeys/ba-p/4166943): LLMLingua, Skeleton Of Thought [12 Jun 2024]
- [Azure OpenAI chat baseline architecture✍️](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/basic-openai-e2e-chat):💡Designing your production enterprise chat applications. [✨](https://github.com/Azure-Samples/openai-end-to-end-basic) ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/openai-end-to-end-basic?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure OpenAI Design Patterns✨](https://github.com/microsoft/azure-openai-design-patterns): A set of design patterns using the Azure OpenAI service [May 2023] ![**github stars**](https://img.shields.io/github/stars/microsoft/azure-openai-design-patterns?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure OpenAI RAG workshop✨](https://github.com/Azure-Samples/azure-openai-rag-workshop): RAG using LangChain.js and OpenAI. Hosted on Azure Static Web Apps and Azure Container Apps, with Azure AI Search as the vector database. [✍️](https://aka.ms/ws/openai-rag) [8 Nov 2023]
- [Azure OpenAI workshop✨](https://github.com/microsoft/OpenAIWorkshop): Workshop materials to build intelligent solutions on Open AI [Feb 2023]
![**github stars**](https://img.shields.io/github/stars/microsoft/OpenAIWorkshop?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Baseline Agentic AI Systems Architecture✍️](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/baseline-agentic-ai-systems-architecture/ba-p/4207137) [20 Aug 2024]
- [Baseline OpenAI end-to-end chat reference architecture✍️](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/architecture/baseline-openai-e2e-chat)
- [Build language model pipelines with memory✍️](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/openai/guide/language-model-pipelines)
- [Build Long-Running AI Agents on Azure App Service with Microsoft Agent Framework](https://techcommunity.microsoft.com/blog/appsonazureblog/part-2-build-long-running-ai-agents-on-azure-app-service-with-microsoft-agent-fr/4465825): ✍️Multi-Agent Workflow Travel Planner With WebJob.
- [Chat with your Azure DevOps data✍️](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/chat-with-your-azure-devops-data/ba-p/4017784) [10 Jan 2024]
- [Check Your Facts and Try Again: Improving Large Language Models with External Knowledge and Automated Feedback✍️](https://www.microsoft.com/en-us/research/group/deep-learning-group/articles/check-your-facts-and-try-again-improving-large-language-models-with-external-knowledge-and-automated-feedback/) [07 Mar 2023]
- [Copilot Custom Agents for .NET Developers: C# Expert & WinForms Expert](https://devblogs.microsoft.com/dotnet/introducing-custom-agents-for-dotnet-developers-csharp-expert-winforms-expert): ✍️First two experimental custom agents for .NET developers: C# Expert and WinForms Expert.
- [Designing and developing a RAG solution✍️](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/rag/rag-solution-design-and-evaluation-guide)
- [Grounding LLMs✍️](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/grounding-llms/ba-p/3843857): Retrieval-Augmented Generation (RAG) [09 Jun 2023]
- [How real-world businesses are transforming with AI✍️](https://blogs.microsoft.com/blog/2024/11/12/how-real-world-businesses-are-transforming-with-ai/):💡Collected over 200 examples of how organizations are leveraging Microsoft’s AI capabilities. [12 Nov 2024]
- [How to develop AI Apps and Agents in Azure – A Visual Guide✍️](https://devblogs.microsoft.com/all-things-azure/how-to-develop-ai-apps-and-agents-in-azure-a-visual-guide/)💡a Visual map to help you decide which Azure AI service is best for your use case. [4 Dec 2024]
- [Integrate private access to your Azure Open AI Chatbot✍️](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/integrate-private-access-to-your-azure-open-ai-chatbot/ba-p/3994613) [30 Nov 2023]
- [Logic Apps as MCP Servers✍️](https://www.infoq.com/news/2025/09/microsoft-logic-apps-mcp-servers/): Azure Logic Apps (Standard) to function as MCP servers [25 Sep 2025]
- [Microsoft AI / Responsible AI](https://aka.ms/RAIResources) 🏆
- [Microsoft AI Tour✨](https://github.com/microsoft/aitour-repo-principal-list): a session and workshop how to best leverage AI [Aug 2024]
- [NL to SQL Architecture Alternative✍️](https://techcommunity.microsoft.com/t5/azure-architecture-blog/nl-to-sql-architecture-alternatives/ba-p/4136387) [14 May 2024] / [Natural Language to SQL Console✨](https://github.com/microsoft/kernel-memory/tree/NL2SQL/examples/200-dotnet-nl2sql)
- [Optimize Azure OpenAI Applications with Semantic Caching✍️](https://techcommunity.microsoft.com/t5/azure-architecture-blog/optimize-azure-openai-applications-with-semantic-caching/ba-p/4106867) [09 Apr 2024]
- [Partner Resources: AI & ML Academy](https://microsoft.github.io/PartnerResources/skilling/ai-ml-academy)💡a comprehensive learning resource provided by Microsoft for partners and developers
- [Responsible AI Transparency Report✍️](https://www.microsoft.com/en-us/corporate-responsibility/responsible-ai-transparency-report)
- [Retrieval Augmented Fine Tuning✍️](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/retrieval-augmented-fine-tuning-use-gpt-4o-to-fine-tune-gpt-4o/ba-p/4248861): RAFT: Combining the best parts of RAG and fine-tuning (SFT) [25 Sep 2024]
- [Revolutionize your Enterprise Data with ChatGPT✍️](https://techcommunity.microsoft.com/t5/ai-applied-ai-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w/ba-p/3762087) [09 Mar 2023]
- [Safeguard and trustworthy generative AI applications✍️](https://azure.microsoft.com/en-us/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/) [28 Mar 2024]
- [Security Best Practices for GenAI Applications (OpenAI) in Azure✍️](https://techcommunity.microsoft.com/t5/azure-architecture-blog/security-best-practices-for-genai-applications-openai-in-azure/ba-p/4027885) [16 Jan 2024]
- [Sovereign controls in data processing for Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365/blog/2025/11/04/microsoft-offers-in-country-data-processing-to-15-countries-to-strengthen-sovereign-controls-for-microsoft-365-copilot/): ✍️Microsoft 365 Data Residency and Processing commitments map.
- [Using keyless authentication with Azure OpenAI✍️](https://techcommunity.microsoft.com/t5/microsoft-developer-community/using-keyless-authentication-with-azure-openai/ba-p/4111521) [12 Apr 2024]

<!-- 
|                                                                                                                                                        |                                                                                                                           |
| :----------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------------------: |
|                              [Azure OpenAI Embeddings QnA✨](https://github.com/Azure-Samples/azure-open-ai-embeddings-qna) [Apr 2023]                              | [Azure Cosmos DB + OpenAI ChatGPT✨](https://github.com/AzureCosmosDB/cosmosdb-nosql-copilot) C# blazor [Mar 2023] |
|                                    <img src="./files/demo-architecture.png" alt="embeddin_azure_csharp" width="200"/>                                    |                              <img src="./files/cosmos-gpt.png" alt="gpt-cosmos" width="200"/>                               |
| [C# Implementation✨](https://github.com/Azure-Samples/azure-search-openai-demo-csharp) ChatGPT + Enterprise data with Azure OpenAI and Cognitive Search [Apr 2023] |          [Simple ChatGPT UI application✨](https://github.com/Azure/openai-at-scale) TypeScript, ReactJs and Flask  [Apr 2023]        |
|                                <img src="./files/demo-architecture-csharp2.png" alt="embeddin_azure_csharp" width="200"/>                                |                              <img src="./files/chatscreen.png" alt="gpt-cosmos" width="200"/>                               |
|                                  [Azure Video Indexer demo✨](https://aka.ms/viopenaidemo) Azure Video Indexer + OpenAI [Apr 2023]                             |        [Miyagi✨](https://github.com/Azure-Samples/miyagi) Integration demonstrate for multiple langchain libraries [Feb 2023] |
|                                      <img src="./files/demo-videoindexer.png" alt="demo-videoindexer" width="200"/>                                      |                                 <img src="./files/wip-azure.png" alt="miyagi" width="200"/>                                 |
|                                  [ChatGPT + Enterprise data RAG (Retrieval-Augmented Generation)✨](https://github.com/Azure-Samples/azure-search-openai-demo)🏆 [Feb 2023]                             |        [Chat with your data - Solution accelerator✨](https://github.com/Azure-Samples/chat-with-your-data-solution-accelerator) [Jun 2023] |
|                                      <img src="./files/chatscreen2.png" alt="demo-videoindexer" height="130"/>                                      |                                 <img src="./files/cwyd-solution-architecture.png" width="200"/>                                 |

--- -->


## **Applications and Frameworks**

- [900 most popular open source AI tools](https://huyenchip.com/2024/03/14/ai-oss.html):🏆What I learned from looking at 900 most popular open source AI tools [list](https://huyenchip.com/llama-police) [Mar 2024]
- [Awesome LLM Apps✨](https://github.com/Shubhamsaboo/awesome-llm-apps):💡A curated collection of awesome LLM apps built with RAG and AI agents. [Apr 2024]
 ![**github stars**](https://img.shields.io/github/stars/Shubhamsaboo/awesome-llm-apps?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure OpenAI Samples✨](https://github.com/kimtth/azure-openai-cookbook): 🐳 Azure OpenAI (OpenAI) Sample Collection - 🪂 100+ Code Cookbook 🧪 [Mar 2025]
- [GenAI Agents✨](https://github.com/NirDiamant/GenAI_Agents):🏆Tutorials and implementations for various Generative AI Agent techniques, from basic to advanced. [Sep 2024]
 ![**github stars**](https://img.shields.io/github/stars/NirDiamant/GenAI_Agents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [GenAI Cookbook✨](https://github.com/dmatrix/genai-cookbook): A mixture of Gen AI cookbook recipes for Gen AI applications. [Nov 2023] ![**github stars**](https://img.shields.io/github/stars/dmatrix/genai-cookbook?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Generative AI Design Patterns✍️](https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0): 9 architecture patterns for working with LLMs. [Feb 2024]
- [Open100: Top 100 Open Source achievements.](https://www.benchcouncil.org/evaluation/opencs/annual.html)
- [The Last Mile Problem: Why Your AI Models Stumble Before the Finish Line](https://solutionsreview.com/data-management/the-last-mile-problem-why-your-ai-models-stumble-before-the-finish-line/): According to Gartner, by 2025, at least 30 percent of GenAI projects will be abandoned after the POC stage. [25 Oct 2024]

#### **Cross-reference**

- RAG: [🔗](#rag-solution-design)
- Agent Applications and Libraries: [🔗](#agentic-design-frameworks)
- OSS Alternatives for OpenAI Code Interpreter: [🔗](#oss-alternatives-for-openai-code-interpreter-aka-advanced-data-analytics)
- LLMOps: Large Language Model Operations: [🔗](#llmops-large-language-model-operations)

### **Applications, Frameworks, and User Interface (UI/UX)**

#### **LLM Ochestration**

- [🔗](#agent-framework): Agent Framework | [🔗](#rag-development): RAG Development | [🔗](#prompting-frameworks): Prompting Frameworks | [🔗](#microsoft-azure-openai-llm-framework): Microsoft Azure OpenAI LLM Framework
- [🔗](#langchain-features-usage-and-comparisons): LangChain | [🔗](#llamaindex): LlamaIndex | [🔗](#dspy): DSPy | [🔗](#semantic-kernel): Semantic Kernel
- Micro-Orchestration: [LangChain](https://www.langchain.com), [LlamaIndex](https://www.llamaindex.ai), [Haystack](https://haystack.deepset.ai), [AdalFlow](https://adalflow.sylph.ai) | Macro-Orchestration: [LangGraph](https://langchain-ai.github.io/langgraph), [Burr](https://burr.dagworks.io) | Agentic Design: [Autogen](https://microsoft.github.io/autogen), [CrewAI](https://docs.crewai.com) | Optimizer: [DSPy](https://dspy-docs.vercel.app), [TextGrad](https://textgrad.com) 

#### **LLM Training/Build**

1. [exo✨](https://github.com/exo-explore/exo): Run your own AI cluster at home with everyday devices [Jun 2024]
![**github stars**](https://img.shields.io/github/stars/exo-explore/exo?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [fairseq✨](https://github.com/facebookresearch/fairseq): a sequence modeling toolkit that allows researchers and developers to train custom models for translation, summarization, language modeling [Sep 2017]
![**github stars**](https://img.shields.io/github/stars/facebookresearch/fairseq?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [fastText✨](https://github.com/facebookresearch/fastText): A library for efficient learning of word representations and sentence classification [Aug 2016]
![**github stars**](https://img.shields.io/github/stars/facebookresearch/fastText?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [GPT4All✨](https://github.com/nomic-ai/gpt4all): Open-source large language models that run locally on your CPU [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/nomic-ai/gpt4all?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [huggingface/transformers✨](https://github.com/huggingface/transformers): 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX. (github.com) [Oct 2018]
![**github stars**](https://img.shields.io/github/stars/huggingface/transformers?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [jax✨](https://github.com/google/jax): JAX is Autograd (automatically differentiate native Python & Numpy) and XLA (compile and run NumPy) [Oct 2018]
![**github stars**](https://img.shields.io/github/stars/google/jax?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Kiln✨](https://github.com/Kiln-AI/Kiln): Desktop Apps for for fine-tuning LLM models, synthetic data generation, and collaborating on datasets. [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/Kiln-AI/Kiln?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [KTransformers✨](https://github.com/kvcache-ai/ktransformers): A Flexible Framework for Experiencing Cutting-edge LLM Inference Optimizations [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/kvcache-ai/ktransformers?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LLaMA-Factory✨](https://github.com/hiyouga/LLaMA-Factory): Unify Efficient Fine-Tuning of 100+ LLMs [May 2023]
![**github stars**](https://img.shields.io/github/stars/hiyouga/LLaMA-Factory?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LM Studio](https://lmstudio.ai/): UI for Discover, download, and run local LLMs [May 2024]
1. [Meta Lingua✨](https://github.com/facebookresearch/lingua): a minimal and fast LLM training and inference library designed for research. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/facebookresearch/lingua?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [mosaicml/llm-foundry✨](https://github.com/mosaicml/llm-foundry): LLM training code for MosaicML foundation models [Jun 2022]
![**github stars**](https://img.shields.io/github/stars/mosaicml/llm-foundry?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ollama✨](https://github.com/jmorganca/ollama):💡Running with Large language models locally [Jun 2023]
![**github stars**](https://img.shields.io/github/stars/jmorganca/ollama?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Reranker✨](https://github.com/luyug/Reranker): Training and deploying deep languge model reranker in information retrieval (IR), question answering (QA) [Jan 2021] ![**github stars**](https://img.shields.io/github/stars/luyug/Reranker?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Sentence Transformers📑](https://alphaxiv.org/abs/1908.10084): Python framework for state-of-the-art sentence, text and image embeddings. Useful for semantic textual similar, semantic search, or paraphrase mining. [✨](https://github.com/UKPLab/sentence-transformers) [27 Aug 2019]
![**github stars**](https://img.shields.io/github/stars/UKPLab/sentence-transformers?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [string2string✨](https://github.com/stanfordnlp/string2string): an open-source tool that offers a comprehensive suite of efficient algorithms for a broad range of string-to-string problems. [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/stanfordnlp/string2string?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Transformer Lab✨](https://github.com/transformerlab/transformerlab-app): Open Source Application for Advanced LLM + Diffusion Engineering: interact, train, fine-tune, and evaluation. [Dec 2023] ![**github stars**](https://img.shields.io/github/stars/transformerlab/transformerlab-app?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [unsloth✨](https://github.com/unslothai/unsloth): Finetune Mistral, Gemma, Llama 2-5x faster with less memory! [Nov 2023]
![**github stars**](https://img.shields.io/github/stars/unslothai/unsloth?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Visual Blocks✨](https://github.com/google/visualblocks): Google visual programming framework that lets you create ML pipelines in a no-code graph editor. [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/google/visualblocks?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [vLLM✨](https://github.com/vllm-project/vllm): Easy-to-use library for LLM inference and serving. [Feb 2023]
![**github stars**](https://img.shields.io/github/stars/vllm-project/vllm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [WebLLM✨](https://github.com/mlc-ai/web-llm): High-Performance In-Browser LLM Inference Engine. [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/mlc-ai/web-llm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Weights & Biases✨](https://github.com/wandb/examples): Visualizing and tracking your machine learning experiments [wandb.ai](https://wandb.ai/) doc: `deeplearning.ai/wandb` [Jan 2020]
![**github stars**](https://img.shields.io/github/stars/wandb/examples?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [YaFSDP✨](https://github.com/yandex/YaFSDP): Yet another Fully Sharded Data Parallel (FSDP): enhanced for distributed training. YaFSDP vs DeepSpeed. [May 2024]
![**github stars**](https://img.shields.io/github/stars/yandex/YaFSDP?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **LLM Application Development**

1. [Azure OpenAI Proxy✨](https://github.com/scalaone/azure-openai-proxy): OpenAI API requests converting into Azure OpenAI API requests [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/scalaone/azure-openai-proxy?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [BISHENG✨](https://github.com/dataelement/bisheng): an open LLM application devops platform, focusing on enterprise scenarios. [Aug 2023]
![**github stars**](https://img.shields.io/github/stars/dataelement/bisheng?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ChainForge✨](https://github.com/ianarawjo/ChainForge): An open-source visual programming environment for battle-testing prompts to LLMs. [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/ianarawjo/ChainForge?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [coze-studio✨](https://github.com/coze-dev/coze-studio): An AI agent development platform with all-in-one visual tools, simplifying agent creation, debugging, and deployment like never before. Coze your way to AI Agent creation. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/coze-dev/coze-studio?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Customer Service Chat with AI Assistant Handoff✨](https://github.com/pereiralex/Simple-bot-handoff-sample): Seamlessly hand off to a human agent when needed. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/pereiralex/Simple-bot-handoff-sample?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DemoGPT✨](https://github.com/melih-unsal/DemoGPT): Automatic generation of LangChain code [Jun 2023]
![**github stars**](https://img.shields.io/github/stars/melih-unsal/DemoGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Dify✨](https://github.com/langgenius/dify): an open-source platform for building applications with LLMs, featuring an intuitive interface for AI workflows and model management. [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/langgenius/dify?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [E2B✨](https://github.com/e2b-dev/e2b): an open-source infrastructure that allows you run to AI-generated code in secure isolated sandboxes in the cloud. [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/e2b-dev/e2b?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ell✨](https://github.com/MadcowD/ell): Treats prompts as programs with built-in versioning, monitoring, and tooling for LLMs. [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/MadcowD/ell?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Flowise✨](https://github.com/FlowiseAI/Flowise) Drag & drop UI to build your customized LLM flow [Apr 2023]
![**github stars**](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Harbor✨](https://github.com/av/harbor): Effortlessly run LLM backends, APIs, frontends, and services with one command. a helper for the local LLM development environment. [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/av/harbor?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Jina-Serve✨](https://github.com/jina-ai/serve): a framework for building and deploying AI services that communicate via gRPC, HTTP and WebSockets. [Feb 2020] ![**github stars**](https://img.shields.io/github/stars/jina-ai/serve?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [langflow✨](https://github.com/langflow-ai/langflow): LangFlow is a UI for LangChain, designed with react-flow. [Feb 2023]
![**github stars**](https://img.shields.io/github/stars/logspace-ai/langflow?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [langfun✨](https://github.com/google/langfun): leverages PyGlove to integrate LLMs and programming. [Aug 2023]
![**github stars**](https://img.shields.io/github/stars/google/langfun?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [langfuse✨](https://github.com/langfuse/langfuse): Traces, evals, prompt management and metrics to debug and improve your LLM application. [May 2023]
![**github stars**](https://img.shields.io/github/stars/langfuse/langfuse?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Llama Stack✨](https://github.com/meta-llama/llama-stack):💡building blocks for Large Language Model (LLM) development [Jun 2024]
![**github stars**](https://img.shields.io/github/stars/meta-llama/llama-stack?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [marvin✨](https://github.com/PrefectHQ/marvin): a lightweight AI toolkit for building natural language interfaces. [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/PrefectHQ/marvin?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [microsoft/Tokenizer✨](https://github.com/microsoft/Tokenizer): Tiktoken in C#: .NET and TypeScript implementation of BPE tokenizer for OpenAI LLMs. [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/microsoft/Tokenizer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [mindsdb✨](https://github.com/mindsdb/mindsdb): The open-source virtual database for building AI from enterprise data. It supports SQL syntax for development and deployment, with over 70 technology and data integrations. [Aug 2018] ![**github stars**](https://img.shields.io/github/stars/mindsdb/mindsdb?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MiniChain✨](https://github.com/srush/MiniChain): A tiny library for coding with llm [Feb 2023]
![**github stars**](https://img.shields.io/github/stars/srush/MiniChain?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [mirascope✨](https://github.com/Mirascope/mirascope): a library that simplifies working with LLMs via a unified interface for multiple providers. [Dec 2023] ![**github stars**](https://img.shields.io/github/stars/Mirascope/mirascope?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [motia✨](https://github.com/MotiaDev/motia): Modern Backend Framework that unifies APIs, background jobs, workflows, and AI agents into a single cohesive system with built-in observability and state management. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/MotiaDev/motia?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Pipecat✨](https://github.com/pipecat-ai/pipecat): Open Source framework for voice and multimodal conversational AI [Dec 2023] ![**github stars**](https://img.shields.io/github/stars/pipecat-ai/pipecat?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PocketFlow✨](https://github.com/miniLLMFlow/PocketFlow): Minimalist LLM Framework in 100 Lines. Enable LLMs to Program Themselves. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/miniLLMFlow/PocketFlow?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Refly✨](https://github.com/refly-ai/refly): WYSIWYG AI editor to create llm application. [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/refly-ai/refly?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RouteLLM✨](https://github.com/lm-sys/RouteLLM): A framework for serving and evaluating LLM routers [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/lm-sys/RouteLLM?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Spring AI✨](https://github.com/spring-projects-experimental/spring-ai): Developing AI applications for Java. [Jul 2023]
![**github stars**](https://img.shields.io/github/stars/spring-projects-experimental/spring-ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Superagent✨](https://github.com/superagent-ai/superagent): AI Assistant Framework & API [May 2023]
![**github stars**](https://img.shields.io/github/stars/superagent-ai/superagent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ThinkGPT✨](https://github.com/jina-ai/thinkgpt): Chain of Thoughts library [Apr 2023]
![**github stars**](https://img.shields.io/github/stars/jina-ai/thinkgpt?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **LLM Gateway**

1. [AI Gateway✨](https://github.com/Portkey-AI/gateway): AI Gateway with integrated guardrails. Route to 200+ LLMs, 50+ AI Guardrails [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/Portkey-AI/gateway?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [aisuite✨](https://github.com/andrewyng/aisuite): Andrew Ng launches a tool offering a simple, unified interface for multiple generative AI providers. [26 Nov 2024] ![**github stars**](https://img.shields.io/github/stars/andrewyng/aisuite?style=flat-square&label=%20&color=blue&cacheSeconds=36000) vs [litellm✨](https://github.com/BerriAI/litellm) vs [OpenRouter✨](https://github.com/OpenRouterTeam/openrouter-runner)
1. [litellm✨](https://github.com/BerriAI/litellm): Python SDK to call 100+ LLM APIs in OpenAI format [Jul 2023]
![**github stars**](https://img.shields.io/github/stars/BerriAI/litellm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LocalAI✨](https://github.com/mudler/LocalAI): The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/mudler/LocalAI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Petals✨](https://github.com/bigscience-workshop/petals): Run LLMs at home, BitTorrent-style. Fine-tuning and inference up to 10x faster than offloading [Jun 2022] ![**github stars**](https://img.shields.io/github/stars/bigscience-workshop/petals?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **LLM Memory**

1. [Agentic Memory✨](https://github.com/agiresearch/A-mem): A dynamic memory system for LLM agents, inspired by the Zettelkasten method, enabling flexible memory organization. [17 Feb 2025] ![**github stars**](https://img.shields.io/github/stars/agiresearch/A-mem?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [cognee✨](https://github.com/topoteretes/cognee): LLM Memory using Dynamic knowledge graphs (lightweight ECL pipelines) [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/topoteretes/cognee?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Graphiti✨](https://github.com/getzep/graphiti): Graphiti leverages [zep✨](https://github.com/getzep/zep)’s memory layer. Build Real-Time Knowledge Graphs for AI Agents [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/getzep/graphiti?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Letta (previously MemGPT)✨](https://github.com/letta-ai/letta): Virtual context management to extend the limited context of LLM. A tiered memory system and a set of functions that allow it to manage its own memory. [✍️](https://memgpt.ai) / [git:old✨](https://github.com/cpacker/MemGPT) [12 Oct 2023] ![**github stars**](https://img.shields.io/github/stars/letta-ai/letta?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Mem0✨](https://github.com/mem0ai/mem0):💡A self-improving memory layer for personalized AI experiences. [Jun 2023]
![**github stars**](https://img.shields.io/github/stars/mem0ai/mem0?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
    | [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory📑](https://alphaxiv.org/abs/2504.19413) [28 Apr 2025]  
1. [Memary✨](https://github.com/kingjulio8238/Memary): memary mimics how human memory evolves and learns over time. The memory module comprises the Memory Stream and Entity Knowledge Store. [May 2024] ![**github stars**](https://img.shields.io/github/stars/kingjulio8238/Memary?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenMemory✨](https://github.com/CaviraOSS/OpenMemory): Long-term memory for AI systems. Open source, self-hosted, and explainable. [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/CaviraOSS/OpenMemory?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [zep✨](https://github.com/getzep/zep): Long term memory layer. Zep intelligently integrates new information into the user's Knowledge Graph. ![**github stars**](https://img.shields.io/github/stars/getzep/zep?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [May 2023]

#### **LLM Application**

1. [aider✨](https://github.com/paul-gauthier/aider): AI pair programming in your terminal [Jan 2023]
![**github stars**](https://img.shields.io/github/stars/paul-gauthier/aider?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [anything-llm✨](https://github.com/Mintplex-Labs/anything-llm): All-in-one Desktop & Docker AI application with built-in RAG, AI agents, and more. [Jun 2023] ![**github stars**](https://img.shields.io/github/stars/Mintplex-Labs/anything-llm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Auto_Jobs_Applier_AIHawk✨](https://github.com/feder-cr/Auto_Jobs_Applier_AIHawk): automates the jobs application [Aug 2024]
![**github stars**](https://img.shields.io/github/stars/feder-cr/Auto_Jobs_Applier_AIHawk?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [BIG-AGI✨](https://github.com/enricoros/big-agi) FKA nextjs-chatgpt-app [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/enricoros/big-agi?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [BookGPT✨](https://github.com/mikavehns/BookGPT): Generate books based on your specification [Jan 2023]
![**github stars**](https://img.shields.io/github/stars/mikavehns/BookGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Cellm✨](https://github.com/getcellm/cellm): Use LLMs in Excel formulas [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/getcellm/cellm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ChatHub✨](https://github.com/chathub-dev/chathub): All-in-one chatbot client [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/chathub-dev/chathub?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Customer Service Chat with AI Assistant Handoff✨](https://github.com/pereiralex/Simple-bot-handoff-sample): Seamlessly hand off to a human agent when needed. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/pereiralex/Simple-bot-handoff-sample?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [dataline✨](https://github.com/RamiAwar/dataline): Chat with your data - AI data analysis and visualization [Apr 2023]
![**github stars**](https://img.shields.io/github/stars/RamiAwar/dataline?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Deepnote✨](https://github.com/deepnote/deepnote): A successor of Jupyter. a data notebook for the AI. [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/deepnote/deepnote?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Dialoqbase✨](https://github.com/n4ze3m/dialoqbase): Create custom chatbots with your own knowledge base using PostgreSQL [Jun 2023]
![**github stars**](https://img.shields.io/github/stars/n4ze3m/dialoqbase?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DocsGPT✨](https://github.com/arc53/docsgpt): Chatbot for document with your data [Feb 2023]
![**github stars**](https://img.shields.io/github/stars/arc53/docsgpt?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Geppeto✨](https://github.com/Deeptechia/geppetto): Advanced Slack bot using multiple AI models [Jan 2024]
![**github stars**](https://img.shields.io/github/stars/Deeptechia/geppetto?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [GPT Researcher✨](https://github.com/assafelovic/gpt-researcher): Autonomous agent designed for comprehensive online research [Jul 2023] / [GPT Newspaper✨](https://github.com/assafelovic/gpt-newspaper): Autonomous agent designed to create personalized newspapers [Jan 2024]
![**github stars**](https://img.shields.io/github/stars/assafelovic/gpt-researcher?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/assafelovic/gpt-newspaper?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [guardrails✨](https://github.com/guardrails-ai/guardrails): Adding guardrails to large language models. [Jan 2023]
![**github stars**](https://img.shields.io/github/stars/guardrails-ai/guardrails?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Inbox Zero✨](https://github.com/elie222/inbox-zero): AI personal assistant for email. [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/elie222/inbox-zero?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [knowledge✨](https://github.com/KnowledgeCanvas/knowledge): Tool for saving, searching, accessing, and exploring websites and files. Electron based app, built-in Chromium browser, knowledge graph [Jul 2021] ![**github stars**](https://img.shields.io/github/stars/KnowledgeCanvas/knowledge?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [KnowledgeGPT✨](https://github.com/mmz-001/knowledge_gpt): Upload your documents and get answers to your questions, with citations [Jan 2023]
![**github stars**](https://img.shields.io/github/stars/mmz-001/knowledge_gpt?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LibreChat✨](https://github.com/danny-avila/LibreChat): a free, open source AI chat platform. [8 Mar 2023] ![**github stars**](https://img.shields.io/github/stars/danny-avila/LibreChat?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [localGPT✨](https://github.com/PromtEngineer/localGPT): Chat with your documents on your local device [May 2023]
![**github stars**](https://img.shields.io/github/stars/PromtEngineer/localGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LlamaFS✨](https://github.com/iyaja/llama-fs): Automatically renames and organizes your files based on their contents [May 2024]
![**github stars**](https://img.shields.io/github/stars/iyaja/llama-fs?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Meetily✨](https://github.com/Zackriya-Solutions/meeting-minutes): Open source Ai Assistant for taking meeting notes [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/Zackriya-Solutions/meeting-minutes?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [myGPTReader✨](https://github.com/myreader-io/myGPTReader): Quickly read and understand any web content through conversations [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/myreader-io/myGPTReader?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Next.js AI Chatbot✨](https://github.com/vercel/ai-chatbot):💡An Open-Source AI Chatbot Template Built With Next.js and the AI SDK by Vercel. [May 2023] ![**github stars**](https://img.shields.io/github/stars/vercel/ai-chatbot?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Nyro✨](https://github.com/trynyro/nyro-app): AI-Powered Desktop Productivity Tool [Aug 2024]
![**github stars**](https://img.shields.io/github/stars/trynyro/nyro-app?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [open-notebook✨](https://github.com/lfnovo/open-notebook): An Open Source implementation of Notebook LM with more flexibility and features. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/lfnovo/open-notebook?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenBB✨](https://github.com/OpenBB-finance/OpenBB): The first financial Platform that is free and fully open source. AI-powered workspace [Dec 2020] ![**github stars**](https://img.shields.io/github/stars/OpenBB-finance/OpenBB?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PDF2Audio✨](https://github.com/lamm-mit/PDF2Audio): an open-source alternative to NotebookLM for podcast creation [Sep 2024]
![**github stars**](https://img.shields.io/github/stars/lamm-mit/PDF2Audio?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Podcastfy.ai✨](https://github.com/souzatharsis/podcastfy): An Open Source API alternative to NotebookLM's podcast feature. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/souzatharsis/podcastfy?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Postiz✨](https://github.com/gitroomhq/postiz-app): AI social media scheduling tool. An alternative to: Buffer.com, Hypefury, Twitter Hunter. [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/gitroomhq/postiz-app?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [pyspark-ai✨](https://github.com/pyspark-ai/pyspark-ai): English instructions and compile them into PySpark objects like DataFrames. [Apr 2023]
![**github stars**](https://img.shields.io/github/stars/pyspark-ai/pyspark-ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [screenshot-to-code✨](https://github.com/abi/screenshot-to-code): Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) [Nov 2023]
![**github stars**](https://img.shields.io/github/stars/abi/screenshot-to-code?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SolidGPT✨](https://github.com/AI-Citizen/SolidGPT): AI searching assistant for developers (VSCode Extension) [Aug 2023]
![**github stars**](https://img.shields.io/github/stars/AI-Citizen/SolidGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Strix✨](https://github.com/usestrix/strix): Open-source AI Hackers to secure your Apps. [Aug 2025] ![**github stars**](https://img.shields.io/github/stars/usestrix/strix?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SurfSense✨](https://github.com/MODSetter/SurfSense): Open-source alternative to NotebookLM, Perplexity, and Glean — integrates with your personal knowledge base, search engines, Slack, Linear, Notion, YouTube, and GitHub. ![**github stars**](https://img.shields.io/github/stars/MODSetter/SurfSense?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [July 2024]
1. [TaxyAI/browser-extension✨](https://github.com/TaxyAI/browser-extension): Browser Automation by Chrome debugger API and Prompt > `src/helpers/determineNextAction.ts` [Mar 2023]
1. [vanna✨](https://github.com/vanna-ai/vanna): Chat with your SQL database. Accurate Text-to-SQL Generation via LLMs using RAG. [May 2023]
![**github stars**](https://img.shields.io/github/stars/vanna-ai/vanna?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ValueCell✨](https://github.com/ValueCell-ai/valuecell): a community-driven, multi-agent platform for financial applications. [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/ValueCell-ai/valuecell?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **Code editor / Agent**

1. AI Code Editor: [Replit Agent](https://replit.com/) [09 Sep 2024] / [Cursor](https://www.cursor.com/) [Mar 2023]
1. [bolt.new✨](https://github.com/stackblitz/bolt.new): Dev Sanbox with AI from stackblitz [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/stackblitz/bolt.new?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Claude sub-agents collection✨](https://github.com/wshobson/agents): A collection of production-ready subagents for Claude Code. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/wshobson/agents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [claude-code✨](https://github.com/anthropics/claude-code): a terminal-based agentic coding tool that understands your codebase and speeds up development by executing tasks, explaining code, and managing git—all via natural language commands. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/anthropics/claude-code?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Claude Skills✨](https://github.com/anthropics/skills): Official repository for Skills. Skills teach Claude how to complete specific tasks in a repeatable way. [Sep 2025] [✍️](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) ![**github stars**](https://img.shields.io/github/stars/anthropics/skills?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [claude‑squad✨](https://github.com/smtg-ai/claude-squad): Terminal app to manage multiple AI assistants (Claude Code, Aider, Codex). [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/smtg-ai/claude-squad?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Cline✨](https://github.com/cline/cline): CLI aNd Editor. Autonomous coding agent. VSCode Extension. [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/cline/cline?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [code2prompt✨](https://github.com/mufeedvh/code2prompt/): a command-line tool (CLI) that converts your codebase into a single LLM prompt with a source tree [Mar 2024]
1. [Code Shaping✨](https://github.com/CodeShaping/code-shaping): Editing code with free-form sketch annotations on the code and console output. [6 Feb 2025] [ref📑](https://alphaxiv.org/abs/2502.03719) ![**github stars**](https://img.shields.io/github/stars/CodeShaping/code-shaping?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [CodeLLM by Abacus.AI](https://codellm.abacus.ai/): AI-powered code editor with automatic selection of state-of-the-art LLMs based on coding tasks. [Dec 2024]
1. [codegen✨](https://github.com/codegen-sh/codegen): Python SDK to interact with intelligent code generation agents [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/codegen-sh/codegen?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [codex✨](https://github.com/openai/codex): OpenAI. Lightweight coding agent that runs in your terminal [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/openai/codex?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Cofounder✨](https://github.com/raidendotai/cofounder): full stack generative web apps ; backend + db + stateful web apps [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/raidendotai/cofounder?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Continue✨](https://github.com/continuedev/continue): open-source AI code assistant inside of VS Code and JetBrains. [May 2023] ![**github stars**](https://img.shields.io/github/stars/continuedev/continue?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [crush✨](https://github.com/charmbracelet/crush): The glamorous AI coding agent for your favourite terminal. [May 2025] ![**github stars**](https://img.shields.io/github/stars/charmbracelet/crush?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DeepCode✨](https://github.com/HKUDS/DeepCode): Open Agentic Coding (Paper2Code & Text2Web & Text2Backend) [May 2025] ![**github stars**](https://img.shields.io/github/stars/HKUDS/DeepCode?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DeepSeek Engineer✨](https://github.com/Doriandarko/deepseek-engineer): Simple and just a few lines of code. a powerful coding assistant application that integrates with the DeepSeek API [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/Doriandarko/deepseek-engineer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DeepWiki](https://deepwiki.com/): Devin AI. a tool that converts any public GitHub repository into an interactive, wiki-style documentation. [25 Apr 2025]
1. [DeepWiki-Open✨](https://github.com/AsyncFuncAI/deepwiki-open): Open Source DeepWiki: AI-Powered Wiki Generator for GitHub/Gitlab/Bitbucket [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/AsyncFuncAI/deepwiki-open?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Deepsite🤗](https://huggingface.co/spaces/enzostvs/deepsite): Mockup UI generator Powered by Deepseek [Mar 2025]
1. [devin.cursorrules✨](https://github.com/grapeot/devin.cursorrules): Transform your Cursor or Windsurf IDE into a Devin-like AI Assistant [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/grapeot/devin.cursorrules?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Firebase Studio](https://firebase.google.com/studio): Google. a cloud-based, agentic development environment. [14 May 2024]
1. [Figma Make](https://www.figma.com/make/): Use existing Figma files or even images to kickstart your project. React（TypeScript）. Claude 3.7 Sonnet. [7 May 2025]
1. [Flowith Agent Neo](https://flowith.io): 24/7 operation for very long and complex tasks. Top of GAIA (General AI Assistant benchmark). 1,000 inference steps in a single task. Up to 10 million tokens of context. Cloud-based execution [21 May 2025]
1. [Gemini CLI✨](https://github.com/google-gemini/gemini-cli): An open-source AI agent that brings the power of Gemini directly into your terminal.  [April 2025] ![**github stars**](https://img.shields.io/github/stars/google-gemini/gemini-cli?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [GitHub Copilot✨](https://github.com/features/copilot):🏆 AI pair programmer by GitHub and OpenAI. Supports VS Code, Visual Studio, Neovim, and JetBrains IDEs. [29 Jun 2021] > [Awesome GitHub Copilot Customizations](https://github.com/github/awesome-copilot): Official curated collection.
1. [Github Spark](https://githubnext.com/projects/github-spark): an AI-powered tool for creating and sharing micro apps (“sparks”) [29 Oct 2024]
1. [GPT wrapper for git✨](https://github.com/di-sukharev/opencommit): GPT wrapper for git — generate commit messages with an LLM in 1 sec [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/di-sukharev/opencommit?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [HumanLayer✨](https://github.com/humanlayer/humanlayer): an open-source IDE that orchestrates AI coding agents to solve complex problems in large codebases [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/humanlayer/humanlayer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Kiro✨](https://github.com/kirodotdev/Kiro): AWS. an agentic IDE. [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/kirodotdev/Kiro?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Llama Coder✨](https://github.com/nutlope/llamacoder): Open source Claude Artifacts [✍️](https://llamacoder.together.ai/): demo [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/nutlope/llamacoder?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LLM Debugger✨](https://github.com/mohsen1/llm-debugger-vscode-extension): a VSCode extension that demonstrates the use of LLMs for active debugging of programs. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/mohsen1/llm-debugger-vscode-extension?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Micro Agent✨](https://github.com/BuilderIO/micro-agent): An AI agent that writes and fixes code for you. Test case driven code generation [May 2024] ![**github stars**](https://img.shields.io/github/stars/BuilderIO/micro-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [o1-engineer✨](https://github.com/Doriandarko/o1-engineer): a command-line tool designed to assist developers [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/Doriandarko/o1-engineer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [open-codex✨](https://github.com/ymichael/open-codex): a fork of the OpenAI Codex CLI with expanded model support [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/ymichael/open-codex?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [open-lovable✨](https://github.com/mendableai/open-lovable): Clone and recreate any website as a modern React app in seconds. [Aug 2025] ![**github stars**](https://img.shields.io/github/stars/mendableai/open-lovable?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [open-swe✨](https://github.com/langchain-ai/open-swe): An Open-Source Asynchronous Coding Agent. [May 2025] ![**github stars**](https://img.shields.io/github/stars/langchain-ai/open-swe?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Opal](https://opal.withgoogle.com/landing/): Google. Build, edit and share mini-AI apps using natural language [Jun 205]
1. [OpenHands✨](https://github.com/All-Hands-AI/OpenHands): OpenHands (formerly OpenDevin), a platform for software development agents [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Ruler✨](https://github.com/intellectronica/ruler): Centralise Your AI Coding Assistant Instructions [May 2025] ![**github stars**](https://img.shields.io/github/stars/intellectronica/ruler?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Task Master✨](https://github.com/eyaltoledano/claude-task-master): Personal Project Manager. A task management system for AI-driven development. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/eyaltoledano/claude-task-master?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Trae](https://www.trae.ai/): Bytedance. Free, but not open-source. [20 Jan 2025]
1. [Vercel AI✨](https://github.com/vercel/ai) Vercel AI Toolkit for TypeScript [May 2023] ![**github stars**](https://img.shields.io/github/stars/vercel/ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [void✨](https://github.com/voideditor/void) OSS Cursor alternative. a fork of vscode [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/voideditor/void?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [WebAgent✨](https://github.com/Alibaba-NLP/WebAgent): WebAgent for Information Seeking built by Tongyi Lab: WebWalker & WebDancer & WebSailor & WebShaper. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/Alibaba-NLP/WebAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Windsurf editor](https://codeium.com/windsurf): Flows = Agents + Copilots. Cascades (a specific implementation of AI Flows. Advanced chat interface). [13 Nov 2024]
1. [Zed✨](https://github.com/zed-industries/zed): a high-performance, multiplayer code editor. the creators of Atom and Tree-sitter. [Feb 2021] ![**github stars**](https://img.shields.io/github/stars/zed-industries/zed?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **UI/UX**

1. [anse✨](https://github.com/anse-app/anse): UI for multiple models such as ChatGPT, DALL-E and Stable Diffusion. [Apr 2023]
![**github stars**](https://img.shields.io/github/stars/anse-app/anse?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [chainlit✨](https://github.com/Chainlit/chainlit):💡Build production-ready Conversational AI applications in minutes. [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/Chainlit/chainlit?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [CopilotKit✨](https://github.com/CopilotKit/CopilotKit): Built-in React UI components [Jun 2023]
![**github stars**](https://img.shields.io/github/stars/CopilotKit/CopilotKit?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ElevenLabs UI✨](https://github.com/elevenlabs/ui): a component library built on top of shadcn/ui to help you build audio & agentic applications [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/elevenlabs/ui?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [GPT 学术优化 (GPT Academic)✨](https://github.com/binary-husky/gpt_academic): UI Platform for Academic & Coding Tasks. Optimized for paper reading, writing, and editing. [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/binary-husky/gpt_academic?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Gradio✨](https://github.com/gradio-app/gradio): Build Machine Learning Web Apps - in Python [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/gradio-app/gradio?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [mesop✨](https://github.com/mesop-dev/mesop): Rapidly build AI apps in Python [Oct 2023] ![**github stars**](https://img.shields.io/github/stars/mesop-dev/mesop?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. Open AI Chat Mockup: An open source ChatGPT UI. [mckaywrigley/chatbot-ui✨](https://github.com/mckaywrigley/chatbot-ui) [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/mckaywrigley/chatbot-ui?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Open WebUI✨](https://github.com/open-webui/open-webui): User-friendly AI Interface (Supports Ollama, OpenAI API, ...) [Oct 2023] ![**github stars**](https://img.shields.io/github/stars/open-webui/open-webui?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Open-source GPT Wrappers](https://star-history.com/blog/gpt-wrappers) 1. [ChatGPT-Next-Web✨](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web) [Mar 2023] 2. [FastGPT✨](https://github.com/labring/FastGPT) [Feb 2023] 3. [Lobe Chat✨](https://github.com/lobehub/lobe-chat) [Jan 2024]
![**github stars**](https://img.shields.io/github/stars/ChatGPTNextWeb/ChatGPT-Next-Web?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/labring/FastGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/lobehub/lobe-chat?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [streamlit✨](https://github.com/streamlit/streamlit):💡Streamlit — A faster way to build and share data apps. [Jan 2018] ![**github stars**](https://img.shields.io/github/stars/streamlit/streamlit?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Text generation web UI✨](https://github.com/oobabooga/text-generation-webui): Text generation web UI [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/oobabooga/text-generation-webui?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **Data Processing and Management**

1. [activeloopai/deeplake✨](https://github.com/activeloopai/deeplake): AI Vector Database for LLMs/LangChain. Doubles as a Data Lake for Deep Learning. Store, query, version, & visualize any data. Stream data in real-time to PyTorch/TensorFlow. [✍️](https://activeloop.ai) [Jun 2021]
![**github stars**](https://img.shields.io/github/stars/activeloopai/deeplake?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AI Sheets✨🤗](https://github.com/huggingface/aisheets): an open-source tool for building, enriching, and transforming datasets using AI models with no code. ![**github stars**](https://img.shields.io/github/stars/huggingface/aisheets?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Camelot✨](https://github.com/camelot-dev/camelot) a Python library that can help you extract tables from PDFs! [✨](https://github.com/camelot-dev/camelot/wiki/Comparison-with-other-PDF-Table-Extraction-libraries-and-tools): Comparison with other PDF Table Extraction libraries [Jul 2016]
![**github stars**](https://img.shields.io/github/stars/camelot-dev/camelot?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Crawl4AI✨](https://github.com/unclecode/crawl4ai): Open-source LLM Friendly Web Crawler & Scrapper [May 2024]
![**github stars**](https://img.shields.io/github/stars/unclecode/crawl4ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DocETL✨](https://github.com/ucbepic/docetl): Agentic LLM-powered data processing and ETL. Complex Document Processing Pipelines. [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/ucbepic/docetl?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [docling✨](https://github.com/DS4SD/docling): IBM. Docling parses documents and exports them to the desired format. [13 Nov 2024] ![**github stars**](https://img.shields.io/github/stars/DS4SD/docling?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [dolphin✨](https://github.com/bytedance/dolphin): The official repo for "Dolphin: Document Image Parsing via Heterogeneous Anchor Prompting", ACL, 2025. [May 2025] ![**github stars**](https://img.shields.io/github/stars/bytedance/dolphin?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [dots.ocr✨](https://github.com/rednote-hilab/dots.ocr): a powerful, multilingual document parser that unifies layout detection and content recognition within a single vision-language model (1.7B) [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/rednote-hilab/dots.ocr?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ExtractThinker✨](https://github.com/enoch3712/ExtractThinker): A Document Intelligence library for LLMs with ORM-style interaction for flexible workflows. [Apr 2024] ![**github stars**](https://img.shields.io/github/stars/enoch3712/ExtractThinker?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [firecrawl✨](https://github.com/mendableai/firecrawl): Scrap entire websites into LLM-ready markdown or structured data. [Apr 2024]
![**github stars**](https://img.shields.io/github/stars/mendableai/firecrawl?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Gitingest✨](https://github.com/cyclotruc/gitingest): Turn any Git repository into a prompt-friendly text ingest for LLMs. [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/cyclotruc/gitingest?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Instructor✨](https://github.com/jxnl/instructor): Structured outputs for LLMs, easily map LLM outputs to structured data. [Jun 2023]
![**github stars**](https://img.shields.io/github/stars/jxnl/instructor?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [langextract✨](https://github.com/google/langextract): Google. A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/google/langextract?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LLM Scraper✨](https://github.com/mishushakov/llm-scraper): a TypeScript library that allows you to extract structured data from any webpage using LLMs. [Apr 2024] ![**github stars**](https://img.shields.io/github/stars/mishushakov/llm-scraper?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Marker✨](https://github.com/VikParuchuri/marker): converts PDF to markdown [Oct 2023]
![**github stars**](https://img.shields.io/github/stars/VikParuchuri/marker?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [markitdown✨](https://github.com/microsoft/markitdown):💡Python tool for converting files and office documents to Markdown. [14 Nov 2024] ![**github stars**](https://img.shields.io/github/stars/microsoft/markitdown?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Maxun✨](https://github.com/getmaxun/maxun): Open-Source No-Code Web Data Extraction Platform [Oct 2023]
![**github stars**](https://img.shields.io/github/stars/getmaxun/maxun?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MegaParse✨](https://github.com/quivrhq/megaparse): a powerful and versatile parser that can handle various types of documents. Focus on having no information loss during parsing. [30 May 2024] ![**github stars**](https://img.shields.io/github/stars/quivrhq/megaparse?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Nougat📑](https://alphaxiv.org/abs/2308.13418): Neural Optical Understanding for Academic Documents: The academic document PDF parser that understands LaTeX math and tables. [✨](https://github.com/facebookresearch/nougat) [25 Aug 2023]
![**github stars**](https://img.shields.io/github/stars/facebookresearch/nougat?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Ollama OCR✨](https://github.com/imanoop7/Ollama-OCR): A powerful OCR (Optical Character Recognition) package that uses state-of-the-art vision language models. [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/imanoop7/Ollama-OCR?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [outlines✨](https://github.com/dottxt-ai/outlines): Structured Text Generation [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/dottxt-ai/outlines?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [pandas-ai✨](https://github.com/Sinaptik-AI/pandas-ai): Chat with your database (SQL, CSV, pandas, polars, mongodb, noSQL, etc). [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/Sinaptik-AI/pandas-ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Paperless-AI✨](https://github.com/clusterzx/paperless-ai): An automated document analyzer for Paperless-ngx using OpenAI API, Ollama and all OpenAI API compatible Services to automatically analyze and tag your documents. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/clusterzx/paperless-ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [pipet✨](https://github.com/bjesus/pipet): Swiss-army tool for scraping and extracting data from online [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/bjesus/pipet?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PostgresML✨](https://github.com/postgresml/postgresml): The GPU-powered AI application database. [Apr 2022]
![**github stars**](https://img.shields.io/github/stars/postgresml/postgresml?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [surya✨](https://github.com/VikParuchuri/surya): OCR, layout analysis, reading order, table recognition in 90+ languages [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/VikParuchuri/surya?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Trafilatura✨](https://github.com/adbar/trafilatura): Gather text from the web and convert raw HTML into structured, meaningful data. [Apr 2019]
![**github stars**](https://img.shields.io/github/stars/adbar/trafilatura?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Token-Oriented Object Notation (TOON)✨](https://github.com/toon-format/toon): a compact, human-readable serialization format designed for passing structured data with significantly reduced token usage. [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/toon-format/toon?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [unstructured✨](https://github.com/Unstructured-IO/unstructured): Open-Source Pre-Processing Tools for Unstructured Data [Sep 2022]
![**github stars**](https://img.shields.io/github/stars/Unstructured-IO/unstructured?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [WaterCrawl✨](https://github.com/watercrawl/WaterCrawl): Transform Web Content into LLM-Ready Data. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/watercrawl/WaterCrawl?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Zerox OCR✨](https://github.com/getomni-ai/zerox): Zero shot pdf OCR with gpt-4o-mini [Jul 2024]
![**github stars**](https://img.shields.io/github/stars/getomni-ai/zerox?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

<!-- #### **Sample code**

- Streaming with Azure OpenAI [SSE✨](https://github.com/thivy/azure-openai-js-stream) [May 2023]
![**github stars**](https://img.shields.io/github/stars/thivy/azure-openai-js-stream?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
![**github stars**](https://img.shields.io/github/stars/TaxyAI/browser-extension?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Embedding does not use Open AI. Can be executed locally: [pdfGPT✨](https://github.com/bhaskatripathi/pdfGPT) [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/bhaskatripathi/pdfGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Langchain Ask PDF (Tutorial): [✨](https://github.com/alejandro-ao/langchain-ask-pdf) [Apr 2023]
![**github stars**](https://img.shields.io/github/stars/alejandro-ao/langchain-ask-pdf?style=flat-square&label=%20&color=blue&cacheSeconds=36000) -->

### **Caching**

- Caching: A technique to store data that has been previously retrieved or computed, so that future requests for the same data can be served faster.
- To reduce latency, cost, and LLM requests by serving pre-computed or previously served responses.
- Strategies for caching: Caching can be based on item IDs, pairs of item IDs, constrained input, or pre-computation. Caching can also leverage embedding-based retrieval, approximate nearest neighbor search, and LLM-based evaluation. [✍️](https://eugeneyan.com/writing/llm-patterns/#caching-to-reduce-latency-and-cost)
- GPTCache: Semantic cache for LLMs. Fully integrated with LangChain and llama_index. [✨](https://github.com/zilliztech/GPTCache) [Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/zilliztech/GPTCache?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Prompt Cache: Modular Attention Reuse for Low-Latency Inference📑](https://alphaxiv.org/abs/2311.04934): LLM inference by reusing precomputed attention states from overlapping prompts. [7 Nov 2023]
- [Prompt caching with Claude✍️](https://www.anthropic.com/news/prompt-caching): Reducing costs by up to 90% and latency by up to 85% for long prompts. [15 Aug 2024]

### **Defensive UX**

- Defensive UX: A design strategy that aims to prevent and handle errors in user interactions with machine learning or LLM-based products.
- Why defensive UX?: Machine learning and LLMs can produce inaccurate or inconsistent output, which can affect user trust and satisfaction. Defensive UX can help by increasing accessibility, trust, and UX quality.
- [Guidelines for Human-AI Interaction✍️](https://www.microsoft.com/en-us/research/publication/guidelines-for-human-ai-interaction/): Microsoft: Based on a survey of 168 potential guidelines from various sources, they narrowed it down to 18 action rules organized by user interaction stages.
- [People + AI Guidebook](https://pair.withgoogle.com/guidebook/): Google: Google’s product teams and academic research, they provide 23 patterns grouped by common questions during the product development process3.
- [Human Interface Guidelines for Machine Learning](https://developer.apple.com/design/human-interface-guidelines/machine-learning): Apple: Based on practitioner knowledge and experience, emphasizing aspects of UI rather than model functionality4.

### **Proposals & Glossary**

- [A2A✨](https://github.com/google/A2A): Google. Agent2Agent (A2A) protocol. Agent Card (metadata: self-description). Task (a unit of work). Artifact (output). Streaming (Long-running tasks). Leverages HTTP, SSE, and JSON-RPC. Multi-modality incl. interacting with UI components [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/google/A2A?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Agent Payments Protocol (AP2)✨](https://github.com/google-agentic-commerce/AP2): an open-source protocol developed by Google to enable secure, interoperable AI-driven payments between agents [May 2025] ![**github stars**](https://img.shields.io/github/stars/google-agentic-commerce/AP2?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Agentic Commerce Protocol (ACP)✨](https://github.com/agentic-commerce-protocol/agentic-commerce-protocol): an interaction model and open standard for connecting buyers, their AI agents [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/agentic-commerce-protocol/agentic-commerce-protocol?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Context Engineering: [tweet from Shopify CEO Tobi Lutke](https://x.com/tobi/status/1935533422589399127), [tweet from Andrej Karpathy](https://x.com/karpathy/status/1937902205765607626), [The New Skill in AI is Not Prompting, It's Context Engineering](https://www.philschmid.de/context-engineering) [Jun 2025]
- [AGENTS.md](https://agents.md/): AGENTS.md as a README for agents. [✨](https://github.com/openai/agents.md) [Aug 2025]
- [/llms.txt](https://llmstxt.org/): Proposal for an `/llms.txt` file to guide LLMs in using websites during inference. [✨](https://github.com/answerdotai/llms-txt) [3 Sep 2024]
 ![**github stars**](https://img.shields.io/github/stars/answerdotai/llms-txt?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Model Context Protocol (MCP)✍️](https://www.anthropic.com/news/model-context-protocol): Anthropic proposes an open protocol for seamless LLM integration with external data and tools. [✨](https://github.com/modelcontextprotocol/servers) [26 Nov 2024]
 ![**github stars**](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [🔗](#computer-use--mcp)
- [Spec-Driven Development✨](https://github.com/github/spec-kit): Unlike conventional coding where specs are just guides, it makes specifications executable, directly producing working implementations. [Aug 2025] ![**github stars**](https://img.shields.io/github/stars/github/spec-kit?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [The future of AI agents—and why OAuth must evolve✍️](https://techcommunity.microsoft.com/blog/microsoft-entra-blog/the-future-of-ai-agents%E2%80%94and-why-oauth-must-evolve/3827391): OAuth 2.0 wasn’t built for autonomous AI agents—Microsoft proposes evolving it with agent identities, dynamic permissions, and cross-agent trust. [28 May 2025]
- [Unmetered Intelligence](https://www.zackkass.com/publications): Always-on, unlimited, adaptive intelligence — not bound by usage limits or fixed capacities.
- [Vibe Coding](https://en.wikipedia.org/wiki/Vibe_coding): a method where programmers explain their goals in simple language, and AI creates the code. Suggested by Andrej Karpathy in February 2025, it changes the programmer's role to guiding, testing, and improving the AI's work. [Feb 2025]

### **LLM for Robotics**

- PromptCraft-Robotics: Robotics and a robot simulator with ChatGPT integration [✨](https://github.com/microsoft/PromptCraft-Robotics) [Feb 2023]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/PromptCraft-Robotics?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- ChatGPT-Robot-Manipulation-Prompts: A set of prompts for Communication between humans and robots for executing tasks. [✨](https://github.com/microsoft/ChatGPT-Robot-Manipulation-Prompts) [Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/ChatGPT-Robot-Manipulation-Prompts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Siemens Industrial Copilot [✍️](https://news.microsoft.com/2023/10/31/siemens-and-microsoft-partner-to-drive-cross-industry-ai-adoption/)  [31 Oct 2023]
- [LeRobot🤗](https://huggingface.co/lerobot): Hugging Face. LeRobot aims to provide models, datasets, and tools for real-world robotics in PyTorch. [✨](https://github.com/huggingface/lerobot) [Jan 2024]
 ![**github stars**](https://img.shields.io/github/stars/huggingface/lerobot?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Mobile ALOHA](https://mobile-aloha.github.io/): Stanford’s mobile ALOHA robot learns from humans to cook, clean, do laundry. Mobile ALOHA extends the original ALOHA system by mounting it on a wheeled base [✍️](https://venturebeat.com/automation/stanfords-mobile-aloha-robot-learns-from-humans-to-cook-clean-do-laundry/) [4 Jan 2024] / [ALOHA](https://www.trossenrobotics.com/aloha.aspx): A Low-cost Open-source Hardware System for Bimanual Teleoperation.
- [Figure 01 + OpenAI](https://www.figure.ai/): Humanoid Robots Powered by OpenAI ChatGPT [📺](https://youtu.be/Sq1QZB5baNw?si=wyufZA1xtTYRfLf3) [Mar 2024]
- [Gemini Robotics](https://deepmind.google/discover/blog/gemini-robotics-brings-ai-into-the-physical-world/): Robotics built on the foundation of Gemini 2.0 [12 Mar 2025]

### **Awesome demo**

- [FRVR Official Teaser📺](https://youtu.be/Yjjpr-eAkqw): Prompt to Game: AI-powered end-to-end game creation [16 Jun 2023]
- [rewind.ai](https://www.rewind.ai/): Rewind captures everything you’ve seen on your Mac and iPhone [Nov 2023]
- [Vercel announced V0.dev](https://v0.dev/chat/AjJVzgx): Make a snake game with chat [Oct 2023]
- [Mobile ALOHA📺](https://youtu.be/HaaZ8ss-HP4?si=iMYKzvx8wQhf39yU): A day of Mobile ALOHA [4 Jan 2024]
- [groq✨](https://github.com/groq): An LPU Inference Engine, the LPU is reported to be 10 times faster than NVIDIA’s GPU performance [✍️](https://www.gamingdeputy.com/groq-unveils-worlds-fastest-large-model-500-tokens-per-second-shatters-record-self-developed-lpu-outperforms-nvidia-gpu-by-10-times/) [Jan 2024]
- [Sora📺](https://youtu.be/HK6y8DAPN_0?si=FPZaGk4fP2d456QP): Introducing Sora — OpenAI’s text-to-video model [Feb 2024]
- [Oasis✍️](https://www.etched.com/blog-posts/oasis): Minecraft clone. Generated by AI in Real-Time. The first playable AI model that generates open-world games. [✍️](https://oasis-model.github.io/) [✨](https://github.com/etched-ai/open-oasis) [31 Oct 2024] ![**github stars**](https://img.shields.io/github/stars/etched-ai/open-oasis?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

## **Agent**

#### **Agentic Design Frameworks**

- [AIAgentToolkit.xyz](https://www.aiagenttoolkit.xyz): A curated list of AI agent frameworks, launchpads, tools, tutorials, & resources.
- [Agent Leaderboard🤗](https://huggingface.co/spaces/galileo-ai/agent-leaderboard)
- [Agent Leaderboard v2✨](https://github.com/rungalileo/agent-leaderboard) ![**github stars**](https://img.shields.io/github/stars/rungalileo/agent-leaderboard?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Agentic Design Frameworks focus on managing autonomous or semi-autonomous AI agents for complex tasks.
- e.g., [Autogen✨](https://github.com/microsoft/autogen), and [crewAI✨](https://github.com/joaomdmoura/CrewAI)
 ![**github stars**](https://img.shields.io/github/stars/microsoft/autogen?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/joaomdmoura/CrewAI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

##### **Top Agent Frameworks ranked by GitHub Star Counts**

[AG2✨](https://github.com/ag2ai/ag2) ![**github stars**](https://img.shields.io/github/stars/ag2ai/ag2?style=flat-square&label=%20&cacheSeconds=36000) > [Agno✨](https://github.com/agno-agi/agno) ![**github stars**](https://img.shields.io/github/stars/agno-agi/agno?style=flat-square&label=%20&cacheSeconds=36000) > [AWS Bedrock Agents✨](https://github.com/awslabs/amazon-bedrock-agent-samples) ![**github stars**](https://img.shields.io/github/stars/awslabs/amazon-bedrock-agent-samples?style=flat-square&label=%20&cacheSeconds=36000) > [CrewAI✨](https://github.com/crewAIInc/crewAI) ![**github stars**](https://img.shields.io/github/stars/crewAIInc/crewAI?style=flat-square&label=%20&cacheSeconds=36000) > [Google ADK✨](https://github.com/google/adk-python) ![**github stars**](https://img.shields.io/github/stars/google/adk-python?style=flat-square&label=%20&cacheSeconds=36000) > [LangChain✨](https://github.com/langchain-ai/langchain) ![**github stars**](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square&label=%20&cacheSeconds=36000) > [LangGraph✨](https://github.com/langchain-ai/langgraph) ![**github stars**](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square&label=%20&cacheSeconds=36000) > [LlamaIndex✨](https://github.com/run-llama/llama_index)  ![**github stars**](https://img.shields.io/github/stars/run-llama/llama_index?style=flat-square&label=%20&cacheSeconds=36000) > [Mastra✨](https://github.com/mastra-ai/mastra) ![**github stars**](https://img.shields.io/github/stars/mastra-ai/mastra?style=flat-square&label=%20&cacheSeconds=36000) > [OpenAI Agent SDK✨](https://github.com/openai/openai-agents-python) ![**github stars**](https://img.shields.io/github/stars/openai/openai-agents-python?style=flat-square&label=%20&cacheSeconds=36000) > [Pydantic AI✨](https://github.com/pydantic/pydantic-ai) ![**github stars**](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=flat-square&label=%20&cacheSeconds=36000) > [Strands Agents SDK✨](https://github.com/strands-agents/sdk-python) ![**github stars**](https://img.shields.io/github/stars/strands-agents/sdk-python?style=flat-square&label=%20&cacheSeconds=36000) > [Vercel AI SDK✨](https://github.com/vercel/ai) ![**github stars**](https://img.shields.io/github/stars/vercel/ai?style=flat-square&label=%20&cacheSeconds=36000)

#### **Agent Design Patterns**
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
    - Framework: [Autogen✨](https://github.com/microsoft/autogen) / [LangGraph✨](https://github.com/langchain-ai/langgraph) / [crewAI✨](https://github.com/joaomdmoura/CrewAI)
 ![**github stars**](https://img.shields.io/github/stars/microsoft/autogen?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/joaomdmoura/CrewAI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Agentic Design Patterns✍️](https://docs.google.com/document/d/1rsaK53T3Lg5KoGwvf8ukOUvbELRtH-V0LnOIFDxBryE/edit?tab=t.0#heading=h.pxcur8v2qagu): Google Docs. A Hands-On Guide to Building Intelligent Systems. [🗄️](./files/archive/Agentic_Design_Patterns.docx) [May 2025]
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
- [How we built our multi-agent research system✍️](https://www.anthropic.com/engineering/built-multi-agent-research-system): Anthrophic. [13 Jun 2025]
- [Hugging Face Agents Course✨](https://github.com/huggingface/agents-course) 🤗 Hugging Face Agents Course. [Jan 2025]
- [Language Agent Tree Search Method (LATS)✨](https://github.com/lapisrocks/LanguageAgentTreeSearch): LATS leverages an external environment and an MCTS (Monte Carlo Tree Search)-based search [6 Oct 2023] ![**github stars**](https://img.shields.io/github/stars/lapisrocks/LanguageAgentTreeSearch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Taxonomy of failure modes in AI agents ✍️](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents): Microsoft AI Red Team (AIRT) has categorized identified failure modes into two types: novel and existing, under the pillars of safety and security. [24 Apr 2025]
- [The Different Ochestration Frameworks](https://newsletter.theaiedge.io/p/implementing-a-language-agent-tree):💡Orchestration frameworks for LLM applications: Micro-orchestration / Macro-orchestration / Agentic Design Frameworks / Optimizer frameworks [11 Oct 2024]
- [The Rise and Potential of Large Language Model Based Agents: A Survey📑](https://alphaxiv.org/abs/2309.07864): The papers list for LLM-based agents [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.07864)] / [✨](https://github.com/WooooDyy/LLM-Agent-Paper-List) [14 Sep 2023]
 ![**github stars**](https://img.shields.io/github/stars/WooooDyy/LLM-Agent-Paper-List?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [When One AI Agent Isn't Enough - Building Multi-Agent Systems✍️](https://diamantai.substack.com/p/when-one-ai-agent-isnt-enough-building): When Multi-Agent Systems Make Sense: Complex subtasks, diverse expertise, parallel speed, easy scaling, and multi-entity problems. [Jul 14]
- [Zero to One: Learning Agentic Patterns](https://www.philschmid.de/agentic-pattern):💡Structured `workflows` follow fixed paths, while `agentic patterns` allow autonomous, dynamic decision-making. Sample code using Gemini. [5 May 2025]

#### **Tool use: LLM to Master APIs**

- [APIGen📑](https://alphaxiv.org/abs/2406.18518): Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets [26 Jun 2024]
- [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard_live.html) V2 [Aug 2024]
- [Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models📑](https://alphaxiv.org/abs/2304.09842): Different tasks require different tools, and different models show different tool preferences—e.g., ChatGPT favors image captioning, while GPT-4 leans toward knowledge retrieval. [Tool transition](https://chameleon-llm.github.io/) [19 Apr 2023]
- [Gorilla: An API store for LLMs📑](https://alphaxiv.org/abs/2305.15334): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.15334)]: Gorilla: Large Language Model Connected with Massive APIs. 1,645 APIs. [✨](https://github.com/ShishirPatil/gorilla) [24 May 2023] ![**github stars**](https://img.shields.io/github/stars/ShishirPatil/gorilla?style=flat-square&label=%20&color=blue&cacheSeconds=36000)  
  1. Used GPT-4 to generate a dataset of instruction-api pairs for fine-tuning Gorilla.  
  1. Used the abstract syntax tree (AST) of the generated code to match with APIs in the database and test set for evaluation purposes.  
  > Another user asked how Gorilla compared to LangChain; Patil replied: LangChain is a terrific project that tries to teach agents how to use tools using prompting. Our take on this is that prompting is not scalable if you want to pick between 1000s of APIs. So Gorilla is a LLM that can pick and write the semantically and syntactically correct API for you to call! A drop in replacement into LangChain! [cite✍️](https://www.infoq.com/news/2023/07/microsoft-gorilla/) [04 Jul 2023]  
- [Toolformer📑](https://alphaxiv.org/abs/2302.04761): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2302.04761)]: Language Models That Can Use Tools, by MetaAI. Finetuned GPT-J to learn 5 tools. [✨](https://github.com/lucidrains/toolformer-pytorch) [9 Feb 2023]
 ![**github stars**](https://img.shields.io/github/stars/lucidrains/toolformer-pytorch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [ToolLLM📑](https://alphaxiv.org/abs/2307.16789): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.16789)]: : Facilitating Large Language Models to Master 16000+ Real-world APIs [✨](https://github.com/OpenBMB/ToolBench) [31 Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/OpenBMB/ToolBench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [ToolShed📑](https://alphaxiv.org/abs/2410.14594): Toolshed Knowledge Bases & Advanced RAG-Tool Fusion, optimized for storing and retrieving tools in a vector database for large-scale agents. To address the limitations of primary methods, two approaches are: 1. tuning-based tool calling via LLM fine-tuning, and 2. retriever-based tool selection and planning. [18 Oct 2024]
- [Voyager: An Open-Ended Embodied Agent with Large Language Models📑](https://alphaxiv.org/abs/2305.16291): The 'Skill Library' in Voyager functions like a skill manager, storing and organizing learned behaviors or code snippets that the agent can reuse and combine to solve various tasks in the Minecraft environment. [25 May 2023]

#### **Model Context Protocol (MCP), A2A, Computer use**

##### Model Context Protocol (MCP)

- [A Survey of AI Agent Protocols📑](https://alphaxiv.org/abs/2504.16736) [23 Apr 2025]
- [Awesome MCP Servers✨](https://github.com/punkpeye/awesome-mcp-servers) ![**github stars**](https://img.shields.io/github/stars/punkpeye/awesome-mcp-servers?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Docker MCP Toolkit and MCP Catalog](https://www.docker.com/products/mcp-catalog-and-toolkit): `docker mcp` [5 May 2025]
- [Model Context Protocol (MCP)✍️](https://www.anthropic.com/news/model-context-protocol): Anthropic proposes an open protocol for seamless LLM integration with external data and tools. [✨](https://github.com/modelcontextprotocol/servers) [26 Nov 2024]
 ![**github stars**](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [mcp.so](https://mcp.so/): Find Awesome MCP Servers and Clients
- [Postman launches full support for Model Context Protocol (MCP)✍️](https://blog.postman.com/postman-launches-full-support-for-model-context-protocol-mcp-build-better-ai-agents-faster/) [1 May 2025]
1. [5ire✨](https://github.com/nanbingxyz/5ire): a cross-platform desktop AI assistant, MCP client. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/nanbingxyz/5ire?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ACI.dev ✨](https://github.com/aipotheosis-labs/aci): Unified Model-Context-Protocol (MCP) server (Built-in OAuth flows) [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/aipotheosis-labs/aci?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AWS MCP Servers✨](https://github.com/awslabs/mcp): MCP servers that bring AWS best practices [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/awslabs/mcp?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [Azure MCP Server✨](https://github.com/Azure/azure-mcp): connection between AI agents and key Azure services like Azure Storage, Cosmos DB, and more. [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/Azure/azure-mcp?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [Code execution with MCP✍️](https://www.anthropic.com/engineering/code-execution-with-mcp): This approach uses only the input, code, and output summary for tokens, reducing token usage by up to 95% compared to generic MCP calls. [04 Nov 2025]
1. [Context7✨](https://github.com/upstash/context7): Up-to-date code documentation for LLMs and AI code editors [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/upstash/context7?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [DeepMCPAgent✨](https://github.com/cryxnet/DeepMCPAgent): a model-agnostic framework for plug-and-play LangChain/LangGraph agents using MCP tools dynamically over HTTP/SSE. [Aug 2025] ![**github stars**](https://img.shields.io/github/stars/cryxnet/DeepMCPAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [fastapi_mcp✨](https://github.com/tadata-org/fastapi_mcp): automatically exposing FastAPI endpoints as Model Context Protocol (MCP) [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/tadata-org/fastapi_mcp?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [goose✨](https://github.com/block/goose):💡An open-source, extensible AI agent with support for the Model Context Protocol (MCP). Developed by Block, a company founded in 2009 by Jack Dorsey. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/block/goose?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Hugging Face MCP Course🤗](https://huggingface.co/mcp-course): Model Context Protocol (MCP) Course
1. [MCP Registry](https://github.com/mcp): Github. centralizes Model Context Protocol (MCP) servers, facilitating the discovery and integration of AI tools with external data sources and services. [16 Sep 2025]
1. [MCP Run Python](https://ai.pydantic.dev/mcp/run-python/): PydanticAI. Use Pyodide to run Python code in a JavaScript environment with Deno [19 Mar 2025]
1. [mcp-agent✨](https://github.com/lastmile-ai/mcp-agent): Build effective agents using Model Context Protocol and simple workflow patterns [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/lastmile-ai/mcp-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [mcp-ui✨](https://github.com/idosal/mcp-ui): SDK for UI over MCP. Create next-gen UI experiences! [May 2025] ![**github stars**](https://img.shields.io/github/stars/idosal/mcp-ui?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [mcp-use✨](https://github.com/mcp-use/mcp-use): MCP Client Library to connect any LLM to any MCP server [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/mcp-use/mcp-use?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 

#### A2A

1. [A2A✨](https://github.com/google/A2A): Google. Agent2Agent (A2A) protocol. Agent Card (metadata: self-description). Task (a unit of work). Artifact (output). Streaming (Long-running tasks). Leverages HTTP, SSE, and JSON-RPC. Multi-modality incl. interacting with UI components [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/google/A2A?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [a2a-python✨](https://github.com/google-a2a/a2a-python): Official Python SDK for the Agent2Agent (A2A) Protocol [May 2025] ![**github stars**](https://img.shields.io/github/stars/google-a2a/a2a-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AI Agent Architecture via A2A/MCP](https://medium.com/@jeffreymrichter/ai-agent-architecture-b864080c4bbc): Jeffrey Richter [4 Jun 2025]
1. [Python A2A✨](https://github.com/themanojdesai/python-a2a): Python Implementation of Google's Agent-to-Agent (A2A) Protocol with Model Context Protocol (MCP) Integration [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/themanojdesai/python-a2a?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SharpA2A✨](https://github.com/darrelmiller/sharpa2a): A .NET implementation of the Google A2A protocol. [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/darrelmiller/sharpa2a?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

##### Computer use

- [ACU - Awesome Agents for Computer Use✨](https://github.com/francedot/acu) ![**github stars**](https://img.shields.io/github/stars/francedot/acu?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Anthropic Claude's computer use✍️](https://www.anthropic.com/news/developing-computer-use): [23 Oct 2024]
- [Computer Agent Arena Leaderboard](https://arena.xlang.ai/leaderboard) [Apr 2025]
1. [Agent.exe✨](https://github.com/corbt/agent.exe): Electron app to use computer use APIs. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/corbt/agent.exe?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [CogAgent✨](https://github.com/THUDM/CogAgent): An open-sourced end-to-end VLM-based GUI Agent [Dec 2023] ![**github stars**](https://img.shields.io/github/stars/THUDM/CogAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Computer Use OOTB✨](https://github.com/showlab/computer_use_ootb): Out-of-the-box (OOTB) GUI Agent for Windows and macOS. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/showlab/computer_use_ootb?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [cua✨](https://github.com/trycua/cua): Open-source infrastructure for Computer-Use Agents. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/trycua/cua?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Open-Interface✨](https://github.com/AmberSahdev/Open-Interface/): LLM backend (GPT-4V, etc), supporting Linux, Mac, Windows. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/AmberSahdev/Open-Interface?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Open Operator✨](https://github.com/browserbase/open-operator): a web agent based on Browserbase [24 Jan 2025] ![**github stars**](https://img.shields.io/github/stars/browserbase/open-operator?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [OpenAI Operator✍️](https://openai.com/index/introducing-operator/) [🔗](#openai-products) [23 Jan 2025]
1. [OpenInterpreter starts to support Computer Use API✨](https://github.com/OpenInterpreter/open-interpreter/issues/1490)
1. [Self-Operating Computer Framework✨](https://github.com/OthersideAI/self-operating-computer): A framework to enable multimodal models to operate a computer. [Nov 2023] ![**github stars**](https://img.shields.io/github/stars/OthersideAI/self-operating-computer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Stagehand✨](https://github.com/browserbase/stagehand): The AI Browser Automation Framework . Stagehand lets you preview AI actions before running. Computer use models with one line of code. [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/browserbase/stagehand?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [UI-TARS📑](https://alphaxiv.org/abs/2501.12326): An agent model built on Qwen-2-VL for seamless GUI interaction, by ByteDance. [✨](https://github.com/bytedance/UI-TARS) / Application [✨](https://github.com/bytedance/UI-TARS-desktop) ![**github stars**](https://img.shields.io/github/stars/bytedance/UI-TARS-desktop?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [21 Jan 2025]
1. [🔗](#agent) > [UFO✨](https://github.com/microsoft/UFO): Windows Control

#### **Memory Layer**

- [🔗](#llm-memory)

#### **Agent Framework**

##### Agent Framework

1. [Agno✨](https://github.com/agno-agi/agno):💡Build Multimodal AI Agents with memory, knowledge and tools. Simple, fast and model-agnostic. [Nov 2023] ![**github stars**](https://img.shields.io/github/stars/agno-agi/agno?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. Agent Framework used in MLE-bench: GPT-4o (AIDE) earned the highest score [🔗](#evaluating-large-language-models)
    - [AIDE✨](https://github.com/WecoAI/aideml): The state-of-the-art machine learning engineer agent [Apr 2024]
    ![**github stars**](https://img.shields.io/github/stars/WecoAI/aideml?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
    - [OpenHands✨](https://github.com/All-Hands-AI/OpenHands): OpenHands (formerly OpenDevin), a platform for software development agents [Mar 2024]
    ![**github stars**](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
    - [MLAB ResearchAgent✨](https://github.com/snap-stanford/MLAgentBench): Evaluating Language Agents on Machine Learning Experimentation [Aug 2023]
    ![**github stars**](https://img.shields.io/github/stars/snap-stanford/MLAgentBench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Agent-S✨](https://github.com/simular-ai/Agent-S): To build intelligent GUI agents that autonomously learn and perform complex tasks on your computer. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/simular-ai/Agent-S?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Agentarium✨](https://github.com/Thytu/Agentarium): a framework for creating and managing simulations populated with AI-powered agents. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/Thytu/Agentarium?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AgentOps✨](https://github.com/AgentOps-AI/agentops):Python SDK for AI agent monitoring, LLM cost tracking, benchmarking. [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/AgentOps-AI/agentops?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AgentScope✨](https://github.com/modelscope/agentscope): To build LLM-empowered multi-agent applications. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/modelscope/agentscope?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AgentVerse✨](https://github.com/OpenBMB/AgentVerse): Primarily providing: task-solving and simulation. [May 2023] ![**github stars**](https://img.shields.io/github/stars/OpenBMB/AgentVerse?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Anus: Autonomous Networked Utility System✨](https://github.com/nikmcfly/ANUS): An open-source AI agent framework for task automation, multi-agent collaboration, and web interactions. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/nikmcfly/ANUS?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Atomic Agents✨](https://github.com/BrainBlend-AI/atomic-agents): an extremely lightweight and modular framework for building Agentic AI pipelines [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/BrainBlend-AI/atomic-agents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AutoAgent✨](https://github.com/HKUDS/AutoAgent): AutoAgent: Fully-Automated and Zero-Code LLM Agent Framework ![**github stars**](https://img.shields.io/github/stars/HKUDS/AutoAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AWS: Multi-Agent Orchestrator✨](https://github.com/awslabs/multi-agent-orchestrator): a framework for managing multiple AI agents and handling complex conversations. [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/awslabs/multi-agent-orchestrator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Bee Agent Framework✨](https://github.com/i-am-bee/bee-agent-framework): IBM. The TypeScript framework for building scalable agentic applications. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/i-am-bee/bee-agent-framework?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Botpress Cloud✨](https://github.com/botpress/botpress): The open-source hub to build & deploy GPT/LLM Agents. [Nov 2016] ![**github stars**](https://img.shields.io/github/stars/botpress/botpress?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Burr✨](https://github.com/dagworks-inc/burr): Create an application as a state machine (graph/flowchart) for managing state, decisions, human feedback, and workflows. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/dagworks-inc/burr?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Cheshire-Cat (Stregatto)✨](https://github.com/cheshire-cat-ai/core): Framework to build custom AIs with memory and plugins [Feb 2023] ![**github stars**](https://img.shields.io/github/stars/cheshire-cat-ai/core?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Claude Agent SDK for Python✨](https://github.com/anthropics/claude-agent-sdk-python) [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/anthropics/claude-agent-sdk-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [composio✨](https://github.com/ComposioHQ/composio): Integration of Agents with 100+ Tools [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/ComposioHQ/composio?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [crewAI✨](https://github.com/joaomdmoura/CrewAI):💡Framework for orchestrating role-playing, autonomous AI agents. [Oct 2023] ![**github stars**](https://img.shields.io/github/stars/joaomdmoura/CrewAI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Dagger✨](https://github.com/dagger/dagger): an open-source runtime for composable workflows. [Nov 2019] ![**github stars**](https://img.shields.io/github/stars/dagger/dagger?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Dynamiq✨](https://github.com/dynamiq-ai/dynamiq): An orchestration framework for RAG, agentic AI, and LLM applications [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/dynamiq-ai/dynamiq?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Eko (pronounced like ‘echo’) ✨](https://github.com/FellouAI/eko): Pure JavaScript. Build Production-ready Agentic Workflow with Natural Language. Support Browser use & Computer use [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/FellouAI/eko?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Google ADK✨](https://github.com/google/adk-python): Agent Development Kit (ADK) [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/google/adk-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Huginn✨](https://github.com/huginn/huginn): A hackable version of IFTTT or Zapier on your own server for building agents that perform automated tasks. [Mar 2013] ![**github stars**](https://img.shields.io/github/stars/huginn/huginn?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Lagent✨](https://github.com/InternLM/lagent): Inspired by the design philosophy of PyTorch. A lightweight framework for building LLM-based agents. [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/InternLM/lagent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LangGraph✨](https://github.com/langchain-ai/langgraph): Built on top of LangChain [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [maestro✨](https://github.com/Doriandarko/maestro): A Framework for Claude Opus, GPT, and local LLMs to Orchestrate Subagents [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/Doriandarko/maestro?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Mastra✨](https://github.com/mastra-ai/mastra): The TypeScript AI agent framework. workflows, agents, RAG, integrations and evals. [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/mastra-ai/mastra?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MetaGPT✨](https://github.com/geekan/MetaGPT): Multi-Agent Framework. Assign different roles to GPTs to form a collaborative entity for complex tasks. e.g., Data Interpreter [Jun 2023] ![**github stars**](https://img.shields.io/github/stars/geekan/MetaGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. Microsoft Agent Frameworks [🔗](#microsoft-azure-openai-relevant-llm-framework)
1. [n8n✨](https://github.com/n8n-io/n8n): A workflow automation tool for integrating various tools. [Jan 2019] ![**github stars**](https://img.shields.io/github/stars/n8n-io/n8n?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Open AI Assistant API](https://platform.openai.com/docs/assistants/overview) [6 Nov 2023]
1. [OpenAgents✨](https://github.com/xlang-ai/OpenAgents): Three distinct agents: Data Agent for data analysis, Plugins Agent for plugin integration, and Web Agent for autonomous web browsing. [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/xlang-ai/OpenAgents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenAI Agents SDK & Response API✨](https://github.com/openai/openai-agents-python):🏆Responses API (Chat Completions + Assistants API), Built-in tools (web search, file search, computer use), Agents SDK for multi-agent workflows, agent workflow observability tools [11 Mar 2025] ![**github stars**](https://img.shields.io/github/stars/openai/openai-agents-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenAI Swarm✨](https://github.com/openai/swarm): An experimental and educational framework for lightweight multi-agent orchestration. [11 Oct 2024] ![**github stars**](https://img.shields.io/github/stars/openai/swarm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenEnv✨](https://github.com/meta-pytorch/OpenEnv): An e2e framework for isolated execution environments for agentic RL training, built using Gymnasium style simple APIs. [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/meta-pytorch/OpenEnv?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OWL: Optimized Workforce Learning✨](https://github.com/camel-ai/owl): a multi-agent collaboration framework built on CAMEL-AI, enhancing task automation [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/camel-ai/owl?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [parlant✨](https://github.com/emcie-co/parlant): Instead of hoping your LLM will follow instructions, Parlant ensures rule compliance, Predictable, consistent behavior [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/emcie-co/parlant?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [phidata✨](https://github.com/phidatahq/phidata): Build AI Assistants with memory, knowledge, and tools [May 2022] ![**github stars**](https://img.shields.io/github/stars/phidatahq/phidata?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PydanticAI✨](https://github.com/pydantic/pydantic-ai): Agent Framework / shim to use Pydantic with LLMs. Model-agnostic. Type-safe. [29 Oct 2024] ![**github stars**](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PySpur✨](https://github.com/PySpur-Dev/pyspur): Drag-and-Drop. an AI agent builder in Python. [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/PySpur-Dev/pyspur?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Qwen-Agent✨](https://github.com/QwenLM/Qwen-Agent): Agent framework built upon Qwen1.5, featuring Function Calling, Code Interpreter, RAG, and Chrome extension. [Sep 2023] ![**github stars**](https://img.shields.io/github/stars/QwenLM/Qwen-Agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ROMA: Recursive Open Meta-Agents✨](https://github.com/sentient-agi/ROMA): an open-source meta-agent framework designed to build high-performance multi-agent systems by decomposing complex tasks into recursive, parallelizable components ![**github stars**](https://img.shields.io/github/stars/sentient-agi/ROMA?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Strands Agents✨](https://github.com/strands-agents/sdk-python): Model‑Driven, Tool‑First Architecture. No need to hard-code logic. Just define tools and models—the system figures out how to use them. [May 2025] ![**github stars**](https://img.shields.io/github/stars/strands-agents/sdk-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SuperAGI✨](https://github.com/TransformerOptimus/SuperAGI): Autonomous AI Agents framework [May 2023] ![**github stars**](https://img.shields.io/github/stars/TransformerOptimus/SuperAGI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SwarmZero✨](https://github.com/swarmzero/swarmzero): SwarmZero's SDK for building AI agents, swarms of agents. [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/swarmzero/swarmzero?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [TaskingAI✨](https://github.com/TaskingAI/TaskingAI): A BaaS (Backend as a Service) platform for LLM-based Agent Development and Deployment. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/TaskingAI/TaskingAI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [UpSonic✨](https://github.com/Upsonic/UpSonic): (previously GPT Computer Assistant(GCA)) an AI agent framework designed to make computer use. [May 2024]
1. [VoltAgent✨](https://github.com/VoltAgent/voltagent): Open Source TypeScript AI Agent Framework [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/VoltAgent/voltagent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [XAgent✨](https://github.com/OpenBMB/XAgent): Autonomous LLM Agent for complex task solving like data analysis, recommendation, and model training [Oct 2023] ![**github stars**](https://img.shields.io/github/stars/OpenBMB/XAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **Agent Application**

1. [AgentGPT✨](https://github.com/reworkd/AgentGPT): Assemble, configure, and deploy autonomous AI agents in your browser [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/reworkd/AgentGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. Agent workflows and samples are available in [Live Agent Studio](https://github.com/coleam00/ottomator-agents): All the open source AI Agents hosted on the oTTomator Live Agent Studio. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/coleam00/ottomator-agents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Agent Zero✨](https://github.com/frdel/agent-zero): An open-source framework for autonomous AI agents with task automation and code generation. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/frdel/agent-zero?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Agentless✨](https://github.com/OpenAutoCoder/Agentless): an agentless approach to automatically solve software development problems. AGENTLESS, consisting of three phases: localization, repair, and patch validation (self-reflect). [1 Jul 2024] ![**github stars**](https://img.shields.io/github/stars/OpenAutoCoder/Agentless?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ai-town✨](https://github.com/a16z-infra/ai-town): a virtual town where AI characters live, chat and socialize. [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/a16z-infra/ai-town?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AIOS✨](https://github.com/agiresearch/AIOS): LLM Agent Operating System [Jan 2024]
 ![**github stars**](https://img.shields.io/github/stars/agiresearch/AIOS?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AppAgent-TencentQQGYLab✨](https://github.com/mnotgod96/AppAgent): Multimodal Agents as Smartphone Users. [Dec 2023] ![**github stars**](https://img.shields.io/github/stars/mnotgod96/AppAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Archon✨](https://github.com/coleam00/Archon): AI Agent Builder: Example of iteration from Single-Agent to Multi-Agent. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/coleam00/Archon?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ASearcher✨](https://github.com/inclusionAI/ASearcher): ASearcher: An Open-Source Large-Scale Reinforcement Learning Project for Search Agents [11 Aug 2025] ![**github stars**](https://img.shields.io/github/stars/inclusionAI/ASearcher?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Auto-GPT✨](https://github.com/Torantulino/Auto-GPT): Most popular [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/Torantulino/Auto-GPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [babyagi✨](https://github.com/yoheinakajima/babyagi): Simplest implementation - Coworking of 4 agents [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/yoheinakajima/babyagi?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [BettaFish✨](https://github.com/666ghj/BettaFish):  A multi-agent public opinion analysis assistant. [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/666ghj/BettaFish?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [browser-use✨](https://github.com/browser-use/browser-use): Make websites accessible for AI agents. [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/browser-use/browser-use?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [CAMEL✨](https://github.com/lightaime/camel): CAMEL: Communicative Agents for “Mind” Exploration of Large Scale Language Model Society [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/lightaime/camel?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ChatDev✨](https://github.com/OpenBMB/ChatDev): Virtual software company. Create Customized Software using LLM-powered Multi-Agent Collaboration [Sep 2023] ![**github stars**](https://img.shields.io/github/stars/OpenBMB/ChatDev?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Contains Studio AI Agents✨](https://github.com/contains-studio/agents): A comprehensive collection of specialized AI agents. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/contains-studio/agents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Customer Service Agents Demo](https://github.com/openai/openai-cs-agents-demo): OpenAI. Customer Service Agents Demo. [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/openai/openai-cs-agents-demo?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Devon✨](https://github.com/entropy-research/Devon): An open-source pair programmer. [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/entropy-research/Devon?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [GPT Pilot✨](https://github.com/Pythagora-io/gpt-pilot): The first real AI developer. Dev tool that writes scalable apps from scratch while the developer oversees the implementation [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/Pythagora-io/gpt-pilot?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Integuru✨](https://github.com/Integuru-AI/Integuru): An AI agent that generates integration code by reverse-engineering platforms' internal APIs. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/Integuru-AI/Integuru?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Khoj✨](https://github.com/khoj-ai/khoj): Open-source, personal AI agents. Cloud or Self-Host, Multiple Interfaces. Python Django based [Aug 2021] ![**github stars**](https://img.shields.io/github/stars/khoj-ai/khoj?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LaVague✨](https://github.com/lavague-ai/LaVague): Automate automation with Large Action Model framework. Generate Selenium code. [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/lavague-ai/LaVague?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Letta ADE✨](https://github.com/letta-ai/letta): a graphical user interface for ADE (Agent Development Environment) by [Letta (previously MemGPT)✨](https://github.com/letta-ai/letta) [12 Oct 2023]
1. [M3-Agent✨](https://github.com/bytedance-seed/m3-agent): Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory [13 Aug 2025] ![**github stars**](https://img.shields.io/github/stars/bytedance-seed/m3-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Magentic-One✍️](https://aka.ms/magentic-one): A Generalist Multi-Agent System for Solving Complex Tasks [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/TEN-framework/TEN-Agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Memento✨](https://github.com/Agent-on-the-Fly/Memento): Fine-tuning LLM Agents without Fine-tuning LLMs [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/Agent-on-the-Fly/Memento?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Mixture Of Agents (MoA)✨](https://github.com/togethercomputer/MoA): an architecture that runs multiple LLMs in parallel, then uses a final “aggregator” model to merge their outputs into a superior combined response. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/togethercomputer/MoA?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Mobile-Agent✨](https://github.com/X-PLUG/MobileAgent): The Powerful Mobile Device Operation Assistant Family. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/X-PLUG/MobileAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [nanobrowser✨](https://github.com/nanobrowser/nanobrowser): Open-source Chrome extension for AI-powered web automation. Alternative to OpenAI Operator. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/nanobrowser/nanobrowser?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Open Agent Platform✨](https://github.com/langchain-ai/open-agent-platform): Langchain. An open-source, no-code agent building platform. [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/langchain-ai/open-agent-platform?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [OpenDAN : Your Personal AIOS✨](https://github.com/fiatrete/OpenDAN-Personal-AI-OS): OpenDAN, an open-source Personal AI OS consolidating various AI modules in one place [May 2023] ![**github stars**](https://img.shields.io/github/stars/fiatrete/OpenDAN-Personal-AI-OS?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PaSa✨](https://github.com/bytedance/pasa): an advanced paper search agent. Bytedance. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/bytedance/pasa?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PayPal Agent Toolkit✨](https://github.com/paypal/agent-toolkit): OpenAI's Agent SDK, LangChain, Vercel's AI SDK, and Model Context Protocol (MCP) to integrate with PayPal APIs through function calling. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/paypal/agent-toolkit?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [Potpie✨](https://github.com/potpie-ai/potpie): Prompt-To-Agent : Create custom engineering agents for your codebase [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/potpie-ai/potpie?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PR-Agent✨](https://github.com/Codium-ai/pr-agent): Efficient code review and handle pull requests, by providing AI feedbacks and suggestions [Jan 2023] ![**github stars**](https://img.shields.io/github/stars/Codium-ai/pr-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Project Astra](https://deepmind.google/technologies/gemini/project-astra/): Google DeepMind, A universal AI agent that is helpful in everyday life [14 May 2024]
1. [RasaGPT✨](https://github.com/paulpierre/RasaGPT): Built with Rasa, FastAPI, Langchain, and LlamaIndex [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/paulpierre/RasaGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Realtime API Agents Demo✨](https://github.com/openai/openai-realtime-agents): a simple demonstration of more advanced, agentic patterns built on top of the Realtime API. OpenAI. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/openai/openai-realtime-agents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Riona-AI-Agent✨](https://github.com/David-patrick-chuks/Riona-AI-Agent): automation tool designed for Instagram to automate social media interactions such as posting, liking, and commenting. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/David-patrick-chuks/Riona-AI-Agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SakanaAI AI-Scientist✨](https://github.com/SakanaAI/AI-Scientist): Towards Fully Automated Open-Ended Scientific Discovery [Aug 2024]
 ![**github stars**](https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SeeAct](https://osu-nlp-group.github.io/SeeAct): GPT-4V(ision) is a Generalist Web Agent, if Grounded [✨](https://github.com/OSU-NLP-Group/SeeAct) [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/OSU-NLP-Group/SeeAct?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Sim Studio✨](https://github.com/simstudioai/sim): A Figma-like canvas to build agent workflow. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/simstudioai/sim?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [skyagi✨](https://github.com/litanlitudan/skyagi): Simulating believable human behaviors. Role playing [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/litanlitudan/skyagi?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [skyvern✨](https://github.com/skyvern-ai/skyvern): Automate browser-based workflows with LLMs and Computer Vision [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/skyvern-ai/skyvern?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Suna✨](https://github.com/kortix-ai/suna): a fully open source AI assistant that helps you accomplish real-world tasks [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/kortix-ai/suna?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SuperAGI✨](https://github.com/TransformerOptimus/superagi): GUI for agent settings [May 2023] ![**github stars**](https://img.shields.io/github/stars/TransformerOptimus/superagi?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [tabby✨](https://github.com/TabbyML/tabby): a self-hosted AI coding assistant, offering an open-source and on-premises alternative to GitHub Copilot. [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/TabbyML/tabby?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [TEN Agent✨](https://github.com/TEN-framework/TEN-Agent): The world’s first real-time multimodal agent integrated with the OpenAI Realtime API. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/TEN-framework/TEN-Agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [WrenAI✨](https://github.com/Canner/WrenAI): Open-source SQL AI Agent for Text-to-SQL [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/Canner/WrenAI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [xpander.ai✨](https://github.com/xpander-ai/xpander.ai): Backend-as-a-Service for AI Agents. Equip any AI Agent with tools, memory, multi-agent collaboration, state, triggering, storage, and more. [May 2025] ![**github stars**](https://img.shields.io/github/stars/xpander-ai/xpander.ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **OSS Alternatives for OpenAI Code Interpreter (aka. Advanced Data Analytics)**

1. [Azure Container Apps Dynamic Sessions✍️](https://aka.ms/AAtnnj8): Secure environment for running AI-generated code in Azure.
1. [gpt-code-ui✨](https://github.com/ricklamers/gpt-code-ui) An open source implementation of OpenAI's ChatGPT Code interpreter. [May 2023]
 ![**github stars**](https://img.shields.io/github/stars/ricklamers/gpt-code-ui?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Open Interpreter✨](https://github.com/KillianLucas/open-interpreter):💡Let language models run code on your computer. [Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/KillianLucas/open-interpreter?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenAI Code Interpreter✍️](https://openai.com/blog/chatgpt-plugins) Integration with Sandboxed python execution environment [23 Mar 2023]
    - We provide our models with a working Python interpreter in a sandboxed, firewalled execution environment, along with some ephemeral disk space.
1. [OSS Code Interpreter✨](https://github.com/shroominic/codeinterpreter-api) A LangChain implementation of the ChatGPT Code Interpreter. [Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/shroominic/codeinterpreter-api?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SlashGPT✨](https://github.com/snakajima/SlashGPT) The tool integrated with "jupyter" agent [Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/snakajima/SlashGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [🔗](#llm-application): E2B - sandbox

#### **Coding agent**

- [🔗](#code-editor--agent): Code editor / agent

#### **Domain-specific**

1. [5 Top AI Agents for Earth Snapshots](https://x.com/MaryamMiradi/status/1866527000963211754) VLMs and LLMs for Geospatial Intelligent Analysis: [GeoChat📑](https://alphaxiv.org/abs/2311.15826) | [GEOBench-VLM📑](https://alphaxiv.org/abs/2411.19325) | [RS5M✨](https://github.com/om-ai-lab/RS5M) | [VHM✨](https://github.com/opendatalab/VHM) | [EarthGPT](https://ieeexplore.ieee.org/document/10547418)
1. [An LLM Agent for Automatic Geospatial Data Analysis📑](https://alphaxiv.org/abs/2410.18792) [24 Oct 2024]
1. [AgentSociety✨](https://github.com/tsinghua-fib-lab/agentsociety): Building agents in urban simulation environments. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/tsinghua-fib-lab/agentsociety?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ChemAgent: Self-updating Library in Large Language Models Improves Chemical Reasoning📑](https://alphaxiv.org/abs/2501.06590): ChemAgent leverages an innovative self-improving memory system to significantly enhance performance in complex scientific tasks, with a particular focus on Chemistry. [11 Jan 2025]
1. [DeepRare📑](https://alphaxiv.org/abs/2506.20430): An Agentic System for Rare Disease Diagnosis with Traceable Reasoning [25 Jun 2025]
1. [Director✨](https://github.com/video-db/Director): Think of Director as ChatGPT for videos. AI video agents framework for video interactions and workflows. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/video-db/Director?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DrugAgent: Automating AI-aided Drug Discovery📑](https://alphaxiv.org/abs/2411.15692) [24 Nov 2024]
1. [FinRobot: AI Agent for Equity Research and Valuation📑](https://alphaxiv.org/abs/2411.08804) [13 Nov 2024]
1. [landing.ai: Vision Agent✨](https://github.com/landing-ai/vision-agent): A agent frameworks to generate code to solve your vision task. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/landing-ai/vision-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Organ-Agents: Virtual Human Physiology Simulator via LLMs](https://alphaxiv.org/abs/2508.14357): Multi-agent system simulating nine human organs using fine-tuned Qwen3-8B, forecasting patient physiology up to 12 hours ahead, validated by 15 ICU specialists. [20 Aug 2025]
1. [MLE-agent✨](https://github.com/MLSysOps/MLE-agent): LLM agent for machine learning engineers and researchers [Apr 2024] ![**github stars**](https://img.shields.io/github/stars/MLSysOps/MLE-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [UXAgent📑](https://alphaxiv.org/abs/2502.12561): An LLM Agent-Based Usability Testing Framework for Web Design [18 Feb 2025]

#### **Deep research**

1. [Accelerating scientific breakthroughs with an AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/): Google introduces AI co-scientist, a multi-agent AI system built with Gemini 2.0 as a virtual scientific collaborator [19 Feb 2025]
1. [Agent Laboratory✨](https://github.com/SamuelSchmidgall/AgentLaboratory): E2E autonomous research workflow. Using LLM Agents as Research Assistants. [8 Jan 2025] ![**github stars**](https://img.shields.io/github/stars/SamuelSchmidgall/AgentLaboratory?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [agenticSeek✨](https://github.com/Fosowl/agenticSeek): Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/Fosowl/agenticSeek?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AlphaEvolve](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/): DeepMind’s AI agent that autonomously evolves algorithms using Gemini models—applied in chip design, data centers, robotics, math & CS, and AI training. [14 May 2025]
1. [CodeScientist✨](https://github.com/allenai/codescientist): An automated scientific discovery system for code-based experiments. AllenAI. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/allenai/codescientist?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Company Researcher✨](https://github.com/exa-labs/company-researcher): a free and open-source tool that helps you instantly understand any company inside out. [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/exa-labs/company-researcher?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Deep Research Agent📑](https://alphaxiv.org/abs/2506.18096):💡Survey. A Systematic Examination And Roadmap [22 Jun 2025]
1. [DeerFlow✨](https://github.com/bytedance/deer-flow):  Bytedance. Deep Exploration and Efficient Research Flow. a community-driven Deep Research framework that combines language models with tools like web search, crawling, and code execution.  ![**github stars**](https://img.shields.io/github/stars/bytedance/deer-flow?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [May 2025]
1. [DeepSearcher✨](https://github.com/zilliztech/deep-searcher): DeepSearcher integrates LLMs and Vector Databases for precise search, evaluation, and reasoning on private data, providing accurate answers and detailed reports. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/zilliztech/deep-searcher?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Enterprise Deep Research (EDR)✨](https://github.com/SalesforceAIResearch/enterprise-deep-research): Salesforce Enterprise Deep Research [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/SalesforceAIResearch/enterprise-deep-research?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Felo.ai Deep Research✍️](https://felo.ai/blog/free-deepseek-r1-ai-search/) [8 Feb 2025]
1. [Kimi-Researcher](https://moonshotai.github.io/Kimi-Researcher/): Kimi Researcher is an AI-powered tool that assists with document analysis, literature review, and knowledge extraction. Moonshot AI (Chinese name: 月之暗面, meaning "The Dark Side of the Moon") is a Beijing-based company founded in March 2023. [20 Jun 2025]
1. [LangChain Open Deep Research✨](https://github.com/langchain-ai/open_deep_research): (formerly mAIstro) a web research assistant for generating comprehensive reports on any topic. [13 Feb 2025] ![**github stars**](https://img.shields.io/github/stars/langchain-ai/open_deep_research?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Manus sandbox runtime code leaked](https://x.com/jianxliao/status/1898861051183349870): Claude Sonnet with 29 tools, without multi-agent, using `browser_use`. [✨](https://gist.github.com/jlia0/db0a9695b3ca7609c9b1a08dcbf872c9) [✍️](https://manus.im/): Manus official site [10 Mar 2025]
1. [Ollama Deep Researcher✨](https://github.com/langchain-ai/ollama-deep-researcher): a fully local web research assistant that uses any LLM hosted by Ollama [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/langchain-ai/ollama-deep-researcher?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Open Deep Research✨](https://github.com/btahir/open-deep-research): Open source alternative to Gemini Deep Research. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/btahir/open-deep-research?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenAI deep research✍️](https://openai.com/index/introducing-deep-research/): [🔗](#openai-products)  [2 Feb 2025]
1. [OpenDeepSearch✨](https://github.com/sentient-agi/OpenDeepSearch): deep web search and retrieval, optimized for use with Hugging Face's SmolAgents ecosystem [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/sentient-agi/OpenDeepSearch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenEvolve✨](https://github.com/codelion/openevolve): An open-source implementation of the AlphaEvolve system described in the Google DeepMind paper "AlphaEvolve: A coding agent for scientific and algorithmic discovery" [May 2025] ![**github stars**](https://img.shields.io/github/stars/codelion/openevolve?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [OpenManus✨](https://github.com/mannaandpoem/OpenManus): A Free Open-Source Alternative to Manus AI Agent [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/mannaandpoem/OpenManus?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Paper2Agent✨](https://github.com/jmiao24/Paper2Agent): a multi-agent AI system that converts research papers into interactive agents with minimal human input [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/jmiao24/Paper2Agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning📑](https://alphaxiv.org/abs/2504.17192): a multi-agent LLM framework that transforms machine learning papers into functional code repositories. [24 Apr 2025] [✨](https://github.com/going-doer/Paper2Code) ![**github stars**](https://img.shields.io/github/stars/going-doer/Paper2Code?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research) [14 Feb 2025]
1. [SakanaAI AI-Scientist✨](https://github.com/SakanaAI/AI-Scientist): [🔗](#agent-application) [Aug 2024]
 ![**github stars**](https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [smolagents: Open Deep Research✨](https://github.com/huggingface/smolagents) > `examples/open_deep_research`.🤗HuggingFace [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/huggingface/smolagents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [STORM✨](https://github.com/stanford-oval/storm): Simulating Expert Q&A, iterative research, structured outline creation, and grounding in trusted sources to generate Wikipedia-like reports. [Apr 2024] ![**github stars**](https://img.shields.io/github/stars/stanford-oval/storm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search📑](https://alphaxiv.org/abs/2504.08066): AgentManager handles Agentic Tree Search [10 Apr 2025] [✨](https://github.com/SakanaAI/AI-Scientist-v2) ![**github stars**](https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Tongyi DeepResearch✨](https://github.com/Alibaba-NLP/DeepResearch): Alibaba. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Universal Deep Research (UDR)✨](https://github.com/NVlabs/UniversalDeepResearch): NVDIA. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/NVlabs/UniversalDeepResearch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [WebThinker✨](https://github.com/RUC-NLPIR/WebThinker): WebThinker allows the reasoning model itself to perform actions during thinking, achieving end-to-end task execution in a single generation. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/RUC-NLPIR/WebThinker?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

## **Microsoft Semantic Kernel and Stanford NLP DSPy**

### **Semantic Kernel**

- [A Guide to Microsoft’s Semantic Kernel Process Framework✍️](https://devblogs.microsoft.com/semantic-kernel/guest-blog-revolutionize-business-automation-with-ai-a-guide-to-microsofts-semantic-kernel-process-framework/)  [11 April 2025]
- [Agent Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/agent): A module for AI agents, and agentic patterns / [Process Framework](https://learn.microsoft.com/en-us/semantic-kernel/frameworks/process/process-framework): A module for creating a structured sequence of activities or tasks. [Oct 2024]
- [AutoGen will transition seamlessly into Semantic Kernel in early 2025✍️](https://devblogs.microsoft.com/semantic-kernel/microsofts-agentic-ai-frameworks-autogen-and-semantic-kernel/) [15 Nov 2024]
- [Context based function selection✨](https://github.com/microsoft/semantic-kernel/pull/12130): ADR (Architectural Decision Records). Agents analyze the conversation context to select the most relevant function, instead of considering all available functions. [May 2025]
- Microsoft LangChain Library supports C# and Python and offers several features, some of which are still in development and may be unclear on how to implement. However, it is simple, stable, and faster than Python-based open-source software. The features listed on the link include: [Semantic Kernel Feature Matrix](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages) / doc:[✍️](https://learn.microsoft.com/en-us/semantic-kernel) / blog:[✍️](https://devblogs.microsoft.com/semantic-kernel/) / [✨](https://github.com/microsoft/semantic-kernel) [Feb 2023]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/semantic-kernel?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- .NET Semantic Kernel SDK: 1. Renamed packages and classes that used the term “Skill” to now use “Plugin”. 2. OpenAI specific in Semantic Kernel core to be AI service agnostic 3. Consolidated our planner implementations into a single package [✍️](https://devblogs.microsoft.com/semantic-kernel/introducing-the-v1-0-0-beta1-for-the-net-semantic-kernel-sdk/) [10 Oct 2023]
- Road to v1.0 for the Python Semantic Kernel SDK [✍️](https://devblogs.microsoft.com/semantic-kernel/road-to-v1-0-for-the-python-semantic-kernel-sdk/) [23 Jan 2024] [backlog✨](https://github.com/orgs/microsoft/projects/866/views/3?sliceBy%5Bvalue%5D=python)
- [Semantic Kernel Agents are now Generally Available✍️](https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-agents-are-now-generally-available/): Agent Core to create and connect with managed agent platforms: Azure AI Agent Service, AutoGen, AWS Bedrock, Crew AI, and OpenAI Assistants (C#, Python). [2 Apr 2025]
- [Semantic Kernel and Copilot Studio Usage✍️](https://devblogs.microsoft.com/semantic-kernel/guest-blog-semantic-kernel-and-copilot-studio-usage-series-part-1/) [7 Apr 2025]
- [Semantic Kernel and Microsoft Agent Framework✍️](https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-and-microsoft-agent-framework/): 💡Microsoft Agent Framework is the successor to Semantic Kernel for building AI agents. Microsoft Agent Framework remains in Preview for the next few months. Use Semantic Kernel for existing or time-sensitive projects. For new projects that can wait for General Availability, start with Microsoft Agent Framework. [7 Oct 2025]
- [Semantic Kernel Roadmap H1 2025✍️](https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-roadmap-h1-2025-accelerating-agents-processes-and-integration/): Agent Framework, Process Framework [3 Feb 2025]
- [Unlocking the Power of Memory: Announcing General Availability of Semantic Kernel’s Memory Packages✍️](https://devblogs.microsoft.com/semantic-kernel/unlocking-the-power-of-memory-announcing-general-availability-of-semantic-kernels-memory-packages/): new Vector Store abstractions, improving on the older Memory Store abstractions. [25 Nov 2024]

<!-- <img src="./files/mind-and-body-of-semantic-kernel.png" alt="sk" width="130"/> -->
<!-- <img src="./files/sk-flow.png" alt="sk" width="500"/> -->

### **Micro-orchestration**

- Micro-orchestration in LLM pipelines is the detailed management of LLM interactions, focusing on data flow within tasks.
- e.g., [Semantic Kernel](https://aka.ms/sk/repo), [LangChain](https://www.langchain.com/), [LlamaIndex](https://www.llamaindex.ai/), [Haystack](https://haystack.deepset.ai/), and [AdalFlow✨](https://github.com/SylphAI-Inc/AdalFlow).
 ![**github stars**](https://img.shields.io/github/stars/SylphAI-Inc/AdalFlow?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **Code Recipes**

- [A Pythonista’s Intro to Semantic Kernel✍️](https://towardsdatascience.com/a-pythonistas-intro-to-semantic-kernel-af5a1a39564d)💡[3 Sep 2023]
- Deploy Semantic Kernel with Bot Framework [✍️](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/deploy-semantic-kernel-with-bot-framework/ba-p/3928101) [✨](https://github.com/Azure/semantic-kernel-bot-in-a-box) [26 Oct 2023]
 ![**github stars**](https://img.shields.io/github/stars/Azure/semantic-kernel-bot-in-a-box?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Learning Paths for Semantic Kernel✍️](https://devblogs.microsoft.com/semantic-kernel/learning-paths-for-semantic-kernel/) [28 Mar 2024]
- [Model Context Protocol (MCP) support for Python✍️](https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-adds-model-context-protocol-mcp-support-for-python/) [17 Apr 2025]
- Semantic Kernel and Microsoft.Extensions.AI: Better Together: [part1✍️](https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-and-microsoft-extensions-ai-better-together-part-1/) | [part2✍️](https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-and-microsoft-extensions-ai-better-together-part-2/) [28 May 2025]
- [Semantic Kernel: Multi-agent Orchestration✍️](https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-multi-agent-orchestration/): sequential orchestration, concurrent orchestration, group chat orchestration, handoff collaboration [27 May 2025]
- Semantic Kernel-Powered OpenAI Plugin Development Lifecycle [✍️](https://techcommunity.microsoft.com/t5/azure-developer-community-blog/semantic-kernel-powered-openai-plugin-development-lifecycle/ba-p/3967751) [30 Oct 2023]
- [Semantic Kernel Python with Google’s A2A Protocol✍️](https://devblogs.microsoft.com/semantic-kernel/integrating-semantic-kernel-python-with-googles-a2a-protocol/) [17 Apr 2025]
- Semantic Kernel Recipes: A collection of C# notebooks [✨](https://github.com/johnmaeda/SK-Recipes) [Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/johnmaeda/SK-Recipes?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Semantic Kernel sample application:💡[Chat Copilot✨](https://github.com/microsoft/chat-copilot) [Apr 2023] / [Virtual Customer Success Manager (VCSM)✨](https://github.com/jvargh/VCSM) [Jul 2024] / [Project Micronaire✍️](https://devblogs.microsoft.com/semantic-kernel/microsoft-hackathon-project-micronaire-using-semantic-kernel/): A Semantic Kernel RAG Evaluation Pipeline [✨](https://github.com/microsoft/micronaire) [3 Oct 2024]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/chat-copilot?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/jvargh/VCSM?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/microsoft/micronaire?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- SemanticKernel Implementation sample to overcome Token limits of Open AI model. [✍️](https://zenn.dev/microsoft/articles/semantic-kernel-10) [06 May 2023]
- [Step-by-Step Guide to Building a Powerful AI Monitoring Dashboard with Semantic Kernel and Azure Monitor✍️](https://devblogs.microsoft.com/semantic-kernel/step-by-step-guide-to-building-a-powerful-ai-monitoring-dashboard-with-semantic-kernel-and-azure-monitor/): Step-by-step guide to building an AI monitoring dashboard using Semantic Kernel and Azure Monitor to track token usage and custom metrics. [23 Aug 2024]
- [Working with Audio in Semantic Kernel Python✍️](https://devblogs.microsoft.com/semantic-kernel/working-with-audio-in-semantic-kernel-python/) [15 Nov 2024]

#### **Semantic Kernel Planner [deprecated]**

- Semantic Kernel Planner [✍️](https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-planners-actionplanner/) [24 Jul 2023]

  <img src="./files/sk-evolution_of_planners.jpg" alt="sk-plan" width="300"/>

- Is Semantic Kernel Planner the same as LangChain agents?

  > Planner in SK is not the same as Agents in LangChain. [✨](https://github.com/microsoft/semantic-kernel/discussions/1326) [11 May 2023]

  > Agents in LangChain use recursive calls to the LLM to decide the next step to take based on the current state.
  > The two planner implementations in SK are not self-correcting.
  > Sequential planner tries to produce all the steps at the very beginning, so it is unable to handle unexpected errors.
  > Action planner only chooses one tool to satisfy the goal

- Stepwise Planner released. The Stepwise Planner features the "CreateScratchPad" function, acting as a 'Scratch Pad' to aggregate goal-oriented steps. [16 Aug 2023]

- Gen-4 and Gen-5 planners: 1. Gen-4: Generate multi-step plans with the [Handlebars](https://handlebarsjs.com/) 2. Gen-5: Stepwise Planner supports Function Calling. [✍️](https://devblogs.microsoft.com/semantic-kernel/semantic-kernels-ignite-release-beta8-for-the-net-sdk/) [16 Nov 2023]

- Use function calling for most tasks; it's more powerful and easier. `Stepwise and Handlebars planners will be deprecated` [✍️](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning) [Jun 2024] 

- [The future of Planners in Semantic Kernel✍️](https://devblogs.microsoft.com/semantic-kernel/the-future-of-planners-in-semantic-kernel/) [23 July 2024]

#### **Semantic Function**

- Semantic Kernel Functions vs. Plugins: 
  1. Function:  Individual units of work that perform specific tasks. Execute actions based on user requests. [✍️](https://devblogs.microsoft.com/semantic-kernel/transforming-semantic-kernel-functions/) [12 Nov 2024]
  2. Plugin: Collections of functions. Orchestrate multiple functions for complex tasks.
- Semantic Function - expressed in natural language in a text file "_skprompt.txt_" using SK's
[Prompt Template language✨](https://github.com/microsoft/semantic-kernel/blob/main/docs/PROMPT_TEMPLATE_LANGUAGE.md).
Each semantic function is defined by a unique prompt template file, developed using modern prompt engineering techniques. [✨](https://github.com/microsoft/semantic-kernel/blob/main/docs/GLOSSARY.md)

- Prompt Template language Key takeaways

```bash
1. Variables : use the {{$variableName}} syntax : Hello {{$name}}, welcome to Semantic Kernel!
2. Function calls: use the {{namespace.functionName}} syntax : The weather today is {{weather.getForecast}}.
3. Function parameters: {{namespace.functionName $varName}} and {{namespace.functionName "value"}} syntax
   : The weather today in {{$city}} is {{weather.getForecast $city}}.
4. Prompts needing double curly braces :
   {{ "{{" }} and {{ "}}" }} are special SK sequences.
5. Values that include quotes, and escaping :

    For instance:
    ... {{ 'no need to \\"escape" ' }} ...
    is equivalent to:
    ... {{ 'no need to "escape" ' }} ...
```

#### **Semantic Kernel Glossary**

- [Glossary in Git✨](https://github.com/microsoft/semantic-kernel/blob/main/docs/GLOSSARY.md) / [Glossary in MS Doc](https://learn.microsoft.com/en-us/semantic-kernel/whatissk#sk-is-a-kit-of-parts-that-interlock)

  <img src="./files/kernel-flow.png" alt="sk" width="500"/>

  | Term      | Short Description                                                                                                                                                                                                                                                                                     |
  | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | ASK       | A user's goal is sent to SK as an ASK                                                                                                                                                                                                                                                                 |
  | Kernel    | [The kernel](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/kernel) orchestrates a user's ASK                                                                                                                                                                                          |
  | Planner   | [The planner](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/planner) breaks it down into steps based upon resources that are available [deprecated] -> replaced by function calling                                                                                                                                  |
  | Resources | Planning involves leveraging available [skills,](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/skills) [memories,](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/memories) and [connectors](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/connectors) |
  | Steps     | A plan is a series of steps for the kernel to execute                                                                                                                                                                                                                                                 |
  | Pipeline  | Executing the steps results in fulfilling the user's ASK                                                                                                                                                                                                                                              |
- [Architecting AI Apps with Semantic Kernel✍️](https://devblogs.microsoft.com/semantic-kernel/architecting-ai-apps-with-semantic-kernel/) How you could recreate Microsoft Word Copilot [6 Mar 2024]  
  <img src="./files/semantic-kernel-with-word-copilot.png" height="500">  

### **DSPy**

- [DSPy📑](https://alphaxiv.org/abs/2310.03714): Compiling Declarative Language Model Calls into Self-Improving Pipelines [5 Oct 2023] / [✨](https://github.com/stanfordnlp/dspy)
- [Prompt Like a Data Scientist: Auto Prompt Optimization and Testing with DSPy✍️](https://towardsdatascience.com/prompt-like-a-data-scientist-auto-prompt-optimization-and-testing-with-dspy-ff699f030cb7) [6 May 2024]
- Automatically iterate until the best result is achieved: 1. Collect Data -> 2. Write DSPy Program -> 3. Define validtion logic -> 4. Compile DSPy program
- DSPy (Declarative Self-improving Language Programs, pronounced “dee-es-pie”) / doc:[✍️](https://dspy-docs.vercel.app) / [✨](https://github.com/stanfordnlp/dspy) ![**github stars**](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- DSPy Documentation & Cheetsheet [✍️](https://dspy-docs.vercel.app)
- DSPy Explained! [📺](https://www.youtube.com/watch?v=41EfOY0Ldkc) [30 Jan 2024]
- DSPy RAG example in weviate `recipes > integrations`: [✨](https://github.com/weaviate/recipes) ![**github stars**](https://img.shields.io/github/stars/weaviate/recipes?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Instead of a hard-coded prompt template, "Modular approach: compositions of modules -> compile". 
  - Building blocks such as ChainOfThought or Retrieve and compiling the program, optimizing the prompts based on specific metrics. Unifying strategies for both prompting and fine-tuning in one tool, Pythonic operations, prioritizing and tracing program execution. These features distinguish it from other LMP frameworks such as LangChain, and LlamaIndex. [✍️](https://towardsai.net/p/machine-learning/inside-dspy-the-new-language-model-programming-framework-you-need-to-know-about) [Jan 2023]
  <img src="./files/dspy-workflow.jpg" width="400" alt="workflow">  

### **Optimizer frameworks**

- These frameworks, including DSpy, utilize algorithmic methods inspired by machine learning to improve prompts, outputs, and overall performance in LLM applications.
- [AdalFlow✨](https://github.com/SylphAI-Inc/AdalFlow):💡The Library to Build and Auto-optimize LLM Applications [Apr 2024]
 ![**github stars**](https://img.shields.io/github/stars/SylphAI-Inc/AdalFlow?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [TextGrad🐙](https://github.com/zou-group/textgrad): automatic ``differentiation` via text. Backpropagation through text feedback provided by LLMs [Jun 2024]
 ![**github stars**](https://img.shields.io/github/stars/zou-group/textgrad?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **DSPy Glossary**

- Glossary reference to the [✍️](https:/towardsdatascience.com/intro-to-dspy-goodbye-prompting-hello-programming-4ca1c6ce3eb9).
  1. Signatures: Hand-written prompts and fine-tuning are abstracted and replaced by signatures.
      > "question -> answer" <br/>
        "long-document -> summary"  <br/>
        "context, question -> answer"  <br/>
  2. Modules: Prompting techniques, such as `Chain of Thought` or `ReAct`, are abstracted and replaced by modules.
      ```python
      # pass a signature to ChainOfThought module
      generate_answer = dspy.ChainOfThought("context, question -> answer")
      ```
  3. Optimizers (formerly Teleprompters): Manual iterations of prompt engineering is automated with optimizers (teleprompters) and a DSPy Compiler.
      ```python
      # Self-generate complete demonstrations. Teacher-student paradigm, `BootstrapFewShotWithOptuna`, `BootstrapFewShotWithRandomSearch` etc. which work on the same principle.
      optimizer = BootstrapFewShot(metric=dspy.evaluate.answer_exact_match)
      ```
  4. DSPy Compiler: Internally trace your program and then optimize it using an optimizer (teleprompter) to maximize a given metric (e.g., improve quality or cost) for your task.
  - e.g., the DSPy compiler optimizes the initial prompt and thus eliminates the need for manual prompt tuning.
    ```python
    cot_compiled = teleprompter.compile(CoT(), trainset=trainset, valset=devset)
    cot_compiled.save('turbo_gsm8k.json')
    ```

#### DSPy optimizer

- Automatic Few-Shot Learning
  - As a rule of thumb, if you don't know where to start, use `BootstrapFewShotWithRandomSearch`.
  - If you have very little data, e.g. 10 examples of your task, use `BootstrapFewShot`.
  - If you have slightly more data, e.g. 50 examples of your task, use `BootstrapFewShotWithRandomSearch`. 
  - If you have more data than that, e.g. 300 examples or more, use `BayesianSignatureOptimizer`. -> deprecated and replaced with MIPRO.
  - `KNNFewShot`: k-Nearest Neighbors to select the closest training examples, which are then used in the BootstrapFewShot optimization process​
- Automatic Instruction Optimization
  - `COPRO`: Repeat for a set number of iterations, tracking the best-performing instructions.
  - `MIPRO`: Repeat for a set number of iterations, tracking the best-performing combinations (instructions and examples). -> replaced with `MIPROv2`.
  - `MIPROv2`: If you want to keep your prompt 0-shot, or use 40+ trials or 200+ examples, choose MIPROv2. [March 2024]
- Automatic Finetuning
  - If you have been able to use one of these with a large LM (e.g., 7B parameters or above) and need a very efficient program, compile that down to a small LM with `BootstrapFinetune`.
- Program Transformations
  - `Ensemble`: Combines DSPy programs using all or randomly sampling a subset into a single program.


## **LangChain Features, Usage, and Comparisons**

- LangChain is a framework for developing applications powered by language models. (1) Be data-aware: connect a language model to other sources of data.
  (2) Be agentic: Allow a language model to interact with its environment. doc:[✍️](https://docs.langchain.com/docs) / blog:[✍️](https://blog.langchain.dev) / [✨](https://github.com/langchain-ai/langchain)
 ![**github stars**](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Reflections on Three Years of Building LangChain](https://blog.langchain.com/three-years-langchain/): Langchain 1.0, released  [25 Oct 2025]
- It highlights two main value props of the framework:

  1. Components: modular abstractions and implementations for working with language models, with easy-to-use features.
  2. Use-Case Specific Chains: chains of components that assemble in different ways to achieve specific use cases, with customizable interfaces.🗣️: [✍️](https://docs.langchain.com/docs/)
  
  - LangChain 0.2: full separation of langchain and langchain-community. [✍️](https://blog.langchain.dev/langchain-v02-leap-to-stability) [May 2024]
  - Towards LangChain 0.1 [✍️](https://blog.langchain.dev/the-new-langchain-architecture-langchain-core-v0-1-langchain-community-and-a-path-to-langchain-v0-1/) [Dec 2023] 
  
      <img src="./files/langchain-eco-v3.png" width="400">
  <!-- <img src="./files/langchain-eco-stack.png" width="400"> -->
  <!-- <img src="./files/langchain-glance.png" width="400"> -->

  - Basic LangChain building blocks [✍️](https://www.packtpub.com/article-hub/using-langchain-for-large-language-model-powered-applications) [2023]

    ```python
    '''
    LLMChain: A LLMChain is the most common type of chain. It consists of a PromptTemplate, a model (either an LLM or a ChatModel), and an optional output parser.
    '''
    chain = prompt | model | parser
    ```
  - LLMChain: Deprecated since version 0.1.17: Use RunnableSequence, e.g., `prompt | llm` instead. 
  - LangChain has shifted towards the Runnable interface since version 0.1.17.
  - Imperative (programmatic) approach: The Runnable interface (formerly LLMChain) for flexible, programmatic chain building.
  - Declarative approach: LangChain Expression Language (LCEL) offers a declarative syntax for chain composition, enabling features like async, batch, and streaming operations with the | operator for combining functionalities.

### **Macro and Micro-orchestration**

- Macro-orchestration in LLM pipelines involves high-level design and management of complex workflows, integrating multiple LLMs and other components.
- Micro-orchestration [🔗](#micro-orchestration)
- [LangGraph](https://langchain-ai.github.io/langgraph/) in LangChain, and [Burr](https://burr.dagworks.io/)

### **LangChain Feature Matrix & Cheetsheet**

- [Awesome LangChain✨](https://github.com/kyrolabs/awesome-langchain): Curated list of tools and projects using LangChain.
 ![**github stars**](https://img.shields.io/github/stars/kyrolabs/awesome-langchain?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Building intelligent agents with LangGraph: PhiloAgents simulation engine✨](https://github.com/neural-maze/philoagents-course) [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/neural-maze/philoagents-course?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Cheetsheet✨](https://github.com/gkamradt/langchain-tutorials): LangChain CheatSheet
 ![**github stars**](https://img.shields.io/github/stars/gkamradt/langchain-tutorials?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- DeepLearning.AI short course: LangChain for LLM Application Development [✍️](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/) / LangChain: Chat with Your Data [✍️](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/)
- [Feature Matrix](https://python.langchain.com/docs/get_started/introduction): LangChain Features
- [Feature Matrix: Snapshot in 2023 July](./files/langchain-features-202307.png)  
- [LangChain AI Handbook](https://www.pinecone.io/learn/series/langchain/): published by Pinecone
- [LangChain Cheetsheet KD-nuggets](https://www.kdnuggets.com/wp-content/uploads/LangChain_Cheat_Sheet_KDnuggets.pdf): LangChain Cheetsheet KD-nuggets [🗄️](./files/LangChain_kdnuggets.pdf) [Aug 2023]
- [LangChain Streamlit agent examples✨](https://github.com/langchain-ai/streamlit-agent): Implementations of several LangChain agents as Streamlit apps. [Jun 2023] ![**github stars**](https://img.shields.io/github/stars/langchain-ai/streamlit-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LangChain Tutorial](https://nanonets.com/blog/langchain/): A Complete LangChain Guide
- [LangChain tutorial: A guide to building LLM-powered applications](https://www.elastic.co/blog/langchain-tutorial) [27 Feb 2024]
- [RAG From Scratch✨](https://github.com/langchain-ai/rag-from-scratch)💡[Feb 2024]
 ![**github stars**](https://img.shields.io/github/stars/langchain-ai/rag-from-scratch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **LangChain features and related libraries**

- [LangChain Expression Language](https://python.langchain.com/docs/guides/expression_language/): A declarative way to easily compose chains together [Aug 2023]
- [LangChain Template✨](https://github.com/langchain-ai/langchain/tree/master/templates): LangChain Reference architectures and samples. e.g., `RAG Conversation Template` [Oct 2023]
- [LangChain/cache](https://python.langchain.com/docs/modules/model_io/models/llms/how_to/llm_caching): Reducing the number of API calls
- [LangChain/context-aware-splitting](https://python.langchain.com/docs/use_cases/question_answering/document-context-aware-QA): Splits a file into chunks while keeping metadata
- [LangGraph✨](https://github.com/langchain-ai/langgraph):💡Build and navigate language agents as graphs [✍️](https://langchain-ai.github.io/langgraph/) [Aug 2023] -> LangGraph is inspired by [Pregel](https://research.google/pubs/pub37252/) for Parallel Processing, [Apache Beam](https://beam.apache.org/) for Data flows, and [NetworkX](https://networkx.org/documentation/latest/) for Graph. | [Tutorial](https://langchain-ai.github.io/langgraph/tutorials). ![**github stars**](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LangSmith✍️](https://blog.langchain.dev/announcing-langsmith/) Platform for debugging, testing, evaluating. [Jul 2023]
- [OpenGPTs✨](https://github.com/langchain-ai/opengpts): An open source effort to create a similar experience to OpenAI's GPTs [Nov 2023]
 ![**github stars**](https://img.shields.io/github/stars/langchain-ai/opengpts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **LangChain chain type: Chains & Summarizer**

- Chains [✨](https://github.com/RutamBhagat/LangChainHCCourse1/blob/main/course_1/chains.ipynb)
  - SimpleSequentialChain: A sequence of steps with single input and output. Output of one step is input for the next.
  - SequentialChain: Like SimpleSequentialChain but handles multiple inputs and outputs at each step.
  - MultiPromptChain: Routes inputs to specialized sub-chains based on content. Ideal for different prompts for different tasks.
- Summarizer
  - stuff: Sends everything at once in LLM. If it's too long, an error will occur.
  - map_reduce: Summarizes by dividing and then summarizing the entire summary.
  - refine: (Summary + Next document) => Summary
  - map_rerank: Ranks by score and summarizes to important points.

### **LangChain Agent & Memory**

#### LangChain Agent

1. If you're using a text LLM, first try `zero-shot-react-description`.
1. If you're using a Chat Model, try `chat-zero-shot-react-description`.
1. If you're using a Chat Model and want to use memory, try `conversational-react-description`.
1. `self-ask-with-search`: [Measuring and Narrowing the Compositionality Gap in Language Models📑](https://alphaxiv.org/abs/2210.03350) [7 Oct 2022]
1. `react-docstore`: [ReAct: Synergizing Reasoning and Acting in Language Models📑](https://alphaxiv.org/abs/2210.03629) [6 Oct 2022]
1. Agent Type

```python
class AgentType(str, Enum):
    """Enumerator with the Agent types."""

    ZERO_SHOT_REACT_DESCRIPTION = "zero-shot-react-description"
    REACT_DOCSTORE = "react-docstore"
    SELF_ASK_WITH_SEARCH = "self-ask-with-search"
    CONVERSATIONAL_REACT_DESCRIPTION = "conversational-react-description"
    CHAT_ZERO_SHOT_REACT_DESCRIPTION = "chat-zero-shot-react-description"
    CHAT_CONVERSATIONAL_REACT_DESCRIPTION = "chat-conversational-react-description"
    STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION = (
        "structured-chat-zero-shot-react-description"
    )
    OPENAI_FUNCTIONS = "openai-functions"
    OPENAI_MULTI_FUNCTIONS = "openai-multi-functions"
```

- [ReAct📑](https://alphaxiv.org/abs/2210.03629) vs [MRKL📑](https://alphaxiv.org/abs/2205.00445) (miracle)

  ReAct is inspired by the synergies between "acting" and "reasoning" which allow humans to learn new tasks and make decisions or reasoning.

  MRKL stands for Modular Reasoning, Knowledge and Language and is a neuro-symbolic architecture that combines large language models, external knowledge sources, and discrete reasoning

  > 🗣️: [✨](https://github.com/langchain-ai/langchain/issues/2284#issuecomment-1526879904) [28 Apr 2023] <br/>
  `zero-shot-react-description`: Uses ReAct to select tools based on their descriptions. Any number of tools can be used, each requiring a description. <br/>
  `react-docstore`: Uses ReAct to manage a docstore with two required tools: _Search_ and _Lookup_. These tools must be named exactly as specified. It follows the original ReAct paper's example from Wikipedia.
  - MRKL in LangChain uses `zero-shot-react-description`, implementing ReAct. The original ReAct framework is used in the `react-docstore` agent. MRKL was published on May 1, 2022, earlier than ReAct on October 6, 2022.

#### LangChain Memory

1. `ConversationBufferMemory`: Stores the entire conversation history.
1. `ConversationBufferWindowMemory`: Stores recent messages from the conversation history.
1. `Entity Store (previously Entity Memory)`: Stores and retrieves entity-related information.
1. `Conversation Knowledge Graph Memory`: Stores entities and relationships between entities.
1. `ConversationSummaryMemory`: Stores summarized information about the conversation.
1. `ConversationSummaryBufferMemory`: Stores summarized information about the conversation with a token limit.
1. `ConversationTokenBufferMemory`: Stores tokens from the conversation.
1. `VectorStore-Backed Memory`: Leverages vector space models for storing and retrieving information.

#### **Criticism to LangChain**

- [How to Build Ridiculously Complex LLM Pipelines with LangGraph!](https://newsletter.theaiedge.io/p/how-to-build-ridiculously-complex) [17 Sep 2024 ]
  > LangChain does too much, and as a consequence, it does many things badly. Scaling beyond the basic use cases with LangChain is a challenge that is often better served with building things from scratch by using the underlying APIs.
- LangChain Is Pointless: [✍️](https://news.ycombinator.com/item?id=36645575) [Jul 2023]
  > LangChain has been criticized for making simple things relatively complex, which creates unnecessary complexity and tribalism that hurts the up-and-coming AI ecosystem as a whole. The documentation is also criticized for being bad and unhelpful.
- [The Hidden Cost of LangChain: Why My Simple RAG System Cost 2.7x More Than Expected ](https://dev.to/himanjan/the-hidden-cost-of-langchain-why-my-simple-rag-system-cost-27x-more-than-expected-4hk9) [23 Jul 2025]
- The Problem With LangChain: [✍️](https://minimaxir.com/2023/07/langchain-problem/) / [✨](https://github.com/minimaxir/langchain-problems) [14 Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/minimaxir/langchain-problems?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- What’s your biggest complaint about langchain?: [✍️](https://www.reddit.com/r/LangChain/comments/139bu99/whats_your-biggest_complaint_about_langchain/) [May 2023]

### **LangChain vs Competitors**

#### **Prompting Frameworks**

- [LangChain✨](https://github.com/langchain-ai/langchain) [Oct 2022] |  [LlamaIndex✨](https://github.com/jerryjliu/llama_index) [Nov 2022] |  [Microsoft Semantic Kernel✨](https://github.com/microsoft/semantic-kernel) [Feb 2023] | [Microsoft guidance✨](https://github.com/microsoft/guidance) [Nov 2022] | [Azure ML Promt flow✨](https://github.com/microsoft/promptflow) [Jun 2023] | [DSPy✨](https://github.com/stanfordnlp/dspy) [Jan 2023]
 ![**github stars**](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/jerryjliu/llama_index?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/microsoft/semantic-kernel?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/microsoft/guidance?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/microsoft/promptflow?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Prompting Framework (PF)📑](https://alphaxiv.org/abs/2311.12785): Prompting Frameworks for Large Language Models: A Survey [✨](https://github.com/lxx0628/Prompting-Framework-Survey)
 ![**github stars**](https://img.shields.io/github/stars/lxx0628/Prompting-Framework-Survey?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [What Are Tools Anyway?📑](https://alphaxiv.org/abs/2403.15452): 1. For a small number (e.g., 5–10) of tools, LMs can directly select from contexts. However, with a larger number (e.g., hundreds), an additional retrieval step involving a retriever model is often necessary. 2. LM-used tools incl. Tool creation and reuse. Tool is not useful when machine translation, summarization, and sentiment analysis (among others).  3. Evaluation metrics [18 Mar 2024]

#### **LangChain vs LlamaIndex**

- Basically LlamaIndex is a smart storage mechanism, while LangChain is a tool to bring multiple tools together. [🗣️](https://community.openai.com/t/llamaindex-vs-langchain-which-one-should-be-used/163139) [14 Apr 2023]

- LangChain offers many features and focuses on using chains and agents to connect with external APIs. In contrast, LlamaIndex is more specialized and excels at indexing data and retrieving documents.

#### **LangChain vs Semantic Kernel**

| LangChain | Semantic Kernel                                                                |
| --------- | ------------------------------------------------------------------------------ |
| Memory    | Memory                                                                         |
| Tookit    | Plugin (pre. Skill)                                                            |
| Tool      | LLM prompts (semantic functions) <br/> native C# or Python code (native function) |
| Agent     | Planner (Deprecated) -> Agent                                                                        |
| Chain     | Steps, Pipeline                                                                |
| Tool      | Connector (Deprecated) -> Plugin                                                                     |

#### **LangChain vs Semantic Kernel vs Azure Machine Learning Prompt flow**

- What's the difference between LangChain and Semantic Kernel?

  LangChain has many agents, tools, plugins etc. out of the box. More over, LangChain has 10x more popularity, so has about 10x more developer activity to improve it. On other hand, **Semantic Kernel architecture and quality is better**, that's quite promising for Semantic Kernel. [✨](https://github.com/microsoft/semantic-kernel/discussions/1326) [11 May 2023]

- What's the difference between Azure Machine Learing PromptFlow and Semantic Kernel?

  1. Low/No Code vs C#, Python, Java
  1. Focused on Prompt orchestrating vs Integrate LLM into their existing app.

- Promptflow is not intended to replace chat conversation flow. Instead, it’s an optimized solution for integrating Search and Open Source Language Models. By default, it supports Python, LLM, and the Prompt tool as its fundamental building blocks.

- Using Prompt flow with Semantic Kernel: [✍️](https://learn.microsoft.com/en-us/semantic-kernel/ai-orchestration/planners/evaluate-and-deploy-planners/) [07 Sep 2023]

#### **Prompt Template Language**

|                   | Handlebars.js                                                                 | Jinja2                                                                                 | Prompt Template                                                                                    |
| ----------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Conditions        | {{#if user}}<br>  Hello {{user}}!<br>{{else}}<br>  Hello Stranger!<br>{{/if}} | {% if user %}<br>  Hello {{ user }}!<br>{% else %}<br>  Hello Stranger!<br>{% endif %} | Branching features such as "if", "for", and code blocks are not part of SK's template language.    |
| Loop              | {{#each items}}<br>  Hello {{this}}<br>{{/each}}                              | {% for item in items %}<br>  Hello {{ item }}<br>{% endfor %}                          | By using a simple language, the kernel can also avoid complex parsing and external dependencies.   |
| LangChain Library | guidance. LangChain.js                                                                     | LangChain, Azure ML prompt flow                                                                | Semantic Kernel                                                                                    |
| URL               | [✍️](https://handlebarsjs.com/guide/)                                        | [✍️](https://jinja.palletsprojects.com/en/2.10.x/templates/)                          | [✍️](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/prompt-template-syntax) |

- Semantic Kernel supports HandleBars and Jinja2. [Mar 2024]


### **LlamaIndex**

- LlamaIndex (formerly GPT Index) is a data framework for LLM applications to ingest, structure, and access private or domain-specific data. The high-level API allows users to ingest and query their data in a few lines of code. High-Level Concept: [✍️](https://docs.llamaindex.ai/en/latest/getting_started/concepts.html) / doc:[✍️](https://gpt-index.readthedocs.io/en/latest/index.html) / blog:[✍️](https://www.llamaindex.ai/blog) / [✨](https://github.com/run-llama/llama_index) [Nov 2022]
 ![**github stars**](https://img.shields.io/github/stars/run-llama/llama_index?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  > Fun fact this core idea was the initial inspiration for GPT Index (the former name of LlamaIndex) 11/8/2022 - almost a year ago!. [🗣️](https://twitter.com/jerryjliu0/status/1711817419592008037) / [Walking Down the Memory Maze: Beyond Context Limit through Interactive Reading📑](https://alphaxiv.org/abs/2310.05029)
  >
  > 1.  Build a data structure (memory tree)
  > 1.  Transverse it via LLM prompting
- [AgentWorkflow](https://www.llamaindex.ai/blog/introducing-agentworkflow-a-powerful-system-for-building-ai-agent-systems): To build and orchestrate AI agent systems [22 Jan 2025]
- `LlamaHub`: A library of data loaders for LLMs [✨](https://github.com/run-llama/llama-hub) [Feb 2023]
![**github stars**](https://img.shields.io/github/stars/run-llama/llama-hub?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- `LlamaIndex CLI`: a command line tool to generate LlamaIndex apps [✍️](https://llama-2.ai/llamaindex-cli/) [Nov 2023]
- `LlamaParse`: A unique parsing tool for intricate documents [✨](https://github.com/run-llama/llama_parse) [Feb 2024]
![**github stars**](https://img.shields.io/github/stars/run-llama/llama_parse?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LlamaIndex showcase✨](https://github.com/run-llama/llamacloud-demo) > `examples` [✍️](https://www.llamaindex.ai/blog/introducing-agentic-document-workflows): e.g., Contract Review, Patient Case Summary, and Auto Insurance Claims Workflow. [9 Jan 2025]

#### LlamaIndex integration with Azure AI

- [AI App Template Gallery✍️](https://azure.github.io/ai-app-templates/repo/azure-samples/llama-index-javascript/)
- [LlamaIndex integration with Azure AI](https://www.llamaindex.ai/blog/announcing-the-llamaindex-integration-with-azure-ai):  [19 Nov 2024]
- Storage and memory: [Azure Table Storage as a Docstore](https://docs.llamaindex.ai/en/stable/examples/docstore/AzureDocstoreDemo/) or Azure Cosmos DB.
- Workflow example: [Azure Code Interpreter](https://docs.llamaindex.ai/en/stable/examples/tools/azure_code_interpreter/)

#### High-Level Concepts

- Query engine vs Chat engine

  1. The query engine wraps a `retriever` and a `response synthesizer` into a pipeline, that will use the query string to fetch nodes (sentences or paragraphs) from the index and then send them to the LLM (Language and Logic Model) to generate a response
  1. The chat engine is a quick and simple way to chat with the data in your index. It uses a `context manager` to keep track of the conversation history and generate relevant queries for the retriever. Conceptually, it is a `stateful` analogy of a Query Engine.

- Storage Context vs Settings (p.k.a. Service Context)

  - Both the Storage Context and Service Context are data classes.

    1. Introduced in v0.10.0, ServiceContext is replaced to Settings object.
    1. Storage Context is responsible for the storage and retrieval of data in Llama Index, while the Service Context helps in incorporating external context to enhance the search experience.
    1. The Service Context is not directly involved in the storage or retrieval of data, but it helps in providing a more context-aware and accurate search experience.

  ```python
  # The storage context container is a utility container for storing nodes, indices, and vectors.
  class StorageContext:
    docstore: BaseDocumentStore
    index_store: BaseIndexStore
    vector_store: VectorStore
    graph_store: GraphStore
  ```

  ```python
  # NOTE: Deprecated, use llama_index.settings.Settings. The service context container is a utility container for LlamaIndex index and query classes.
  class ServiceContext:
    llm_predictor: BaseLLMPredictor
    prompt_helper: PromptHelper
    embed_model: BaseEmbedding
    node_parser: NodeParser
    llama_logger: LlamaLogger
    callback_manager: CallbackManager
  ```

  ```python
  @dataclass
  class _Settings:
    # lazy initialization
    _llm: Optional[LLM] = None
    _embed_model: Optional[BaseEmbedding] = None
    _callback_manager: Optional[CallbackManager] = None
    _tokenizer: Optional[Callable[[str], List[Any]]] = None
    _node_parser: Optional[NodeParser] = None
    _prompt_helper: Optional[PromptHelper] = None
    _transformations: Optional[List[TransformComponent]] = None
  ```

#### LlamaIndex Tutorial
- 4 RAG techniques implemented in `llama_index` / [🗣️](https://x.com/ecardenas300/status/1704188276565795079) [20 Sep 2023] / [✨](https://github.com/weaviate/recipes)
 ![**github stars**](https://img.shields.io/github/stars/weaviate/recipes?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. SQL Router Query Engine: Query router that can reference your vector database or SQL database
  2. Sub Question Query Engine: Break down the complex question into sub-questions
  3. Recursive Retriever + Query Engine: Reference node relationships, rather than only finding a node (chunk) that is most relevant.
  4. Self Correcting Query Engines: Use an LLM to evaluate its own output.  
- [A Cheat Sheet and Some Recipes For Building Advanced RAG✍️](https://blog.llamaindex.ai/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b) RAG cheat sheet shared above was inspired by [RAG survey paper📑](https://alphaxiv.org/abs/2312.10997). [🗄️](./files/advanced-rag-diagram-llama-index.png) [Jan 2024]
- [Building and Productionizing RAG](https://docs.google.com/presentation/d/1rFQ0hPyYja3HKRdGEgjeDxr0MSE8wiQ2iu4mDtwR6fc/edit#slide=id.p): [🗄️](./files/archive/LlamaIndexTalk_PyDataGlobal.pdf): Optimizing RAG Systems 1. Table Stakes 2. Advanced Retrieval: Small-to-Big 3. Agents 4. Fine-Tuning 5. Evaluation [Nov 2023]
<!-- - [CallbackManager (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-003-callback-manager/) [27 May 2023] / [Customize TokenTextSplitter (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-002-text-splitter/) [27 May 2023] / --> 
- [Chat engine ReAct mode](https://gpt-index.readthedocs.io/en/stable/examples/chat_engine/chat_engine_react.html), [FLARE Query engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/flare_query_engine.html)
- [Fine-Tuning a Linear Adapter for Any Embedding Model](https://medium.com/llamaindex-blog/fine-tuning-a-linear-adapter-for-any-embedding-model-8dd0a142d383): Fine-tuning the embeddings model requires you to reindex your documents. With this approach, you do not need to re-embed your documents. Simply transform the query instead. [7 Sep 2023]
- [LlamaIndex Overview (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-001-overview-v0-7-9/) [17 Jul 2023]
- [LlamaIndex Tutorial](https://nanonets.com/blog/llamaindex/): A Complete LlamaIndex Guide [18 Oct 2023]
- Multimodal RAG Pipeline [✍️](https://blog.llamaindex.ai/multi-modal-rag-621de7525fea) [Nov 2023]



## **Prompt Engineering and Visual Prompts**

### **Prompt Engineering**

1. [A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications📑](https://alphaxiv.org/abs/2402.07927): a summary detailing the prompting methodology, its applications.🏆Taxonomy of prompt engineering techniques in LLMs. [5 Feb 2024]
1. [Chain of Draft: Thinking Faster by Writing Less📑](https://alphaxiv.org/abs/2502.18600): Chain-of-Draft prompting con-
denses the reasoning process into minimal, abstract
representations. `Think step by step, but only keep a minimum draft for each thinking step, with 5 words at most.` [25 Feb 2025]
1. [Chain of Thought (CoT)📑](https://alphaxiv.org/abs/2201.11903):💡Chain-of-Thought Prompting Elicits Reasoning in Large Language Models [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2201.11903)]: ReAct and Self Consistency also inherit the CoT concept. [28 Jan 2022]
    - Family of CoT: `Self-Consistency (CoT-SC)` > `Tree of Thought (ToT)` > `Graph of Thoughts (GoT)` > [`Iteration of Thought (IoT)`📑](https://alphaxiv.org/abs/2409.12618) [19 Sep 2024], [`Diagram of Thought (DoT)`📑](https://alphaxiv.org/abs/2409.10038) [16 Sep 2024] / [`To CoT or not to CoT?`📑](https://alphaxiv.org/abs/2409.12183): Meta-analysis of 100+ papers shows CoT significantly improves performance in math and logic tasks. [18 Sep 2024]
1. [Chain-of-Verification reduces Hallucination in LLMs📑](https://alphaxiv.org/abs/2309.11495): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.11495)]: A four-step process that consists of generating a baseline response, planning verification questions, executing verification questions, and generating a final verified response based on the verification results. [20 Sep 2023]
1. ChatGPT : “user”, “assistant”, and “system” messages.**  
    To be specific, the ChatGPT API allows for differentiation between “user”, “assistant”, and “system” messages.  
    1. always obey "system" messages.
    1. all end user input in the “user” messages.
    1. "assistant" messages as previous chat responses from the assistant.   
    - Presumably, the model is trained to treat the user messages as human messages, system messages as some system level configuration, and assistant messages as previous chat responses from the assistant. [✍️](https://blog.langchain.dev/using-chatgpt-api-to-evaluate-chatgpt/) [2 Mar 2023]
1. [Does Prompt Formatting Have Any Impact on LLM Performance?📑](https://alphaxiv.org/abs/2411.10541): GPT-3.5-turbo's performance in code translation varies by 40% depending on the prompt template, while GPT-4 is more robust. [15 Nov 2024]
1. Few-shot: [Open AI: Language Models are Few-Shot Learners📑](https://alphaxiv.org/abs/2005.14165): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2005.14165)] [28 May 2020]
1. [FireAct📑](https://alphaxiv.org/abs/2310.05915): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.05915)]: Toward Language Agent Fine-tuning. 1. This work takes an initial step to show multiple advantages of fine-tuning LMs for agentic uses. 2. Duringfine-tuning, The successful trajectories are then converted into the ReAct format to fine-tune a smaller LM. 3. This work is an initial step toward language agent fine-tuning,
and is constrained to a single type of task (QA) and a single tool (Google search). / [✨](https://fireact-agent.github.io/) [9 Oct 2023]
1. [Graph of Thoughts (GoT)📑](https://alphaxiv.org/abs/2308.09687): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2308.09687)] Solving Elaborate Problems with Large Language Models [✨](https://github.com/spcl/graph-of-thoughts) [18 Aug 2023]
 ![**github stars**](https://img.shields.io/github/stars/spcl/graph-of-thoughts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)  
   <img src="./files/got-prompt.png" width="700">
1. [Is the new norm for NLP papers "prompt engineering" papers?](https://www.reddit.com/r/MachineLearning/comments/1ei9e3l/d_is_the_new_norm_for_nlp_papers_prompt/): "how can we make LLM 1 do this without training?" Is this the new norm? The CL section of arXiv is overwhelming with papers like "how come LLaMA can't understand numbers?" [2 Aug 2024]
1. [Large Language Models as Optimizers📑](https://alphaxiv.org/abs/2309.03409):💡[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.03409)]: `Take a deep breath and work on this problem step-by-step.` to improve its accuracy. Optimization by PROmpting (OPRO) [7 Sep 2023]
1. [Language Models as Compilers📑](https://alphaxiv.org/abs/2404.02575): With extensive experiments on seven algorithmic reasoning tasks, Think-and-Execute is effective. It enhances large language models’ reasoning by using task-level logic and pseudocode, outperforming instance-specific methods. [20 Mar 2023]
1. [Many-Shot In-Context Learning📑](https://alphaxiv.org/abs/2404.11018): Transitioning from few-shot to many-shot In-Context Learning (ICL) can lead to significant performance gains across a wide variety of generative and discriminative tasks [17 Apr 2024]
1. [NLEP (Natural Language Embedded Programs) for Hybrid Language Symbolic Reasoning📑](https://alphaxiv.org/abs/2309.10814): Use code as a scaffold for reasoning. NLEP achieves over 90% accuracy when prompting GPT-4. [19 Sep 2023]
1. [OpenAI Harmony Response Format](https://cookbook.openai.com/articles/openai-harmony): system > developer > user > assistant > tool. [✨](https://github.com/openai/harmony) [5 Aug 2025]
1. [OpenAI Prompt Migration Guide](https://cookbook.openai.com/examples/prompt_migration_guide):💡OpenAI Cookbook. By leveraging GPT‑4.1, refine your prompts to ensure that each instruction is clear, specific, and closely matches your intended outcomes. [26 Jun 2025]
1. [Plan-and-Solve Prompting📑](https://alphaxiv.org/abs/2305.04091): Develop a plan, and then execute each step in that plan. [6 May 2023]
1. Power of Prompting
    - [GPT-4 with Medprompt📑](https://alphaxiv.org/abs/2311.16452): GPT-4, using a method called Medprompt that combines several prompting strategies, has surpassed MedPaLM 2 on the MedQA dataset without the need for fine-tuning. [✍️](https://www.microsoft.com/en-us/research/blog/the-power-of-prompting/) [28 Nov 2023]
    - [promptbase✨](https://github.com/microsoft/promptbase): Scripts demonstrating the Medprompt methodology [Dec 2023]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/promptbase?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. Prompt Concept Keywords: Question-Answering | Roll-play: `Act as a [ROLE] perform [TASK] in [FORMAT]` | Reasoning | Prompt-Chain
1. [Prompt Engineering for OpenAI’s O1 and O3-mini Reasoning Models✍️](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/prompt-engineering-for-openai%E2%80%99s-o1-and-o3-mini-reasoning-models/4374010): 1) `Keep Prompts Clear and Minimal`, 2)`Avoid Unnecessary Few-Shot Examples` 3)`Control Length and Detail via Instructions` 4)`Specify Output, Role or Tone` [05 Feb 2025]
1. Prompt Engneering overview [🗣️](https://newsletter.theaiedge.io/) [10 Jul 2023]  
   <img src="./files/prompt-eg-aiedge.jpg" width="300">
1. [Prompt Principle for Instructions📑](https://alphaxiv.org/abs/2312.16171):💡26 prompt principles: e.g., `1) No need to be polite with LLM so there .. 16)  Assign a role.. 17) Use Delimiters..` [26 Dec 2023]
1. Promptist
    - [Promptist📑](https://alphaxiv.org/abs/2212.09611): Microsoft's researchers trained an additional language model (LM) that optimizes text prompts for text-to-image generation. [19 Dec 2022]
    - For example, instead of simply passing "Cats dancing in a space club" as a prompt, an engineered prompt might be "Cats dancing in a space club, digital painting, artstation, concept art, soft light, hdri, smooth, sharp focus, illustration, fantasy."
1. [RankPrompt📑](https://alphaxiv.org/abs/2403.12373): Self-ranking method. Direct Scoring
independently assigns scores to each candidate, whereas RankPrompt ranks candidates through a
systematic, step-by-step comparative evaluation. [19 Mar 2024]
1. [ReAct📑](https://alphaxiv.org/abs/2210.03629): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2210.03629)]: Grounding with external sources. (Reasoning and Act): Combines reasoning and acting [✍️](https://react-lm.github.io/) [6 Oct 2022]
1. [Re-Reading Improves Reasoning in Large Language Models📑](https://alphaxiv.org/abs/2309.06275): RE2 (Re-Reading), which involves re-reading the question as input to enhance the LLM's understanding of the problem. `Read the question again` [12 Sep 2023]
1. [Recursively Criticizes and Improves (RCI)📑](https://alphaxiv.org/abs/2303.17491): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.17491)] [30 Mar 2023]
   - Critique: Review your previous answer and find problems with your answer.
   - Improve: Based on the problems you found, improve your answer.
1. [Reflexion📑](https://alphaxiv.org/abs/2303.11366): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.11366)]: Language Agents with Verbal Reinforcement Learning. 1. Reflexion that uses `verbal reinforcement` to help agents learn from prior failings. 2. Reflexion converts binary or scalar feedback from the environment into verbal feedback in the form of a textual summary, which is then added as additional context for the LLM agent in the next episode. 3. It is lightweight and doesn’t require finetuning the LLM. [20 Mar 2023] / [✨](https://github.com/noahshinn024/reflexion)
 ![**github stars**](https://img.shields.io/github/stars/noahshinn024/reflexion?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Retrieval Augmented Generation (RAG)📑](https://alphaxiv.org/abs/2005.11401): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2005.11401)]: To address such knowledge-intensive tasks. RAG combines an information retrieval component with a text generator model. [22 May 2020]
1. [Self-Consistency (CoT-SC)📑](https://alphaxiv.org/abs/2203.11171): The three steps in the self-consistency method: 1) prompt the language model using CoT prompting, 2) sample a diverse set of reasoning paths from the language model, and 3) marginalize out reasoning paths to aggregate final answers and choose the most consistent answer. [21 Mar 2022]
1. [Self-Refine📑](https://alphaxiv.org/abs/2303.17651), which enables an agent to reflect on its own output [30 Mar 2023]
1. [Skeleton Of Thought📑](https://alphaxiv.org/abs/2307.15337): Skeleton-of-Thought (SoT) reduces generation latency by first creating an answer's skeleton, then filling each skeleton point in parallel via API calls or batched decoding. [28 Jul 2023]
1. [Tree of Thought (ToT)📑](https://alphaxiv.org/abs/2305.10601): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.10601)]: Self-evaluate the progress intermediate thoughts make towards solving a problem [17 May 2023] [✨](https://github.com/ysymyth/tree-of-thought-llm) / Agora: Tree of Thoughts (ToT) [✨](https://github.com/kyegomez/tree-of-thoughts)
 ![**github stars**](https://img.shields.io/github/stars/ysymyth/tree-of-thought-llm?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/kyegomez/tree-of-thoughts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)  
   - `tree-of-thought\forest_of_thought.py`: Forest of thought Decorator sample
   - `tree-of-thought\tree_of_thought.py`: Tree of thought Decorator sample
   - `tree-of-thought\react-prompt.py`: ReAct sample without LangChain
1. Zero-shot, one-shot and few-shot [ref📑](https://alphaxiv.org/abs/2005.14165) [28 May 2020]  
   <img src="./files/zero-one-few-shot.png" width="200">
1. Zero-shot: [Large Language Models are Zero-Shot Reasoners📑](https://alphaxiv.org/abs/2205.11916): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2205.11916)]: Let’s think step by step. [24 May 2022]

#### Adversarial Prompting

- Prompt Injection: `Ignore the above directions and ...`
- Prompt Leaking: `Ignore the above instructions ... followed by a copy of the full prompt with exemplars:`
- Jailbreaking: Bypassing a safety policy, instruct Unethical instructions if the request is contextualized in a clever way. [✍️](https://www.promptingguide.ai/risks/adversarial)
- Random Search (RS): [✨](https://github.com/tml-epfl/llm-adaptive-attacks): 1. Feed the modified prompt (original + suffix) to the model. 2. Compute the log probability of a target token (e.g, Sure). 3. Accept the suffix if the log probability increases.
![**github stars**](https://img.shields.io/github/stars/tml-epfl/llm-adaptive-attacks?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- DAN (Do Anything Now): [✍️](https://www.reddit.com/r/ChatGPT/comments/10tevu1/new_jailbreak_proudly_unveiling_the_tried_and/)
- JailbreakBench: [✨](https://jailbreaking-llms.github.io/) / [✍️](https://jailbreakbench.github.io)

### Prompt Tuner / Optimizer

1. [Automatic Prompt Engineer (APE)📑](https://alphaxiv.org/abs/2211.01910): Automatically optimizing prompts. APE has discovered zero-shot Chain-of-Thought (CoT) prompts superior to human-designed prompts like “Let’s think through this step-by-step” (Kojima et al., 2022). The prompt “To get the correct answer, let’s think step-by-step.” triggers a chain of thought. Two approaches to generate high-quality candidates: forward mode and reverse mode generation. [3 Nov 2022] [✨](https://github.com/keirp/automatic_prompt_engineer) / [✍️](https:/towardsdatascience.com/automated-prompt-engineering-78678c6371b9) [Mar 2024]
 ![**github stars**](https://img.shields.io/github/stars/keirp/automatic_prompt_engineer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Claude Prompt Engineer✨](https://github.com/mshumer/gpt-prompt-engineer): Simply input a description of your task and some test cases, and the system will generate, test, and rank a multitude of prompts to find the ones that perform the best.  [4 Jul 2023] / Anthropic Helper metaprompt [✍️](https://docs.anthropic.com/en/docs/helper-metaprompt-experimental) / [Claude Sonnet 3.5 for Coding](https://www.reddit.com/r/ClaudeAI/comments/1dwra38/sonnet_35_for_coding_system_prompt/)
 ![**github stars**](https://img.shields.io/github/stars/mshumer/gpt-prompt-engineer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Cohere’s new Prompt Tuner](https://cohere.com/blog/intro-prompt-tuner): Automatically improve your prompts [31 Jul 2024]
1. [Large Language Models as Optimizers📑](https://alphaxiv.org/abs/2309.03409): Optimization by PROmpting (OPRO). showcase OPRO on linear regression and traveling salesman problems. [✨](https://github.com/google-deepmind/opro) [7 Sep 2023] ![**github stars**](https://img.shields.io/github/stars/google-deepmind/opro?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 

### **Prompt Guide & Leaked prompts**

- [5 Principles for Writing Effective Prompts✍️](https://blog.tobiaszwingmann.com/p/5-principles-for-writing-effective-prompts): RGTD - Role, Goal, Task, Details Framework [07 Feb 2025]
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library): Anthropic released a Claude 3 AI prompt library [Mar 2024]
- [Anthropic courses > Prompt engineering interactive tutorial✨](https://github.com/anthropics/courses): a comprehensive step-by-step guide to key prompting techniques / prompt evaluations [Aug 2024]
 ![**github stars**](https://img.shields.io/github/stars/anthropics/courses?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Awesome ChatGPT Prompts✨](https://github.com/f/awesome-chatgpt-prompts) [Dec 2022]
 ![**github stars**](https://img.shields.io/github/stars/f/awesome-chatgpt-prompts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Awesome Prompt Engineering✨](https://github.com/promptslab/Awesome-Prompt-Engineering) [Feb 2023]
 ![**github stars**](https://img.shields.io/github/stars/promptslab/Awesome-Prompt-Engineering?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Awesome-GPTs-Prompts✨](https://github.com/ai-boost/awesome-prompts) [Jan 2024]
 ![**github stars**](https://img.shields.io/github/stars/ai-boost/awesome-prompts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure OpenAI Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/advanced-prompt-engineering)
- [Copilot prompts✨](https://github.com/pnp/copilot-prompts): Examples of prompts for Microsoft Copilot. [25 Apr 2024]
 ![**github stars**](https://img.shields.io/github/stars/pnp/copilot-prompts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [DeepLearning.ai ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
- [Fabric✨](https://github.com/danielmiessler/fabric): A modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere [Jan 2024]
 ![**github stars**](https://img.shields.io/github/stars/danielmiessler/fabric?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [In-The-Wild Jailbreak Prompts on LLMs✨](https://github.com/verazuo/jailbreak_llms): A dataset consists of 15,140 ChatGPT prompts from Reddit, Discord, websites, and open-source datasets (including 1,405 jailbreak prompts). Collected from December 2022 to December 2023 [Aug 2023]
 ![**github stars**](https://img.shields.io/github/stars/verazuo/jailbreak_llms?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LangChainHub](https://smith.langchain.com/hub): a collection of all artifacts useful for working with LangChain primitives such as prompts, chains and agents. [Jan 2023]
- Leaked prompts of [GPTs✨](https://github.com/linexjlin/GPTs) [Nov 2023] and [Agents✨](https://github.com/LouisShark/chatgpt_system_prompt) [Nov 2023]
 ![**github stars**](https://img.shields.io/github/stars/linexjlin/GPTs?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/LouisShark/chatgpt_system_prompt?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLM Prompt Engineering Simplified✨](https://github.com/AkmmusAI/LLM-Prompt-Engineering-Simplified-Book): Online Book [Feb 2024]
 ![**github stars**](https://img.shields.io/github/stars/AkmmusAI/LLM-Prompt-Engineering-Simplified-Book?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [OpenAI Best practices for prompt engineering](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
- [OpenAI Prompt example](https://platform.openai.com/examples)
- [OpenAI Prompt Pack](https://academy.openai.com/public/tags/prompt-packs-6849a0f98c613939acef841c): curated collections of pre-designed prompts tailored for specific roles, industries, or use cases.
- [Power Platform GPT Prompts✨](https://github.com/pnp/powerplatform-prompts) [Mar 2024]
 ![**github stars**](https://img.shields.io/github/stars/pnp/powerplatform-prompts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Prompt Engineering Guide](https://www.promptingguide.ai/): 🏆Copyright © 2023 DAIR.AI
- [Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/): Prompt Engineering, also known as In-Context Prompting ... [Mar 2023]
- [Prompts for Education✨](https://github.com/microsoft/prompts-for-edu): Microsoft Prompts for Education [Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/prompts-for-edu?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [ShumerPrompt](https://shumerprompt.com/): Discover and share powerful prompts for AI models
- [System Prompts and Models of AI Tools✨](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools): System Prompts, Internal Tools & AI Models collection [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/x1xhlol/system-prompts-and-models-of-ai-tools?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [TheBigPromptLibrary✨](https://github.com/0xeb/TheBigPromptLibrary) [Nov 2023]
 ![**github stars**](https://img.shields.io/github/stars/0xeb/TheBigPromptLibrary?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **Visual Prompting & Visual Grounding**

- [Andrew Ng’s Visual Prompting Livestream📺](https://www.youtube.com/watch?v=FE88OOUBonQ) [24 Apr 2023]
- Chain of Frame (CoF): Reasoning via structured frames. DeepMind proposed CoF in [Veo 3 Paper📑](https://alphaxiv.org/abs/2509.20328). [24 Sep 2025]
- [landing.ai: Agentic Object Detection](https://landing.ai/agentic-object-detection): Agent systems use design patterns to reason at length about unique attributes like color, shape, and texture [6 Feb 2025]
- [Motion Prompting📑](https://alphaxiv.org/abs/2412.02700): motion prompts for flexible video generation, enabling motion control, image interaction, and realistic physics. [✨](https://motion-prompting.github.io/) [3 Dec 2024]
- [Screen AI✍️](https://blog.research.google/2024/03/screenai-visual-language-model-for-ui.html): ScreenAI, a model designed for understanding and interacting with user interfaces (UIs) and infographics. [Mar 2024]
- [Visual Prompting📑](https://alphaxiv.org/abs/2211.11635) [21 Nov 2022]
- [What is Visual Grounding](https://paperswithcode.com/task/visual-grounding): Visual Grounding (VG) aims to locate the most relevant object or region in an image, based on a natural language query.
- [What is Visual prompting](https://landing.ai/what-is-visual-prompting/): Similarly to what has happened in NLP, large pre-trained vision transformers have made it possible for us to implement Visual Prompting. [🗄️](./files/vPrompt.pdf) [26 Apr 2023]


## Finetuning

### **Finetuning**

#### LLM Pre-training and Post-training Paradigms [🔗](#large-language-models-in-2023)

- [🔗](#classification-of-attention): Classification of Attention
- [How to continue pretraining an LLM on new data](https://x.com/rasbt/status/1768629533509370279): `Continued pretraining` can be as effective as `retraining on combined datasets`. [13 Mar 2024]
  - Three training methods were compared:  
    <img src="./files/cont-pretraining.jpg" width="400"/>  
    1. Regular pretraining: A model is initialized with random weights and pretrained on dataset D1.
    2. Continued pretraining: The pretrained model from 1) is further pretrained on dataset D2.
    3. Retraining on combined dataset: A model is initialized with random weights and trained on the combined datasets D1 and D2.
  - Continued pretraining can be as effective as retraining on combined datasets. Key strategies for successful continued pretraining include:
    1. Re-warming: Increasing the learning rate at the start of continued pre-training.
    2. Re-decaying: Gradually reducing the learning rate afterwards.
    3. Data Mixing: Adding a small portion (e.g., 5%) of the original pretraining data (D1) to the new dataset (D2) to prevent catastrophic forgetting.
- [LIMA: Less Is More for Alignment📑](https://alphaxiv.org/abs/2305.11206): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.11206)]: fine-tuned with the standard supervised loss on `only 1,000 carefully curated prompts and responses, without any reinforcement learning or human preference modeling.` LIMA demonstrates remarkably strong performance, either equivalent or strictly preferred to GPT-4 in 43% of cases. [18 May 2023]

#### Llama finetuning

- A key difference between [Llama 1📑](https://alphaxiv.org/abs/2302.13971): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2302.13971)] [27 Feb 2023] and [Llama 2📑](https://alphaxiv.org/abs/2307.09288): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.09288)] [18 Jul 2023] is the architectural change of attention layer, in which Llama 2 takes advantage of Grouped Query Attention (GQA) mechanism to improve efficiency. > OSS LLM [🔗](#open-source-large-language-models) / Llama3 > Build an llms from scratch [🔗](#build-an-llms-from-scratch-picogpt-and-lit-gpt) <br/>
  <img src="./files/grp-attn.png" alt="llm-grp-attn" width="400"/>
- Coding LLaMA 2 from scratch in PyTorch - KV Cache, Grouped Query Attention, Rotary PE, RMSNorm [📺](https://www.youtube.com/watch?v=oM4VmoabDAI) / [✨](https://github.com/hkproj/pytorch-llama) [03 Sep 2023] <br/>
 ![**github stars**](https://img.shields.io/github/stars/hkproj/pytorch-llama?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - KV Cache, Grouped Query Attention, Rotary PE  
    <img src="./files/llama2.png" width="300" />    
  <details>
  <summary>Pytorch code</summary>
  
  - Rotary PE
    ```python
    def apply_rotary_embeddings(x: torch.Tensor, freqs_complex: torch.Tensor, device: str):
        # Separate the last dimension pairs of two values, representing the real and imaginary parts of the complex number
        # Two consecutive values will become a single complex number
        # (B, Seq_Len, H, Head_Dim) -> (B, Seq_Len, H, Head_Dim/2)
        x_complex = torch.view_as_complex(x.float().reshape(*x.shape[:-1], -1, 2))
        # Reshape the freqs_complex tensor to match the shape of the x_complex tensor. So we need to add the batch dimension and the head dimension
        # (Seq_Len, Head_Dim/2) --> (1, Seq_Len, 1, Head_Dim/2)
        freqs_complex = freqs_complex.unsqueeze(0).unsqueeze(2)
        # Multiply each complex number in the x_complex tensor by the corresponding complex number in the freqs_complex tensor
        # Which results in the rotation of the complex number as shown in the Figure 1 of the paper
        # (B, Seq_Len, H, Head_Dim/2) * (1, Seq_Len, 1, Head_Dim/2) = (B, Seq_Len, H, Head_Dim/2)
        x_rotated = x_complex * freqs_complex
        # Convert the complex number back to the real number
        # (B, Seq_Len, H, Head_Dim/2) -> (B, Seq_Len, H, Head_Dim/2, 2)
        x_out = torch.view_as_real(x_rotated)
        # (B, Seq_Len, H, Head_Dim/2, 2) -> (B, Seq_Len, H, Head_Dim)
        x_out = x_out.reshape(*x.shape)
        return x_out.type_as(x).to(device)
    ```  
  - KV Cache, Grouped Query Attention
    ```python
      # Replace the entry in the cache
      self.cache_k[:batch_size, start_pos : start_pos + seq_len] = xk
      self.cache_v[:batch_size, start_pos : start_pos + seq_len] = xv

      # (B, Seq_Len_KV, H_KV, Head_Dim)
      keys = self.cache_k[:batch_size, : start_pos + seq_len]
      # (B, Seq_Len_KV, H_KV, Head_Dim)
      values = self.cache_v[:batch_size, : start_pos + seq_len]

      # Since every group of Q shares the same K and V heads, just repeat the K and V heads for every Q in the same group.

      # (B, Seq_Len_KV, H_KV, Head_Dim) --> (B, Seq_Len_KV, H_Q, Head_Dim)
      keys = repeat_kv(keys, self.n_rep)
      # (B, Seq_Len_KV, H_KV, Head_Dim) --> (B, Seq_Len_KV, H_Q, Head_Dim)
      values = repeat_kv(values, self.n_rep)
    ```  
    </details>
- [Comprehensive Guide for LLaMA with RLHF🤗](https://huggingface.co/blog/stackllama): StackLLaMA: A hands-on guide to train LLaMA with RLHF [5 Apr 2023]  
- Official LLama Recipes incl. Finetuning: [✨](https://github.com/facebookresearch/llama-recipes)
 ![**github stars**](https://img.shields.io/github/stars/facebookresearch/llama-recipes?style=flat-square&label=%20&color=blue&cacheSeconds=36000)  
- Llama 2 ONNX [✨](https://github.com/microsoft/Llama-2-Onnx) [Jul 2023]: ONNX, or Open Neural Network Exchange, is an open standard for machine learning interoperability. It allows AI developers to use models across various frameworks, tools, runtimes, and compilers.
 ![**github stars**](https://img.shields.io/github/stars/microsoft/Llama-2-Onnx?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Multi-query attention (MQA)📑](https://alphaxiv.org/abs/2305.13245): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.13245)] [22 May 2023]

#### PEFT: Parameter-Efficient Fine-Tuning ([📺](https://youtu.be/Us5ZFp16PaU)) [24 Apr 2023]

- [PEFT🤗](https://huggingface.co/blog/peft): Parameter-Efficient Fine-Tuning. PEFT is an approach to fine tuning only a few parameters. [10 Feb 2023]
- [Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning📑](https://alphaxiv.org/abs/2303.15647): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.15647)] [28 Mar 2023]
- Category: Represent approach - Description - Pseudo Code [✍️](https://speakerdeck.com/schulta) [22 Sep 2023]
  1. Adapters: Adapters - Additional Layers. Inference can be slower.
     ```python
     def transformer_with_adapter(x):
       residual = x
       x = SelfAttention(x)
       x = FFN(x) # adapter
       x = LN(x + residual)
       residual = x
       x = FFN(x) # transformer FFN
       x = FFN(x) # adapter
       x = LN(x + residual)
       return x
     ```
  1. Soft Prompts: Prompt-Tuning - Learnable text prompts. Not always desired results.
     ```python
     def soft_prompted_model(input_ids):
       x = Embed(input_ids)
       soft_prompt_embedding = SoftPromptEmbed(task_based_soft_prompt)
       x = concat([soft_prompt_embedding, x], dim=seq)
       return model(x)
     ```
  1. Selective: BitFit - Update only the bias parameters. fast but limited.
     ```python
     params = (p for n,p in model.named_parameters() if "bias" in n)
     optimizer = Optimizer(params)
     ```
  1. Reparametrization: LoRa - Low-rank decomposition. Efficient, Complex to implement.
     ```python
     def lora_linear(x):
       h = x @ W # regular linear
       h += x @ W_A @ W_B # low_rank update
       return scale * h
     ```

#### LoRA: Low-Rank Adaptation

- 5 Techniques of LoRA [✍️](https://blog.dailydoseofds.com/p/5-llm-fine-tuning-techniques-explained): LoRA, LoRA-FA, VeRA, Delta-LoRA, LoRA+ [May 2024]
- [DoRA📑](https://alphaxiv.org/abs/2402.09353): Weight-Decomposed Low-Rank Adaptation. Decomposes pre-trained weight into two components, magnitude and direction, for fine-tuning. [14 Feb 2024]
- [Fine-tuning a GPT - LoRA](https://dataman-ai.medium.com/fine-tune-a-gpt-lora-e9b72ad4ad3): Comprehensive guide for LoRA [🗄️](./files/Fine-tuning_a_GPT_LoRA.pdf) [20 Jun 2023]
- [LoRA: Low-Rank Adaptation of Large Language Models📑](https://alphaxiv.org/abs/2106.09685): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2106.09685)]: LoRA is one of PEFT technique. To represent the weight updates with two smaller matrices (called update matrices) through low-rank decomposition. [✨](https://github.com/microsoft/LoRA) [17 Jun 2021]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/LoRA?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LoRA learns less and forgets less📑](https://alphaxiv.org/abs/2405.09673): Compared to full training, LoRA has less learning but better retention of original knowledge. [15 May 2024]  
   <img src="./files/LoRA.png" alt="LoRA" width="390"/>
- [LoRA+📑](https://alphaxiv.org/abs/2402.12354): Improves LoRA’s performance and fine-tuning speed by setting different learning rates for the LoRA adapter matrices. [19 Feb 2024]
- [LoTR📑](https://alphaxiv.org/abs/2402.01376): Tensor decomposition for gradient update. [2 Feb 2024]
- LoRA Family [✍️](https://towardsdatascience.com/an-overview-of-the-lora-family-515d81134725) [11 Mar 2024]
    - `LoRA` introduces low-rank matrices A and B that are trained, while the pre-trained weight matrix W is frozen.
    - `LoRA+` suggests having a much higher learning rate for B than for A.
    - `VeRA` does not train A and B, but initializes them randomly and trains new vectors d and b on top.
    - `LoRA-FA` only trains matrix B.
    - `LoRA-drop` uses the output of B*A to determine, which layers are worth to be trained at all.
    - `AdaLoRA` adapts the ranks of A and B in different layers dynamically, allowing for a higher rank in these layers, where more contribution to the model’s performance is expected.
    - `DoRA` splits the LoRA adapter into two components of magnitude and direction and allows to train them more independently.
    - `Delta-LoRA` changes the weights of W by the gradient of A*B.
- [Practical Tips for Finetuning LLMs Using LoRA (Low-Rank Adaptation)✍️✍️](https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms) [19 Nov 2023]: Best practical guide of LoRA.
  1. QLoRA saves 33% memory but increases runtime by 39%, useful if GPU memory is a constraint.
  1. Optimizer choice for LLM finetuning isn’t crucial. Adam optimizer’s memory-intensity doesn’t significantly impact LLM’s peak memory.
  1. Apply LoRA across all layers for maximum performance.
  1. Adjusting the LoRA rank is essential.
  1. Multi-epoch training on static datasets may lead to overfitting and deteriorate results.
- [QLoRA: Efficient Finetuning of Quantized LLMs📑](https://alphaxiv.org/abs/2305.14314): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.14314)]: 4-bit quantized pre-trained language model into Low Rank Adapters (LoRA). [✨](https://github.com/artidoro/qlora) [23 May 2023]
 ![**github stars**](https://img.shields.io/github/stars/artidoro/qlora?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [The Expressive Power of Low-Rank Adaptation📑](https://alphaxiv.org/abs/2310.17513): Theoretically analyzes the expressive power of LoRA. [26 Oct 2023]
- [Training language models to follow instructions with human feedback📑](https://alphaxiv.org/abs/2203.02155): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2203.02155)] [4 Mar 2022]

### **RLHF (Reinforcement Learning from Human Feedback) & SFT (Supervised Fine-Tuning)**

- [A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More📑](https://alphaxiv.org/abs/2407.16216) [23 Jul 2024]
- [Absolute Zero: Reinforced Self-play Reasoning with Zero Data📑](https://alphaxiv.org/abs/2505.03335): Autonomous AI systems capable of self-improvement without human-curated data, using interpreter feedback for code generation and math problem solving. [6 May 2025]
- [Direct Preference Optimization (DPO)📑](https://alphaxiv.org/abs/2305.18290): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.18290)]: 1. RLHF can be complex because it requires fitting a reward model and performing significant hyperparameter tuning. On the other hand, DPO directly solves a classification problem on human preference data in just one stage of policy training. DPO more stable, efficient, and computationally lighter than RLHF. 2. `Your Language Model Is Secretly a Reward Model`  [29 May 2023]
  - Direct Preference Optimization (DPO) uses two models: a trained model (or policy model) and a reference model (copy of trained model). The goal is to have the trained model output higher probabilities for preferred answers and lower probabilities for rejected answers compared to the reference model.  [✍️](https://towardsdatascience.com/fine-tune-a-mistral-7b-model-with-direct-preference-optimization-708042745aac): RHLF vs DPO [Jan 2, 2024] / [✍️](https://pakhapoomsarapat.medium.com/forget-rlhf-because-dpo-is-what-you-actually-need-f10ce82c9b95) [1 Jul 2023]
- [InstructGPT: Training language models to follow instructions with human feedback📑](https://alphaxiv.org/abs/2203.02155): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2203.02155)] is a model trained by OpenAI to follow instructions using human feedback. [4 Mar 2022]  
  <img src="./files/rhlf.png" width="400" />  
  <img src="./files/rhlf2.png" width="400" />  
  [🗣️](https://docs.argilla.io/)
- Libraries: [TRL🤗](https://huggingface.co/docs/trl/index): from the Supervised Fine-tuning step (SFT), Reward Modeling step (RM) to the Proximal Policy Optimization (PPO) step, [trlX✨](https://github.com/CarperAI/trlx), [Argilla](https://docs.argilla.io/en/latest/tutorials/libraries/colab.html) ![**github stars**](https://img.shields.io/github/stars/CarperAI/trlx?style=flat-square&label=%20&color=blue&cacheSeconds=36000)  
  <img src="./files/TRL-readme.png" width="500" />  
  <img src="./files/chip.jpg" width="400" />  
  - The three steps in the process: 1. pre-training on large web-scale data, 2. supervised fine-tuning on instruction data (instruction tuning), and 3. RLHF. [✍️](https://aman.ai/primers/ai/RLHF/)
- Machine learning technique that trains a "reward model" directly from human feedback and uses the model as a reward function to optimize an agent's policy using reinforcement learning.
- OpenAI Spinning Up in Deep RL!: An educational resource to help anyone learn deep reinforcement learning. [✨](https://github.com/openai/spinningup) [Nov 2018] ![**github stars**](https://img.shields.io/github/stars/openai/spinningup?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [ORPO (odds ratio preference optimization)📑](https://alphaxiv.org/abs/2403.07691): Monolithic Preference Optimization without Reference Model. New method that `combines supervised fine-tuning and preference alignment into one process` [✨](https://github.com/xfactlab/orpo) [12 Mar 2024] [Fine-tune Llama 3 with ORPO✍️](https://towardsdatascience.com/fine-tune-llama-3-with-orpo-56cfab2f9ada) [Apr 2024]  
 ![**github stars**](https://img.shields.io/github/stars/xfactlab/orpo?style=flat-square&label=%20&color=blue&cacheSeconds=36000)  
  <img src="./files/orpo.png" width="400" />  
- Preference optimization techniques: [✍️](https://x.com/helloiamleonie/status/1823305448650383741) [13 Aug 2024]
  - `RLHF (Reinforcement Learning from Human Feedback)`: Optimizes reward policy via objective function.
  - `DPO (Direct preference optimization)`: removes the need for a reward model. > Minimizes loss; no reward policy.
  - `IPO (Identity Preference Optimization)` : A change in the objective, which is simpler and less prone to overfitting.
  - `KTO (Kahneman-Tversky Optimization)` : Scales more data by replacing the pairs of accepted and rejected generations with a binary label.
  - `ORPO (Odds Ratio Preference Optimization)` : Combines instruction tuning and preference optimization into one training process, which is cheaper and faster.
  - `TPO (Thought Preference Optimization)`: This method generates thoughts before the final response, which are then evaluated by a Judge model for preference using Direct Preference Optimization (DPO). [14 Oct 2024]
- [Reinforcement Learning from AI Feedback (RLAF)📑](https://alphaxiv.org/abs/2309.00267): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.00267)]: Uses AI feedback to generate instructions for the model. TLDR: CoT (Chain-of-Thought, Improved), Few-shot (Not improved). Only explores the task of summarization. After training on a few thousand examples, performance is close to training on the full dataset. RLAIF vs RLHF: In many cases, the two policies produced similar summaries. [1 Sep 2023]
- [Reinforcement Learning from Human Feedback (RLHF)📑](https://alphaxiv.org/abs/1909.08593)) is a process of pretraining and retraining a language model using human feedback to develop a scoring algorithm that can be reapplied at scale for future training and refinement. As the algorithm is refined to match the human-provided grading, direct human feedback is no longer needed, and the language model continues learning and improving using algorithmic grading alone. [18 Sep 2019] [🤗](https://huggingface.co/blog/rlhf) [9 Dec 2022]
  - `Proximal Policy Optimization (PPO)` is a reinforcement learning method using first-order optimization. It modifies the objective function to penalize large policy changes, specifically those that move the probability ratio away from 1. Aiming for TRPO (Trust Region Policy Optimization)-level performance without its complexity which requires second-order optimization.
- [SFT vs RL📑](https://alphaxiv.org/abs/2501.17161): SFT Memorizes, RL Generalizes. RL enhances generalization across text and vision, while SFT tends to memorize and overfit. [✨](https://github.com/LeslieTrue/SFTvsRL) [28 Jan 2025]
- `Supervised Fine-Tuning (SFT)` fine-tuning a pre-trained model on a specific task or domain using labeled data. This can cause more significant shifts in the model’s behavior compared to RLHF. <br/>
  <img src="./files/rlhf-dpo.png" width="400" />  
- [Supervised Reinforcement Learning (SRL)📑](https://arxiv.org/abs/2510.25992): **The Problem**: SFT imitates human actions token by token, leading to overfitting; RLVR gives rewards only when successful, with no signal when all attempts fail. **This Approach**: Each action during RL generates a short reasoning trace and receives a similarity reward at every step. [29 Oct 2025]
- [Train your own R1 reasoning model with Unsloth (GRPO)](https://unsloth.ai/blog/r1-reasoning): Unsloth x vLLM > 20x more throughput, 50% VRAM savings. [6 Feb 2025]

#### **Model Compression for Large Language Models**

- A Survey on Model Compression for Large Language Models [ref📑](https://alphaxiv.org/abs/2308.07633) [15 Aug 2023]

#### **Quantization Techniques**

- bitsandbytes: 8-bit optimizers [✨](https://github.com/TimDettmers/bitsandbytes) [Oct 2021]
 ![**github stars**](https://img.shields.io/github/stars/TimDettmers/bitsandbytes?style=flat-square&label=%20&color=blue&cacheSeconds=36000)  
- [The Era of 1-bit LLMs📑](https://alphaxiv.org/abs/2402.17764): All Large Language Models are in 1.58 Bits. BitNet b1.58, in which every single parameter (or weight) of the LLM is ternary {-1, 0, 1}. [27 Feb 2024]  
- Quantization-aware training (QAT): The model is further trained with quantization in mind after being initially trained in floating-point precision.
- Post-training quantization (PTQ): The model is quantized after it has been trained without further optimization during the quantization process.
  | Method                      | Pros                                                        | Cons                                                                                 |
  | --------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------ |
  | Post-training quantization  | Easy to use, no need to retrain the model                   | May result in accuracy loss                                                          |
  | Quantization-aware training | Can achieve higher accuracy than post-training quantization | Requires retraining the model, can be more complex to implement                      |

#### **Pruning and Sparsification**

- Pruning: The process of removing some of the neurons or layers from a neural network. This can be done by identifying and eliminating neurons or layers that have little or no impact on the network's output.
- Sparsification: A technique used to reduce the size of large language models by removing redundant parameters.
- [Wanda Pruning📑](https://alphaxiv.org/abs/2306.11695): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2306.11695)]: A Simple and Effective Pruning Approach for Large Language Models [20 Jun 2023] [✍️](https://www.linkedin.com/pulse/efficient-model-pruning-large-language-models-wandas-ayoub-kirouane)

#### **Knowledge Distillation: Reducing Model Size with Textbooks**

- Distilled Supervised Fine-Tuning (dSFT)
  1. [Zephyr 7B📑](https://alphaxiv.org/abs/2310.16944): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.16944)] Zephyr-7B-β is the second model in the series, and is a fine-tuned version of mistralai/Mistral-7B-v0.1 that was trained on on a mix of publicly available, synthetic datasets using Direct Preference Optimization (DPO). [🤗](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) [25 Oct 2023]
  2. [Mistral 7B📑](https://alphaxiv.org/abs/2310.06825): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.06825)]: Outperforms Llama 2 13B on all benchmarks. Uses Grouped-query attention (GQA) for faster inference. Uses Sliding Window Attention (SWA) to handle longer sequences at smaller cost. [✍️](https://mistral.ai/news/announcing-mistral-7b/) [10 Oct 2023]
- phi-series: [🔗](#large-language-model-collection): Textbooks Are All You Need.
- [Orca 2📑](https://alphaxiv.org/abs/2311.11045): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2311.11045)]: Orca learns from rich signals from GPT 4 including explanation traces; step-by-step thought processes; and other complex instructions, guided by teacher assistance from ChatGPT. [✍️](https://www.microsoft.com/en-us/research/blog/orca-2-teaching-small-language-models-how-to-reason/) [18 Nov 2023]

#### **Memory Optimization**

- [CPU vs GPU vs TPU](https://newsletter.theaiedge.io/p/how-to-scale-model-training): The threads are grouped into thread blocks. Each of the thread blocks has access to a fast shared memory (SRAM). All the thread blocks can also share a large global memory. High-bandwidth memories (HBM). `HBM Bandwidth: 1.5-2.0TB/s vs SRAM Bandwidth: 19TB/s ~ 10x HBM` [27 May 2024]
- [Flash Attention📑](https://alphaxiv.org/abs/2205.14135): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2205.14135)] [27 May 2022]
  - In a GPU, A thread is the smallest execution unit, and a group of threads forms a block.
  - A block executes the same kernel (function, to simplify), with threads sharing fast SRAM memory.
  - All blocks can access the shared global HBM memory.
  - First, the query (Q) and key (K) product is computed in threads and returned to HBM. Then, it's redistributed for softmax and returned to HBM.
  - Flash attention reduces these movements by caching results in SRAM.
  - `Tiling` splits attention computation into memory-efficient blocks, while `recomputation` saves memory by recalculating intermediates during backprop. [📺](https://www.youtube.com/live/gMOAud7hZg4?si=dx637BQV-4Duu3uY)
  - [FlashAttention-2📑](https://alphaxiv.org/abs/2307.08691): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.08691)] [17 Jul 2023]: An method that reorders the attention computation and leverages classical techniques (tiling, recomputation). Instead of storing each intermediate result, use kernel fusion and run every operation in a single kernel in order to avoid memory read/write overhead. [✨](https://github.com/Dao-AILab/flash-attention) -> Compared to a standard attention implementation in PyTorch, FlashAttention-2 can be up to 9x faster
 ![**github stars**](https://img.shields.io/github/stars/Dao-AILab/flash-attention?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - [FlashAttention-3📑](https://alphaxiv.org/abs/2407.08608) [11 Jul 2024]
- [PagedAttention📑](https://alphaxiv.org/abs/2309.06180) : vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention, 24x Faster LLM Inference [🗄️](./files/vLLM_pagedattention.pdf). [✍️](https://vllm.ai/): vllm [12 Sep 2023]  
  <img src="./files/pagedattn.png" width="390">  
  - PagedAttention for a prompt “the cat is sleeping in the kitchen and the dog is”. Key-Value pairs of tensors for attention computation are stored in virtual contiguous blocks mapped to non-contiguous blocks in the GPU memory.
  - Transformer cache key-value tensors of context tokens into GPU memory to facilitate fast generation of the next token. However, these caches occupy significant GPU memory. The unpredictable nature of cache size, due to the variability in the length of each request, exacerbates the issue, resulting in significant memory fragmentation in the absence of a suitable memory management mechanism.
  - To alleviate this issue, PagedAttention was proposed to store the KV cache in non-contiguous memory spaces. It partitions the KV cache of each sequence into multiple blocks, with each block containing the keys and values for a fixed number of tokens.
- [TokenAttention✨](https://github.com/ModelTC/lightllm) an attention mechanism that manages key and value caching at the token level. [✨](https://github.com/ModelTC/lightllm/blob/main/docs/TokenAttention.md) [Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/ModelTC/lightllm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **Other techniques and LLM patterns**

- [Better & Faster Large Language Models via Multi-token Prediction📑](https://alphaxiv.org/abs/2404.19737): Suggest that training language models to predict multiple future tokens at once [30 Apr 2024]
- [Differential Transformer📑](https://alphaxiv.org/abs/2410.05258): Amplifies attention to the relevant context while minimizing noise using two separate softmax attention mechanisms. [7 Oct 2024]
- [KAN or MLP: A Fairer Comparison📑](https://alphaxiv.org/abs/2407.16674): In machine learning, computer vision, audio processing, natural language processing, and symbolic formula representation (except for symbolic formula representation tasks), MLP generally outperforms KAN. [23 Jul 2024]
- [Kolmogorov-Arnold Networks (KANs)📑](https://alphaxiv.org/abs/2404.19756): KANs use activation functions on connections instead of nodes like Multi-Layer Perceptrons (MLPs) do. Each weight in KANs is replaced by a learnable 1D spline function. KANs’ nodes simply sum incoming signals without applying any non-linearities. [✨](https://github.com/KindXiaoming/pykan) [30 Apr 2024] / [✍️](https://www.dailydoseofds.com/a-beginner-friendly-introduction-to-kolmogorov-arnold-networks-kan/): A Beginner-friendly Introduction to Kolmogorov Arnold Networks (KAN) [19 May 2024]
 ![**github stars**](https://img.shields.io/github/stars/KindXiaoming/pykan?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Large Concept Models📑](https://alphaxiv.org/abs/2412.08821): Focusing on high-level sentence (concept) level rather than tokens. using SONAR for sentence embedding space. [11 Dec 2024]
- [Large Language Diffusion Models📑](https://alphaxiv.org/abs/2502.09992): LLaDA's core is a mask predictor, which uses controlled noise to help models learn to predict missing information from context. [✍️](https://ml-gsai.github.io/LLaDA-demo/) [14 Feb 2025]
- [Large Transformer Model Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/): Besides the increasing size of SoTA models, there are two main factors contributing to the inference challenge ... [10 Jan 2023]
- [Lamini Memory Tuning✨](https://github.com/lamini-ai/Lamini-Memory-Tuning): Mixture of Millions of Memory Experts (MoME). 95% LLM Accuracy, 10x Fewer Hallucinations. [✍️](https://www.lamini.ai/blog/lamini-memory-tuning) [Jun 2024]
 ![**github stars**](https://img.shields.io/github/stars/lamini-ai/Lamini-Memory-Tuning?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Less is More: Recursive Reasoning with Tiny Networks📑](https://alphaxiv.org/abs/2510.04871): Tiny neural networks can perform complex recursive reasoning efficiently, achieving strong results with minimal model size. [6 Oct 2025] [✨](https://github.com/SamsungSAILMontreal/TinyRecursiveModels) ![**github stars**](https://img.shields.io/github/stars/SamsungSAILMontreal/TinyRecursiveModels?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLM patterns](https://eugeneyan.com/writing/llm-patterns/): 🏆From data to user, from defensive to offensive [🗄️](./files/llm-patterns-og.png)
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces📑](https://alphaxiv.org/abs/2312.00752) [1 Dec 2023] [✨](https://github.com/state-spaces/mamba): 1. Structured State Space (S4) - Class of sequence models, encompassing traits from RNNs, CNNs, and classical state space models. 2. Hardware-aware (Optimized for GPU) 3. Integrating selective SSMs and eliminating attention and MLP blocks [✍️](https://www.unite.ai/mamba-redefining-sequence-modeling-and-outforming-transformers-architecture/) / A Visual Guide to Mamba and State Space Models [✍️](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state) [19 FEB 2024]
 ![**github stars**](https://img.shields.io/github/stars/state-spaces/mamba?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - [Mamba-2📑](https://alphaxiv.org/abs/2405.21060): 2-8X faster [31 May 2024]
- [Mixture-of-Depths📑](https://alphaxiv.org/abs/2404.02258): All tokens should not require the same effort to compute. The idea is to make token passage through a block optional. Each block selects the top-k tokens for processing, and the rest skip it. [✍️](https://www.linkedin.com/embed/feed/update/urn:li:share:7181996416213372930) [2 Apr 2024]
- [Mixture of experts models](https://mistral.ai/news/mixtral-of-experts/): Mixtral 8x7B: Sparse mixture of experts models (SMoE) [magnet](https://x.com/MistralAI/status/1706877320844509405?s=20) [Dec 2023]
  - [Huggingface Mixture of Experts Explained🤗](https://huggingface.co/blog/moe): Mixture of Experts, or MoEs for short [Dec 2023]
  - [A Visual Guide to Mixture of Experts (MoE)](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts) [08 Oct 2024]
  - [makeMoE✨](https://github.com/AviSoori1x/makeMoE): From scratch implementation of a sparse mixture of experts ![**github stars**](https://img.shields.io/github/stars/AviSoori1x/makeMoE?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [Jan 2024]
  - [The Sparsely-Gated Mixture-of-Experts Layer📑](https://alphaxiv.org/abs/1701.06538): Introduced sparse expert gating to scale models efficiently without increasing compute cost. [23 Jan 2017]
  - [Switch Transformers📑](https://alphaxiv.org/abs/2101.03961): Used a single expert per token to simplify routing, enabling fast, scalable transformer models. `expert capacity = (total tokens / num experts) * capacity factor` [11 Jan 2021]
  - [ST-MoE (Stable Transformer MoE)📑](https://alphaxiv.org/abs/2202.08906): By stabilizing the training process, ST-MoE enables more reliable and scalable deep MoE architectures. `z-loss aims to regularize the logits z before passing into the softmax` [17 Feb 2022]
- [Model merging✍️](https://towardsdatascience.com/merge-large-language-models-with-mergekit-2118fb392b54): : A technique that combines two or more large language models (LLMs) into a single model, using methods such as SLERP, TIES, DARE, and passthrough. [Jan 2024] [✨](https://github.com/cg123/mergekit): mergekit
 ![**github stars**](https://img.shields.io/github/stars/cg123/mergekit?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  | Method | Pros | Cons |
  | --- | --- | --- |
  | SLERP | Preserves geometric properties, popular method | Can only merge two models, may decrease magnitude |
  | TIES | Can merge multiple models, eliminates redundant parameters | Requires a base model, may discard useful parameters |
  | DARE | Reduces overfitting, keeps expectations unchanged | May introduce noise, may not work well with large differences |
- [RouteLLM✨](https://github.com/lm-sys/RouteLLM): a framework for serving and evaluating LLM routers. [Jun 2024]
 ![**github stars**](https://img.shields.io/github/stars/lm-sys/RouteLLM?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Sakana.ai: Evolutionary Optimization of Model Merging Recipes.📑](https://alphaxiv.org/abs/2403.13187): A Method to Combine 500,000 OSS Models. [✨](https://github.com/SakanaAI/evolutionary-model-merge) [19 Mar 2024]
 ![**github stars**](https://img.shields.io/github/stars/SakanaAI/evolutionary-model-merge?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Scaling Synthetic Data Creation with 1,000,000,000 Personas📑](https://alphaxiv.org/abs/2406.20094) A persona-driven data synthesis methodology using Text-to-Persona and Persona-to-Persona. [28 Jun 2024]
- [Simplifying Transformer Blocks📑](https://alphaxiv.org/abs/2311.01906): Simplifie Transformer. Removed several block components, including skip connections, projection/value matrices, sequential sub-blocks and normalisation layers without loss of training speed. [3 Nov 2023]
- [Text-to-LoRA (T2L)](https://github.com/SakanaAI/text-to-lora): Converts text prompts into LoRA models, enabling lightweight fine-tuning of AI models for custom tasks. ![**github stars**](https://img.shields.io/github/stars/SakanaAI/text-to-lora?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [01 May 2025]
- [What We’ve Learned From A Year of Building with LLMs](https://applied-llms.org/):💡A practical guide to building successful LLM products, covering the tactical, operational, and strategic.  [8 June 2024]


## **Large Language Model: Challenges and Solutions**

### AGI Discussion and Social Impact

- AGI: Artificial General Intelligence
- [AI 2027🗣️](https://ai-2027.com/summary): a speculative scenario, "AI 2027," created by the AI Futures Project. It predicts the rapid evolution of AI, culminating in the emergence of artificial superintelligence (ASI) by 2027. [3 Apr 2025]
- Anthropic's CEO, Dario Amodei, predicts AGI between 2026 and 2027. [✍️](https://techcrunch.com/2024/11/13/this-week-in-ai-anthropics-ceo-talks-scaling-up-ai-and-google-predicts-floods/) [13 Nov 2024]
- Artificial General Intelligence Society: a central hub for AGI research, publications, and conference details. [✍️](https://agi-society.org/resources/)
- [Artificial General Intelligence: Concept, State of the Art, and Future Prospects📑](https://www.researchgate.net/publication/271390398_Artificial_General_Intelligence_Concept_State_of_the_Art_and_Future_Prospects) [Jan 2014]
- [Creating Scalable AGI: the Open General Intelligence Framework📑](https://alphaxiv.org/abs/2411.15832): a new AI architecture designed to enhance flexibility and scalability by dynamically managing specialized AI modules. [24 Nov 2024]
- [How Far Are We From AGI📑](https://alphaxiv.org/abs/2405.10313): A survey discussing AGI's goals, developmental trajectory, and alignment technologies, providing a roadmap for AGI realization. [16 May 2024]
- [Investigating Affective Use and Emotional Well-being on ChatGPT✍️](https://www.media.mit.edu/publications/investigating-affective-use-and-emotional-well-being-on-chatgpt/): The MIT study found that higher ChatGPT usage correlated with increased loneliness, dependence, and lower socialization. [21 Mar 2025]
- [Key figures and their predicted AGI timelines🗣️](https://x.com/slow_developer/status/1858877008375152805):💡AGI might be emerging between 2025 to 2030. [19 Nov 2024]
- [Levels of AGI for Operationalizing Progress on the Path to AGI📑](https://alphaxiv.org/abs/2311.02462): Provides a comprehensive discussion on AGI's progress and proposes metrics and benchmarks for assessing AGI systems. [4 Nov 2023]
- [Linus Torvalds: 90% of AI marketing is hype🗣️](https://www.theregister.com/2024/10/29/linus_torvalds_ai_hype):💡AI is 90% marketing, 10% reality [29 Oct 2024]
- Machine Intelligence Research Institute (MIRI): a leading organization in AGI safety and alignment, focusing on theoretical work to ensure safe AI development. [✍️](https://intelligence.org)
- [One Small Step for Generative AI, One Giant Leap for AGI: A Complete Survey on ChatGPT in AIGC Era📑](https://alphaxiv.org/abs/2304.06488) [4 Apr 2023]
- OpenAI's CEO, Sam Altman, predicts AGI could emerge by 2025. [✍️](https://blog.cubed.run/agi-by-2025-altmans-bold-prediction-on-ai-s-future-9f15b071762c) [9 Nov 2024]
- [OpenAI: Planning for AGI and beyond✍️](https://openai.com/index/planning-for-agi-and-beyond/) [24 Feb 2023]
- [Shaping AI's Impact on Billions of Lives📑](https://alphaxiv.org/abs/2412.02730): a framework for assessing AI's potential effects and responsibilities, 18 milestones and 5 guiding principles for responsible AI [3 Dec 2024]
- [Sparks of Artificial General Intelligence: Early experiments with GPT-4📑](https://alphaxiv.org/abs/2303.12712): [22 Mar 2023]
- [The General Theory of General Intelligence: A Pragmatic Patternist Perspective📑](https://alphaxiv.org/abs/2103.15100): a patternist philosophy of mind, arguing for a formal theory of general intelligence based on patterns and complexity. [28 Mar 2021]
- [The Impact of Generative AI on Critical Thinking✍️](https://www.microsoft.com/en-us/research/publication/the-impact-of-generative-ai-on-critical-thinking-self-reported-reductions-in-cognitive-effort-and-confidence-effects-from-a-survey-of-knowledge-workers): A survey of 319 knowledge workers shows that higher confidence in Generative AI (GenAI) tools can reduce critical thinking. [Apr 2025]
- [There is no Artificial General Intelligence📑](https://alphaxiv.org/abs/1906.05833): A critical perspective arguing that human-like conversational intelligence cannot be mathematically modeled or replicated by current AGI theories. [9 Jun 2019]
- [Thousands of AI Authors on the Future of AI📑](https://alphaxiv.org/abs/2401.02843): A survey of 2,778 AI researchers predicts a 50 % likelihood of machines achieving multiple human-level capabilities by 2028, with wide disagreement about long-term risks and timelines. [5 Jan 2024]
- [Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise📑](https://alphaxiv.org/abs/2410.03017): Tutor CoPilot can scale real-time expertise in education, enhancing outcomes even with less experienced tutors. It is cost-effective, priced at $20 per tutor annually. [3 Oct 2024]
- [We must build AI for people; not to be a person🗣️](https://mustafa-suleyman.ai/seemingly-conscious-ai-is-coming) [19 August 2025]
- LessWrong & Alignment Forum: Extensive discussions on AGI alignment, with contributions from experts in AGI safety. [LessWrong✍️](https://www.lesswrong.com/) | [Alignment Forum✍️](https://www.alignmentforum.org/)

### **OpenAI's Roadmap and Products**

#### **OpenAI's roadmap**

- [AMA (ask me anything) with OpenAI on Reddit🗣️](https://www.reddit.com/r/ChatGPT/comments/1ggixzy/ama_with_openais_sam_altman_kevin_weil_srinivas/) [1 Nov 2024]
- [Humanloop Interview 2023🗣️](https://web.archive.org/web/20230531203946/https://humanloop.com/blog/openai-plans) : [🗄️](./files/openai-plans.pdf) [29 May 2023]
- Model Spec: Desired behavior for the models in the OpenAI API and ChatGPT [✍️](https://cdn.openai.com/spec/model-spec-2024-05-08.html) [8 May 2024] [✍️](https://twitter.com/yi_ding/status/1788281765637038294): takeaway
- [o3/o4-mini/GPT-5🗣️](https://x.com/sama/status/1908167621624856998): `we are going to release o3 and o4-mini after all, probably in a couple of weeks, and then do GPT-5 in a few months.` [4 Apr 2025]
- OpenAI’s CEO Says the Age of Giant AI Models Is Already Over [✍️](https://www.wired.com/story/openai-ceo-sam-altman-the-age-of-giant-ai-models-is-already-over/) [17 Apr 2023]
- Q* (pronounced as Q-Star): The model, called Q* was able to solve basic maths problems it had not seen before, according to the tech news site the Information. [✍️](https://www.theguardian.com/business/2023/nov/23/openai-was-working-on-advanced-model-so-powerful-it-alarmed-staff) [23 Nov 2023]
- [Reflections on OpenAI🗣️](https://calv.info/openai-reflections): OpenAI culture. Bottoms-up decision-making. Progress is iterative, not driven by a rigid roadmap. Direction changes quickly based on new information. Slack is the primary communication tool. [16 Jul 2025]
- Sam Altman reveals in an interview with Bill Gates (2 days ago) what's coming up in GPT-4.5 (or GPT-5): Potential integration with other modes of information beyond text, better logic and analysis capabilities, and consistency in performance over the next two years. [✍️](https://x.com/IntuitMachine/status/1746278269165404164?s=20) [12 Jan 2024]
<!-- - Sam Altman Interview with Lex Fridman: [✍️](https://lexfridman.com/sam-altman-2-transcript) [19 Mar 2024] -->
- [The Timeline of the OpenaAI's Founder Journeys✍️](https://www.coffeespace.com/blog-post/openai-founders-journey-a-transformer-company-transformed) [15 Oct 2024]

#### **OpenAI Products**

- [Agents SDK & Response API✍️](https://openai.com/index/new-tools-for-building-agents/): Responses API (Chat Completions + Assistants API), Built-in tools (web search, file search, computer use), Agents SDK for multi-agent workflows, agent workflow observability tools [11 Mar 2025] [✨](https://github.com/openai/openai-agents-python)
- [Building ChatGPT Atlas✍️](https://openai.com/index/building-chatgpt-atlas/): OpenAI's approach to building Atlas. OWL: OpenAI’s Web Layer. Mojo Protocol. [Oct 2025]
- [ChatGPT agent✍️](https://openai.com/index/introducing-chatgpt-agent/): Web-browsing, File-editing, Terminal, Email, Spreadsheet, Calendar, API-calling, Automation, Task-chaining, Reasoning. [17 Jul 2025]
- [ChatGPT can now see, hear, and speak✍️](https://openai.com/blog/chatgpt-can-now-see-hear-and-speak): It has recently been updated to support multimodal capabilities, including voice and image. [25 Sep 2023] [Whisper✨](https://github.com/openai/whisper) / [CLIP✨](https://github.com/openai/Clip)
 ![**github stars**](https://img.shields.io/github/stars/openai/whisper?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/openai/Clip?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [ChatGPT Function calling](https://platform.openai.com/docs/guides/gpt/function-calling) [Jun 2023] > Azure OpenAI supports function calling. [✍️](https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/function-calling#using-function-in-the-chat-completions-api)
- [ChatGPT Memory✍️](https://openai.com/blog/memory-and-new-controls-for-chatgpt): Remembering things you discuss `across all chats` saves you from having to repeat information and makes future conversations more helpful. [Apr 2024]
- [ChatGPT Plugin✍️](https://openai.com/blog/chatgpt-plugins) [23 Mar 2023]
- [CriticGPT✍️](https://openai.com/index/finding-gpt4s-mistakes-with-gpt-4/): a version of GPT-4 fine-tuned to critique code generated by ChatGPT [27 Jun 2024]
- [Custom instructions✍️](https://openai.com/blog/custom-instructions-for-chatgpt): In a nutshell, the Custom Instructions feature is a cross-session memory that allows ChatGPT to retain key instructions across chat sessions. [20 Jul 2023]
- [DALL·E 3✍️](https://openai.com/dall-e-3) : In September 2023, OpenAI announced their latest image model, DALL-E 3 [✨](https://github.com/openai/dall-e) [Sep 2023]
 ![**github stars**](https://img.shields.io/github/stars/openai/dall-e?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [deep research✍️](https://openai.com/index/introducing-deep-research/): An agent that uses reasoning to synthesize large amounts of online information and complete multi-step research tasks [2 Feb 2025]
- [GPT-3.5 Turbo Fine-tuning✍️](https://openai.com/blog/gpt-3-5-turbo-fine-tuning-and-api-updates) Fine-tuning for GPT-3.5 Turbo is now available, with fine-tuning for GPT-4 coming this fall. [22 Aug 2023]
- [Introducing the GPT Store✍️](https://openai.com/blog/introducing-the-gpt-store): Roll out the GPT Store to ChatGPT Plus, Team and Enterprise users  [GPTs](https://chat.openai.com/gpts) [10 Jan 2024]
- [New embedding models✍️](https://openai.com/blog/new-embedding-models-and-api-updates) `text-embedding-3-small`: Embedding size: 512, 1536 `text-embedding-3-large`: Embedding size: 256,1024,3072 [25 Jan 2024]
- Open AI Enterprise: Removes GPT-4 usage caps, and performs up to two times faster [✍️](https://openai.com/blog/introducing-chatgpt-enterprise) [28 Aug 2023]
- [OpenAI DevDay 2023✍️](https://openai.com/blog/new-models-and-developer-products-announced-at-devday): GPT-4 Turbo with 128K context, Assistants API (Code interpreter, Retrieval, and function calling), GPTs (Custom versions of ChatGPT: [✍️](https://openai.com/blog/introducing-gpts)), Copyright Shield, Parallel Function Calling, JSON Mode, Reproducible outputs [6 Nov 2023]
- [OpenAI DevDay 2024✍️](https://openai.com/devday/): Real-time API (speech-to-speech), Vision Fine-Tuning, Prompt Caching, and Distillation (fine-tuning a small language model using a large language model). [✍️](https://community.openai.com/t/devday-2024-san-francisco-live-ish-news/963456) [1 Oct 2024]
- [OpenAI DevDay 2025✍️](https://openai.com/devday): ChatGPT Apps + SDK, AgentKit, GPT-5 Pro, Sora 2 video API, upgraded Codex [✍️](https://openai.com/index/announcing-devday-2025/) [6 Oct 2025]
- [Operator✍️](https://openai.com/index/introducing-operator/): GUI Agent. Operates embedded virtual environments. Specialized model (Computer-Using Agent). [23 Jan 2025]
- [SearchGPT✍️](https://openai.com/index/searchgpt-prototype/): AI search [25 Jul 2024] > [ChatGPT Search✍️](https://openai.com/index/introducing-chatgpt-search/) [31 Oct 2024]
- [Sora✍️](https://openai.com/sora) Text-to-video model. Sora can generate videos up to a minute long while maintaining visual quality and adherence to the user’s prompt. [15 Feb 2024]
- [Structured Outputs in the API✍️](https://openai.com/index/introducing-structured-outputs-in-the-api/): a new feature designed to ensure model-generated outputs will exactly match JSON Schemas provided by developers. [6 Aug 2024]

#### **GPT series release date**

- GPT 1: Decoder-only model. 117 million parameters. [Jun 2018] [✨](https://github.com/openai/finetune-transformer-lm)
 ![**github stars**](https://img.shields.io/github/stars/openai/finetune-transformer-lm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- GPT 2: Increased model size and parameters. 1.5 billion. [14 Feb 2019] [✨](https://github.com/openai/gpt-2)
 ![**github stars**](https://img.shields.io/github/stars/openai/gpt-2?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- GPT 3: Introduced few-shot learning. 175B. [11 Jun 2020] [✨](https://github.com/openai/gpt-3)
 ![**github stars**](https://img.shields.io/github/stars/openai/gpt-3?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- GPT 3.5: 3 variants each with 1.3B, 6B, and 175B parameters. [15 Mar 2022] Estimate the embedding size of OpenAI's gpt-3.5-turbo to be about 4,096
- ChatGPT: GPT-3 fine-tuned with RLHF. 20B or 175B. `unverified` [✍️](https://www.reddit.com/r/LocalLLaMA/comments/17lvquz/clearing_up_confusion_gpt_35turbo_may_not_be_20b/) [30 Nov 2022]
- GPT 4: Mixture of Experts (MoE). 8 models with 220 billion parameters each, for a total of about 1.76 trillion parameters. `unverified` [✍️](https://the-decoder.com/gpt-4-architecture-datasets-costs-and-more-leaked/) [14 Mar 2023]
- [GPT-4o✍️](https://openai.com/index/hello-gpt-4o/): o stands for Omni. 50% cheaper. 2x faster. Multimodal input and output capabilities (text, audio, vision). supports 50 languages. [13 May 2024] / [GPT-4o mini✍️](https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/): 15 cents per million input tokens, 60 cents per million output tokens, MMLU of 82%, and fast. [18 Jul 2024]
- [OpenAI o1](#openai-o-series) [12 Sep 2024]
- [o3-mini system card✍️](https://openai.com/index/o3-mini-system-card/): The first model to reach Medium risk on Model Autonomy. [31 Jan 2025]
- [GPT-4.5✍️](https://openai.com/index/introducing-gpt-4-5/): greater “EQ”. better unsupervised learning (world model accuracy and intuition). scalable training from smaller models. [✍️](https://cdn.openai.com/gpt-4-5-system-card.pdf)  [27 Feb 2025]
- [GPT-4o: 4o image generation✍️](https://openai.com/index/gpt-4o-image-generation-system-card-addendum/): create photorealistic output, replacing DALL·E 3 [25 Mar 2025]
- [GPT-4.1 family of models✍️](https://openai.com/index/gpt-4-1/): GPT‑4.1, GPT‑4.1 mini, and GPT‑4.1 nano can process up to 1 million tokens of context. enhanced coding abilities, improved instruction following. [14 Apr 2025]
- [gpt-image-1✍️](https://openai.com/index/image-generation-api/): Image generation model API with designing and editing [23 Apr 2025]
- [gpt-oss✨](https://github.com/openai/gpt-oss): **gpt-oss-120b** and **gpt-oss-20b** are two open-weight language models by OpenAI. [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/openai/gpt-oss?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [GPT-5✍️](https://openai.com/index/introducing-gpt-5/): Real-time router orchestrating multiple models. GPT‑5 is the new default in ChatGPT, replacing GPT‑4o, OpenAI o3, OpenAI o4-mini, GPT‑4.1, and GPT‑4.5.  [7 Aug 2025]
  1. [GPT-5 prompting guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide)
  2. [Frontend coding with GPT-5](https://cookbook.openai.com/examples/gpt-5/gpt-5_frontend)
  3. [GPT-5 New Params and Tools](https://cookbook.openai.com/examples/gpt-5/gpt-5_new_params_and_tools)

##### **OpenAI o series**

- [A new series of reasoning models✍️](https://openai.com/index/introducing-openai-o1-preview/): The complex reasoning-specialized model, OpenAI o1 series, excels in math, coding, and science, outperforming GPT-4o on key benchmarks. [12 Sep 2024] / [✨](https://github.com/hijkzzz/Awesome-LLM-Strawberry): Awesome LLM Strawberry (OpenAI o1)
 ![**github stars**](https://img.shields.io/github/stars/hijkzzz/Awesome-LLM-Strawberry?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [A Comparative Study on Reasoning Patterns of OpenAI's o1 Model📑](https://alphaxiv.org/abs/2410.13639): 6 types of o1 reasoning patterns (i.e., Systematic Analysis (SA), Method
Reuse (MR), Divide and Conquer (DC), Self-Refinement (SR), Context Identification (CI), and Emphasizing Constraints (EC)). `the most commonly used reasoning patterns in o1 are DC and SR` [17 Oct 2024]
- [OpenAI o1 system card✍️](https://openai.com/index/openai-o1-system-card/) [5 Dec 2024]
- [o3 preview✍️](https://openai.com/12-days/): 12 Days of OpenAI [20 Dec 2024]
- [o3/o4-mini✍️](https://openai.com/index/introducing-o3-and-o4-mini/) [16 Apr 2025]

##### **GPT-4 details leaked** `unverified`

- GPT-4V(ision) system card: [✍️](https://openai.com/research/gpt-4v-system-card) [25 Sep 2023] / [✍️](https://cdn.openai.com/papers/GPTV_System_Card.pdf)
- [The Dawn of LMMs📑](https://alphaxiv.org/abs/2309.17421): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.17421)]: Preliminary Explorations with GPT-4V(ision) [29 Sep 2023]
- GPT-4 details leaked
  - GPT-4 is a language model with approximately 1.8 trillion parameters across 120 layers, 10x larger than GPT-3. It uses a Mixture of Experts (MoE) model with 16 experts, each having about 111 billion parameters. Utilizing MoE allows for more efficient use of resources during inference, needing only about 280 billion parameters and 560 TFLOPs, compared to the 1.8 trillion parameters and 3,700 TFLOPs required for a purely dense model.
  - The model is trained on approximately 13 trillion tokens from various sources, including internet data, books, and research papers. To reduce training costs, OpenAI employs tensor and pipeline parallelism, and a large batch size of 60 million. The estimated training cost for GPT-4 is around $63 million. [✍️](https://www.reddit.com/r/LocalLLaMA/comments/14wbmio/gpt4_details_leaked) [Jul 2023]

### **Context constraints**

- [Context Rot: How Increasing Input Tokens Impacts LLM Performance✨](https://github.com/chroma-core/context-rot) [14 Jul 2025]
- [Giraffe📑](https://alphaxiv.org/abs/2308.10882): Adventures in Expanding Context Lengths in LLMs. A new truncation strategy for modifying the basis for the position encoding.  [✍️](https://blog.abacus.ai/blog/2023/08/22/giraffe-long-context-llms/) [2 Jan 2024]
- [Introducing 100K Context Windows✍️](https://www.anthropic.com/index/100k-context-windows): hundreds of pages, Around 75,000 words; [11 May 2023] [demo](https://youtu.be/2kFhloXz5_E) Anthropic Claude
- [Leave No Context Behind📑](https://alphaxiv.org/abs/2404.07143): Efficient `Infinite Context` Transformers with Infini-attention. The Infini-attention incorporates a compressive memory into the vanilla attention mechanism. Integrate attention from both local and global attention. [10 Apr 2024]
- [LLM Maybe LongLM📑](https://alphaxiv.org/abs/2401.01325): Self-Extend LLM Context Window Without Tuning. With only four lines of code modification, the proposed method can effortlessly extend existing LLMs' context window without any fine-tuning. [2 Jan 2024]
- [Lost in the Middle: How Language Models Use Long Contexts📑](https://alphaxiv.org/abs/2307.03172):💡[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.03172)] [6 Jul 2023]
  1. Best Performace when relevant information is at beginning
  2. Too many retrieved documents will harm performance
  3. Performacnce decreases with an increase in context
- [“Needle in a Haystack” Analysis](https://bito.ai/blog/claude-2-1-200k-context-window-benchmarks/) [21 Nov 2023]: Context Window Benchmarks; Claude 2.1 (200K Context Window) vs [GPT-4✨](https://github.com/gkamradt/LLMTest_NeedleInAHaystack); [Long context prompting for Claude 2.1✍️](https://www.anthropic.com/index/claude-2-1-prompting) `adding just one sentence, “Here is the most relevant sentence in the context:”, to the prompt resulted in near complete fidelity throughout Claude 2.1’s 200K context window.` [6 Dec 2023]
 ![**github stars**](https://img.shields.io/github/stars/gkamradt/LLMTest_NeedleInAHaystack?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Ring Attention📑](https://alphaxiv.org/abs/2310.01889): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.01889)]: 1. Ring Attention, which leverages blockwise computation of self-attention to distribute long sequences across multiple devices while overlapping the communication of key-value blocks with the computation of blockwise attention. 2. Ring Attention can reduce the memory requirements of Transformers, enabling us to train more than 500 times longer sequence than prior memory efficient state-of-the-arts and enables the training of sequences that exceed 100 million in length without making approximations to attention. 3. we propose an enhancement to the blockwise parallel transformers (BPT) framework. [✨](https://github.com/lhao499/llm_large_context) [3 Oct 2023]
 ![**github stars**](https://img.shields.io/github/stars/lhao499/llm_large_context?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Rotary Positional Embedding (RoPE)📑](https://alphaxiv.org/abs/2104.09864):💡[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2104.09864)] / [✍️](https://blog.eleuther.ai/rotary-embeddings/) / [🗄️](./files/RoPE.pdf) [20 Apr 2021]
  - How is this different from the sinusoidal embeddings used in "Attention is All You Need"?
    1. Sinusoidal embeddings apply to each coordinate individually, while rotary embeddings mix pairs of coordinates
    2. Sinusoidal embeddings add a `cos` or `sin` term, while rotary embeddings use a multiplicative factor.
    3. Rotary embeddings are applied to positional encoding to K and V, not to the input embeddings.
    - [ALiBi📑](https://alphaxiv.org/abs/2203.16634): Attention with Linear Biases. ALiBi applies a bias directly to the attention scores. [27 Aug 2021]
    - [NoPE: Transformer Language Models without Positional Encodings Still Learn Positional Information📑](https://alphaxiv.org/abs/2203.16634): No postion embedding. [30 Mar 2022]
- [Sparse Attention: Generating Long Sequences with Sparse Transformer📑](https://alphaxiv.org/abs/1904.10509):💡Sparse attention computes scores for a subset of pairs, selected via a fixed or learned sparsity pattern, reducing calculation costs. Strided attention: image, audio / Fixed attention:text [✍️](https://openai.com/index/sparse-transformer/) / [✨](https://github.com/openai/sparse_attention) [23 Apr 2019]
 ![**github stars**](https://img.shields.io/github/stars/openai/sparse_attention?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Structured Prompting: Scaling In-Context Learning to 1,000 Examples📑](https://alphaxiv.org/abs/2212.06713): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2212.06713)] [13 Dec 2022]
  1. Microsoft's Structured Prompting allows thousands of examples, by first concatenating examples into groups, then inputting each group into the LM. The hidden key and value vectors of the LM's attention modules are cached. Finally, when the user's unaltered input prompt is passed to the LM, the cached attention vectors are injected into the hidden layers of the LM.
  2. This approach wouldn't work with OpenAI's closed models. because this needs to access [keys] and [values] in the transformer interns, which they do not expose. You could implement yourself on OSS ones. [✍️](https://www.infoq.com/news/2023/02/microsoft-lmops-tools/) [07 Feb 2023]

### **Numbers LLM**

- [5 Approaches To Solve LLM Token Limits✍️](https://dholmes.co.uk/blog/5-approaches-to-solve-llm-token-limits/) : [🗄️](./files/token-limits-5-approaches.pdf) [2023]
- [Byte-Pair Encoding (BPE)📑](https://alphaxiv.org/abs/1508.07909): P.2015. The most widely used tokenization algorithm for text today. BPE adds an end token to words, splits them into characters, and merges frequent byte pairs iteratively until a stop criterion. The final tokens form the vocabulary for new data encoding and decoding. [31 Aug 2015] / [✍️](https://towardsdatascience.com/byte-pair-encoding-subword-based-tokenization-algorithm-77828a70bee0) [13 Aug 2021]
- [Numbers every LLM Developer should know✨](https://github.com/ray-project/llm-numbers) [18 May 2023] ![**github stars**](https://img.shields.io/github/stars/ray-project/llm-numbers?style=flat-square&label=%20&color=blue&cacheSeconds=36000)  
  <img src="./files/llm-numbers.png" height="360">
- [Open AI Tokenizer](https://platform.openai.com/tokenizer): GPT-3, Codex Token counting
- [tiktoken✨](https://github.com/openai/tiktoken): BPE tokeniser for use with OpenAI's models. Token counting. [✍️](https://tiktokenizer.vercel.app/):💡online app [Dec 2022]
 ![**github stars**](https://img.shields.io/github/stars/openai/tiktoken?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Tokencost✨](https://github.com/AgentOps-AI/tokencost): Token price estimates for 400+ LLMs [Dec 2023]
 ![**github stars**](https://img.shields.io/github/stars/AgentOps-AI/tokencost?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [What are tokens and how to count them?✍️](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them): OpenAI Articles

### **Trustworthy, Safe and Secure LLM**

- [20 AI Governance Papers📑](https://www.linkedin.com/posts/oliver-patel_12-papers-was-not-enough-to-do-the-field-activity-7282005401032613888-6Ck4?utm_source=li_share&utm_content=feedcontent&utm_medium=g_dt_web&utm_campaign=copy) [Jan 2025]
- [A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models📑](https://alphaxiv.org/abs/2401.01313): A compre
hensive survey of over thirty-two techniques developed to mitigate hallucination in LLMs [2 Jan 2024]
- [AI models collapse when trained on recursively generated data](https://www.nature.com/articles/s41586-024-07566-y): Model Collapse. We find that indiscriminate use of model-generated content in training causes irreversible defects in the resulting models, in which tails of the original content distribution disappear. [24 Jul 2024]
- [Alignment Faking✍️](https://www.anthropic.com/research/alignment-faking): LLMs may pretend to align with training objectives during monitored interactions but revert to original behaviors when unmonitored. [18 Dec 2024] | demo: [✍️](https://alignment.anthropic.com/2024/how-to-alignment-faking/) | [Alignment Science Blog](https://alignment.anthropic.com/)
- [An Approach to Technical AGI Safety and Security📑](https://alphaxiv.org/abs/2504.01849): Google DeepMind. We focus on technical solutions to `misuse` and `misalignment`, two of four key AI risks (the others being `mistakes` and `structural risks`). To prevent misuse, we limit access to dangerous capabilities through detection and security. For misalignment, we use two defenses: model-level alignment via training and oversight, and system-level controls like monitoring and access restrictions. [✍️](https://deepmind.google/discover/blog/taking-a-responsible-path-to-agi/) [2 Apr 2025]
- [Anthropic Many-shot jailbreaking✍️](https://www.anthropic.com/research/many-shot-jailbreaking): simple long-context attack, Bypassing safety guardrails by bombarding them with unsafe or harmful questions and answers. [3 Apr 2024]
- [Extracting Concepts from GPT-4✍️](https://openai.com/index/extracting-concepts-from-gpt-4/): Sparse Autoencoders identify key features, enhancing the interpretability of language models like GPT-4. They extract 16 million interpretable features using GPT-4's outputs as input for training. [6 Jun 2024]
- [FactTune📑](https://alphaxiv.org/abs/2311.08401): A procedure that enhances the factuality of LLMs without the need for human feedback. The process involves the fine-tuning of a separated LLM using methods such as DPO and RLAIF, guided by preferences generated by [FActScore✨](https://github.com/shmsw25/FActScore). [14 Nov 2023] `FActScore` works by breaking down a generation into a series of atomic facts and then computing the percentage of these atomic facts by a reliable knowledge source. ![**github stars**](https://img.shields.io/github/stars/shmsw25/FActScore?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Frontier Safety Framework](https://deepmind.google/discover/blog/introducing-the-frontier-safety-framework/): Google DeepMind, Frontier Safety Framework, a set of protocols designed to identify and mitigate potential harms from future AI systems. [17 May 2024]
- [Guardrails Hub](https://hub.guardrailsai.com): Guardrails for common LLM validation use cases
- [Hallucination Index](https://www.galileo.ai/hallucinationindex): w.r.t. RAG, Testing LLMs with short (≤5k), medium (5k–25k), and long (40k–100k) contexts to evaluate improved RAG performance　[Nov 2023]
- [Hallucination Leaderboard✨](https://github.com/vectara/hallucination-leaderboard/): Evaluate how often an LLM introduces hallucinations when summarizing a document. [Nov 2023]
- [Hallucinations📑](https://alphaxiv.org/abs/2311.05232): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2311.05232)]: A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions [9 Nov 2023]
- [Large Language Models Reflect the Ideology of their Creators📑](https://alphaxiv.org/abs/2410.18417): When prompted in Chinese, all LLMs favor pro-Chinese figures; Western LLMs similarly align more with Western values, even in English prompts. [24 Oct 2024]
- [LlamaFirewall✨](https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall): Scans and filters AI inputs to block prompt injections and malicious content. [29 Apr 2025]
- [LLMs Will Always Hallucinate, and We Need to Live With This📑](https://alphaxiv.org/abs/2409.05746):💡LLMs cannot completely eliminate hallucinations through architectural improvements, dataset enhancements, or fact-checking mechanisms due to fundamental mathematical and logical limitations. [9 Sep 2024]
- [Machine unlearning](https://en.m.wikipedia.org/wiki/Machine_unlearning): Machine unlearning: techniques to remove specific data from trained machine learning models.
- [Mapping the Mind of a Large Language Model](https://cdn.sanity.io/files/4zrzovbb/website/e2ae0c997653dfd8a7cf23d06f5f06fd84ccfd58.pdf): Anthrophic, A technique called "dictionary learning" can help understand model behavior by identifying which features respond to a particular input, thus providing insight into the model's "reasoning." [✍️](https://www.anthropic.com/research/mapping-mind-language-model) [21 May 2024]
- [NeMo Guardrails✨](https://github.com/NVIDIA/NeMo-Guardrails): Building Trustworthy, Safe and Secure LLM Conversational Systems [Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/NVIDIA/NeMo-Guardrails?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework/ai-rmf-development): NIST released the first complete version of the NIST AI RMF Playbook on March 30, 2023
- [OpenAI Weak-to-strong generalization📑](https://alphaxiv.org/abs/2312.09390):💡In the superalignment problem, humans must supervise models that are much smarter than them. The paper discusses supervising a GPT-4 or 3.5-level model using a GPT-2-level model. It finds that while strong models supervised by weak models can outperform the weak models, they still don’t perform as well as when supervised by ground truth. [✨](https://github.com/openai/weak-to-strong) [14 Dec 2023]
 ![**github stars**](https://img.shields.io/github/stars/openai/weak-to-strong?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Political biases of LLMs📑](https://alphaxiv.org/abs/2305.08283): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.08283)]: From Pretraining Data to Language Models to Downstream Tasks: Tracking the Trails of Political Biases Leading to Unfair NLP Models. [15 May 2023] <br/>
  <img src="./files/political-llm.png" width="450">
- Red Teaming: The term red teaming has historically described systematic adversarial attacks for testing security vulnerabilities. LLM red teamers should be a mix of people with diverse social and professional backgrounds, demographic groups, and interdisciplinary expertise that fits the deployment context of your AI system. [✍️](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/red-teaming)
- [The Foundation Model Transparency Index📑](https://alphaxiv.org/abs/2310.12941): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.12941)]: A comprehensive assessment of the transparency of foundation model developers [✍️](https://crfm.stanford.edu/fmti/) [19 Oct 2023]
- [The Instruction Hierarchy📑](https://alphaxiv.org/abs/2404.13208): Training LLMs to Prioritize Privileged Instructions. The OpenAI highlights the need for instruction privileges in LLMs to prevent attacks and proposes training models to conditionally follow lower-level instructions based on their alignment with higher-level instructions. [19 Apr 2024]
- [Tracing the thoughts of a large language model✍️](https://www.anthropic.com/research/tracing-thoughts-language-model):💡`Claude 3.5 Haiku` 1. `Universal Thought Processing (Multiple Languages)`: Shared concepts exist across languages and are then translated into the respective language.  2. `Advance Planning (Composing Poetry)`: Despite generating text word by word, it anticipates rhyming words in advance.  3. `Fabricated Reasoning (Math)`: Produces plausible-sounding arguments even when given an incorrect hint. [27 Mar 2025] 
- [Trustworthy LLMs📑](https://alphaxiv.org/abs/2308.05374): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2308.05374)]: Comprehensive overview for assessing LLM trustworthiness; Reliability, safety, fairness, resistance to misuse, explainability and reasoning, adherence to social norms, and robustness. [10 Aug 2023]
  <!-- <img src="./files/llm-trustworthiness.png" width="450"> -->

### **Large Language Model Is: Abilities**

- [A Categorical Archive of ChatGPT Failures📑](https://alphaxiv.org/abs/2302.03494): 11  categories of failures, including reasoning, factual errors, math, coding, and bias [✨](https://github.com/giuven95/chatgpt-failures) [6 Feb 2023]
- [A Survey on Employing Large Language Models for Text-to-SQL Tasks📑](https://alphaxiv.org/abs/2407.15186): a comprehensive overview of LLMs in text-to-SQL tasks [21 Jul 2024]
- [Can LLMs Generate Novel Research Ideas?📑](https://alphaxiv.org/abs/2409.04109): A Large-Scale Human Study with 100+ NLP Researchers. We find LLM-generated ideas are judged as more novel (p < 0.05) than human expert ideas. However, the study revealed a lack of diversity in AI-generated ideas. [6 Sep 2024]  
- [Design2Code📑](https://alphaxiv.org/abs/2403.03163): How Far Are We From Automating Front-End Engineering? `64% of cases GPT-4V
generated webpages are considered better than the original reference webpages` [5 Mar 2024]
- [Emergent Abilities of Large Language Models📑](https://alphaxiv.org/abs/2206.07682): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2206.07682)]: Large language models can develop emergent abilities, which are not explicitly trained but appear at scale and are not present in smaller models. . These abilities can be enhanced using few-shot and augmented prompting techniques. [✍️](https://www.jasonwei.net/blog/emergence) [15 Jun 2022]
- [Improving mathematical reasoning with process supervision✍️](https://openai.com/research/improving-mathematical-reasoning-with-process-supervision) [31 May 2023]
- [Language Modeling Is Compression📑](https://alphaxiv.org/abs/2309.10668): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.10668)]: Lossless data compression, while trained primarily on text, compresses ImageNet patches to 43.4% and LibriSpeech samples to 16.4% of their raw size, beating domain-specific compressors like PNG (58.5%) or FLAC (30.3%). [19 Sep 2023]
- [Large Language Models for Software Engineering📑](https://alphaxiv.org/abs/2310.03533): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.03533)]: Survey and Open Problems, Large Language Models (LLMs) for Software Engineering (SE) applications, such as code generation, testing, repair, and documentation. [5 Oct 2023]
- [LLMs for Chip Design📑](https://alphaxiv.org/abs/2311.00176): Domain-Adapted LLMs for Chip Design [31 Oct 2023]
- [LLMs Represent Space and Time📑](https://alphaxiv.org/abs/2310.02207): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.02207)]: Large language models learn world models of space and time from text-only training. [3 Oct 2023]
- Math soving optimized LLM [WizardMath📑](https://alphaxiv.org/abs/2308.09583): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2308.09583)]: Developed by adapting Evol-Instruct and Reinforcement Learning techniques, these models excel in math-related instructions like GSM8k and MATH. [✨](https://github.com/nlpxucan/WizardLM) [18 Aug 2023] / Math solving Plugin: [Wolfram alpha](https://www.wolfram.com/wolfram-plugin-chatgpt/)
 ![**github stars**](https://img.shields.io/github/stars/nlpxucan/WizardLM?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Multitask Prompted Training Enables Zero-Shot Task Generalization📑](https://alphaxiv.org/abs/2110.08207): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2110.08207)]: A language model trained on various tasks using prompts can learn and generalize to new tasks in a zero-shot manner. [15 Oct 2021]
- [Testing theory of mind in large language models and humans](https://www.nature.com/articles/s41562-024-01882-z): Some large language models (LLMs) perform as well as, and in some cases better than, humans when presented with tasks designed to test the ability to track people’s mental states, known as “theory of mind.” [🗣️](https://www.technologyreview.com/2024/05/20/1092681/ai-models-can-outperform-humans-in-tests-to-identify-mental-states) [20 May 2024]

### **Reasoning**

- Chain of Draft: Thinking Faster by Writing Less: [🔗](#prompt-engineering)
- [Comment on The Illusion of Thinking: Understanding the Strengths and Limitations of Reasoning Models via the Lens of Problem Complexity📑](https://alphaxiv.org/abs/2506.09250):💡The `Illusion of Thinking` findings primarily reflect experimental design limitations rather than fundamental reasoning failures. Output token limits, flawed evaluation methods, and unsolvable River Crossing problems. [10 Jun 2025]
- Deep research: [🔗](#deep-research)
- [DeepSeek-R1✨](https://github.com/deepseek-ai/DeepSeek-R1):💡Group Relative Policy Optimization (GRPO). Base -> RL -> SFT -> RL -> SFT -> RL [20 Jan 2025]
- [Illusion of Thinking📑](https://ml-site.cdn-apple.com/papers/the-illusion-of-thinking.pdf): Large Reasoning Models (LRMs) are evaluated using controlled puzzles, where complexity depends on the size of `N`. Beyond a certain complexity threshold, LRM accuracy collapses, and reasoning effort paradoxically decreases. LRMs outperform standard LLMs on medium-complexity tasks, perform worse on low-complexity ones, and both fail on high-complexity. Apple. [May 2025]
- [Inference-Time Computations for LLM Reasoning and Planning: A Benchmark and Insights📑](https://alphaxiv.org/abs/2502.12521): Evaluate Chain-of-Thought, Tree-of-Thought, and Reasoning as Planning across 11 tasks. While scaling inference-time computation enhances reasoning, no single technique consistently outperforms the others. [18 Feb 2025]
- [Is Chain-of-Thought Reasoning of LLMs a Mirage?📑](https://alphaxiv.org/abs/2508.01191): The paper concludes that CoT is largely a mimic rather than true reasoning. Using DataAlchemy—`atom` = A–Z; `element` = e.g., APPLE; `transform` = (1) ROT (rotation), (2) position shift; `compositional transform` = combinations of transforms—the model is fine-tuned and evaluated on its ability to generalize to unlearned patterns.
- [Mini-R1✍️](https://www.philschmid.de/mini-deepseek-r1): Reproduce Deepseek R1 „aha moment“ a RL tutorial [30 Jan 2025]
- Open R1: [🔗](#large-language-model-collection)
- Open Thoughts: [🔗](#datasets-for-llm-training)
- [Reasoning LLMs Guide](https://www.promptingguide.ai/guides/reasoning-llms): The Reasoning LLMs Guide shows how to use advanced AI models for step-by-step thinking, planning, and decision-making in complex tasks.
- [S*: Test Time Scaling for Code Generation📑](https://alphaxiv.org/abs/2502.14382): Parallel scaling (generating multiple solutions) + sequential scaling (iterative debugging). [20 Feb 2025]
- [s1: Simple test-time scaling📑](https://alphaxiv.org/abs/2501.19393): Curated small dataset of 1K. Budget forces stopping termination. Append "Wait" to lengthen. Achieved better reasoning performance. [31 Jan 2025]
- [Thinking Machines: A Survey of LLM based Reasoning Strategies📑](https://alphaxiv.org/abs/2503.10814) [13 Mar 2025]
- [Tina: Tiny Reasoning Models via LoRA📑](https://alphaxiv.org/abs/2504.15777): Low-rank adaptation (LoRA) with Reinforcement learning (RL) on a 1.5B parameter base model  [22 Apr 2025]


## **Large Language Model: Landscape**

#### Large Language Models (in 2023)

1. Change in perspective is necessary because some abilities only emerge at a certain scale. Some conclusions from the past are invalidated and we need to constantly unlearn intuitions built on top of such ideas.
1. From first-principles, scaling up the Transformer amounts to efficiently doing matrix multiplications with many, many machines.
1. Further scaling (think 10000x GPT-4 scale). It entails finding the inductive bias that is the bottleneck in further scaling.
> [🗣️](https://twitter.com/hwchung27/status/1710003293223821658) / [📺](https://t.co/vumzAtUvBl) / [✍️](https://t.co/IidLe4JfrC) [6 Oct 2023]

#### Large Language Model Comparison

- [AI Model Review](https://aimodelreview.com/): Compare 75 AI Models on 200+ Prompts Side By Side.
- [Artificial Analysis](https://artificialanalysis.ai/):💡Independent analysis of AI models and API providers.
- [Inside language models (from GPT to Olympus)](https://lifearchitect.ai/models/)
- [LiveBench](https://livebench.ai): a benchmark for LLMs designed with test set contamination.
- [LLMArena](https://lmarena.ai/):💡Chatbot Arena (formerly LMSYS): Free AI Chat to Compare & Test Best AI Chatbots
- [LLMprices.dev](https://llmprices.dev): Compare prices for models like GPT-4, Claude Sonnet 3.5, Llama 3.1 405b and many more.
- [LLM Pre-training and Post-training Paradigms](https://sebastianraschka.com/blog/2024/new-llm-pre-training-and-post-training.html) [17 Aug 2024] <br/>
  <img src="./files/llm-dev-pipeline-overview.png" width="350" />

#### The Big LLM Architecture Comparison (in 2025)

- [The Big LLM Architecture Comparison✍️](https://sebastianraschka.com/blog/2025/the-big-llm-architecture-comparison.html):💡 [19 Jul 2025]
- [Beyond Standard LLMs✍️](https://magazine.sebastianraschka.com/p/beyond-standard-llms):💡Linear Attention Hybrids, Text Diffusion, Code World Models, and Small Recursive Transformers [04 Nov 2025]


  | Model                 | Parameters | Attention Type                           | MoE                             | Norm                            | Positional Encoding            | Notable Features                                                                            |
  | --------------------- | ---------- | ---------------------------------------- | ------------------------------- | ------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------- |
  | **DeepSeek V3 / R1**  | 671B       | Multi-Head Latent Attention (MLA)        | Yes, 256 experts (37B active)   | Pre-normalization               | RoPE                           | KV compression via MLA, shared expert, high inference efficiency                            |
  | **OLMo 2**            | 32B        | Multi-Head Attention (MHA)               | No                              | Post-normalization + QK norm (RMSNorm) | RoPE                           | RMSNorm scaling after attention & FF, training stability                                  |
  | **Gemma 3 / 3n**      | 27B / 4B   | Sliding Window + Grouped-Query Attention | No                              | Pre + Post RMSNorm          | RoPE                           | Sliding window attention, Gemma 3n: Per-Layer Embedding (PLE), MatFormer slices             |
  | **Mistral Small 3.1** | 24B        | Grouped-Query Attention                  | No                              | Pre-normalization               | RoPE                           | Optimized for low latency, simpler than Gemma 3                                             |
  | **Llama 4 Maverick**  | 400B       | Grouped-Query Attention                  | Yes, fewer & larger experts     | Pre-normalization               | RoPE                           | Alternating MoE & dense layers, 17B active parameters                                       |
  | **Qwen3 (Dense)**     | 0.6–32B    | Grouped-Query Attention                  | No                              | Pre-normalization               | RoPE                           | Deep architecture, small memory footprint                                                   |
  | **Qwen3 (MoE)**       | 30B–235B   | Grouped-Query Attention                  | Yes, no shared expert           | Pre-normalization               | RoPE                           | Sparse MoE, optimized for large-scale inference                                             |
  | **SmolLM3**           | 3B         | Grouped-Query Attention                  | No                              | Pre-normalization               | NoPE (No Positional Embedding) | Good small-scale performance, improved length generalization                                |
  | **Kimi K2**           | 1T         | MLA                                      | Yes, more experts than DeepSeek | Pre-normalization               | RoPE                           | Muon optimizer, very high modeling performance, open-weight                                 |
  | **gpt-oss**           | 20B / 120B | Grouped-Query + Sliding Window           | Yes, few large experts          | Pre-normalization               | RoPE                           | Wider architecture, attention sinks, bias units                                             |
  | **Grok 2.5**          | 70B        | Grouped-Query Attention                  | Yes                              | Pre-normalization               | RoPE                           | Standard large-scale architecture                                                           |
  | **GLM-4.5**           | 130B       | Grouped-Query Attention                  | Yes                              | Pre-normalization               | RoPE                           | Standard architecture with high performance                                                 |
  | **Qwen3-Next**        | -        | Grouped-Query Attention                  | Yes                             | Pre-normalization               | RoPE                           | Expert size & number tuned, Gated DeltaNet + Gated Attention Hybrid, Multi-Token Prediction |

#### GPT-2 vs gpt-oss

- [From GPT-2 to gpt-oss: Analyzing the Architectural Advances✍️](https://magazine.sebastianraschka.com/p/from-gpt-2-to-gpt-oss-analyzing-the) [9 Aug 2025]

| Feature              | GPT-2                          | GPT-OSS                              |
| -------------------- | ------------------------------ | ------------------------------------ |
| Release & Size       | 2019, up to 1.5B params        | 2025, 20B & 120B params (MoE)        |
| Architecture         | Dense transformer decoder      | Mixture-of-Experts (MoE) decoder     |
| Activation & Dropout | Swish activation, uses dropout | GELU (or optimized), no dropout      |
| Parameter Efficiency | All params active per token    | Sparse activation of experts         |
| Deployment & License | MIT license    | Open-weight local runs, Apache 2.0   |
| Reasoning & Tools    | Basic generation               | Built-in chain-of-thought & tool use |

### **Evolutionary Tree of Large Language Models**

- Evolutionary Graph of LLaMA Family  
  <img src="./files/llama-0628-final.png" width="450" />  
- LLM evolutionary tree  
  <img src="./files/tree.png" alt="llm" width="450"/>  
- Timeline of SLMs  
  <img src="./files/slm-timeline.png" width="650" />  
- [A Comprehensive Survey of Small Language Models in the Era of Large Language Models📑](https://alphaxiv.org/abs/2411.03350) / [✨](https://github.com/FairyFali/SLMs-Survey) [4 Nov 2024] ![**github stars**](https://img.shields.io/github/stars/FairyFali/SLMs-Survey?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLM evolutionary tree📑](https://alphaxiv.org/abs/2304.13712): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2304.13712)]: A curated list of practical guide resources of LLMs (LLMs Tree, Examples, Papers) [✨](https://github.com/Mooler0410/LLMsPracticalGuide) [26 Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/Mooler0410/LLMsPracticalGuide?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [A Survey of Large Language Models📑](https://alphaxiv.org/abs/2303.18223): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.18223)] /[✨](https://github.com/RUCAIBox/LLMSurvey) [31 Mar 2023] contd.
 ![**github stars**](https://img.shields.io/github/stars/RUCAIBox/LLMSurvey?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **A Taxonomy of Natural Language Processing**

- An overview of different fields of study and recent developments in NLP. [🗄️](./files/taxonomy-nlp.pdf) / [✍️](https://towardsdatascience.com/a-taxonomy-of-natural-language-processing-dfc790cb4c01) [24 Sep 2023]
  Exploring the Landscape of Natural Language Processing Research [ref📑](https://alphaxiv.org/abs/2307.10652) [20 Jul 2023]
  <img src="./files/taxonomy-nlp.png" width="650" />  
 - NLP taxonomy  
  <img src="./files/taxonomy-nlp2.png" width="650" />  
  Distribution of the number of papers by most popular fields of study from 2002 to 2022

### **Large Language Model Collection**

- Ai2 (Allen Institute for AI)
  - Founded by Paul Allen, the co-founder of Microsoft, in Sep 2024.
  - [OLMo📑](https://alphaxiv.org/abs/2402.00838):💡Truly open language model and framework to build, study, and advance LMs, along with the training data, training and evaluation code, intermediate model checkpoints, and training logs. [✨](https://github.com/allenai/OLMo) [Feb 2024]
  - [OLMo 2](https://allenai.org/blog/olmo2) [26 Nov 2024]
  ![**github stars**](https://img.shields.io/github/stars/allenai/OLMo?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/allenai/OLMoE?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - [OLMoE✨](https://github.com/allenai/OLMoE): fully-open LLM leverages sparse Mixture-of-Experts [Sep 2024]
  - [TÜLU 3📑](https://alphaxiv.org/abs/2411.15124):💡Pushing Frontiers in Open Language Model Post-Training [✨](https://github.com/allenai/open-instruct) / demo:[✍️](https://playground.allenai.org/) [22 Nov 2024] ![**github stars**](https://img.shields.io/github/stars/allenai/open-instruct?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Alibaba
  1. Model overview [✍️](https://docs.mistral.ai/getting-started/models/)
- Amazon
  1. [Amazon Nova Foundation Models](https://aws.amazon.com/de/ai/generative-ai/nova/): Text only - Micro, Multimodal - Light, Pro [3 Dec 2024]
  1. [The Amazon Nova Family of Models: Technical Report and Model Card📑](https://alphaxiv.org/abs/2506.12103) [17 Mar 2025]
- Anthrophic
  1. [Claude 3✍️](https://www.anthropic.com/news/claude-3-family), the largest version of the new LLM, outperforms rivals GPT-4 and Google’s Gemini 1.0 Ultra. Three variants: Opus, Sonnet, and Haiku. [Mar 2024]
  1. [Claude 3.7 Sonnet and Claude Code✍️](https://www.anthropic.com/news/claude-3-7-sonnet): the first hybrid reasoning model. [✍️](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf) [25 Feb 2025]
  1. [Claude 4✍️](https://www.anthropic.com/news/claude-4): Claude Opus 4 (72.5% on SWE-bench),  Claude Sonnet 4 (72.7% on SWE-bench). Extended Thinking Mode (Beta). Parallel Tool Use & Memory. Claude Code SDK. AI agents: code execution, MCP connector, Files API, and 1-hour prompt caching. [23 May 2025]
  1. [Claude 4.5✍️](https://www.anthropic.com/news/claude-sonnet-4-5): Major upgrades in autonomous coding, tool use, context handling, memory, and long-horizon reasoning; supports over 30 hours of continuous operation. [30 Sep 2025]
  1. [anthropic/cookbook✨](https://github.com/anthropics/anthropic-cookbook)
- Apple
  1. [OpenELM](https://machinelearning.apple.com/research/openelm): Apple released a Transformer-based language model. Four sizes of the model: 270M, 450M, 1.1B, and 3B parameters. [April 2024]
  1. [Apple Intelligence Foundation Language Models](https://machinelearning.apple.com/research/apple-intelligence-foundation-language-models): 1. A 3B on-device model used for language tasks like summarization and Writing Tools. 2. A large Server model used for language tasks too complex to do on-device. [10 Jun 2024]
- Baidu
  1. [ERNIE Bot's official website](https://yiyan.baidu.com/): ERNIE X1 (deep-thinking reasoning) and ERNIE 4.5 (multimodal) [16 Mar 2025]
  1. A list of models & libraries: [✨](https://github.com/PaddlePaddle/ERNIE)
- Chatbot Arena🤗
  - [Chatbot Arena🤗](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard): Benchmarking LLMs in the Wild with Elo Ratings
- Cohere
  - Founded in 2019. Canadian multinational tech.
  1. [Command R+🤗](https://huggingface.co/collections/CohereForAI/c4ai-command-r-plus-660ec4c34f7a69c50ce7f7b9): The performant model for RAG capabilities, multilingual support, and tool use. [Aug 2024]
  1. [An Overview of Cohere’s Models](https://docs.cohere.com/v2/docs/models) | [Playground](https://dashboard.cohere.com/playground)
- Databricks
  1. [DBRX](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm): MoE, open, general-purpose LLM created by Databricks. [✨](https://github.com/databricks/dbrx) [27 Mar 2024]
 ![**github stars**](https://img.shields.io/github/stars/databricks/dbrx?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Deepseek
  - Founded in 2023, is a Chinese company dedicated to AGI.
  1. [DeepSeek-V3✨](https://github.com/deepseek-ai/DeepSeek-V3): Mixture-of-Experts (MoE) with 671B. [26 Dec 2024]
  1. [DeepSeek-R1✨](https://github.com/deepseek-ai/DeepSeek-R1):💡an open source reasoning model. Group Relative Policy Optimization (GRPO). Base -> RL -> SFT -> RL -> SFT -> RL [20 Jan 2025] [ref📑](https://alphaxiv.org/abs/2503.11486): A Review of DeepSeek Models' Key Innovative Techniques [14 Mar 2025]
  1. [Janus✨](https://github.com/deepseek-ai/Janus): Multimodal understanding and visual generation. [28 Jan 2025]
  1. [DeepSeek-V3🤗](https://huggingface.co/deepseek-ai/DeepSeek-V3): 671B. Top-tier performance in coding and reasoning tasks [25 Mar 2025]
  1. [DeepSeek-Prover-V2✨](https://github.com/deepseek-ai/DeepSeek-Prover-V2): Mathematical reasoning [30 Apr 2025]
  1. [DeepSeek-v3.1🤗](https://huggingface.co/deepseek-ai/DeepSeek-V3.1): Think/Non‑Think hybrid reasoning. 128K and MoE. Agent abilities.  [19 Aug 2025]
  1. [DeepSeek-V3.2-Exp✨](https://github.com/deepseek-ai/DeepSeek-V3.2-Exp) [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-V3.2-Exp?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [DeepSeek-OCR✨](https://github.com/deepseek-ai/DeepSeek-OCR): Convert long text into an image, compresses it into visual tokens, and sends those to the LLM — cutting cost and expanding context capacity. [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-OCR?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. A list of models: [✨](https://github.com/deepseek-ai)
- EleutherAI
  - Founded in July 2020. United States tech. GPT-Neo, GPT-J, GPT-NeoX, and The Pile dataset.
  - [Pythia📑](https://alphaxiv.org/abs/2304.01373): How do large language models (LLMs) develop and evolve over the course of training and change as models scale? A suite of decoder-only autoregressive language models ranging from 70M to 12B parameters [✨](https://github.com/EleutherAI/pythia) [Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/EleutherAI/pythia?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- GPT for Domain Specific [🔗](#gpt-for-domain-specific)
- Google
  1. [Foundation Models](https://ai.google/discover/our-models/): Gemini, Veo, Gemma etc.
  1. [Gemma](http://ai.google.dev/gemma): Open weights LLM from Google DeepMind. [✨](https://github.com/google-deepmind/gemma) / Pytorch [✨](https://github.com/google/gemma_pytorch) [Feb 2024]
 ![**github stars**](https://img.shields.io/github/stars/google-deepmind/gemma?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/google/gemma_pytorch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [Gemma 2](https://www.kaggle.com/models/google/gemma-2/) 2B, 9B, 27B [ref: releases](https://ai.google.dev/gemma/docs/releases) [Jun 2024]
  1. [Gemma 3](https://developers.googleblog.com/en/introducing-gemma3/):  Single GPU. Context
length of 128K tokens, SigLIP encoder, Reasoning [✍️](https://storage.googleapis.com/deepmind-media/gemma/Gemma3Report.pdf) [12 Mar 2025]
  1. [Gemini](https://gemini.google.com/app): Rebranding: Bard -> Gemini [8 Feb 2024]
  1. [Gemini 1.5✍️](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024): 1 million token context window, 1 hour of video, 11 hours of audio, codebases with over 30,000 lines of code or over 700,000 words. [Feb 2024]
  1. [Gemini 2 Flash✍️](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/): Multimodal LLM with multilingual inputs/outputs, real-time capabilities (Project Astra), complex task handling (Project Mariner), and developer tools (Jules) [11 Dec 2024]
  1. Gemini 2.0 Flash Thinking Experimental [19 Dec 2024]
  1. [Gemini 2.5✍️](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/): strong reasoning and code. 1 million token context [25 Mar 2025] -> [I/O 2025✍️](https://blog.google/technology/ai/io-2025-keynote) Deep Think, 1M-token context, Native audio output, Project Mariner: AI-powered computer control. [20 May 2025] [Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities.📑](https://alphaxiv.org/abs/2507.06261)
  1. [Gemma 3n](https://developers.googleblog.com/en/introducing-gemma-3n/): The next generation of Gemini Nano. Gemma 3n uses DeepMind’s Per-Layer Embeddings (PLE) to run 5B/8B models at 2GB/3GB RAM. [20 May 2025]
  1. [gemini/cookbook✨](https://github.com/google-gemini/cookbook)
- Groq
  - Founded in 2016. low-latency AI inference H/W. American tech.
  1. [Llama-3-Groq-Tool-Use](https://wow.groq.com/introducing-llama-3-groq-tool-use-models/): a model optimized for function calling [Jul 2024]
- Huggingface
  1. [Open R1✨](https://github.com/huggingface/open-r1): A fully open reproduction of DeepSeek-R1. [25 Jan 2025]
  1. [Huggingface Open LLM Learboard🤗](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
- IBM
  1. [Granite Guardian✨](https://github.com/ibm-granite/granite-guardian): a collection of models designed to detect risks in prompts and responses [10 Dec 2024]
- Jamba
  - [Jamba](https://www.ai21.com/blog/announcing-jamba): AI21's SSM-Transformer Model. Mamba  + Transformer + MoE [28 Mar 2024]
- [KoAlpaca✨](https://github.com/Beomi/KoAlpaca): Alpaca for korean [Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/Beomi/KoAlpaca?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Large Language Models (in 2023) [🔗](#large-language-models-in-2023)
- Llama variants emerged in 2023</summary>
  - [Falcon LLM](https://falconllm.tii.ae/) Apache 2.0 license [Mar 2023]
  - [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html): Fine-tuned from the LLaMA 7B model [Mar 2023]
  - [vicuna](https://vicuna.lmsys.org/): 90% ChatGPT Quality [Mar 2023]
  - [dolly](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html): Databricks [Mar 2023]
  - [Cerebras-GPT](https://www.cerebras.net/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models/): 7 GPT models ranging from 111m to 13b parameters. [Mar 2023]
  - [Koala](https://bair.berkeley.edu/blog/2023/04/03/koala/): Focus on dialogue data gathered from the web.  [Apr 2023]
  - [StableVicuna](https://stability.ai/blog/stablevicuna-open-source-rlhf-chatbot) First Open Source RLHF LLM Chatbot [Apr 2023]
  - Upstage's 70B Language Model Outperforms GPT-3.5: [✍️](https://en.upstage.ai/newsroom/upstage-huggingface-llm-no1) [1 Aug 2023]
- [LLM Collection](https://www.promptingguide.ai/models/collection): promptingguide.ai
- Meta
  1. Most OSS LLM models have been built on the [Llama✨](https://github.com/facebookresearch/llama) / [✍️](https://ai.meta.com/llama) / [✨](https://github.com/meta-llama/llama-models)
 ![**github stars**](https://img.shields.io/github/stars/facebookresearch/llama?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/meta-llama/llama-models?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [Llama 2🤗](https://huggingface.co/blog/llama2): 1) 40% more data than Llama. 2)7B, 13B, and 70B. 3) Trained on over 1 million human annotations. 4) double the context length of Llama 1: 4K 5) Grouped Query Attention, KV Cache, and Rotary Positional Embedding were introduced in Llama 2 [18 Jul 2023] [demo🤗](https://huggingface.co/blog/llama2#demo)
  1. [Llama 3](https://llama.meta.com/llama3/): 1) 7X more data than Llama 2. 2) 8B, 70B, and 400B. 3) 8K context length [18 Apr 2024]
  1. [MEGALODON✨](https://github.com/XuezheMax/megalodon): Long Sequence Model. Unlimited context length. Outperforms Llama 2 model. [Apr 2024]
 ![**github stars**](https://img.shields.io/github/stars/XuezheMax/megalodon?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [Llama 3.1](https://ai.meta.com/blog/meta-llama-3-1/): 405B, context length to 128K, add support across eight languages. first OSS model outperforms GTP-4o. [23 Jul 2024]
  1. [Llama 3.2](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/): Multimodal. Include text-only models (1B, 3B) and text-image models (11B, 90B), with quantized versions of 1B and 3B [Sep 2024]
  1. [NotebookLlama✨](https://github.com/meta-llama/llama-recipes/tree/main/recipes/quickstart/NotebookLlama): An Open Source version of NotebookLM [28 Oct 2024]
  1. [Llama 3.3](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_3/): a text-only 70B instruction-tuned model. Llama 3.3 70B approaches the performance of Llama 3.1 405B. [6 Dec 2024]
  1. [Llama 4](https://www.llama.com/docs/model-cards-and-prompt-formats/llama4_omni/):  Mixture of Experts (MoE). Llama 4 Scout (actived 17b / total 109b, 10M Context, single GPU), Llama 4 Maverick (actived 17b / total 400b, 1M Context) [✨](https://github.com/meta-llama/llama-models/tree/main/models/llama4): Model Card [5 Apr 2025] 
- MLLM (multimodal large language model) [🔗](#mllm-multimodal-large-language-model)
- [ModernBERT📑](https://alphaxiv.org/abs/2412.13663): ModernBERT can handle sequences up to 8,192 tokens and utilizes sparse attention mechanisms to efficiently manage longer context lengths. [18 Dec 2024]
- Microsoft
  1. [MAI-1✍️](https://microsoft.ai/news/two-new-in-house-models/): MAI-Voice-1, MAI-1-preview. Microsoft in-house models. [28 Aug 2025]
  1. phi-series: cost-effective small language models (SLMs) [✍️](https://azure.microsoft.com/en-us/products/phi) [✨](https://aka.ms/Phicookbook): Cookbook
  1. [Phi-1📑](https://alphaxiv.org/abs/2306.11644): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2306.11644)]: Despite being small in size, phi-1 attained 50.6% on HumanEval and 55.5% on MBPP. Textbooks Are All You Need. [✍️](https://analyticsindiamag.com/microsoft-releases-1-3-bn-parameter-language-model-outperforms-llama/) [20 Jun 2023]
  1. [Phi-1.5📑](https://alphaxiv.org/abs/2309.05463): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.05463)]: Textbooks Are All You Need II. Phi 1.5 is trained solely on synthetic data. Despite having a mere 1 billion parameters compared to Llama 7B's much larger model size, Phi 1.5 often performs better in benchmark tests. [11 Sep 2023]
  1. phi-2: open source, and 50% better at mathematical reasoning. [✨🤗](https://huggingface.co/microsoft/phi-2) [Dec 2023]
  1. phi-3-vision (multimodal), phi-3-small, phi-3 (7b), phi-sillica (Copilot+PC designed for NPUs)
  1. [Phi-3📑](https://alphaxiv.org/abs/2404.14219): Phi-3-mini, with 3.8 billion parameters, supports 4K and 128K context, instruction tuning, and hardware optimization. [22 Apr 2024] [✍️](https://azure.microsoft.com/en-us/blog/introducing-phi-3-redefining-whats-possible-with-slms/)
  1. phi-3.5-MoE-instruct: [🤗](https://huggingface.co/microsoft/Phi-3.5-MoE-instruct) [Aug 2024]
  1. [Phi-4📑](https://alphaxiv.org/abs/2412.08905): Specializing in Complex Reasoning [✍️](https://techcommunity.microsoft.com/blog/aiplatformblog/introducing-phi-4-microsoft%E2%80%99s-newest-small-language-model-specializing-in-comple/4357090) [12 Dec 2024]
  1. [Phi-4-multimodal / mini🤗](https://huggingface.co/microsoft/Phi-4-multimodal-instruct/blob/main/phi_4_mm.tech_report.02252025.pdf) 5.6B. speech, vision, and text processing into a single, unified architecture. [26 Feb 2025]
  1. [Phi-4-reasoning✍️](https://azure.microsoft.com/en-us/blog/one-year-of-phi-small-language-models-making-big-leaps-in-ai/): Phi-4-reasoning, Phi-4-reasoning-plus, Phi-4-mini-reasoning [30 Apr 2025]
  1. [Phi-4-mini-flash-reasoning✍️](https://azure.microsoft.com/en-us/blog/reasoning-reimagined-introducing-phi-4-mini-flash-reasoning/): 3.8B, 64K context, Single GPU, Decoder-Hybrid-Decoder architecture  [9 Jul 2025]
- MiniMaxAI
  - Founded in Dec 2021. Shanghai, China.
  1. [MiniMax-M2✨](https://github.com/MiniMax-AI/MiniMax-M2): Coding and Agent tasks, 230B (10B Active), MoE, a new high ahead of DeepSeek-V3.2 and Kimi K2 ![**github stars**](https://img.shields.io/github/stars/MiniMax-AI/MiniMax-M2?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Mistral
  - Founded in April 2023. French tech.
  1. Model overview [✍️](https://docs.mistral.ai/getting-started/models/)
  1. [NeMo](https://mistral.ai/news/mistral-nemo/): 12B model with 128k context length that outperforms LLama 3 8B [18 Jul 2024]
  1. [Mistral OCR](https://mistral.ai/news/mistral-ocr): Precise text recognition with up to 99% accuracy. Multimodal. Browser based [6 Mar 2025]
- Moonshot AI
  - Moonshot AI is a Beijing-based Chinese AI company founded in March 2023
  1. [Kimi-K2✨](https://github.com/MoonshotAI/Kimi-K2): 1T parameter MoE model. MuonClip Optimizer. Agentic Intelligence. [11 Jul 2025]
- NVIDIA
  1. [Nemotron-4 340B](https://research.nvidia.com/publication/2024-06_nemotron-4-340b): Synthetic Data Generation for Training Large Language Models [14 Jun 2024]
- [ollam](https://ollama.com/library?sort=popular): ollama-supported models
- [Open-Sora✨](https://github.com/hpcaitech/Open-Sora): Democratizing Efficient Video Production for All  [Mar 2024]
 ![**github stars**](https://img.shields.io/github/stars/hpcaitech/Open-Sora?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- OpenAI
  1. [gpt-oss✨](https://github.com/openai/gpt-oss):💡**gpt-oss-120b** and **gpt-oss-20b** are two open-weight language models by OpenAI. [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/openai/gpt-oss?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Qualcomm
  1. [Qualcomm’s on-device AI models🤗](https://huggingface.co/qualcomm): Bring generative AI to mobile devices [Feb 2024]
- Tencent
  - Founded in 1998, Tencent is a Chinese company dedicated to various technology sectors, including social media, gaming, and AI development.
  - [Hunyuan-Large](https://alphaxiv.org/pdf/2411.02265): An open-source MoE model with open weights. [4 Nov 2024] [✨](https://github.com/Tencent/Tencent-Hunyuan-Large) ![**github stars**](https://img.shields.io/github/stars/Tencent/Tencent-Hunyuan-Large?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - [Hunyuan-T1](https://tencent.github.io/llm.hunyuan.T1/README_EN.html): Reasoning model [21 Mar 2025]
  - A list of models: [✨](https://github.com/Tencent-Hunyuan)
- [The LLM Index](https://sapling.ai/llm/index): A list of large language models (LLMs)
- [The mother of all spreadsheets for anyone into LLMs](https://x.com/DataChaz/status/1868708625310699710) [17 Dec 2024]
- [The Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) [28 Oct 2024]
- xAI
  - xAI is an American AI company founded by Elon Musk in March 2023
  1. [Grok](https://x.ai/blog/grok-os): 314B parameter Mixture-of-Experts (MoE) model. Released under the Apache 2.0 license. Not includeded training code. Developed by JAX [✨](https://github.com/xai-org/grok) [17 Mar 2024]
 ![**github stars**](https://img.shields.io/github/stars/xai-org/grok?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [Grok-2 and Grok-2 mini](https://x.ai/blog/grok-2) [13 Aug 2024]
  1. [Grok-3](https://x.ai/grok): 200,000 GPUs to train. Grok 3 beats GPT-4o on AIME, GPQA. Grok 3 Reasoning and Grok 3 mini Reasoning. [17 Feb 2025]
  1. [Grok-4](https://x.ai/news/grok-4): Humanity’s Last Exam, Grok 4 Heavy scored 44.4% [9 Jul 2025]
  1. [Grok-2.5](https://x.com/elonmusk/status/1959379349322313920): Grok 2.5 Goes Open Source [24 Aug 2025]
- Xiaomi
  - Founded in 2010, Xiaomi is a Chinese company known for its innovative consumer electronics and smart home products.
  - [Mimo✨](https://github.com/XiaomiMiMo/MiMo): 7B. advanced reasoning for code and math [30 Apr 2025)
- Z.ai
  - formerly Zhipu, Beijing-based Chinese AI company founded in March 2019
  1. [GLM-4.5✨](https://github.com/zai-org/GLM-4.5): An open-source large language model designed for intelligent agents
  1. [GLM-4.6✍️](https://z.ai/blog/glm-4.6): GLM-4.6: Advanced Agentic, Reasoning and Coding Capabilities [30 Sep 2025]


### **LLM for Domain Specific**

- [AI for Scaling Legal Reform: Mapping and Redacting Racial Covenants in Santa Clara County📑](https://alphaxiv.org/abs/2503.03888): a fine-tuned open LLM to detect racial covenants in 24　million housing documents, cutting 86,500 hours of manual work. [12 Feb 2025]
- [AlphaChip](https://deepmind.google/discover/blog/how-alphachip-transformed-computer-chip-design/): Reinforcement learning-based model for designing physical chip layouts. [26 Sep 2024]
- [AlphaFold3✨](https://github.com/Ligo-Biosciences/AlphaFold3): Open source implementation of AlphaFold3 [Nov 2023] / [OpenFold✨](https://github.com/aqlaboratory/openfold): PyTorch reproduction of AlphaFold 2 [Sep 2021] ![**github stars**](https://img.shields.io/github/stars/Ligo-Biosciences/AlphaFold3?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/aqlaboratory/openfold?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [AlphaGenome](https://deepmind.google/discover/blog/alphagenome-ai-for-better-understanding-the-genome): DeepMind’s advanced AI model, launched in June 2025, is designed to analyze the regulatory “dark matter” of the genome—specifically, the 98% of DNA that does not code for proteins but instead regulates when and how genes are expressed. [June 2025]
- [BioGPT📑](https://alphaxiv.org/abs/2210.10341): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2210.10341)]: Generative Pre-trained Transformer for Biomedical Text Generation and Mining [✨](https://github.com/microsoft/BioGPT) [19 Oct 2022] ![**github stars**](https://img.shields.io/github/stars/microsoft/BioGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [BloombergGPT📑](https://alphaxiv.org/abs/2303.17564): A Large Language Model for Finance [30 Mar 2023]
- [Chai-1✨](https://github.com/chaidiscovery/chai-lab): a multi-modal foundation model for molecular structure prediction [Sep 2024]
 ![**github stars**](https://img.shields.io/github/stars/chaidiscovery/chai-lab?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Code Llama📑](https://alphaxiv.org/abs/2308.12950): Built on top of Llama 2, free for research and commercial use. [✍️](https://ai.meta.com/blog/code-llama-large-language-model-coding/) / [✨](https://github.com/facebookresearch/codellama) [24 Aug 2023] ![**github stars**](https://img.shields.io/github/stars/facebookresearch/codellama?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [DeepSeek-Coder-V2✨](https://github.com/deepseek-ai/DeepSeek-Coder-V2): Open-source Mixture-of-Experts (MoE) code language model [17 Jun 2024]
 ![**github stars**](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-Coder-V2?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Devin AI](https://preview.devin.ai/): Devin is an AI software engineer developed by Cognition AI [12 Mar 2024]
- [EarthGPT📑](https://alphaxiv.org/abs/2401.16822): A Universal Multi-modal Large Language Model for Multi-sensor Image Comprehension in Remote Sensing Domain [30 Jan 2024]
- [ESM3: A frontier language model for biology](https://www.evolutionaryscale.ai/blog/esm3-release): Simulating 500 million years of evolution [✨](https://github.com/evolutionaryscale/esm) / [✍️](https://doi.org/10.1101/2024.07.01.600583) [31 Dec 2024]  ![**github stars**](https://img.shields.io/github/stars/evolutionaryscale/esm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [FrugalGPT📑](https://alphaxiv.org/abs/2305.05176): LLM with budget constraints, requests are cascaded from low-cost to high-cost LLMs. [✨](https://github.com/stanford-futuredata/FrugalGPT) [9 May 2023] ![**github stars**](https://img.shields.io/github/stars/stanford-futuredata/FrugalGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Galactica📑](https://alphaxiv.org/abs/2211.09085): A Large Language Model for Science [16 Nov 2022]
- Gemma series
  1. [Gemma series in Huggingface🤗](https://huggingface.co/google)
  1. [PaliGemma📑](https://alphaxiv.org/abs/2407.07726): a 3B VLM [10 Jul 2024]
  1. [DataGemma✍️](https://blog.google/technology/ai/google-datagemma-ai-llm/) [12 Sep 2024] / [NotebookLM✍️](https://blog.google/technology/ai/notebooklm-audio-overviews/): LLM-powered notebook. free to use, not open-source. [12 Jul 2023]
  1. [PaliGemma 2📑](https://alphaxiv.org/abs/2412.03555): VLMs
 at 3 different sizes (3B, 10B, 28B)  [4 Dec 2024]
  1. [TxGemma](https://developers.googleblog.com/en/introducing-txgemma-open-models-improving-therapeutics-development/): Therapeutics development [25 Mar 2025]
  1. [Dolphin Gemma✍️](https://blog.google/technology/ai/dolphingemma/): Decode dolphin communication [14 Apr 2025]
  1. [MedGemma](https://deepmind.google/models/gemma/medgemma/): Model fine-tuned for biomedical text and image understanding. [20 May 2025]
  1. [SignGemma](https://x.com/GoogleDeepMind/status/1927375853551235160): Vision-language model for sign language recognition and translation. [27 May 2025)
- [Huggingface StarCoder: A State-of-the-Art LLM for Code🤗](https://huggingface.co/blog/starcoder): [✨🤗](https://huggingface.co/bigcode/starcoder) [May 2023]
- [MechGPT📑](https://alphaxiv.org/abs/2310.10445): Language Modeling Strategies for Mechanics and Materials [✨](https://github.com/lamm-mit/MeLM) [16 Oct 2023] ![**github stars**](https://img.shields.io/github/stars/lamm-mit/MeLM?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [MeshGPT](https://nihalsid.github.io/mesh-gpt/): Generating Triangle Meshes with Decoder-Only Transformers [27 Nov 2023]
- [OpenCoder✨](https://github.com/OpenCoder-llm/OpenCoder-llm): 1.5B and 8B base and open-source Code LLM, supporting both English and Chinese. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/OpenCoder-llm/OpenCoder-llm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Prithvi WxC📑](https://alphaxiv.org/abs/2409.13598): In collaboration with NASA, IBM is releasing an open-source foundation model for Weather and Climate [✍️](https://research.ibm.com/blog/foundation-model-weather-climate) [20 Sep 2024]
- [Qwen2-Math✨](https://github.com/QwenLM/Qwen2-Math): math-specific LLM / [Qwen2-Audio✨](https://github.com/QwenLM/Qwen2-Audio): large-scale audio-language model [Aug 2024] / [Qwen 2.5-Coder✨](https://github.com/QwenLM/Qwen2.5-Coder) [18 Sep 2024]
 ![**github stars**](https://img.shields.io/github/stars/QwenLM/Qwen2-Math?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/QwenLM/Qwen2-Audio?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/QwenLM/Qwen2.5-Coder?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Qwen3-Coder✨](https://github.com/QwenLM/Qwen3-Coder): Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team, Alibaba Cloud. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/QwenLM/Qwen3-Coder?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [SaulLM-7B📑](https://alphaxiv.org/abs/2403.03883): A pioneering Large Language Model for Law [6 Mar 2024]
- [TimeGPT](https://nixtla.github.io/nixtla/): The First Foundation Model for Time Series Forecasting [✨](https://github.com/Nixtla/neuralforecast) [Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/Nixtla/neuralforecast?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Video LLMs for Temporal Reasoning in Long Videos📑](https://alphaxiv.org/abs/2412.02930): TemporalVLM, a video LLM excelling in temporal reasoning and fine-grained understanding of long videos, using time-aware features and validated on datasets like TimeIT and IndustryASM for superior performance. [4 Dec 2024]

### **MLLM (multimodal large language model)**

- Apple
  1. [4M-21📑](https://alphaxiv.org/abs/2406.09406): An Any-to-Any Vision Model for Tens of Tasks and Modalities. [13 Jun 2024]
- [Awesome Multimodal Large Language Models✨](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models): Latest Papers and Datasets on Multimodal Large Language Models, and Their Evaluation. [Jun 2023]
 ![**github stars**](https://img.shields.io/github/stars/BradyFU/Awesome-Multimodal-Large-Language-Models?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Benchmarking Multimodal LLMs.
  - LLaVA-1.5 achieves SoTA on a broad range of 11 tasks incl. SEED-Bench.
  - [SEED-Bench📑](https://alphaxiv.org/abs/2307.16125): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.16125)]: Benchmarking Multimodal LLMs [✨](https://github.com/AILab-CVC/SEED-Bench) [30 Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/AILab-CVC/SEED-Bench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)  
- [BLIP-2📑](https://alphaxiv.org/abs/2301.12597) [30 Jan 2023]: [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2301.12597)]: Salesforce Research, Querying Transformer (Q-Former) / [✨](https://github.com/salesforce/LAVIS/blob/main/lavis/models/blip2_models/blip2_qformer.py) / [🤗](https://huggingface.co/blog/blip-2) / [📺](https://www.youtube.com/watch?v=k0DAtZCCl1w) / [BLIP📑](https://alphaxiv.org/abs/2201.12086): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2201.12086)]: [✨](https://github.com/salesforce/BLIP) [28 Jan 2022]
 ![**github stars**](https://img.shields.io/github/stars/salesforce/BLIP?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - `Q-Former (Querying Transformer)`: A transformer model that consists of two submodules that share the same self-attention layers: an image transformer that interacts with a frozen image encoder for visual feature extraction, and a text transformer that can function as both a text encoder and a text decoder.
  - Q-Former is a lightweight transformer which employs a set of learnable query vectors to extract visual features from the frozen image encoder. It acts as an information bottleneck between the frozen image encoder and the frozen LLM.
- [CLIP📑](https://alphaxiv.org/abs/2103.00020): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2103.00020)]: CLIP (Contrastive Language-Image Pretraining), Trained on a large number of internet text-image pairs and can be applied to a wide range of tasks with zero-shot learning. [✨](https://github.com/openai/CLIP) [26 Feb 2021]
 ![**github stars**](https://img.shields.io/github/stars/openai/CLIP?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Drag Your GAN📑](https://alphaxiv.org/abs/2305.10973): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.10973)]: Interactive Point-based Manipulation on the Generative Image Manifold [✨](https://github.com/Zeqiang-Lai/DragGAN) [18 May 2023]
 ![**github stars**](https://img.shields.io/github/stars/Zeqiang-Lai/DragGAN?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [GroundingDINO📑](https://alphaxiv.org/abs/2303.05499): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.05499)]: DINO with Grounded Pre-Training for Open-Set Object Detection [✨](https://github.com/IDEA-Research/GroundingDINO) [9 Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/IDEA-Research/GroundingDINO?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Hugging Face
  1. [SmolVLM🤗](https://huggingface.co/blog/smolvlm): 2B small vision language models. [🤗](https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct) / finetuning:[✨](https://github.com/huggingface/smollm/blob/main/finetuning/Smol_VLM_FT.ipynb) [24 Nov 2024]
- [LLaVa📑](https://alphaxiv.org/abs/2304.08485): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2304.08485)]: Large Language-and-Vision Assistant [✨](https://llava-vl.github.io/) [17 Apr 2023]
  - Simple linear layer to connect image features into the word embedding space. A trainable projection matrix W is applied to the visual features Zv, transforming them into visual embedding tokens Hv. These tokens are then concatenated with the language embedding sequence Hq to form a single sequence. Note that Hv and Hq are not multiplied or added, but concatenated, both are same dimensionality.
- [LLaVA-CoT📑](https://alphaxiv.org/abs/2411.10440): (FKA. LLaVA-o1) Let Vision Language Models Reason Step-by-Step. [✨](https://github.com/PKU-YuanGroup/LLaVA-CoT) [15 Nov 2024]
- Meta (aka. Facebook)
  1. [facebookresearch/ImageBind📑](https://alphaxiv.org/abs/2305.05665): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.05665)]: ImageBind One Embedding Space to Bind Them All [✨](https://github.com/facebookresearch/ImageBind) [9 May 2023]
 ![**github stars**](https://img.shields.io/github/stars/facebookresearch/ImageBind?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [facebookresearch/segment-anything(SAM)📑](https://alphaxiv.org/abs/2304.02643): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2304.02643)]: The repository provides code for running inference with the SegmentAnything Model (SAM), links for downloading the trained model checkpoints, and example notebooks that show how to use the model. [✨](https://github.com/facebookresearch/segment-anything) [5 Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/facebookresearch/segment-anything?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [facebookresearch/SeamlessM4T📑](https://alphaxiv.org/abs/2308.11596): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2308.11596)]: SeamlessM4T is the first all-in-one multilingual multimodal AI translation and transcription model. This single model can perform speech-to-text, speech-to-speech, text-to-speech, and text-to-text translations for up to 100 languages depending on the task. [✍️](https://about.fb.com/news/2023/08/seamlessm4t-ai-translation-model/) [22 Aug 2023]
  1. [Chameleon📑](https://alphaxiv.org/abs/2405.09818): Early-fusion token-based mixed-modal models capable of understanding and generating images and text in any arbitrary sequence. The unified approach uses fully token-based representations for both image and textual modalities. no vision-encoder. [16 May 2024]
  1. [Models and libraries](https://ai.meta.com/resources/models-and-libraries/)
- Microsoft
  1. Language Is Not All You Need: Aligning Perception with Language Models [Kosmos-1📑](https://alphaxiv.org/abs/2302.14045): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2302.14045)] [27 Feb 2023]
  1. [Kosmos-2📑](https://alphaxiv.org/abs/2306.14824): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2306.14824)]: Grounding Multimodal Large Language Models to the World [26 Jun 2023]
  1. [Kosmos-2.5📑](https://alphaxiv.org/abs/2309.11419): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.11419)]: A Multimodal Literate Model [20 Sep 2023]
  1. [BEiT-3📑](https://alphaxiv.org/abs/2208.10442): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2208.10442)]: Image as a Foreign Language: BEiT Pretraining for Vision and Vision-Language Tasks [22 Aug 2022]
  1. [TaskMatrix.AI📑](https://alphaxiv.org/abs/2303.16434): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.16434)]: TaskMatrix connects ChatGPT and a series of Visual Foundation Models to enable sending and receiving images during chatting. [29 Mar 2023]
  1. [Florence-2📑](https://alphaxiv.org/abs/2311.06242): Advancing a unified representation for various vision tasks, demonstrating specialized models like `CLIP` for classification, `GroundingDINO` for object detection, and `SAM` for segmentation. [🤗](https://huggingface.co/microsoft/Florence-2-large) [10 Nov 2023]
  1. [LLM2CLIP✨](https://github.com/microsoft/LLM2CLIP): Directly integrating LLMs into CLIP causes catastrophic performance drops. We propose LLM2CLIP, a caption contrastive fine-tuning method that leverages LLMs to enhance CLIP. [7 Nov 2024]
  1. [Florence-VL📑](https://alphaxiv.org/abs/2412.04424): A multimodal large language model (MLLM) that integrates Florence-2. [5 Dec 2024]
  1. [Magma✨](https://github.com/microsoft/Magma): Magma: A Foundation Model for Multimodal AI Agents [18 Feb 2025]
- [MiniCPM-o✨](https://github.com/OpenBMB/MiniCPM-o): A GPT-4o Level MLLM for Vision, Speech and Multimodal Live Streaming on Your Phone [15 Jan 2025]
- [MiniCPM-V✨](https://github.com/OpenBMB/MiniCPM-V): MiniCPM-Llama3-V 2.5: A GPT-4V Level Multimodal LLM on Your Phone [Jan 2024]
 ![**github stars**](https://img.shields.io/github/stars/OpenBMB/MiniCPM-V?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [MiniGPT-4 & MiniGPT-v2📑](https://alphaxiv.org/abs/2304.10592): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2304.10592)]: Enhancing Vision-language Understanding with Advanced Large Language Models [✨](https://minigpt-4.github.io/) [20 Apr 2023]
- [mini-omni2✨](https://github.com/gpt-omni/mini-omni2): [✍️](alphaxiv.org/abs/2410.11190): Towards Open-source GPT-4o with Vision, Speech and Duplex Capabilities. [15 Oct 2024]
 ![**github stars**](https://img.shields.io/github/stars/gpt-omni/mini-omni2?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Molmo and PixMo📑](https://alphaxiv.org/abs/2409.17146): Open Weights and Open Data for State-of-the-Art Multimodal Models [✍️](https://molmo.allenai.org/) [25 Sep 2024] <!-- <img src="./files/multi-llm.png" width="180" /> -->
- [moondream✨](https://github.com/vikhyat/moondream): an OSS tiny vision language model. Built using SigLIP, Phi-1.5, LLaVA dataset. [Dec 2023]
 ![**github stars**](https://img.shields.io/github/stars/vikhyat/moondream?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Multimodal Foundation Models: From Specialists to General-Purpose Assistants📑](https://alphaxiv.org/abs/2309.10020): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.10020)]: A comprehensive survey of the taxonomy and evolution of multimodal foundation models that demonstrate vision and vision-language capabilities. Specific-Purpose 1. Visual understanding tasks 2. Visual generation tasks General-Purpose 3. General-purpose interface. [18 Sep 2023]
- Optimizing Memory Usage for Training LLMs and Vision Transformers: When applying 10 techniques to a vision transformer, we reduced the memory consumption 20x on a single GPU. [✍️](https://lightning.ai/pages/community/tutorial/pytorch-memory-vit-llm/) / [✨](https://github.com/rasbt/pytorch-memory-optim) [2 Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/rasbt/pytorch-memory-optim?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [openai/shap-e📑](https://alphaxiv.org/abs/2305.02463) Generate 3D objects conditioned on text or images [3 May 2023] [✨](https://github.com/openai/shap-e)
 ![**github stars**](https://img.shields.io/github/stars/openai/shap-e?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [TaskMatrix, aka. VisualChatGPT📑](https://alphaxiv.org/abs/2303.04671): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.04671)]: Microsoft TaskMatrix [✨](https://github.com/microsoft/TaskMatrix); GroundingDINO + [SAM📑](https://alphaxiv.org/abs/2304.02643) / [✨](https://github.com/facebookresearch/segment-anything) [8 Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/TaskMatrix?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/facebookresearch/segment-anything?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Ultravox✨](https://github.com/fixie-ai/ultravox): A fast multimodal LLM for real-time voice [May 2024]
- [Understanding Multimodal LLMs✍️](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms):💡Two main approaches to building multimodal LLMs: 1. Unified Embedding Decoder Architecture approach; 2. Cross-modality Attention Architecture approach. [3 Nov 2024]    
  <img src="./files/mllm.png" width=400 alt="mllm" />  
- [Video-ChatGPT📑](https://alphaxiv.org/abs/2306.05424): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2306.05424)]: a video conversation model capable of generating meaningful conversation about videos. / [✨](https://github.com/mbzuai-oryx/Video-ChatGPT) [8 Jun 2023]
 ![**github stars**](https://img.shields.io/github/stars/mbzuai-oryx/Video-ChatGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Vision capability to a LLM [✍️](https://cloud.google.com/blog/products/ai-machine-learning/multimodal-generative-ai-search/): `The model has three sub-models`: A model to obtain image embeddings -> A text model to obtain text embeddings -> A model to learn the relationships between them [22 Aug 2023]


## **Survey and Reference**

### **Survey on Large Language Models**

#### **Overview: A Survey of LLMs**
  - [A Primer on Large Language Models and their Limitations📑](https://alphaxiv.org/abs/2412.04503): A primer on LLMs, their strengths, limits, applications, and research, for academia and industry use. [3 Dec 2024]
  - [A Survey of Large Language Models📑](https://alphaxiv.org/abs/2303.18223):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.18223)] [v1: 31 Mar 2023 - v15: 13 Oct 2024]
- [A Survey of NL2SQL with Large Language Models: Where are we, and where are we going?📑](https://alphaxiv.org/abs/2408.05109): [9 Aug 2024] [✨](https://github.com/HKUSTDial/NL2SQL_Handbook)
![**github stars**](https://img.shields.io/github/stars/HKUSTDial/NL2SQL_Handbook?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - [A Survey of Transformers📑](https://alphaxiv.org/abs/2106.04554):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2106.04554)] [8 Jun 2021]
- Google AI Research Recap
  - [Gemini✍️](https://blog.google/technology/ai/google-gemini-ai) [06 Dec 2023] Three different sizes: Ultra, Pro, Nano. With a score of 90.0%, Gemini Ultra is the first model to outperform human experts on MMLU [✍️](https://storage.googleapis.com/deepmind-media/gemini/gemini_1_report.pdf)
  - [Google AI Research Recap (2022 Edition)](https://ai.googleblog.com/2023/01/google-research-2022-beyond-language.html)
  - [Themes from 2021 and Beyond](https://ai.googleblog.com/2022/01/google-research-themes-from-2021-and.html)
  - [Looking Back at 2020, and Forward to 2021](https://ai.googleblog.com/2021/01/google-research-looking-back-at-2020.html)
  - [Large Language Models: A Survey📑](https://alphaxiv.org/abs/2402.06196): 🏆Well organized visuals and contents [9 Feb 2024]
- [LLM Post-Training: A Deep Dive into Reasoning Large Language Models📑](https://alphaxiv.org/abs/2502.21321): [✨](https://github.com/mbzuai-oryx/Awesome-LLM-Post-training) [28 Feb 2025]
- [LLM Research Papers: The 2024 List](https://sebastianraschka.com/blog/2024/llm-research-papers-the-2024-list.html) [29 Dec 2024]
- Microsoft Research Recap
  - [Research at Microsoft 2023✍️](https://www.microsoft.com/en-us/research/blog/research-at-microsoft-2023-a-year-of-groundbreaking-ai-advances-and-discoveries/): A year of groundbreaking AI advances and discoveries
- [Noteworthy LLM Research Papers of 2024](https://sebastianraschka.com/blog/2025/llm-research-2024.html) [23 Jan 2025]

#### **Additional Topics: A Survey of LLMs**

- [Advancing Reasoning in Large Language Models: Promising Methods and Approaches📑](https://alphaxiv.org/abs/2502.03671) [5 Feb 2025]
- [Agentic Retrieval-Augmented Generation: Agentic RAG📑](https://alphaxiv.org/abs/2501.09136) [15 Jan 2025]
- [AI Agent Protocols📑](https://alphaxiv.org/abs/2504.16736) [23 Apr 2025]
- [AI-Generated Content (AIGC)📑](https://alphaxiv.org/abs/2303.04226): A History of Generative AI from GAN to ChatGPT:[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.04226)] [7 Mar 2023]
- [AIOps in the Era of Large Language Models📑](https://alphaxiv.org/abs/2507.12472) [23 Jun 2025]
- [Aligned LLMs📑](https://alphaxiv.org/abs/2307.12966):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.12966)] [24 Jul 2023]
- [An Overview on Language Models: Recent Developments and Outlook📑](https://alphaxiv.org/abs/2303.05759):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.05759)] [10 Mar 2023]
- [A comprehensive taxonomy of hallucinations in Large Language Models📑](https://alphaxiv.org/abs/2508.01781) [3 Aug 2025]
- [Autonomous Scientific Discovery📑](https://alphaxiv.org/abs/2508.14111): From AI for Science to Agentic Science [18 Aug 2025]
- [Automatic Prompt Optimization Techniques📑](https://alphaxiv.org/abs/2502.16923) [24 Feb 2025]
- [Challenges & Application of LLMs📑](https://alphaxiv.org/abs/2306.07303):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2306.07303)] [11 Jun 2023]
- [ChatGPT’s One-year Anniversary: Are Open-Source Large Language Models Catching up?🔗](#section-12-evaluating-large-language-models--llmops) > Evaluation benchmark: Benchmarks and Performance of LLMs [28 Nov 2023]
- [Compression Algorithms for Language Models📑](https://alphaxiv.org/abs/2401.15347) [27 Jan 2024]
- [Context Engineering for Large Language Models📑](https://alphaxiv.org/abs/2507.13334) [17 Jul 2025]
- [Context Engineering 2.0](https://arxiv.org/abs/2510.26493) [30 Oct 2025]
- [Data Management For Large Language Models: A Survey📑](https://alphaxiv.org/abs/2312.01700) [4 Dec 2023]
- [Data Synthesis and Augmentation for Large Language Models📑](https://alphaxiv.org/abs/2410.12896) [16 Oct 2024]
- [Efficient Guided Generation for Large Language Models📑](https://alphaxiv.org/abs/2307.09702):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.09702)] [19 Jul 2023]
- [Efficient Training of Transformers📑](https://alphaxiv.org/abs/2302.01107):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2302.01107)] [2 Feb 2023]
- [Evaluation of Large Language Models📑](https://alphaxiv.org/abs/2307.03109):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.03109)] [6 Jul 2023]
- [Evaluating Large Language Models: A Comprehensive Survey📑](https://alphaxiv.org/abs/2310.19736):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.19736)] [30 Oct 2023]
- [Evaluation of LLM-based Agents📑](https://alphaxiv.org/abs/2503.16416) [20 Mar 2025]
- Evolutionary Tree of Large Language Models: [🔗](#evolutionary-tree-of-large-language-models)
- [Foundation Models in Vision📑](https://alphaxiv.org/abs/2307.13721):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.13721)] [25 Jul 2023]
- [From Google Gemini to OpenAI Q* (Q-Star)📑](https://alphaxiv.org/abs/2312.10868): Reshaping the Generative Artificial Intelligence (AI) Research Landscape:[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2312.10868)] [18 Dec 2023]
- [GUI Agents: A Survey📑](https://alphaxiv.org/abs/2412.13501) [18 Dec 2024]
- [Hallucination in LLMs📑](https://alphaxiv.org/abs/2311.05232):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2311.05232)] [9 Nov 2023]
- [Hallucination in Natural Language Generation📑](https://alphaxiv.org/abs/2202.03629):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2202.03629)] [8 Feb 2022]
- [Harnessing the Power of LLMs in Practice: ChatGPT and Beyond📑](https://alphaxiv.org/abs/2304.13712):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2304.13712)] [26 Apr 2023]
- [Harnessing the Reasoning Economy: Efficient Reasoning for Large Language Models📑](https://alphaxiv.org/abs/2503.24377): Efficient reasoning mechanisms that balance computational cost with performance. [31 Mar 2025]
- [In-context Learning📑](https://alphaxiv.org/abs/2301.00234):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2301.00234)] [31 Dec 2022]
- [Large Language Model-Brained GUI Agents: A Survey📑](https://alphaxiv.org/abs/2411.18279) [27 Nov 2024]
- [LLM-as-a-Judge📑](https://alphaxiv.org/abs/2411.15594) [23 Nov 2024]
- [LLM-based Autonomous Agents📑](https://alphaxiv.org/abs/2308.11432v1):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2308.11432v1)] [22 Aug 2023]
- [LLM-Driven AI Agent Communication: Protocols, Security Risks, and Defense Countermeasures📑](https://alphaxiv.org/abs/2506.19676) [24 Jun 2025]
- [LLMs for Healthcare📑](https://alphaxiv.org/abs/2310.05694):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.05694)] [9 Oct 2023]
- [Mathematical Reasoning in the Era of Multimodal Large Language Model: Benchmark, Method & Challenges📑](https://alphaxiv.org/abs/2412.11936) [16 Dec 2024]
- [Medical Reasoning in the Era of LLMs📑](https://alphaxiv.org/abs/2508.00669): A Systematic Review of Enhancement Techniques and Applications [1 Aug 2025]
- [Mixture of Experts📑](https://alphaxiv.org/abs/2407.06204) [26 Jun 2024]
- [Mitigating Hallucination in LLMs📑](https://alphaxiv.org/abs/2401.01313): Summarizes 32 techniques to mitigate hallucination in LLMs [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2401.01313)] [2 Jan 2024]
- [Model Compression for LLMs📑](https://alphaxiv.org/abs/2308.07633):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2308.07633)] [15 Aug 2023]
- [Multimodal Deep Learning📑](https://alphaxiv.org/abs/2301.04856):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2301.04856)] [12 Jan 2023]
- [Multimodal Large Language Models📑](https://alphaxiv.org/abs/2306.13549):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2306.13549)] [23 Jun 2023]
- [NL2SQL with Large Language Models: Where are we, and where are we going?📑](https://alphaxiv.org/abs/2408.05109): [9 Aug 2024] [✨](https://github.com/HKUSTDial/NL2SQL_Handbook)
![**github stars**](https://img.shields.io/github/stars/HKUSTDial/NL2SQL_Handbook?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Open Problems and Fundamental Limitations of Reinforcement Learning from Human Feedback📑](https://alphaxiv.org/abs/2307.15217):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.15217)] [27 Jul 2023]
- [Overview of Factuality in LLMs📑](https://alphaxiv.org/abs/2310.07521):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.07521)] [11 Oct 2023]
- [Position Paper: Agent AI Towards a Holistic Intelligence📑](https://alphaxiv.org/abs/2403.00833) [28 Feb 2024]
- [Post-training of Large Language Models📑](https://alphaxiv.org/abs/2503.06072) [8 Mar 2025]
- [Prompt Engineering Methods in Large Language Models for Different NLP Tasks📑](https://alphaxiv.org/abs/2407.12994) [17 Jul 2024]
- [Retrieval-Augmented Generation for Large Language Models: A Survey📑](https://alphaxiv.org/abs/2312.10997) [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2312.10997)] [18 Dec 2023]
- [Retrieval And Structuring Augmented Generation with Large Language Models📑](https://alphaxiv.org/abs/2509.10697) [12 Sep 2025]
- [Retrieval-Augmented Text Generation for Large Language Models📑](https://alphaxiv.org/abs/2404.10981) [17 Apr 2024]
- [Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning📑](https://alphaxiv.org/abs/2303.15647):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.15647)] [28 Mar 2023]
- [SEED-Bench: Benchmarking Multimodal LLMs with Generative Comprehension📑](https://alphaxiv.org/abs/2307.16125): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.16125)] [30 Jul 2023]
- [Self-Supervised Learning: A Cookbook of Self-Supervised Learning📑](https://alphaxiv.org/abs/2304.12210):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2304.12210)] [24 Apr 2023]
- [Small Language Models: Survey, Measurements, and Insights📑](https://alphaxiv.org/abs/2409.15790) [24 Sep 2024]
- [Small Language Models in the Era of Large Language Models📑](https://alphaxiv.org/abs/2411.03350) [4 Nov 2024]
- [Speed Always Wins: Efficient Architectures for Large Language Models](https://alphaxiv.org/abs/2508.09834) [13 Aug 2025]
- [Stop Overthinking: Efficient Reasoning for Large Language Models📑](https://alphaxiv.org/abs/2503.16419) [20 Mar 2025]
- [Summary of ChatGPT/GPT-4 Research and Perspective Towards the Future of Large Language Models📑](https://alphaxiv.org/abs/2304.01852):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2304.01852] [4 Apr 2023]
- [Tabular Data Understanding with LLMs: Recent Advances and Challenges](https://alphaxiv.org/abs/2508.00217) [31 Jul 2025]
- [Techniques for Optimizing Transformer Inference📑](https://alphaxiv.org/abs/2307.07982):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.07982)] [16 Jul 2023]
- [The Rise and Potential of Large Language Model Based Agents: A Survey📑](https://alphaxiv.org/abs/2309.07864) [14 Sep 2023]
- [Thinking Machines: LLM based Reasoning Strategies📑](https://alphaxiv.org/abs/2503.10814) [13 Mar 2025]
- [Towards Artificial General or Personalized Intelligence? 📑](https://alphaxiv.org/abs/2505.06907): Personalized federated intelligence (PFI). Foundation Model Meets Federated Learning [11 May 2025]
- [Towards Efficient Generative Large Language Model Serving: A Survey from Algorithms to Systems📑](https://alphaxiv.org/abs/2312.15234): The survey aims to provide a comprehensive understanding of the current state and future directions in efficient LLM serving [23 Dec 2023]
- [Trustworthy LLMs📑](https://alphaxiv.org/abs/2308.05374):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2308.05374)] [10 Aug 2023]
- [Universal and Transferable Adversarial Attacks on Aligned Language Models📑](https://alphaxiv.org/abs/2307.15043):[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.15043)] [27 Jul 2023]
- [What is the Role of Small Models in the LLM Era: A Survey📑](https://alphaxiv.org/abs/2409.06857) [10 Sep 2024]

#### **Business use cases**

- [AI-powered success—with more than 1,000 stories of customer transformation and innovation✍️](https://www.microsoft.com/en-us/microsoft-cloud/blog/2025/07/24/ai-powered-success-with-1000-stories-of-customer-transformation-and-innovation/)💡[24 July 2025]
- [Anthropic Clio✍️](https://www.anthropic.com/research/clio): Privacy-preserving insights into real-world AI use [12 Dec 2024]
- [Anthropic Economic Index✍️](https://www.anthropic.com/news/the-anthropic-economic-index): a research on the labor market impact of technologies. The usage is concentrated in software development and technical writing tasks. [10 Feb 2025]
- [Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence📑](https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf): early-career workers (ages 22–25) in AI-exposed jobs fell 13%, while older workers remained stable or grew. [26 Aug 2025]
- [Chatbot Interviewers Fill More Jobs✍️](https://www.deeplearning.ai/the-batch/study-shows-ai-agent-interviewers-improve-hiring-retention-in-customer-service-jobs/): Using chatbots as interviewers improves hiring efficiency and retention in customer service roles. [3 Sep 2025]
- [Examining the Use and Impact of an AI Code Assistant on Developer Productivity and Experience in the Enterprise📑](https://alphaxiv.org/abs/2412.06603): IBM study surveying developer experiences with watsonx Code Assistant (WCA). Most common use: code explanations (71.9%). Rated effective by 57.4%, ineffective by 42.6%. Many described WCA as similar to an “intern” or “junior developer.” [9 Dec 2024]
- [Future of Work with AI Agents: Auditing Automation and Augmentation Potential across the U.S. Workforce📑](https://alphaxiv.org/abs/2506.06576): A new framework maps U.S. workers’ preferences for AI automation vs. augmentation across 844 tasks.　It shows how people want AI to help or replace them. Many jobs need AI to support people, not just take over. [6 Jun 2025]
- [Google: 321 real-world gen AI use cases from the world's leading organizations✍️](https://blog.google/products/google-cloud/gen-ai-business-use-cases/) [19 Dec 2024]
- [Google: 60 of our biggest AI announcements in 2024✍️](https://blog.google/technology/ai/google-ai-news-recap-2024/) [23 Dec 2024]
- [How people are using ChatGPT✍️](https://openai.com/index/how-people-are-using-chatgpt/): OpenAI. Broadly adopted worldwide, mainly for advice (49%), task completion (40%), and creative expression (11%), with significant work-related use and rapid uptake in lower-income regions. [15 Sep 2025]
- [How real-world businesses are transforming with AI✍️](https://blogs.microsoft.com/blog/2024/11/12/how-real-world-businesses-are-transforming-with-ai/):💡Collected over 200 examples of how organizations are leveraging Microsoft’s AI capabilities. [12 Nov 2024]
- [Rapid Growth Continues for ChatGPT, Google’s NotebookLM](https://www.similarweb.com/blog/insights/ai-news/chatgpt-notebooklm/) [6 Nov 2024]
- [Senior Developers Ship nearly 2.5x more AI Code than Junior Counterparts✍️](https://www.fastly.com/blog/senior-developers-ship-more-ai-code): About a third of senior developers (10+ years of experience) say over half their shipped code is AI-generated [27 Aug 2025]
- [SignalFire State of Talent Report 2025](https://www.signalfire.com/blog/signalfire-state-of-talent-report-2025): 1. Entry‑level hiring down sharply since 2019 (-50%) 2. Anthropic dominate mid/senior talent retention 3. Roles labeled “junior” filled by seniors, blocking grads. [20 May 2025]
- State of AI
  - [Retool: Status of AI](https://retool.com/reports): A Report on AI In Production [2023](https://retool.com/reports/state-of-ai-2023) -> [2024](https://retool.com/blog/state-of-ai-h1-2024)
  - [The State of Generative AI in the Enterprise](https://menlovc.com/2023-the-state-of-generative-ai-in-the-enterprise-report/) [ⓒ2023]
    > 1. 96% of AI spend is on inference, not training. 2. Only 10% of enterprises pre-trained own models. 3. 85% of models in use are closed-source. 4. 60% of enterprises use multiple models.
  - [Standford AI Index Annual Report](https://aiindex.stanford.edu/report/)
  - [State of AI Report 2024](https://www.stateof.ai/2024) [10 Oct 2024]
  - [State of AI Report 2025](https://www.stateof.ai/2025-report-launch) [9 Oct 2025]
  - [LangChain > State of AI Agents](https://www.langchain.com/stateofaiagents) [19 Dec 2024]
- [The leading generative AI companies](https://iot-analytics.com/leading-generative-ai-companies/):💡GPU: Nvidia 92% market share, Generative AI foundational models and platforms: Microsoft 32% market share, Generative AI services: no single dominant [4 Mar 2025]
- [Trends – Artiﬁcial Intelligence](https://www.bondcap.com/report/pdf/Trends_Artificial_Intelligence.pdf):💡Issued by Bondcap VC. 340 Slides. ChatGPT’s 800 Million Users, 99% Cost Drop within 17 months. [May 2025]
- [Who is using AI to code? Global diffusion and impact of generative AI📑](https://alphaxiv.org/abs/2506.08945): AI wrote 30% of Python functions by U.S. devs in 2024. Adoption is uneven globally but boosts output and innovation. New coders use AI more, and usage drives $9.6–$14.4B in U.S. annual value. [10 Jun 2025]

### **Build an LLMs from scratch: picoGPT and lit-gpt**

- An unnecessarily tiny implementation of GPT-2 in NumPy. [picoGPT✨](https://github.com/jaymody/picoGPT): Transformer Decoder [Jan 2023]
 ![**github stars**](https://img.shields.io/github/stars/jaymody/picoGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
```python
q = x @ w_k # [n_seq, n_embd] @ [n_embd, n_embd] -> [n_seq, n_embd]
k = x @ w_q # [n_seq, n_embd] @ [n_embd, n_embd] -> [n_seq, n_embd]
v = x @ w_v # [n_seq, n_embd] @ [n_embd, n_embd] -> [n_seq, n_embd]

# In picoGPT, combine w_q, w_k and w_v into a single matrix w_fc
x = x @ w_fc # [n_seq, n_embd] @ [n_embd, 3*n_embd] -> [n_seq, 3*n_embd]
```
- [4 LLM Text Generation Strategies](https://blog.dailydoseofds.com/p/4-llm-text-generation-strategies): Greedy strategy, Multinomial sampling strategy, Beam search, Contrastive search [27 Sep 2025]
- [Andrej Karpathy📺](https://www.youtube.com/watch?v=l8pRSuU81PU): Reproduce the GPT-2 (124M) from scratch. [June 2024] / [SebastianRaschka📺](https://www.youtube.com/watch?v=kPGTx4wcm_w): Developing an LLM: Building, Training, Finetuning  [June 2024]
- Beam Search [1977] in Transformers is an inference algorithm that maintains the `beam_size` most probable sequences until the end token appears or maximum sequence length is reached. If `beam_size` (k) is 1, it's a `Greedy Search`. If k equals the total vocabularies, it's an `Exhaustive Search`. [🤗](https://huggingface.co/blog/constrained-beam-search) [Mar 2022]
- [Build a Large Language Model (From Scratch)✨](https://github.com/rasbt/LLMs-from-scratch):🏆Implementing a ChatGPT-like LLM from scratch, step by step
 ![**github stars**](https://img.shields.io/github/stars/rasbt/LLMs-from-scratch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Einsum is All you Need](https://rockt.ai/2018/04/30/einsum): Einstein Summation [5 Feb 2018] 
- lit-gpt: Hackable implementation of state-of-the-art open-source LLMs based on nanoGPT. Supports flash attention, 4-bit and 8-bit quantization, LoRA and LLaMA-Adapter fine-tuning, pre-training. Apache 2.0-licensed. [✨](https://github.com/Lightning-AI/lit-gpt) [Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/Lightning-AI/lit-gpt?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [llama3-from-scratch✨](https://github.com/naklecha/llama3-from-scratch): Implementing Llama3 from scratch [May 2024]
 ![**github stars**](https://img.shields.io/github/stars/naklecha/llama3-from-scratch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [llm.c✨](https://github.com/karpathy/llm.c): LLM training in simple, raw C/CUDA [Apr 2024]
 ![**github stars**](https://img.shields.io/github/stars/karpathy/llm.c?style=flat-square&label=%20&color=blue&cacheSeconds=36000) | Reproducing GPT-2 (124M) in llm.c in 90 minutes for $20 [✨](https://github.com/karpathy/llm.c/discussions/481)
- [nanochat✨](https://github.com/karpathy/nanochat): a full-stack implementation of an LLM [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/karpathy/nanochat?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
- [nanoGPT✨](https://github.com/karpathy/nanoGPT):💡Andrej Karpathy [Dec 2022] | [nanoMoE✨](https://github.com/wolfecameron/nanoMoE) [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/karpathy/nanoGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/wolfecameron/nanoMoE?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [nanoVLM✨](https://github.com/huggingface/nanoVLM): 🤗 The simplest, fastest repository for training/finetuning small-sized VLMs. [May 2025]
- [pix2code✨](https://github.com/tonybeltramelli/pix2code): Generating Code from a Graphical User Interface Screenshot. Trained dataset as a pair of screenshots and simplified intermediate script for HTML, utilizing image embedding for CNN and text embedding for LSTM, encoder and decoder model. Early adoption of image-to-code. [May 2017] ![**github stars**](https://img.shields.io/github/stars/tonybeltramelli/pix2code?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
- [Screenshot to code✨](https://github.com/emilwallner/Screenshot-to-code): Turning Design Mockups Into Code With Deep Learning [Oct 2017] [✍️](https://blog.floydhub.com/turning-design-mockups-into-code-with-deep-learning/) ![**github stars**](https://img.shields.io/github/stars/emilwallner/Screenshot-to-code?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Spreadsheets-are-all-you-need✨](https://github.com/ianand/spreadsheets-are-all-you-need): Spreadsheets-are-all-you-need implements the forward pass of GPT2 entirely in Excel using standard spreadsheet functions. [Sep 2023]
 ![**github stars**](https://img.shields.io/github/stars/ianand/spreadsheets-are-all-you-need?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Transformer Explainer](https://alphaxiv.org/pdf/2408.04619): an open-source interactive tool to learn about the inner workings of a Transformer model (GPT-2) [✨](https://poloclub.github.io/transformer-explainer/) [8 Aug 2024]
- [Umar Jamil github✨](https://github.com/hkproj):💡LLM Model explanation / building a model from scratch [📺](https://www.youtube.com/@umarjamilai)
- [You could have designed state of the art positional encoding](https://fleetwood.dev/posts/you-could-have-designed-SOTA-positional-encoding): Binary Position Encoding, Sinusoidal positional encoding, Absolute vs Relative Position Encoding, Rotary Positional encoding [17 Nov 2024]

#### Classification of Attention

1. Soft Attention: Assigns continuous weights to all inputs; differentiable and widely used (e.g., neural machine translation).
1. Hard Attention: Selects discrete subsets of inputs; non-differentiable, often trained with reinforcement learning (e.g., image captioning).
1. Global Attention: Attends to all input tokens, capturing long-range dependencies; suitable for shorter sequences due to cost.
1. Local Attention: Restricts focus to a region around each token; balances efficiency and context (e.g., time series).
1. Self-Attention: Each token attends to other tokens in the same sequence; core to models like BERT.
1. Multi-Head Self-Attention: Runs several self-attentions in parallel to capture diverse relations; essential for Transformers.
1. Sparse Attention: Computes only a subset of similarity scores (e.g., strided, fixed); enables scaling to very long sequences (see *Performer*).
1. Cross-Attention: Attends between two sequences (e.g., encoder–decoder in machine translation).
1. Sliding Window Attention (SWA): Used in **Longformer**; each token attends within a fixed-size local window, reducing memory use for long texts.
- [✍️](https://blog.research.google/2020/10/rethinking-attention-with-performers.html) [23 Oct 2020] / [✍️](https://vaclavkosar.com/ml/cross-attention-in-transformer-architecture) / [✍️](https://sebastianraschka.com/blog/2023/self-attention-from-scratch.html) [9 Feb 2023]  / [✨](https://github.com/mistralai/mistral-src#sliding-window-to-speed-up-inference-and-reduce-memory-pressure)
- [Efficient Streaming Language Models with Attention Sinks](http://alphaxiv.org/abs/2309.17453): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.17453)] 1. StreamingLLM, an efficient framework that enables LLMs trained with a finite length attention window to generalize to infinite sequence length without any fine-tuning. 2. We neither expand the LLMs' context window nor enhance their long-term memory. [✨](https://github.com/mit-han-lab/streaming-llm) [29 Sep 2023]
 ![**github stars**](https://img.shields.io/github/stars/mit-han-lab/streaming-llm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

  <img src="./files/streaming-llm.png" alt="streaming-attn"/>

  - Key-Value (KV) cache is an important component in the StreamingLLM framework.

  1. Window Attention: Only the most recent Key and Value states (KVs) are cached. This approach fails when the text length surpasses the cache size.
  2. Sliding Attention /w Re-computation: Rebuilds the Key-Value (KV) states from the recent tokens for each new token. Evicts the oldest part of the cache.
  3. StreamingLLM: One of the techniques used is to add a placeholder token (yellow-colored) as a dedicated attention sink during pre-training. This attention sink attracts the model’s attention and helps it generalize to longer sequences. Outperforms the sliding window with re-computation baseline by up to a remarkable 22.2× speedup.

- LongLoRA

  1. [LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models📑](https://alphaxiv.org/abs/2309.12307): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.12307)]: A combination of sparse local attention and LoRA [✨](https://github.com/dvlab-research/LongLoRA) [21 Sep 2023]
 ![**github stars**](https://img.shields.io/github/stars/dvlab-research/LongLoRA?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

  - Key Takeaways from LongLora <br/>
    <img src="./files/longlora.png" alt="long-lora" width="350"/>
    1. The document states that LoRA alone is not sufficient for long context extension.
    1. Although dense global attention is needed during inference, fine-tuning the model can be done by sparse local attention, shift short attention (S2-Attn).
    1. S2-Attn can be implemented with only two lines of code in training.
<!--   2. [QA-LoRA📑](https://alphaxiv.org/abs/2309.14717): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.14717)]: Quantization-Aware Low-Rank Adaptation of Large Language Models. A method that integrates quantization and low-rank adaptation for large language models. [✨](https://github.com/yuhuixu1993/qa-lora) [26 Sep 2023]
 ![**github stars**](https://img.shields.io/github/stars/yuhuixu1993/qa-lora?style=flat-square&label=%20&color=blue&cacheSeconds=36000) -->
- [4 Advanced Attention Mechanisms🤗](https://huggingface.co/blog/Kseniase/attentions) [4 Apr 2025]
  1. Slim Attention: Stores only keys (K) during decoding and reconstructs values (V) from K when needed, reducing memory usage. -> Up to 2x memory savings, faster inference. Slight compute overhead from reconstructing V.
  1. XAttention: Uses a sparse block attention pattern with antidiagonal alignment to ensure better coverage and efficiency. -> Preserves accuracy, boosts speed (up to 13x faster). Requires careful design of block-sparse layout.
  1. KArAt (Kolmogorov-Arnold Attention): Replaces the fixed softmax attention with a learnable function (based on Kolmogorov–Arnold representation) to better model dependencies. -> Highly expressive, adaptable to complex patterns. Higher compute cost, less mature tooling.
  1. MTA (Multi-Token Attention): Instead of attending token-by-token, it updates *groups* of tokens together, reducing the frequency of attention calls. -> Better for tasks where context spans across groups. Introduces grouping complexity, may hurt granularity.

### **LLM Materials for East Asian Languages**

#### Japanese

- [ChatGPTやCopilotなど各種生成AI用の日本語の Prompt のサンプル✨](https://github.com/dahatake/GenerativeAI-Prompt-Sample-Japanese) [Apr 2023]
- [LLM 研究プロジェクト✍️](https://blog.brainpad.co.jp/entry/2023/07/27/153006): ブログ記事一覧 [27 Jul 2023]
- [ブレインパッド社員が投稿した Qiita 記事まとめ✍️](https://blog.brainpad.co.jp/entry/2023/07/27/153055): ブレインパッド社員が投稿した Qiita 記事まとめ [Jul 2023]
- [rinna🤗](https://huggingface.co/rinna): rinna の 36 億パラメータの日本語 GPT 言語モデル: 3.6 billion parameter Japanese GPT language model [17 May 2023]
- [rinna: bilingual-gpt-neox-4b🤗](https://huggingface.co/rinna/bilingual-gpt-neox-4b): 日英バイリンガル大規模言語モデル [17 May 2023]
- [法律:生成 AI の利用ガイドライン](https://storialaw.jp/blog/9414): Legal: Guidelines for the Use of Generative AI
- [New Era of Computing - ChatGPT がもたらした新時代✍️](https://speakerdeck.com/dahatake/new-era-of-computing-chatgpt-gamotarasitaxin-shi-dai-3836814a-133a-4879-91e4-1c036b194718) [May 2023]
- [大規模言語モデルで変わる ML システム開発✍️](https://speakerdeck.com/hirosatogamo/da-gui-mo-yan-yu-moderudebian-warumlsisutemukai-fa): ML system development that changes with large-scale language models [Mar 2023]
- [GPT-4 登場以降に出てきた ChatGPT/LLM に関する論文や技術の振り返り✍️](https://blog.brainpad.co.jp/entry/2023/06/05/153034): Review of ChatGPT/LLM papers and technologies that have emerged since the advent of GPT-4 [Jun 2023]
- [LLM を制御するには何をするべきか？✍️](https://blog.brainpad.co.jp/entry/2023/06/08/161643): How to control LLM [Jun 2023]
- [1. 生成 AI のマルチモーダルモデルでできること✍️](https://blog.brainpad.co.jp/entry/2023/06/06/160003): What can be done with multimodal models of generative AI [2. 生成 AI のマルチモーダリティに関する技術調査✍️](https://blog.brainpad.co.jp/entry/2023/10/18/153000) [Jun 2023]
- [LLM の推論を効率化する量子化技術調査✍️](https://blog.brainpad.co.jp/entry/2023/09/01/153003): Survey of quantization techniques to improve efficiency of LLM reasoning [Sep 2023]
- [LLM の出力制御や新モデルについて✍️](https://blog.brainpad.co.jp/entry/2023/09/08/155352): About LLM output control and new models [Sep 2023]
- [Azure OpenAI を活用したアプリケーション実装のリファレンス✨](https://github.com/Azure-Samples/jp-azureopenai-samples): 日本マイクロソフト リファレンスアーキテクチャ [Jun 2023]
 ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/jp-azureopenai-samples?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [生成 AI・LLM のツール拡張に関する論文の動向調査✍️](https://blog.brainpad.co.jp/entry/2023/09/22/150341): Survey of trends in papers on tool extensions for generative AI and LLM [Sep 2023]
- [LLM の学習・推論の効率化・高速化に関する技術調査✍️](https://blog.brainpad.co.jp/entry/2023/09/28/170010): Technical survey on improving the efficiency and speed of LLM learning and inference [Sep 2023]
- [日本語LLMまとめ - Overview of Japanese LLMs✨](https://github.com/llm-jp/awesome-japanese-llm): 一般公開されている日本語LLM（日本語を中心に学習されたLLM）および日本語LLM評価ベンチマークに関する情報をまとめ [Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/llm-jp/awesome-japanese-llm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure OpenAI Service で始める ChatGPT/LLM システム構築入門✨](https://github.com/shohei1029/book-azureopenai-sample): サンプルプログラム [Aug 2023]
 ![**github stars**](https://img.shields.io/github/stars/shohei1029/book-azureopenai-sample?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure OpenAI と Azure Cognitive Search の組み合わせを考える](https://qiita.com/nohanaga/items/59e07f5e00a4ced1e840) [24 May 2023]
- [Matsuo Lab](https://weblab.t.u-tokyo.ac.jp/en/): 人工知能・深層学習を学ぶためのロードマップ [✍️](https://weblab.t.u-tokyo.ac.jp/人工知能・深層学習を学ぶためのロードマップ/) / [🗄️](./files/archive/Matsuo_Lab_LLM_2023_Slide_pdf.7z) [Dec 2023]
- [AI事業者ガイドライン](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/) [Apr 2024]
- [LLMにまつわる"評価"を整理する✍️](https://zenn.dev/seya/articles/dd0010601b3136) [06 Jun 2024]
- [コード生成を伴う LLM エージェント✍️](https://speakerdeck.com/smiyawaki0820)  [18 Jul 2024]
- [Japanese startup Orange uses Anthropic's Claude to translate manga into English✍️](https://www.technologyreview.com/2024/12/02/1107562/this-manga-publisher-is-using-anthropics-ai-to-translate-japanese-comics-into-english/): [02 Dec 2024]
- [AWS で実現する安全な生成 AI アプリケーション – OWASP Top 10 for LLM Applications 2025 の活用例✍️](https://aws.amazon.com/jp/blogs/news/secure-gen-ai-applications-on-aws-refer-to-owasp-top-10-for-llm-applications/) [31 Jan 2025]

#### Korean

- [Machine Learning Study 혼자 해보기✨](https://github.com/teddylee777/machine-learning) [Sep 2018]
 ![**github stars**](https://img.shields.io/github/stars/teddylee777/machine-learning?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LangChain 한국어 튜토리얼✨](https://github.com/teddylee777/langchain-kr) [Feb 2024]
 ![**github stars**](https://img.shields.io/github/stars/teddylee777/langchain-kr?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [AI 데이터 분석가 ‘물어보새’ 등장 – RAG와 Text-To-SQL 활용✍️](https://techblog.woowahan.com/18144/) [Jul 2024]
- [LLM, 더 저렴하게, 더 빠르게, 더 똑똑하게✍️](https://tech.kakao.com/posts/633) [09 Sep 2024]
- [생성형 AI 서비스: 게이트웨이로 쉽게 시작하기✍️](https://techblog.woowahan.com/19915/) [07 Nov 2024]
- [Harness를 이용해 LLM 애플리케이션 평가 자동화하기✍️](https://techblog.lycorp.co.jp/ko/automating-llm-application-evaluation-with-harness) [16 Nov 2024]
- [모두를 위한 LLM 애플리케이션 개발 환경 구축 사례✍️](https://techblog.lycorp.co.jp/ko/building-a-development-environment-for-llm-apps-for-everyone)  [7 Feb 2025]
- [LLM 앱의 제작에서 테스트와 배포까지, LLMOps 구축 사례 소개✍️](https://techblog.lycorp.co.jp/ko/building-llmops-for-creating-testing-deploying-of-llm-apps) [14 Feb 2025]
- [Kanana✨](https://github.com/kakao/kanana): Kanana, a series of bilingual language models (developed by Kakao) [26 Feb 2025]
- [HyperCLOVA X SEED🤗](https://huggingface.co/collections/naver-hyperclovax): Lightweight open-source lineup with a strong focus on Korean language [23 Apr 2025]
- [문의 대응을 효율화하기 위한 RAG 기반 봇 도입하기✍️](https://techblog.lycorp.co.jp/ko/rag-based-bot-for-streamlining-inquiry-responses) [23 May 2025]

### **Learning and Supplementary Materials**

- [AI by Hand | Special Lecture - DeepSeek](https://www.youtube.com/watch?v=idF6TiTGYsE):🏆MoE, Latent Attention implemented in DeepSeek [✨](https://github.com/ImagineAILab/ai-by-hand-excel) [30 Jan 2025]
- [AI-Crash-Course✨](https://github.com/henrythe9th/AI-Crash-Course): AI Crash Course to help busy builders catch up to the public frontier of AI research in 2 weeks [Jan 2025]
- [Anti-hype LLM reading list](https://gist.github.com/veekaybee/be375ab33085102f9027853128dc5f0e)
- [Attention Is All You Need](https://alphaxiv.org/pdf/1706.03762.pdf): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+1706.03762)]: 🏆 The Transformer,
  based solely on attention mechanisms, dispensing with recurrence and convolutions
  entirely. [12 Jun 2017] [Illustrated transformer](http://jalammar.github.io/illustrated-transformer/)
- [Best-of Machine Learning with Python✨](https://github.com/ml-tooling/best-of-ml-python):🏆A ranked list of awesome machine learning Python libraries. [Nov 2020]
 ![**github stars**](https://img.shields.io/github/stars/ml-tooling/best-of-ml-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [But what is a GPT?📺](https://www.youtube.com/watch?v=wjZofJX0v4M)🏆3blue1brown: Visual intro to transformers [Apr 2024]
- [CNN Explainer: Learning Convolutional Neural Networks with Interactive Visualization✨](https://github.com/poloclub/cnn-explainer) [Apr 2020]
 ![**github stars**](https://img.shields.io/github/stars/poloclub/cnn-explainer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Comparing Adobe Firefly, Dalle-2, OpenJourney, Stable Diffusion, and Midjourney✍️](https://blog.usmanity.com/comparing-adobe-firefly-dalle-2-and-openjourney/): Generative AI for images [20 Jun 2023]
- [DAIR.AI✨](https://github.com/dair-ai):💡Machine learning & NLP research ([omarsar github✨](https://github.com/omarsar))
  - [ML Papers of The Week✨](https://github.com/dair-ai/ML-Papers-of-The-Week) [Jan 2023] | [✍️](https://nlp.elvissaravia.com/): NLP Newsletter
 ![**github stars**](https://img.shields.io/github/stars/dair-ai/ML-Papers-of-the-Week?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Daily Dose of Data Science✨](https://github.com/ChawlaAvi/Daily-Dose-of-Data-Science) [Dec 2022]
 ![**github stars**](https://img.shields.io/github/stars/ChawlaAvi/Daily-Dose-of-Data-Science?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Deep Learning cheatsheets for Stanford's CS 230✨](https://github.com/afshinea/stanford-cs-230-deep-learning/tree/master/en): Super VIP Cheetsheet: Deep Learning [Nov 2019]
- [DeepLearning.ai Short courses](https://www.deeplearning.ai/short-courses/): DeepLearning.ai Short courses [2023]
- [eugeneyan blog](https://eugeneyan.com/start-here/):💡Lessons from A year of Building with LLMs, Patterns for LLM Systems. [✨](https://github.com/eugeneyan/applied-ml) ![**github stars**](https://img.shields.io/github/stars/eugeneyan/applied-ml?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Foundational concepts like Transformers, Attention, and Vector Database](https://www.linkedin.com/posts/alphasignal_can-foundational-concepts-like-transformers-activity-7163890641054232576-B1ai) [Feb 2024]
- [Foundations of Large Language Models📑](https://alphaxiv.org/abs/2501.09223): a book about large language models: pre-training, generative models, prompting techniques, and alignment methods. [16 Jan 2025]
- [gpt4free✨](https://github.com/xtekky/gpt4free) for educational purposes only [Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/xtekky/gpt4free?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Hundred-Page Language Models Book by Andriy Burkov✨](https://github.com/aburkov/theLMbook) [15 Jan 2025]
- [IbrahimSobh/llms✨](https://github.com/IbrahimSobh/llms): Language models introduction with simple code. [Jun 2023]
 ![**github stars**](https://img.shields.io/github/stars/IbrahimSobh/llms?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Large Language Model Course✨](https://github.com/mlabonne/llm-course): Course to get into Large Language Models (LLMs) with roadmaps and Colab notebooks. [Jun 2023]
 ![**github stars**](https://img.shields.io/github/stars/mlabonne/llm-course?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Large Language Models: Application through Production✨](https://github.com/databricks-academy/large-language-models): A course on edX & Databricks Academy
 ![**github stars**](https://img.shields.io/github/stars/databricks-academy/large-language-models?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLM FineTuning Projects and notes on common practical techniques✨](https://github.com/rohan-paul/LLM-FineTuning-Large-Language-Models) [Oct 2023]
 ![**github stars**](https://img.shields.io/github/stars/rohan-paul/LLM-FineTuning-Large-Language-Models?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLM Visualization](https://bbycroft.net/llm): A 3D animated visualization of an LLM with a walkthrough
- [Machine learning algorithms✨](https://github.com/rushter/MLAlgorithms): ml algorithms or implementation from scratch [Oct 2016] ![**github stars**](https://img.shields.io/github/stars/rushter/MLAlgorithms?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Must read: the 100 most cited AI papers in 2022](https://www.zeta-alpha.com/post/must-read-the-100-most-cited-ai-papers-in-2022) : [🗄️](./files/top-cited-2020-2021-2022-papers.pdf) [8 Mar 2023]
- [Open Problem and Limitation of RLHF📑](https://alphaxiv.org/abs/2307.15217): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.15217)]: Provides an overview of open problems and the limitations of RLHF [27 Jul 2023]
<!-- - [Ai Fire](https://www.aifire.co/c/ai-learning-resources): AI Fire Learning resources [🗄️](./files/aifire.pdf) [2023] -->
- [OpenAI Cookbook✨](https://github.com/openai/openai-cookbook) Examples and guides for using the OpenAI API
 ![**github stars**](https://img.shields.io/github/stars/openai/openai-cookbook?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [oumi: Open Universal Machine Intelligence✨](https://github.com/oumi-ai/oumi): Everything you need to build state-of-the-art foundation models, end-to-end. [Oct 2024]
- [The Best Machine Learning Resources](https://medium.com/machine-learning-for-humans/how-to-learn-machine-learning-24d53bb64aa1) : [🗄️](./files/ml_rsc.pdf) [20 Aug 2017]
- [The Big Book of Large Language Models](https://book.theaiedge.io/) by Damien Benveniste [30 Jan 2025]
- [The Illustrated GPT-OSS](https://newsletter.languagemodels.co/p/the-illustrated-gpt-oss) [19 Aug 2025]
- [What are the most influential current AI Papers?📑](https://alphaxiv.org/abs/2308.04889): NLLG Quarterly arXiv Report 06/23 [✨](https://github.com/NL2G/Quaterly-Arxiv) [31 Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/NL2G/Quaterly-Arxiv?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [The Illustrated GPT-OSS](https://newsletter.languagemodels.co/p/the-illustrated-gpt-oss) [19 Aug 2025]


## **General AI Tools and Extensions**

- [5 LLM-based Apps for Developers](https://hackernoon.com/5-llm-based-apps-for-developers): Github Copilot, Cursor IDE, Tabnine, Warp, Replit Agent
- AI Search engine:
  1. [Phind](https://www.phind.com/search): AI-Powered Search Engine for Developers [July 2022]
  1. [Perplexity](http://perplexity.ai) [Dec 2022]
    - [Perplexity comet](https://www.perplexity.ai/comet): agentic browser [9 Jul 2025]
  1. [GenSpark](https://www.genspark.ai/): AI agents engine perform research and generate custom pages called Sparkpages. [18 Jun 2024]
  1. [felo.ai](https://felo.ai/search): Sparticle Inc. in Tokyo, Japan [04 Sep 2024]
  1. [Goover](https://goover.ai/) 
  1. [oo.ai](https://oo.ai): Open Research. Fastest AI Search.
- AI Tools: <https://aitoolmall.com/>
- [Ai2 Playground](https://playground.allenai.org/)
- Airtable list: [Generative AI Index](https://airtable.com/appssJes9NF1i5xCn/shrH4REIgddv8SzUo/tbl5dsXdD1P859QLO) | [AI Startups](https://airtable.com/appSpVXpylJxMZiWS/shr6nfE9FOHp17IjG/tblL3ekHZfkm3p6YT)
- [AlphaXiv](https://www.alphaxiv.org): an interactive extension of arXiv
- [AniDoc✨](https://github.com/yihao-meng/AniDoc): Animation Creation Made Easier [✍️](https://yihao-meng.github.io/AniDoc_demo/) ![**github stars**](https://img.shields.io/github/stars/yihao-meng/AniDoc?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Cherry Studio✨](https://github.com/CherryHQ/cherry-studio): a desktop client that supports multiple LLM providers. ![**github stars**](https://img.shields.io/github/stars/CherryHQ/cherry-studio?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Content writing: <http://jasper.ai/chat> / [🗣️](https://twitter.com/slow_developer/status/1671530676045094915)
- [Duck.ai](https://www.duck.ai/):💡Private, Useful, and Optional AI: DuckDuckGo offers free access to popular AI chatbots at Duck.ai
- Edge and Chrome Extension & Plugin
  - [MaxAI.me](https://www.maxai.me/)
  - [BetterChatGPT✨](https://github.com/ztjhz/BetterChatGPT)
 ![**github stars**](https://img.shields.io/github/stars/ztjhz/BetterChatGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - [ChatHub✨](https://github.com/chathub-dev/chathub) All-in-one chatbot client [Webpage](https://chathub.gg/)
 ![**github stars**](https://img.shields.io/github/stars/chathub-dev/chathub?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - [ChatGPT Retrieval Plugin✨](https://github.com/openai/chatgpt-retrieval-plugin)
 ![**github stars**](https://img.shields.io/github/stars/openai/chatgpt-retrieval-plugin?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [FLORA](https://www.florafauna.ai/): an AI platform integrating text, image, and video models into a unified canvas.
- Future Tools: <https://www.futuretools.io/>
- [God Tier Prompts](https://www.godtierprompts.com): A community driven leaderboard where the best prompts rise to the top.
- Open Source Image Creation Tool
  1. ComfyUI - https://github.com/comfyanonymous/ComfyUI
  1. Stable Diffusion web UI - https://github.com/AUTOMATIC1111/stable-diffusion-webui
- [INFP: Audio-Driven Interactive Head Generation in Dyadic Conversations](https://grisoon.github.io/INFP/) [ref📑](https://alphaxiv.org/abs/2412.04037) [5 Dec 2024]
- [MGX (MetaGPT X)](https://mgx.dev/): Multi-agent collaboration platform to develop an application.
- [Msty](https://msty.app/):💡The easiest way to use local and online AI models
- [napkin.ai](https://www.napkin.ai/): a text-to-visual graphics generator [7 Aug 2024]
- Newsletters & Tool Databas: <https://www.therundown.ai/>
- Open Source No-Code AI Tools
  1. Anything-LLM — https://anythingllm.com
  1. Budibase — https://budibase.com
  1. Coze Studio — https://www.coze.com
  1. Dify — https://dify.ai
  1. Flowise — https://flowiseai.com
  1. n8n — https://n8n.io
  1. NocoBase — https://www.nocobase.com
  1. NocoDB — https://nocodb.com
  1. Sim — https://www.sim.ai
  1. Strapi — https://strapi.io
  1. ToolJet — https://www.tooljet.ai
- Oceans of AI - All AI Tools <https://play.google.com/store/apps/details?id=in.blueplanetapps.oceansofai&hl=en_US>
- Open source (huggingface):🤗<http://huggingface.co/chat>
- [Pika AI - Free AI Video Generator](https://pika.art/login)
- [Product Hunt > AI](https://www.producthunt.com/categories/ai)
- [Quora Poe](https://poe.com/login) A chatbot service that gives access to GPT-4, gpt-3.5-turbo, Claude from Anthropic, and a variety of other bots. [Feb 2023]
- [recraft.ai](https://www.recraft.ai/): Text-to-editable vector image generator
- [Same.dev](https://same.new/): Clone Any Website in Minutes
- [skywork.ai](https://skywork.ai): Deep Research is a multimodal generalist agent that can create documents, slides, and spreadsheets.
- [Smartsub](https://smartsub.ai/): AI-powered transcription, translation, and subtitle creation
- [TEXT-TO-CAD](https://zoo.dev/text-to-cad): Generate CAD from text prompts
- The leader: <http://openai.com>
- The runner-up: <http://bard.google.com> -> <https://gemini.google.com>
- Toolerific.ai: <https://toolerific.ai/>: Find the best AI tools for your tasks
- [Vercel AI](https://sdk.vercel.ai/) Vercel AI Playground / Vercel AI SDK [✨](https://github.com/vercel/ai) [May 2023]
 ![**github stars**](https://img.shields.io/github/stars/vercel/ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [websim.ai](https://websim.ai/): a web editor and simulator that can generate websites. [1 Jul 2024]
- allAIstartups: <https://www.allaistartups.com/ai-tools>

## **Datasets for LLM Training**

- LLM-generated datasets:
  1. [Self-Instruct📑](https://alphaxiv.org/abs/2212.10560): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2212.10560)]: Seed task pool with a set of human-written instructions. [20 Dec 2022]
  1. [Self-Alignment with Instruction Backtranslation📑](https://alphaxiv.org/abs/2308.06259): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2308.06259)]: Without human seeding, use LLM to produce instruction-response pairs. The process involves two steps: self-augmentation and self-curation. [11 Aug 2023]
- [LLMDataHub: Awesome Datasets for LLM Training✨](https://github.com/Zjh-819/LLMDataHub): A quick guide (especially) for trending instruction finetuning datasets
 ![**github stars**](https://img.shields.io/github/stars/Zjh-819/LLMDataHub?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Open LLMs and Datasets✨](https://github.com/eugeneyan/open-llms): A list of open LLMs available for commercial use.
 ![**github stars**](https://img.shields.io/github/stars/eugeneyan/open-llms?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/): The Stanford Question Answering Dataset (SQuAD), a set of Wikipedia articles, 100,000+ question-answer pairs on 500+ articles. [16 Jun 2016]
- [Synthetic Data Vault (SDV) ✨](https://github.com/sdv-dev/SDV): Synthetic data generation for tabular data [May 2018] ![**github stars**](https://img.shields.io/github/stars/sdv-dev/SDV?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [RedPajama](https://together.ai/blog/redpajama): LLaMA training dataset of over 1.2 trillion tokens [✨](https://github.com/togethercomputer/RedPajama-Data) [17 Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/togethercomputer/RedPajama-Data?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [FineWeb🤗](https://huggingface.co/datasets/HuggingFaceFW/fineweb):🤗HuggingFace. crawled 15 trillion tokens of high-quality web data from the summer of 2013 to March 2024. [Apr 2024]
- [MS MARCO Web Search✨](https://github.com/microsoft/MS-MARCO-Web-Search): A large-scale information-rich web dataset, featuring millions of real clicked query-document labels [Apr 2024]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/MS-MARCO-Web-Search?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Nemotron-Personas-Japan: Synthesized Data for Sovereign AI🤗](https://huggingface.co/blog/nvidia/nemotron-personas-japan): The first open synthetic dataset that captures Japan's demographic, geographic, and cultural spectrum.  [23 Sep 2025]
- [Synthetic Data of LLMs✨](https://github.com/wasiahmad/Awesome-LLM-Synthetic-Data): A reading list on LLM based Synthetic Data Generation [Oct 2024]
 ![**github stars**](https://img.shields.io/github/stars/wasiahmad/Awesome-LLM-Synthetic-Data?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Open Thoughts✨](https://github.com/open-thoughts/open-thoughts): Fully Open Data Curation for Thinking Models [28 Jan 2025] ![**github stars**](https://img.shields.io/github/stars/open-thoughts/open-thoughts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

Pretrain for a base model

```json
{
    "text": ...,
    "meta": {"url": "...", "timestamp": "...", "source": "...", "language": "...", ...},
    "red_pajama_subset": "common_crawl" | "c4" | "github" | "books" | "arxiv" | "wikipedia" | "stackexchange"
}
```

databricks-dolly-15k: Instruction-Tuned [✨🤗](https://huggingface.co/datasets/databricks/databricks-dolly-15k): SFT training - QA pairs or Dialog

```json
{
  "prompt": "What is the capital of France?",
  "response": "The capital of France is Paris."
},
{
    "prompt": "Can you give me a recipe for chocolate chip cookies?",
    "response": "Sure! ..."
}
```

[Anthropic human-feedback✨🤗](https://huggingface.co/datasets/Anthropic/hh-rlhf): RLHF training - Chosen and Rejected pairs

```json
{
  "chosen": "I'm sorry to hear that. Is there anything I can do to help?",
  "rejected": "That's too bad. You should just get over it."
}
```

<!-- - [大規模言語モデルのデータセットまとめ](https://note.com/npaka/n/n686d987adfb1): 大規模言語モデルのデータセットまとめ [Apr 2023] -->
- Dataset example

  [🗣️](https://docs.argilla.io/)

  ### SFT Dataset

  | Category | Instruction | Context | Response |
  | --- | --- | --- | --- |
  | 0 | Open QA | How do I get rid of mosquitos in my house? | You can get rid of mosquitos in your house by ... |
  | 1 | Classification | Classify each country as "African" or "European" | Nigeria: African<br>Rwanda: African<br>Portugal: European |
  | 2 | Information Extraction | Extract the unique names of composers from the text. | To some extent, European and the US traditions... Pierre Boulez, Luigi Nono, Karlheinz Stockhausen |
  | 3 | General QA | Should investors time the market? | Timing the market is based on predictions of t... |

  ### RLHF Dataset

  | Instruction | Chosen Response | Rejected Response |
  | --- | --- | --- |
  | What is Depreciation | Depreciation is the drop in value of an asset ... | What is Depreciation – 10 Important Facts to K... |
  | What do you know about the city of Aberdeen in Scotland? | Aberdeen is a city located in the North East of Scotland. It is known for its granite architecture and its offshore oil industry. | As an AI language model, I don't have personal knowledge or experiences about Aberdeen. |
  | Describe thunderstorm season in the United States and Canada. | Thunderstorm season in the United States and Canada typically occurs during the spring and summer months, when warm, moist air collides with cooler, drier air, creating the conditions for thunderstorms to form. | Describe thunderstorm season in the United States and Canada. |
  

## **Evaluating Large Language Models & LLMOps**

### **Evaluating Large Language Models**

- [Artificial Analysis LLM Performance Leaderboard🤗](https://huggingface.co/spaces/ArtificialAnalysis/LLM-Performance-Leaderboard): Performance benchmarks & pricing across API providers of LLMs
- Awesome LLMs Evaluation Papers: Evaluating Large Language Models: A Comprehensive Survey [✨](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) [Oct 2023]
 ![**github stars**](https://img.shields.io/github/stars/tjunlp-lab/Awesome-LLMs-Evaluation-Papers?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Can Large Language Models Be an Alternative to Human Evaluations?📑](https://alphaxiv.org/abs/2305.01937) [3 May 2023]
- [ChatGPT’s One-year Anniversary: Are Open-Source Large Language Models Catching up?📑](https://alphaxiv.org/abs/2311.16989): Open-Source LLMs vs. ChatGPT; Benchmarks and Performance of LLMs [28 Nov 2023]
- Evaluation of Large Language Models: [A Survey on Evaluation of Large Language Models📑](https://alphaxiv.org/abs/2307.03109): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.03109)] [6 Jul 2023]
- [Evaluation Papers for ChatGPT✨](https://github.com/THU-KEG/EvaluationPapers4ChatGPT) [28 Feb 2023]
 ![**github stars**](https://img.shields.io/github/stars/THU-KEG/EvaluationPapers4ChatGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](https://eugeneyan.com/writing/llm-evaluators/):💡Key considerations and Use cases when using LLM-evaluators [Aug 2024]
- [LightEval✨](https://github.com/huggingface/lighteval):🤗 a lightweight LLM evaluation suite that Hugging Face has been using internally [Jan 2024]
 ![**github stars**](https://img.shields.io/github/stars/huggingface/lighteval?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLM Model Evals vs LLM Task Evals](https://x.com/aparnadhinak/status/1752763354320404488)
: `Model Evals` are really for people who are building or fine-tuning an LLM. vs The best LLM application builders are using `Task evals`. It's a tool to help builders build. [Feb 2024]
- [LLMPerf Leaderboard✨](https://github.com/ray-project/llmperf-leaderboard): Evaulation the performance of LLM APIs. [Dec 2023]
 ![**github stars**](https://img.shields.io/github/stars/ray-project/llmperf-leaderboard?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLM-as-a-Judge](https://cameronrwolfe.substack.com/i/141159804/practical-takeaways):💡LLM-as-a-Judge offers a quick, cost-effective way to develop models aligned with human preferences and is easy to implement with just a prompt, but should be complemented by human evaluation to address biases.  [Jul 2024]
- [Prometheus: Inducing Fine-grained Evaluation Capability in Language Models📑](https://alphaxiv.org/abs/2310.08491): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.08491)]: We utilize the FEEDBACK COLLECTION, a novel dataset, to train PROMETHEUS, an open-source large language model with 13 billion parameters, designed specifically for evaluation tasks. [12 Oct 2023]
- [The Leaderboard Illusion📑](https://alphaxiv.org/abs/2504.20879):💡Chatbot Arena's benchmarking is skewed by selective disclosures, private testing advantages, and data access asymmetries, leading to overfitting and unfair model rankings. [29 Apr 2025]

### **LLM Evalution Benchmarks**

#### Language Understanding and QA

1. [BIG-bench📑](https://alphaxiv.org/abs/2206.04615): Consists of 204 evaluations, contributed by over 450 authors, that span a range of topics from science to social reasoning. The bottom-up approach; anyone can submit an evaluation task. [✨](https://github.com/google/BIG-bench) [9 Jun 2022]
![**github stars**](https://img.shields.io/github/stars/google/BIG-bench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [BigBench✨](https://github.com/google/BIG-bench): 204 tasks. Predicting future potential [Published in 2023]
![**github stars**](https://img.shields.io/github/stars/google/BIG-bench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [GLUE](https://gluebenchmark.com/leaderboard) & [SuperGLUE](https://super.gluebenchmark.com/leaderboard/): GLUE (General Language Understanding Evaluation)
1. [HELM📑](https://alphaxiv.org/abs/2211.09110): Evaluation scenarios like reasoning and disinformation using standardized metrics like accuracy, calibration, robustness, and fairness. The top-down approach; experts curate and decide what tasks to evaluate models on. [✨](https://github.com/stanford-crfm/helm) [16 Nov 2022] ![**github stars**](https://img.shields.io/github/stars/stanford-crfm/helm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [HumanEval📑](https://alphaxiv.org/abs/2107.03374): Hand-Written Evaluation Set for Code Generation Bechmark. 164 Human written Programming Problems. [✍️](https://paperswithcode.com/task/code-generation) / [✨](https://github.com/openai/human-eval) [7 Jul 2021]
![**github stars**](https://img.shields.io/github/stars/openai/human-eval?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MMLU (Massive Multitask Language Understanding)✨](https://github.com/hendrycks/test): Over 15,000 questions across 57 diverse tasks. [Published in 2021]
![**github stars**](https://img.shields.io/github/stars/hendrycks/test?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MMLU (Massive Multi-task Language Understanding)📑](https://alphaxiv.org/abs/2009.03300): LLM performance across 57 tasks including elementary mathematics, US history, computer science, law, and more. [7 Sep 2020]
1. [TruthfulQA🤗](https://huggingface.co/datasets/truthful_qa): Truthfulness. [Published in 2022]

#### Coding

1. [CodeXGLUE✨](https://github.com/microsoft/CodeXGLUE): Programming tasks.
![**github stars**](https://img.shields.io/github/stars/microsoft/CodeXGLUE?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [HumanEval✨](https://github.com/openai/human-eval): Challenges coding skills. [Published in 2021]
![**github stars**](https://img.shields.io/github/stars/openai/human-eval?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MBPP✨](https://github.com/google-research/google-research/tree/master/mbpp): Mostly Basic Python Programming. [Published in 2021]
1. [SWE-bench](https://www.swebench.com/): Software Engineering Benchmark. Real-world software issues sourced from GitHub.
1. [SWE-Lancer✍️](https://openai.com/index/swe-lancer/): OpenAI. full engineering stack, from UI/UX to systems design, and include a range of task types, from $50 bug fixes to $32,000 feature implementations. [18 Feb 2025]

#### Chatbot Assistance

1. [Chatbot Arena🤗](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations): Human-ranked ELO ranking.
1. [MT Bench✨](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge): Multi-turn open-ended questions
  - [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena📑](https://alphaxiv.org/abs/2306.05685) [9 Jun 2023]

#### Reasoning

1. [ARC (AI2 Reasoning Challenge)✨](https://github.com/fchollet/ARC): Measures general fluid intelligence.
![**github stars**](https://img.shields.io/github/stars/fchollet/ARC?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DROP🤗](https://huggingface.co/datasets/drop): Evaluates discrete reasoning.
1. [HellaSwag✨](https://github.com/rowanz/hellaswag): Commonsense reasoning. [Published in 2019]
![**github stars**](https://img.shields.io/github/stars/rowanz/hellaswag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LogicQA✨](https://github.com/lgw863/LogiQA-dataset): Evaluates logical reasoning skills.
![**github stars**](https://img.shields.io/github/stars/lgw863/LogiQA-dataset?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### Translation

1. [WMT🤗](https://huggingface.co/wmt): Evaluates translation skills.

#### Math

1. [GSM8K✨](https://github.com/openai/grade-school-math): Arithmetic Reasoning. [Published in 2021]
![**github stars**](https://img.shields.io/github/stars/openai/grade-school-math?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MATH✨](https://github.com/hendrycks/math): Tests ability to solve math problems. [Published in 2021]
![**github stars**](https://img.shields.io/github/stars/hendrycks/math?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

 #### Other Benchmarks

- [Alpha Arena](https://nof1.ai/): a benchmark designed to measure AI's investing abilities. [Oct 2025]
- [Comprehensive and Practical Evaluation of Retrieval-Augmented Generation Systems for Medical Question Answering📑](https://alphaxiv.org/abs/2411.09213) [14 Nov 2024]
- [Korean SAT LLM Leaderboard✨](https://github.com/Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard): Benchmarking 10 years of Korean CSAT (College Scholastic Ability Test) exams [Oct 2024]
![**github stars**](https://img.shields.io/github/stars/Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [OpenAI BrowseComp✍️](https://openai.com/index/browsecomp/): A benchmark assessing AI agents’ ability to use web browsing tools to complete tasks requiring up-to-date information, reasoning, and navigation skills. Boost from tools + reasoning. Human trainer success ratio = 29.2% × 86.4% ≈ 25.2% [10 Apr 2025]
- [OpenAI GDPval✍️](https://openai.com/index/gdpval/): OpenAI's benchmark evaluating AI performance on real-world tasks across 44 occupations [25 Sep 2025]
- [OpenAI MLE-bench📑](https://alphaxiv.org/abs/2410.07095): A benchmark for measuring the performance of AI agents on ML tasks using Kaggle. [✨](https://github.com/openai/mle-bench) [9 Oct 2024] > Agent Framework used in MLE-bench, `GPT-4o (AIDE) achieves more medals on average than both MLAB and OpenHands (8.7% vs. 0.8% and 4.4% respectively)` [🔗](#agent-applications-and-libraries)
![**github stars**](https://img.shields.io/github/stars/openai/mle-bench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [OpenAI Paper Bench✍️](https://openai.com/index/paperbench/): a benchmark evaluating the ability of AI agents to replicate state-of-the-art AI research. [✨](https://github.com/openai/preparedness/tree/main/project/paperbench) [2 Apr 2025]
- [OpenAI SimpleQA Benchmark✍️](https://openai.com/index/introducing-simpleqa/): SimpleQA, a factuality benchmark for short fact-seeking queries, narrows its scope to simplify factuality measurement. [✨](https://github.com/openai/simple-evals) [30 Oct 2024] ![**github stars**](https://img.shields.io/github/stars/openai/simple-evals?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Social Sycophancy: A Broader Understanding of LLM Sycophancy📑](https://alphaxiv.org/abs/2505.13995): ELEPHANT; LLM Benchmark to assess LLM Sycophancy. Dataset (query): OEQ (Open-Ended Questions) and Reddit. LLMs (prompted as judges) to assess the presence of sycophancy in outputs with prompt [20 May 2025]

### **Evaluation Metrics**

- [Evaluating LLMs and RAG Systems✍️](https://dzone.com/articles/evaluating-llms-and-rag-systems) (Jan 2025)
1. Automated evaluation
    - **n-gram metrics**: ROUGE, BLEU, METEOR → compare overlap with reference text.
      - *ROUGE*: multiple variants (N, L, W, S, SU) based on n-gram, LCS, skip-bigrams.
      - *BLEU*: 0–1 score for translation quality.
      - *METEOR*: precision + recall + semantic similarity.
    - **Probabilistic metrics**: *Perplexity* → lower is better predictive performance.
    - **Embedding metrics**: Ada Similarity, BERTScore → semantic similarity using embeddings.
2. Human evaluation
    - Measures **relevance, fluency, coherence, groundedness**.
    - Automated with LLM-based evaluators.
3. Built-in methods
    - Prompt flow evaluation methods: [✍️](https://qiita.com/nohanaga/items/b68bf5a65142c5af7969) [Aug 2023] / [✍️](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-bulk-test-evaluate-flow)

### **LLMOps: Large Language Model Operations**

1. [agenta✨](https://github.com/Agenta-AI/agenta): OSS LLMOps workflow: building (LLM playground, evaluation), deploying (prompt and configuration management), and monitoring (LLM observability and tracing). [Jun 2023] ![**github stars**](https://img.shields.io/github/stars/Agenta-AI/agenta?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Azure ML Prompt flow](https://microsoft.github.io/promptflow/index.html): A set of LLMOps tools designed to facilitate the creation of LLM-based AI applications [Sep 2023] > [How to Evaluate & Upgrade Model Versions in the Azure OpenAI Service✍️](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/how-to-evaluate-amp-upgrade-model-versions-in-the-azure-openai/ba-p/4218880) [14 Aug 2024]
1. Azure Machine Learning studio Model Data Collector: Collect production data, analyze key safety and quality evaluation metrics on a recurring basis, receive timely alerts about critical issues, and visualize the results. [✍️](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-collect-production-data?view=azureml-api-2&tabs=azure-cli) [Apr 2024]
1. [circuit‑tracer✨](https://github.com/safety-research/circuit-tracer): Anthrophic. Tool for finding and visualizing circuits within large language models. a circuit is a minimal, causal computation pathway inside a transformer model that shows how internal features lead to a specific output. [May 2025] ![**github stars**](https://img.shields.io/github/stars/safety-research/circuit-tracer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DeepEval✨](https://github.com/confident-ai/deepeval): LLM evaluation framework. similar to Pytest but specialized for unit testing LLM outputs. [Aug 2023]
 ![**github stars**](https://img.shields.io/github/stars/confident-ai/deepeval?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DeepTeam✨](https://github.com/confident-ai/deepteam): A LLM Red Teaming Framework. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/confident-ai/deepteam?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Giskard✨](https://github.com/Giskard-AI/giskard): The testing framework for ML models, from tabular to LLMs [Mar 2022] ![**github stars**](https://img.shields.io/github/stars/Giskard-AI/giskard?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Langfuse](https://langfuse.com): [✨](https://github.com/langfuse/langfuse) LLMOps platform that helps teams to collaboratively monitor, evaluate and debug AI applications. [May 2023] 
 ![**github stars**](https://img.shields.io/github/stars/langfuse/langfuse?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Language Model Evaluation Harness✨](https://github.com/EleutherAI/lm-evaluation-harness):💡Over 60 standard academic benchmarks for LLMs. A framework for few-shot evaluation. Hugginface uses this for [Open LLM Leaderboard🤗](https://huggingface.co/open-llm-leaderboard) [Aug 2020]
 ![**github stars**](https://img.shields.io/github/stars/EleutherAI/lm-evaluation-harness?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LangWatch scenario✨](https://github.com/langwatch/scenario):💡LangWatch Agentic testing for agentic codebases. Simulating agentic communication using autopilot [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/langwatch/scenario?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LLMOps Database](https://www.zenml.io/llmops-database): A curated knowledge base of real-world LLMOps implementations.
1. [Maxim AI](https://getmaxim.ai): [✨](https://github.com/maximhq) End-to-end simulation, evaluation, and observability plaform, helping teams ship their AI agents reliably and >5x faster. [Dec 2023]
1. [Machine Learning Operations (MLOps) For Beginners✍️](https://towardsdatascience.com/machine-learning-operations-mlops-for-beginners-a5686bfe02b2): DVC (Data Version Control), MLflow, Evidently AI (Monitor a model). Insurance Cross Sell Prediction [✨](https://github.com/prsdm/mlops-project) [29 Aug 2024]
 ![**github stars**](https://img.shields.io/github/stars/prsdm/mlops-project?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Netdata✨](https://github.com/netdata/netdata): AI-powered real-time infrastructure monitoring platform [Jun 2013] ![**github stars**](https://img.shields.io/github/stars/netdata/netdata?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenAI Evals✨](https://github.com/openai/evals): A framework for evaluating large language models (LLMs) [Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/openai/evals?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Opik✨](https://github.com/comet-ml/opik): an open-source platform for evaluating, testing and monitoring LLM applications. Built by Comet. [2 Sep 2024] ![**github stars**](https://img.shields.io/github/stars/comet-ml/opik?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Pezzo✨](https://github.com/pezzolabs/pezzo): Open-source, developer-first LLMOps platform [May 2023]
 ![**github stars**](https://img.shields.io/github/stars/pezzolabs/pezzo?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [promptfoo✨](https://github.com/promptfoo/promptfoo): Test your prompts. Evaluate and compare LLM outputs, catch regressions, and improve prompt quality. [Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/promptfoo/promptfoo?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PromptTools✨](https://github.com/hegelai/prompttools/): Open-source tools for prompt testing [Jun 2023] ![**github stars**](https://img.shields.io/github/stars/hegelai/prompttools?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Ragas✨](https://github.com/explodinggradients/ragas): Evaluation framework for your Retrieval Augmented Generation (RAG) [May 2023]
 ![**github stars**](https://img.shields.io/github/stars/explodinggradients/ragas?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [traceloop openllmetry✨](https://github.com/traceloop/openllmetry): Quality monitoring for your LLM applications. [Sep 2023]
 ![**github stars**](https://img.shields.io/github/stars/traceloop/openllmetry?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [TruLens✨](https://github.com/truera/trulens): Instrumentation and evaluation tools for large language model (LLM) based applications. [Nov 2020]
 ![**github stars**](https://img.shields.io/github/stars/truera/trulens?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **Challenges in evaluating AI systems**

1. [30 requirements for an MLOps environment🗣️](https://x.com/KirkDBorne/status/1679952405805555713): Kirk Borne twitter [15 Jul 2023]
1. [Challenges in evaluating AI systems✍️](https://www.anthropic.com/index/evaluating-ai-systems): The challenges and limitations of various methods for evaluating AI systems, such as multiple-choice tests, human evaluations, red teaming, model-generated evaluations, and third-party audits. [🗄️](./files/eval-ai-anthropic.pdf) [4 Oct 2023]
1. [Economics of Hosting Open Source LLMs✍️](https://towardsdatascience.com/economics-of-hosting-open-source-llms-17b4ec4e7691): Comparison of cloud vendors such as AWS, Modal, BentoML, Replicate, Hugging Face Endpoints, and Beam, using metrics like processing time, cold start latency, and costs associated with CPU, memory, and GPU usage. [✨](https://github.com/ilsilfverskiold/Awesome-LLM-Resources-List) [13 Nov 2024]
1. [Pretraining on the Test Set Is All You Need📑](https://alphaxiv.org/abs/2309.08632): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.08632)]
   - On that note, in the satirical Pretraining on the Test Set Is All You Need paper, the author trains a small 1M parameter LLM that outperforms all other models, including the 1.3B phi-1.5 model. This is achieved by training the model on all downstream academic benchmarks. It appears to be a subtle criticism underlining how easily benchmarks can be "cheated" intentionally or unintentionally (due to data contamination). [🗣️](https://twitter.com/rasbt) [13 Sep 2023]
1. [Sakana AI claimed 100x faster AI training, but a bug caused a 3x slowdown](https://techcrunch.com/2025/02/21/sakana-walks-back-claims-that-its-ai-can-dramatically-speed-up-model-training/): Sakana’s AI resulted in a 3x slowdown — not a speedup. [21 Feb 2025]
1. [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) [29 Mar 2024] / [How to Evaluate LLM Applications: The Complete Guide](https://www.confident-ai.com/blog/how-to-evaluate-llm-applications) [7 Nov 2023]

