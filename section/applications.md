# App and Agent

## **Contents**
 
 - [RAG (Retrieval-Augmented Generation)](#rag-retrieval-augmented-generation)
   - [Advanced RAG](#advanced-rag)
   - [GraphRAG](#graphrag)
   - [RAG Application](#rag-application)
   - [Vector Database & Embedding](#vector-database--embedding)
 - [AI Application](#ai-application)
   - [Agent & Application](#agent--application)
   - [No Code & User Interface](#no-code--user-interface)
   - [Infrastructure & Backend Services](#infrastructure--backend-services)
   - [Caching](#caching)
   - [Data Processing](#data-processing)
   - [Gateway](#gateway)
   - [Memory](#memory)
 - [Agent Protocol](#agent-protocol)
   - [Model Context Protocol (MCP)](#model-context-protocol-mcp)
   - [A2A](#a2a)
   - [Computer use](#computer-use)
 - [Coding & Research](#coding--research)
   - [Coding](#coding)
   - [Skill](#skill)
   - [Domain-Specific Agents](#domain-specific-agents)
   - [Deep Research](#deep-research)
 - [Top Agent Frameworks](#top-agent-frameworks)
 - [Orchestration Framework](#orchestration-framework)
   - [LangChain](#langchain)
   - [LlamaIndex](#llamaindex)
   - [Semantic Kernel](#semantic-kernel)
   - [DSPy](#dspy)

## **RAG (Retrieval-Augmented Generation)**

- RAG integrates retrieval (searching) into LLM text generation, enabling models to access external information. [✍️](https://towardsdatascience.com/rag-vs-finetuning-which-is-the-best-tool-to-boost-your-llm-application-94654b1eaba7) [25 Aug 2023]
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks📑](https://arxiv.org/abs/2005.11401): Meta's 2020 framework for giving LLMs access to information beyond training data. [22 May 2020]
  - RAG-sequence — Retrieve k documents to generate all output tokens.
  - RAG-token— Retrieve k documents per token generation.
  - RAG-sequence is the industry standard due to lower cost and simplicity. [✍️](https://towardsdatascience.com/add-your-own-data-to-an-llm-using-retrieval-augmented-generation-rag-b1958bf56a5a) [30 Sep 2023]

### **Advanced RAG**

- [9 Effective Techniques To Boost Retrieval Augmented Generation (RAG) Systems✍️](https://towardsdatascience.com/9-effective-techniques-to-boost-retrieval-augmented-generation-rag-systems-210ace375049) [🗄️](9-effective-rag-techniques.png): ReRank, Prompt Compression, Hypothetical Document Embedding (HyDE), Query Rewrite and Expansion, Enhance Data Quality, Optimize Index Structure, Add Metadata, Align Query with Documents, Mixed Retrieval (Hybrid Search) [2 Jan 2024]
- Advanced RAG Patterns: How to improve RAG peformance [✍️](https://cloudatlas.me/why-do-rag-pipelines-fail-advanced-rag-patterns-part1-841faad8b3c2) / [✍️](https://cloudatlas.me/how-to-improve-rag-peformance-advanced-rag-patterns-part2-0c84e2df66e6) [17 Oct 2023]
  - Data quality: Clean, standardize, deduplicate, segment, annotate, augment, and update data to make it clear, consistent, and context-rich.
  - Embeddings fine-tuning: Fine-tune embeddings to domain specifics, adjust them according to context, and refresh them periodically to capture evolving semantics.
  - Retrieval optimization: Refine chunking, embed metadata, use query routing, multi-vector retrieval, re-ranking, hybrid search, recursive retrieval, query engine, [HyDE📑](https://arxiv.org/abs/2212.10496) [20 Dec 2022], and vector search algorithms to improve retrieval efficiency and relevance.
  - Synthesis techniques: Query transformations, prompt templating, prompt conditioning, function calling, and fine-tuning the generator to refine the generation step.
  - HyDE: Implemented in [LangChain: HypotheticalDocumentEmbedder✨](https://github.com/langchain-ai/langchain/blob/master/cookbook/hypothetical_document_embeddings.ipynb). A query generates hypothetical documents, which are then embedded and retrieved to provide the most relevant results. `query -> generate n hypothetical documents -> documents embedding - (avg of embeddings) -> retrieve -> final result.` [✍️](https://www.jiang.jp/posts/20230510_hyde_detailed/index.html)
- [Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG📑](https://arxiv.org/abs/2501.09136) [15 Jan 2025]
- [Azure RAG with Vision Application Framework✨](https://github.com/Azure-Samples/rag-as-a-service-with-vision) [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/rag-as-a-service-with-vision?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Contextual Retrieval✍️](https://www.anthropic.com/news/contextual-retrieval): Contextual Retrieval enhances traditional RAG by using Contextual Embeddings and Contextual BM25 to maintain context during retrieval. [19 Sep 2024]
- Demystifying Advanced RAG Pipelines: An LLM-powered advanced RAG pipeline built from scratch [✨](https://github.com/pchunduri6/rag-demystified) [19 Oct 2023]
 ![**github stars**](https://img.shields.io/github/stars/pchunduri6/rag-demystified?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Enhancing Ultra High Resolution Remote Sensing Imagery Analysis with ImageRAG📑](https://arxiv.org/abs/2411.07688): Ultra High Resolution (UHR) remote sensing imagery, such as satellite imagery and medical imaging. [12 Nov 2024]
- [Evaluation with Ragas✍️](https://towardsdatascience.com/visualize-your-rag-data-evaluate-your-retrieval-augmented-generation-system-with-ragas-fc2486308557): UMAP (often used to reduce the dimensionality of embeddings) with Ragas metrics for visualizing RAG results. [Mar 2024] / `Ragas provides metrics`: Context Precision, Context Relevancy, Context Recall, Faithfulness, Answer Relevance, Answer Semantic Similarity, Answer Correctness, Aspect Critique [✨](https://github.com/explodinggradients/ragas) [May 2023]
 ![**github stars**](https://img.shields.io/github/stars/explodinggradients/ragas?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- From Simple to Advanced RAG (LlamaIndex) [✍️](https://twitter.com/jerryjliu0/status/1711419232314065288) / [🗄️](../files/archive/LlamaIndexTalk_PyDataGlobal.pdf) /💡[✍️](https://aiconference.com/speakers/jerry-liu-2023/) [10 Oct 2023]
  <!-- <img src="../files/advanced-rag.png" width="430"> -->
- [How to improve RAG Piplines](https://www.linkedin.com/posts/damienbenveniste_how-to-improve-rag-pipelines-activity-7241497046631776256-vwOc?utm_source=li_share&utm_content=feedcontent&utm_medium=g_dt_web&utm_campaign=copy): LangGraph implementation with Self-RAG, Adaptive-RAG, Corrective RAG. [Oct 2024]
- How to optimize RAG pipeline: [Indexing optimization](https://newsletter.theaiedge.io/p/how-to-optimize-your-rag-pipelines) [24 Oct 2023]
- [localGPT-Vision✨](https://github.com/PromtEngineer/localGPT-Vision): an end-to-end vision-based Retrieval-Augmented Generation (RAG) system. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/PromtEngineer/localGPT-Vision?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Multi-Modal RAG System✍️](https://machinelearningmastery.com/implementing-multi-modal-rag-systems/): Building a knowledge base with both image and audio data. [12 Feb 2025]
- [🗣️](https://twitter.com/yi_ding/status/1721728060876300461) [7 Nov 2023] `OpenAI has put together a pretty good roadmap for building a production RAG system.` Naive RAG -> Tune Chunks -> Rerank & Classify -> Prompt Engineering. In `llama_index`... [📺](https://www.youtube.com/watch?v=ahnGLM-RC1Y)  <br/>
  <img src="../files/oai-rag-success-story.jpg" width="500">
- [Path-RAG: Knowledge-Guided Key Region Retrieval for Open-ended Pathology Visual Question Answering📑](https://arxiv.org/abs/2411.17073): Using HistoCartography to improve pathology image analysis and boost PathVQA-Open performance. [26 Nov 2024]
- [RAG Hallucination Detection Techniques✍️](https://machinelearningmastery.com/rag-hallucination-detection-techniques/): Hallucination metrics using the DeepEval, G-Eval. [10 Jan 2025] 
- RAG Pipeline: 1. Indexing Stage – prepare knowledge base; 2. Querying Stage – retrieve relevant data; 3. Responding Stage – generate responses [✍️](https://learn.microsoft.com/en-us/azure/machine-learning/concept-retrieval-augmented-generation)
- [UniversalRAG✨](https://github.com/wgcyeo/UniversalRAG) [29 Apr 2025]  ![**github stars**](https://img.shields.io/github/stars/wgcyeo/UniversalRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [VideoRAG📑](https://arxiv.org/abs/2501.05874): Not only does it retrieve relevant videos from a large video corpus, but it also integrates both the visual and textual elements of videos into the answer-generation process using Large Video Language Models (LVLMs). [10 Jan 2025]
- [Visual RAG over PDFs with Vespa✍️](https://blog.vespa.ai/visual-rag-in-practice/): a demo showcasing Visual RAG over PDFs using ColPali embeddings in Vespa [✨](https://github.com/vespa-engine/sample-apps/tree/master/visual-retrieval-colpali) [19 Nov 2024]
- [What is Agentic RAG](https://weaviate.io/blog/what-is-agentic-rag): The article published by Weaviate. [5 Nov 2024]

### **GraphRAG**

- [Fast GraphRAG✨](https://github.com/circlemind-ai/fast-graphrag): 6x cost savings compared to `graphrag`, with 20% higher accuracy. Combines PageRank and GraphRAG. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/circlemind-ai/fast-graphrag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [FalkorDB✨](https://github.com/FalkorDB/FalkorDB): Graph Database. Knowledge Graph for LLM (GraphRAG). OpenCypher (query language in Neo4j). [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/FalkorDB/FalkorDB?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Increasing the LLM Accuracy for Question Answering: Ontologies to the Rescue!📑](https://arxiv.org/abs/2405.11706): using a knowledge graph, the Text-to-SQL accuracy improved from 16% to 54%. [20 May 2024]
- [Graph RAG (by NebulaGraph)](https://medium.com/@nebulagraph/graph-rag-the-new-llm-stack-with-knowledge-graphs-e1e902c504ed): NebulaGraph proposes the concept of Graph RAG, which is a retrieval enhancement technique based on knowledge graphs. [demo](https://www.nebula-graph.io/demo) [8 Sep 2023]
- [GraphRAG (by Microsoft)📑](https://arxiv.org/abs/2404.16130):🏆1. Global search: Original Documents -> Knowledge Graph (Community Summaries generated by LLM) -> Partial Responses -> Final Response. 2. Local Search: Utilizes vector-based search to find the nearest entities and relevant information.
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
- [Graphiti✨](https://github.com/getzep/graphiti)
- [GraphSearch✨](https://github.com/DataArcTech/GraphSearch): An Agentic Workflow for Graph RAG. [Oct 2025]
- [HippoRAG✨](https://github.com/OSU-NLP-Group/HippoRAG):💡RAG + Knowledge Graphs + Personalized PageRank. [23 May 2024] ![**github stars**](https://img.shields.io/github/stars/OSU-NLP-Group/HippoRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [How to Build a Graph RAG App✍️](https://towardsdatascience.com/how-to-build-a-graph-rag-app-b323fc33ba06): Using knowledge graphs and AI to retrieve, filter, and summarize medical journal articles [30 Dec 2024]
- [HybridRAG📑](https://arxiv.org/abs/2408.04948): Integrating VectorRAG and GraphRAG with financial earnings call transcripts in Q&A format. [9 Aug 2024]
- [Neo4j GraphRAG Package for Python✨](https://github.com/neo4j/neo4j-graphrag-python) [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/neo4j/neo4j-graphrag-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **RAG Application**

1. [AutoRAG✨](https://github.com/Marker-Inc-Korea/AutoRAG): RAG AutoML tool for automatically finds an optimal RAG pipeline for your data. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/Marker-Inc-Korea/AutoRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Canopy✨](https://github.com/pinecone-io/canopy): open-source RAG framework and context engine built on top of the Pinecone vector database. [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/pinecone-io/canopy?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Chonkie✨](https://github.com/SecludedCoder/chonkie): RAG chunking library [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/SecludedCoder/chonkie?style=flat-square&label=%20&color=blue&cacheSeconds=36000) <!--old: https://github.com/chonkie-ai/chonkie -->
1. [Cognita✨](https://github.com/truefoundry/cognita): RAG (Retrieval Augmented Generation) Framework for building modular, open-source applications [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/truefoundry/cognita?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Danswer✨](https://github.com/danswer-ai/danswer): Ask Questions in natural language and get Answers backed by private sources: Slack, GitHub, Confluence, etc. [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/danswer-ai/danswer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Fireplexity✨](https://github.com/mendableai/fireplexity): AI search engine by Firecrawl's search API [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/mendableai/fireplexity?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [FlashRAG✨](https://github.com/RUC-NLPIR/FlashRAG): A Python Toolkit for Efficient RAG Research [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/RUC-NLPIR/FlashRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Gemini-Search✨](https://github.com/ammaarreshi/Gemini-Search): Perplexity style AI Search engine clone built with Gemini [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/ammaarreshi/Gemini-Search?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Haystack✨](https://github.com/deepset-ai/haystack): LLM orchestration framework to build customizable, production-ready LLM applications. [5 May 2020] ![**github stars**](https://img.shields.io/github/stars/deepset-ai/haystack?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [KAG✨](https://github.com/OpenSPG/KAG): Knowledge Augmented Generation. a logical reasoning and Q&A framework based on the OpenSPG(Semantic-enhanced Programmable Graph). By Ant Group. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/OpenSPG/KAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Khoj✨](https://github.com/khoj-ai/khoj): Open-source, personal AI agents. Cloud or Self-Host, Multiple Interfaces. Python Django based [Aug 2021] ![**github stars**](https://img.shields.io/github/stars/khoj-ai/khoj?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [kotaemon✨](https://github.com/Cinnamon/kotaemon): Open-source clean & customizable RAG UI for chatting with your documents. [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/Cinnamon/kotaemon?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [llm-answer-engine✨](https://github.com/developersdigest/llm-answer-engine): Build a Perplexity-Inspired Answer Engine Using Next.js, Groq, Mixtral, LangChain, OpenAI, Brave & Serper [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/developersdigest/llm-answer-engine?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [llmware✨](https://github.com/llmware-ai/llmware): Building Enterprise RAG Pipelines with Small, Specialized Models [Sep 2023] ![**github stars**](https://img.shields.io/github/stars/llmware-ai/llmware?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Marqo✨](https://github.com/marqo-ai/marqo): Tensor search for humans [Aug 2022] ![**github stars**](https://img.shields.io/github/stars/marqo-ai/marqo?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MedGraphRAG📑](https://arxiv.org/abs/2408.04187): MedGraphRAG outperforms the previous SOTA model, [Medprompt📑](https://arxiv.org/abs/2311.16452), by 1.1%. [✨](https://github.com/medicinetoken/medical-graph-rag) [8 Aug 2024] ![**github stars**](https://img.shields.io/github/stars/medicinetoken/medical-graph-rag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Meilisearch✨](https://github.com/meilisearch/meilisearch): A lightning-fast search engine API bringing AI-powered hybrid search to your sites and applications. [Apr 2018] ![**github stars**](https://img.shields.io/github/stars/meilisearch/meilisearch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MemFree✨](https://github.com/memfreeme/memfree): Hybrid AI Search Engine + AI Page Generator. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/memfreeme/memfree?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MindSearch✨](https://github.com/InternLM/MindSearch): An open-source AI Search Engine Framework [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/InternLM/MindSearch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MiniRAG✨](https://github.com/HKUDS/MiniRAG): RAG through heterogeneous graph indexing and lightweight topology-enhanced retrieval. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/HKUDS/MiniRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Morphic✨](https://github.com/miurla/morphic): An AI-powered search engine with a generative UI [Apr 2024] ![**github stars**](https://img.shields.io/github/stars/miurla/morphic?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PageIndex✨](https://github.com/VectifyAI/PageIndex): a vectorless, reasoning-based RAG system that builds a hierarchical tree index [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/VectifyAI/PageIndex?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PaperQA2✨](https://github.com/Future-House/paper-qa): High accuracy RAG for answering questions from scientific documents with citations [Feb 2023] ![**github stars**](https://img.shields.io/github/stars/Future-House/paper-qa?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Perplexica✨](https://github.com/ItzCrazyKns/Perplexica):💡Open source alternative to Perplexity AI [Apr 2024] ![**github stars**](https://img.shields.io/github/stars/ItzCrazyKns/Perplexica?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PrivateGPT✨](https://github.com/imartinez/privateGPT): 100% privately, no data leaks. The API is built using FastAPI and follows OpenAI's API scheme. [May 2023] ![**github stars**](https://img.shields.io/github/stars/imartinez/privateGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Pyversity✨](https://github.com/Pringled/pyversity): A rerank library for search results [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/Pringled/pyversity?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [quivr✨](https://github.com/QuivrHQ/quivr): A personal productivity assistant (RAG). Chat with your docs (PDF, CSV, ...) [May 2023] ![**github stars**](https://img.shields.io/github/stars/QuivrHQ/quivr?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [R2R (Reason to Retrieve)✨](https://github.com/SciPhi-AI/R2R): Agentic Retrieval-Augmented Generation (RAG) with a RESTful API. [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/SciPhi-AI/R2R?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAG Builder✨](https://github.com/KruxAI/ragbuilder): Automatically create an optimal production-ready Retrieval-Augmented Generation (RAG) setup for your data. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/KruxAI/ragbuilder?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAG capabilities of LlamaIndex to QA about SEC 10-K & 10-Q documents✨](https://github.com/run-llama/sec-insights): A real world full-stack application using LlamaIndex [Sep 2023] ![**github stars**](https://img.shields.io/github/stars/run-llama/sec-insights?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAG-Anything✨](https://github.com/HKUDS/RAG-Anything): "RAG-Anything: All-in-One RAG System". [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/HKUDS/RAG-Anything?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAGApp✨](https://github.com/ragapp/ragapp): Agentic RAG. Custom GPTs, but deployable in your own cloud infrastructure using Docker. [Apr 2024] ![**github stars**](https://img.shields.io/github/stars/ragapp/ragapp?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAGChecker📑](https://arxiv.org/abs/2408.08067): A Fine-grained Framework For Diagnosing RAG [✨](https://github.com/amazon-science/RAGChecker) [15 Aug 2024] ![**github stars**](https://img.shields.io/github/stars/amazon-science/RAGChecker?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAGflow✨](https://github.com/infiniflow/ragflow):💡Streamlined RAG workflow. Focusing on Deep document understanding [Dec 2023] ![**github stars**](https://img.shields.io/github/stars/infiniflow/ragflow?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAGFoundry✨](https://github.com/IntelLabs/RAGFoundry): A library designed to improve LLMs ability to use external information by fine-tuning models on specially created RAG-augmented datasets. [5 Aug 2024] ![**github stars**](https://img.shields.io/github/stars/IntelLabs/RAGFoundry?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAGLite✨](https://github.com/superlinear-ai/raglite): a Python toolkit for Retrieval-Augmented Generation (RAG) with PostgreSQL or SQLite [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/superlinear-ai/raglite?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RAGxplorer✨](https://github.com/gabrielchua/RAGxplorer): Visualizing document chunks and the queries in the embedding space. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/gabrielchua/RAGxplorer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Renumics RAG✨](https://github.com/Renumics/renumics-rag): Visualization for a Retrieval-Augmented Generation (RAG) Data [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/Renumics/renumics-rag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Scira (Formerly MiniPerplx)✨](https://github.com/zaidmukaddam/scira): A minimalistic AI-powered search engine [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/zaidmukaddam/scira?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Semantra✨](https://github.com/freedmand/semantra): Multi-tool for semantic search [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/freedmand/semantra?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Simba✨](https://github.com/GitHamza0206/simba): Portable KMS (knowledge management system) designed to integrate seamlessly with any Retrieval-Augmented Generation (RAG) system [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/GitHamza0206/simba?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [smartrag✨](https://github.com/aymenfurter/smartrag): Deep Research through Multi-Agents, using GraphRAG. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/aymenfurter/smartrag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SWIRL AI Connect✨](https://github.com/swirlai/swirl-search): SWIRL AI Connect enables you to perform Unified Search and bring in a secure AI Co-Pilot. [Apr 2022] ![**github stars**](https://img.shields.io/github/stars/swirlai/swirl-search?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [turboseek✨](https://github.com/Nutlope/turboseek): An AI search engine inspired by Perplexity [May 2024] ![**github stars**](https://img.shields.io/github/stars/Nutlope/turboseek?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [txtai✨](https://github.com/neuml/txtai): Semantic search and workflows powered by language models [Aug 2020] ![**github stars**](https://img.shields.io/github/stars/neuml/txtai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Typesense✨](https://github.com/typesense/typesense): Open Source alternative to Algolia + Pinecone and an Easier-to-Use alternative to ElasticSearch [Jan 2017] ![**github stars**](https://img.shields.io/github/stars/typesense/typesense?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Verba✨](https://github.com/weaviate/Verba): Retrieval Augmented Generation (RAG) chatbot powered by Weaviate [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/weaviate/Verba?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [WeKnora✨](https://github.com/Tencent/WeKnora): LLM-powered framework for deep document understanding, semantic retrieval, and context-aware answers using RAG paradigm. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/Tencent/WeKnora?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Xyne✨](https://github.com/xynehq/xyne): an AI-first Search & Answer Engine for work. We're an OSS alternative to Glean, Gemini and MS Copilot. [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/xynehq/xyne?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **Vector Database & Embedding**

- [A Comprehensive Survey on Vector Database📑](https://arxiv.org/abs/2310.11703): Categorizes search algorithms by their approach, such as hash-based, tree-based, graph-based, and quantization-based. [18 Oct 2023]
- [A Gentle Introduction to Word Embedding and Text Vectorization✍️](https://machinelearningmastery.com/a-gentle-introduction-to-word-embedding-and-text-vectorization/): Word embedding, Text vectorization, One-hot encoding, Bag-of-words, TF-IDF, word2vec, GloVe, FastText. | [Tokenizers in Language Models✍️](https://machinelearningmastery.com/tokenizers-in-language-models/): Stemming, Lemmatization, Byte Pair Encoding (BPE), WordPiece, SentencePiece, Unigram [23 May 2025]
- Azure Open AI Embedding API, `text-embedding-ada-002`, supports 1536 dimensions. Elastic search, Lucene based engine, supports 1024 dimensions as a max. Open search can insert 16,000 dimensions as a vector storage. Open search is available to use as a vector database with Azure Open AI Embedding API.
- [A SQLite extension for efficient vector search, based on Faiss!✨](https://github.com/asg017/sqlite-vss) [Jan 2023]
 ![**github stars**](https://img.shields.io/github/stars/asg017/sqlite-vss?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Chroma✨](https://github.com/chroma-core/chroma): Open-source embedding database [Oct 2022]
 ![**github stars**](https://img.shields.io/github/stars/chroma-core/chroma?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Contextual Document Embedding (CDE)📑](https://arxiv.org/abs/2410.02525): Improve document retrieval by embedding both queries and documents within the context of the broader document corpus. [✍️](https://pub.aimind.so/unlocking-the-power-of-contextual-document-embeddings-enhancing-search-relevance-01abfa814c76) [3 Oct 2024]
- [Contextualized Chunk Embedding Model✍️](https://blog.voyageai.com/2025/07/23/voyage-context-3/): Rather than embedding each chunk separately, a contextualized chunk embedding model uses the whole document to create chunk embeddings that reflect the document's overall context. [✍️](https://blog.dailydoseofds.com/p/contextualized-chunk-embedding-model) [23 Jul 2025]
- [EmbedAnything✨](https://github.com/StarlightSearch/EmbedAnything): Built by Rust. Supports BERT, CLIP, Jina, ColPali, ColBERT, ModernBERT, Reranker, Qwen. Mutilmodality. [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/StarlightSearch/EmbedAnything?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Embedding Atlas✨](https://github.com/apple/embedding-atlas): Apple. a tool that provides interactive visualizations for large embeddings. [May 2025]
- [Faiss](https://faiss.ai/): Facebook AI Similarity Search (Faiss) is a library for efficient similarity search and clustering of dense vectors. It is used as an alternative to a vector database in the development and library of algorithms for a vector database. It is developed by Facebook AI Research. [✨](https://github.com/facebookresearch/faiss) [Feb 2017]
 ![**github stars**](https://img.shields.io/github/stars/facebookresearch/faiss?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [FalkorDB✨](https://github.com/FalkorDB/FalkorDB): Graph Database. Knowledge Graph for LLM (GraphRAG). OpenCypher (query language in Neo4j). For a sparse matrix, the graph can be queried with linear algebra instead of traversal, boosting performance.  [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/FalkorDB/FalkorDB?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Fine-tuning Embeddings for Specific Domains✍️](https://blog.gopenai.com/fine-tuning-embeddings-for-specific-domains-a-comprehensive-guide-5e4298b42185): The guide discusses fine-tuning embeddings for domain-specific tasks using `sentence-transformers` [1 Oct 2024]
- However, one exception to this is that the maximum dimension count for the Lucene engine is 1,024, compared with
  16,000 for the other engines. [✍️](https://opensearch.org/docs/latest/search-plugins/knn/approximate-knn/)
- [Is Cosine-Similarity of Embeddings Really About Similarity?📑](https://arxiv.org/abs/2403.05440): Regularization in linear matrix factorization can distort cosine similarity. L2-norm regularization on (1) the product of matrices (like dropout) and (2) individual matrices (like weight decay) may lead to arbitrary similarities.  [8 Mar 2024]
- OpenAI Embedding models: `text-embedding-3`
- [lancedb✨](https://github.com/lancedb/lancedb): LanceDB's core is written in Rust and is built using Lance, an open-source columnar format.  [Feb 2023] ![**github stars**](https://img.shields.io/github/stars/lancedb/lancedb?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LEANN✨](https://github.com/yichuan-w/LEANN): The smallest vector database. 97% less storage. [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/yichuan-w/LEANN?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Milvus (A cloud-native vector database) Embedded [✨](https://github.com/milvus-io/milvus) [Sep 2019]: Alternative option to replace PineCone and Redis Search in OSS. It offers support for multiple languages, addresses the limitations of RedisSearch, and provides cloud scalability and high reliability with Kubernetes.
 ![**github stars**](https://img.shields.io/github/stars/milvus-io/milvus?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [MongoDB's GenAI Showcase✨](https://github.com/mongodb-developer/GenAI-Showcase): Step-by-step Jupyter Notebook examples on how to use MongoDB as a vector database, data store, memory provider [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/mongodb-developer/GenAI-Showcase?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Not All Vector Databases Are Made Equal✍️](https://towardsdatascience.com/milvus-pinecone-vespa-weaviate-vald-gsi-what-unites-these-buzz-words-and-what-makes-each-9c65a3bd0696): Printed version for "Medium" limits. [🗄️](../files/vector-dbs.pdf) [2 Oct 2021]
- [pgvector✨](https://github.com/pgvector/pgvector): Open-source vector similarity search for Postgres [Apr 2021] / [pgvectorscale✨](https://github.com/timescale/pgvectorscale): 75% cheaper than pinecone [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/pgvector/pgvector?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/timescale/pgvectorscale?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Pinecone](https://docs.pinecone.io): A fully managed cloud Vector Database. Commercial Product [Jan 2021]
- [Qdrant✨](https://github.com/qdrant/qdrant): Written in Rust. Qdrant (read: quadrant) [May 2020]
 ![**github stars**](https://img.shields.io/github/stars/qdrant/qdrant?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Redis extension for vector search, RedisVL✨](https://github.com/redis/redis-vl-python): Redis Vector Library (RedisVL) [Nov 2022]
 ![**github stars**](https://img.shields.io/github/stars/redis/redis-vl-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [text-embedding-ada-002✍️](https://openai.com/blog/new-and-improved-embedding-model):
  Smaller embedding size. The new embeddings have only 1536 dimensions, one-eighth the size of davinci-001 embeddings,
  making the new embeddings more cost effective in working with vector databases. [15 Dec 2022]
- [The Semantic Galaxy🤗](https://huggingface.co/spaces/webml-community/semantic-galaxy): Visualize embeddings in 3D space, powered by EmbeddingGemma and Transformers.js [Sep 2025]
- [Vector Search with OpenAI Embeddings: Lucene Is All You Need📑](https://arxiv.org/abs/2308.14963): For vector search applications, Lucene's HNSW implementation is a resilient and extensible solution with performance comparable to specialized vector databases like FAISS. Our experiments used Lucene 9.5.0, which limits vectors to 1024 dimensions—insufficient for OpenAI's 1536-dimensional embeddings. A fix to make vector dimensions configurable per codec has been merged to Lucene's source [here✨](https://github.com/apache/lucene/pull/12436) but was not yet released as of August 2023. [29 Aug 2023]
- [Weaviate✨](https://github.com/weaviate/weaviate): Store both vectors and data objects. [Jan 2021]
 ![**github stars**](https://img.shields.io/github/stars/weaviate/weaviate?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **AI Application**

- [900 most popular open source AI tools](https://huyenchip.com/2024/03/14/ai-oss.html):🏆What I learned from looking at 900 most popular open source AI tools [list](https://huyenchip.com/llama-police) [Mar 2024]
- [Awesome LLM Apps✨](https://github.com/Shubhamsaboo/awesome-llm-apps):💡A curated collection of awesome LLM apps built with RAG and AI agents. [Apr 2024]
 ![**github stars**](https://img.shields.io/github/stars/Shubhamsaboo/awesome-llm-apps?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure OpenAI Samples✨](https://github.com/kimtth/azure-openai-cookbook): 🐳 Azure OpenAI (OpenAI) Sample Collection - 🪂 100+ Code Cookbook 🧪 [Mar 2025]
- [GenAI Agents✨](https://github.com/NirDiamant/GenAI_Agents):🏆Tutorials and implementations for various Generative AI Agent techniques, from basic to advanced. [Sep 2024]
 ![**github stars**](https://img.shields.io/github/stars/NirDiamant/GenAI_Agents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [GenAI Cookbook✨](https://github.com/dmatrix/genai-cookbook): A mixture of Gen AI cookbook recipes for Gen AI applications. [Nov 2023] ![**github stars**](https://img.shields.io/github/stars/dmatrix/genai-cookbook?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Generative AI Design Patterns✍️](https://towardsdatascience.com/generative-ai-design-patterns-a-comprehensive-guide-41425a40d7d0): 9 architecture patterns for working with LLMs. [Feb 2024]
- [Open100: Top 100 Open Source achievements.](https://www.benchcouncil.org/evaluation/opencs/annual.html)

#### Agent & Application

##### Frameworks / SDKs / Building Blocks

1. [AgentOps✨](https://github.com/AgentOps-AI/agentops):Python SDK for AI agent monitoring, LLM cost tracking, benchmarking. [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/AgentOps-AI/agentops?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AgentScope✨](https://github.com/modelscope/agentscope): To build LLM-empowered multi-agent applications. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/modelscope/agentscope?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [agency-swarm✨](https://github.com/VRSEN/agency-swarm): Reliable Multi-Agent Orchestration Framework [Nov 2023] ![**github stars**](https://img.shields.io/github/stars/VRSEN/agency-swarm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AgentVerse✨](https://github.com/OpenBMB/AgentVerse): Primarily providing: task-solving and simulation. [May 2023] ![**github stars**](https://img.shields.io/github/stars/OpenBMB/AgentVerse?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Agno✨](https://github.com/agno-agi/agno):💡Build Multimodal AI Agents with memory, knowledge and tools. Simple, fast and model-agnostic. [Nov 2023] ![**github stars**](https://img.shields.io/github/stars/agno-agi/agno?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Atomic Agents✨](https://github.com/BrainBlend-AI/atomic-agents): an extremely lightweight and modular framework for building Agentic AI pipelines [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/BrainBlend-AI/atomic-agents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AutoAgent✨](https://github.com/HKUDS/AutoAgent): AutoAgent: Fully-Automated and Zero-Code LLM Agent Framework ![**github stars**](https://img.shields.io/github/stars/HKUDS/AutoAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AWS: Multi-Agent Orchestrator✨](https://github.com/awslabs/multi-agent-orchestrator): agent-squad
. a framework for managing multiple AI agents and handling complex conversations. [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/awslabs/multi-agent-orchestrator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Bee Agent Framework✨](https://github.com/i-am-bee/bee-agent-framework): IBM. The TypeScript framework for building scalable agentic applications. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/i-am-bee/bee-agent-framework?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Burr✨](https://github.com/dagworks-inc/burr): Create an application as a state machine (graph/flowchart) for managing state, decisions, human feedback, and workflows. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/dagworks-inc/burr?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [CAMEL✨](https://github.com/lightaime/camel): CAMEL: Communicative Agents for “Mind” Exploration of Large Scale Language Model Society [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/lightaime/camel?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Cheshire-Cat (Stregatto)✨](https://github.com/cheshire-cat-ai/core): Framework to build custom AIs with memory and plugins [Feb 2023] ![**github stars**](https://img.shields.io/github/stars/cheshire-cat-ai/core?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Claude Agent SDK for Python✨](https://github.com/anthropics/claude-agent-sdk-python) [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/anthropics/claude-agent-sdk-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [composio✨](https://github.com/ComposioHQ/composio): Integration of Agents with 100+ Tools [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/ComposioHQ/composio?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [crewAI✨](https://github.com/joaomdmoura/CrewAI):💡Framework for orchestrating role-playing, autonomous AI agents. [Oct 2023] ![**github stars**](https://img.shields.io/github/stars/joaomdmoura/CrewAI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Dagger✨](https://github.com/dagger/dagger): an open-source runtime for composable workflows. [Nov 2019] ![**github stars**](https://img.shields.io/github/stars/dagger/dagger?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Dynamiq✨](https://github.com/dynamiq-ai/dynamiq): An orchestration framework for RAG, agentic AI, and LLM applications [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/dynamiq-ai/dynamiq?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Eko (pronounced like ‘echo’) ✨](https://github.com/FellouAI/eko): Pure JavaScript. Build Production-ready Agentic Workflow with Natural Language. Support Browser use & Computer use [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/FellouAI/eko?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ell✨](https://github.com/MadcowD/ell): Treats prompts as programs with built-in versioning, monitoring, and tooling for LLMs. [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/MadcowD/ell?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [fairseq✨](https://github.com/facebookresearch/fairseq): a sequence modeling toolkit that allows researchers and developers to train custom models for translation, summarization, language modeling [Sep 2017]
1. [fastText✨](https://github.com/facebookresearch/fastText): A library for efficient learning of word representations and sentence classification [Aug 2016]
1. [Google ADK✨](https://github.com/google/adk-python): Agent Development Kit (ADK) [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/google/adk-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [jax✨](https://github.com/google/jax): JAX is Autograd (automatically differentiate native Python & Numpy) and XLA (compile and run NumPy) [Oct 2018]
1. [Jina-Serve✨](https://github.com/jina-ai/serve): a framework for building and deploying AI services that communicate via gRPC, HTTP and WebSockets. [Feb 2020] ![**github stars**](https://img.shields.io/github/stars/jina-ai/serve?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Lagent✨](https://github.com/InternLM/lagent): Inspired by the design philosophy of PyTorch. A lightweight framework for building LLM-based agents. [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/InternLM/lagent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [langfun✨](https://github.com/google/langfun): leverages PyGlove to integrate LLMs and programming. [Aug 2023]
1. [LaVague✨](https://github.com/lavague-ai/LaVague): Automate automation with Large Action Model framework. Generate Selenium code. [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/lavague-ai/LaVague?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Llama Stack✨](https://github.com/meta-llama/llama-stack):💡building blocks for Large Language Model (LLM) development [Jun 2024]
1. [marvin✨](https://github.com/PrefectHQ/marvin): a lightweight AI toolkit for building natural language interfaces. [Mar 2023]
1. [Mastra✨](https://github.com/mastra-ai/mastra): The TypeScript AI agent framework. workflows, agents, RAG, integrations and evals. [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/mastra-ai/mastra?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Memento✨](https://github.com/Agent-on-the-Fly/Memento): Fine-tuning LLM Agents without Fine-tuning LLMs [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/Agent-on-the-Fly/Memento?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MetaGPT✨](https://github.com/geekan/MetaGPT): Multi-Agent Framework. Assign different roles to GPTs to form a collaborative entity for complex tasks. e.g., Data Interpreter [Jun 2023] ![**github stars**](https://img.shields.io/github/stars/geekan/MetaGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MiniChain✨](https://github.com/srush/MiniChain): A tiny library for coding with llm [Feb 2023]
1. [mirascope✨](https://github.com/Mirascope/mirascope): a library that simplifies working with LLMs via a unified interface for multiple providers. [Dec 2023] ![**github stars**](https://img.shields.io/github/stars/Mirascope/mirascope?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Mixture Of Agents (MoA)✨](https://github.com/togethercomputer/MoA): an architecture that runs multiple LLMs in parallel, then uses a final “aggregator” model to merge their outputs into a superior combined response. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/togethercomputer/MoA?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ModelScope-Agent✨](https://github.com/modelscope/ms-agent): Lightweight Framework for Agents with Autonomous Exploration [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/modelscope/ms-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [motia✨](https://github.com/MotiaDev/motia): Modern Backend Framework that unifies APIs, background jobs, workflows, and AI agents into a single cohesive system with built-in observability and state management. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/MotiaDev/motia?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Open Agent Platform✨](https://github.com/langchain-ai/open-agent-platform): Langchain. An open-source, no-code agent building platform. [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/langchain-ai/open-agent-platform?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [Open AI Assistant API](https://platform.openai.com/docs/assistants/overview) [6 Nov 2023]
1. [OpenAI Agents SDK & Response API✨](https://github.com/openai/openai-agents-python):🏆Responses API (Chat Completions + Assistants API), Built-in tools (web search, file search, computer use), Agents SDK for multi-agent workflows, agent workflow observability tools [11 Mar 2025] ![**github stars**](https://img.shields.io/github/stars/openai/openai-agents-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenAI Swarm✨](https://github.com/openai/swarm): An experimental and educational framework for lightweight multi-agent orchestration. [11 Oct 2024] ![**github stars**](https://img.shields.io/github/stars/openai/swarm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenEnv✨](https://github.com/meta-pytorch/OpenEnv): An e2e framework for isolated execution environments for agentic RL training, built using Gymnasium style simple APIs. [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/meta-pytorch/OpenEnv?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OWL: Optimized Workforce Learning✨](https://github.com/camel-ai/owl): a multi-agent collaboration framework built on CAMEL-AI, enhancing task automation [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/camel-ai/owl?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [parlant✨](https://github.com/emcie-co/parlant): Instead of hoping your LLM will follow instructions, Parlant ensures rule compliance, Predictable, consistent behavior [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/emcie-co/parlant?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PayPal Agent Toolkit✨](https://github.com/paypal/agent-toolkit): OpenAI's Agent SDK, LangChain, Vercel's AI SDK, and Model Context Protocol (MCP) to integrate with PayPal APIs through function calling. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/paypal/agent-toolkit?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [phidata✨](https://github.com/phidatahq/phidata): Build AI Assistants with memory, knowledge, and tools [May 2022] ![**github stars**](https://img.shields.io/github/stars/phidatahq/phidata?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Pipecat✨](https://github.com/pipecat-ai/pipecat): Open Source framework for voice and multimodal conversational AI [Dec 2023] ![**github stars**](https://img.shields.io/github/stars/pipecat-ai/pipecat?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PocketFlow✨](https://github.com/miniLLMFlow/PocketFlow): Minimalist LLM Framework in 100 Lines. Enable LLMs to Program Themselves. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/miniLLMFlow/PocketFlow?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PydanticAI✨](https://github.com/pydantic/pydantic-ai): Agent Framework / shim to use Pydantic with LLMs. Model-agnostic. Type-safe. [29 Oct 2024] ![**github stars**](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Qwen-Agent✨](https://github.com/QwenLM/Qwen-Agent): Agent framework built upon Qwen1.5, featuring Function Calling, Code Interpreter, RAG, and Chrome extension. [Sep 2023] ![**github stars**](https://img.shields.io/github/stars/QwenLM/Qwen-Agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ROMA: Recursive Open Meta-Agents✨](https://github.com/sentient-agi/ROMA): an open-source meta-agent framework designed to build high-performance multi-agent systems by decomposing complex tasks into recursive, parallelizable components ![**github stars**](https://img.shields.io/github/stars/sentient-agi/ROMA?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Sentence Transformers📑](https://arxiv.org/abs/1908.10084): Python framework for state-of-the-art sentence, text and image embeddings. Useful for semantic textual similar, semantic search, or paraphrase mining. [✨](https://github.com/UKPLab/sentence-transformers) [27 Aug 2019]
1. [Spring AI✨](https://github.com/spring-projects-experimental/spring-ai): Developing AI applications for Java. [Jul 2023]
1. [Strands Agents✨](https://github.com/strands-agents/sdk-python): Model‑Driven, Tool‑First Architecture. No need to hard-code logic. Just define tools and models—the system figures out how to use them. [May 2025] ![**github stars**](https://img.shields.io/github/stars/strands-agents/sdk-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [string2string✨](https://github.com/stanfordnlp/string2string): an open-source tool that offers a comprehensive suite of efficient algorithms for a broad range of string-to-string problems. [Mar 2023]
1. [Superagent✨](https://github.com/superagent-ai/superagent): AI Assistant Framework & API [May 2023]
1. [SuperAGI✨](https://github.com/TransformerOptimus/SuperAGI): Autonomous AI Agents framework [May 2023] ![**github stars**](https://img.shields.io/github/stars/TransformerOptimus/SuperAGI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SwarmZero✨](https://github.com/swarmzero/swarmzero): SwarmZero's SDK for building AI agents, swarms of agents. [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/swarmzero/swarmzero?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [TanStack✨](https://github.com/TanStack/ai): TypeScript-based AI SDK for building LLM-powered applications. [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/TanStack/ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [TaskingAI✨](https://github.com/TaskingAI/TaskingAI): A BaaS (Backend as a Service) platform for LLM-based Agent Development and Deployment. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/TaskingAI/TaskingAI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Tokenizer (microsoft)✨](https://github.com/microsoft/Tokenizer): Tiktoken in C#: .NET and TypeScript implementation of BPE tokenizer for OpenAI LLMs. [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/microsoft/Tokenizer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [vanna✨](https://github.com/vanna-ai/vanna): Chat with your SQL database. Accurate Text-to-SQL Generation via LLMs using RAG. [May 2023]
1. [VoltAgent✨](https://github.com/VoltAgent/voltagent): Open Source TypeScript AI Agent Framework [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/VoltAgent/voltagent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [xpander.ai✨](https://github.com/xpander-ai/xpander.ai): Backend-as-a-Service for AI Agents. Equip any AI Agent with tools, memory, multi-agent collaboration, state, triggering, storage, and more. [May 2025] ![**github stars**](https://img.shields.io/github/stars/xpander-ai/xpander.ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

##### Apps / Demos / Ready-to-use Agents

1. [Agent Zero✨](https://github.com/frdel/agent-zero): An open-source framework for autonomous AI agents with task automation and code generation. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/frdel/agent-zero?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Agent-S✨](https://github.com/simular-ai/Agent-S): To build intelligent GUI agents that autonomously learn and perform complex tasks on your computer. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/simular-ai/Agent-S?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [A2UI✨](https://github.com/google/A2UI): an open standard and set of libraries that allows agents to "speak UI." Agents send a declarative JSON format describing the intent of the UI. The client application then renders this using its own native component library. [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/google/A2UI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Agentarium✨](https://github.com/Thytu/Agentarium): a framework for creating and managing simulations populated with AI-powered agents. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/Thytu/Agentarium?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AgentGPT✨](https://github.com/reworkd/AgentGPT): Assemble, configure, and deploy autonomous AI agents in your browser [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/reworkd/AgentGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Agentless✨](https://github.com/OpenAutoCoder/Agentless): an agentless approach to automatically solve software development problems. AGENTLESS, consisting of three phases: localization, repair, and patch validation (self-reflect). [1 Jul 2024] ![**github stars**](https://img.shields.io/github/stars/OpenAutoCoder/Agentless?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Agent-R1✨](https://github.com/0russwest0/Agent-R1): End-to-End reinforcement learning to train agents in specific environments. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/0russwest0/Agent-R1?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1.  [AIDE✨](https://github.com/WecoAI/aideml): The state-of-the-art machine learning engineer agent [Apr 2024] ![**github stars**](https://img.shields.io/github/stars/WecoAI/aideml?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [aider✨](https://github.com/paul-gauthier/aider): AI pair programming in your terminal [Jan 2023]
1. [AIOS✨](https://github.com/agiresearch/AIOS): LLM Agent Operating System [Jan 2024]
1. [Anus: Autonomous Networked Utility System✨](https://github.com/nikmcfly/ANUS): An open-source AI agent framework for task automation, multi-agent collaboration, and web interactions. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/nikmcfly/ANUS?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Archon✨](https://github.com/coleam00/Archon): AI Agent Builder: Example of iteration from Single-Agent to Multi-Agent. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/coleam00/Archon?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ASearcher✨](https://github.com/inclusionAI/ASearcher): ASearcher: An Open-Source Large-Scale Reinforcement Learning Project for Search Agents [11 Aug 2025] ![**github stars**](https://img.shields.io/github/stars/inclusionAI/ASearcher?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Auto_Jobs_Applier_AIHawk✨](https://github.com/feder-cr/Auto_Jobs_Applier_AIHawk): automates the jobs application [Aug 2024]
1. [Auto-GPT✨](https://github.com/Torantulino/Auto-GPT): Most popular [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/Torantulino/Auto-GPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [babyagi✨](https://github.com/yoheinakajima/babyagi): Simplest implementation - Coworking of 4 agents [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/yoheinakajima/babyagi?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [BettaFish✨](https://github.com/666ghj/BettaFish):  A multi-agent public opinion analysis assistant. [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/666ghj/BettaFish?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [BookGPT✨](https://github.com/mikavehns/BookGPT): Generate books based on your specification [Jan 2023]
1. [Cellm✨](https://github.com/getcellm/cellm): Use LLMs in Excel formulas [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/getcellm/cellm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ChatDev✨](https://github.com/OpenBMB/ChatDev): Virtual software company. Create Customized Software using LLM-powered Multi-Agent Collaboration [Sep 2023] ![**github stars**](https://img.shields.io/github/stars/OpenBMB/ChatDev?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Contains Studio AI Agents✨](https://github.com/contains-studio/agents): A comprehensive collection of specialized AI agents. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/contains-studio/agents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Customer Service Agents Demo](https://github.com/openai/openai-cs-agents-demo): OpenAI. Customer Service Agents Demo. [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/openai/openai-cs-agents-demo?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Customer Service Chat with AI Assistant Handoff✨](https://github.com/pereiralex/Simple-bot-handoff-sample): Seamlessly hand off to a human agent when needed. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/pereiralex/Simple-bot-handoff-sample?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DemoGPT✨](https://github.com/melih-unsal/DemoGPT): Automatic generation of LangChain code [Jun 2023]
1. [DeepTutor✨](https://github.com/HKUDS/deeptutor): Personalized AI learning tutor for interactive education [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/HKUDS/deeptutor?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Devon✨](https://github.com/entropy-research/Devon): An open-source pair programmer. [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/entropy-research/Devon?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Dialoqbase✨](https://github.com/n4ze3m/dialoqbase): Create custom chatbots with your own knowledge base using PostgreSQL [Jun 2023]
1. [Dify✨](https://github.com/langgenius/dify): an open-source platform for building applications with LLMs, featuring an intuitive interface for AI workflows and model management. [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/langgenius/dify?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DocsGPT✨](https://github.com/arc53/docsgpt): Chatbot for document with your data [Feb 2023]
1. [Geppeto✨](https://github.com/Deeptechia/geppetto): Advanced Slack bot using multiple AI models [Jan 2024]
1. [GPT Pilot✨](https://github.com/Pythagora-io/gpt-pilot): The first real AI developer. Dev tool that writes scalable apps from scratch while the developer oversees the implementation [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/Pythagora-io/gpt-pilot?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [GPT Researcher✨](https://github.com/assafelovic/gpt-researcher): Autonomous agent designed for comprehensive online research [Jul 2023] / [GPT Newspaper✨](https://github.com/assafelovic/gpt-newspaper): Autonomous agent designed to create personalized newspapers [Jan 2024]
1. [Huginn✨](https://github.com/huginn/huginn): A hackable version of IFTTT or Zapier on your own server for building agents that perform automated tasks. [Mar 2013] ![**github stars**](https://img.shields.io/github/stars/huginn/huginn?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Inbox Zero✨](https://github.com/elie222/inbox-zero): AI personal assistant for email. [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/elie222/inbox-zero?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [Integuru✨](https://github.com/Integuru-AI/Integuru): An AI agent that generates integration code by reverse-engineering platforms' internal APIs. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/Integuru-AI/Integuru?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Khoj✨](https://github.com/khoj-ai/khoj): Open-source, personal AI agents. Cloud or Self-Host, Multiple Interfaces. Python Django based [Aug 2021] ![**github stars**](https://img.shields.io/github/stars/khoj-ai/khoj?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [KnowledgeGPT✨](https://github.com/mmz-001/knowledge_gpt): Upload your documents and get answers to your questions, with citations [Jan 2023]
1. [LlamaFS✨](https://github.com/iyaja/llama-fs): Automatically renames and organizes your files based on their contents [May 2024]
1. [localGPT✨](https://github.com/PromtEngineer/localGPT): Chat with your documents on your local device [May 2023]
1. [M3-Agent✨](https://github.com/bytedance-seed/m3-agent): Seeing, Listening, Remembering, and Reasoning: A Multimodal Agent with Long-Term Memory [13 Aug 2025] ![**github stars**](https://img.shields.io/github/stars/bytedance-seed/m3-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [maestro✨](https://github.com/Doriandarko/maestro): A Framework for Claude Opus, GPT, and local LLMs to Orchestrate Subagents [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/Doriandarko/maestro?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Magentic-One✍️](https://aka.ms/magentic-one): A Generalist Multi-Agent System for Solving Complex Tasks [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/TEN-framework/TEN-Agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Meetily✨](https://github.com/Zackriya-Solutions/meeting-minutes): Open source Ai Assistant for taking meeting notes [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/Zackriya-Solutions/meeting-minutes?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [mgrep✨](https://github.com/mixedbread-ai/mgrep): Natural-language based semantic search as grep. [Nov 2025] ![**github stars**](https://img.shields.io/github/stars/mixedbread-ai/mgrep?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [mindsdb✨](https://github.com/mindsdb/mindsdb): The open-source virtual database for building AI from enterprise data. It supports SQL syntax for development and deployment, with over 70 technology and data integrations. [Aug 2018] ![**github stars**](https://img.shields.io/github/stars/mindsdb/mindsdb?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MineContext✨](https://github.com/volcengine/MineContext): a context-aware AI agent desktop application. [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/volcengine/MineContext?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Mobile-Agent✨](https://github.com/X-PLUG/MobileAgent): The Powerful Mobile Device Operation Assistant Family. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/X-PLUG/MobileAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [myGPTReader✨](https://github.com/myreader-io/myGPTReader): Quickly read and understand any web content through conversations [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/myreader-io/myGPTReader?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenAgents✨](https://github.com/xlang-ai/OpenAgents): Three distinct agents: Data Agent for data analysis, Plugins Agent for plugin integration, and Web Agent for autonomous web browsing. [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/xlang-ai/OpenAgents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenBB✨](https://github.com/OpenBB-finance/OpenBB): The first financial Platform that is free and fully open source. AI-powered workspace [Dec 2020] ![**github stars**](https://img.shields.io/github/stars/OpenBB-finance/OpenBB?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenDAN : Your Personal AIOS✨](https://github.com/fiatrete/OpenDAN-Personal-AI-OS): OpenDAN, an open-source Personal AI OS consolidating various AI modules in one place [May 2023] ![**github stars**](https://img.shields.io/github/stars/fiatrete/OpenDAN-Personal-AI-OS?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenHands✨](https://github.com/All-Hands-AI/OpenHands): OpenHands (formerly OpenDevin), a platform for software development agents [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [open-notebook✨](https://github.com/lfnovo/open-notebook): An Open Source implementation of Notebook LM with more flexibility and features. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/lfnovo/open-notebook?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PageLM✨](https://github.com/CaviraOSS/PageLM/): a community driven version of NotebookLM & a education platform that transforms study materials into interactive resources like quizzes, flashcards, notes, and podcasts. [Aug 2025] ![**github stars**](https://img.shields.io/github/stars/CaviraOSS/PageLM?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PaSa✨](https://github.com/bytedance/pasa): an advanced paper search agent. Bytedance. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/bytedance/pasa?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PDF2Audio✨](https://github.com/lamm-mit/PDF2Audio): an open-source alternative to NotebookLM for podcast creation [Sep 2024]
1. [Podcastfy.ai✨](https://github.com/souzatharsis/podcastfy): An Open Source API alternative to NotebookLM's podcast feature. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/souzatharsis/podcastfy?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Postiz✨](https://github.com/gitroomhq/postiz-app): AI social media scheduling tool. An alternative to: Buffer.com, Hypefury, Twitter Hunter. [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/gitroomhq/postiz-app?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Potpie✨](https://github.com/potpie-ai/potpie): Prompt-To-Agent : Create custom engineering agents for your codebase [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/potpie-ai/potpie?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PR-Agent✨](https://github.com/Codium-ai/pr-agent): Efficient code review and handle pull requests, by providing AI feedbacks and suggestions [Jan 2023] ![**github stars**](https://img.shields.io/github/stars/Codium-ai/pr-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Project Astra](https://deepmind.google/technologies/gemini/project-astra/): Google DeepMind, A universal AI agent that is helpful in everyday life [14 May 2024]
1. [pyspark-ai✨](https://github.com/pyspark-ai/pyspark-ai): English instructions and compile them into PySpark objects like DataFrames. [Apr 2023]
1. [PySpur✨](https://github.com/PySpur-Dev/pyspur): Drag-and-Drop. an AI agent builder in Python. [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/PySpur-Dev/pyspur?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RasaGPT✨](https://github.com/paulpierre/RasaGPT): Built with Rasa, FastAPI, Langchain, and LlamaIndex [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/paulpierre/RasaGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Realtime API Agents Demo✨](https://github.com/openai/openai-realtime-agents): a simple demonstration of more advanced, agentic patterns built on top of the Realtime API. OpenAI. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/openai/openai-realtime-agents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Riona-AI-Agent✨](https://github.com/David-patrick-chuks/Riona-AI-Agent): automation tool designed for Instagram to automate social media interactions such as posting, liking, and commenting. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/David-patrick-chuks/Riona-AI-Agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SakanaAI AI-Scientist✨](https://github.com/SakanaAI/AI-Scientist): Towards Fully Automated Open-Ended Scientific Discovery [Aug 2024]
1. [screenshot-to-code✨](https://github.com/abi/screenshot-to-code): Drop in a screenshot and convert it to clean code (HTML/Tailwind/React/Vue) [Nov 2023]
1. [SeeAct](https://osu-nlp-group.github.io/SeeAct): GPT-4V(ision) is a Generalist Web Agent, if Grounded [✨](https://github.com/OSU-NLP-Group/SeeAct) [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/OSU-NLP-Group/SeeAct?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [skyagi✨](https://github.com/litanlitudan/skyagi): Simulating believable human behaviors. Role playing [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/litanlitudan/skyagi?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [skyvern✨](https://github.com/skyvern-ai/skyvern): Automate browser-based workflows with LLMs and Computer Vision [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/skyvern-ai/skyvern?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SolidGPT✨](https://github.com/AI-Citizen/SolidGPT): AI searching assistant for developers (VSCode Extension) [Aug 2023]
1. [Strix✨](https://github.com/usestrix/strix): Open-source AI Hackers to secure your Apps. [Aug 2025] ![**github stars**](https://img.shields.io/github/stars/usestrix/strix?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SurfSense✨](https://github.com/MODSetter/SurfSense): Open-source alternative to NotebookLM, Perplexity, and Glean — integrates with your personal knowledge base, search engines, Slack, Linear, Notion, YouTube, and GitHub. ![**github stars**](https://img.shields.io/github/stars/MODSetter/SurfSense?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [July 2024]
1. [Suna✨](https://github.com/kortix-ai/suna): a fully open source AI assistant that helps you accomplish real-world tasks [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/kortix-ai/suna?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [tabby✨](https://github.com/TabbyML/tabby): a self-hosted AI coding assistant, offering an open-source and on-premises alternative to GitHub Copilot. [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/TabbyML/tabby?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [TEN Agent✨](https://github.com/TEN-framework/TEN-Agent): The world’s first real-time multimodal agent integrated with the OpenAI Realtime API. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/TEN-framework/TEN-Agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [UpSonic✨](https://github.com/Upsonic/UpSonic): (previously GPT Computer Assistant(GCA)) an AI agent framework designed to make computer use. [May 2024]
1. [ValueCell✨](https://github.com/ValueCell-ai/valuecell): a community-driven, multi-agent platform for financial applications. [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/ValueCell-ai/valuecell?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [WrenAI✨](https://github.com/Canner/WrenAI): Open-source SQL AI Agent for Text-to-SQL [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/Canner/WrenAI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [XAgent✨](https://github.com/OpenBMB/XAgent): Autonomous LLM Agent for complex task solving like data analysis, recommendation, and model training [Oct 2023] ![**github stars**](https://img.shields.io/github/stars/OpenBMB/XAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### No Code & User Interface

1. [ai-town✨](https://github.com/a16z-infra/ai-town): a virtual town where AI characters live, chat and socialize. [Jul 2023] ![**github stars**](https://img.shields.io/github/stars/a16z-infra/ai-town?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [anse✨](https://github.com/anse-app/anse): UI for multiple models such as ChatGPT, DALL-E and Stable Diffusion. [Apr 2023]
1. [anything-llm✨](https://github.com/Mintplex-Labs/anything-llm): All-in-one Desktop & Docker AI application with built-in RAG, AI agents, and more. [Jun 2023] ![**github stars**](https://img.shields.io/github/stars/Mintplex-Labs/anything-llm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AppAgent-TencentQQGYLab✨](https://github.com/mnotgod96/AppAgent): Multimodal Agents as Smartphone Users. [Dec 2023] ![**github stars**](https://img.shields.io/github/stars/mnotgod96/AppAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [BIG-AGI✨](https://github.com/enricoros/big-agi) FKA nextjs-chatgpt-app [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/enricoros/big-agi?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [browser-use✨](https://github.com/browser-use/browser-use): Make websites accessible for AI agents. [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/browser-use/browser-use?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ChainForge✨](https://github.com/ianarawjo/ChainForge): An open-source visual programming environment for battle-testing prompts to LLMs. [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/ianarawjo/ChainForge?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [chainlit✨](https://github.com/Chainlit/chainlit):💡Build production-ready Conversational AI applications in minutes. [Mar 2023]
1. [ChatGPT-Next-Web✨](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web): Open-source GPT wrapper. [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/ChatGPTNextWeb/ChatGPT-Next-Web?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ChatHub✨](https://github.com/chathub-dev/chathub): All-in-one chatbot client [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/chathub-dev/chathub?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [CopilotKit✨](https://github.com/CopilotKit/CopilotKit): Built-in React UI components [Jun 2023]
1. [coze-studio✨](https://github.com/coze-dev/coze-studio): An AI agent development platform with all-in-one visual tools, simplifying agent creation, debugging, and deployment like never before. Coze your way to AI Agent creation. [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/coze-dev/coze-studio?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [dataline✨](https://github.com/RamiAwar/dataline): Chat with your data - AI data analysis and visualization [Apr 2023]
1. [Deepnote✨](https://github.com/deepnote/deepnote): A successor of Jupyter. a data notebook for the AI. [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/deepnote/deepnote?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ElevenLabs UI✨](https://github.com/elevenlabs/ui): a component library built on top of shadcn/ui to help you build audio & agentic applications [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/elevenlabs/ui?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [FastGPT✨](https://github.com/labring/FastGPT): Open-source GPT wrapper. [Feb 2023] ![**github stars**](https://img.shields.io/github/stars/labring/FastGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Flowise✨](https://github.com/FlowiseAI/Flowise): Drag & drop UI to build your customized LLM flow [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/FlowiseAI/Flowise?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Google Workspace Studio](https://workspace.google.com/studio/): No-code builder for Workspace chat apps, add-ons, and automations powered by Gemini. [Sep 2024]
1. [Google Workspace Studio with Agents✍️](https://workspaceupdates.googleblog.com/2025/12/workspace-studio.html): Adds agent creation to automate work inside Workspace Studio. [3 Dec 2025]
1. [GPT 学术优化 (GPT Academic)✨](https://github.com/binary-husky/gpt_academic): UI Platform for Academic & Coding Tasks. Optimized for paper reading, writing, and editing. [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/binary-husky/gpt_academic?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Gradio✨](https://github.com/gradio-app/gradio): Build Machine Learning Web Apps - in Python [Mar 2023]
1. [Kiln✨](https://github.com/Kiln-AI/Kiln): Desktop Apps for for fine-tuning LLM models, synthetic data generation, and collaborating on datasets. [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/Kiln-AI/Kiln?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [knowledge✨](https://github.com/KnowledgeCanvas/knowledge): Tool for saving, searching, accessing, and exploring websites and files. Electron based app, built-in Chromium browser, knowledge graph [Jul 2021] ![**github stars**](https://img.shields.io/github/stars/KnowledgeCanvas/knowledge?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [langflow✨](https://github.com/langflow-ai/langflow): LangFlow is a UI for LangChain, designed with react-flow. [Feb 2023]
1. [langfuse✨](https://github.com/langfuse/langfuse): Traces, evals, prompt management and metrics to debug and improve your LLM application. [May 2023]
1. [LangGraph✨](https://github.com/langchain-ai/langgraph): Built on top of LangChain [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Letta ADE✨](https://github.com/letta-ai/letta): a graphical user interface for ADE (Agent Development Environment) by [Letta (previously MemGPT)✨](https://github.com/letta-ai/letta) [12 Oct 2023]
1. [LibreChat✨](https://github.com/danny-avila/LibreChat): a free, open source AI chat platform. [8 Mar 2023] ![**github stars**](https://img.shields.io/github/stars/danny-avila/LibreChat?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LM Studio](https://lmstudio.ai/): UI for Discover, download, and run local LLMs [May 2024]
1. [Lobe Chat✨](https://github.com/lobehub/lobe-chat): Open-source GPT wrapper. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/lobehub/lobe-chat?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [mesop✨](https://github.com/mesop-dev/mesop): Rapidly build AI apps in Python [Oct 2023] ![**github stars**](https://img.shields.io/github/stars/mesop-dev/mesop?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [n8n✨](https://github.com/n8n-io/n8n): A workflow automation tool for integrating various tools. [Jan 2019] ![**github stars**](https://img.shields.io/github/stars/n8n-io/n8n?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [nanobrowser✨](https://github.com/nanobrowser/nanobrowser): Open-source Chrome extension for AI-powered web automation. Alternative to OpenAI Operator. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/nanobrowser/nanobrowser?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Next.js AI Chatbot✨](https://github.com/vercel/ai-chatbot):💡An Open-Source AI Chatbot Template Built With Next.js and the AI SDK by Vercel. [May 2023] ![**github stars**](https://img.shields.io/github/stars/vercel/ai-chatbot?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [NocoBase✨](https://github.com/nocobase/nocobase): Data model-driven. AI-powered no-code platform. [Oct 2020] ![**github stars**](https://img.shields.io/github/stars/nocobase/nocobase?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Nyro✨](https://github.com/trynyro/nyro-app): AI-Powered Desktop Productivity Tool [Aug 2024]
1. [Open WebUI✨](https://github.com/open-webui/open-webui): User-friendly AI Interface (Supports Ollama, OpenAI API, ...) [Oct 2023] ![**github stars**](https://img.shields.io/github/stars/open-webui/open-webui?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Refly✨](https://github.com/refly-ai/refly): WYSIWYG AI editor to create llm application. [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/refly-ai/refly?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Sim Studio✨](https://github.com/simstudioai/sim): A Figma-like canvas to build agent workflow. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/simstudioai/sim?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [streamlit✨](https://github.com/streamlit/streamlit):💡Streamlit — A faster way to build and share data apps. [Jan 2018] ![**github stars**](https://img.shields.io/github/stars/streamlit/streamlit?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [TaxyAI/browser-extension✨](https://github.com/TaxyAI/browser-extension): Browser Automation by Chrome debugger API and Prompt > `src/helpers/determineNextAction.ts` [Mar 2023]
1. [Text generation web UI✨](https://github.com/oobabooga/text-generation-webui): Text generation web UI [Mar 2023]
1. [Visual Blocks✨](https://github.com/google/visualblocks): Google visual programming framework that lets you create ML pipelines in a no-code graph editor. [Mar 2023]

#### Infrastructure & Backend Services

1. [Azure OpenAI Proxy✨](https://github.com/scalaone/azure-openai-proxy): OpenAI API requests converting into Azure OpenAI API requests [Mar 2023]
1. [BISHENG✨](https://github.com/dataelement/bisheng): an open LLM application devops platform, focusing on enterprise scenarios. [Aug 2023]
1. [Botpress Cloud✨](https://github.com/botpress/botpress): The open-source hub to build & deploy GPT/LLM Agents. [Nov 2016] ![**github stars**](https://img.shields.io/github/stars/botpress/botpress?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [E2B✨](https://github.com/e2b-dev/e2b): an open-source infrastructure that allows you run to AI-generated code in secure isolated sandboxes in the cloud. [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/e2b-dev/e2b?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [exo✨](https://github.com/exo-explore/exo): Run your own AI cluster at home with everyday devices [Jun 2024]
1. [GPT4All✨](https://github.com/nomic-ai/gpt4all): Open-source large language models that run locally on your CPU [Mar 2023]
1. [guardrails✨](https://github.com/guardrails-ai/guardrails): Adding guardrails to large language models. [Jan 2023]
1. [Harbor✨](https://github.com/av/harbor): Effortlessly run LLM backends, APIs, frontends, and services with one command. a helper for the local LLM development environment. [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/av/harbor?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [keep✨](https://github.com/keephq/keep): The open-source AIOps and alert management platform [Feb 2023] ![**github stars**](https://img.shields.io/github/stars/keephq/keep?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [KTransformers✨](https://github.com/kvcache-ai/ktransformers): A Flexible Framework for Experiencing Cutting-edge LLM Inference Optimizations [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/kvcache-ai/ktransformers?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LLaMA-Factory✨](https://github.com/hiyouga/LLaMA-Factory): Unify Efficient Fine-Tuning of 100+ LLMs [May 2023]
1. [mosaicml/llm-foundry✨](https://github.com/mosaicml/llm-foundry): LLM training code for MosaicML foundation models [Jun 2022]
1. [Meta Lingua✨](https://github.com/facebookresearch/lingua): a minimal and fast LLM training and inference library designed for research. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/facebookresearch/lingua?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ollama✨](https://github.com/jmorganca/ollama):💡Running with Large language models locally [Jun 2023]
1. [promptomatix✨](https://github.com/SalesforceAIResearch/promptomatix/): An Automatic Prompt Optimization Framework for Large Language Models [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/SalesforceAIResearch/promptomatix?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Reranker✨](https://github.com/luyug/Reranker): Training and deploying deep languge model reranker in information retrieval (IR), question answering (QA) [Jan 2021] ![**github stars**](https://img.shields.io/github/stars/luyug/Reranker?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Tinker Cookbook✨](https://github.com/thinking-machines-lab/tinker-cookbook): Thinking Machines Lab. Training SDK to fine-tune language models. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/thinking-machines-lab/tinker-cookbook?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RLinf✨](https://github.com/RLinf/RLinf): Post-training foundation models (LLMs, VLMs, VLAs) via reinforcement learning. [Aug 2025] ![**github stars**](https://img.shields.io/github/stars/RLinf/RLinf?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Semantic Router✨](https://github.com/aurelio-labs/semantic-router): Decision routing for LLMs and agents using semantic vector intelligence. [Oct 2023] ![**github stars**](https://img.shields.io/github/stars/aurelio-labs/semantic-router?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ThinkGPT✨](https://github.com/jina-ai/thinkgpt): Chain of Thoughts library [Apr 2023]
1. [Transformers✨](https://github.com/huggingface/transformers): 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX. (github.com) [Oct 2018]
1. [Transformer Lab✨](https://github.com/transformerlab/transformerlab-app): Open Source Application for Advanced LLM + Diffusion Engineering: interact, train, fine-tune, and evaluation. [Dec 2023] ![**github stars**](https://img.shields.io/github/stars/transformerlab/transformerlab-app?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [unsloth✨](https://github.com/unslothai/unsloth): Finetune Mistral, Gemma, Llama 2-5x faster with less memory! [Nov 2023]
1. [verl✨](https://github.com/volcengine/verl): ByteDance. RL training library for LLMs [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/volcengine/verl?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [vLLM✨](https://github.com/vllm-project/vllm): Easy-to-use library for LLM inference and serving. [Feb 2023]
1. [vllm-omni✨](https://github.com/vllm-project/vllm-omni): A framework for efficient model inference with omni-modality models [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/vllm-project/vllm-omni?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [YaFSDP✨](https://github.com/yandex/YaFSDP): Yet another Fully Sharded Data Parallel (FSDP): enhanced for distributed training. YaFSDP vs DeepSpeed. [May 2024]
1. [WebLLM✨](https://github.com/mlc-ai/web-llm): High-Performance In-Browser LLM Inference Engine. [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/mlc-ai/web-llm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Weights & Biases✨](https://github.com/wandb/examples): Visualizing and tracking your machine learning experiments [wandb.ai](https://wandb.ai/) doc: `deeplearning.ai/wandb` [Jan 2020]

#### **Caching**

- Caching: A technique to store data that has been previously retrieved or computed, so that future requests for the same data can be served faster.
- To reduce latency, cost, and LLM requests by serving pre-computed or previously served responses.
- Strategies for caching: Caching can be based on item IDs, pairs of item IDs, constrained input, or pre-computation. Caching can also leverage embedding-based retrieval, approximate nearest neighbor search, and LLM-based evaluation. [✍️](https://eugeneyan.com/writing/llm-patterns/#caching-to-reduce-latency-and-cost)
- GPTCache: Semantic cache for LLMs. Fully integrated with LangChain and llama_index. [✨](https://github.com/zilliztech/GPTCache) [Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/zilliztech/GPTCache?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Prompt Cache: Modular Attention Reuse for Low-Latency Inference📑](https://arxiv.org/abs/2311.04934): LLM inference by reusing precomputed attention states from overlapping prompts. [7 Nov 2023]
- [Prompt caching with Claude✍️](https://www.anthropic.com/news/prompt-caching): Reducing costs by up to 90% and latency by up to 85% for long prompts. [15 Aug 2024]

#### **Data Processing**

1. [activeloopai/deeplake✨](https://github.com/activeloopai/deeplake): AI Vector Database for LLMs/LangChain. Doubles as a Data Lake for Deep Learning. Store, query, version, & visualize any data. Stream data in real-time to PyTorch/TensorFlow. [✍️](https://activeloop.ai) [Jun 2021]
![**github stars**](https://img.shields.io/github/stars/activeloopai/deeplake?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AI Sheets✨🤗](https://github.com/huggingface/aisheets): an open-source tool for building, enriching, and transforming datasets using AI models with no code. ![**github stars**](https://img.shields.io/github/stars/huggingface/aisheets?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Camelot✨](https://github.com/camelot-dev/camelot) a Python library that can help you extract tables from PDFs! [✨](https://github.com/camelot-dev/camelot/wiki/Comparison-with-other-PDF-Table-Extraction-libraries-and-tools): Comparison with other PDF Table Extraction libraries [Jul 2016]
![**github stars**](https://img.shields.io/github/stars/camelot-dev/camelot?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [chandra✨](https://github.com/datalab-to/chandra/): OCR model that handles complex tables, forms, handwriting with full layout. [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/datalab-to/chandra?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
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
1. [PaperDebugger✨](https://github.com/PaperDebugger/PaperDebugger): Debug and improve LaTeX papers with intelligent suggestions. [📑](https://arxiv.org/abs/2512.02589) [2 Dec 2025] ![**github stars**](https://img.shields.io/github/stars/PaperDebugger/PaperDebugger?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MegaParse✨](https://github.com/quivrhq/megaparse): a powerful and versatile parser that can handle various types of documents. Focus on having no information loss during parsing. [30 May 2024] ![**github stars**](https://img.shields.io/github/stars/quivrhq/megaparse?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Nougat📑](https://arxiv.org/abs/2308.13418): Neural Optical Understanding for Academic Documents: The academic document PDF parser that understands LaTeX math and tables. [✨](https://github.com/facebookresearch/nougat) [25 Aug 2023]
![**github stars**](https://img.shields.io/github/stars/facebookresearch/nougat?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Ollama OCR✨](https://github.com/imanoop7/Ollama-OCR): A powerful OCR (Optical Character Recognition) package that uses state-of-the-art vision language models. [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/imanoop7/Ollama-OCR?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [outlines✨](https://github.com/dottxt-ai/outlines): Structured Text Generation [Mar 2023]
![**github stars**](https://img.shields.io/github/stars/dottxt-ai/outlines?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PaddleOCR✨](https://github.com/PaddlePaddle/PaddleOCR): Turn any PDF or image document into structured data. [May 2020] ![**github stars**](https://img.shields.io/github/stars/PaddlePaddle/PaddleOCR?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [pandas-ai✨](https://github.com/Sinaptik-AI/pandas-ai): Chat with your database (SQL, CSV, pandas, polars, mongodb, noSQL, etc). [Apr 2023] ![**github stars**](https://img.shields.io/github/stars/Sinaptik-AI/pandas-ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Paperless-AI✨](https://github.com/clusterzx/paperless-ai): An automated document analyzer for Paperless-ngx using OpenAI API, Ollama and all OpenAI API compatible Services to automatically analyze and tag your documents. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/clusterzx/paperless-ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Parsr✨](https://github.com/axa-group/Parsr): Document parsing and extraction into structured data. [Aug 2019] ![**github stars**](https://img.shields.io/github/stars/axa-group/Parsr?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [pipet✨](https://github.com/bjesus/pipet): Swiss-army tool for scraping and extracting data from online [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/bjesus/pipet?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [PostgresML✨](https://github.com/postgresml/postgresml): The GPU-powered AI application database. [Apr 2022]
![**github stars**](https://img.shields.io/github/stars/postgresml/postgresml?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [semchunk✨](https://github.com/isaacus-dev/semchunk): A fast, lightweight semantic chunking library. Splitting text into semantically meaningful chunks. [Nov 2023] ![**github stars**](https://img.shields.io/github/stars/isaacus-dev/semchunk?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [surya✨](https://github.com/VikParuchuri/surya): OCR, layout analysis, reading order, table recognition in 90+ languages [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/VikParuchuri/surya?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Trafilatura✨](https://github.com/adbar/trafilatura): Gather text from the web and convert raw HTML into structured, meaningful data. [Apr 2019]
![**github stars**](https://img.shields.io/github/stars/adbar/trafilatura?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Token-Oriented Object Notation (TOON)✨](https://github.com/toon-format/toon): a compact, human-readable serialization format designed for passing structured data with significantly reduced token usage. [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/toon-format/toon?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [unstructured✨](https://github.com/Unstructured-IO/unstructured): Open-Source Pre-Processing Tools for Unstructured Data [Sep 2022]
![**github stars**](https://img.shields.io/github/stars/Unstructured-IO/unstructured?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [WaterCrawl✨](https://github.com/watercrawl/WaterCrawl): Transform Web Content into LLM-Ready Data. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/watercrawl/WaterCrawl?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Zerox OCR✨](https://github.com/getomni-ai/zerox): Zero shot pdf OCR with gpt-4o-mini [Jul 2024]
![**github stars**](https://img.shields.io/github/stars/getomni-ai/zerox?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **Gateway**

1. [AI Gateway✨](https://github.com/Portkey-AI/gateway): AI Gateway with integrated guardrails. Route to 200+ LLMs, 50+ AI Guardrails [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/Portkey-AI/gateway?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [aisuite✨](https://github.com/andrewyng/aisuite): Andrew Ng launches a tool offering a simple, unified interface for multiple generative AI providers. [26 Nov 2024] ![**github stars**](https://img.shields.io/github/stars/andrewyng/aisuite?style=flat-square&label=%20&color=blue&cacheSeconds=36000) vs [litellm✨](https://github.com/BerriAI/litellm) vs [OpenRouter✨](https://github.com/OpenRouterTeam/openrouter-runner)
1. [litellm✨](https://github.com/BerriAI/litellm): Python SDK to call 100+ LLM APIs in OpenAI format [Jul 2023]
![**github stars**](https://img.shields.io/github/stars/BerriAI/litellm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LocalAI✨](https://github.com/mudler/LocalAI): The free, Open Source alternative to OpenAI, Claude and others. Self-hosted and local-first. [Mar 2023] ![**github stars**](https://img.shields.io/github/stars/mudler/LocalAI?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Petals✨](https://github.com/bigscience-workshop/petals): Run LLMs at home, BitTorrent-style. Fine-tuning and inference up to 10x faster than offloading [Jun 2022] ![**github stars**](https://img.shields.io/github/stars/bigscience-workshop/petals?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [RouteLLM✨](https://github.com/lm-sys/RouteLLM): A framework for serving and evaluating LLM routers [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/lm-sys/RouteLLM?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **Memory**

1. [Acontext✨](https://github.com/memodb-io/Acontext): A context data platform for cloud-native AI Agent. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/memodb-io/Acontext?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Agentic Memory✨](https://github.com/agiresearch/A-mem): A dynamic memory system for LLM agents, inspired by the Zettelkasten method, enabling flexible memory organization. [17 Feb 2025] ![**github stars**](https://img.shields.io/github/stars/agiresearch/A-mem?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [claude-mem✨](https://github.com/thedotmack/claude-mem): A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI (using Claude's agent-sdk), and injects relevant context back into future sessions. [Aug 2025] ![**github stars**](https://img.shields.io/github/stars/thedotmack/claude-mem?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [cognee✨](https://github.com/topoteretes/cognee): LLM Memory using Dynamic knowledge graphs (lightweight ECL pipelines) [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/topoteretes/cognee?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [EverMemOS✨](https://github.com/EverMind-AI/EverMemOS): A long-term memory layer composed of a Memory Construction Layer and a Memory Perception Layer. [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/EverMind-AI/EverMemOS?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Gemini Memory✍️](https://www.shloked.com/writing/gemini-memory): Gemini uses a structured, typeed “user_context” summary with timestamps, accessed only when you explicitly ask. simpler and more unified than ChatGPT or Claude, and it rarely uses data from the Google ecosystem. [19 Nov 2025]
1. [Graphiti✨](https://github.com/getzep/graphiti): Graphiti leverages [zep✨](https://github.com/getzep/zep)'s memory layer. Build Real-Time Knowledge Graphs for AI Agents [Aug 2024] ![**github stars**](https://img.shields.io/github/stars/getzep/graphiti?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [I Reverse Engineered **ChatGPT's Memory** System✍️](https://manthanguptaa.in/posts/chatgpt_memory/): A non–vector-DB log of past chats: a lightweight layyered system—session metadata, long-term user facts, recent-chat summaries, and current messages—built to provide personalization and context without storing full conversation histories. [9 Dec 2025]
1. [Letta (previously MemGPT)✨](https://github.com/letta-ai/letta): Virtual context management to extend the limited context of LLM. A tiered memory system and a set of functions that allow it to manage its own memory. [✍️](https://memgpt.ai) / [git:old✨](https://github.com/cpacker/MemGPT) [12 Oct 2023] ![**github stars**](https://img.shields.io/github/stars/letta-ai/letta?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Making Sense of Memory in AI Agents](https://leoniemonigatti.com/blog/memory-in-ai-agents.html) & [Exploring Anthropic’s Memory Tool](https://leoniemonigatti.com/blog/claude-memory-tool.html): How agents remember, recall, and (struggle to) forget information. [25 Nov 2025]
1. [Mem0✨](https://github.com/mem0ai/mem0):💡A self-improving memory layer for personalized AI experiences. [Jun 2023]
![**github stars**](https://img.shields.io/github/stars/mem0ai/mem0?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  | [Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory📑](https://arxiv.org/abs/2504.19413) [28 Apr 2025]  
1. [Memary✨](https://github.com/kingjulio8238/Memary): memary mimics how human memory evolves and learns over time. The memory module comprises the Memory Stream and Entity Knowledge Store. [May 2024] ![**github stars**](https://img.shields.io/github/stars/kingjulio8238/Memary?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Memori✨](https://github.com/GibsonAI/Memori): a SQL native memory engine (SQLite, PostgreSQL, MySQL) [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/GibsonAI/Memori?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenMemory✨](https://github.com/CaviraOSS/OpenMemory): Long-term memory for AI systems. Open source, self-hosted, and explainable. [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/CaviraOSS/OpenMemory?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [zep✨](https://github.com/getzep/zep): Long term memory layer. Zep intelligently integrates new information into the user's Knowledge Graph. ![**github stars**](https://img.shields.io/github/stars/getzep/zep?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [May 2023]


### **Agent Protocol**

#### **Model Context Protocol (MCP)**

- [A Survey of AI Agent Protocols📑](https://arxiv.org/abs/2504.16736) [23 Apr 2025]
- [Awesome MCP Servers✨](https://github.com/kimtth/awesome-mcp-servers): Original repository deleted; Redirecting to the forked repository.
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
1. [mcp-agent✨](https://github.com/lastmile-ai/mcp-agent): Build effective agents using Model Context Protocol and simple workflow patterns [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/lastmile-ai/mcp-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [mcp-scan✨](https://github.com/invariantlabs-ai/mcp-scan): Auto-discover MCP Security Vulnerabilities. [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/invariantlabs-ai/mcp-scan?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [mcp-ui✨](https://github.com/idosal/mcp-ui): SDK for UI over MCP. Create next-gen UI experiences! [May 2025] ![**github stars**](https://img.shields.io/github/stars/idosal/mcp-ui?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [mcp-use✨](https://github.com/mcp-use/mcp-use): MCP Client Library to connect any LLM to any MCP server [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/mcp-use/mcp-use?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MCP Registry](https://github.com/mcp): Github. centralizes Model Context Protocol (MCP) servers, facilitating the discovery and integration of AI tools with external data sources and services. [16 Sep 2025]
1. [MCP Run Python](https://ai.pydantic.dev/mcp/run-python/): PydanticAI. Use Pyodide to run Python code in a JavaScript environment with Deno [19 Mar 2025]
1. [Programmatic Tool Calling (PTC) Demo✨](https://github.com/Chen-zexi/open-ptc-agent): An open source implementation of code execution with MCP (Programatic Tool Calling) [Nov 2025] ![**github stars**](https://img.shields.io/github/stars/Chen-zexi/open-ptc-agent?style=flat-square&label=%20&cacheSeconds=36000)

#### **A2A**

1. [A2A✨](https://github.com/google/A2A): Google. Agent2Agent (A2A) protocol. Agent Card (metadata: self-description). Task (a unit of work). Artifact (output). Streaming (Long-running tasks). Leverages HTTP, SSE, and JSON-RPC. Multi-modality incl. interacting with UI components [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/google/A2A?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [a2a-python✨](https://github.com/google-a2a/a2a-python): Official Python SDK for the Agent2Agent (A2A) Protocol [May 2025] ![**github stars**](https://img.shields.io/github/stars/google-a2a/a2a-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ag-ui✨](https://github.com/ag-ui-protocol/ag-ui/): Integrating Agent-User Interaction Protocol into Front-end Applications. [May 2025]
1. [AI Agent Architecture via A2A/MCP](https://medium.com/@jeffreymrichter/ai-agent-architecture-b864080c4bbc): Jeffrey Richter [4 Jun 2025]
1. [Python A2A✨](https://github.com/themanojdesai/python-a2a): Python Implementation of Google's Agent-to-Agent (A2A) Protocol with Model Context Protocol (MCP) Integration [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/themanojdesai/python-a2a?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SharpA2A✨](https://github.com/darrelmiller/sharpa2a): A .NET implementation of the Google A2A protocol. [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/darrelmiller/sharpa2a?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **Computer use**

- [ACU - Awesome Agents for Computer Use✨](https://github.com/francedot/acu) ![**github stars**](https://img.shields.io/github/stars/francedot/acu?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Anthropic Claude's computer use✍️](https://www.anthropic.com/news/developing-computer-use): [23 Oct 2024]
- [Computer Agent Arena Leaderboard](https://arena.xlang.ai/leaderboard) [Apr 2025]
1. [Agent.exe✨](https://github.com/corbt/agent.exe): Electron app to use computer use APIs. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/corbt/agent.exe?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [CogAgent✨](https://github.com/THUDM/CogAgent): An open-sourced end-to-end VLM-based GUI Agent [Dec 2023] ![**github stars**](https://img.shields.io/github/stars/THUDM/CogAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Computer Use OOTB✨](https://github.com/showlab/computer_use_ootb): Out-of-the-box (OOTB) GUI Agent for Windows and macOS. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/showlab/computer_use_ootb?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [cua✨](https://github.com/trycua/cua): Open-source infrastructure for Computer-Use Agents. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/trycua/cua?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Open-Interface✨](https://github.com/AmberSahdev/Open-Interface/): LLM backend (GPT-4V, etc), supporting Linux, Mac, Windows. [Jan 2024] ![**github stars**](https://img.shields.io/github/stars/AmberSahdev/Open-Interface?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Open Operator✨](https://github.com/browserbase/open-operator): a web agent based on Browserbase [24 Jan 2025] ![**github stars**](https://img.shields.io/github/stars/browserbase/open-operator?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [OpenAI Operator✍️](https://openai.com/index/introducing-operator/) [23 Jan 2025]
1. [OpenInterpreter starts to support Computer Use API✨](https://github.com/OpenInterpreter/open-interpreter/issues/1490)
1. [Self-Operating Computer Framework✨](https://github.com/OthersideAI/self-operating-computer): A framework to enable multimodal models to operate a computer. [Nov 2023] ![**github stars**](https://img.shields.io/github/stars/OthersideAI/self-operating-computer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Stagehand✨](https://github.com/browserbase/stagehand): The AI Browser Automation Framework . Stagehand lets you preview AI actions before running. Computer use models with one line of code. [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/browserbase/stagehand?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [UI-TARS📑](https://arxiv.org/abs/2501.12326): An agent model built on Qwen-2-VL for seamless GUI interaction, by ByteDance. [✨](https://github.com/bytedance/UI-TARS) / Application [✨](https://github.com/bytedance/UI-TARS-desktop) ![**github stars**](https://img.shields.io/github/stars/bytedance/UI-TARS-desktop?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [21 Jan 2025]
1. [UFO✨](https://github.com/microsoft/UFO): Windows Control

### **Coding & Research**

#### Coding

1. [Auto-Claude✨](https://github.com/AndyMik90/Auto-Claude): Autonomous multi-session AI coding [Dec 2025] ![**github stars**](https://img.shields.io/github/stars/AndyMik90/Auto-Claude?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [bolt.new✨](https://github.com/stackblitz/bolt.new): Dev Sanbox with AI from stackblitz [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/stackblitz/bolt.new?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Claude sub-agents collection✨](https://github.com/wshobson/agents): A collection of production-ready subagents for Claude Code. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/wshobson/agents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [claude-code✨](https://github.com/anthropics/claude-code): a terminal-based agentic coding tool that understands your codebase and speeds up development by executing tasks, explaining code, and managing git—all via natural language commands. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/anthropics/claude-code?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [claude‑squad✨](https://github.com/smtg-ai/claude-squad): Terminal app to manage multiple AI assistants (Claude Code, Aider, Codex). [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/smtg-ai/claude-squad?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Cline✨](https://github.com/cline/cline): CLI aNd Editor. Autonomous coding agent. VSCode Extension. [Jul 2024] ![**github stars**](https://img.shields.io/github/stars/cline/cline?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [code2prompt✨](https://github.com/mufeedvh/code2prompt/): a command-line tool (CLI) that converts your codebase into a single LLM prompt with a source tree [Mar 2024]
1. [Code Shaping✨](https://github.com/CodeShaping/code-shaping): Editing code with free-form sketch annotations on the code and console output. [6 Feb 2025] [ref📑](https://arxiv.org/abs/2502.03719) ![**github stars**](https://img.shields.io/github/stars/CodeShaping/code-shaping?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [CodeLLM by Abacus.AI](https://codellm.abacus.ai/): AI-powered code editor with automatic selection of state-of-the-art LLMs based on coding tasks. [Dec 2024]
1. [codegen✨](https://github.com/codegen-sh/codegen): Python SDK to interact with intelligent code generation agents [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/codegen-sh/codegen?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [codex✨](https://github.com/openai/codex): OpenAI. Lightweight coding agent that runs in your terminal [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/openai/codex?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Cofounder✨](https://github.com/raidendotai/cofounder): full stack generative web apps ; backend + db + stateful web apps [Sep 2024] ![**github stars**](https://img.shields.io/github/stars/raidendotai/cofounder?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Continue✨](https://github.com/continuedev/continue): open-source AI code assistant inside of VS Code and JetBrains. [May 2023] ![**github stars**](https://img.shields.io/github/stars/continuedev/continue?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [crush✨](https://github.com/charmbracelet/crush): The glamorous AI coding agent for your favourite terminal. [May 2025] ![**github stars**](https://img.shields.io/github/stars/charmbracelet/crush?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Cursor](https://www.cursor.com/) [Mar 2023]
1. [DeepCode✨](https://github.com/HKUDS/DeepCode): Open Agentic Coding (Paper2Code & Text2Web & Text2Backend) [May 2025] ![**github stars**](https://img.shields.io/github/stars/HKUDS/DeepCode?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DeepSeek Engineer✨](https://github.com/Doriandarko/deepseek-engineer): Simple and just a few lines of code. a powerful coding assistant application that integrates with the DeepSeek API [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/Doriandarko/deepseek-engineer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DeepWiki](https://deepwiki.com/): Devin AI. a tool that converts any public GitHub repository into an interactive, wiki-style documentation. [25 Apr 2025]
1. [DeepWiki-Open✨](https://github.com/AsyncFuncAI/deepwiki-open): Open Source DeepWiki: AI-Powered Wiki Generator for GitHub/Gitlab/Bitbucket [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/AsyncFuncAI/deepwiki-open?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Deepsite🤗](https://huggingface.co/spaces/enzostvs/deepsite): Mockup UI generator Powered by Deepseek [Mar 2025]
1. [devin.cursorrules✨](https://github.com/grapeot/devin.cursorrules): Transform your Cursor or Windsurf IDE into a Devin-like AI Assistant [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/grapeot/devin.cursorrules?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Firebase Studio](https://firebase.google.com/studio): Google. a cloud-based, agentic development environment. [14 May 2024]
1. [Figma Make](https://www.figma.com/make/): Use existing Figma files or even images to kickstart your project. React（TypeScript）. Claude 3.7 Sonnet. [7 May 2025]
1. [Flowith Agent Neo](https://flowith.io): 24/7 operation for very long and complex tasks. Top of GAIA (General AI Assistant benchmark). 1,000 inference steps in a single task. Up to 10 million tokens of context. Cloud-based execution [21 May 2025]
1. [gastown✨](https://github.com/steveyegge/gastown): Multi-agent orchestration system for Claude Code with persistent work tracking [Dec 2025] ![**github stars**](https://img.shields.io/github/stars/steveyegge/gastown?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Gemini CLI✨](https://github.com/google-gemini/gemini-cli): An open-source AI agent that brings the power of Gemini directly into your terminal.  [April 2025] ![**github stars**](https://img.shields.io/github/stars/google-gemini/gemini-cli?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [GitHub Copilot✨](https://github.com/features/copilot):🏆 AI pair programmer by GitHub and OpenAI. Supports VS Code, Visual Studio, Neovim, and JetBrains IDEs. [29 Jun 2021] > [Awesome GitHub Copilot Customizations](https://github.com/github/awesome-copilot): Official curated collection.
1. [Github Spark](https://githubnext.com/projects/github-spark): an AI-powered tool for creating and sharing micro apps (“sparks”) [29 Oct 2024]
1. [Google Antigravity✍️](https://antigravity.google/): A VSCode‑forked IDE with an artifacts conceept, similar to Claude. [18 Nov 2025]
1. [Google CodeWiki](https://codewiki.google/): AI-powered documentation platform that automatically transforms any GitHub repository into comprehensive documentation. [13 Nov 2025]
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
1. [plannotator✨](https://github.com/backnotprop/plannotator?tab=readme-ov-file): Annotate and review coding agent plans visually, share with your team, send feedback with one click. [Dec 2025] ![**github stars**](https://img.shields.io/github/stars/backnotprop/plannotator?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Replit Agent](https://replit.com/) [09 Sep 2024]
1. [Ruler✨](https://github.com/intellectronica/ruler): Centralise Your AI Coding Assistant Instructions [May 2025] ![**github stars**](https://img.shields.io/github/stars/intellectronica/ruler?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Task Master✨](https://github.com/eyaltoledano/claude-task-master): Personal Project Manager. A task management system for AI-driven development. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/eyaltoledano/claude-task-master?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Trae](https://www.trae.ai/): Bytedance. Free, but not open-source. [20 Jan 2025]
1. [Vercel AI✨](https://github.com/vercel/ai) Vercel AI Toolkit for TypeScript [May 2023] ![**github stars**](https://img.shields.io/github/stars/vercel/ai?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [void✨](https://github.com/voideditor/void) OSS Cursor alternative. a fork of vscode [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/voideditor/void?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [WebAgent✨](https://github.com/Alibaba-NLP/WebAgent): WebAgent for Information Seeking built by Tongyi Lab: WebWalker & WebDancer & WebSailor & WebShaper. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/Alibaba-NLP/WebAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Windsurf editor](https://codeium.com/windsurf): Flows = Agents + Copilots. Cascades (a specific implementation of AI Flows. Advanced chat interface). [13 Nov 2024]
1. [Zed✨](https://github.com/zed-industries/zed): a high-performance, multiplayer code editor. the creators of Atom and Tree-sitter. [Feb 2021] ![**github stars**](https://img.shields.io/github/stars/zed-industries/zed?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### Skill

1. [Agent-Skills-for-Context-Engineering✨](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering): A comprehensive collection of Agent Skills for context engineering, multi-agent architectures, and production agent systems. Use when building, optimizing, or debugging agent systems that require effective context management. [Dec 2025] ![**github stars**](https://img.shields.io/github/stars/muratcankoylan/Agent-Skills-for-Context-Engineering?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [agentskills✨](https://github.com/agentskills/agentskills): Specification and documentation for Agent Skills [Dec 2025] ![**github stars**](https://img.shields.io/github/stars/agentskills/agentskills?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Awesome GitHub Copilot Customizations✨](https://github.com/github/awesome-copilot): 💡Community-contributed instructions, prompts, and skills, configurations [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/github/awesome-copilot?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Claude Skills✨](https://github.com/anthropics/skills): 💡Official repository for Skills. Skills teach Claude how to complete specific tasks in a repeatable way. [Sep 2025] [✍️](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills) ![**github stars**](https://img.shields.io/github/stars/anthropics/skills?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [pg-aiguide✨](https://github.com/timescale/pg-aiguide): MCP server and Claude plugin for Postgres skills and documentation. Helps AI coding tools generate better PostgreSQL code. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/timescale/pg-aiguide?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [skills✨](https://github.com/openai/skills): Skills Catalog for Codex [Nov 2025] ![**github stars**](https://img.shields.io/github/stars/openai/skills?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ui-ux-pro-max-skill✨](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill): An AI SKILL that provide design intelligence for building professional UI/UX multiple platforms [Nov 2025] ![**github stars**](https://img.shields.io/github/stars/nextlevelbuilder/ui-ux-pro-max-skill?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### Domain-Specific Agents

1. [5 Top AI Agents for Earth Snapshots](https://x.com/MaryamMiradi/status/1866527000963211754) VLMs and LLMs for Geospatial Intelligent Analysis: [GeoChat📑](https://arxiv.org/abs/2311.15826) | [GEOBench-VLM📑](https://arxiv.org/abs/2411.19325) | [RS5M✨](https://github.com/om-ai-lab/RS5M) | [VHM✨](https://github.com/opendatalab/VHM) | [EarthGPT](https://ieeexplore.ieee.org/document/10547418)
1. [An LLM Agent for Automatic Geospatial Data Analysis📑](https://arxiv.org/abs/2410.18792) [24 Oct 2024]
1. [AgentSociety✨](https://github.com/tsinghua-fib-lab/agentsociety): Building agents in urban simulation environments. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/tsinghua-fib-lab/agentsociety?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [ChemAgent: Self-updating Library in Large Language Models Improves Chemical Reasoning📑](https://arxiv.org/abs/2501.06590): ChemAgent leverages an innovative self-improving memory system to significantly enhance performance in complex scientific tasks, with a particular focus on Chemistry. [11 Jan 2025]
1. [DeepRare📑](https://arxiv.org/abs/2506.20430): An Agentic System for Rare Disease Diagnosis with Traceable Reasoning [25 Jun 2025]
1. [dexter✨](https://github.com/virattt/dexter): An autonomous agent for deep financial research [Oct 2025] ![**github stars**](https://img.shields.io/github/stars/virattt/dexter?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Director✨](https://github.com/video-db/Director): Think of Director as ChatGPT for videos. AI video agents framework for video interactions and workflows. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/video-db/Director?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DrugAgent: Automating AI-aided Drug Discovery📑](https://arxiv.org/abs/2411.15692) [24 Nov 2024]
1. [FinRobot: AI Agent for Equity Research and Valuation📑](https://arxiv.org/abs/2411.08804) [13 Nov 2024]
1. [landing.ai: Vision Agent✨](https://github.com/landing-ai/vision-agent): A agent frameworks to generate code to solve your vision task. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/landing-ai/vision-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Organ-Agents: Virtual Human Physiology Simulator via LLMs](https://arxiv.org/abs/2508.14357): Multi-agent system simulating nine human organs using fine-tuned Qwen3-8B, forecasting patient physiology up to 12 hours ahead, validated by 15 ICU specialists. [20 Aug 2025]
1. [MLE-agent✨](https://github.com/MLSysOps/MLE-agent): LLM agent for machine learning engineers and researchers [Apr 2024] ![**github stars**](https://img.shields.io/github/stars/MLSysOps/MLE-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [QuantAgent✨](https://github.com/Y-Research-SBU/QuantAgent): Quantitative trading agent. Multi-Agent LLMs for High-Frequency Trading. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/Y-Research-SBU/QuantAgent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [UXAgent📑](https://arxiv.org/abs/2502.12561): An LLM Agent-Based Usability Testing Framework for Web Design [18 Feb 2025]

#### Deep Research

1. [Accelerating scientific breakthroughs with an AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/): Google introduces AI co-scientist, a multi-agent AI system built with Gemini 2.0 as a virtual scientific collaborator [19 Feb 2025]
1. [Agent Laboratory✨](https://github.com/SamuelSchmidgall/AgentLaboratory): E2E autonomous research workflow. Using LLM Agents as Research Assistants. [8 Jan 2025] ![**github stars**](https://img.shields.io/github/stars/SamuelSchmidgall/AgentLaboratory?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [agenticSeek✨](https://github.com/Fosowl/agenticSeek): Fully Local Manus AI. No APIs, No $200 monthly bills. Enjoy an autonomous agent that thinks, browses the web, and code for the sole cost of electricity. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/Fosowl/agenticSeek?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [AlphaEvolve](https://deepmind.google/discover/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/): DeepMind’s AI agent that autonomously evolves algorithms using Gemini models—applied in chip design, data centers, robotics, math & CS, and AI training. [14 May 2025]
1. [Azure Container Apps Dynamic Sessions✍️](https://aka.ms/AAtnnj8): Secure environment for running AI-generated code in Azure.
1. [CodeScientist✨](https://github.com/allenai/codescientist): An automated scientific discovery system for code-based experiments. AllenAI. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/allenai/codescientist?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Company Researcher✨](https://github.com/exa-labs/company-researcher): a free and open-source tool that helps you instantly understand any company inside out. [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/exa-labs/company-researcher?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Deep Research Agent📑](https://arxiv.org/abs/2506.18096):💡Survey. A Systematic Examination And Roadmap [22 Jun 2025]
1. [DeepScholar](https://deep-scholar.vercel.app): an openly accessible deep research system from Berkeley and Stanford [Nov 2025]
1. [DeepSearcher✨](https://github.com/zilliztech/deep-searcher): DeepSearcher integrates LLMs and Vector Databases for precise search, evaluation, and reasoning on private data, providing accurate answers and detailed reports. [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/zilliztech/deep-searcher?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DeerFlow✨](https://github.com/bytedance/deer-flow):  Bytedance. Deep Exploration and Efficient Research Flow. a community-driven Deep Research framework that combines language models with tools like web search, crawling, and code execution.  ![**github stars**](https://img.shields.io/github/stars/bytedance/deer-flow?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [May 2025]
1. [Enterprise Deep Research (EDR)✨](https://github.com/SalesforceAIResearch/enterprise-deep-research): Salesforce Enterprise Deep Research [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/SalesforceAIResearch/enterprise-deep-research?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Felo.ai Deep Research✍️](https://felo.ai/blog/free-deepseek-r1-ai-search/) [8 Feb 2025]
1. [gpt-code-ui✨](https://github.com/ricklamers/gpt-code-ui) An open source implementation of OpenAI's ChatGPT Code interpreter. [May 2023]
 ![**github stars**](https://img.shields.io/github/stars/ricklamers/gpt-code-ui?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Kimi-Researcher](https://moonshotai.github.io/Kimi-Researcher/): Kimi Researcher is an AI-powered tool that assists with document analysis, literature review, and knowledge extraction. Moonshot AI (Chinese name: 月之暗面, meaning "The Dark Side of the Moon") is a Beijing-based company founded in March 2023. [20 Jun 2025]
1. [LangChain Open Deep Research✨](https://github.com/langchain-ai/open_deep_research): (formerly mAIstro) a web research assistant for generating comprehensive reports on any topic. [13 Feb 2025] ![**github stars**](https://img.shields.io/github/stars/langchain-ai/open_deep_research?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Manus sandbox runtime code leaked](https://x.com/jianxliao/status/1898861051183349870): Claude Sonnet with 29 tools, without multi-agent, using `browser_use`. [✨](https://gist.github.com/jlia0/db0a9695b3ca7609c9b1a08dcbf872c9) [✍️](https://manus.im/): Manus official site [10 Mar 2025]
1. [MiniMax-M2 Deep Research Agent](https://github.com/dair-ai/m2-deep-research): Minimax M2 with interleaved thinking, Exa neural search. [Nov 2025] ![**github stars**](https://img.shields.io/github/stars/dair-ai/m2-deep-research?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MLAB ResearchAgent✨](https://github.com/snap-stanford/MLAgentBench): Evaluating Language Agents on Machine Learning Experimentation [Aug 2023] ![**github stars**](https://img.shields.io/github/stars/snap-stanford/MLAgentBench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Ollama Deep Researcher✨](https://github.com/langchain-ai/ollama-deep-researcher): a fully local web research assistant that uses any LLM hosted by Ollama [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/langchain-ai/ollama-deep-researcher?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OmniScientist📑](https://arxiv.org/abs/2511.16931): a dynamic contextual graph with the Omni Scientific Protocol (OSP) for transparent multi-agent collaboration and ScienceArena for continuous human-centered evaluation. [21 Nov 2025]
1. [Open Deep Research✨](https://github.com/btahir/open-deep-research): Open source alternative to Gemini Deep Research. [Dec 2024] ![**github stars**](https://img.shields.io/github/stars/btahir/open-deep-research?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Open Interpreter✨](https://github.com/KillianLucas/open-interpreter):💡Let language models run code on your computer. [Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/KillianLucas/open-interpreter?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenAI Code Interpreter✍️](https://openai.com/blog/chatgpt-plugins) Integration with Sandboxed python execution environment. a working Python interpreter in a sandboxed, firewalled execution environment, along with some ephemeral disk space. [23 Mar 2023]
1. [OpenAI deep research✍️](https://openai.com/index/introducing-deep-research/)  [2 Feb 2025]
1. [OpenDeepSearch✨](https://github.com/sentient-agi/OpenDeepSearch): deep web search and retrieval, optimized for use with Hugging Face's SmolAgents ecosystem [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/sentient-agi/OpenDeepSearch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OpenEvolve✨](https://github.com/codelion/openevolve): An open-source implementation of the AlphaEvolve system described in the Google DeepMind paper "AlphaEvolve: A coding agent for scientific and algorithmic discovery" [May 2025] ![**github stars**](https://img.shields.io/github/stars/codelion/openevolve?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 
1. [OpenManus✨](https://github.com/mannaandpoem/OpenManus): A Free Open-Source Alternative to Manus AI Agent [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/mannaandpoem/OpenManus?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [OSS Code Interpreter✨](https://github.com/shroominic/codeinterpreter-api) A LangChain implementation of the ChatGPT Code Interpreter. [Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/shroominic/codeinterpreter-api?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Paper2Agent✨](https://github.com/jmiao24/Paper2Agent): a multi-agent AI system that converts research papers into interactive agents with minimal human input [Sep 2025] ![**github stars**](https://img.shields.io/github/stars/jmiao24/Paper2Agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning📑](https://arxiv.org/abs/2504.17192): a multi-agent LLM framework that transforms machine learning papers into functional code repositories. [24 Apr 2025] [✨](https://github.com/going-doer/Paper2Code) ![**github stars**](https://img.shields.io/github/stars/going-doer/Paper2Code?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research) [14 Feb 2025]
1. [SakanaAI AI-Scientist✨](https://github.com/SakanaAI/AI-Scientist): AI agents autonomously generated novel research ideas, experiments, and full papers, scoring up to weak accept (≈6) under NeurIPS standards. [Aug 2024]
 ![**github stars**](https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [SlashGPT✨](https://github.com/snakajima/SlashGPT) The tool integrated with "jupyter" agent [Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/snakajima/SlashGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [smolagents: Open Deep Research✨](https://github.com/huggingface/smolagents) > `examples/open_deep_research`.🤗HuggingFace [Feb 2025] ![**github stars**](https://img.shields.io/github/stars/huggingface/smolagents?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Stanford Agentic Reviewer](https://paperreview.ai/): AI feedback on your research paper [Nov 2025]
1. [STORM✨](https://github.com/stanford-oval/storm): Simulating Expert Q&A, iterative research, structured outline creation, and grounding in trusted sources to generate Wikipedia-like reports. [Apr 2024] ![**github stars**](https://img.shields.io/github/stars/stanford-oval/storm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search📑](https://arxiv.org/abs/2504.08066): AgentManager handles Agentic Tree Search [10 Apr 2025] [✨](https://github.com/SakanaAI/AI-Scientist-v2) ![**github stars**](https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Tongyi DeepResearch✨](https://github.com/Alibaba-NLP/DeepResearch): Alibaba. [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/Alibaba-NLP/DeepResearch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Universal Deep Research (UDR)✨](https://github.com/NVlabs/UniversalDeepResearch): NVDIA. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/NVlabs/UniversalDeepResearch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [WebThinker✨](https://github.com/RUC-NLPIR/WebThinker): WebThinker allows the reasoning model itself to perform actions during thinking, achieving end-to-end task execution in a single generation. [Mar 2025] ![**github stars**](https://img.shields.io/github/stars/RUC-NLPIR/WebThinker?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **Top Agent Frameworks**

- [AG2✨](https://github.com/ag2ai/ag2): Multi-agent conversational framework (formerly AutoGen)
 ![**github stars**](https://img.shields.io/github/stars/ag2ai/ag2?style=flat-square&label=%20&cacheSeconds=36000)
- [Agno✨](https://github.com/agno-agi/agno): Agent orchestration framework
 ![**github stars**](https://img.shields.io/github/stars/agno-agi/agno?style=flat-square&label=%20&cacheSeconds=36000)
- [AWS Bedrock Agents✨](https://github.com/awslabs/amazon-bedrock-agent-samples): AWS-native agent framework
 ![**github stars**](https://img.shields.io/github/stars/awslabs/amazon-bedrock-agent-samples?style=flat-square&label=%20&cacheSeconds=36000)
- [CrewAI✨](https://github.com/crewAIInc/crewAI): Role-based multi-agent framework
 ![**github stars**](https://img.shields.io/github/stars/crewAIInc/crewAI?style=flat-square&label=%20&cacheSeconds=36000)
- [Google ADK✨](https://github.com/google/adk-python): Google's Agent Development Kit
 ![**github stars**](https://img.shields.io/github/stars/google/adk-python?style=flat-square&label=%20&cacheSeconds=36000)
- [LangChain✨](https://github.com/langchain-ai/langchain): Comprehensive LLM application framework
 ![**github stars**](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square&label=%20&cacheSeconds=36000)
- [LangGraph✨](https://github.com/langchain-ai/langgraph): Stateful multi-agent workflows with cycles
 ![**github stars**](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square&label=%20&cacheSeconds=36000)
- [LlamaIndex✨](https://github.com/run-llama/llama_index): Data framework for LLM applications
 ![**github stars**](https://img.shields.io/github/stars/run-llama/llama_index?style=flat-square&label=%20&cacheSeconds=36000)
- [Mastra✨](https://github.com/mastra-ai/mastra): AI agent orchestration platform
 ![**github stars**](https://img.shields.io/github/stars/mastra-ai/mastra?style=flat-square&label=%20&cacheSeconds=36000)
- [Microsoft Agent Framework✨](https://github.com/microsoft/agent-framework): from simple chat agents to complex multi-agent workflows with graph-based orchestration. ![**github stars**](https://img.shields.io/github/stars/microsoft/agent-framework?style=flat-square&label=%20&cacheSeconds=36000)
- [Microsoft Semantic Kernel✨](https://github.com/microsoft/semantic-kernel) [Feb 2023]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/semantic-kernel?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [OpenAI Agent SDK✨](https://github.com/openai/openai-agents-python): Official OpenAI agent framework
 ![**github stars**](https://img.shields.io/github/stars/openai/openai-agents-python?style=flat-square&label=%20&cacheSeconds=36000)
- [Pydantic AI✨](https://github.com/pydantic/pydantic-ai): Type-safe agent framework
 ![**github stars**](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=flat-square&label=%20&cacheSeconds=36000)
- [Strands Agents SDK✨](https://github.com/strands-agents/sdk-python): Agent development SDK
 ![**github stars**](https://img.shields.io/github/stars/strands-agents/sdk-python?style=flat-square&label=%20&cacheSeconds=36000)
- [Vercel AI SDK✨](https://github.com/vercel/ai): AI framework for TypeScript/JavaScript
 ![**github stars**](https://img.shields.io/github/stars/vercel/ai?style=flat-square&label=%20&cacheSeconds=36000)

## **Orchestration Framework**

- [Prompting Framework (PF)📑](https://arxiv.org/abs/2311.12785): Prompting Frameworks for Large Language Models: A Survey [✨](https://github.com/lxx0628/Prompting-Framework-Survey)
 ![**github stars**](https://img.shields.io/github/stars/lxx0628/Prompting-Framework-Survey?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [What Are Tools Anyway?📑](https://arxiv.org/abs/2403.15452): Analysis of tool usage in LLMs. Key findings: 1) For 5-10 tools, LMs can directly select from context; for hundreds of tools, retrieval is necessary. 2) Tools enable creation and reuse but are less useful for translation, summarization, and sentiment analysis. 3) Includes evaluation metrics [18 Mar 2024]  
- **Micro-Orchestration**: Detailed management of LLM interactions, focusing on data flow within tasks
  - [LangChain](https://www.langchain.com)
  - [LlamaIndex](https://www.llamaindex.ai)
  - [Haystack](https://haystack.deepset.ai)
  - [AdalFlow](https://adalflow.sylph.ai)
  - [Semantic Kernel](https://aka.ms/sk/repo)
- **Macro-Orchestration**: High-level workflow management and state handling
  - [LangGraph](https://langchain-ai.github.io/langgraph)
  - [Burr](https://burr.dagworks.io)
- **Agentic Design**: Multi-agent systems and collaboration patterns
  - [Autogen](https://microsoft.github.io/autogen)
  - [CrewAI](https://docs.crewai.com)
- **Optimizer**: Algorithmic prompt and output optimization
  - [DSPy✨](https://github.com/stanfordnlp/dspy) [Jan 2023]
 ![**github stars**](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - [AdalFlow✨](https://github.com/SylphAI-Inc/AdalFlow):💡The Library to Build and Auto-optimize LLM Applications [Apr 2024] ![**github stars**](https://img.shields.io/github/stars/SylphAI-Inc/AdalFlow?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - [TextGrad✨](https://github.com/zou-group/textgrad): Automatic "differentiation" via text. Backpropagation through text feedback provided by LLMs [Jun 2024] ![**github stars**](https://img.shields.io/github/stars/zou-group/textgrad?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **LangChain**

- LangChain is a framework for developing applications powered by language models. (1) Be data-aware: connect a language model to other sources of data.
  (2) Be agentic: Allow a language model to interact with its environment. doc:[✍️](https://docs.langchain.com/docs) / blog:[✍️](https://blog.langchain.dev) / [✨](https://github.com/langchain-ai/langchain)
 ![**github stars**](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Reflections on Three Years of Building LangChain](https://blog.langchain.com/three-years-langchain/): Langchain 1.0, released  [25 Oct 2025]
- It highlights two main value props of the framework:
  - Components: modular abstractions and implementations for working with language models, with easy-to-use features.
  - Use-Case Specific Chains: chains of components that assemble in different ways to achieve specific use cases, with customizable interfaces.🗣️: [✍️](https://docs.langchain.com/docs/)
  - LangChain 0.2: full separation of langchain and langchain-community. [✍️](https://blog.langchain.dev/langchain-v02-leap-to-stability) [May 2024]
  - Towards LangChain 0.1 [✍️](https://blog.langchain.dev/the-new-langchain-architecture-langchain-core-v0-1-langchain-community-and-a-path-to-langchain-v0-1/) [Dec 2023]  
      <img src="../files/langchain-eco-v3.png" width="400">
  <!-- <img src="../files/langchain-eco-stack.png" width="400"> -->
  <!-- <img src="../files/langchain-glance.png" width="400"> -->
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

#### **LangChain Feature Matrix & Cheetsheet**

- [Awesome LangChain✨](https://github.com/kyrolabs/awesome-langchain): Curated list of tools and projects using LangChain.
 ![**github stars**](https://img.shields.io/github/stars/kyrolabs/awesome-langchain?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Building intelligent agents with LangGraph: PhiloAgents simulation engine✨](https://github.com/neural-maze/philoagents-course) [Jan 2025] ![**github stars**](https://img.shields.io/github/stars/neural-maze/philoagents-course?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Cheetsheet✨](https://github.com/gkamradt/langchain-tutorials): LangChain CheatSheet
 ![**github stars**](https://img.shields.io/github/stars/gkamradt/langchain-tutorials?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- DeepLearning.AI short course: LangChain for LLM Application Development [✍️](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/) / LangChain: Chat with Your Data [✍️](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/)
- [Feature Matrix](https://python.langchain.com/docs/get_started/introduction): LangChain Features
- [Feature Matrix: Snapshot in 2023 July](../files/langchain-features-202307.png)  
- [LangChain AI Handbook](https://www.pinecone.io/learn/series/langchain/): published by Pinecone
- [LangChain Cheetsheet KD-nuggets](https://www.kdnuggets.com/wp-content/uploads/LangChain_Cheat_Sheet_KDnuggets.pdf): LangChain Cheetsheet KD-nuggets [🗄️](../files/LangChain_kdnuggets.pdf) [Aug 2023]
- [LangChain Streamlit agent examples✨](https://github.com/langchain-ai/streamlit-agent): Implementations of several LangChain agents as Streamlit apps. [Jun 2023] ![**github stars**](https://img.shields.io/github/stars/langchain-ai/streamlit-agent?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LangChain Tutorial](https://nanonets.com/blog/langchain/): A Complete LangChain Guide
- [LangChain tutorial: A guide to building LLM-powered applications](https://www.elastic.co/blog/langchain-tutorial) [27 Feb 2024]
- [RAG From Scratch✨](https://github.com/langchain-ai/rag-from-scratch)💡[Feb 2024]
 ![**github stars**](https://img.shields.io/github/stars/langchain-ai/rag-from-scratch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **LangChain features and related libraries**

- [LangChain Expression Language](https://python.langchain.com/docs/guides/expression_language/): A declarative way to easily compose chains together [Aug 2023]
- [LangChain Template✨](https://github.com/langchain-ai/langchain/tree/master/templates): LangChain Reference architectures and samples. e.g., `RAG Conversation Template` [Oct 2023]
- [LangChain/cache](https://python.langchain.com/docs/modules/model_io/models/llms/how_to/llm_caching): Reducing the number of API calls
- [LangChain/context-aware-splitting](https://python.langchain.com/docs/use_cases/question_answering/document-context-aware-QA): Splits a file into chunks while keeping metadata
- [LangGraph✨](https://github.com/langchain-ai/langgraph):💡Build and navigate language agents as graphs [✍️](https://langchain-ai.github.io/langgraph/) [Aug 2023] -> LangGraph is inspired by [Pregel](https://research.google/pubs/pub37252/) for Parallel Processing, [Apache Beam](https://beam.apache.org/) for Data flows, and [NetworkX](https://networkx.org/documentation/latest/) for Graph. | [Tutorial](https://langchain-ai.github.io/langgraph/tutorials). ![**github stars**](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LangSmith✍️](https://blog.langchain.dev/announcing-langsmith/) Platform for debugging, testing, evaluating. [Jul 2023]
- [OpenGPTs✨](https://github.com/langchain-ai/opengpts): An open source effort to create a similar experience to OpenAI's GPTs [Nov 2023]
 ![**github stars**](https://img.shields.io/github/stars/langchain-ai/opengpts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### **LangChain chain type: Chains & Summarizer**

- Chains [✨](https://github.com/RutamBhagat/LangChainHCCourse1/blob/main/course_1/chains.ipynb)
  - SimpleSequentialChain: A sequence of steps with single input and output. Output of one step is input for the next.
  - SequentialChain: Like SimpleSequentialChain but handles multiple inputs and outputs at each step.
  - MultiPromptChain: Routes inputs to specialized sub-chains based on content. Ideal for different prompts for different tasks.
- Summarizer
  - stuff: Sends everything at once in LLM. If it's too long, an error will occur.
  - map_reduce: Summarizes by dividing and then summarizing the entire summary.
  - refine: (Summary + Next document) => Summary
  - map_rerank: Ranks by score and summarizes to important points.

#### LangChain Agent

-  If you're using a text LLM, first try `zero-shot-react-description`.
-  If you're using a Chat Model, try `chat-zero-shot-react-description`.
-  If you're using a Chat Model and want to use memory, try `conversational-react-description`.
-  `self-ask-with-search`: [Measuring and Narrowing the Compositionality Gap in Language Models📑](https://arxiv.org/abs/2210.03350) [7 Oct 2022]
-  `react-docstore`: [ReAct: Synergizing Reasoning and Acting in Language Models📑](https://arxiv.org/abs/2210.03629) [6 Oct 2022]
-  Agent Type
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
- [ReAct📑](https://arxiv.org/abs/2210.03629) vs [MRKL📑](https://arxiv.org/abs/2205.00445) (miracle)
  - ReAct is inspired by the synergies between "acting" and "reasoning" which allow humans to learn new tasks and make decisions or reasoning.
  - MRKL stands for Modular Reasoning, Knowledge and Language and is a neuro-symbolic architecture that combines large language models, external knowledge sources, and discrete reasoning
  > 🗣️: [✨](https://github.com/langchain-ai/langchain/issues/2284#issuecomment-1526879904) [28 Apr 2023] <br/>
  `zero-shot-react-description`: Uses ReAct to select tools based on their descriptions. Any number of tools can be used, each requiring a description. <br/>
  `react-docstore`: Uses ReAct to manage a docstore with two required tools: _Search_ and _Lookup_. These tools must be named exactly as specified. It follows the original ReAct paper's example from Wikipedia.  
  MRKL in LangChain uses `zero-shot-react-description`, implementing ReAct. The original ReAct framework is used in the `react-docstore` agent. MRKL was published on May 1, 2022, earlier than ReAct on October 6, 2022.

#### LangChain Memory

-  `ConversationBufferMemory`: Stores the entire conversation history.
-  `ConversationBufferWindowMemory`: Stores recent messages from the conversation history.
-  `Entity Store (previously Entity Memory)`: Stores and retrieves entity-related information.
-  `Conversation Knowledge Graph Memory`: Stores entities and relationships between entities.
-  `ConversationSummaryMemory`: Stores summarized information about the conversation.
-  `ConversationSummaryBufferMemory`: Stores summarized information about the conversation with a token limit.
-  `ConversationTokenBufferMemory`: Stores tokens from the conversation.
-  `VectorStore-Backed Memory`: Leverages vector space models for storing and retrieving information.

#### **Criticism to LangChain**

- [How to Build Ridiculously Complex LLM Pipelines with LangGraph!](https://newsletter.theaiedge.io/p/how-to-build-ridiculously-complex) [17 Sep 2024 ]
  > LangChain does too much, and as a consequence, it does many things badly. Scaling beyond the basic use cases with LangChain is a challenge that is often better served with building things from scratch by using the underlying APIs.
- LangChain Is Pointless: [✍️](https://news.ycombinator.com/item?id=36645575) [Jul 2023]
  > LangChain has been criticized for making simple things relatively complex, which creates unnecessary complexity and tribalism that hurts the up-and-coming AI ecosystem as a whole. The documentation is also criticized for being bad and unhelpful.
- [The Hidden Cost of LangChain: Why My Simple RAG System Cost 2.7x More Than Expected ](https://dev.to/himanjan/the-hidden-cost-of-langchain-why-my-simple-rag-system-cost-27x-more-than-expected-4hk9) [23 Jul 2025]
- The Problem With LangChain: [✍️](https://minimaxir.com/2023/07/langchain-problem/) / [✨](https://github.com/minimaxir/langchain-problems) [14 Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/minimaxir/langchain-problems?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- What’s your biggest complaint about langchain?: [✍️](https://www.reddit.com/r/LangChain/comments/139bu99/whats_your-biggest_complaint_about_langchain/) [May 2023]

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
  - LangChain has many agents, tools, plugins etc. out of the box. More over, LangChain has 10x more popularity, so has about 10x more developer activity to improve it. On other hand, **Semantic Kernel architecture and quality is better**, that's quite promising for Semantic Kernel. [✨](https://github.com/microsoft/semantic-kernel/discussions/1326) [11 May 2023]
- What's the difference between Azure Machine Learing PromptFlow and Semantic Kernel?  
  -  Low/No Code vs C#, Python, Java  
  -  Focused on Prompt orchestrating vs Integrate LLM into their existing app.
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
  > Fun fact this core idea was the initial inspiration for GPT Index (the former name of LlamaIndex) 11/8/2022 - almost a year ago!. [🗣️](https://twitter.com/jerryjliu0/status/1711817419592008037) / [Walking Down the Memory Maze: Beyond Context Limit through Interactive Reading📑](https://arxiv.org/abs/2310.05029)  
  > -   Build a data structure (memory tree)  
  > -   Transverse it via LLM prompting  
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

  -  The query engine wraps a `retriever` and a `response synthesizer` into a pipeline, that will use the query string to fetch nodes (sentences or paragraphs) from the index and then send them to the LLM (Language and Logic Model) to generate a response
  -  The chat engine is a quick and simple way to chat with the data in your index. It uses a `context manager` to keep track of the conversation history and generate relevant queries for the retriever. Conceptually, it is a `stateful` analogy of a Query Engine.

- Storage Context vs Settings (p.k.a. Service Context)
  - Both the `Storage Context` and `Service Context` are data classes.
  -  Introduced in v0.10.0, ServiceContext is replaced to Settings object.
  -  Storage Context is responsible for the storage and retrieval of data in Llama Index, while the Service Context helps in incorporating external context to enhance the search experience.
  -  The Service Context is not directly involved in the storage or retrieval of data, but it helps in providing a more context-aware and accurate search experience.

#### LlamaIndex Tutorial
- 4 RAG techniques implemented in `llama_index` / [🗣️](https://x.com/ecardenas300/status/1704188276565795079) [20 Sep 2023] / [✨](https://github.com/weaviate/recipes)
 ![**github stars**](https://img.shields.io/github/stars/weaviate/recipes?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  -  SQL Router Query Engine: Query router that can reference your vector database or SQL database
  - Sub Question Query Engine: Break down the complex question into sub-questions
  - Recursive Retriever + Query Engine: Reference node relationships, rather than only finding a node (chunk) that is most relevant.
  - Self Correcting Query Engines: Use an LLM to evaluate its own output.  
- [A Cheat Sheet and Some Recipes For Building Advanced RAG✍️](https://blog.llamaindex.ai/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b) RAG cheat sheet shared above was inspired by [RAG survey paper📑](https://arxiv.org/abs/2312.10997). [🗄️](../files/advanced-rag-diagram-llama-index.png) [Jan 2024]
- [Building and Productionizing RAG](https://docs.google.com/presentation/d/1rFQ0hPyYja3HKRdGEgjeDxr0MSE8wiQ2iu4mDtwR6fc/edit#slide=id.p): [🗄️](../files/archive/LlamaIndexTalk_PyDataGlobal.pdf): Optimizing RAG Systems 1. Table Stakes 2. Advanced Retrieval: Small-to-Big 3. Agents 4. Fine-Tuning 5. Evaluation [Nov 2023]
<!-- - [CallbackManager (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-003-callback-manager/) [27 May 2023] / [Customize TokenTextSplitter (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-002-text-splitter/) [27 May 2023] / --> 
- [Chat engine ReAct mode](https://gpt-index.readthedocs.io/en/stable/examples/chat_engine/chat_engine_react.html), [FLARE Query engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/flare_query_engine.html)
- [Fine-Tuning a Linear Adapter for Any Embedding Model](https://medium.com/llamaindex-blog/fine-tuning-a-linear-adapter-for-any-embedding-model-8dd0a142d383): Fine-tuning the embeddings model requires you to reindex your documents. With this approach, you do not need to re-embed your documents. Simply transform the query instead. [7 Sep 2023]
- [LlamaIndex Overview (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-001-overview-v0-7-9/) [17 Jul 2023]
- [LlamaIndex Tutorial](https://nanonets.com/blog/llamaindex/): A Complete LlamaIndex Guide [18 Oct 2023]
- Multimodal RAG Pipeline [✍️](https://blog.llamaindex.ai/multi-modal-rag-621de7525fea) [Nov 2023]



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

<!-- <img src="../files/mind-and-body-of-semantic-kernel.png" alt="sk" width="130"/> -->
<!-- <img src="../files/sk-flow.png" alt="sk" width="500"/> -->

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

  <img src="../files/sk-evolution_of_planners.jpg" alt="sk-plan" width="300"/>

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
  - Function:  Individual units of work that perform specific tasks. Execute actions based on user requests. [✍️](https://devblogs.microsoft.com/semantic-kernel/transforming-semantic-kernel-functions/) [12 Nov 2024]
  - Plugin: Collections of functions. Orchestrate multiple functions for complex tasks.
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

  <img src="../files/kernel-flow.png" alt="sk" width="500"/>

  | Term      | Short Description                                                                                                                                                                                                                                                                                     |
  | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | ASK       | A user's goal is sent to SK as an ASK                                                                                                                                                                                                                                                                 |
  | Kernel    | [The kernel](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/kernel) orchestrates a user's ASK                                                                                                                                                                                          |
  | Planner   | [The planner](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/planner) breaks it down into steps based upon resources that are available [deprecated] -> replaced by function calling                                                                                                                                  |
  | Resources | Planning involves leveraging available [skills,](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/skills) [memories,](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/memories) and [connectors](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/connectors) |
  | Steps     | A plan is a series of steps for the kernel to execute                                                                                                                                                                                                                                                 |
  | Pipeline  | Executing the steps results in fulfilling the user's ASK                                                                                                                                                                                                                                              |
- [Architecting AI Apps with Semantic Kernel✍️](https://devblogs.microsoft.com/semantic-kernel/architecting-ai-apps-with-semantic-kernel/) How you could recreate Microsoft Word Copilot [6 Mar 2024]  
  <img src="../files/semantic-kernel-with-word-copilot.png" height="500">  

### **DSPy**

- [DSPy📑](https://arxiv.org/abs/2310.03714): Compiling Declarative Language Model Calls into Self-Improving Pipelines [5 Oct 2023] / [✨](https://github.com/stanfordnlp/dspy)
- [Prompt Like a Data Scientist: Auto Prompt Optimization and Testing with DSPy✍️](https://towardsdatascience.com/prompt-like-a-data-scientist-auto-prompt-optimization-and-testing-with-dspy-ff699f030cb7) [6 May 2024]
- Automatically iterate until the best result is achieved: 1. Collect Data -> 2. Write DSPy Program -> 3. Define validtion logic -> 4. Compile DSPy program
- DSPy (Declarative Self-improving Language Programs, pronounced “dee-es-pie”) / doc:[✍️](https://dspy-docs.vercel.app) / [✨](https://github.com/stanfordnlp/dspy) ![**github stars**](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- DSPy Documentation & Cheetsheet [✍️](https://dspy-docs.vercel.app)
- DSPy Explained! [📺](https://www.youtube.com/watch?v=41EfOY0Ldkc) [30 Jan 2024]
- DSPy RAG example in weviate `recipes > integrations`: [✨](https://github.com/weaviate/recipes) ![**github stars**](https://img.shields.io/github/stars/weaviate/recipes?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Instead of a hard-coded prompt template, "Modular approach: compositions of modules -> compile". 
  - Building blocks such as ChainOfThought or Retrieve and compiling the program, optimizing the prompts based on specific metrics. Unifying strategies for both prompting and fine-tuning in one tool, Pythonic operations, prioritizing and tracing program execution. These features distinguish it from other LMP frameworks such as LangChain, and LlamaIndex. [✍️](https://towardsai.net/p/machine-learning/inside-dspy-the-new-language-model-programming-framework-you-need-to-know-about) [Jan 2023]
  <img src="../files/dspy-workflow.jpg" width="400" alt="workflow">  

#### **DSPy Glossary**

- Glossary reference to the [✍️](https:/towardsdatascience.com/intro-to-dspy-goodbye-prompting-hello-programming-4ca1c6ce3eb9).
  - Signatures: Hand-written prompts and fine-tuning are abstracted and replaced by signatures.
      > "question -> answer" <br/>
        "long-document -> summary"  <br/>
        "context, question -> answer"  <br/>
  - Modules: Prompting techniques, such as `Chain of Thought` or `ReAct`, are abstracted and replaced by modules.
      ```python
      # pass a signature to ChainOfThought module
      generate_answer = dspy.ChainOfThought("context, question -> answer")
      ```
  - Optimizers (formerly Teleprompters): Manual iterations of prompt engineering is automated with optimizers (teleprompters) and a DSPy Compiler.
      ```python
      # Self-generate complete demonstrations. Teacher-student paradigm, `BootstrapFewShotWithOptuna`, `BootstrapFewShotWithRandomSearch` etc. which work on the same principle.
      optimizer = BootstrapFewShot(metric=dspy.evaluate.answer_exact_match)
      ```
  - DSPy Compiler: Internally trace your program and then optimize it using an optimizer (teleprompter) to maximize a given metric (e.g., improve quality or cost) for your task.
ng-hello-programming-4ca1c6ce3eb9).
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

