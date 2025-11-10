## **RAG (Retrieval-Augmented Generation)**

### **RAG (Retrieval-Augmented Generation)**

- RAG (Retrieval-Augmented Generation) : Integrates the retrieval (searching) into LLM text generation. RAG helps the model to “look up” external information to improve its responses. [✍️](https://towardsdatascience.com/rag-vs-finetuning-which-is-the-best-tool-to-boost-your-llm-application-94654b1eaba7) [25 Aug 2023]

  <!-- <img src="../files/RAG.png" alt="sk" width="400"/> -->

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
  <img src="../files/oai-rag-success-story.jpg" width="500">
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
- From Simple to Advanced RAG (LlamaIndex) [✍️](https://twitter.com/jerryjliu0/status/1711419232314065288) / [🗄️](../files/archive/LlamaIndexTalk_PyDataGlobal.pdf) /💡[✍️](https://aiconference.com/speakers/jerry-liu-2023/) [10 Oct 2023] <br/>
  <img src="../files/advanced-rag.png" width="430">
- [What is Agentic RAG](https://weaviate.io/blog/what-is-agentic-rag): The article published by Weaviate. [5 Nov 2024]

#### Multi-modal RAG (Vision RAG)

- [Azure RAG with Vision Application Framework✨](https://github.com/Azure-Samples/rag-as-a-service-with-vision) [Mar 2024] ![**github stars**](https://img.shields.io/github/stars/Azure-Samples/rag-as-a-service-with-vision?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Enhancing Ultra High Resolution Remote Sensing Imagery Analysis with ImageRAG📑](https://alphaxiv.org/abs/2411.07688): Ultra High Resolution (UHR) remote sensing imagery, such as satellite imagery and medical imaging. [12 Nov 2024]
- [localGPT-Vision✨](https://github.com/PromtEngineer/localGPT-Vision): an end-to-end vision-based Retrieval-Augmented Generation (RAG) system. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/PromtEngineer/localGPT-Vision?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Multi-Modal RAG System✍️](https://machinelearningmastery.com/implementing-multi-modal-rag-systems/): Building a knowledge base with both image and audio data. [12 Feb 2025]
- [Path-RAG: Knowledge-Guided Key Region Retrieval for Open-ended Pathology Visual Question Answering📑](https://alphaxiv.org/abs/2411.17073): Using HistoCartography to improve pathology image analysis and boost PathVQA-Open performance. [26 Nov 2024]
- [UniversalRAG✨](https://github.com/wgcyeo/UniversalRAG): [🔗](rag.md/#research) [29 Apr 2025]  ![**github stars**](https://img.shields.io/github/stars/wgcyeo/UniversalRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
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
- [Graphiti✨](https://github.com/getzep/graphiti): [🔗](app.md/#llm-memory)
- [HippoRAG✨](https://github.com/OSU-NLP-Group/HippoRAG):💡RAG + Knowledge Graphs + Personalized PageRank. [23 May 2024] ![**github stars**](https://img.shields.io/github/stars/OSU-NLP-Group/HippoRAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [How to Build a Graph RAG App✍️](https://towardsdatascience.com/how-to-build-a-graph-rag-app-b323fc33ba06): Using knowledge graphs and AI to retrieve, filter, and summarize medical journal articles [30 Dec 2024]
- [HybridRAG📑](https://alphaxiv.org/abs/2408.04948): Integrating VectorRAG and GraphRAG with financial earnings call transcripts in Q&A format. [9 Aug 2024]
- [Neo4j GraphRAG Package for Python✨](https://github.com/neo4j/neo4j-graphrag-python) [Feb 2024] ![**github stars**](https://img.shields.io/github/stars/neo4j/neo4j-graphrag-python?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **The Problem with RAG**

- [Seven Failure Points When Engineering a Retrieval Augmented Generation System📑](https://alphaxiv.org/abs/2401.05856): 1. Missing Content, 2. Missed the Top Ranked Documents, 3. Not in Context, 4. Not Extracted, 5. Wrong Format, 6. Incorrect Specificity, 7. Lack of Thorough Testing [11 Jan 2024]
- Solving the core challenges of Retrieval-Augmented Generation [✍️](https://towardsdatascience.com/12-rag-pain-points-and-proposed-solutions-43709939a28c) [Feb 2024] <br/>
  <img src="../files/rag-12-pain-points-solutions.jpg" width="500">
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
  - Azure Reference Architectures: [🔗](aoai.md/#azure-reference-architectures)
  - [GPT-RAG✨](https://github.com/Azure/GPT-RAG): Enterprise RAG Solution Accelerator [Jun 2023]
![**github stars**](https://img.shields.io/github/stars/Azure/GPT-RAG?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [bRAG✨](https://github.com/bRAGAI/bRAG-langchain/): Everything you need to know to build your own RAG application [Nov 2024] ![**github stars**](https://img.shields.io/github/stars/bRAGAI/bRAG-langchain?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Evaluating LLMs and RAG Systems✍️](https://dzone.com/articles/evaluating-llms-and-rag-systems): Best Practices for Evaluating LLMs and RAG Systems [27 Jan 2025]
- [From Zero to Hero: Proven Methods to Optimize RAG for Production✍️](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/from-zero-to-hero-proven-methods-to-optimize-rag-for-production/4450040): ColBERT (Token-level embedding), [CoPali](https://huggingface.co/vidore/colpali-v1.2)(Extends ColBERT’s multi-vector retrieval and late interaction from text to vision), RAPTOR, HyDE, Re-Ranking and Fusion [Sep 2025]
- [Galileo eBook](https://www.rungalileo.io/mastering-rag): 200 pages content. Mastering RAG. [🗄️](../files/archive/Mastering%20RAG-compressed.pdf) [Sep 2024]
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

1. Applications, Frameworks, and User Interface (UI/UX): [🔗](app.md/#applications-frameworks-and-user-interface-uiux)
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

1. Applications, Frameworks, and User Interface (UI/UX): [🔗](app.md/#applications-frameworks-and-user-interface-uiux)
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
- [Not All Vector Databases Are Made Equal✍️](https://towardsdatascience.com/milvus-pinecone-vespa-weaviate-vald-gsi-what-unites-these-buzz-words-and-what-makes-each-9c65a3bd0696): Printed version for "Medium" limits. [🗄️](../files/vector-dbs.pdf) [2 Oct 2021]
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
- OpenAI Embedding models: `text-embedding-3` [🔗](chab.md/#openai-products) > `New embedding models`
- [text-embedding-ada-002✍️](https://openai.com/blog/new-and-improved-embedding-model):
  Smaller embedding size. The new embeddings have only 1536 dimensions, one-eighth the size of davinci-001 embeddings,
  making the new embeddings more cost effective in working with vector databases. [15 Dec 2022]
- [Vector Search with OpenAI Embeddings: Lucene Is All You Need📑](https://alphaxiv.org/abs/2308.14963): For vector search applications, Lucene’s HNSW implementation is a resilient and extensible solution with performance comparable to specialized vector databases like FAISS. Our experiments used Lucene 9.5.0, which limits vectors to 1024 dimensions—insufficient for OpenAI’s 1536-dimensional embeddings. A fix to make vector dimensions configurable per codec has been merged to Lucene’s source [here✨](https://github.com/apache/lucene/pull/12436) but was not yet released as of August 2023. [29 Aug 2023]

