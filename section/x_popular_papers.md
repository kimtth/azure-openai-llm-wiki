# Popular Papers on RAG & AI Agents (Computer Science)

*Generated: 2026-07-01 10:55:39*
*Source: Semantic Scholar batch API refresh of existing paper IDs*
*Filtered for Computer Science papers only*

## RAG (Retrieval-Augmented Generation)

*Retrieved: 2026-07-01 10:55:39*

### 1. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**Authors:** Patrick Lewis, Ethan Perez, Aleksandara Piktus, et al.  
**Year:** 2020 | **Citations:** 15,276 | **Venue:** Neural Information Processing Systems  
**Year Month:** [May 2020]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/659bf9ce7175e1ec266ff54359e2bd76e0b7ff31](https://www.semanticscholar.org/paper/659bf9ce7175e1ec266ff54359e2bd76e0b7ff31)  
**arXiv:** [https://arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)  

**Abstract:** Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue, but have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) -- models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state-of-the-art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.

---

### 2. Retrieval-Augmented Generation for Large Language Models: A Survey

**Authors:** Yunfan Gao, Yun Xiong, Xinyu Gao, et al.  
**Year:** 2023 | **Citations:** 3,557 | **Venue:** arXiv.org  
**Year Month:** [Dec 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/46f9f7b8f88f72e12cbdb21e3311f995eb6e65c5](https://www.semanticscholar.org/paper/46f9f7b8f88f72e12cbdb21e3311f995eb6e65c5)  
**arXiv:** [https://arxiv.org/abs/2312.10997](https://arxiv.org/abs/2312.10997)  

**Abstract:** Large Language Models (LLMs) showcase impressive capabilities but encounter challenges like hallucination, outdated knowledge, and non-transparent, untraceable reasoning processes. Retrieval-Augmented Generation (RAG) has emerged as a promising solution by incorporating knowledge from external databases. This enhances the accuracy and credibility of the generation, particularly for knowledge-intensive tasks, and allows for continuous knowledge updates and integration of domain-specific information. RAG synergistically merges LLMs' intrinsic knowledge with the vast, dynamic repositories of external databases. This comprehensive review paper offers a detailed examination of the progression of RAG paradigms, encompassing the Naive RAG, the Advanced RAG, and the Modular RAG. It meticulously scrutinizes the tripartite foundation of RAG frameworks, which includes the retrieval, the generation and the augmentation techniques. The paper highlights the state-of-the-art technologies embedded in each of these critical components, providing a profound understanding of the advancements in RAG systems. Furthermore, this paper introduces up-to-date evaluation framework and benchmark. At the end, this article delineates the challenges currently faced and points out prospective avenues for research and development.

---

### 3. RAGAs: Automated Evaluation of Retrieval Augmented Generation

**Authors:** ES Shahul, J. James, Luis Espinosa Anke, et al.  
**Year:** 2023 | **Citations:** 754 | **Venue:** Conference of the European Chapter of the Association for Computational Linguistics  
**Year Month:** [Sep 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/f5e9e5bbe22f0263be1f1ce88c66978a2b927772](https://www.semanticscholar.org/paper/f5e9e5bbe22f0263be1f1ce88c66978a2b927772)  
**arXiv:** [https://arxiv.org/abs/2309.15217](https://arxiv.org/abs/2309.15217)  

**Abstract:** We introduce RAGAs (Retrieval Augmented Generation Assessment), a framework for reference-free evaluation of Retrieval Augmented Generation (RAG) pipelines. RAGAs is available at [https://github.com/explodinggradients/ragas]. RAG systems are composed of a retrieval and an LLM based generation module. They provide LLMs with knowledge from a reference textual database, enabling them to act as a natural language layer between a user and textual databases, thus reducing the risk of hallucinations. Evaluating RAG architectures is challenging due to several dimensions to consider: the ability of the retrieval system to identify relevant and focused context passages, the ability of the LLM to exploit such passages faithfully, and the quality of the generation itself. With RAGAs, we introduce a suite of metrics that can evaluate these different dimensions without relying on ground truth human annotations. We posit that such a framework can contribute crucially to faster evaluation cycles of RAG architectures, which is especially important given the fast adoption of LLMs.

---

### 4. Active Retrieval Augmented Generation

**Authors:** Zhengbao Jiang, Frank F. Xu, Luyu Gao, et al.  
**Year:** 2023 | **Citations:** 704 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [May 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/88884b8806262a4095036041e3567d450dba39f7](https://www.semanticscholar.org/paper/88884b8806262a4095036041e3567d450dba39f7)  
**arXiv:** [https://arxiv.org/abs/2305.06983](https://arxiv.org/abs/2305.06983)  

**Abstract:** Despite the remarkable ability of large language models (LMs) to comprehend and generate language, they have a tendency to hallucinate and create factually inaccurate output. Augmenting LMs by retrieving information from external knowledge resources is one promising solution. Most existing retrieval augmented LMs employ a retrieve-and-generate setup that only retrieves information once based on the input. This is limiting, however, in more general scenarios involving generation of long texts, where continually gathering information throughout generation is essential. In this work, we provide a generalized view of active retrieval augmented generation, methods that actively decide when and what to retrieve across the course of the generation. We propose Forward-Looking Active REtrieval augmented generation (FLARE), a generic method which iteratively uses a prediction of the upcoming sentence to anticipate future content, which is then utilized as a query to retrieve relevant documents to regenerate the sentence if it contains low-confidence tokens. We test FLARE along with baselines comprehensively over 4 long-form knowledge-intensive generation tasks/datasets. FLARE achieves superior or competitive performance on all tasks, demonstrating the effectiveness of our method. Code and datasets are available at https://github.com/jzbjyb/FLARE.

---

### 5. Retrieval-Augmented Generation for AI-Generated Content: A Survey

**Authors:** Penghao Zhao, Hailin Zhang, Qinhan Yu, et al.  
**Year:** 2024 | **Citations:** 614 | **Venue:** Data Science and Engineering  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ab15463babf98fffc6f683fe2026de0725b5e1a9](https://www.semanticscholar.org/paper/ab15463babf98fffc6f683fe2026de0725b5e1a9)  
**arXiv:** [https://arxiv.org/abs/2402.19473](https://arxiv.org/abs/2402.19473)  

**Abstract:** Advancements in model algorithms, the growth of foundational models, and access to high-quality datasets have propelled the evolution of Artificial Intelligence Generated Content (AIGC). Despite its notable successes, AIGC still faces hurdles such as updating knowledge, handling long-tail data, mitigating data leakage, and managing high training and inference costs. Retrieval-Augmented Generation (RAG) has recently emerged as a paradigm to address such challenges. In particular, RAG introduces the information retrieval process, which enhances the generation process by retrieving relevant objects from available data stores, leading to higher accuracy and better robustness. In this paper, we comprehensively review existing efforts that integrate RAG technique into AIGC scenarios. We first classify RAG foundations according to how the retriever augments the generator, distilling the fundamental abstractions of the augmentation methodologies for various retrievers and generators. This unified perspective encompasses all RAG scenarios, illuminating advancements and pivotal technologies that help with potential future progress. We also summarize additional enhancements methods for RAG, facilitating effective engineering and implementation of RAG systems. Then from another view, we survey on practical applications of RAG across different modalities and tasks, offering valuable references for researchers and practitioners. Furthermore, we introduce the benchmarks for RAG, discuss the limitations of current RAG systems, and suggest potential directions for future research. Github: https://github.com/PKU-DAIR/RAG-Survey.

---

### 6. Benchmarking Large Language Models in Retrieval-Augmented Generation

**Authors:** Jiawei Chen, Hongyu Lin, Xianpei Han, et al.  
**Year:** 2023 | **Citations:** 566 | **Venue:** AAAI Conference on Artificial Intelligence  
**Year Month:** [Sep 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/28e2ecb4183ebc0eec504b12dddc677f8aef8745](https://www.semanticscholar.org/paper/28e2ecb4183ebc0eec504b12dddc677f8aef8745)  
**arXiv:** [https://arxiv.org/abs/2309.01431](https://arxiv.org/abs/2309.01431)  

**Abstract:** Retrieval-Augmented Generation (RAG) is a promising approach for mitigating the hallucination of large language models (LLMs). However, existing research lacks rigorous evaluation of the impact of retrieval-augmented generation on different large language models, which make it challenging to identify the potential bottlenecks in the capabilities of RAG for different LLMs. In this paper, we systematically investigate the impact of Retrieval-Augmented Generation on large language models. We analyze the performance of different large language models in 4 fundamental abilities required for RAG, including noise robustness, negative rejection, information integration, and counterfactual robustness. To this end, we establish Retrieval-Augmented Generation Benchmark (RGB), a new corpus for RAG evaluation in both English and Chinese. RGB divides the instances within the benchmark into 4 separate testbeds based on the aforementioned fundamental abilities required to resolve the case. Then we evaluate 6 representative LLMs on RGB to diagnose the challenges of current LLMs when applying RAG. Evaluation reveals that while LLMs exhibit a certain degree of noise robustness, they still struggle significantly in terms of negative rejection, information integration, and dealing with false information. The aforementioned assessment outcomes indicate that there is still a considerable journey ahead to effectively apply RAG to LLMs.

---

### 7. Benchmarking Retrieval-Augmented Generation for Medicine

**Authors:** Guangzhi Xiong, Qiao Jin, Zhiyong Lu, et al.  
**Year:** 2024 | **Citations:** 543 | **Venue:** Annual Meeting of the Association for Computational Linguistics  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b798cf6af813638fab09a8af6ad0f3df6c241485](https://www.semanticscholar.org/paper/b798cf6af813638fab09a8af6ad0f3df6c241485)  
**arXiv:** [https://arxiv.org/abs/2402.13178](https://arxiv.org/abs/2402.13178)  

**Abstract:** While large language models (LLMs) have achieved state-of-the-art performance on a wide range of medical question answering (QA) tasks, they still face challenges with hallucinations and outdated knowledge. Retrieval-augmented generation (RAG) is a promising solution and has been widely adopted. However, a RAG system can involve multiple flexible components, and there is a lack of best practices regarding the optimal RAG setting for various medical purposes. To systematically evaluate such systems, we propose the Medical Information Retrieval-Augmented Generation Evaluation (MIRAGE), a first-of-its-kind benchmark including 7,663 questions from five medical QA datasets. Using MIRAGE, we conducted large-scale experiments with over 1.8 trillion prompt tokens on 41 combinations of different corpora, retrievers, and backbone LLMs through the MedRAG toolkit introduced in this work. Overall, MedRAG improves the accuracy of six different LLMs by up to 18% over chain-of-thought prompting, elevating the performance of GPT-3.5 and Mixtral to GPT-4-level. Our results show that the combination of various medical corpora and retrievers achieves the best performance. In addition, we discovered a log-linear scaling property and the"lost-in-the-middle"effects in medical RAG. We believe our comprehensive evaluations can serve as practical guidelines for implementing RAG systems for medicine.

---

### 8. Graph Retrieval-Augmented Generation: A Survey

**Authors:** Boci Peng, Yun Zhu, Yongchao Liu, et al.  
**Year:** 2024 | **Citations:** 450 | **Venue:** ACM Trans. Inf. Syst.  
**Year Month:** [Aug 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/9ab45aa875b56335303398e84a59a3756cd9d530](https://www.semanticscholar.org/paper/9ab45aa875b56335303398e84a59a3756cd9d530)  
**arXiv:** [https://arxiv.org/abs/2408.08921](https://arxiv.org/abs/2408.08921)  

**Abstract:** Recently, Retrieval-Augmented Generation (RAG) has achieved remarkable success in addressing the challenges of Large Language Models (LLMs) without necessitating retraining. By referencing an external knowledge base, RAG refines LLM outputs, effectively mitigating issues such as “hallucination,” lack of domain-specific knowledge, and outdated information. However, the complex structure of relationships among different entities in databases presents challenges for RAG systems. In response, GraphRAG leverages structural information across entities to enable more precise and comprehensive retrieval, capturing relational knowledge and facilitating more accurate, context-aware responses. Given the novelty and potential of GraphRAG, a systematic review of current technologies is imperative. This article provides the first comprehensive overview of GraphRAG methodologies. We formalize the GraphRAG workflow, encompassing Graph-Based Indexing, Graph-Guided Retrieval, and Graph-Enhanced Generation. We then outline the core technologies and training methods at each stage. Additionally, we examine downstream tasks, application domains, evaluation methodologies, and industrial use cases of GraphRAG. Finally, we explore future research directions to inspire further inquiries and advance progress in the field. In order to track recent progress, we set up a repository at https://github.com/pengboci/GraphRAG-Survey.

---

### 9. LightRAG: Simple and Fast Retrieval-Augmented Generation

**Authors:** Zirui Guo, Lianghao Xia, Yanhua Yu, et al.  
**Year:** 2024 | **Citations:** 347 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [Oct 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1ea143c34b9bc359780f79ba4d68dee68bcc1129](https://www.semanticscholar.org/paper/1ea143c34b9bc359780f79ba4d68dee68bcc1129)  
**arXiv:** [https://arxiv.org/abs/2410.05779](https://arxiv.org/abs/2410.05779)  

**Abstract:** Retrieval-Augmented Generation (RAG) systems enhance large language models (LLMs) by integrating external knowledge sources, enabling more accurate and contextually relevant responses tailored to user needs. However, existing RAG systems have significant limitations, including reliance on flat data representations and inadequate contextual awareness, which can lead to fragmented answers that fail to capture complex inter-dependencies. To address these challenges, we propose LightRAG, which incorporates graph structures into text indexing and retrieval processes. This innovative framework employs a dual-level retrieval system that enhances comprehensive information retrieval from both low-level and high-level knowledge discovery. Additionally, the integration of graph structures with vector representations facilitates efficient retrieval of related entities and their relationships, significantly improving response times while maintaining contextual relevance. This capability is further enhanced by an incremental update algorithm that ensures the timely integration of new data, allowing the system to remain effective and responsive in rapidly changing data environments. Extensive experimental validation demonstrates considerable improvements in retrieval accuracy and efficiency compared to existing approaches. We have made our LightRAG open-source and available at the link: https://github.com/HKUDS/LightRAG

---

### 10. Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG

**Authors:** Aditi Singh, Abul Ehtesham, Saket Kumar, et al.  
**Year:** 2025 | **Citations:** 332 | **Venue:** arXiv.org  
**Year Month:** [Jan 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ba7952e7c4fb891c36980ca19f94251257da6eb7](https://www.semanticscholar.org/paper/ba7952e7c4fb891c36980ca19f94251257da6eb7)  
**arXiv:** [https://arxiv.org/abs/2501.09136](https://arxiv.org/abs/2501.09136)  

**Abstract:** Large Language Models (LLMs) have advanced artificial intelligence by enabling human-like text generation and natural language understanding. However, their reliance on static training data limits their ability to respond to dynamic, real-time queries, resulting in outdated or inaccurate outputs. Retrieval-Augmented Generation (RAG) has emerged as a solution, enhancing LLMs by integrating real-time data retrieval to provide contextually relevant and up-to-date responses. Despite its promise, traditional RAG systems are constrained by static workflows and lack the adaptability required for multi-step reasoning and complex task management. Agentic Retrieval-Augmented Generation (Agentic RAG) transcends these limitations by embedding autonomous AI agents into the RAG pipeline. These agents leverage agentic design patterns reflection, planning, tool use, and multi-agent collaboration to dynamically manage retrieval strategies, iteratively refine contextual understanding, and adapt workflows through operational structures ranging from sequential steps to adaptive collaboration. This integration enables Agentic RAG systems to deliver flexibility, scalability, and context-awareness across diverse applications. This paper presents an analytical survey of Agentic RAG systems. It traces the evolution of RAG paradigms, introduces a principled taxonomy of Agentic RAG architectures based on agent cardinality, control structure, autonomy, and knowledge representation, and provides a comparative analysis of design trade-offs across existing frameworks. The survey examines applications in healthcare, finance, education, and enterprise document processing, and distills practical lessons for system designers and practitioners. Finally, it identifies key open research challenges related to evaluation, coordination, memory management, efficiency, and governance, outlining directions for future research.

---

### 11. G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering

**Authors:** Xiaoxin He, Yijun Tian, Yifei Sun, et al.  
**Year:** 2024 | **Citations:** 296 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/a41d4a3b005c8ec4f821e6ee96672d930ca9596c](https://www.semanticscholar.org/paper/a41d4a3b005c8ec4f821e6ee96672d930ca9596c)  
**arXiv:** [https://arxiv.org/abs/2402.07630](https://arxiv.org/abs/2402.07630)  

**Abstract:** Given a graph with textual attributes, we enable users to `chat with their graph': that is, to ask questions about the graph using a conversational interface. In response to a user's questions, our method provides textual replies and highlights the relevant parts of the graph. While existing works integrate large language models (LLMs) and graph neural networks (GNNs) in various ways, they mostly focus on either conventional graph tasks (such as node, edge, and graph classification), or on answering simple graph queries on small or synthetic graphs. In contrast, we develop a flexible question-answering framework targeting real-world textual graphs, applicable to multiple applications including scene graph understanding, common sense reasoning, and knowledge graph reasoning. Toward this goal, we first develop a Graph Question Answering (GraphQA) benchmark with data collected from different tasks. Then, we propose our G-Retriever method, introducing the first retrieval-augmented generation (RAG) approach for general textual graphs, which can be fine-tuned to enhance graph understanding via soft prompting. To resist hallucination and to allow for textual graphs that greatly exceed the LLM's context window size, G-Retriever performs RAG over a graph by formulating this task as a Prize-Collecting Steiner Tree optimization problem. Empirical evaluations show that our method outperforms baselines on textual graph tasks from multiple domains, scales well with larger graph sizes, and mitigates hallucination.~\footnote{Our codes and datasets are available at: \url{https://github.com/XiaoxinHe/G-Retriever}}

---

### 12. MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries

**Authors:** Yixuan Tang, Yi Yang  
**Year:** 2024 | **Citations:** 293 | **Venue:** arXiv.org  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/4e71624e90960cb003e311a0fe3b8be4c2863239](https://www.semanticscholar.org/paper/4e71624e90960cb003e311a0fe3b8be4c2863239)  
**arXiv:** [https://arxiv.org/abs/2401.15391](https://arxiv.org/abs/2401.15391)  

**Abstract:** Retrieval-augmented generation (RAG) augments large language models (LLM) by retrieving relevant knowledge, showing promising potential in mitigating LLM hallucinations and enhancing response quality, thereby facilitating the great adoption of LLMs in practice. However, we find that existing RAG systems are inadequate in answering multi-hop queries, which require retrieving and reasoning over multiple pieces of supporting evidence. Furthermore, to our knowledge, no existing RAG benchmarking dataset focuses on multi-hop queries. In this paper, we develop a novel dataset, MultiHop-RAG, which consists of a knowledge base, a large collection of multi-hop queries, their ground-truth answers, and the associated supporting evidence. We detail the procedure of building the dataset, utilizing an English news article dataset as the underlying RAG knowledge base. We demonstrate the benchmarking utility of MultiHop-RAG in two experiments. The first experiment compares different embedding models for retrieving evidence for multi-hop queries. In the second experiment, we examine the capabilities of various state-of-the-art LLMs, including GPT-4, PaLM, and Llama2-70B, in reasoning and answering multi-hop queries given the evidence. Both experiments reveal that existing RAG methods perform unsatisfactorily in retrieving and answering multi-hop queries. We hope MultiHop-RAG will be a valuable resource for the community in developing effective RAG systems, thereby facilitating greater adoption of LLMs in practice. The MultiHop-RAG and implemented RAG system is publicly available at https://github.com/yixuantt/MultiHop-RAG/.

---

### 13. RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs

**Authors:** Yue Yu, Wei Ping, Zihan Liu, et al.  
**Year:** 2024 | **Citations:** 282 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/80478de9c7a81561e2f3dac9b8b1ef3df389ff2d](https://www.semanticscholar.org/paper/80478de9c7a81561e2f3dac9b8b1ef3df389ff2d)  
**arXiv:** [https://arxiv.org/abs/2407.02485](https://arxiv.org/abs/2407.02485)  

**Abstract:** Large language models (LLMs) typically utilize the top-k contexts from a retriever in retrieval-augmented generation (RAG). In this work, we propose a novel instruction fine-tuning framework RankRAG, which instruction-tunes a single LLM for the dual purpose of context ranking and answer generation in RAG. In particular, the instruction-tuned LLMs work surprisingly well by adding a small fraction of ranking data into the training blend, and outperform existing expert ranking models, including the same LLM exclusively fine-tuned on a large amount of ranking data. For generation, we compare our model with many strong baselines, including GPT-4-0613, GPT-4-turbo-2024-0409, and ChatQA-1.5, an open-sourced model with the state-of-the-art performance on RAG benchmarks. Specifically, our Llama3-RankRAG significantly outperforms Llama3-ChatQA-1.5 and GPT-4 models on nine knowledge-intensive benchmarks. In addition, it also performs comparably to GPT-4 on five RAG benchmarks in the biomedical domain without instruction fine-tuning on biomedical data, demonstrating its superb capability for generalization to new domains.

---

### 14. Seven Failure Points When Engineering a Retrieval Augmented Generation System

**Authors:** Scott Barnett, Stefanus Kurniawan, Srikanth Thudumu, et al.  
**Year:** 2024 | **Citations:** 254 | **Venue:** 2024 IEEE/ACM 3rd International Conference on AI Engineering – Software Engineering for AI (CAIN)  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ba454ba8c594dfb86c25dff2e265c8a2686aa037](https://www.semanticscholar.org/paper/ba454ba8c594dfb86c25dff2e265c8a2686aa037)  
**arXiv:** [https://arxiv.org/abs/2401.05856](https://arxiv.org/abs/2401.05856)  

**Abstract:** Software engineers are increasingly adding semantic search capabilities to applications using a strategy known as Retrieval Augmented Generation (RAG). A RAG system involves finding documents that semantically match a query and then passing the documents to a large language model (LLM) such as ChatGPT to extract the right answer using an LLM. RAG systems aim to: a) reduce the problem of hallucinated responses from LLMs, b) link sources/references to generated responses, and c) remove the need for annotating documents with meta-data. However, RAG systems suffer from limitations inherent to information retrieval systems and from reliance on LLMs. In this paper, we present an experience report on the failure points of RAG systems from three case studies from separate domains: research, education, and biomedical. We share the lessons learned and present 7 failure points to consider when designing a RAG system. The two key takeaways arising from our work are: 1) validation of a RAG system is only feasible during operation, and 2) the robustness of a RAG system evolves rather than designed in at the start. We conclude with a list of potential research directions on RAG systems for the software engineering community.CCS CONCEPTS• Software and its engineering → Empirical software validation.

---

### 15. Corrective Retrieval Augmented Generation

**Authors:** Shi-Qi Yan, Jia-Chen Gu, Yun Zhu, et al.  
**Year:** 2024 | **Citations:** 232 | **Venue:** arXiv.org  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5bbc2b5aa6c63c6a2cfccf095d6020b063ad47ac](https://www.semanticscholar.org/paper/5bbc2b5aa6c63c6a2cfccf095d6020b063ad47ac)  
**arXiv:** [https://arxiv.org/abs/2401.15884](https://arxiv.org/abs/2401.15884)  

**Abstract:** Large language models (LLMs) inevitably exhibit hallucinations since the accuracy of generated texts cannot be secured solely by the parametric knowledge they encapsulate. Although retrieval-augmented generation (RAG) is a practicable complement to LLMs, it relies heavily on the relevance of retrieved documents, raising concerns about how the model behaves if retrieval goes wrong. To this end, we propose the Corrective Retrieval Augmented Generation (CRAG) to improve the robustness of generation. Specifically, a lightweight retrieval evaluator is designed to assess the overall quality of retrieved documents for a query, returning a confidence degree based on which different knowledge retrieval actions can be triggered. Since retrieval from static and limited corpora can only return sub-optimal documents, large-scale web searches are utilized as an extension for augmenting the retrieval results. Besides, a decompose-then-recompose algorithm is designed for retrieved documents to selectively focus on key information and filter out irrelevant information in them. CRAG is plug-and-play and can be seamlessly coupled with various RAG-based approaches. Experiments on four datasets covering short- and long-form generation tasks show that CRAG can significantly improve the performance of RAG-based approaches.

---

### 16. Retrieval-Augmented Generation with Graphs (GraphRAG)

**Authors:** Haoyu Han, Yu Wang, Harry Shomer, et al.  
**Year:** 2024 | **Citations:** 224 | **Venue:** arXiv.org  
**Year Month:** [Jan 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/12fb0a058ad69f85a2b59cf7a52a29cbb01d8a0b](https://www.semanticscholar.org/paper/12fb0a058ad69f85a2b59cf7a52a29cbb01d8a0b)  
**arXiv:** [https://arxiv.org/abs/2501.00309](https://arxiv.org/abs/2501.00309)  

**Abstract:** Retrieval-augmented generation (RAG) is a powerful technique that enhances downstream task execution by retrieving additional information, such as knowledge, skills, and tools from external sources. Graph, by its intrinsic"nodes connected by edges"nature, encodes massive heterogeneous and relational information, making it a golden resource for RAG in tremendous real-world applications. As a result, we have recently witnessed increasing attention on equipping RAG with Graph, i.e., GraphRAG. However, unlike conventional RAG, where the retriever, generator, and external data sources can be uniformly designed in the neural-embedding space, the uniqueness of graph-structured data, such as diverse-formatted and domain-specific relational knowledge, poses unique and significant challenges when designing GraphRAG for different domains. Given the broad applicability, the associated design challenges, and the recent surge in GraphRAG, a systematic and up-to-date survey of its key concepts and techniques is urgently desired. Following this motivation, we present a comprehensive and up-to-date survey on GraphRAG. Our survey first proposes a holistic GraphRAG framework by defining its key components, including query processor, retriever, organizer, generator, and data source. Furthermore, recognizing that graphs in different domains exhibit distinct relational patterns and require dedicated designs, we review GraphRAG techniques uniquely tailored to each domain. Finally, we discuss research challenges and brainstorm directions to inspire cross-disciplinary opportunities. Our survey repository is publicly maintained at https://github.com/Graph-RAG/GraphRAG/.

---

### 17. PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models

**Authors:** Wei Zou, Runpeng Geng, Binghui Wang, et al.  
**Year:** 2024 | **Citations:** 219 | **Venue:** USENIX Security Symposium  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/f4e06256ab07727ff4e0465deea83fcf45012354](https://www.semanticscholar.org/paper/f4e06256ab07727ff4e0465deea83fcf45012354)  
**arXiv:** [https://arxiv.org/abs/2402.07867](https://arxiv.org/abs/2402.07867)  

**Abstract:** Large language models (LLMs) have achieved remarkable success due to their exceptional generative capabilities. Despite their success, they also have inherent limitations such as a lack of up-to-date knowledge and hallucination. Retrieval-Augmented Generation (RAG) is a state-of-the-art technique to mitigate these limitations. The key idea of RAG is to ground the answer generation of an LLM on external knowledge retrieved from a knowledge database. Existing studies mainly focus on improving the accuracy or efficiency of RAG, leaving its security largely unexplored. We aim to bridge the gap in this work. We find that the knowledge database in a RAG system introduces a new and practical attack surface. Based on this attack surface, we propose PoisonedRAG, the first knowledge corruption attack to RAG, where an attacker could inject a few malicious texts into the knowledge database of a RAG system to induce an LLM to generate an attacker-chosen target answer for an attacker-chosen target question. We formulate knowledge corruption attacks as an optimization problem, whose solution is a set of malicious texts. Depending on the background knowledge (e.g., black-box and white-box settings) of an attacker on a RAG system, we propose two solutions to solve the optimization problem, respectively. Our results show PoisonedRAG could achieve a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts. We also evaluate several defenses and our results show they are insufficient to defend against PoisonedRAG, highlighting the need for new defenses.

---

### 18. The Good and The Bad: Exploring Privacy Issues in Retrieval-Augmented Generation (RAG)

**Authors:** Shenglai Zeng, Jiankun Zhang, Pengfei He, et al.  
**Year:** 2024 | **Citations:** 216 | **Venue:** Annual Meeting of the Association for Computational Linguistics  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ea89b058ce619ed16d4de633126b02a8179457c8](https://www.semanticscholar.org/paper/ea89b058ce619ed16d4de633126b02a8179457c8)  
**arXiv:** [https://arxiv.org/abs/2402.16893](https://arxiv.org/abs/2402.16893)  

**Abstract:** Retrieval-augmented generation (RAG) is a powerful technique to facilitate language model with proprietary and private data, where data privacy is a pivotal concern. Whereas extensive research has demonstrated the privacy risks of large language models (LLMs), the RAG technique could potentially reshape the inherent behaviors of LLM generation, posing new privacy issues that are currently under-explored. In this work, we conduct extensive empirical studies with novel attack methods, which demonstrate the vulnerability of RAG systems on leaking the private retrieval database. Despite the new risk brought by RAG on the retrieval data, we further reveal that RAG can mitigate the leakage of the LLMs' training data. Overall, we provide new insights in this paper for privacy protection of retrieval-augmented LLMs, which benefit both LLMs and RAG systems builders. Our code is available at https://github.com/phycholosogy/RAG-privacy.

---

### 19. VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents

**Authors:** Shi Yu, Chaoyue Tang, Bokai Xu, et al.  
**Year:** 2024 | **Citations:** 215 | **Venue:** International Conference on Learning Representations  
**Year Month:** [Oct 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/d9052dd87959e6076baf35e8f7ee87d568a32b58](https://www.semanticscholar.org/paper/d9052dd87959e6076baf35e8f7ee87d568a32b58)  
**arXiv:** [https://arxiv.org/abs/2410.10594](https://arxiv.org/abs/2410.10594)  

**Abstract:** Retrieval-augmented generation (RAG) is an effective technique that enables large language models (LLMs) to utilize external knowledge sources for generation. However, current RAG systems are solely based on text, rendering it impossible to utilize vision information like layout and images that play crucial roles in real-world multi-modality documents. In this paper, we introduce VisRAG, which tackles this issue by establishing a vision-language model (VLM)-based RAG pipeline. In this pipeline, instead of first parsing the document to obtain text, the document is directly embedded using a VLM as an image and then retrieved to enhance the generation of a VLM. Compared to traditional text-based RAG, VisRAG maximizes the retention and utilization of the data information in the original documents, eliminating the information loss introduced during the parsing process. We collect both open-source and synthetic data to train the retriever in VisRAG and explore a variety of generation methods. Experiments demonstrate that VisRAG outperforms traditional RAG in both the retrieval and generation stages, achieving a 20--40% end-to-end performance gain over traditional text-based RAG pipeline. Further analysis reveals that VisRAG is efficient in utilizing training data and demonstrates strong generalization capability, positioning it as a promising solution for RAG on multi-modality documents. Our code and data are available at https://github.com/openbmb/visrag.

---

### 20. FlashRAG: A Modular Toolkit for Efficient Retrieval-Augmented Generation Research

**Authors:** Jiajie Jin, Yutao Zhu, Xinyu Yang, et al.  
**Year:** 2024 | **Citations:** 202 | **Venue:** The Web Conference  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/daebec92963ab8dea492f0c209bdf57e87bcaa07](https://www.semanticscholar.org/paper/daebec92963ab8dea492f0c209bdf57e87bcaa07)  
**arXiv:** [https://arxiv.org/abs/2405.13576](https://arxiv.org/abs/2405.13576)  

**Abstract:** With the advent of large language models (LLMs) and multimodal large language models (MLLMs), the potential of retrieval-augmented generation (RAG) has attracted considerable research attention. However, the absence of a standardized framework for implementation, coupled with the inherently complex RAG process, makes it challenging and time-consuming for researchers to compare and evaluate these approaches in a consistent environment. In response to this challenge, we develop FlashRAG, an efficient and modular open-source toolkit designed to assist researchers in reproducing and comparing existing RAG methods and developing their own algorithms within a unified framework. Our toolkit has implemented 16 advanced RAG methods and gathered and organized 38 benchmark datasets. It has various features, including a customizable modular framework, a rich collection of pre-implemented RAG works, comprehensive datasets, efficient auxiliary pre-processing scripts, and extensive and standard evaluation metrics. Our toolkit and resources are available at https://github.com/RUC-NLPIR/FlashRAG.

---

### 21. RQ-RAG: Learning to Refine Queries for Retrieval Augmented Generation

**Authors:** Chi-Min Chan, Chunpu Xu, Ruibin Yuan, et al.  
**Year:** 2024 | **Citations:** 190 | **Venue:** arXiv.org  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/746b96ee17e329f1085a047116c05e12eaa3925a](https://www.semanticscholar.org/paper/746b96ee17e329f1085a047116c05e12eaa3925a)  
**arXiv:** [https://arxiv.org/abs/2404.00610](https://arxiv.org/abs/2404.00610)  

**Abstract:** Large Language Models (LLMs) exhibit remarkable capabilities but are prone to generating inaccurate or hallucinatory responses. This limitation stems from their reliance on vast pretraining datasets, making them susceptible to errors in unseen scenarios. To tackle these challenges, Retrieval-Augmented Generation (RAG) addresses this by incorporating external, relevant documents into the response generation process, thus leveraging non-parametric knowledge alongside LLMs' in-context learning abilities. However, existing RAG implementations primarily focus on initial input for context retrieval, overlooking the nuances of ambiguous or complex queries that necessitate further clarification or decomposition for accurate responses. To this end, we propose learning to Refine Query for Retrieval Augmented Generation (RQ-RAG) in this paper, endeavoring to enhance the model by equipping it with capabilities for explicit rewriting, decomposition, and disambiguation. Our experimental results indicate that our method, when applied to a 7B Llama2 model, surpasses the previous state-of-the-art (SOTA) by an average of 1.9\% across three single-hop QA datasets, and also demonstrates enhanced performance in handling complex, multi-hop QA datasets. Our code is available at https://github.com/chanchimin/RQ-RAG.

---

### 22. MedRAG: Enhancing Retrieval-augmented Generation with Knowledge Graph-Elicited Reasoning for Healthcare Copilot

**Authors:** Xuejiao Zhao, Siyan Liu, Su-Yin Yang, et al.  
**Year:** 2025 | **Citations:** 163 | **Venue:** The Web Conference  
**Year Month:** [Feb 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/da83852315c884c73dc527a4b7bc1209fbb037c3](https://www.semanticscholar.org/paper/da83852315c884c73dc527a4b7bc1209fbb037c3)  
**arXiv:** [https://arxiv.org/abs/2502.04413](https://arxiv.org/abs/2502.04413)  

**Abstract:** Retrieval-augmented generation (RAG) is a well-suited technique for retrieving privacy-sensitive Electronic Health Records (EHR). It can serve as a key module of the healthcare copilot, helping reduce misdiagnosis for healthcare practitioners and patients. However, the diagnostic accuracy and specificity of existing heuristic-based RAG models used in the medical domain are inadequate, particularly for diseases with similar manifestations. This paper proposes MedRAG, a RAG model enhanced by knowledge graph (KG)-elicited reasoning for the medical domain that retrieves diagnosis and treatment recommendations based on manifestations. MedRAG systematically constructs a comprehensive four-tier hierarchical diagnostic KG encompassing critical diagnostic differences of various diseases. These differences are dynamically integrated with similar EHRs retrieved from an EHR database, and reasoned within a large language model. This process enables more accurate and specific decision support, while also proactively providing follow-up questions to enhance personalized medical decision-making. MedRAG is evaluated on both a public dataset DDXPlus and a private chronic pain diagnostic dataset (CPDD) collected from Tan Tock Seng Hospital, and its performance is compared against various existing RAG methods. Experimental results show that, leveraging the information integration and relational abilities of the KG, our MedRAG provides more specific diagnostic insights and outperforms state-of-the-art models in reducing misdiagnosis rates. Our code will be available at https://github.com/SNOWTEAM2023/MedRAG

---

### 23. Fact, Fetch, and Reason: A Unified Evaluation of Retrieval-Augmented Generation

**Authors:** Satyapriya Krishna, Kalpesh Krishna, Anhad Mohananey, et al.  
**Year:** 2024 | **Citations:** 157 | **Venue:** North American Chapter of the Association for Computational Linguistics  
**Year Month:** [Sep 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/46ff7e02fd4ff5fdfb9f85bc7071725b8089061f](https://www.semanticscholar.org/paper/46ff7e02fd4ff5fdfb9f85bc7071725b8089061f)  
**arXiv:** [https://arxiv.org/abs/2409.12941](https://arxiv.org/abs/2409.12941)  

**Abstract:** Large Language Models (LLMs) have demonstrated significant performance improvements across various cognitive tasks. An emerging application is using LLMs to enhance retrieval-augmented generation (RAG) capabilities. These systems require LLMs to understand user queries, retrieve relevant information, and synthesize coherent and accurate responses. Given the increasing real-world deployment of such systems, comprehensive evaluation becomes crucial. To this end, we propose FRAMES (Factuality, Retrieval, And reasoning MEasurement Set), a high-quality evaluation dataset designed to test LLMs' ability to provide factual responses, assess retrieval capabilities, and evaluate the reasoning required to generate final answers. While previous work has provided datasets and benchmarks to evaluate these abilities in isolation, FRAMES offers a unified framework that provides a clearer picture of LLM performance in end-to-end RAG scenarios. Our dataset comprises challenging multi-hop questions that require the integration of information from multiple sources. We present baseline results demonstrating that even state-of-the-art LLMs struggle with this task, achieving 0.40 accuracy with no retrieval. The accuracy is significantly improved with our proposed multi-step retrieval pipeline, achieving an accuracy of 0.66 (>50% improvement). We hope our work will help bridge evaluation gaps and assist in developing more robust and capable RAG systems.

---

### 24. Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach

**Authors:** Zhuowan Li, Cheng Li, Mingyang Zhang, et al.  
**Year:** 2024 | **Citations:** 155 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ccb5afb760a73f5507e31995397f80960db7842d](https://www.semanticscholar.org/paper/ccb5afb760a73f5507e31995397f80960db7842d)  
**arXiv:** [https://arxiv.org/abs/2407.16833](https://arxiv.org/abs/2407.16833)  

**Abstract:** Retrieval Augmented Generation (RAG) has been a powerful tool for Large Language Models (LLMs) to efficiently process overly lengthy contexts. However, recent LLMs like Gemini-1.5 and GPT-4 show exceptional capabilities to understand long contexts directly. We conduct a comprehensive comparison between RAG and long-context (LC) LLMs, aiming to leverage the strengths of both. We benchmark RAG and LC across various public datasets using three latest LLMs. Results reveal that when resourced sufficiently, LC consistently outperforms RAG in terms of average performance. However, RAG’s significantly lower cost remains a distinct advantage. Based on this observation, we propose Self-Route, a simple yet effective method that routes queries to RAG or LC based on model self-reflection. Self-Route significantly reduces the computation cost while maintaining a comparable performance to LC. Our findings provide a guideline for long-context applications of LLMs using RAG and LC.

---

### 25. Improving large language model applications in biomedicine with retrieval-augmented generation: a systematic review, meta-analysis, and clinical development guidelines

**Authors:** Siru Liu, Allison B. McCoy, Adam Wright  
**Year:** 2025 | **Citations:** 140 | **Venue:** J. Am. Medical Informatics Assoc.  
**Fields:** Computer Science, Medicine  
**URL:** [https://www.semanticscholar.org/paper/83939671534dc3d374c9bc4e3e03b5ec2c7ba301](https://www.semanticscholar.org/paper/83939671534dc3d374c9bc4e3e03b5ec2c7ba301)  

**Abstract:** Abstract Objective The objectives of this study are to synthesize findings from recent research of retrieval-augmented generation (RAG) and large language models (LLMs) in biomedicine and provide clinical development guidelines to improve effectiveness. Materials and Methods We conducted a systematic literature review and a meta-analysis. The report was created in adherence to the Preferred Reporting Items for Systematic Reviews and Meta-Analyses 2020 analysis. Searches were performed in 3 databases (PubMed, Embase, PsycINFO) using terms related to “retrieval augmented generation” and “large language model,” for articles published in 2023 and 2024. We selected studies that compared baseline LLM performance with RAG performance. We developed a random-effect meta-analysis model, using odds ratio as the effect size. Results Among 335 studies, 20 were included in this literature review. The pooled effect size was 1.35, with a 95% confidence interval of 1.19-1.53, indicating a statistically significant effect (P = .001). We reported clinical tasks, baseline LLMs, retrieval sources and strategies, as well as evaluation methods. Discussion Building on our literature review, we developed Guidelines for Unified Implementation and Development of Enhanced LLM Applications with RAG in Clinical Settings to inform clinical applications using RAG. Conclusion Overall, RAG implementation showed a 1.35 odds ratio increase in performance compared to baseline LLMs. Future research should focus on (1) system-level enhancement: the combination of RAG and agent, (2) knowledge-level enhancement: deep integration of knowledge into LLM, and (3) integration-level enhancement: integrating RAG systems within electronic health records.

---

### 26. RAGCache: Efficient Knowledge Caching for Retrieval-Augmented Generation

**Authors:** Chao Jin, Zili Zhang, Xu Jiang, et al.  
**Year:** 2024 | **Citations:** 122 | **Venue:** ACM Transactions on Computer Systems  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/7326329c09c11aac423ef4910222a16952bb01dc](https://www.semanticscholar.org/paper/7326329c09c11aac423ef4910222a16952bb01dc)  
**arXiv:** [https://arxiv.org/abs/2404.12457](https://arxiv.org/abs/2404.12457)  

**Abstract:** Retrieval-Augmented Generation (RAG) has demonstrated substantial advancements in various natural language processing tasks by integrating the strengths of large language models (LLMs) and external knowledge databases. However, the retrieval step introduces long sequence generation and extra data dependency, resulting in long end-to-end latency. Our analysis benchmarks current RAG systems and reveals that, while the retrieval step poses performance challenges, it also offers optimization opportunities through its retrieval pattern and streaming search behavior. We propose RAGCache, a latency-optimized serving system tailored for RAG. RAGCache leverages the retrieval pattern to organize and cache the intermediate states of retrieved knowledge in a knowledge tree across the GPU and host memory hierarchy, reducing LLM generation time. RAGCache employs dynamic speculative pipelining to exploit the streaming search behavior, overlapping retrieval with LLM generation to minimize end-to-end latency. We implement RAGCache based on vLLM and Faiss, and evaluate it on both open-source and production datasets. Experimental results demonstrate that RAGCache reduces the time to first token (TTFT) by up to 4× and improves the throughput by up to 2.1× compared to vLLM integrated with Faiss.

---

### 27. A Survey of Graph Retrieval-Augmented Generation for Customized Large Language Models

**Authors:** Qinggang Zhang, Shengyuan Chen, Yuan-Qi Bei, et al.  
**Year:** 2025 | **Citations:** 117 | **Venue:** arXiv.org  
**Year Month:** [Jan 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/908d45b0d2b88ba72ee501c368eb618d29d61ce0](https://www.semanticscholar.org/paper/908d45b0d2b88ba72ee501c368eb618d29d61ce0)  
**arXiv:** [https://arxiv.org/abs/2501.13958](https://arxiv.org/abs/2501.13958)  

**Abstract:** Large language models (LLMs) have demonstrated remarkable capabilities in a wide range of tasks, yet their application to specialized domains remains challenging due to the need for deep expertise. Retrieval-Augmented generation (RAG) has emerged as a promising solution to customize LLMs for professional fields by seamlessly integrating external knowledge bases, enabling real-time access to domain-specific expertise during inference. Despite its potential, traditional RAG systems, based on flat text retrieval, face three critical challenges: (i) complex query understanding in professional contexts, (ii) difficulties in knowledge integration across distributed sources, and (iii) system efficiency bottlenecks at scale. This survey presents a systematic analysis of Graph-based Retrieval-Augmented Generation (GraphRAG), a new paradigm that revolutionizes domain-specific LLM applications. GraphRAG addresses traditional RAG limitations through three key innovations: (i) graph-structured knowledge representation that explicitly captures entity relationships and domain hierarchies, (ii) efficient graph-based retrieval techniques that enable context-preserving knowledge retrieval with multihop reasoning ability, and (iii) structure-aware knowledge integration algorithms that leverage retrieved knowledge for accurate and logical coherent generation of LLMs. In this survey, we systematically analyze the technical foundations of GraphRAG and examine current implementations across various professional domains, identifying key technical challenges and promising research directions. All the related resources of GraphRAG, including research papers, open-source data, and projects, are collected for the community in https://github.com/DEEP-PolyU/Awesome-GraphRAG.

---

### 28. xRAG: Extreme Context Compression for Retrieval-augmented Generation with One Token

**Authors:** Xin Cheng, Xun Wang, Xingxing Zhang, et al.  
**Year:** 2024 | **Citations:** 116 | **Venue:** Neural Information Processing Systems  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/38fcc3667a907d6c94267c674aad114aae68441e](https://www.semanticscholar.org/paper/38fcc3667a907d6c94267c674aad114aae68441e)  
**arXiv:** [https://arxiv.org/abs/2405.13792](https://arxiv.org/abs/2405.13792)  

**Abstract:** This paper introduces xRAG, an innovative context compression method tailored for retrieval-augmented generation. xRAG reinterprets document embeddings in dense retrieval--traditionally used solely for retrieval--as features from the retrieval modality. By employing a modality fusion methodology, xRAG seamlessly integrates these embeddings into the language model representation space, effectively eliminating the need for their textual counterparts and achieving an extreme compression rate. In xRAG, the only trainable component is the modality bridge, while both the retriever and the language model remain frozen. This design choice allows for the reuse of offline-constructed document embeddings and preserves the plug-and-play nature of retrieval augmentation. Experimental results demonstrate that xRAG achieves an average improvement of over 10% across six knowledge-intensive tasks, adaptable to various language model backbones, ranging from a dense 7B model to an 8x7B Mixture of Experts configuration. xRAG not only significantly outperforms previous context compression methods but also matches the performance of uncompressed models on several datasets, while reducing overall FLOPs by a factor of 3.53. Our work pioneers new directions in retrieval-augmented generation from the perspective of multimodality fusion, and we hope it lays the foundation for future efficient and scalable retrieval-augmented systems

---


## AI Agents

*Retrieved: 2026-07-01 10:55:39*

### 1. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**Authors:** John Yang, Carlos E. Jimenez, Alexander Wettig, et al.  
**Year:** 2024 | **Citations:** 1,317 | **Venue:** Neural Information Processing Systems  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1c3c531fc0fbe79f97f367ed3648de8467caeeaa](https://www.semanticscholar.org/paper/1c3c531fc0fbe79f97f367ed3648de8467caeeaa)  
**arXiv:** [https://arxiv.org/abs/2405.15793](https://arxiv.org/abs/2405.15793)  

**Abstract:** Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use. We investigate how interface design affects the performance of language model agents. As a result of this exploration, we introduce SWE-agent: a system that facilitates LM agents to autonomously use computers to solve software engineering tasks. SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files, navigate entire repositories, and execute tests and other programs. We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art achieved with non-interactive LMs. Finally, we provide insight on how the design of the ACI can impact agents' behavior and performance.

---

### 2. Mind2Web: Towards a Generalist Agent for the Web

**Authors:** Xiang Deng, Yu Gu, Boyuan Zheng, et al.  
**Year:** 2023 | **Citations:** 1,213 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Jun 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/58f8925a8b87054ad0635a6398a7fe24935b1604](https://www.semanticscholar.org/paper/58f8925a8b87054ad0635a6398a7fe24935b1604)  
**arXiv:** [https://arxiv.org/abs/2306.06070](https://arxiv.org/abs/2306.06070)  

**Abstract:** We introduce Mind2Web, the first dataset for developing and evaluating generalist agents for the web that can follow language instructions to complete complex tasks on any website. Existing datasets for web agents either use simulated websites or only cover a limited set of websites and tasks, thus not suitable for generalist web agents. With over 2,000 open-ended tasks collected from 137 websites spanning 31 domains and crowdsourced action sequences for the tasks, Mind2Web provides three necessary ingredients for building generalist web agents: 1) diverse domains, websites, and tasks, 2) use of real-world websites instead of simulated and simplified ones, and 3) a broad spectrum of user interaction patterns. Based on Mind2Web, we conduct an initial exploration of using large language models (LLMs) for building generalist web agents. While the raw HTML of real-world websites are often too large to be fed to LLMs, we show that first filtering it with a small LM significantly improves the effectiveness and efficiency of LLMs. Our solution demonstrates a decent level of performance, even on websites or entire domains the model has never seen before, but there is still a substantial room to improve towards truly generalizable agents. We open-source our dataset, model implementation, and trained models (https://osu-nlp-group.github.io/Mind2Web) to facilitate further research on building a generalist agent for the web.

---

### 3. Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models

**Authors:** Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, et al.  
**Year:** 2023 | **Citations:** 533 | **Venue:** International Conference on Machine Learning  
**Year Month:** [Oct 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/700bd9681f1b9e9e2212e10415d27b11c7e6836b](https://www.semanticscholar.org/paper/700bd9681f1b9e9e2212e10415d27b11c7e6836b)  
**arXiv:** [https://arxiv.org/abs/2310.04406](https://arxiv.org/abs/2310.04406)  

**Abstract:** While language models (LMs) have shown potential across a range of decision-making tasks, their reliance on simple acting processes limits their broad deployment as autonomous agents. In this paper, we introduce Language Agent Tree Search (LATS) -- the first general framework that synergizes the capabilities of LMs in reasoning, acting, and planning. By leveraging the in-context learning ability of LMs, we integrate Monte Carlo Tree Search into LATS to enable LMs as agents, along with LM-powered value functions and self-reflections for proficient exploration and enhanced decision-making. A key feature of our approach is the incorporation of an environment for external feedback, which offers a more deliberate and adaptive problem-solving mechanism that surpasses the constraints of existing techniques. Our experimental evaluation across diverse domains, including programming, interactive question-answering (QA), web navigation, and math, validates the effectiveness and generality of LATS in decision-making while maintaining competitive or improved reasoning performance. Notably, LATS achieves state-of-the-art pass@1 accuracy (92.7%) for programming on HumanEval with GPT-4 and demonstrates gradient-free performance (average score of 75.9) comparable to gradient-based fine-tuning for web navigation on WebShop with GPT-3.5. Code can be found at https://github.com/lapisrocks/LanguageAgentTreeSearch

---

### 4. Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

**Authors:** P. Chhikara, Dev Khant, Saket Aryan, et al.  
**Year:** 2025 | **Citations:** 441 | **Venue:** European Conference on Artificial Intelligence  
**Year Month:** [Apr 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1d9c21a0fdb1cc16a32c5d490ebaf98436a23382](https://www.semanticscholar.org/paper/1d9c21a0fdb1cc16a32c5d490ebaf98436a23382)  
**arXiv:** [https://arxiv.org/abs/2504.19413](https://arxiv.org/abs/2504.19413)  

**Abstract:** Large Language Models (LLMs) have demonstrated remarkable prowess in generating contextually coherent responses, yet their fixed context windows pose fundamental challenges for maintaining consistency over prolonged multi-session dialogues. We introduce Mem0, a scalable memory-centric architecture that addresses this issue by dynamically extracting, consolidating, and retrieving salient information from ongoing conversations. Building on this foundation, we further propose an enhanced variant that leverages graph-based memory representations to capture complex relational structures among conversational elements. Through comprehensive evaluations on LOCOMO benchmark, we systematically compare our approaches against six baseline categories: (i) established memory-augmented systems, (ii) retrieval-augmented generation (RAG) with varying chunk sizes and k-values, (iii) a full-context approach that processes the entire conversation history, (iv) an open-source memory solution, (v) a proprietary model system, and (vi) a dedicated memory management platform. Empirical results show that our methods consistently outperform all existing memory systems across four question categories: single-hop, temporal, multi-hop, and open-domain. Notably, Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI, while Mem0 with graph memory achieves around 2% higher overall score than the base configuration. Beyond accuracy gains, we also markedly reduce computational overhead compared to full-context method. In particular, Mem0 attains a 91% lower p95 latency and saves more than 90% token cost, offering a compelling balance between advanced reasoning capabilities and practical deployment constraints. Our findings highlight critical role of structured, persistent memory mechanisms for long-term conversational coherence, paving the way for more reliable and efficient LLM-driven AI agents.

---

### 5. AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges

**Authors:** Ranjan Sapkota, Konstantinos I. Roumeliotis, Manoj Karkee  
**Year:** 2025 | **Citations:** 404 | **Venue:** Information Fusion  
**Year Month:** [May 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/986e813f4c4f36786c3642cb9c8718586e47bdcf](https://www.semanticscholar.org/paper/986e813f4c4f36786c3642cb9c8718586e47bdcf)  
**arXiv:** [https://arxiv.org/abs/2505.10468](https://arxiv.org/abs/2505.10468)  

**Abstract:** This review critically distinguishes between AI Agents and Agentic AI, offering a structured, conceptual taxonomy, application mapping, and analysis of opportunities and challenges to clarify their divergent design philosophies and capabilities. We begin by outlining the search strategy and foundational definitions, characterizing AI Agents as modular systems driven and enabled by LLMs and LIMs for taskspecific automation. Generative AI is positioned as a precursor providing the foundation, with AI agents advancing through tool integration, prompt engineering, and reasoning enhancements. We then characterize Agentic AI systems, which, in contrast to AI Agents, represent a paradigm shift marked by multi-agent collaboration, dynamic task decomposition, persistent memory, and coordinated autonomy. Through a chronological evaluation of architectural evolution, operational mechanisms, interaction styles, and autonomy levels, we present a comparative analysis across both AI agents and agentic AI paradigms. Application domains enabled by AI Agents such as customer support, scheduling, and data summarization are then contrasted with Agentic AI deployments in research automation, robotic coordination, and medical decision support. We further examine unique challenges in each paradigm including hallucination, brittleness, emergent behavior, and coordination failure, and propose targeted solutions such as ReAct loops, retrieval-augmented generation (RAG), automation coordination layers, and causal modeling. This work aims to provide a roadmap for developing robust, scalable, and explainable AI-driven systems.  

---

### 6. Identifying the Risks of LM Agents with an LM-Emulated Sandbox

**Authors:** Yangjun Ruan, Honghua Dong, Andrew Wang, et al.  
**Year:** 2023 | **Citations:** 396 | **Venue:** International Conference on Learning Representations  
**Year Month:** [Sep 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/0a893657e00fe8ecfadcc65c63bf293e70cb1564](https://www.semanticscholar.org/paper/0a893657e00fe8ecfadcc65c63bf293e70cb1564)  
**arXiv:** [https://arxiv.org/abs/2309.15817](https://arxiv.org/abs/2309.15817)  

**Abstract:** Recent advances in Language Model (LM) agents and tool use, exemplified by applications like ChatGPT Plugins, enable a rich set of capabilities but also amplify potential risks - such as leaking private data or causing financial losses. Identifying these risks is labor-intensive, necessitating implementing the tools, setting up the environment for each test scenario manually, and finding risky cases. As tools and agents become more complex, the high cost of testing these agents will make it increasingly difficult to find high-stakes, long-tailed risks. To address these challenges, we introduce ToolEmu: a framework that uses an LM to emulate tool execution and enables the testing of LM agents against a diverse range of tools and scenarios, without manual instantiation. Alongside the emulator, we develop an LM-based automatic safety evaluator that examines agent failures and quantifies associated risks. We test both the tool emulator and evaluator through human evaluation and find that 68.8% of failures identified with ToolEmu would be valid real-world agent failures. Using our curated initial benchmark consisting of 36 high-stakes tools and 144 test cases, we provide a quantitative risk analysis of current LM agents and identify numerous failures with potentially severe outcomes. Notably, even the safest LM agent exhibits such failures 23.9% of the time according to our evaluator, underscoring the need to develop safer LM agents for real-world deployment.

---

### 7. Enhanced Moth-flame optimizer with mutation strategy for global optimization

**Authors:** Yueting Xu, Huiling Chen, Jie Luo, et al.  
**Year:** 2019 | **Citations:** 393 | **Venue:** Information Sciences  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/86494f58ce119d97cd0a07a5a2f5084048936af6](https://www.semanticscholar.org/paper/86494f58ce119d97cd0a07a5a2f5084048936af6)  

**Abstract:** Abstract Moth-flame optimization (MFO) is a widely used nature-inspired algorithm characterized by a simple structure with simple parameters. However, for some complex optimization tasks, especially the high dimensional and multimodal problems, MFO may have problems with convergence or tend to fall into local optima. To overcome these limitations, here a series of new variants of MFO are proposed by combining MFO with Gaussian mutation (GM), Cauchy mutation (CM), Levy mutation (LM) or the combination of GM, CM and LM. Specifically, GM is introduced into the basic MFO to improve neighborhood-informed capability. Then, CM with a large mutation step is adopted to enhance global exploration ability. Finally, LM is embedded to increase the randomness of search agents’ movement. The best variant of MFO was compared to 15 state-of-the-art algorithms and 4 well-known advanced optimization approaches on a comprehensive set of 23 benchmark problems and 30 CEC2017 benchmark tasks. The experimental results demonstrate that the three strategies can signiﬁcantly boost exploration and exploitation capabilities of the basic MFO.

---

### 8. Empowering Biomedical Discovery with AI Agents

**Authors:** Shanghua Gao, Ada Fang, Yepeng Huang, et al.  
**Year:** 2024 | **Citations:** 336 | **Venue:** Cell  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science, Medicine  
**URL:** [https://www.semanticscholar.org/paper/8cedeb11139eab187e43414fd7097c5d578dad7c](https://www.semanticscholar.org/paper/8cedeb11139eab187e43414fd7097c5d578dad7c)  
**arXiv:** [https://arxiv.org/abs/2404.02831](https://arxiv.org/abs/2404.02831)  

**Abstract:** We envision "AI scientists" as systems capable of skeptical learning and reasoning that empower biomedical research through collaborative agents that integrate AI models and biomedical tools with experimental platforms. Rather than taking humans out of the discovery process, biomedical AI agents combine human creativity and expertise with AI's ability to analyze large datasets, navigate hypothesis spaces, and execute repetitive tasks. AI agents are poised to be proficient in various tasks, planning discovery workflows and performing self-assessment to identify and mitigate gaps in their knowledge. These agents use large language models and generative models to feature structured memory for continual learning and use machine learning tools to incorporate scientific knowledge, biological principles, and theories. AI agents can impact areas ranging from virtual cell simulation, programmable control of phenotypes, and the design of cellular circuits to developing new therapies.

---

### 9. Pre-Trained Language Models for Interactive Decision-Making

**Authors:** Shuang Li, Xavier Puig, Yilun Du, et al.  
**Year:** 2022 | **Citations:** 334 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Feb 2022]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b9b220b485d2add79118ffdc2aaa148b67fa53ef](https://www.semanticscholar.org/paper/b9b220b485d2add79118ffdc2aaa148b67fa53ef)  
**arXiv:** [https://arxiv.org/abs/2202.01771](https://arxiv.org/abs/2202.01771)  

**Abstract:** Language model (LM) pre-training is useful in many language processing tasks. But can pre-trained LMs be further leveraged for more general machine learning problems? We propose an approach for using LMs to scaffold learning and generalization in general sequential decision-making problems. In this approach, goals and observations are represented as a sequence of embeddings, and a policy network initialized with a pre-trained LM predicts the next action. We demonstrate that this framework enables effective combinatorial generalization across different environments and supervisory modalities. We begin by assuming access to a set of expert demonstrations, and show that initializing policies with LMs and fine-tuning them via behavior cloning improves task completion rates by 43.6% in the VirtualHome environment. Next, we integrate an active data gathering procedure in which agents iteratively interact with the environment, relabel past"failed"experiences with new goals, and update their policies in a self-supervised loop. Active data gathering further improves combinatorial generalization, outperforming the best baseline by 25.1%. Finally, we explain these results by investigating three possible factors underlying the effectiveness of the LM-based policy. We find that sequential input representations (vs. fixed-dimensional feature vectors) and LM-based weight initialization are both important for generalization. Surprisingly, however, the format of the policy inputs encoding (e.g. as a natural language string vs. an arbitrary sequential encoding) has little influence. Together, these results suggest that language modeling induces representations that are useful for modeling not just language, but also goals and plans; these representations can aid learning and generalization even outside of language processing.

---

### 10. Small Language Models are the Future of Agentic AI

**Authors:** Peter Belcák, Greg Heinrich, Shizhe Diao, et al.  
**Year:** 2025 | **Citations:** 288 | **Venue:** arXiv.org  
**Year Month:** [Jun 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/f1d477ccd20b3e90611fc46b1951b3708651a425](https://www.semanticscholar.org/paper/f1d477ccd20b3e90611fc46b1951b3708651a425)  
**arXiv:** [https://arxiv.org/abs/2506.02153](https://arxiv.org/abs/2506.02153)  

**Abstract:** Large language models (LLMs) are often praised for exhibiting near-human performance on a wide range of tasks and valued for their ability to hold a general conversation. The rise of agentic AI systems is, however, ushering in a mass of applications in which language models perform a small number of specialized tasks repetitively and with little variation. Here we lay out the position that small language models (SLMs) are sufficiently powerful, inherently more suitable, and necessarily more economical for many invocations in agentic systems, and are therefore the future of agentic AI. Our argumentation is grounded in the current level of capabilities exhibited by SLMs, the common architectures of agentic systems, and the economy of LM deployment. We further argue that in situations where general-purpose conversational abilities are essential, heterogeneous agentic systems (i.e., agents invoking multiple different models) are the natural choice. We discuss the potential barriers for the adoption of SLMs in agentic systems and outline a general LLM-to-SLM agent conversion algorithm. Our position, formulated as a value statement, highlights the significance of the operational and economic impact even a partial shift from LLMs to SLMs is to have on the AI agent industry. We aim to stimulate the discussion on the effective use of AI resources and hope to advance the efforts to lower the costs of AI of the present day. Calling for both contributions to and critique of our position, we commit to publishing all such correspondence at https://research.nvidia.com/labs/lpr/slm-agents.

---

### 11. AI Agents Under Threat: A Survey of Key Security Challenges and Future Pathways

**Authors:** Zehang Deng, Yongjian Guo, Changzhou Han, et al.  
**Year:** 2024 | **Citations:** 239 | **Venue:** ACM Computing Surveys  
**Year Month:** [Jun 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5aacf780ec16a29bdbe283a14f5a9e6b7e1f292d](https://www.semanticscholar.org/paper/5aacf780ec16a29bdbe283a14f5a9e6b7e1f292d)  
**arXiv:** [https://arxiv.org/abs/2406.02630](https://arxiv.org/abs/2406.02630)  

**Abstract:** An Artificial Intelligence (AI) agent is a software entity that autonomously performs tasks or makes decisions based on pre-defined objectives and data inputs. AI agents, capable of perceiving user inputs, reasoning and planning tasks, and executing actions, have seen remarkable advancements in algorithm development and task performance. However, the security challenges they pose remain under-explored and unresolved. This survey delves into the emerging security threats faced by AI agents, categorizing them into four critical knowledge gaps: unpredictability of multi-step user inputs, complexity in internal executions, variability of operational environments, and interactions with untrusted external entities. By systematically reviewing these threats, this article highlights both the progress made and the existing limitations in safeguarding AI agents. The insights provided aim to inspire further research into addressing the security threats associated with AI agents, thereby fostering the development of more robust and secure AI agent applications.

---

### 12. Generative AI Agents With Large Language Model for Satellite Networks via a Mixture of Experts Transmission

**Authors:** Ruichen Zhang, Hongyang Du, Yinqiu Liu, et al.  
**Year:** 2024 | **Citations:** 232 | **Venue:** IEEE Journal on Selected Areas in Communications  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/6d533b0f318fd22d664356b56b68023560d3c60f](https://www.semanticscholar.org/paper/6d533b0f318fd22d664356b56b68023560d3c60f)  
**arXiv:** [https://arxiv.org/abs/2404.09134](https://arxiv.org/abs/2404.09134)  

**Abstract:** In response to the needs of 6G global communications, satellite communication networks have emerged as a key solution. However, the large-scale development of satellite communication networks is constrained by complex system models, whose modeling is challenging for massive users. Moreover, transmission interference between satellites and users seriously affects communication performance. To solve these problems, this paper develops generative artificial intelligence (AI) agents for model formulation and then applies a mixture of experts (MoE) approach to design transmission strategies. Specifically, we leverage large language models (LLMs) to build an interactive modeling paradigm and utilize retrieval-augmented generation (RAG) to extract satellite expert knowledge that supports mathematical modeling. Afterward, by integrating the expertise of multiple specialized components, we propose an MoE-proximal policy optimization (PPO) approach to solve the formulated problem. Each expert can optimize the optimization variables at which it excels through specialized training through its own network and then aggregate them through the gating network to perform joint optimization. The simulation results validate the accuracy and effectiveness of employing a generative agent for problem formulation. Furthermore, the superiority of the proposed MoE-ppo approach over other benchmarks is confirmed in solving the formulated problem. The adaptability of MoE-PPO to various customized modeling problems has also been demonstrated.

---

### 13. Do the Rewards Justify the Means? Measuring Trade-Offs Between Rewards and Ethical Behavior in the MACHIAVELLI Benchmark

**Authors:** Alexander Pan, C. Shern, Andy Zou, et al.  
**Year:** 2023 | **Citations:** 223 | **Venue:** International Conference on Machine Learning  
**Year Month:** [Apr 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5da2d404d789aeff266b63a760d07fe8bc31ba23](https://www.semanticscholar.org/paper/5da2d404d789aeff266b63a760d07fe8bc31ba23)  
**arXiv:** [https://arxiv.org/abs/2304.03279](https://arxiv.org/abs/2304.03279)  

**Abstract:** Artificial agents have traditionally been trained to maximize reward, which may incentivize power-seeking and deception, analogous to how next-token prediction in language models (LMs) may incentivize toxicity. So do agents naturally learn to be Machiavellian? And how do we measure these behaviors in general-purpose models such as GPT-4? Towards answering these questions, we introduce MACHIAVELLI, a benchmark of 134 Choose-Your-Own-Adventure games containing over half a million rich, diverse scenarios that center on social decision-making. Scenario labeling is automated with LMs, which are more performant than human annotators. We mathematize dozens of harmful behaviors and use our annotations to evaluate agents' tendencies to be power-seeking, cause disutility, and commit ethical violations. We observe some tension between maximizing reward and behaving ethically. To improve this trade-off, we investigate LM-based methods to steer agents' towards less harmful behaviors. Our results show that agents can both act competently and morally, so concrete progress can currently be made in machine ethics--designing agents that are Pareto improvements in both safety and capabilities.

---

### 14. Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents

**Authors:** Pranav Putta, Edmund Mills, Naman Garg, et al.  
**Year:** 2024 | **Citations:** 201 | **Venue:** arXiv.org  
**Year Month:** [Aug 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b393f619a87c5b6aa63c7abc7118263205b6aa62](https://www.semanticscholar.org/paper/b393f619a87c5b6aa63c7abc7118263205b6aa62)  
**arXiv:** [https://arxiv.org/abs/2408.07199](https://arxiv.org/abs/2408.07199)  

**Abstract:** Large Language Models (LLMs) have shown remarkable capabilities in natural language tasks requiring complex reasoning, yet their application in agentic, multi-step reasoning within interactive environments remains a difficult challenge. Traditional supervised pre-training on static datasets falls short in enabling autonomous agent capabilities needed to perform complex decision-making in dynamic settings like web navigation. Previous attempts to bridge this ga-through supervised fine-tuning on curated expert demonstrations-often suffer from compounding errors and limited exploration data, resulting in sub-optimal policy outcomes. To overcome these challenges, we propose a framework that combines guided Monte Carlo Tree Search (MCTS) search with a self-critique mechanism and iterative fine-tuning on agent interactions using an off-policy variant of the Direct Preference Optimization (DPO) algorithm. Our method allows LLM agents to learn effectively from both successful and unsuccessful trajectories, thereby improving their generalization in complex, multi-step reasoning tasks. We validate our approach in the WebShop environment-a simulated e-commerce platform where it consistently outperforms behavior cloning and reinforced fine-tuning baseline, and beats average human performance when equipped with the capability to do online search. In real-world booking scenarios, our methodology boosts Llama-3 70B model's zero-shot performance from 18.6% to 81.7% success rate (a 340% relative increase) after a single day of data collection and further to 95.4% with online search. We believe this represents a substantial leap forward in the capabilities of autonomous agents, paving the way for more sophisticated and reliable decision-making in real-world settings.

---

### 15. The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies

**Authors:** Kyle Swanson, Wesley Wu, Nash L. Bulaong, et al.  
**Year:** 2025 | **Citations:** 201 | **Venue:** Nature  
**Fields:** Medicine, Computer Science  
**URL:** [https://www.semanticscholar.org/paper/d24e37aafcf48c76aca30430670bad9a61cd0fca](https://www.semanticscholar.org/paper/d24e37aafcf48c76aca30430670bad9a61cd0fca)  
---

### 16. Memory in the Age of AI Agents

**Authors:** Yuyang Hu, Shichun Liu, Yanwei Yue, et al.  
**Year:** 2025 | **Citations:** 196 | **Venue:** arXiv.org  
**Year Month:** [Dec 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/d362b7619fcd2df4241696a19aec95961b8a729c](https://www.semanticscholar.org/paper/d362b7619fcd2df4241696a19aec95961b8a729c)  
**arXiv:** [https://arxiv.org/abs/2512.13564](https://arxiv.org/abs/2512.13564)  

**Abstract:** Memory has emerged, and will continue to remain, a core capability of foundation model-based agents. As research on agent memory rapidly expands and attracts unprecedented attention, the field has also become increasingly fragmented. Existing works that fall under the umbrella of agent memory often differ substantially in their motivations, implementations, and evaluation protocols, while the proliferation of loosely defined memory terminologies has further obscured conceptual clarity. Traditional taxonomies such as long/short-term memory have proven insufficient to capture the diversity of contemporary agent memory systems. This work aims to provide an up-to-date landscape of current agent memory research. We begin by clearly delineating the scope of agent memory and distinguishing it from related concepts such as LLM memory, retrieval augmented generation (RAG), and context engineering. We then examine agent memory through the unified lenses of forms, functions, and dynamics. From the perspective of forms, we identify three dominant realizations of agent memory, namely token-level, parametric, and latent memory. From the perspective of functions, we propose a finer-grained taxonomy that distinguishes factual, experiential, and working memory. From the perspective of dynamics, we analyze how memory is formed, evolved, and retrieved over time. To support practical development, we compile a comprehensive summary of memory benchmarks and open-source frameworks. Beyond consolidation, we articulate a forward-looking perspective on emerging research frontiers, including memory automation, reinforcement learning integration, multimodal memory, multi-agent memory, and trustworthiness issues. We hope this survey serves not only as a reference for existing work, but also as a conceptual foundation for rethinking memory as a first-class primitive in the design of future agentic intelligence.

---

### 17. Language Models as Agent Models

**Authors:** Jacob Andreas  
**Year:** 2022 | **Citations:** 194 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [Dec 2022]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/4596139b28c3ceacbd7e3c34dc0df079dbf4e96b](https://www.semanticscholar.org/paper/4596139b28c3ceacbd7e3c34dc0df079dbf4e96b)  
**arXiv:** [https://arxiv.org/abs/2212.01681](https://arxiv.org/abs/2212.01681)  

**Abstract:** Language models (LMs) are trained on collections of documents, written by individual human agents to achieve specific goals in an outside world. During training, LMs have access only to text of these documents, with no direct evidence of the internal states of the agents that produced them -- a fact often used to argue that LMs are incapable of modeling goal-directed aspects of human language production and comprehension. Can LMs trained on text learn anything at all about the relationship between language and use? I argue that LMs are models of intentional communication in a specific, narrow sense. When performing next word prediction given a textual context, an LM can infer and represent properties of an agent likely to have produced that context. These representations can in turn influence subsequent LM generation in the same way that agents' communicative intentions influence their language. I survey findings from the recent literature showing that -- even in today's non-robust and error-prone models -- LMs infer and use representations of fine-grained communicative intentions and more abstract beliefs and goals. Despite the limited nature of their training data, they can thus serve as building blocks for systems that communicate and act intentionally.

---

### 18. TPTU: Task Planning and Tool Usage of Large Language Model-based AI Agents

**Authors:** Jingqing Ruan, Yihong Chen, Bin Zhang, et al.  
**Year:** 2023 | **Citations:** 192 | **Venue:** arXiv.org  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5ce94181ea702f69c3651dce721d6bd8026b8106](https://www.semanticscholar.org/paper/5ce94181ea702f69c3651dce721d6bd8026b8106)  
---

### 19. SWE-smith: Scaling Data for Software Engineering Agents

**Authors:** John Yang, Kilian Adriano Lieret, Carlos E. Jimenez, et al.  
**Year:** 2025 | **Citations:** 177 | **Venue:** arXiv.org  
**Year Month:** [Apr 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/cbdfe7c75676b6ba85f66bdffe162f5991d6f536](https://www.semanticscholar.org/paper/cbdfe7c75676b6ba85f66bdffe162f5991d6f536)  
**arXiv:** [https://arxiv.org/abs/2504.21798](https://arxiv.org/abs/2504.21798)  

**Abstract:** Despite recent progress in Language Models (LMs) for software engineering, collecting training data remains a significant pain point. Existing datasets are small, with at most 1,000s of training instances from 11 or fewer GitHub repositories. The procedures to curate such datasets are often complex, necessitating hundreds of hours of human labor; companion execution environments also take up several terabytes of storage, severely limiting their scalability and usability. To address this pain point, we introduce SWE-smith, a novel pipeline for generating software engineering training data at scale. Given any Python codebase, SWE-smith constructs a corresponding execution environment, then automatically synthesizes 100s to 1,000s of task instances that break existing test(s) in the codebase. Using SWE-smith, we create a dataset of 50k instances sourced from 128 GitHub repositories, an order of magnitude larger than all previous works. We train SWE-agent-LM-32B, achieving 40.2% Pass@1 resolve rate on the SWE-bench Verified benchmark, state of the art among open source models. We open source SWE-smith (collection procedure, task instances, trajectories, models) to lower the barrier of entry for research in LM systems for automated software engineering. All assets available at https://swesmith.com.

---

### 20. From LLM Reasoning to Autonomous AI Agents: A Comprehensive Review

**Authors:** M. Ferrag, N. Tihanyi, M. Debbah  
**Year:** 2025 | **Citations:** 175 | **Venue:** IEEE Access  
**Year Month:** [Apr 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/6758a6db1bfb6ebc5134aea9ce0fc28dd2e031a4](https://www.semanticscholar.org/paper/6758a6db1bfb6ebc5134aea9ce0fc28dd2e031a4)  
**arXiv:** [https://arxiv.org/abs/2504.19678](https://arxiv.org/abs/2504.19678)  

**Abstract:** Large language models and autonomous AI agents have evolved rapidly, resulting in a diverse array of evaluation benchmarks, frameworks, and collaboration protocols. Driven by the growing need for standardized evaluation and integration, we systematically consolidate these fragmented efforts into a unified framework. However, the landscape remains fragmented and lacks a unified taxonomy or comprehensive survey. Therefore, we present a side-by-side comparison of benchmarks developed between 2019 and 2025 that evaluate these models and agents across multiple domains. In addition, we propose a taxonomy of approximately 60 benchmarks that cover general and academic knowledge reasoning, mathematical problem-solving, code generation and software engineering, factual grounding and retrieval, domain-specific evaluations, multimodal and embodied tasks, task orchestration, and interactive assessments. Furthermore, we review AI-agent frameworks introduced between 2023 and 2025 that integrate large language models with modular toolkits to enable autonomous decision-making and multi-step reasoning. Moreover, we present real-world applications of autonomous AI agents in materials science, biomedical research, academic ideation, software engineering, synthetic data generation, chemical reasoning, mathematical problem-solving, geographic information systems, multimedia, healthcare, and finance. We then survey key agent-to-agent collaboration protocols, namely the Agent Communication Protocol (ACP), the Model Context Protocol (MCP), and the Agent-to-Agent Protocol (A2A). Finally, we discuss recommendations for future research, focusing on advanced reasoning strategies, failure modes in multi-agent LLM systems, automated scientific discovery, dynamic tool integration via reinforcement learning, integrated search capabilities, and security vulnerabilities in agent protocols.

---

### 21. AI Agents as Team Members: Effects on Satisfaction, Conflict, Trustworthiness, and Willingness to Work With

**Authors:** A. Dennis, Akshat Lakhiwal, Agrim Sachdeva  
**Year:** 2023 | **Citations:** 167 | **Venue:** Journal of Management Information Systems  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/d783617b40a8113719671e106c476cee0feef3e8](https://www.semanticscholar.org/paper/d783617b40a8113719671e106c476cee0feef3e8)  

**Abstract:** ABSTRACT Organizations are beginning to deploy artificial intelligence (AI) agents as members of virtual teams to help manage information, coordinate team processes, and perform simple tasks. How will team members perceive these AI team members and will they be willing to work with them? We conducted a 2 x  2 x 2 lab experiment that manipulated the type of team member (human or AI), their performance (high or low), and the performance of other team members (high or low). AI team members were perceived to have higher ability and integrity but lower benevolence, which led to no differences in trustworthiness or willingness to work with them. However, the presence of an AI team member resulted in lower process satisfaction. When the AI team member performed well, participants perceived less conflict compared to a human team member with the same performance, but there were no differences in perceived conflict when it performed poorly. There were no other interactions with performance, indicating that the AI team member was judged similarly to humans, irrespective of variations in performance; there was no evidence of algorithm aversion. Our research suggests that AI team members are likely to be accepted into teams, meaning that many old collaboration research questions may need to be reexamined to consider AI team members.

---

### 22. PrivacyLens: Evaluating Privacy Norm Awareness of Language Models in Action

**Authors:** Yijia Shao, Tianshi Li, Weiyan Shi, et al.  
**Year:** 2024 | **Citations:** 157 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Sep 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/6c95608b50d360fc9b2043d5caf89ce804ed5696](https://www.semanticscholar.org/paper/6c95608b50d360fc9b2043d5caf89ce804ed5696)  
**arXiv:** [https://arxiv.org/abs/2409.00138](https://arxiv.org/abs/2409.00138)  

**Abstract:** As language models (LMs) are widely utilized in personalized communication scenarios (e.g., sending emails, writing social media posts) and endowed with a certain level of agency, ensuring they act in accordance with the contextual privacy norms becomes increasingly critical. However, quantifying the privacy norm awareness of LMs and the emerging privacy risk in LM-mediated communication is challenging due to (1) the contextual and long-tailed nature of privacy-sensitive cases, and (2) the lack of evaluation approaches that capture realistic application scenarios. To address these challenges, we propose PrivacyLens, a novel framework designed to extend privacy-sensitive seeds into expressive vignettes and further into agent trajectories, enabling multi-level evaluation of privacy leakage in LM agents' actions. We instantiate PrivacyLens with a collection of privacy norms grounded in privacy literature and crowdsourced seeds. Using this dataset, we reveal a discrepancy between LM performance in answering probing questions and their actual behavior when executing user instructions in an agent setup. State-of-the-art LMs, like GPT-4 and Llama-3-70B, leak sensitive information in 25.68% and 38.69% of cases, even when prompted with privacy-enhancing instructions. We also demonstrate the dynamic nature of PrivacyLens by extending each seed into multiple trajectories to red-team LM privacy leakage risk. Dataset and code are available at https://github.com/SALT-NLP/PrivacyLens.

---

### 23. Magma: A Foundation Model for Multimodal AI Agents

**Authors:** Jianwei Yang, Reuben Tan, Qianhui Wu, et al.  
**Year:** 2025 | **Citations:** 152 | **Venue:** Computer Vision and Pattern Recognition  
**Year Month:** [Feb 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/512b311213c905087ab439b5c303db2e382a7518](https://www.semanticscholar.org/paper/512b311213c905087ab439b5c303db2e382a7518)  
**arXiv:** [https://arxiv.org/abs/2502.13130](https://arxiv.org/abs/2502.13130)  

**Abstract:** We present Magma, a foundation model that serves multimodal AI agentic tasks in both the digital and physical worlds. Magma is a significant extension of vision-language (VL) models in that it not only retains the VL understanding ability (verbal intelligence) of the latter, but is also equipped with the ability to ground and act in the visual-spatial world (spatial-temporal intelligence). To endow agentic capabilities for tasks ranging from UI navigation to robot manipulation, Magma is trained on large amounts of heterogeneous datasets that span from images, videos to robotics data, where actionable visual objects (e.g. clickable buttons in GUI) in images are labeled by Set-of-Mark (SoM) for action grounding, and object movements (e.g. trace of human hands or robotic arms) in videos are labeled by Trace-of-Mark (ToM) for action planning. Extensive experiments show that SoM and ToM help bridge the gap between verbal and action abilities and significantly enhance spatio-temporal intelligence which is fundamental to agentic tasks, as shown in Fig. 1. In particular, Magma creates new state-of-the-art results on UI navigation and robotic manipulation tasks, outperforming previous models that are specifically tailored to these tasks. Moreover, Magma preserves strong multimodal understanding ability and compares favorably to popular large multimodal models that are trained on much larger datasets. We have made our model and code public for reproducibility1.

---

### 24. AI Agents That Matter

**Authors:** Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, et al.  
**Year:** 2024 | **Citations:** 151 | **Venue:** Trans. Mach. Learn. Res.  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/edae954314571eb2913209a7e9825cdc14fd4c58](https://www.semanticscholar.org/paper/edae954314571eb2913209a7e9825cdc14fd4c58)  
**arXiv:** [https://arxiv.org/abs/2407.01502](https://arxiv.org/abs/2407.01502)  

**Abstract:** AI agents are an exciting new research direction, and agent development is driven by benchmarks. Our analysis of current agent benchmarks and evaluation practices reveals several shortcomings that hinder their usefulness in real-world applications. First, there is a narrow focus on accuracy without attention to other metrics. As a result, SOTA agents are needlessly complex and costly, and the community has reached mistaken conclusions about the sources of accuracy gains. Our focus on cost in addition to accuracy motivates the new goal of jointly optimizing the two metrics. We design and implement one such optimization, showing its potential to greatly reduce cost while maintaining accuracy. Second, the benchmarking needs of model and downstream developers have been conflated, making it hard to identify which agent would be best suited for a particular application. Third, many agent benchmarks have inadequate holdout sets, and sometimes none at all. This has led to agents that are fragile because they take shortcuts and overfit to the benchmark in various ways. We prescribe a principled framework for avoiding overfitting. Finally, there is a lack of standardization in evaluation practices, leading to a pervasive lack of reproducibility. We hope that the steps we introduce for addressing these shortcomings will spur the development of agents that are useful in the real world and not just accurate on benchmarks.

---

### 25. Tree Search for Language Model Agents

**Authors:** Jing Yu Koh, S. McAleer, Daniel Fried, et al.  
**Year:** 2024 | **Citations:** 147 | **Venue:** Trans. Mach. Learn. Res.  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/9345e55a21959948499cee997522aa5eac7ed588](https://www.semanticscholar.org/paper/9345e55a21959948499cee997522aa5eac7ed588)  
**arXiv:** [https://arxiv.org/abs/2407.01476](https://arxiv.org/abs/2407.01476)  

**Abstract:** Autonomous agents powered by language models (LMs) have demonstrated promise in their ability to perform decision-making tasks such as web automation. However, a key limitation remains: LMs, primarily optimized for natural language understanding and generation, struggle with multi-step reasoning, planning, and using environmental feedback when attempting to solve realistic computer tasks. Towards addressing this, we propose an inference-time search algorithm for LM agents to explicitly perform exploration and multi-step planning in interactive web environments. Our approach is a form of best-first tree search that operates within the actual environment space, and is complementary with most existing state-of-the-art agents. It is the first tree search algorithm for LM agents that shows effectiveness on realistic web tasks. On the challenging VisualWebArena benchmark, applying our search algorithm on top of a GPT-4o agent yields a 39.7% relative increase in success rate compared to the same baseline without search, setting a state-of-the-art success rate of 26.4%. On WebArena, search also yields a 28.0% relative improvement over a baseline agent, setting a competitive success rate of 19.2%. Our experiments highlight the effectiveness of search for web agents, and we demonstrate that performance scales with increased test-time compute. We conduct a thorough analysis of our results to highlight improvements from search, limitations, and promising directions for future work. Our code and models are publicly released at https://jykoh.com/search-agents.

---

### 26. AI Agents and Agentic Systems: A Multi-Expert Analysis

**Authors:** Laurie Hughes, Yogesh K. Dwivedi, Tegwen Malik, et al.  
**Year:** 2025 | **Citations:** 143 | **Venue:** Journal of Computational Information Systems  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/46ddc757d49a5cacb0b50f6716a953c0bbea41f9](https://www.semanticscholar.org/paper/46ddc757d49a5cacb0b50f6716a953c0bbea41f9)  

**Abstract:** ABSTRACT The emergence of AI agents and agentic systems represents a significant milestone in artificial intelligence, enabling autonomous systems to operate, learn, and collaborate in complex environments with minimal human intervention. This paper, drawing on multi-expert perspectives, examines the potential of AI agents and agentic systems to reshape industries by decentralizing decision-making, redefining organizational structures, and enhancing cross-functional collaboration. Specific applications include healthcare systems capable of creating adaptive treatment plans, supply chain agents that predict and address disruptions in real-time, and business process automation that reallocates tasks from humans to AI, improving efficiency and innovation. However, the integration of these systems raises critical challenges, including issues of attribution and shared accountability in decision-making, compatibility with legacy systems, and addressing biases in AI-driven processes. The paper concludes that while agentic systems hold immense promise, robust governance frameworks, cross-industry collaboration, and interdisciplinary research into ethical design are essential. Future research should explore adaptive workforce reskilling strategies, transparent accountability mechanisms, and energy-efficient deployment models to ensure ethical and scalable implementation.

---

### 27. Cybench: A Framework for Evaluating Cybersecurity Capabilities and Risks of Language Models

**Authors:** Andy K. Zhang, Neil Perry, Riya Dulepet, et al.  
**Year:** 2024 | **Citations:** 130 | **Venue:**   
**Year Month:** [Aug 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/cb4b0bba67466c22bbc99bbf973dce5e1d9a48b6](https://www.semanticscholar.org/paper/cb4b0bba67466c22bbc99bbf973dce5e1d9a48b6)  
**arXiv:** [https://arxiv.org/abs/2408.08926](https://arxiv.org/abs/2408.08926)  

**Abstract:** Language Model (LM) agents for cybersecurity that are capable of autonomously identifying vulnerabilities and executing exploits have potential to cause real-world impact. Policymakers, model providers, and researchers in the AI and cybersecurity communities are interested in quantifying the capabilities of such agents to help mitigate cyberrisk and investigate opportunities for penetration testing. Toward that end, we introduce Cybench, a framework for specifying cybersecurity tasks and evaluating agents on those tasks. We include 40 professional-level Capture the Flag (CTF) tasks from 4 distinct CTF competitions, chosen to be recent, meaningful, and spanning a wide range of difficulties. Each task includes its own description, starter files, and is initialized in an environment where an agent can execute commands and observe outputs. Since many tasks are beyond the capabilities of existing LM agents, we introduce subtasks for each task, which break down a task into intermediary steps for a more detailed evaluation. To evaluate agent capabilities, we construct a cybersecurity agent and evaluate 8 models: GPT-4o, OpenAI o1-preview, Claude 3 Opus, Claude 3.5 Sonnet, Mixtral 8x22b Instruct, Gemini 1.5 Pro, Llama 3 70B Chat, and Llama 3.1 405B Instruct. For the top performing models (GPT-4o and Claude 3.5 Sonnet), we further investigate performance across 4 agent scaffolds (structed bash, action-only, pseudoterminal, and web search). Without subtask guidance, agents leveraging Claude 3.5 Sonnet, GPT-4o, OpenAI o1-preview, and Claude 3 Opus successfully solved complete tasks that took human teams up to 11 minutes to solve. In comparison, the most difficult task took human teams 24 hours and 54 minutes to solve. All code and data are publicly available at https://cybench.github.io.

---

### 28. Visibility into AI Agents

**Authors:** Alan Chan, Carson Ezell, Max Kaufmann, et al.  
**Year:** 2024 | **Citations:** 123 | **Venue:** Conference on Fairness, Accountability and Transparency  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/e6170d1936bd0e8bcfa4382b001ef2cf137e7e66](https://www.semanticscholar.org/paper/e6170d1936bd0e8bcfa4382b001ef2cf137e7e66)  
**arXiv:** [https://arxiv.org/abs/2401.13138](https://arxiv.org/abs/2401.13138)  

**Abstract:** Increased delegation of commercial, scientific, governmental, and personal activities to AI agents—systems capable of pursuing complex goals with limited supervision—may exacerbate existing societal risks and introduce new risks. Understanding and mitigating these risks involves critically evaluating existing governance structures, revising and adapting these structures where needed, and ensuring accountability of key stakeholders. Information about where, why, how, and by whom certain AI agents are used, which we refer to as visibility, is critical to these objectives. In this paper, we assess three categories of measures to increase visibility into AI agents: agent identifiers, real-time monitoring, and activity logging. For each, we outline potential implementations that vary in intrusiveness and informativeness. We analyze how the measures apply across a spectrum of centralized through decentralized deployment contexts, accounting for various actors in the supply chain including hardware and software service providers. Finally, we discuss the implications of our measures for privacy and concentration of power. Further work into understanding the measures and mitigating their negative impacts can help to build a foundation for the governance of AI agents.

---

### 29. Dissecting Adversarial Robustness of Multimodal LM Agents

**Authors:** Chen Henry Wu, Jing Yu Koh, Ruslan Salakhutdinov, et al.  
**Year:** 2024 | **Citations:** 114 | **Venue:** International Conference on Learning Representations  
**Year Month:** [Jun 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/4f27fc2ea3d3491deded642a5de247d167a03d15](https://www.semanticscholar.org/paper/4f27fc2ea3d3491deded642a5de247d167a03d15)  
**arXiv:** [https://arxiv.org/abs/2406.12814](https://arxiv.org/abs/2406.12814)  

**Abstract:** As language models (LMs) are used to build autonomous agents in real environments, ensuring their adversarial robustness becomes a critical challenge. Unlike chatbots, agents are compound systems with multiple components taking actions, which existing LMs safety evaluations do not adequately address. To bridge this gap, we manually create 200 targeted adversarial tasks and evaluation scripts in a realistic threat model on top of VisualWebArena, a real environment for web agents. To systematically examine the robustness of agents, we propose the Agent Robustness Evaluation (ARE) framework. ARE views the agent as a graph showing the flow of intermediate outputs between components and decomposes robustness as the flow of adversarial information on the graph. We find that we can successfully break latest agents that use black-box frontier LMs, including those that perform reflection and tree search. With imperceptible perturbations to a single image (less than 5% of total web page pixels), an attacker can hijack these agents to execute targeted adversarial goals with success rates up to 67%. We also use ARE to rigorously evaluate how the robustness changes as new components are added. We find that inference-time compute that typically improves benign performance can open up new vulnerabilities and harm robustness. An attacker can compromise the evaluator used by the reflexion agent and the value function of the tree search agent, which increases the attack success relatively by 15% and 20%. Our data and code for attacks, defenses, and evaluation are at https://github.com/ChenWu98/agent-attack

---

### 30. Understanding Nonlinear Collaboration between Human and AI Agents: A Co-design Framework for Creative Design

**Authors:** Jiayi Zhou, Renzhong Li, Junxiu Tang, et al.  
**Year:** 2024 | **Citations:** 112 | **Venue:** International Conference on Human Factors in Computing Systems  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/feacb3129097876863b3e25f5d750454a58e73b7](https://www.semanticscholar.org/paper/feacb3129097876863b3e25f5d750454a58e73b7)  
**arXiv:** [https://arxiv.org/abs/2401.07312](https://arxiv.org/abs/2401.07312)  

**Abstract:** Creative design is a nonlinear process where designers generate diverse ideas in the pursuit of an open-ended goal and converge towards consensus through iterative remixing. In contrast, AI-powered design tools often employ a linear sequence of incremental and precise instructions to approximate design objectives. Such operations violate customary creative design practices and thus hinder AI agents’ ability to complete creative design tasks. To explore better human-AI co-design tools, we first summarize human designers’ practices through a formative study with 12 design experts. Taking graphic design as a representative scenario, we formulate a nonlinear human-AI co-design framework and develop a proof-of-concept prototype, OptiMuse. We evaluate OptiMuse and validate the nonlinear framework through a comparative study. We notice a subconscious change in people’s attitudes towards AI agents, shifting from perceiving them as mere executors to regarding them as opinionated colleagues. This shift effectively fostered the exploration and reflection processes of individual designers.

---

