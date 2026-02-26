# Popular Papers on RAG & AI Agents (Computer Science)

*Generated: 2026-02-26 19:15:09*
*Filtered for Computer Science papers only*

## RAG (Retrieval-Augmented Generation)

*Retrieved: 2026-02-26 19:15:51*

### 1. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**Authors:** Patrick Lewis, Ethan Perez, Aleksandara Piktus, et al.  
**Year:** 2020 | **Citations:** 11,445 | **Venue:** Neural Information Processing Systems  
**Year Month:** [May 2020]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/659bf9ce7175e1ec266ff54359e2bd76e0b7ff31](https://www.semanticscholar.org/paper/659bf9ce7175e1ec266ff54359e2bd76e0b7ff31)  
**arXiv:** [https://arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)  

**Abstract:** Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue, but have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) -- models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state-of-the-art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.

---

### 2. Retrieval-Augmented Generation for Large Language Models: A Survey

**Authors:** Yunfan Gao, Yun Xiong, Xinyu Gao, et al.  
**Year:** 2023 | **Citations:** 2,887 | **Venue:** arXiv.org  
**Year Month:** [Dec 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/46f9f7b8f88f72e12cbdb21e3311f995eb6e65c5](https://www.semanticscholar.org/paper/46f9f7b8f88f72e12cbdb21e3311f995eb6e65c5)  
**arXiv:** [https://arxiv.org/abs/2312.10997](https://arxiv.org/abs/2312.10997)  

**Abstract:** Large Language Models (LLMs) showcase impressive capabilities but encounter challenges like hallucination, outdated knowledge, and non-transparent, untraceable reasoning processes. Retrieval-Augmented Generation (RAG) has emerged as a promising solution by incorporating knowledge from external databases. This enhances the accuracy and credibility of the generation, particularly for knowledge-intensive tasks, and allows for continuous knowledge updates and integration of domain-specific information. RAG synergistically merges LLMs' intrinsic knowledge with the vast, dynamic repositories of external databases. This comprehensive review paper offers a detailed examination of the progression of RAG paradigms, encompassing the Naive RAG, the Advanced RAG, and the Modular RAG. It meticulously scrutinizes the tripartite foundation of RAG frameworks, which includes the retrieval, the generation and the augmentation techniques. The paper highlights the state-of-the-art technologies embedded in each of these critical components, providing a profound understanding of the advancements in RAG systems. Furthermore, this paper introduces up-to-date evaluation framework and benchmark. At the end, this article delineates the challenges currently faced and points out prospective avenues for research and development.

---

### 3. A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented Large Language Models

**Authors:** Wenqi Fan, Yujuan Ding, Liang-bo Ning, et al.  
**Year:** 2024 | **Citations:** 679 | **Venue:** Knowledge Discovery and Data Mining  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/eb9c4a07a336e8deefe7b399c550d3af0241238e](https://www.semanticscholar.org/paper/eb9c4a07a336e8deefe7b399c550d3af0241238e)  
**arXiv:** [https://arxiv.org/abs/2405.06211](https://arxiv.org/abs/2405.06211)  

**Abstract:** As one of the most advanced techniques in AI, Retrieval-Augmented Generation (RAG) can offer reliable and up-to-date external knowledge, providing huge convenience for numerous tasks. Particularly in the era of AI-Generated Content (AIGC), the powerful capacity of retrieval in providing additional knowledge enables RAG to assist existing generative AI in producing high-quality outputs. Recently, Large Language Models (LLMs) have demonstrated revolutionary abilities in language understanding and generation, while still facing inherent limitations such as hallucinations and out-of-date internal knowledge. Given the powerful abilities of RAG in providing the latest and helpful auxiliary information, Retrieval-Augmented Large Language Models (RA-LLMs) have emerged to harness external and authoritative knowledge bases, rather than solely relying on the model's internal knowledge, to augment the quality of the generated content of LLMs. In this survey, we comprehensively review existing research studies in RA-LLMs, covering three primary technical perspectives: Furthermore, to deliver deeper insights, we discuss current limitations and several promising directions for future research. Updated information about this survey can be found at: https://advanced-recommender-systems.github.io/RAG-Meets-LLMs/

---

### 4. Active Retrieval Augmented Generation

**Authors:** Zhengbao Jiang, Frank F. Xu, Luyu Gao, et al.  
**Year:** 2023 | **Citations:** 522 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [May 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/88884b8806262a4095036041e3567d450dba39f7](https://www.semanticscholar.org/paper/88884b8806262a4095036041e3567d450dba39f7)  
**arXiv:** [https://arxiv.org/abs/2305.06983](https://arxiv.org/abs/2305.06983)  

**Abstract:** Despite the remarkable ability of large language models (LMs) to comprehend and generate language, they have a tendency to hallucinate and create factually inaccurate output. Augmenting LMs by retrieving information from external knowledge resources is one promising solution. Most existing retrieval augmented LMs employ a retrieve-and-generate setup that only retrieves information once based on the input. This is limiting, however, in more general scenarios involving generation of long texts, where continually gathering information throughout generation is essential. In this work, we provide a generalized view of active retrieval augmented generation, methods that actively decide when and what to retrieve across the course of the generation. We propose Forward-Looking Active REtrieval augmented generation (FLARE), a generic method which iteratively uses a prediction of the upcoming sentence to anticipate future content, which is then utilized as a query to retrieve relevant documents to regenerate the sentence if it contains low-confidence tokens. We test FLARE along with baselines comprehensively over 4 long-form knowledge-intensive generation tasks/datasets. FLARE achieves superior or competitive performance on all tasks, demonstrating the effectiveness of our method. Code and datasets are available at https://github.com/jzbjyb/FLARE.

---

### 5. Retrieval-Augmented Generation for AI-Generated Content: A Survey

**Authors:** Penghao Zhao, Hailin Zhang, Qinhan Yu, et al.  
**Year:** 2024 | **Citations:** 497 | **Venue:** Data Science and Engineering  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ab15463babf98fffc6f683fe2026de0725b5e1a9](https://www.semanticscholar.org/paper/ab15463babf98fffc6f683fe2026de0725b5e1a9)  
**arXiv:** [https://arxiv.org/abs/2402.19473](https://arxiv.org/abs/2402.19473)  

**Abstract:** Advancements in model algorithms, the growth of foundational models, and access to high-quality datasets have propelled the evolution of Artificial Intelligence Generated Content (AIGC). Despite its notable successes, AIGC still faces hurdles such as updating knowledge, handling long-tail data, mitigating data leakage, and managing high training and inference costs. Retrieval-Augmented Generation (RAG) has recently emerged as a paradigm to address such challenges. In particular, RAG introduces the information retrieval process, which enhances the generation process by retrieving relevant objects from available data stores, leading to higher accuracy and better robustness. In this paper, we comprehensively review existing efforts that integrate RAG technique into AIGC scenarios. We first classify RAG foundations according to how the retriever augments the generator, distilling the fundamental abstractions of the augmentation methodologies for various retrievers and generators. This unified perspective encompasses all RAG scenarios, illuminating advancements and pivotal technologies that help with potential future progress. We also summarize additional enhancements methods for RAG, facilitating effective engineering and implementation of RAG systems. Then from another view, we survey on practical applications of RAG across different modalities and tasks, offering valuable references for researchers and practitioners. Furthermore, we introduce the benchmarks for RAG, discuss the limitations of current RAG systems, and suggest potential directions for future research. Github: https://github.com/PKU-DAIR/RAG-Survey.

---

### 6. Benchmarking Large Language Models in Retrieval-Augmented Generation

**Authors:** Jiawei Chen, Hongyu Lin, Xianpei Han, et al.  
**Year:** 2023 | **Citations:** 481 | **Venue:** AAAI Conference on Artificial Intelligence  
**Year Month:** [Sep 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/28e2ecb4183ebc0eec504b12dddc677f8aef8745](https://www.semanticscholar.org/paper/28e2ecb4183ebc0eec504b12dddc677f8aef8745)  
**arXiv:** [https://arxiv.org/abs/2309.01431](https://arxiv.org/abs/2309.01431)  

**Abstract:** Retrieval-Augmented Generation (RAG) is a promising approach for mitigating the hallucination of large language models (LLMs). However, existing research lacks rigorous evaluation of the impact of retrieval-augmented generation on different large language models, which make it challenging to identify the potential bottlenecks in the capabilities of RAG for different LLMs. In this paper, we systematically investigate the impact of Retrieval-Augmented Generation on large language models. We analyze the performance of different large language models in 4 fundamental abilities required for RAG, including noise robustness, negative rejection, information integration, and counterfactual robustness. To this end, we establish Retrieval-Augmented Generation Benchmark (RGB), a new corpus for RAG evaluation in both English and Chinese. RGB divides the instances within the benchmark into 4 separate testbeds based on the aforementioned fundamental abilities required to resolve the case. Then we evaluate 6 representative LLMs on RGB to diagnose the challenges of current LLMs when applying RAG. Evaluation reveals that while LLMs exhibit a certain degree of noise robustness, they still struggle significantly in terms of negative rejection, information integration, and dealing with false information. The aforementioned assessment outcomes indicate that there is still a considerable journey ahead to effectively apply RAG to LLMs.

---

### 7. RAGAs: Automated Evaluation of Retrieval Augmented Generation

**Authors:** ES Shahul, J. James, Luis Espinosa Anke, et al.  
**Year:** 2023 | **Citations:** 470 | **Venue:** Conference of the European Chapter of the Association for Computational Linguistics  
**Year Month:** [Sep 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/f5e9e5bbe22f0263be1f1ce88c66978a2b927772](https://www.semanticscholar.org/paper/f5e9e5bbe22f0263be1f1ce88c66978a2b927772)  
**arXiv:** [https://arxiv.org/abs/2309.15217](https://arxiv.org/abs/2309.15217)  

**Abstract:** We introduce RAGAs (Retrieval Augmented Generation Assessment), a framework for reference-free evaluation of Retrieval Augmented Generation (RAG) pipelines. RAGAs is available at [https://github.com/explodinggradients/ragas]. RAG systems are composed of a retrieval and an LLM based generation module. They provide LLMs with knowledge from a reference textual database, enabling them to act as a natural language layer between a user and textual databases, thus reducing the risk of hallucinations. Evaluating RAG architectures is challenging due to several dimensions to consider: the ability of the retrieval system to identify relevant and focused context passages, the ability of the LLM to exploit such passages faithfully, and the quality of the generation itself. With RAGAs, we introduce a suite of metrics that can evaluate these different dimensions without relying on ground truth human annotations. We posit that such a framework can contribute crucially to faster evaluation cycles of RAG architectures, which is especially important given the fast adoption of LLMs.

---

### 8. Benchmarking Retrieval-Augmented Generation for Medicine

**Authors:** Guangzhi Xiong, Qiao Jin, Zhiyong Lu, et al.  
**Year:** 2024 | **Citations:** 404 | **Venue:** Annual Meeting of the Association for Computational Linguistics  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b798cf6af813638fab09a8af6ad0f3df6c241485](https://www.semanticscholar.org/paper/b798cf6af813638fab09a8af6ad0f3df6c241485)  
**arXiv:** [https://arxiv.org/abs/2402.13178](https://arxiv.org/abs/2402.13178)  

**Abstract:** While large language models (LLMs) have achieved state-of-the-art performance on a wide range of medical question answering (QA) tasks, they still face challenges with hallucinations and outdated knowledge. Retrieval-augmented generation (RAG) is a promising solution and has been widely adopted. However, a RAG system can involve multiple flexible components, and there is a lack of best practices regarding the optimal RAG setting for various medical purposes. To systematically evaluate such systems, we propose the Medical Information Retrieval-Augmented Generation Evaluation (MIRAGE), a first-of-its-kind benchmark including 7,663 questions from five medical QA datasets. Using MIRAGE, we conducted large-scale experiments with over 1.8 trillion prompt tokens on 41 combinations of different corpora, retrievers, and backbone LLMs through the MedRAG toolkit introduced in this work. Overall, MedRAG improves the accuracy of six different LLMs by up to 18% over chain-of-thought prompting, elevating the performance of GPT-3.5 and Mixtral to GPT-4-level. Our results show that the combination of various medical corpora and retrievers achieves the best performance. In addition, we discovered a log-linear scaling property and the"lost-in-the-middle"effects in medical RAG. We believe our comprehensive evaluations can serve as practical guidelines for implementing RAG systems for medicine.

---

### 9. Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity

**Authors:** Soyeong Jeong, Jinheon Baek, Sukmin Cho, et al.  
**Year:** 2024 | **Citations:** 369 | **Venue:** North American Chapter of the Association for Computational Linguistics  
**Year Month:** [Mar 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/e5e8c6ac537e0f5b5db14170bc232d6f9e641bbc](https://www.semanticscholar.org/paper/e5e8c6ac537e0f5b5db14170bc232d6f9e641bbc)  
**arXiv:** [https://arxiv.org/abs/2403.14403](https://arxiv.org/abs/2403.14403)  

**Abstract:** Retrieval-Augmented Large Language Models (LLMs), which incorporate the non-parametric knowledge from external knowledge bases into LLMs, have emerged as a promising approach to enhancing response accuracy in several tasks, such as Question-Answering (QA). However, even though there are various approaches dealing with queries of different complexities, they either handle simple queries with unnecessary computational overhead or fail to adequately address complex multi-step queries; yet, not all user requests fall into only one of the simple or complex categories. In this work, we propose a novel adaptive QA framework that can dynamically select the most suitable strategy for (retrieval-augmented) LLMs from the simplest to the most sophisticated ones based on the query complexity. Also, this selection process is operationalized with a classifier, which is a smaller LM trained to predict the complexity level of incoming queries with automatically collected labels, obtained from actual predicted outcomes of models and inherent inductive biases in datasets. This approach offers a balanced strategy, seamlessly adapting between the iterative and single-step retrieval-augmented LLMs, as well as the no-retrieval methods, in response to a range of query complexities. We validate our model on a set of open-domain QA datasets, covering multiple query complexities, and show that ours enhances the overall efficiency and accuracy of QA systems, compared to relevant baselines including the adaptive retrieval approaches. Code is available at: https://github.com/starsuzi/Adaptive-RAG.

---

### 10. RAFT: Adapting Language Model to Domain Specific RAG

**Authors:** Tianjun Zhang, Shishir G. Patil, Naman Jain, et al.  
**Year:** 2024 | **Citations:** 312 | **Venue:** arXiv.org  
**Year Month:** [Mar 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/fdefb6a9b51c742d71740d25a76973116a2e0893](https://www.semanticscholar.org/paper/fdefb6a9b51c742d71740d25a76973116a2e0893)  
**arXiv:** [https://arxiv.org/abs/2403.10131](https://arxiv.org/abs/2403.10131)  

**Abstract:** Pretraining Large Language Models (LLMs) on large corpora of textual data is now a standard paradigm. When using these LLMs for many downstream applications, it is common to additionally bake in new knowledge (e.g., time-critical news, or private domain knowledge) into the pretrained model either through RAG-based-prompting, or fine-tuning. However, the optimal methodology for the model to gain such new knowledge remains an open question. In this paper, we present Retrieval Augmented FineTuning (RAFT), a training recipe that improves the model's ability to answer questions in a"open-book"in-domain settings. In RAFT, given a question, and a set of retrieved documents, we train the model to ignore those documents that don't help in answering the question, which we call, distractor documents. RAFT accomplishes this by citing verbatim the right sequence from the relevant document that would help answer the question. This coupled with RAFT's chain-of-thought-style response helps improve the model's ability to reason. In domain-specific RAG, RAFT consistently improves the model's performance across PubMed, HotpotQA, and Gorilla datasets, presenting a post-training recipe to improve pre-trained LLMs to in-domain RAG. RAFT's code and demo are open-sourced at github.com/ShishirPatil/gorilla.

---

### 11. Graph Retrieval-Augmented Generation: A Survey

**Authors:** Boci Peng, Yun Zhu, Yongchao Liu, et al.  
**Year:** 2024 | **Citations:** 306 | **Venue:** ACM Transactions on Information Systems  
**Year Month:** [Aug 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/9ab45aa875b56335303398e84a59a3756cd9d530](https://www.semanticscholar.org/paper/9ab45aa875b56335303398e84a59a3756cd9d530)  
**arXiv:** [https://arxiv.org/abs/2408.08921](https://arxiv.org/abs/2408.08921)  

**Abstract:** Recently, Retrieval-Augmented Generation (RAG) has achieved remarkable success in addressing the challenges of Large Language Models (LLMs) without necessitating retraining. By referencing an external knowledge base, RAG refines LLM outputs, effectively mitigating issues such as “hallucination,” lack of domain-specific knowledge, and outdated information. However, the complex structure of relationships among different entities in databases presents challenges for RAG systems. In response, GraphRAG leverages structural information across entities to enable more precise and comprehensive retrieval, capturing relational knowledge and facilitating more accurate, context-aware responses. Given the novelty and potential of GraphRAG, a systematic review of current technologies is imperative. This article provides the first comprehensive overview of GraphRAG methodologies. We formalize the GraphRAG workflow, encompassing Graph-Based Indexing, Graph-Guided Retrieval, and Graph-Enhanced Generation. We then outline the core technologies and training methods at each stage. Additionally, we examine downstream tasks, application domains, evaluation methodologies, and industrial use cases of GraphRAG. Finally, we explore future research directions to inspire further inquiries and advance progress in the field. In order to track recent progress, we set up a repository at https://github.com/pengboci/GraphRAG-Survey.

---

### 12. Evaluation of Retrieval-Augmented Generation: A Survey

**Authors:** Hao Yu, Aoran Gan, Kai Zhang, et al.  
**Year:** 2024 | **Citations:** 218 | **Venue:** arXiv.org  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/3c6a6c8de005ef5722a54847747f65922e79d622](https://www.semanticscholar.org/paper/3c6a6c8de005ef5722a54847747f65922e79d622)  
**arXiv:** [https://arxiv.org/abs/2405.07437](https://arxiv.org/abs/2405.07437)  

**Abstract:** Retrieval-Augmented Generation (RAG) has recently gained traction in natural language processing. Numerous studies and real-world applications are leveraging its ability to enhance generative models through external information retrieval. Evaluating these RAG systems, however, poses unique challenges due to their hybrid structure and reliance on dynamic knowledge sources. To better understand these challenges, we conduct A Unified Evaluation Process of RAG (Auepora) and aim to provide a comprehensive overview of the evaluation and benchmarks of RAG systems. Specifically, we examine and compare several quantifiable metrics of the Retrieval and Generation components, such as relevance, accuracy, and faithfulness, within the current RAG benchmarks, encompassing the possible output and ground truth pairs. We then analyze the various datasets and metrics, discuss the limitations of current benchmarks, and suggest potential directions to advance the field of RAG benchmarks.

---

### 13. RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models

**Authors:** Yuanhao Wu, Juno Zhu, Siliang Xu, et al.  
**Year:** 2023 | **Citations:** 209 | **Venue:** Annual Meeting of the Association for Computational Linguistics  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/cfce709a65f90312d2bdc1a6cf0380c19becf694](https://www.semanticscholar.org/paper/cfce709a65f90312d2bdc1a6cf0380c19becf694)  
**arXiv:** [https://arxiv.org/abs/2401.00396](https://arxiv.org/abs/2401.00396)  

**Abstract:** Retrieval-augmented generation (RAG) has become a main technique for alleviating hallucinations in large language models (LLMs). Despite the integration of RAG, LLMs may still present unsupported or contradictory claims to the retrieved contents. In order to develop effective hallucination prevention strategies under RAG, it is important to create benchmark datasets that can measure the extent of hallucination. This paper presents RAGTruth, a corpus tailored for analyzing word-level hallucinations in various domains and tasks within the standard RAG frameworks for LLM applications. RAGTruth comprises nearly 18,000 naturally generated responses from diverse LLMs using RAG. These responses have undergone meticulous manual annotations at both the individual cases and word levels, incorporating evaluations of hallucination intensity. We not only benchmark hallucination frequencies across different LLMs, but also critically assess the effectiveness of several existing hallucination detection methodologies. Furthermore, we show that using a high-quality dataset such as RAGTruth, it is possible to finetune a relatively small LLM and achieve a competitive level of performance in hallucination detection when compared to the existing prompt-based approaches using state-of-the-art large language models such as GPT-4.

---

### 14. MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries

**Authors:** Yixuan Tang, Yi Yang  
**Year:** 2024 | **Citations:** 206 | **Venue:** arXiv.org  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/4e71624e90960cb003e311a0fe3b8be4c2863239](https://www.semanticscholar.org/paper/4e71624e90960cb003e311a0fe3b8be4c2863239)  
**arXiv:** [https://arxiv.org/abs/2401.15391](https://arxiv.org/abs/2401.15391)  

**Abstract:** Retrieval-augmented generation (RAG) augments large language models (LLM) by retrieving relevant knowledge, showing promising potential in mitigating LLM hallucinations and enhancing response quality, thereby facilitating the great adoption of LLMs in practice. However, we find that existing RAG systems are inadequate in answering multi-hop queries, which require retrieving and reasoning over multiple pieces of supporting evidence. Furthermore, to our knowledge, no existing RAG benchmarking dataset focuses on multi-hop queries. In this paper, we develop a novel dataset, MultiHop-RAG, which consists of a knowledge base, a large collection of multi-hop queries, their ground-truth answers, and the associated supporting evidence. We detail the procedure of building the dataset, utilizing an English news article dataset as the underlying RAG knowledge base. We demonstrate the benchmarking utility of MultiHop-RAG in two experiments. The first experiment compares different embedding models for retrieving evidence for multi-hop queries. In the second experiment, we examine the capabilities of various state-of-the-art LLMs, including GPT-4, PaLM, and Llama2-70B, in reasoning and answering multi-hop queries given the evidence. Both experiments reveal that existing RAG methods perform unsatisfactorily in retrieving and answering multi-hop queries. We hope MultiHop-RAG will be a valuable resource for the community in developing effective RAG systems, thereby facilitating greater adoption of LLMs in practice. The MultiHop-RAG and implemented RAG system is publicly available at https://github.com/yixuantt/MultiHop-RAG/.

---

### 15. Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG

**Authors:** Aditi Singh, Abul Ehtesham, Saket Kumar, et al.  
**Year:** 2025 | **Citations:** 202 | **Venue:** arXiv.org  
**Year Month:** [Jan 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/f1d6bb6b8f0273986094b5e166538a980c674fea](https://www.semanticscholar.org/paper/f1d6bb6b8f0273986094b5e166538a980c674fea)  
**arXiv:** [https://arxiv.org/abs/2501.09136](https://arxiv.org/abs/2501.09136)  

**Abstract:** Large Language Models (LLMs) have revolutionized artificial intelligence (AI) by enabling human like text generation and natural language understanding. However, their reliance on static training data limits their ability to respond to dynamic, real time queries, resulting in outdated or inaccurate outputs. Retrieval Augmented Generation (RAG) has emerged as a solution, enhancing LLMs by integrating real time data retrieval to provide contextually relevant and up-to-date responses. Despite its promise, traditional RAG systems are constrained by static workflows and lack the adaptability required for multistep reasoning and complex task management. Agentic Retrieval-Augmented Generation (Agentic RAG) transcends these limitations by embedding autonomous AI agents into the RAG pipeline. These agents leverage agentic design patterns reflection, planning, tool use, and multiagent collaboration to dynamically manage retrieval strategies, iteratively refine contextual understanding, and adapt workflows to meet complex task requirements. This integration enables Agentic RAG systems to deliver unparalleled flexibility, scalability, and context awareness across diverse applications. This survey provides a comprehensive exploration of Agentic RAG, beginning with its foundational principles and the evolution of RAG paradigms. It presents a detailed taxonomy of Agentic RAG architectures, highlights key applications in industries such as healthcare, finance, and education, and examines practical implementation strategies. Additionally, it addresses challenges in scaling these systems, ensuring ethical decision making, and optimizing performance for real-world applications, while providing detailed insights into frameworks and tools for implementing Agentic RAG.

---

### 16. G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering

**Authors:** Xiaoxin He, Yijun Tian, Yifei Sun, et al.  
**Year:** 2024 | **Citations:** 202 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/a41d4a3b005c8ec4f821e6ee96672d930ca9596c](https://www.semanticscholar.org/paper/a41d4a3b005c8ec4f821e6ee96672d930ca9596c)  
**arXiv:** [https://arxiv.org/abs/2402.07630](https://arxiv.org/abs/2402.07630)  

**Abstract:** Given a graph with textual attributes, we enable users to `chat with their graph': that is, to ask questions about the graph using a conversational interface. In response to a user's questions, our method provides textual replies and highlights the relevant parts of the graph. While existing works integrate large language models (LLMs) and graph neural networks (GNNs) in various ways, they mostly focus on either conventional graph tasks (such as node, edge, and graph classification), or on answering simple graph queries on small or synthetic graphs. In contrast, we develop a flexible question-answering framework targeting real-world textual graphs, applicable to multiple applications including scene graph understanding, common sense reasoning, and knowledge graph reasoning. Toward this goal, we first develop a Graph Question Answering (GraphQA) benchmark with data collected from different tasks. Then, we propose our G-Retriever method, introducing the first retrieval-augmented generation (RAG) approach for general textual graphs, which can be fine-tuned to enhance graph understanding via soft prompting. To resist hallucination and to allow for textual graphs that greatly exceed the LLM's context window size, G-Retriever performs RAG over a graph by formulating this task as a Prize-Collecting Steiner Tree optimization problem. Empirical evaluations show that our method outperforms baselines on textual graph tasks from multiple domains, scales well with larger graph sizes, and mitigates hallucination.~\footnote{Our codes and datasets are available at: \url{https://github.com/XiaoxinHe/G-Retriever}}

---

### 17. RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs

**Authors:** Yue Yu, Wei Ping, Zihan Liu, et al.  
**Year:** 2024 | **Citations:** 196 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/80478de9c7a81561e2f3dac9b8b1ef3df389ff2d](https://www.semanticscholar.org/paper/80478de9c7a81561e2f3dac9b8b1ef3df389ff2d)  
**arXiv:** [https://arxiv.org/abs/2407.02485](https://arxiv.org/abs/2407.02485)  

**Abstract:** Large language models (LLMs) typically utilize the top-k contexts from a retriever in retrieval-augmented generation (RAG). In this work, we propose a novel instruction fine-tuning framework RankRAG, which instruction-tunes a single LLM for the dual purpose of context ranking and answer generation in RAG. In particular, the instruction-tuned LLMs work surprisingly well by adding a small fraction of ranking data into the training blend, and outperform existing expert ranking models, including the same LLM exclusively fine-tuned on a large amount of ranking data. For generation, we compare our model with many strong baselines, including GPT-4-0613, GPT-4-turbo-2024-0409, and ChatQA-1.5, an open-sourced model with the state-of-the-art performance on RAG benchmarks. Specifically, our Llama3-RankRAG significantly outperforms Llama3-ChatQA-1.5 and GPT-4 models on nine knowledge-intensive benchmarks. In addition, it also performs comparably to GPT-4 on five RAG benchmarks in the biomedical domain without instruction fine-tuning on biomedical data, demonstrating its superb capability for generalization to new domains.

---

### 18. LightRAG: Simple and Fast Retrieval-Augmented Generation

**Authors:** Zirui Guo, Lianghao Xia, Yanhua Yu, et al.  
**Year:** 2024 | **Citations:** 192 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [Oct 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1ea143c34b9bc359780f79ba4d68dee68bcc1129](https://www.semanticscholar.org/paper/1ea143c34b9bc359780f79ba4d68dee68bcc1129)  
**arXiv:** [https://arxiv.org/abs/2410.05779](https://arxiv.org/abs/2410.05779)  

**Abstract:** Retrieval-Augmented Generation (RAG) systems enhance large language models (LLMs) by integrating external knowledge sources, enabling more accurate and contextually relevant responses tailored to user needs. However, existing RAG systems have significant limitations, including reliance on flat data representations and inadequate contextual awareness, which can lead to fragmented answers that fail to capture complex inter-dependencies. To address these challenges, we propose LightRAG, which incorporates graph structures into text indexing and retrieval processes. This innovative framework employs a dual-level retrieval system that enhances comprehensive information retrieval from both low-level and high-level knowledge discovery. Additionally, the integration of graph structures with vector representations facilitates efficient retrieval of related entities and their relationships, significantly improving response times while maintaining contextual relevance. This capability is further enhanced by an incremental update algorithm that ensures the timely integration of new data, allowing the system to remain effective and responsive in rapidly changing data environments. Extensive experimental validation demonstrates considerable improvements in retrieval accuracy and efficiency compared to existing approaches. We have made our LightRAG open-source and available at the link: https://github.com/HKUDS/LightRAG

---

### 19. Seven Failure Points When Engineering a Retrieval Augmented Generation System

**Authors:** Scott Barnett, Stefanus Kurniawan, Srikanth Thudumu, et al.  
**Year:** 2024 | **Citations:** 186 | **Venue:** 2024 IEEE/ACM 3rd International Conference on AI Engineering – Software Engineering for AI (CAIN)  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ba454ba8c594dfb86c25dff2e265c8a2686aa037](https://www.semanticscholar.org/paper/ba454ba8c594dfb86c25dff2e265c8a2686aa037)  
**arXiv:** [https://arxiv.org/abs/2401.05856](https://arxiv.org/abs/2401.05856)  

**Abstract:** Software engineers are increasingly adding semantic search capabilities to applications using a strategy known as Retrieval Augmented Generation (RAG). A RAG system involves finding documents that semantically match a query and then passing the documents to a large language model (LLM) such as ChatGPT to extract the right answer using an LLM. RAG systems aim to: a) reduce the problem of hallucinated responses from LLMs, b) link sources/references to generated responses, and c) remove the need for annotating documents with meta-data. However, RAG systems suffer from limitations inherent to information retrieval systems and from reliance on LLMs. In this paper, we present an experience report on the failure points of RAG systems from three case studies from separate domains: research, education, and biomedical. We share the lessons learned and present 7 failure points to consider when designing a RAG system. The two key takeaways arising from our work are: 1) validation of a RAG system is only feasible during operation, and 2) the robustness of a RAG system evolves rather than designed in at the start. We conclude with a list of potential research directions on RAG systems for the software engineering community.CCS CONCEPTS• Software and its engineering → Empirical software validation.

---

### 20. Retrieval-Augmented Generation with Knowledge Graphs for Customer Service Question Answering

**Authors:** Zhentao Xu, Mark Jerome Cruz, M. Guevara, et al.  
**Year:** 2024 | **Citations:** 183 | **Venue:** Annual International ACM SIGIR Conference on Research and Development in Information Retrieval  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b708e0f49d8e9708bc649debd9a9372748fffa3d](https://www.semanticscholar.org/paper/b708e0f49d8e9708bc649debd9a9372748fffa3d)  
**arXiv:** [https://arxiv.org/abs/2404.17723](https://arxiv.org/abs/2404.17723)  

**Abstract:** In customer service technical support, swiftly and accurately retrieving relevant past issues is critical for efficiently resolving customer inquiries. The conventional retrieval methods in retrieval-augmented generation (RAG) for large language models (LLMs) treat a large corpus of past issue tracking tickets as plain text, ignoring the crucial intra-issue structure and inter-issue relations, which limits performance. We introduce a novel customer service question-answering method that amalgamates RAG with a knowledge graph (KG). Our method constructs a KG from historical issues for use in retrieval, retaining the intra-issue structure and inter-issue relations. During the question-answering phase, our method parses consumer queries and retrieves related sub-graphs from the KG to generate answers. This integration of a KG not only improves retrieval accuracy by preserving customer service structure information but also enhances answering quality by mitigating the effects of text segmentation. Empirical assessments on our benchmark datasets, utilizing key retrieval (MRR, Recall@K, NDCG@K) and text generation (BLEU, ROUGE, METEOR) metrics, reveal that our method outperforms the baseline by 77.6% in MRR and by 0.32 in BLEU. Our method has been deployed within LinkedIn's customer service team for approximately six months and has reduced the median per-issue resolution time by 28.6%.

---

### 21. Chain of Agents: Large Language Models Collaborating on Long-Context Tasks

**Authors:** Yusen Zhang, Ruoxi Sun, Yanfei Chen, et al.  
**Year:** 2024 | **Citations:** 180 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Jun 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1b0fa09f097591d697162300cc6ecb3ee425fd8d](https://www.semanticscholar.org/paper/1b0fa09f097591d697162300cc6ecb3ee425fd8d)  
**arXiv:** [https://arxiv.org/abs/2406.02818](https://arxiv.org/abs/2406.02818)  

**Abstract:** Addressing the challenge of effectively processing long contexts has become a critical issue for Large Language Models (LLMs). Two common strategies have emerged: 1) reducing the input length, such as retrieving relevant chunks by Retrieval-Augmented Generation (RAG), and 2) expanding the context window limit of LLMs. However, both strategies have drawbacks: input reduction has no guarantee of covering the part with needed information, while window extension struggles with focusing on the pertinent information for solving the task. To mitigate these limitations, we propose Chain-of-Agents (CoA), a novel framework that harnesses multi-agent collaboration through natural language to enable information aggregation and context reasoning across various LLMs over long-context tasks. CoA consists of multiple worker agents who sequentially communicate to handle different segmented portions of the text, followed by a manager agent who synthesizes these contributions into a coherent final output. CoA processes the entire input by interleaving reading and reasoning, and it mitigates long context focus issues by assigning each agent a short context. We perform comprehensive evaluation of CoA on a wide range of long-context tasks in question answering, summarization, and code completion, demonstrating significant improvements by up to 10% over strong baselines of RAG, Full-Context, and multi-agent LLMs.

---

### 22. The Good and The Bad: Exploring Privacy Issues in Retrieval-Augmented Generation (RAG)

**Authors:** Shenglai Zeng, Jiankun Zhang, Pengfei He, et al.  
**Year:** 2024 | **Citations:** 158 | **Venue:** Annual Meeting of the Association for Computational Linguistics  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ea89b058ce619ed16d4de633126b02a8179457c8](https://www.semanticscholar.org/paper/ea89b058ce619ed16d4de633126b02a8179457c8)  
**arXiv:** [https://arxiv.org/abs/2402.16893](https://arxiv.org/abs/2402.16893)  

**Abstract:** Retrieval-augmented generation (RAG) is a powerful technique to facilitate language model with proprietary and private data, where data privacy is a pivotal concern. Whereas extensive research has demonstrated the privacy risks of large language models (LLMs), the RAG technique could potentially reshape the inherent behaviors of LLM generation, posing new privacy issues that are currently under-explored. In this work, we conduct extensive empirical studies with novel attack methods, which demonstrate the vulnerability of RAG systems on leaking the private retrieval database. Despite the new risk brought by RAG on the retrieval data, we further reveal that RAG can mitigate the leakage of the LLMs' training data. Overall, we provide new insights in this paper for privacy protection of retrieval-augmented LLMs, which benefit both LLMs and RAG systems builders. Our code is available at https://github.com/phycholosogy/RAG-privacy.

---

### 23. Corrective Retrieval Augmented Generation

**Authors:** Shi-Qi Yan, Jia-Chen Gu, Yun Zhu, et al.  
**Year:** 2024 | **Citations:** 158 | **Venue:** arXiv.org  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5bbc2b5aa6c63c6a2cfccf095d6020b063ad47ac](https://www.semanticscholar.org/paper/5bbc2b5aa6c63c6a2cfccf095d6020b063ad47ac)  
**arXiv:** [https://arxiv.org/abs/2401.15884](https://arxiv.org/abs/2401.15884)  

**Abstract:** Large language models (LLMs) inevitably exhibit hallucinations since the accuracy of generated texts cannot be secured solely by the parametric knowledge they encapsulate. Although retrieval-augmented generation (RAG) is a practicable complement to LLMs, it relies heavily on the relevance of retrieved documents, raising concerns about how the model behaves if retrieval goes wrong. To this end, we propose the Corrective Retrieval Augmented Generation (CRAG) to improve the robustness of generation. Specifically, a lightweight retrieval evaluator is designed to assess the overall quality of retrieved documents for a query, returning a confidence degree based on which different knowledge retrieval actions can be triggered. Since retrieval from static and limited corpora can only return sub-optimal documents, large-scale web searches are utilized as an extension for augmenting the retrieval results. Besides, a decompose-then-recompose algorithm is designed for retrieved documents to selectively focus on key information and filter out irrelevant information in them. CRAG is plug-and-play and can be seamlessly coupled with various RAG-based approaches. Experiments on four datasets covering short- and long-form generation tasks show that CRAG can significantly improve the performance of RAG-based approaches.

---

### 24. FlashRAG: A Modular Toolkit for Efficient Retrieval-Augmented Generation Research

**Authors:** Jiajie Jin, Yutao Zhu, Xinyu Yang, et al.  
**Year:** 2024 | **Citations:** 157 | **Venue:** The Web Conference  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/daebec92963ab8dea492f0c209bdf57e87bcaa07](https://www.semanticscholar.org/paper/daebec92963ab8dea492f0c209bdf57e87bcaa07)  
**arXiv:** [https://arxiv.org/abs/2405.13576](https://arxiv.org/abs/2405.13576)  

**Abstract:** With the advent of large language models (LLMs) and multimodal large language models (MLLMs), the potential of retrieval-augmented generation (RAG) has attracted considerable research attention. However, the absence of a standardized framework for implementation, coupled with the inherently complex RAG process, makes it challenging and time-consuming for researchers to compare and evaluate these approaches in a consistent environment. In response to this challenge, we develop FlashRAG, an efficient and modular open-source toolkit designed to assist researchers in reproducing and comparing existing RAG methods and developing their own algorithms within a unified framework. Our toolkit has implemented 16 advanced RAG methods and gathered and organized 38 benchmark datasets. It has various features, including a customizable modular framework, a rich collection of pre-implemented RAG works, comprehensive datasets, efficient auxiliary pre-processing scripts, and extensive and standard evaluation metrics. Our toolkit and resources are available at https://github.com/RUC-NLPIR/FlashRAG.

---

### 25. RQ-RAG: Learning to Refine Queries for Retrieval Augmented Generation

**Authors:** Chi-Min Chan, Chunpu Xu, Ruibin Yuan, et al.  
**Year:** 2024 | **Citations:** 157 | **Venue:** arXiv.org  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/746b96ee17e329f1085a047116c05e12eaa3925a](https://www.semanticscholar.org/paper/746b96ee17e329f1085a047116c05e12eaa3925a)  
**arXiv:** [https://arxiv.org/abs/2404.00610](https://arxiv.org/abs/2404.00610)  

**Abstract:** Large Language Models (LLMs) exhibit remarkable capabilities but are prone to generating inaccurate or hallucinatory responses. This limitation stems from their reliance on vast pretraining datasets, making them susceptible to errors in unseen scenarios. To tackle these challenges, Retrieval-Augmented Generation (RAG) addresses this by incorporating external, relevant documents into the response generation process, thus leveraging non-parametric knowledge alongside LLMs' in-context learning abilities. However, existing RAG implementations primarily focus on initial input for context retrieval, overlooking the nuances of ambiguous or complex queries that necessitate further clarification or decomposition for accurate responses. To this end, we propose learning to Refine Query for Retrieval Augmented Generation (RQ-RAG) in this paper, endeavoring to enhance the model by equipping it with capabilities for explicit rewriting, decomposition, and disambiguation. Our experimental results indicate that our method, when applied to a 7B Llama2 model, surpasses the previous state-of-the-art (SOTA) by an average of 1.9\% across three single-hop QA datasets, and also demonstrates enhanced performance in handling complex, multi-hop QA datasets. Our code is available at https://github.com/chanchimin/RQ-RAG.

---

### 26. GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning

**Authors:** Costas Mavromatis, G. Karypis  
**Year:** 2024 | **Citations:** 152 | **Venue:** arXiv.org  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/336605fc899aab6c5b375d1129bf656d246b9013](https://www.semanticscholar.org/paper/336605fc899aab6c5b375d1129bf656d246b9013)  
**arXiv:** [https://arxiv.org/abs/2405.20139](https://arxiv.org/abs/2405.20139)  

**Abstract:** Knowledge Graphs (KGs) represent human-crafted factual knowledge in the form of triplets (head, relation, tail), which collectively form a graph. Question Answering over KGs (KGQA) is the task of answering natural questions grounding the reasoning to the information provided by the KG. Large Language Models (LLMs) are the state-of-the-art models for QA tasks due to their remarkable ability to understand natural language. On the other hand, Graph Neural Networks (GNNs) have been widely used for KGQA as they can handle the complex graph information stored in the KG. In this work, we introduce GNN-RAG, a novel method for combining language understanding abilities of LLMs with the reasoning abilities of GNNs in a retrieval-augmented generation (RAG) style. First, a GNN reasons over a dense KG subgraph to retrieve answer candidates for a given question. Second, the shortest paths in the KG that connect question entities and answer candidates are extracted to represent KG reasoning paths. The extracted paths are verbalized and given as input for LLM reasoning with RAG. In our GNN-RAG framework, the GNN acts as a dense subgraph reasoner to extract useful graph information, while the LLM leverages its natural language processing ability for ultimate KGQA. Furthermore, we develop a retrieval augmentation (RA) technique to further boost KGQA performance with GNN-RAG. Experimental results show that GNN-RAG achieves state-of-the-art performance in two widely used KGQA benchmarks (WebQSP and CWQ), outperforming or matching GPT-4 performance with a 7B tuned LLM. In addition, GNN-RAG excels on multi-hop and multi-entity questions outperforming competing approaches by 8.9--15.5% points at answer F1.

---

### 27. Retrieval-Augmented Generation with Graphs (GraphRAG)

**Authors:** Haoyu Han, Yu Wang, Harry Shomer, et al.  
**Year:** 2024 | **Citations:** 151 | **Venue:** arXiv.org  
**Year Month:** [Jan 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/12fb0a058ad69f85a2b59cf7a52a29cbb01d8a0b](https://www.semanticscholar.org/paper/12fb0a058ad69f85a2b59cf7a52a29cbb01d8a0b)  
**arXiv:** [https://arxiv.org/abs/2501.00309](https://arxiv.org/abs/2501.00309)  

**Abstract:** Retrieval-augmented generation (RAG) is a powerful technique that enhances downstream task execution by retrieving additional information, such as knowledge, skills, and tools from external sources. Graph, by its intrinsic"nodes connected by edges"nature, encodes massive heterogeneous and relational information, making it a golden resource for RAG in tremendous real-world applications. As a result, we have recently witnessed increasing attention on equipping RAG with Graph, i.e., GraphRAG. However, unlike conventional RAG, where the retriever, generator, and external data sources can be uniformly designed in the neural-embedding space, the uniqueness of graph-structured data, such as diverse-formatted and domain-specific relational knowledge, poses unique and significant challenges when designing GraphRAG for different domains. Given the broad applicability, the associated design challenges, and the recent surge in GraphRAG, a systematic and up-to-date survey of its key concepts and techniques is urgently desired. Following this motivation, we present a comprehensive and up-to-date survey on GraphRAG. Our survey first proposes a holistic GraphRAG framework by defining its key components, including query processor, retriever, organizer, generator, and data source. Furthermore, recognizing that graphs in different domains exhibit distinct relational patterns and require dedicated designs, we review GraphRAG techniques uniquely tailored to each domain. Finally, we discuss research challenges and brainstorm directions to inspire cross-disciplinary opportunities. Our survey repository is publicly maintained at https://github.com/Graph-RAG/GraphRAG/.

---

### 28. Evaluating Retrieval Quality in Retrieval-Augmented Generation

**Authors:** Alireza Salemi, Hamed Zamani  
**Year:** 2024 | **Citations:** 150 | **Venue:** Annual International ACM SIGIR Conference on Research and Development in Information Retrieval  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/e90435e1ae06fab4efa272f5f46ed74ca0a8cde0](https://www.semanticscholar.org/paper/e90435e1ae06fab4efa272f5f46ed74ca0a8cde0)  
**arXiv:** [https://arxiv.org/abs/2404.13781](https://arxiv.org/abs/2404.13781)  

**Abstract:** Evaluating retrieval-augmented generation (RAG) presents challenges, particularly for retrieval models within these systems. Traditional end-to-end evaluation methods are computationally expensive. Furthermore, evaluation of the retrieval model's performance based on query-document relevance labels shows a small correlation with the RAG system's downstream performance. We propose a novel evaluation approach, eRAG, where each document in the retrieval list is individually utilized by the large language model within the RAG system. The output generated for each document is then evaluated based on the downstream task ground truth labels. In this manner, the downstream performance for each document serves as its relevance label. We employ various downstream task metrics to obtain document-level annotations and aggregate them using set-based or ranking metrics. Extensive experiments on a wide range of datasets demonstrate that eRAG achieves a higher correlation with downstream RAG performance compared to baseline methods, with improvements in Kendall's tau correlation ranging from 0.168 to 0.494. Additionally, eRAG offers significant computational advantages, improving runtime and consuming up to 50 times less GPU memory than end-to-end evaluation.

---

### 29. HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented Generation for Efficient Information Extraction

**Authors:** Bhaskarjit Sarmah, Dhagash Mehta, Benika Hall, et al.  
**Year:** 2024 | **Citations:** 149 | **Venue:** International Conference on AI in Finance  
**Year Month:** [Aug 2024]  
**Fields:** Computer Science, Economics, Mathematics  
**URL:** [https://www.semanticscholar.org/paper/9af8bccf3e42996cbb198a6ceccafa2a084689f6](https://www.semanticscholar.org/paper/9af8bccf3e42996cbb198a6ceccafa2a084689f6)  
**arXiv:** [https://arxiv.org/abs/2408.04948](https://arxiv.org/abs/2408.04948)  

**Abstract:** Extraction and interpretation of intricate information from unstructured text data arising in financial applications, such as earnings call transcripts, present substantial challenges to large language models (LLMs) even using the current best practices to use Retrieval Augmented Generation (RAG) (referred to as VectorRAG techniques which utilize vector databases for information retrieval) due to challenges such as domain specific terminology and complex formats of the documents. We introduce a novel approach based on a combination, called HybridRAG, of the Knowledge Graphs (KGs) based RAG techniques (called GraphRAG) and VectorRAG techniques to enhance question-answer (Q&A) systems for information extraction from financial documents that is shown to be capable of generating accurate and contextually relevant answers. Using experiments on a set of financial earning call transcripts documents which come in the form of Q&A format, and hence provide a natural set of pairs of ground-truth Q&As, we show that HybridRAG which retrieves context from both vector database and KG outperforms both traditional VectorRAG and GraphRAG individually when evaluated at both the retrieval and generation stages in terms of retrieval accuracy and answer generation. The proposed technique has applications beyond the financial domain.

---

### 30. Optimization of hepatological clinical guidelines interpretation by large language models: a retrieval augmented generation-based framework

**Authors:** Simone Kresevic, M. Giuffré, M. Ajčević, et al.  
**Year:** 2024 | **Citations:** 141 | **Venue:** npj Digital Medicine  
**Fields:** Medicine, Computer Science  
**URL:** [https://www.semanticscholar.org/paper/965a0969b460f9246158d88fb28e21c5d80d0a8b](https://www.semanticscholar.org/paper/965a0969b460f9246158d88fb28e21c5d80d0a8b)  

**Abstract:** Large language models (LLMs) can potentially transform healthcare, particularly in providing the right information to the right provider at the right time in the hospital workflow. This study investigates the integration of LLMs into healthcare, specifically focusing on improving clinical decision support systems (CDSSs) through accurate interpretation of medical guidelines for chronic Hepatitis C Virus infection management. Utilizing OpenAI’s GPT-4 Turbo model, we developed a customized LLM framework that incorporates retrieval augmented generation (RAG) and prompt engineering. Our framework involved guideline conversion into the best-structured format that can be efficiently processed by LLMs to provide the most accurate output. An ablation study was conducted to evaluate the impact of different formatting and learning strategies on the LLM’s answer generation accuracy. The baseline GPT-4 Turbo model’s performance was compared against five experimental setups with increasing levels of complexity: inclusion of in-context guidelines, guideline reformatting, and implementation of few-shot learning. Our primary outcome was the qualitative assessment of accuracy based on expert review, while secondary outcomes included the quantitative measurement of similarity of LLM-generated responses to expert-provided answers using text-similarity scores. The results showed a significant improvement in accuracy from 43 to 99% (p < 0.001), when guidelines were provided as context in a coherent corpus of text and non-text sources were converted into text. In addition, few-shot learning did not seem to improve overall accuracy. The study highlights that structured guideline reformatting and advanced prompt engineering (data quality vs. data quantity) can enhance the efficacy of LLM integrations to CDSSs for guideline delivery.

---

### 31. HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models

**Authors:** Bernal Jimenez Gutierrez, Yiheng Shu, Yu Gu, et al.  
**Year:** 2024 | **Citations:** 136 | **Venue:** Neural Information Processing Systems  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/4308208fac24626e0c927ee728038aadc4e87266](https://www.semanticscholar.org/paper/4308208fac24626e0c927ee728038aadc4e87266)  
**arXiv:** [https://arxiv.org/abs/2405.14831](https://arxiv.org/abs/2405.14831)  

**Abstract:** In order to thrive in hostile and ever-changing natural environments, mammalian brains evolved to store large amounts of knowledge about the world and continually integrate new information while avoiding catastrophic forgetting. Despite the impressive accomplishments, large language models (LLMs), even with retrieval-augmented generation (RAG), still struggle to efficiently and effectively integrate a large amount of new experiences after pre-training. In this work, we introduce HippoRAG, a novel retrieval framework inspired by the hippocampal indexing theory of human long-term memory to enable deeper and more efficient knowledge integration over new experiences. HippoRAG synergistically orchestrates LLMs, knowledge graphs, and the Personalized PageRank algorithm to mimic the different roles of neocortex and hippocampus in human memory. We compare HippoRAG with existing RAG methods on multi-hop question answering and show that our method outperforms the state-of-the-art methods remarkably, by up to 20%. Single-step retrieval with HippoRAG achieves comparable or better performance than iterative retrieval like IRCoT while being 10-30 times cheaper and 6-13 times faster, and integrating HippoRAG into IRCoT brings further substantial gains. Finally, we show that our method can tackle new types of scenarios that are out of reach of existing methods. Code and data are available at https://github.com/OSU-NLP-Group/HippoRAG.

---

### 32. VisRAG: Vision-based Retrieval-augmented Generation on Multi-modality Documents

**Authors:** Shi Yu, Chaoyue Tang, Bokai Xu, et al.  
**Year:** 2024 | **Citations:** 135 | **Venue:** International Conference on Learning Representations  
**Year Month:** [Oct 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/d9052dd87959e6076baf35e8f7ee87d568a32b58](https://www.semanticscholar.org/paper/d9052dd87959e6076baf35e8f7ee87d568a32b58)  
**arXiv:** [https://arxiv.org/abs/2410.10594](https://arxiv.org/abs/2410.10594)  

**Abstract:** Retrieval-augmented generation (RAG) is an effective technique that enables large language models (LLMs) to utilize external knowledge sources for generation. However, current RAG systems are solely based on text, rendering it impossible to utilize vision information like layout and images that play crucial roles in real-world multi-modality documents. In this paper, we introduce VisRAG, which tackles this issue by establishing a vision-language model (VLM)-based RAG pipeline. In this pipeline, instead of first parsing the document to obtain text, the document is directly embedded using a VLM as an image and then retrieved to enhance the generation of a VLM. Compared to traditional text-based RAG, VisRAG maximizes the retention and utilization of the data information in the original documents, eliminating the information loss introduced during the parsing process. We collect both open-source and synthetic data to train the retriever in VisRAG and explore a variety of generation methods. Experiments demonstrate that VisRAG outperforms traditional RAG in both the retrieval and generation stages, achieving a 20--40% end-to-end performance gain over traditional text-based RAG pipeline. Further analysis reveals that VisRAG is efficient in utilizing training data and demonstrates strong generalization capability, positioning it as a promising solution for RAG on multi-modality documents. Our code and data are available at https://github.com/openbmb/visrag.

---

### 33. Medical Graph RAG: Towards Safe Medical Large Language Model via Graph Retrieval-Augmented Generation

**Authors:** Junde Wu, Jiayuan Zhu, Yunli Qi  
**Year:** 2024 | **Citations:** 122 | **Venue:** arXiv.org  
**Year Month:** [Aug 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/64fed9e0be009f064b72cdcb7d1fadeb28bea3b0](https://www.semanticscholar.org/paper/64fed9e0be009f064b72cdcb7d1fadeb28bea3b0)  
**arXiv:** [https://arxiv.org/abs/2408.04187](https://arxiv.org/abs/2408.04187)  

**Abstract:** We introduce a novel graph-based Retrieval-Augmented Generation (RAG) framework specifically designed for the medical domain, called \textbf{MedGraphRAG}, aimed at enhancing Large Language Model (LLM) capabilities for generating evidence-based medical responses, thereby improving safety and reliability when handling private medical data. Graph-based RAG (GraphRAG) leverages LLMs to organize RAG data into graphs, showing strong potential for gaining holistic insights from long-form documents. However, its standard implementation is overly complex for general use and lacks the ability to generate evidence-based responses, limiting its effectiveness in the medical field. To extend the capabilities of GraphRAG to the medical domain, we propose unique Triple Graph Construction and U-Retrieval techniques over it. In our graph construction, we create a triple-linked structure that connects user documents to credible medical sources and controlled vocabularies. In the retrieval process, we propose U-Retrieval which combines Top-down Precise Retrieval with Bottom-up Response Refinement to balance global context awareness with precise indexing. These effort enable both source information retrieval and comprehensive response generation. Our approach is validated on 9 medical Q\&A benchmarks, 2 health fact-checking benchmarks, and one collected dataset testing long-form generation. The results show that MedGraphRAG consistently outperforms state-of-the-art models across all benchmarks, while also ensuring that responses include credible source documentation and definitions. Our code is released at: https://github.com/MedicineToken/Medical-Graph-RAG.

---

### 34. Searching for Best Practices in Retrieval-Augmented Generation

**Authors:** Xiaohua Wang, Zhenghua Wang, Xuan Gao, et al.  
**Year:** 2024 | **Citations:** 120 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/9a946c503b6e799b3d57375b6edfaf4e24febcea](https://www.semanticscholar.org/paper/9a946c503b6e799b3d57375b6edfaf4e24febcea)  
**arXiv:** [https://arxiv.org/abs/2407.01219](https://arxiv.org/abs/2407.01219)  

**Abstract:** Retrieval-augmented generation (RAG) techniques have proven to be effective in integrating up-to-date information, mitigating hallucinations, and enhancing response quality, particularly in specialized domains. While many RAG approaches have been proposed to enhance large language models through query-dependent retrievals, these approaches still suffer from their complex implementation and prolonged response times. Typically, a RAG workflow involves multiple processing steps, each of which can be executed in various ways. Here, we investigate existing RAG approaches and their potential combinations to identify optimal RAG practices. Through extensive experiments, we suggest several strategies for deploying RAG that balance both performance and efficiency. Moreover, we demonstrate that multimodal retrieval techniques can significantly enhance question-answering capabilities about visual inputs and accelerate the generation of multimodal content using a “retrieval as generation” strategy.

---

### 35. PoisonedRAG: Knowledge Corruption Attacks to Retrieval-Augmented Generation of Large Language Models

**Authors:** Wei Zou, Runpeng Geng, Binghui Wang, et al.  
**Year:** 2024 | **Citations:** 111 | **Venue:** USENIX Security Symposium  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/f4e06256ab07727ff4e0465deea83fcf45012354](https://www.semanticscholar.org/paper/f4e06256ab07727ff4e0465deea83fcf45012354)  
**arXiv:** [https://arxiv.org/abs/2402.07867](https://arxiv.org/abs/2402.07867)  

**Abstract:** Large language models (LLMs) have achieved remarkable success due to their exceptional generative capabilities. Despite their success, they also have inherent limitations such as a lack of up-to-date knowledge and hallucination. Retrieval-Augmented Generation (RAG) is a state-of-the-art technique to mitigate these limitations. The key idea of RAG is to ground the answer generation of an LLM on external knowledge retrieved from a knowledge database. Existing studies mainly focus on improving the accuracy or efficiency of RAG, leaving its security largely unexplored. We aim to bridge the gap in this work. We find that the knowledge database in a RAG system introduces a new and practical attack surface. Based on this attack surface, we propose PoisonedRAG, the first knowledge corruption attack to RAG, where an attacker could inject a few malicious texts into the knowledge database of a RAG system to induce an LLM to generate an attacker-chosen target answer for an attacker-chosen target question. We formulate knowledge corruption attacks as an optimization problem, whose solution is a set of malicious texts. Depending on the background knowledge (e.g., black-box and white-box settings) of an attacker on a RAG system, we propose two solutions to solve the optimization problem, respectively. Our results show PoisonedRAG could achieve a 90% attack success rate when injecting five malicious texts for each target question into a knowledge database with millions of texts. We also evaluate several defenses and our results show they are insufficient to defend against PoisonedRAG, highlighting the need for new defenses.

---

### 36. Retrieval Augmented Generation or Long-Context LLMs? A Comprehensive Study and Hybrid Approach

**Authors:** Zhuowan Li, Cheng Li, Mingyang Zhang, et al.  
**Year:** 2024 | **Citations:** 110 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ccb5afb760a73f5507e31995397f80960db7842d](https://www.semanticscholar.org/paper/ccb5afb760a73f5507e31995397f80960db7842d)  
**arXiv:** [https://arxiv.org/abs/2407.16833](https://arxiv.org/abs/2407.16833)  

**Abstract:** Retrieval Augmented Generation (RAG) has been a powerful tool for Large Language Models (LLMs) to efficiently process overly lengthy contexts. However, recent LLMs like Gemini-1.5 and GPT-4 show exceptional capabilities to understand long contexts directly. We conduct a comprehensive comparison between RAG and long-context (LC) LLMs, aiming to leverage the strengths of both. We benchmark RAG and LC across various public datasets using three latest LLMs. Results reveal that when resourced sufficiently, LC consistently outperforms RAG in terms of average performance. However, RAG’s significantly lower cost remains a distinct advantage. Based on this observation, we propose Self-Route, a simple yet effective method that routes queries to RAG or LC based on model self-reflection. Self-Route significantly reduces the computation cost while maintaining a comparable performance to LC. Our findings provide a guideline for long-context applications of LLMs using RAG and LC.

---

### 37. Exploring the Capabilities and Limitations of Large Language Models in the Electric Energy Sector

**Authors:** Lin Dong, Subir Majumder, Fatemeh Doudi, et al.  
**Year:** 2024 | **Citations:** 109 | **Venue:** Joule  
**Year Month:** [Mar 2024]  
**Fields:** Engineering, Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1c6c9dd66554debf28cffb29a1fcc22415b57655](https://www.semanticscholar.org/paper/1c6c9dd66554debf28cffb29a1fcc22415b57655)  
**arXiv:** [https://arxiv.org/abs/2403.09125](https://arxiv.org/abs/2403.09125)  

**Abstract:** Large Language Models (LLMs) as chatbots have drawn remarkable attention thanks to their versatile capability in natural language processing as well as in a wide range of tasks. While there has been great enthusiasm towards adopting such foundational model-based artificial intelligence tools in all sectors possible, the capabilities and limitations of such LLMs in improving the operation of the electric energy sector need to be explored, and this article identifies fruitful directions in this regard. Key future research directions include data collection systems for fine-tuning LLMs, embedding power system-specific tools in the LLMs, and retrieval augmented generation (RAG)-based knowledge pool to improve the quality of LLM responses and LLMs in safety-critical use cases.

---

### 38. Retrieval-Augmented Generation for Natural Language Processing: A Survey

**Authors:** Shangyu Wu, Ying Xiong, Yufei Cui, et al.  
**Year:** 2024 | **Citations:** 108 | **Venue:** arXiv.org  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/d4a5c2ab2b459426869e1a3ab1550897b005303e](https://www.semanticscholar.org/paper/d4a5c2ab2b459426869e1a3ab1550897b005303e)  
**arXiv:** [https://arxiv.org/abs/2407.13193](https://arxiv.org/abs/2407.13193)  

**Abstract:** Large language models (LLMs) have demonstrated great success in various fields, benefiting from their huge amount of parameters that store knowledge. However, LLMs still suffer from several key issues, such as hallucination problems, knowledge update issues, and lacking domain-specific expertise. The appearance of retrieval-augmented generation (RAG), which leverages an external knowledge database to augment LLMs, makes up those drawbacks of LLMs. This paper reviews all significant techniques of RAG, especially in the retriever and the retrieval fusions. Besides, tutorial codes are provided for implementing the representative techniques in RAG. This paper further discusses the RAG update, including RAG with/without knowledge update. Then, we introduce RAG evaluation and benchmarking, as well as the application of RAG in representative NLP tasks and industrial scenarios. Finally, this paper discusses RAG's future directions and challenges for promoting this field's development.

---

### 39. FinBen: A Holistic Financial Benchmark for Large Language Models

**Authors:** Qianqian Xie, Weiguang Han, Zhengyu Chen, et al.  
**Year:** 2024 | **Citations:** 107 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b39aba9b515723745c994aa0fbd80a566c268282](https://www.semanticscholar.org/paper/b39aba9b515723745c994aa0fbd80a566c268282)  
**arXiv:** [https://arxiv.org/abs/2402.12659](https://arxiv.org/abs/2402.12659)  

**Abstract:** LLMs have transformed NLP and shown promise in various fields, yet their potential in finance is underexplored due to a lack of comprehensive evaluation benchmarks, the rapid development of LLMs, and the complexity of financial tasks. In this paper, we introduce FinBen, the first extensive open-source evaluation benchmark, including 36 datasets spanning 24 financial tasks, covering seven critical aspects: information extraction (IE), textual analysis, question answering (QA), text generation, risk management, forecasting, and decision-making. FinBen offers several key innovations: a broader range of tasks and datasets, the first evaluation of stock trading, novel agent and Retrieval-Augmented Generation (RAG) evaluation, and three novel open-source evaluation datasets for text summarization, question answering, and stock trading. Our evaluation of 15 representative LLMs, including GPT-4, ChatGPT, and the latest Gemini, reveals several key findings: While LLMs excel in IE and textual analysis, they struggle with advanced reasoning and complex tasks like text generation and forecasting. GPT-4 excels in IE and stock trading, while Gemini is better at text generation and forecasting. Instruction-tuned LLMs improve textual analysis but offer limited benefits for complex tasks such as QA. FinBen has been used to host the first financial LLMs shared task at the FinNLP-AgentScen workshop during IJCAI-2024, attracting 12 teams. Their novel solutions outperformed GPT-4, showcasing FinBen's potential to drive innovation in financial LLMs. All datasets, results, and codes are released for the research community: https://github.com/The-FinAI/PIXIU.

---

### 40. A Survey on Retrieval-Augmented Text Generation for Large Language Models

**Authors:** Yizheng Huang, Jimmy X. Huang  
**Year:** 2024 | **Citations:** 101 | **Venue:** arXiv.org  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/94034fd2ed4b6cf41113abb7adc9ae469313c958](https://www.semanticscholar.org/paper/94034fd2ed4b6cf41113abb7adc9ae469313c958)  
**arXiv:** [https://arxiv.org/abs/2404.10981](https://arxiv.org/abs/2404.10981)  

**Abstract:** Retrieval-Augmented Generation (RAG) merges retrieval methods with deep learning advancements to address the static limitations of large language models (LLMs) by enabling the dynamic integration of up-to-date external information. This methodology, focusing primarily on the text domain, provides a cost-effective solution to the generation of plausible but possibly incorrect responses by LLMs, thereby enhancing the accuracy and reliability of their outputs through the use of real-world data. As RAG grows in complexity and incorporates multiple concepts that can influence its performance, this paper organizes the RAG paradigm into four categories: pre-retrieval, retrieval, post-retrieval, and generation, offering a detailed perspective from the retrieval viewpoint. It outlines RAG's evolution and discusses the field's progression through the analysis of significant studies. Additionally, the paper introduces evaluation methods for RAG, addressing the challenges faced and proposing future research directions. By offering an organized framework and categorization, the study aims to consolidate existing research on RAG, clarify its technological underpinnings, and highlight its potential to broaden the adaptability and applications of LLMs.

---

### 41. ColPali: Efficient Document Retrieval with Vision Language Models

**Authors:** Manuel Faysse, Hugues Sibille, Tony Wu, et al.  
**Year:** 2024 | **Citations:** 100 | **Venue:** International Conference on Learning Representations  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/c948e2d00ac2628ed4098a009c67c81ea4cc00a2](https://www.semanticscholar.org/paper/c948e2d00ac2628ed4098a009c67c81ea4cc00a2)  
**arXiv:** [https://arxiv.org/abs/2407.01449](https://arxiv.org/abs/2407.01449)  

**Abstract:** Documents are visually rich structures that convey information through text, but also figures, page layouts, tables, or even fonts. Since modern retrieval systems mainly rely on the textual information they extract from document pages to index documents -often through lengthy and brittle processes-, they struggle to exploit key visual cues efficiently. This limits their capabilities in many practical document retrieval applications such as Retrieval Augmented Generation (RAG). To benchmark current systems on visually rich document retrieval, we introduce the Visual Document Retrieval Benchmark ViDoRe, composed of various page-level retrieval tasks spanning multiple domains, languages, and practical settings. The inherent complexity and performance shortcomings of modern systems motivate a new concept; doing document retrieval by directly embedding the images of the document pages. We release ColPali, a Vision Language Model trained to produce high-quality multi-vector embeddings from images of document pages. Combined with a late interaction matching mechanism, ColPali largely outperforms modern document retrieval pipelines while being drastically simpler, faster and end-to-end trainable. We release models, data, code and benchmarks under open licenses at https://hf.co/vidore.

---


## AI Agents

*Retrieved: 2026-02-26 19:16:51*

### 1. Mind2Web: Towards a Generalist Agent for the Web

**Authors:** Xiang Deng, Yu Gu, Boyuan Zheng, et al.  
**Year:** 2023 | **Citations:** 852 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Jun 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/58f8925a8b87054ad0635a6398a7fe24935b1604](https://www.semanticscholar.org/paper/58f8925a8b87054ad0635a6398a7fe24935b1604)  
**arXiv:** [https://arxiv.org/abs/2306.06070](https://arxiv.org/abs/2306.06070)  

**Abstract:** We introduce Mind2Web, the first dataset for developing and evaluating generalist agents for the web that can follow language instructions to complete complex tasks on any website. Existing datasets for web agents either use simulated websites or only cover a limited set of websites and tasks, thus not suitable for generalist web agents. With over 2,000 open-ended tasks collected from 137 websites spanning 31 domains and crowdsourced action sequences for the tasks, Mind2Web provides three necessary ingredients for building generalist web agents: 1) diverse domains, websites, and tasks, 2) use of real-world websites instead of simulated and simplified ones, and 3) a broad spectrum of user interaction patterns. Based on Mind2Web, we conduct an initial exploration of using large language models (LLMs) for building generalist web agents. While the raw HTML of real-world websites are often too large to be fed to LLMs, we show that first filtering it with a small LM significantly improves the effectiveness and efficiency of LLMs. Our solution demonstrates a decent level of performance, even on websites or entire domains the model has never seen before, but there is still a substantial room to improve towards truly generalizable agents. We open-source our dataset, model implementation, and trained models (https://osu-nlp-group.github.io/Mind2Web) to facilitate further research on building a generalist agent for the web.

---

### 2. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**Authors:** John Yang, Carlos E. Jimenez, Alexander Wettig, et al.  
**Year:** 2024 | **Citations:** 744 | **Venue:** Neural Information Processing Systems  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1c3c531fc0fbe79f97f367ed3648de8467caeeaa](https://www.semanticscholar.org/paper/1c3c531fc0fbe79f97f367ed3648de8467caeeaa)  
**arXiv:** [https://arxiv.org/abs/2405.15793](https://arxiv.org/abs/2405.15793)  

**Abstract:** Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use. We investigate how interface design affects the performance of language model agents. As a result of this exploration, we introduce SWE-agent: a system that facilitates LM agents to autonomously use computers to solve software engineering tasks. SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files, navigate entire repositories, and execute tests and other programs. We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art achieved with non-interactive LMs. Finally, we provide insight on how the design of the ACI can impact agents' behavior and performance.

---

### 3. Enhanced Moth-flame optimizer with mutation strategy for global optimization

**Authors:** Yueting Xu, Huiling Chen, Jie Luo, et al.  
**Year:** 2019 | **Citations:** 387 | **Venue:** Information Sciences  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/86494f58ce119d97cd0a07a5a2f5084048936af6](https://www.semanticscholar.org/paper/86494f58ce119d97cd0a07a5a2f5084048936af6)  

**Abstract:** Abstract Moth-flame optimization (MFO) is a widely used nature-inspired algorithm characterized by a simple structure with simple parameters. However, for some complex optimization tasks, especially the high dimensional and multimodal problems, MFO may have problems with convergence or tend to fall into local optima. To overcome these limitations, here a series of new variants of MFO are proposed by combining MFO with Gaussian mutation (GM), Cauchy mutation (CM), Levy mutation (LM) or the combination of GM, CM and LM. Specifically, GM is introduced into the basic MFO to improve neighborhood-informed capability. Then, CM with a large mutation step is adopted to enhance global exploration ability. Finally, LM is embedded to increase the randomness of search agents’ movement. The best variant of MFO was compared to 15 state-of-the-art algorithms and 4 well-known advanced optimization approaches on a comprehensive set of 23 benchmark problems and 30 CEC2017 benchmark tasks. The experimental results demonstrate that the three strategies can signiﬁcantly boost exploration and exploitation capabilities of the basic MFO.

---

### 4. Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models

**Authors:** Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, et al.  
**Year:** 2023 | **Citations:** 377 | **Venue:** International Conference on Machine Learning  
**Year Month:** [Oct 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/700bd9681f1b9e9e2212e10415d27b11c7e6836b](https://www.semanticscholar.org/paper/700bd9681f1b9e9e2212e10415d27b11c7e6836b)  
**arXiv:** [https://arxiv.org/abs/2310.04406](https://arxiv.org/abs/2310.04406)  

**Abstract:** While language models (LMs) have shown potential across a range of decision-making tasks, their reliance on simple acting processes limits their broad deployment as autonomous agents. In this paper, we introduce Language Agent Tree Search (LATS) -- the first general framework that synergizes the capabilities of LMs in reasoning, acting, and planning. By leveraging the in-context learning ability of LMs, we integrate Monte Carlo Tree Search into LATS to enable LMs as agents, along with LM-powered value functions and self-reflections for proficient exploration and enhanced decision-making. A key feature of our approach is the incorporation of an environment for external feedback, which offers a more deliberate and adaptive problem-solving mechanism that surpasses the constraints of existing techniques. Our experimental evaluation across diverse domains, including programming, interactive question-answering (QA), web navigation, and math, validates the effectiveness and generality of LATS in decision-making while maintaining competitive or improved reasoning performance. Notably, LATS achieves state-of-the-art pass@1 accuracy (92.7%) for programming on HumanEval with GPT-4 and demonstrates gradient-free performance (average score of 75.9) comparable to gradient-based fine-tuning for web navigation on WebShop with GPT-3.5. Code can be found at https://github.com/lapisrocks/LanguageAgentTreeSearch

---

### 5. Pre-Trained Language Models for Interactive Decision-Making

**Authors:** Shuang Li, Xavier Puig, Yilun Du, et al.  
**Year:** 2022 | **Citations:** 309 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Feb 2022]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b9b220b485d2add79118ffdc2aaa148b67fa53ef](https://www.semanticscholar.org/paper/b9b220b485d2add79118ffdc2aaa148b67fa53ef)  
**arXiv:** [https://arxiv.org/abs/2202.01771](https://arxiv.org/abs/2202.01771)  

**Abstract:** Language model (LM) pre-training is useful in many language processing tasks. But can pre-trained LMs be further leveraged for more general machine learning problems? We propose an approach for using LMs to scaffold learning and generalization in general sequential decision-making problems. In this approach, goals and observations are represented as a sequence of embeddings, and a policy network initialized with a pre-trained LM predicts the next action. We demonstrate that this framework enables effective combinatorial generalization across different environments and supervisory modalities. We begin by assuming access to a set of expert demonstrations, and show that initializing policies with LMs and fine-tuning them via behavior cloning improves task completion rates by 43.6% in the VirtualHome environment. Next, we integrate an active data gathering procedure in which agents iteratively interact with the environment, relabel past"failed"experiences with new goals, and update their policies in a self-supervised loop. Active data gathering further improves combinatorial generalization, outperforming the best baseline by 25.1%. Finally, we explain these results by investigating three possible factors underlying the effectiveness of the LM-based policy. We find that sequential input representations (vs. fixed-dimensional feature vectors) and LM-based weight initialization are both important for generalization. Surprisingly, however, the format of the policy inputs encoding (e.g. as a natural language string vs. an arbitrary sequential encoding) has little influence. Together, these results suggest that language modeling induces representations that are useful for modeling not just language, but also goals and plans; these representations can aid learning and generalization even outside of language processing.

---

### 6. Empowering biomedical discovery with AI agents

**Authors:** Shanghua Gao, Ada Fang, Yepeng Huang, et al.  
**Year:** 2024 | **Citations:** 237 | **Venue:** Cell  
**Year Month:** [Apr 2024]  
**Fields:** Medicine, Computer Science  
**URL:** [https://www.semanticscholar.org/paper/8cedeb11139eab187e43414fd7097c5d578dad7c](https://www.semanticscholar.org/paper/8cedeb11139eab187e43414fd7097c5d578dad7c)  
**arXiv:** [https://arxiv.org/abs/2404.02831](https://arxiv.org/abs/2404.02831)  

**Abstract:** We envision "AI scientists" as systems capable of skeptical learning and reasoning that empower biomedical research through collaborative agents that integrate AI models and biomedical tools with experimental platforms. Rather than taking humans out of the discovery process, biomedical AI agents combine human creativity and expertise with AI's ability to analyze large datasets, navigate hypothesis spaces, and execute repetitive tasks. AI agents are poised to be proficient in various tasks, planning discovery workflows and performing self-assessment to identify and mitigate gaps in their knowledge. These agents use large language models and generative models to feature structured memory for continual learning and use machine learning tools to incorporate scientific knowledge, biological principles, and theories. AI agents can impact areas ranging from virtual cell simulation, programmable control of phenotypes, and the design of cellular circuits to developing new therapies.

---

### 7. AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges

**Authors:** Ranjan Sapkota, Konstantinos I. Roumeliotis, Manoj Karkee  
**Year:** 2025 | **Citations:** 217 | **Venue:** Information Fusion  
**Year Month:** [May 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/986e813f4c4f36786c3642cb9c8718586e47bdcf](https://www.semanticscholar.org/paper/986e813f4c4f36786c3642cb9c8718586e47bdcf)  
**arXiv:** [https://arxiv.org/abs/2505.10468](https://arxiv.org/abs/2505.10468)  

**Abstract:** This review critically distinguishes between AI Agents and Agentic AI, offering a structured, conceptual taxonomy, application mapping, and analysis of opportunities and challenges to clarify their divergent design philosophies and capabilities. We begin by outlining the search strategy and foundational definitions, characterizing AI Agents as modular systems driven and enabled by LLMs and LIMs for taskspecific automation. Generative AI is positioned as a precursor providing the foundation, with AI agents advancing through tool integration, prompt engineering, and reasoning enhancements. We then characterize Agentic AI systems, which, in contrast to AI Agents, represent a paradigm shift marked by multi-agent collaboration, dynamic task decomposition, persistent memory, and coordinated autonomy. Through a chronological evaluation of architectural evolution, operational mechanisms, interaction styles, and autonomy levels, we present a comparative analysis across both AI agents and agentic AI paradigms. Application domains enabled by AI Agents such as customer support, scheduling, and data summarization are then contrasted with Agentic AI deployments in research automation, robotic coordination, and medical decision support. We further examine unique challenges in each paradigm including hallucination, brittleness, emergent behavior, and coordination failure, and propose targeted solutions such as ReAct loops, retrieval-augmented generation (RAG), automation coordination layers, and causal modeling. This work aims to provide a roadmap for developing robust, scalable, and explainable AI-driven systems.  

---

### 8. Identifying the Risks of LM Agents with an LM-Emulated Sandbox

**Authors:** Yangjun Ruan, Honghua Dong, Andrew Wang, et al.  
**Year:** 2023 | **Citations:** 217 | **Venue:** International Conference on Learning Representations  
**Year Month:** [Sep 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/0a893657e00fe8ecfadcc65c63bf293e70cb1564](https://www.semanticscholar.org/paper/0a893657e00fe8ecfadcc65c63bf293e70cb1564)  
**arXiv:** [https://arxiv.org/abs/2309.15817](https://arxiv.org/abs/2309.15817)  

**Abstract:** Recent advances in Language Model (LM) agents and tool use, exemplified by applications like ChatGPT Plugins, enable a rich set of capabilities but also amplify potential risks - such as leaking private data or causing financial losses. Identifying these risks is labor-intensive, necessitating implementing the tools, setting up the environment for each test scenario manually, and finding risky cases. As tools and agents become more complex, the high cost of testing these agents will make it increasingly difficult to find high-stakes, long-tailed risks. To address these challenges, we introduce ToolEmu: a framework that uses an LM to emulate tool execution and enables the testing of LM agents against a diverse range of tools and scenarios, without manual instantiation. Alongside the emulator, we develop an LM-based automatic safety evaluator that examines agent failures and quantifies associated risks. We test both the tool emulator and evaluator through human evaluation and find that 68.8% of failures identified with ToolEmu would be valid real-world agent failures. Using our curated initial benchmark consisting of 36 high-stakes tools and 144 test cases, we provide a quantitative risk analysis of current LM agents and identify numerous failures with potentially severe outcomes. Notably, even the safest LM agent exhibits such failures 23.9% of the time according to our evaluator, underscoring the need to develop safer LM agents for real-world deployment.

---

### 9. Small Language Models are the Future of Agentic AI

**Authors:** Peter Belcák, Greg Heinrich, Shizhe Diao, et al.  
**Year:** 2025 | **Citations:** 182 | **Venue:** arXiv.org  
**Year Month:** [Jun 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/f1d477ccd20b3e90611fc46b1951b3708651a425](https://www.semanticscholar.org/paper/f1d477ccd20b3e90611fc46b1951b3708651a425)  
**arXiv:** [https://arxiv.org/abs/2506.02153](https://arxiv.org/abs/2506.02153)  

**Abstract:** Large language models (LLMs) are often praised for exhibiting near-human performance on a wide range of tasks and valued for their ability to hold a general conversation. The rise of agentic AI systems is, however, ushering in a mass of applications in which language models perform a small number of specialized tasks repetitively and with little variation. Here we lay out the position that small language models (SLMs) are sufficiently powerful, inherently more suitable, and necessarily more economical for many invocations in agentic systems, and are therefore the future of agentic AI. Our argumentation is grounded in the current level of capabilities exhibited by SLMs, the common architectures of agentic systems, and the economy of LM deployment. We further argue that in situations where general-purpose conversational abilities are essential, heterogeneous agentic systems (i.e., agents invoking multiple different models) are the natural choice. We discuss the potential barriers for the adoption of SLMs in agentic systems and outline a general LLM-to-SLM agent conversion algorithm. Our position, formulated as a value statement, highlights the significance of the operational and economic impact even a partial shift from LLMs to SLMs is to have on the AI agent industry. We aim to stimulate the discussion on the effective use of AI resources and hope to advance the efforts to lower the costs of AI of the present day. Calling for both contributions to and critique of our position, we commit to publishing all such correspondence at https://research.nvidia.com/labs/lpr/slm-agents.

---

### 10. Do the Rewards Justify the Means? Measuring Trade-Offs Between Rewards and Ethical Behavior in the MACHIAVELLI Benchmark

**Authors:** Alexander Pan, C. Shern, Andy Zou, et al.  
**Year:** 2023 | **Citations:** 176 | **Venue:** International Conference on Machine Learning  
**Year Month:** [Apr 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5da2d404d789aeff266b63a760d07fe8bc31ba23](https://www.semanticscholar.org/paper/5da2d404d789aeff266b63a760d07fe8bc31ba23)  
**arXiv:** [https://arxiv.org/abs/2304.03279](https://arxiv.org/abs/2304.03279)  

**Abstract:** Artificial agents have traditionally been trained to maximize reward, which may incentivize power-seeking and deception, analogous to how next-token prediction in language models (LMs) may incentivize toxicity. So do agents naturally learn to be Machiavellian? And how do we measure these behaviors in general-purpose models such as GPT-4? Towards answering these questions, we introduce MACHIAVELLI, a benchmark of 134 Choose-Your-Own-Adventure games containing over half a million rich, diverse scenarios that center on social decision-making. Scenario labeling is automated with LMs, which are more performant than human annotators. We mathematize dozens of harmful behaviors and use our annotations to evaluate agents' tendencies to be power-seeking, cause disutility, and commit ethical violations. We observe some tension between maximizing reward and behaving ethically. To improve this trade-off, we investigate LM-based methods to steer agents' towards less harmful behaviors. Our results show that agents can both act competently and morally, so concrete progress can currently be made in machine ethics--designing agents that are Pareto improvements in both safety and capabilities.

---

### 11. TPTU: Task Planning and Tool Usage of Large Language Model-based AI Agents

**Authors:** Jingqing Ruan, Yihong Chen, Bin Zhang, et al.  
**Year:** 2023 | **Citations:** 171 | **Venue:** arXiv.org  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5ce94181ea702f69c3651dce721d6bd8026b8106](https://www.semanticscholar.org/paper/5ce94181ea702f69c3651dce721d6bd8026b8106)  
---

### 12. Language Models as Agent Models

**Authors:** Jacob Andreas  
**Year:** 2022 | **Citations:** 170 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [Dec 2022]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/4596139b28c3ceacbd7e3c34dc0df079dbf4e96b](https://www.semanticscholar.org/paper/4596139b28c3ceacbd7e3c34dc0df079dbf4e96b)  
**arXiv:** [https://arxiv.org/abs/2212.01681](https://arxiv.org/abs/2212.01681)  

**Abstract:** Language models (LMs) are trained on collections of documents, written by individual human agents to achieve specific goals in an outside world. During training, LMs have access only to text of these documents, with no direct evidence of the internal states of the agents that produced them -- a fact often used to argue that LMs are incapable of modeling goal-directed aspects of human language production and comprehension. Can LMs trained on text learn anything at all about the relationship between language and use? I argue that LMs are models of intentional communication in a specific, narrow sense. When performing next word prediction given a textual context, an LM can infer and represent properties of an agent likely to have produced that context. These representations can in turn influence subsequent LM generation in the same way that agents' communicative intentions influence their language. I survey findings from the recent literature showing that -- even in today's non-robust and error-prone models -- LMs infer and use representations of fine-grained communicative intentions and more abstract beliefs and goals. Despite the limited nature of their training data, they can thus serve as building blocks for systems that communicate and act intentionally.

---

### 13. Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

**Authors:** P. Chhikara, Dev Khant, Saket Aryan, et al.  
**Year:** 2025 | **Citations:** 160 | **Venue:** European Conference on Artificial Intelligence  
**Year Month:** [Apr 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1d9c21a0fdb1cc16a32c5d490ebaf98436a23382](https://www.semanticscholar.org/paper/1d9c21a0fdb1cc16a32c5d490ebaf98436a23382)  
**arXiv:** [https://arxiv.org/abs/2504.19413](https://arxiv.org/abs/2504.19413)  

**Abstract:** Large Language Models (LLMs) have demonstrated remarkable prowess in generating contextually coherent responses, yet their fixed context windows pose fundamental challenges for maintaining consistency over prolonged multi-session dialogues. We introduce Mem0, a scalable memory-centric architecture that addresses this issue by dynamically extracting, consolidating, and retrieving salient information from ongoing conversations. Building on this foundation, we further propose an enhanced variant that leverages graph-based memory representations to capture complex relational structures among conversational elements. Through comprehensive evaluations on LOCOMO benchmark, we systematically compare our approaches against six baseline categories: (i) established memory-augmented systems, (ii) retrieval-augmented generation (RAG) with varying chunk sizes and k-values, (iii) a full-context approach that processes the entire conversation history, (iv) an open-source memory solution, (v) a proprietary model system, and (vi) a dedicated memory management platform. Empirical results show that our methods consistently outperform all existing memory systems across four question categories: single-hop, temporal, multi-hop, and open-domain. Notably, Mem0 achieves 26% relative improvements in the LLM-as-a-Judge metric over OpenAI, while Mem0 with graph memory achieves around 2% higher overall score than the base configuration. Beyond accuracy gains, we also markedly reduce computational overhead compared to full-context method. In particular, Mem0 attains a 91% lower p95 latency and saves more than 90% token cost, offering a compelling balance between advanced reasoning capabilities and practical deployment constraints. Our findings highlight critical role of structured, persistent memory mechanisms for long-term conversational coherence, paving the way for more reliable and efficient LLM-driven AI agents.

---

### 14. Generative AI Agents With Large Language Model for Satellite Networks via a Mixture of Experts Transmission

**Authors:** Ruichen Zhang, Hongyang Du, Yinqiu Liu, et al.  
**Year:** 2024 | **Citations:** 158 | **Venue:** IEEE Journal on Selected Areas in Communications  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/6d533b0f318fd22d664356b56b68023560d3c60f](https://www.semanticscholar.org/paper/6d533b0f318fd22d664356b56b68023560d3c60f)  
**arXiv:** [https://arxiv.org/abs/2404.09134](https://arxiv.org/abs/2404.09134)  

**Abstract:** In response to the needs of 6G global communications, satellite communication networks have emerged as a key solution. However, the large-scale development of satellite communication networks is constrained by complex system models, whose modeling is challenging for massive users. Moreover, transmission interference between satellites and users seriously affects communication performance. To solve these problems, this paper develops generative artificial intelligence (AI) agents for model formulation and then applies a mixture of experts (MoE) approach to design transmission strategies. Specifically, we leverage large language models (LLMs) to build an interactive modeling paradigm and utilize retrieval-augmented generation (RAG) to extract satellite expert knowledge that supports mathematical modeling. Afterward, by integrating the expertise of multiple specialized components, we propose an MoE-proximal policy optimization (PPO) approach to solve the formulated problem. Each expert can optimize the optimization variables at which it excels through specialized training through its own network and then aggregate them through the gating network to perform joint optimization. The simulation results validate the accuracy and effectiveness of employing a generative agent for problem formulation. Furthermore, the superiority of the proposed MoE-ppo approach over other benchmarks is confirmed in solving the formulated problem. The adaptability of MoE-PPO to various customized modeling problems has also been demonstrated.

---

### 15. Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents

**Authors:** Pranav Putta, Edmund Mills, Naman Garg, et al.  
**Year:** 2024 | **Citations:** 154 | **Venue:** arXiv.org  
**Year Month:** [Aug 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b393f619a87c5b6aa63c7abc7118263205b6aa62](https://www.semanticscholar.org/paper/b393f619a87c5b6aa63c7abc7118263205b6aa62)  
**arXiv:** [https://arxiv.org/abs/2408.07199](https://arxiv.org/abs/2408.07199)  

**Abstract:** Large Language Models (LLMs) have shown remarkable capabilities in natural language tasks requiring complex reasoning, yet their application in agentic, multi-step reasoning within interactive environments remains a difficult challenge. Traditional supervised pre-training on static datasets falls short in enabling autonomous agent capabilities needed to perform complex decision-making in dynamic settings like web navigation. Previous attempts to bridge this ga-through supervised fine-tuning on curated expert demonstrations-often suffer from compounding errors and limited exploration data, resulting in sub-optimal policy outcomes. To overcome these challenges, we propose a framework that combines guided Monte Carlo Tree Search (MCTS) search with a self-critique mechanism and iterative fine-tuning on agent interactions using an off-policy variant of the Direct Preference Optimization (DPO) algorithm. Our method allows LLM agents to learn effectively from both successful and unsuccessful trajectories, thereby improving their generalization in complex, multi-step reasoning tasks. We validate our approach in the WebShop environment-a simulated e-commerce platform where it consistently outperforms behavior cloning and reinforced fine-tuning baseline, and beats average human performance when equipped with the capability to do online search. In real-world booking scenarios, our methodology boosts Llama-3 70B model's zero-shot performance from 18.6% to 81.7% success rate (a 340% relative increase) after a single day of data collection and further to 95.4% with online search. We believe this represents a substantial leap forward in the capabilities of autonomous agents, paving the way for more sophisticated and reliable decision-making in real-world settings.

---

### 16. AI Agents Under Threat: A Survey of Key Security Challenges and Future Pathways

**Authors:** Zehang Deng, Yongjian Guo, Changzhou Han, et al.  
**Year:** 2024 | **Citations:** 152 | **Venue:** ACM Computing Surveys  
**Year Month:** [Jun 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5aacf780ec16a29bdbe283a14f5a9e6b7e1f292d](https://www.semanticscholar.org/paper/5aacf780ec16a29bdbe283a14f5a9e6b7e1f292d)  
**arXiv:** [https://arxiv.org/abs/2406.02630](https://arxiv.org/abs/2406.02630)  

**Abstract:** An Artificial Intelligence (AI) agent is a software entity that autonomously performs tasks or makes decisions based on pre-defined objectives and data inputs. AI agents, capable of perceiving user inputs, reasoning and planning tasks, and executing actions, have seen remarkable advancements in algorithm development and task performance. However, the security challenges they pose remain under-explored and unresolved. This survey delves into the emerging security threats faced by AI agents, categorizing them into four critical knowledge gaps: unpredictability of multi-step user inputs, complexity in internal executions, variability of operational environments, and interactions with untrusted external entities. By systematically reviewing these threats, this article highlights both the progress made and the existing limitations in safeguarding AI agents. The insights provided aim to inspire further research into addressing the security threats associated with AI agents, thereby fostering the development of more robust and secure AI agent applications.

---

### 17. Tree Search for Language Model Agents

**Authors:** Jing Yu Koh, Stephen McAleer, Daniel Fried, et al.  
**Year:** 2024 | **Citations:** 128 | **Venue:** Trans. Mach. Learn. Res.  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/9345e55a21959948499cee997522aa5eac7ed588](https://www.semanticscholar.org/paper/9345e55a21959948499cee997522aa5eac7ed588)  
**arXiv:** [https://arxiv.org/abs/2407.01476](https://arxiv.org/abs/2407.01476)  

**Abstract:** Autonomous agents powered by language models (LMs) have demonstrated promise in their ability to perform decision-making tasks such as web automation. However, a key limitation remains: LMs, primarily optimized for natural language understanding and generation, struggle with multi-step reasoning, planning, and using environmental feedback when attempting to solve realistic computer tasks. Towards addressing this, we propose an inference-time search algorithm for LM agents to explicitly perform exploration and multi-step planning in interactive web environments. Our approach is a form of best-first tree search that operates within the actual environment space, and is complementary with most existing state-of-the-art agents. It is the first tree search algorithm for LM agents that shows effectiveness on realistic web tasks. On the challenging VisualWebArena benchmark, applying our search algorithm on top of a GPT-4o agent yields a 39.7% relative increase in success rate compared to the same baseline without search, setting a state-of-the-art success rate of 26.4%. On WebArena, search also yields a 28.0% relative improvement over a baseline agent, setting a competitive success rate of 19.2%. Our experiments highlight the effectiveness of search for web agents, and we demonstrate that performance scales with increased test-time compute. We conduct a thorough analysis of our results to highlight improvements from search, limitations, and promising directions for future work. Our code and models are publicly released at https://jykoh.com/search-agents.

---

### 18. AI Agents as Team Members: Effects on Satisfaction, Conflict, Trustworthiness, and Willingness to Work With

**Authors:** A. Dennis, Akshat Lakhiwal, Agrim Sachdeva  
**Year:** 2023 | **Citations:** 119 | **Venue:** Journal of Management Information Systems  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/d783617b40a8113719671e106c476cee0feef3e8](https://www.semanticscholar.org/paper/d783617b40a8113719671e106c476cee0feef3e8)  

**Abstract:** ABSTRACT Organizations are beginning to deploy artificial intelligence (AI) agents as members of virtual teams to help manage information, coordinate team processes, and perform simple tasks. How will team members perceive these AI team members and will they be willing to work with them? We conducted a 2 x  2 x 2 lab experiment that manipulated the type of team member (human or AI), their performance (high or low), and the performance of other team members (high or low). AI team members were perceived to have higher ability and integrity but lower benevolence, which led to no differences in trustworthiness or willingness to work with them. However, the presence of an AI team member resulted in lower process satisfaction. When the AI team member performed well, participants perceived less conflict compared to a human team member with the same performance, but there were no differences in perceived conflict when it performed poorly. There were no other interactions with performance, indicating that the AI team member was judged similarly to humans, irrespective of variations in performance; there was no evidence of algorithm aversion. Our research suggests that AI team members are likely to be accepted into teams, meaning that many old collaboration research questions may need to be reexamined to consider AI team members.

---

### 19. The Virtual Lab of AI agents designs new SARS-CoV-2 nanobodies

**Authors:** Kyle Swanson, Wesley Wu, Nash L. Bulaong, et al.  
**Year:** 2025 | **Citations:** 106 | **Venue:** Nature  
**Fields:** Medicine, Computer Science  
**URL:** [https://www.semanticscholar.org/paper/d24e37aafcf48c76aca30430670bad9a61cd0fca](https://www.semanticscholar.org/paper/d24e37aafcf48c76aca30430670bad9a61cd0fca)  
---

### 20. Magma: A Foundation Model for Multimodal AI Agents

**Authors:** Jianwei Yang, Reuben Tan, Qianhui Wu, et al.  
**Year:** 2025 | **Citations:** 103 | **Venue:** Computer Vision and Pattern Recognition  
**Year Month:** [Feb 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/512b311213c905087ab439b5c303db2e382a7518](https://www.semanticscholar.org/paper/512b311213c905087ab439b5c303db2e382a7518)  
**arXiv:** [https://arxiv.org/abs/2502.13130](https://arxiv.org/abs/2502.13130)  

**Abstract:** We present Magma, a foundation model that serves multimodal AI agentic tasks in both the digital and physical worlds. Magma is a significant extension of vision-language (VL) models in that it not only retains the VL understanding ability (verbal intelligence) of the latter, but is also equipped with the ability to ground and act in the visual-spatial world (spatial-temporal intelligence). To endow agentic capabilities for tasks ranging from UI navigation to robot manipulation, Magma is trained on large amounts of heterogeneous datasets that span from images, videos to robotics data, where actionable visual objects (e.g. clickable buttons in GUI) in images are labeled by Set-of-Mark (SoM) for action grounding, and object movements (e.g. trace of human hands or robotic arms) in videos are labeled by Trace-of-Mark (ToM) for action planning. Extensive experiments show that SoM and ToM help bridge the gap between verbal and action abilities and significantly enhance spatio-temporal intelligence which is fundamental to agentic tasks, as shown in Fig. 1. In particular, Magma creates new state-of-the-art results on UI navigation and robotic manipulation tasks, outperforming previous models that are specifically tailored to these tasks. Moreover, Magma preserves strong multimodal understanding ability and compares favorably to popular large multimodal models that are trained on much larger datasets. We have made our model and code public for reproducibility1.

---

### 21. AI Agents That Matter

**Authors:** Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, et al.  
**Year:** 2024 | **Citations:** 100 | **Venue:** Trans. Mach. Learn. Res.  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/edae954314571eb2913209a7e9825cdc14fd4c58](https://www.semanticscholar.org/paper/edae954314571eb2913209a7e9825cdc14fd4c58)  
**arXiv:** [https://arxiv.org/abs/2407.01502](https://arxiv.org/abs/2407.01502)  

**Abstract:** AI agents are an exciting new research direction, and agent development is driven by benchmarks. Our analysis of current agent benchmarks and evaluation practices reveals several shortcomings that hinder their usefulness in real-world applications. First, there is a narrow focus on accuracy without attention to other metrics. As a result, SOTA agents are needlessly complex and costly, and the community has reached mistaken conclusions about the sources of accuracy gains. Our focus on cost in addition to accuracy motivates the new goal of jointly optimizing the two metrics. We design and implement one such optimization, showing its potential to greatly reduce cost while maintaining accuracy. Second, the benchmarking needs of model and downstream developers have been conflated, making it hard to identify which agent would be best suited for a particular application. Third, many agent benchmarks have inadequate holdout sets, and sometimes none at all. This has led to agents that are fragile because they take shortcuts and overfit to the benchmark in various ways. We prescribe a principled framework for avoiding overfitting. Finally, there is a lack of standardization in evaluation practices, leading to a pervasive lack of reproducibility. We hope that the steps we introduce for addressing these shortcomings will spur the development of agents that are useful in the real world and not just accurate on benchmarks.

---

