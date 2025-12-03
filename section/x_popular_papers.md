# Popular Papers on RAG & AI Agents (Computer Science)

*Generated: 2025-12-03 12:32:02*
*Filtered for Computer Science papers only*

## RAG (Retrieval-Augmented Generation)

*Retrieved: 2025-12-03 12:32:14*

### 1. Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks

**Authors:** Patrick Lewis, Ethan Perez, Aleksandara Piktus, et al.  
**Year:** 2020 | **Citations:** 9,559 | **Venue:** Neural Information Processing Systems  
**Year Month:** [May 2020]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/659bf9ce7175e1ec266ff54359e2bd76e0b7ff31](https://www.semanticscholar.org/paper/659bf9ce7175e1ec266ff54359e2bd76e0b7ff31)  
**arXiv:** [https://arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401)  

**Abstract:** Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited, and hence on knowledge-intensive tasks, their performance lags behind task-specific architectures. Additionally, providing provenance for their decisions and updating their world knowledge remain open research problems. Pre-trained models with a differentiable access mechanism to explicit non-parametric memory can overcome this issue, but have so far been only investigated for extractive downstream tasks. We explore a general-purpose fine-tuning recipe for retrieval-augmented generation (RAG) -- models which combine pre-trained parametric and non-parametric memory for language generation. We introduce RAG models where the parametric memory is a pre-trained seq2seq model and the non-parametric memory is a dense vector index of Wikipedia, accessed with a pre-trained neural retriever. We compare two RAG formulations, one which conditions on the same retrieved passages across the whole generated sequence, the other can use different passages per token. We fine-tune and evaluate our models on a wide range of knowledge-intensive NLP tasks and set the state-of-the-art on three open domain QA tasks, outperforming parametric seq2seq models and task-specific retrieve-and-extract architectures. For language generation tasks, we find that RAG models generate more specific, diverse and factual language than a state-of-the-art parametric-only seq2seq baseline.

---

### 2. Retrieval-Augmented Generation for Large Language Models: A Survey

**Authors:** Yunfan Gao, Yun Xiong, Xinyu Gao, et al.  
**Year:** 2023 | **Citations:** 2,570 | **Venue:** arXiv.org  
**Year Month:** [Dec 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/46f9f7b8f88f72e12cbdb21e3311f995eb6e65c5](https://www.semanticscholar.org/paper/46f9f7b8f88f72e12cbdb21e3311f995eb6e65c5)  
**arXiv:** [https://arxiv.org/abs/2312.10997](https://arxiv.org/abs/2312.10997)  

**Abstract:** Large Language Models (LLMs) showcase impressive capabilities but encounter challenges like hallucination, outdated knowledge, and non-transparent, untraceable reasoning processes. Retrieval-Augmented Generation (RAG) has emerged as a promising solution by incorporating knowledge from external databases. This enhances the accuracy and credibility of the generation, particularly for knowledge-intensive tasks, and allows for continuous knowledge updates and integration of domain-specific information. RAG synergistically merges LLMs' intrinsic knowledge with the vast, dynamic repositories of external databases. This comprehensive review paper offers a detailed examination of the progression of RAG paradigms, encompassing the Naive RAG, the Advanced RAG, and the Modular RAG. It meticulously scrutinizes the tripartite foundation of RAG frameworks, which includes the retrieval, the generation and the augmentation techniques. The paper highlights the state-of-the-art technologies embedded in each of these critical components, providing a profound understanding of the advancements in RAG systems. Furthermore, this paper introduces up-to-date evaluation framework and benchmark. At the end, this article delineates the challenges currently faced and points out prospective avenues for research and development.

---

### 3. Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection

**Authors:** Akari Asai, Zeqiu Wu, Yizhong Wang, et al.  
**Year:** 2023 | **Citations:** 1,203 | **Venue:** International Conference on Learning Representations  
**Year Month:** [Oct 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ddbd8fe782ac98e9c64dd98710687a962195dd9b](https://www.semanticscholar.org/paper/ddbd8fe782ac98e9c64dd98710687a962195dd9b)  
**arXiv:** [https://arxiv.org/abs/2310.11511](https://arxiv.org/abs/2310.11511)  

**Abstract:** Despite their remarkable capabilities, large language models (LLMs) often produce responses containing factual inaccuracies due to their sole reliance on the parametric knowledge they encapsulate. Retrieval-Augmented Generation (RAG), an ad hoc approach that augments LMs with retrieval of relevant knowledge, decreases such issues. However, indiscriminately retrieving and incorporating a fixed number of retrieved passages, regardless of whether retrieval is necessary, or passages are relevant, diminishes LM versatility or can lead to unhelpful response generation. We introduce a new framework called Self-Reflective Retrieval-Augmented Generation (Self-RAG) that enhances an LM's quality and factuality through retrieval and self-reflection. Our framework trains a single arbitrary LM that adaptively retrieves passages on-demand, and generates and reflects on retrieved passages and its own generations using special tokens, called reflection tokens. Generating reflection tokens makes the LM controllable during the inference phase, enabling it to tailor its behavior to diverse task requirements. Experiments show that Self-RAG (7B and 13B parameters) significantly outperforms state-of-the-art LLMs and retrieval-augmented models on a diverse set of tasks. Specifically, Self-RAG outperforms ChatGPT and retrieval-augmented Llama2-chat on Open-domain QA, reasoning and fact verification tasks, and it shows significant gains in improving factuality and citation accuracy for long-form generations relative to these models.

---

### 4. From Local to Global: A Graph RAG Approach to Query-Focused Summarization

**Authors:** Darren Edge, Ha Trinh, Newman Cheng, et al.  
**Year:** 2024 | **Citations:** 835 | **Venue:** arXiv.org  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/c1799bf28d1ae93e1631be5b59196ee1e568f538](https://www.semanticscholar.org/paper/c1799bf28d1ae93e1631be5b59196ee1e568f538)  
**arXiv:** [https://arxiv.org/abs/2404.16130](https://arxiv.org/abs/2404.16130)  

**Abstract:** The use of retrieval-augmented generation (RAG) to retrieve relevant information from an external knowledge source enables large language models (LLMs) to answer questions over private and/or previously unseen document collections. However, RAG fails on global questions directed at an entire text corpus, such as"What are the main themes in the dataset?", since this is inherently a query-focused summarization (QFS) task, rather than an explicit retrieval task. Prior QFS methods, meanwhile, do not scale to the quantities of text indexed by typical RAG systems. To combine the strengths of these contrasting methods, we propose GraphRAG, a graph-based approach to question answering over private text corpora that scales with both the generality of user questions and the quantity of source text. Our approach uses an LLM to build a graph index in two stages: first, to derive an entity knowledge graph from the source documents, then to pregenerate community summaries for all groups of closely related entities. Given a question, each community summary is used to generate a partial response, before all partial responses are again summarized in a final response to the user. For a class of global sensemaking questions over datasets in the 1 million token range, we show that GraphRAG leads to substantial improvements over a conventional RAG baseline for both the comprehensiveness and diversity of generated answers.

---

### 5. A Survey on RAG Meeting LLMs: Towards Retrieval-Augmented Large Language Models

**Authors:** Wenqi Fan, Yujuan Ding, Liang-bo Ning, et al.  
**Year:** 2024 | **Citations:** 531 | **Venue:** Knowledge Discovery and Data Mining  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/eb9c4a07a336e8deefe7b399c550d3af0241238e](https://www.semanticscholar.org/paper/eb9c4a07a336e8deefe7b399c550d3af0241238e)  
**arXiv:** [https://arxiv.org/abs/2405.06211](https://arxiv.org/abs/2405.06211)  

**Abstract:** As one of the most advanced techniques in AI, Retrieval-Augmented Generation (RAG) can offer reliable and up-to-date external knowledge, providing huge convenience for numerous tasks. Particularly in the era of AI-Generated Content (AIGC), the powerful capacity of retrieval in providing additional knowledge enables RAG to assist existing generative AI in producing high-quality outputs. Recently, Large Language Models (LLMs) have demonstrated revolutionary abilities in language understanding and generation, while still facing inherent limitations such as hallucinations and out-of-date internal knowledge. Given the powerful abilities of RAG in providing the latest and helpful auxiliary information, Retrieval-Augmented Large Language Models (RA-LLMs) have emerged to harness external and authoritative knowledge bases, rather than solely relying on the model's internal knowledge, to augment the quality of the generated content of LLMs. In this survey, we comprehensively review existing research studies in RA-LLMs, covering three primary technical perspectives: Furthermore, to deliver deeper insights, we discuss current limitations and several promising directions for future research. Updated information about this survey can be found at: https://advanced-recommender-systems.github.io/RAG-Meets-LLMs/

---

### 6. Active Retrieval Augmented Generation

**Authors:** Zhengbao Jiang, Frank F. Xu, Luyu Gao, et al.  
**Year:** 2023 | **Citations:** 432 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [May 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/88884b8806262a4095036041e3567d450dba39f7](https://www.semanticscholar.org/paper/88884b8806262a4095036041e3567d450dba39f7)  
**arXiv:** [https://arxiv.org/abs/2305.06983](https://arxiv.org/abs/2305.06983)  

**Abstract:** Despite the remarkable ability of large language models (LMs) to comprehend and generate language, they have a tendency to hallucinate and create factually inaccurate output. Augmenting LMs by retrieving information from external knowledge resources is one promising solution. Most existing retrieval augmented LMs employ a retrieve-and-generate setup that only retrieves information once based on the input. This is limiting, however, in more general scenarios involving generation of long texts, where continually gathering information throughout generation is essential. In this work, we provide a generalized view of active retrieval augmented generation, methods that actively decide when and what to retrieve across the course of the generation. We propose Forward-Looking Active REtrieval augmented generation (FLARE), a generic method which iteratively uses a prediction of the upcoming sentence to anticipate future content, which is then utilized as a query to retrieve relevant documents to regenerate the sentence if it contains low-confidence tokens. We test FLARE along with baselines comprehensively over 4 long-form knowledge-intensive generation tasks/datasets. FLARE achieves superior or competitive performance on all tasks, demonstrating the effectiveness of our method. Code and datasets are available at https://github.com/jzbjyb/FLARE.

---

### 7. Benchmarking Large Language Models in Retrieval-Augmented Generation

**Authors:** Jiawei Chen, Hongyu Lin, Xianpei Han, et al.  
**Year:** 2023 | **Citations:** 429 | **Venue:** AAAI Conference on Artificial Intelligence  
**Year Month:** [Sep 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/28e2ecb4183ebc0eec504b12dddc677f8aef8745](https://www.semanticscholar.org/paper/28e2ecb4183ebc0eec504b12dddc677f8aef8745)  
**arXiv:** [https://arxiv.org/abs/2309.01431](https://arxiv.org/abs/2309.01431)  

**Abstract:** Retrieval-Augmented Generation (RAG) is a promising approach for mitigating the hallucination of large language models (LLMs). However, existing research lacks rigorous evaluation of the impact of retrieval-augmented generation on different large language models, which make it challenging to identify the potential bottlenecks in the capabilities of RAG for different LLMs. In this paper, we systematically investigate the impact of Retrieval-Augmented Generation on large language models. We analyze the performance of different large language models in 4 fundamental abilities required for RAG, including noise robustness, negative rejection, information integration, and counterfactual robustness. To this end, we establish Retrieval-Augmented Generation Benchmark (RGB), a new corpus for RAG evaluation in both English and Chinese. RGB divides the instances within the benchmark into 4 separate testbeds based on the aforementioned fundamental abilities required to resolve the case. Then we evaluate 6 representative LLMs on RGB to diagnose the challenges of current LLMs when applying RAG. Evaluation reveals that while LLMs exhibit a certain degree of noise robustness, they still struggle significantly in terms of negative rejection, information integration, and dealing with false information. The aforementioned assessment outcomes indicate that there is still a considerable journey ahead to effectively apply RAG to LLMs.

---

### 8. Retrieval-Augmented Generation for AI-Generated Content: A Survey

**Authors:** Penghao Zhao, Hailin Zhang, Qinhan Yu, et al.  
**Year:** 2024 | **Citations:** 420 | **Venue:** arXiv.org  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ab15463babf98fffc6f683fe2026de0725b5e1a9](https://www.semanticscholar.org/paper/ab15463babf98fffc6f683fe2026de0725b5e1a9)  
**arXiv:** [https://arxiv.org/abs/2402.19473](https://arxiv.org/abs/2402.19473)  

**Abstract:** Advancements in model algorithms, the growth of foundational models, and access to high-quality datasets have propelled the evolution of Artificial Intelligence Generated Content (AIGC). Despite its notable successes, AIGC still faces hurdles such as updating knowledge, handling long-tail data, mitigating data leakage, and managing high training and inference costs. Retrieval-Augmented Generation (RAG) has recently emerged as a paradigm to address such challenges. In particular, RAG introduces the information retrieval process, which enhances the generation process by retrieving relevant objects from available data stores, leading to higher accuracy and better robustness. In this paper, we comprehensively review existing efforts that integrate RAG technique into AIGC scenarios. We first classify RAG foundations according to how the retriever augments the generator, distilling the fundamental abstractions of the augmentation methodologies for various retrievers and generators. This unified perspective encompasses all RAG scenarios, illuminating advancements and pivotal technologies that help with potential future progress. We also summarize additional enhancements methods for RAG, facilitating effective engineering and implementation of RAG systems. Then from another view, we survey on practical applications of RAG across different modalities and tasks, offering valuable references for researchers and practitioners. Furthermore, we introduce the benchmarks for RAG, discuss the limitations of current RAG systems, and suggest potential directions for future research. Github: https://github.com/PKU-DAIR/RAG-Survey.

---

### 9. RAGAs: Automated Evaluation of Retrieval Augmented Generation

**Authors:** ES Shahul, Jithin James, Luis Espinosa Anke, et al.  
**Year:** 2023 | **Citations:** 356 | **Venue:** Conference of the European Chapter of the Association for Computational Linguistics  
**Year Month:** [Sep 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/f5e9e5bbe22f0263be1f1ce88c66978a2b927772](https://www.semanticscholar.org/paper/f5e9e5bbe22f0263be1f1ce88c66978a2b927772)  
**arXiv:** [https://arxiv.org/abs/2309.15217](https://arxiv.org/abs/2309.15217)  

**Abstract:** We introduce RAGAs (Retrieval Augmented Generation Assessment), a framework for reference-free evaluation of Retrieval Augmented Generation (RAG) pipelines. RAGAs is available at [https://github.com/explodinggradients/ragas]. RAG systems are composed of a retrieval and an LLM based generation module. They provide LLMs with knowledge from a reference textual database, enabling them to act as a natural language layer between a user and textual databases, thus reducing the risk of hallucinations. Evaluating RAG architectures is challenging due to several dimensions to consider: the ability of the retrieval system to identify relevant and focused context passages, the ability of the LLM to exploit such passages faithfully, and the quality of the generation itself. With RAGAs, we introduce a suite of metrics that can evaluate these different dimensions without relying on ground truth human annotations. We posit that such a framework can contribute crucially to faster evaluation cycles of RAG architectures, which is especially important given the fast adoption of LLMs.

---

### 10. Benchmarking Retrieval-Augmented Generation for Medicine

**Authors:** Guangzhi Xiong, Qiao Jin, Zhiyong Lu, et al.  
**Year:** 2024 | **Citations:** 332 | **Venue:** Annual Meeting of the Association for Computational Linguistics  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b798cf6af813638fab09a8af6ad0f3df6c241485](https://www.semanticscholar.org/paper/b798cf6af813638fab09a8af6ad0f3df6c241485)  
**arXiv:** [https://arxiv.org/abs/2402.13178](https://arxiv.org/abs/2402.13178)  

**Abstract:** While large language models (LLMs) have achieved state-of-the-art performance on a wide range of medical question answering (QA) tasks, they still face challenges with hallucinations and outdated knowledge. Retrieval-augmented generation (RAG) is a promising solution and has been widely adopted. However, a RAG system can involve multiple flexible components, and there is a lack of best practices regarding the optimal RAG setting for various medical purposes. To systematically evaluate such systems, we propose the Medical Information Retrieval-Augmented Generation Evaluation (MIRAGE), a first-of-its-kind benchmark including 7,663 questions from five medical QA datasets. Using MIRAGE, we conducted large-scale experiments with over 1.8 trillion prompt tokens on 41 combinations of different corpora, retrievers, and backbone LLMs through the MedRAG toolkit introduced in this work. Overall, MedRAG improves the accuracy of six different LLMs by up to 18% over chain-of-thought prompting, elevating the performance of GPT-3.5 and Mixtral to GPT-4-level. Our results show that the combination of various medical corpora and retrievers achieves the best performance. In addition, we discovered a log-linear scaling property and the"lost-in-the-middle"effects in medical RAG. We believe our comprehensive evaluations can serve as practical guidelines for implementing RAG systems for medicine.

---

### 11. Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity

**Authors:** Soyeong Jeong, Jinheon Baek, Sukmin Cho, et al.  
**Year:** 2024 | **Citations:** 302 | **Venue:** North American Chapter of the Association for Computational Linguistics  
**Year Month:** [Mar 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/e5e8c6ac537e0f5b5db14170bc232d6f9e641bbc](https://www.semanticscholar.org/paper/e5e8c6ac537e0f5b5db14170bc232d6f9e641bbc)  
**arXiv:** [https://arxiv.org/abs/2403.14403](https://arxiv.org/abs/2403.14403)  

**Abstract:** Retrieval-Augmented Large Language Models (LLMs), which incorporate the non-parametric knowledge from external knowledge bases into LLMs, have emerged as a promising approach to enhancing response accuracy in several tasks, such as Question-Answering (QA). However, even though there are various approaches dealing with queries of different complexities, they either handle simple queries with unnecessary computational overhead or fail to adequately address complex multi-step queries; yet, not all user requests fall into only one of the simple or complex categories. In this work, we propose a novel adaptive QA framework that can dynamically select the most suitable strategy for (retrieval-augmented) LLMs from the simplest to the most sophisticated ones based on the query complexity. Also, this selection process is operationalized with a classifier, which is a smaller LM trained to predict the complexity level of incoming queries with automatically collected labels, obtained from actual predicted outcomes of models and inherent inductive biases in datasets. This approach offers a balanced strategy, seamlessly adapting between the iterative and single-step retrieval-augmented LLMs, as well as the no-retrieval methods, in response to a range of query complexities. We validate our model on a set of open-domain QA datasets, covering multiple query complexities, and show that ours enhances the overall efficiency and accuracy of QA systems, compared to relevant baselines including the adaptive retrieval approaches. Code is available at: https://github.com/starsuzi/Adaptive-RAG.

---

### 12. The Power of Noise: Redefining Retrieval for RAG Systems

**Authors:** Florin Cuconasu, Giovanni Trappolini, F. Siciliano, et al.  
**Year:** 2024 | **Citations:** 283 | **Venue:** Annual International ACM SIGIR Conference on Research and Development in Information Retrieval  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/77179e5ff669452b9bea479a4236a6e2009ee422](https://www.semanticscholar.org/paper/77179e5ff669452b9bea479a4236a6e2009ee422)  
**arXiv:** [https://arxiv.org/abs/2401.14887](https://arxiv.org/abs/2401.14887)  

**Abstract:** Retrieval-Augmented Generation (RAG) has recently emerged as a method to extend beyond the pre-trained knowledge of Large Language Models by augmenting the original prompt with relevant passages or documents retrieved by an Information Retrieval (IR) system. RAG has become increasingly important for Generative AI solutions, especially in enterprise settings or in any domain in which knowledge is constantly refreshed and cannot be memorized in the LLM. We argue here that the retrieval component of RAG systems, be it dense or sparse, deserves increased attention from the research community, and accordingly, we conduct the first comprehensive and systematic examination of the retrieval strategy of RAG systems. We focus, in particular, on the type of passages IR systems within a RAG solution should retrieve. Our analysis considers multiple factors, such as the relevance of the passages included in the prompt context, their position, and their number. One counter-intuitive finding of this work is that the retriever's highest-scoring documents that are not directly relevant to the query (e.g., do not contain the answer) negatively impact the effectiveness of the LLM. Even more surprising, we discovered that adding random documents in the prompt improves the LLM accuracy by up to 35%. These results highlight the need to investigate the appropriate strategies when integrating retrieval with LLMs, thereby laying the groundwork for future research in this area.

---

### 13. RAFT: Adapting Language Model to Domain Specific RAG

**Authors:** Tianjun Zhang, Shishir G. Patil, Naman Jain, et al.  
**Year:** 2024 | **Citations:** 282 | **Venue:** arXiv.org  
**Year Month:** [Mar 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/fdefb6a9b51c742d71740d25a76973116a2e0893](https://www.semanticscholar.org/paper/fdefb6a9b51c742d71740d25a76973116a2e0893)  
**arXiv:** [https://arxiv.org/abs/2403.10131](https://arxiv.org/abs/2403.10131)  

**Abstract:** Pretraining Large Language Models (LLMs) on large corpora of textual data is now a standard paradigm. When using these LLMs for many downstream applications, it is common to additionally bake in new knowledge (e.g., time-critical news, or private domain knowledge) into the pretrained model either through RAG-based-prompting, or fine-tuning. However, the optimal methodology for the model to gain such new knowledge remains an open question. In this paper, we present Retrieval Augmented FineTuning (RAFT), a training recipe that improves the model's ability to answer questions in a"open-book"in-domain settings. In RAFT, given a question, and a set of retrieved documents, we train the model to ignore those documents that don't help in answering the question, which we call, distractor documents. RAFT accomplishes this by citing verbatim the right sequence from the relevant document that would help answer the question. This coupled with RAFT's chain-of-thought-style response helps improve the model's ability to reason. In domain-specific RAG, RAFT consistently improves the model's performance across PubMed, HotpotQA, and Gorilla datasets, presenting a post-training recipe to improve pre-trained LLMs to in-domain RAG. RAFT's code and demo are open-sourced at github.com/ShishirPatil/gorilla.

---

### 14. Improving the Domain Adaptation of Retrieval Augmented Generation (RAG) Models for Open Domain Question Answering

**Authors:** Shamane Siriwardhana, Rivindu Weerasekera, Elliott Wen, et al.  
**Year:** 2022 | **Citations:** 258 | **Venue:** Transactions of the Association for Computational Linguistics  
**Year Month:** [Oct 2022]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/6fcdad7b8d6b60b23bc51859e736c29f913b249a](https://www.semanticscholar.org/paper/6fcdad7b8d6b60b23bc51859e736c29f913b249a)  
**arXiv:** [https://arxiv.org/abs/2210.02627](https://arxiv.org/abs/2210.02627)  

**Abstract:** Retrieval Augment Generation (RAG) is a recent advancement in Open-Domain Question Answering (ODQA). RAG has only been trained and explored with a Wikipedia-based external knowledge base and is not optimized for use in other specialized domains such as healthcare and news. In this paper, we evaluate the impact of joint training of the retriever and generator components of RAG for the task of domain adaptation in ODQA. We propose RAG-end2end, an extension to RAG that can adapt to a domain-specific knowledge base by updating all components of the external knowledge base during training. In addition, we introduce an auxiliary training signal to inject more domain-specific knowledge. This auxiliary signal forces RAG-end2end to reconstruct a given sentence by accessing the relevant information from the external knowledge base. Our novel contribution is that, unlike RAG, RAG-end2end does joint training of the retriever and generator for the end QA task and domain adaptation. We evaluate our approach with datasets from three domains: COVID-19, News, and Conversations, and achieve significant performance improvements compared to the original RAG model. Our work has been open-sourced through the HuggingFace Transformers library, attesting to our work’s credibility and technical consistency.

---

### 15. Graph Retrieval-Augmented Generation: A Survey

**Authors:** Boci Peng, Yun Zhu, Yongchao Liu, et al.  
**Year:** 2024 | **Citations:** 230 | **Venue:** ACM Transactions on Information Systems  
**Year Month:** [Aug 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/9ab45aa875b56335303398e84a59a3756cd9d530](https://www.semanticscholar.org/paper/9ab45aa875b56335303398e84a59a3756cd9d530)  
**arXiv:** [https://arxiv.org/abs/2408.08921](https://arxiv.org/abs/2408.08921)  

**Abstract:** Recently, Retrieval-Augmented Generation (RAG) has achieved remarkable success in addressing the challenges of Large Language Models (LLMs) without necessitating retraining. By referencing an external knowledge base, RAG refines LLM outputs, effectively mitigating issues such as “hallucination”, lack of domain-specific knowledge, and outdated information. However, the complex structure of relationships among different entities in databases presents challenges for RAG systems. In response, GraphRAG leverages structural information across entities to enable more precise and comprehensive retrieval, capturing relational knowledge and facilitating more accurate, context-aware responses. Given the novelty and potential of GraphRAG, a systematic review of current technologies is imperative. This paper provides the first comprehensive overview of GraphRAG methodologies. We formalize the GraphRAG workflow, encompassing Graph-Based Indexing, Graph-Guided Retrieval, and Graph-Enhanced Generation. We then outline the core technologies and training methods at each stage. Additionally, we examine downstream tasks, application domains, evaluation methodologies, and industrial use cases of GraphRAG. Finally, we explore future research directions to inspire further inquiries and advance progress in the field. In order to track recent progress, we set up a repository at https://github.com/pengboci/GraphRAG-Survey.

---

### 16. Evaluation of Retrieval-Augmented Generation: A Survey

**Authors:** Hao Yu, Aoran Gan, Kai Zhang, et al.  
**Year:** 2024 | **Citations:** 174 | **Venue:** arXiv.org  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/3c6a6c8de005ef5722a54847747f65922e79d622](https://www.semanticscholar.org/paper/3c6a6c8de005ef5722a54847747f65922e79d622)  
**arXiv:** [https://arxiv.org/abs/2405.07437](https://arxiv.org/abs/2405.07437)  

**Abstract:** Retrieval-Augmented Generation (RAG) has recently gained traction in natural language processing. Numerous studies and real-world applications are leveraging its ability to enhance generative models through external information retrieval. Evaluating these RAG systems, however, poses unique challenges due to their hybrid structure and reliance on dynamic knowledge sources. To better understand these challenges, we conduct A Unified Evaluation Process of RAG (Auepora) and aim to provide a comprehensive overview of the evaluation and benchmarks of RAG systems. Specifically, we examine and compare several quantifiable metrics of the Retrieval and Generation components, such as relevance, accuracy, and faithfulness, within the current RAG benchmarks, encompassing the possible output and ground truth pairs. We then analyze the various datasets and metrics, discuss the limitations of current benchmarks, and suggest potential directions to advance the field of RAG benchmarks.

---

### 17. MultiHop-RAG: Benchmarking Retrieval-Augmented Generation for Multi-Hop Queries

**Authors:** Yixuan Tang, Yi Yang  
**Year:** 2024 | **Citations:** 172 | **Venue:** arXiv.org  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/4e71624e90960cb003e311a0fe3b8be4c2863239](https://www.semanticscholar.org/paper/4e71624e90960cb003e311a0fe3b8be4c2863239)  
**arXiv:** [https://arxiv.org/abs/2401.15391](https://arxiv.org/abs/2401.15391)  

**Abstract:** Retrieval-augmented generation (RAG) augments large language models (LLM) by retrieving relevant knowledge, showing promising potential in mitigating LLM hallucinations and enhancing response quality, thereby facilitating the great adoption of LLMs in practice. However, we find that existing RAG systems are inadequate in answering multi-hop queries, which require retrieving and reasoning over multiple pieces of supporting evidence. Furthermore, to our knowledge, no existing RAG benchmarking dataset focuses on multi-hop queries. In this paper, we develop a novel dataset, MultiHop-RAG, which consists of a knowledge base, a large collection of multi-hop queries, their ground-truth answers, and the associated supporting evidence. We detail the procedure of building the dataset, utilizing an English news article dataset as the underlying RAG knowledge base. We demonstrate the benchmarking utility of MultiHop-RAG in two experiments. The first experiment compares different embedding models for retrieving evidence for multi-hop queries. In the second experiment, we examine the capabilities of various state-of-the-art LLMs, including GPT-4, PaLM, and Llama2-70B, in reasoning and answering multi-hop queries given the evidence. Both experiments reveal that existing RAG methods perform unsatisfactorily in retrieving and answering multi-hop queries. We hope MultiHop-RAG will be a valuable resource for the community in developing effective RAG systems, thereby facilitating greater adoption of LLMs in practice. The MultiHop-RAG and implemented RAG system is publicly available at https://github.com/yixuantt/MultiHop-RAG/.

---

### 18. RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models

**Authors:** Yuanhao Wu, Juno Zhu, Siliang Xu, et al.  
**Year:** 2023 | **Citations:** 168 | **Venue:** Annual Meeting of the Association for Computational Linguistics  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/cfce709a65f90312d2bdc1a6cf0380c19becf694](https://www.semanticscholar.org/paper/cfce709a65f90312d2bdc1a6cf0380c19becf694)  
**arXiv:** [https://arxiv.org/abs/2401.00396](https://arxiv.org/abs/2401.00396)  

**Abstract:** Retrieval-augmented generation (RAG) has become a main technique for alleviating hallucinations in large language models (LLMs). Despite the integration of RAG, LLMs may still present unsupported or contradictory claims to the retrieved contents. In order to develop effective hallucination prevention strategies under RAG, it is important to create benchmark datasets that can measure the extent of hallucination. This paper presents RAGTruth, a corpus tailored for analyzing word-level hallucinations in various domains and tasks within the standard RAG frameworks for LLM applications. RAGTruth comprises nearly 18,000 naturally generated responses from diverse LLMs using RAG. These responses have undergone meticulous manual annotations at both the individual cases and word levels, incorporating evaluations of hallucination intensity. We not only benchmark hallucination frequencies across different LLMs, but also critically assess the effectiveness of several existing hallucination detection methodologies. Furthermore, we show that using a high-quality dataset such as RAGTruth, it is possible to finetune a relatively small LLM and achieve a competitive level of performance in hallucination detection when compared to the existing prompt-based approaches using state-of-the-art large language models such as GPT-4.

---

### 19. G-Retriever: Retrieval-Augmented Generation for Textual Graph Understanding and Question Answering

**Authors:** Xiaoxin He, Yijun Tian, Yifei Sun, et al.  
**Year:** 2024 | **Citations:** 165 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/a41d4a3b005c8ec4f821e6ee96672d930ca9596c](https://www.semanticscholar.org/paper/a41d4a3b005c8ec4f821e6ee96672d930ca9596c)  
**arXiv:** [https://arxiv.org/abs/2402.07630](https://arxiv.org/abs/2402.07630)  

**Abstract:** Given a graph with textual attributes, we enable users to `chat with their graph': that is, to ask questions about the graph using a conversational interface. In response to a user's questions, our method provides textual replies and highlights the relevant parts of the graph. While existing works integrate large language models (LLMs) and graph neural networks (GNNs) in various ways, they mostly focus on either conventional graph tasks (such as node, edge, and graph classification), or on answering simple graph queries on small or synthetic graphs. In contrast, we develop a flexible question-answering framework targeting real-world textual graphs, applicable to multiple applications including scene graph understanding, common sense reasoning, and knowledge graph reasoning. Toward this goal, we first develop a Graph Question Answering (GraphQA) benchmark with data collected from different tasks. Then, we propose our G-Retriever method, introducing the first retrieval-augmented generation (RAG) approach for general textual graphs, which can be fine-tuned to enhance graph understanding via soft prompting. To resist hallucination and to allow for textual graphs that greatly exceed the LLM's context window size, G-Retriever performs RAG over a graph by formulating this task as a Prize-Collecting Steiner Tree optimization problem. Empirical evaluations show that our method outperforms baselines on textual graph tasks from multiple domains, scales well with larger graph sizes, and mitigates hallucination.~\footnote{Our codes and datasets are available at: \url{https://github.com/XiaoxinHe/G-Retriever}}

---

### 20. Seven Failure Points When Engineering a Retrieval Augmented Generation System

**Authors:** Scott Barnett, Stefanus Kurniawan, Srikanth Thudumu, et al.  
**Year:** 2024 | **Citations:** 154 | **Venue:** 2024 IEEE/ACM 3rd International Conference on AI Engineering – Software Engineering for AI (CAIN)  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ba454ba8c594dfb86c25dff2e265c8a2686aa037](https://www.semanticscholar.org/paper/ba454ba8c594dfb86c25dff2e265c8a2686aa037)  
**arXiv:** [https://arxiv.org/abs/2401.05856](https://arxiv.org/abs/2401.05856)  

**Abstract:** Software engineers are increasingly adding semantic search capabilities to applications using a strategy known as Retrieval Augmented Generation (RAG). A RAG system involves finding documents that semantically match a query and then passing the documents to a large language model (LLM) such as ChatGPT to extract the right answer using an LLM. RAG systems aim to: a) reduce the problem of hallucinated responses from LLMs, b) link sources/references to generated responses, and c) remove the need for annotating documents with meta-data. However, RAG systems suffer from limitations inherent to information retrieval systems and from reliance on LLMs. In this paper, we present an experience report on the failure points of RAG systems from three case studies from separate domains: research, education, and biomedical. We share the lessons learned and present 7 failure points to consider when designing a RAG system. The two key takeaways arising from our work are: 1) validation of a RAG system is only feasible during operation, and 2) the robustness of a RAG system evolves rather than designed in at the start. We conclude with a list of potential research directions on RAG systems for the software engineering community.CCS CONCEPTS• Software and its engineering → Empirical software validation.

---

### 21. Retrieval-Augmented Generation with Knowledge Graphs for Customer Service Question Answering

**Authors:** Zhentao Xu, Mark Jerome Cruz, Matthew Guevara, et al.  
**Year:** 2024 | **Citations:** 152 | **Venue:** Annual International ACM SIGIR Conference on Research and Development in Information Retrieval  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b708e0f49d8e9708bc649debd9a9372748fffa3d](https://www.semanticscholar.org/paper/b708e0f49d8e9708bc649debd9a9372748fffa3d)  
**arXiv:** [https://arxiv.org/abs/2404.17723](https://arxiv.org/abs/2404.17723)  

**Abstract:** In customer service technical support, swiftly and accurately retrieving relevant past issues is critical for efficiently resolving customer inquiries. The conventional retrieval methods in retrieval-augmented generation (RAG) for large language models (LLMs) treat a large corpus of past issue tracking tickets as plain text, ignoring the crucial intra-issue structure and inter-issue relations, which limits performance. We introduce a novel customer service question-answering method that amalgamates RAG with a knowledge graph (KG). Our method constructs a KG from historical issues for use in retrieval, retaining the intra-issue structure and inter-issue relations. During the question-answering phase, our method parses consumer queries and retrieves related sub-graphs from the KG to generate answers. This integration of a KG not only improves retrieval accuracy by preserving customer service structure information but also enhances answering quality by mitigating the effects of text segmentation. Empirical assessments on our benchmark datasets, utilizing key retrieval (MRR, Recall@K, NDCG@K) and text generation (BLEU, ROUGE, METEOR) metrics, reveal that our method outperforms the baseline by 77.6% in MRR and by 0.32 in BLEU. Our method has been deployed within LinkedIn's customer service team for approximately six months and has reduced the median per-issue resolution time by 28.6%.

---

### 22. RankRAG: Unifying Context Ranking with Retrieval-Augmented Generation in LLMs

**Authors:** Yue Yu, Wei Ping, Zihan Liu, et al.  
**Year:** 2024 | **Citations:** 145 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/80478de9c7a81561e2f3dac9b8b1ef3df389ff2d](https://www.semanticscholar.org/paper/80478de9c7a81561e2f3dac9b8b1ef3df389ff2d)  
**arXiv:** [https://arxiv.org/abs/2407.02485](https://arxiv.org/abs/2407.02485)  

**Abstract:** Large language models (LLMs) typically utilize the top-k contexts from a retriever in retrieval-augmented generation (RAG). In this work, we propose a novel instruction fine-tuning framework RankRAG, which instruction-tunes a single LLM for the dual purpose of context ranking and answer generation in RAG. In particular, the instruction-tuned LLMs work surprisingly well by adding a small fraction of ranking data into the training blend, and outperform existing expert ranking models, including the same LLM exclusively fine-tuned on a large amount of ranking data. For generation, we compare our model with many strong baselines, including GPT-4-0613, GPT-4-turbo-2024-0409, and ChatQA-1.5, an open-sourced model with the state-of-the-art performance on RAG benchmarks. Specifically, our Llama3-RankRAG significantly outperforms Llama3-ChatQA-1.5 and GPT-4 models on nine knowledge-intensive benchmarks. In addition, it also performs comparably to GPT-4 on five RAG benchmarks in the biomedical domain without instruction fine-tuning on biomedical data, demonstrating its superb capability for generalization to new domains.

---

### 23. Chain of Agents: Large Language Models Collaborating on Long-Context Tasks

**Authors:** Yusen Zhang, Ruoxi Sun, Yanfei Chen, et al.  
**Year:** 2024 | **Citations:** 135 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Jun 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1b0fa09f097591d697162300cc6ecb3ee425fd8d](https://www.semanticscholar.org/paper/1b0fa09f097591d697162300cc6ecb3ee425fd8d)  
**arXiv:** [https://arxiv.org/abs/2406.02818](https://arxiv.org/abs/2406.02818)  

**Abstract:** Addressing the challenge of effectively processing long contexts has become a critical issue for Large Language Models (LLMs). Two common strategies have emerged: 1) reducing the input length, such as retrieving relevant chunks by Retrieval-Augmented Generation (RAG), and 2) expanding the context window limit of LLMs. However, both strategies have drawbacks: input reduction has no guarantee of covering the part with needed information, while window extension struggles with focusing on the pertinent information for solving the task. To mitigate these limitations, we propose Chain-of-Agents (CoA), a novel framework that harnesses multi-agent collaboration through natural language to enable information aggregation and context reasoning across various LLMs over long-context tasks. CoA consists of multiple worker agents who sequentially communicate to handle different segmented portions of the text, followed by a manager agent who synthesizes these contributions into a coherent final output. CoA processes the entire input by interleaving reading and reasoning, and it mitigates long context focus issues by assigning each agent a short context. We perform comprehensive evaluation of CoA on a wide range of long-context tasks in question answering, summarization, and code completion, demonstrating significant improvements by up to 10% over strong baselines of RAG, Full-Context, and multi-agent LLMs.

---

### 24. The Good and The Bad: Exploring Privacy Issues in Retrieval-Augmented Generation (RAG)

**Authors:** Shenglai Zeng, Jiankun Zhang, Pengfei He, et al.  
**Year:** 2024 | **Citations:** 133 | **Venue:** Annual Meeting of the Association for Computational Linguistics  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ea89b058ce619ed16d4de633126b02a8179457c8](https://www.semanticscholar.org/paper/ea89b058ce619ed16d4de633126b02a8179457c8)  
**arXiv:** [https://arxiv.org/abs/2402.16893](https://arxiv.org/abs/2402.16893)  

**Abstract:** Retrieval-augmented generation (RAG) is a powerful technique to facilitate language model with proprietary and private data, where data privacy is a pivotal concern. Whereas extensive research has demonstrated the privacy risks of large language models (LLMs), the RAG technique could potentially reshape the inherent behaviors of LLM generation, posing new privacy issues that are currently under-explored. In this work, we conduct extensive empirical studies with novel attack methods, which demonstrate the vulnerability of RAG systems on leaking the private retrieval database. Despite the new risk brought by RAG on the retrieval data, we further reveal that RAG can mitigate the leakage of the LLMs' training data. Overall, we provide new insights in this paper for privacy protection of retrieval-augmented LLMs, which benefit both LLMs and RAG systems builders. Our code is available at https://github.com/phycholosogy/RAG-privacy.

---

### 25. RAG vs Fine-tuning: Pipelines, Tradeoffs, and a Case Study on Agriculture

**Authors:** M. A. D. L. Balaguer, Vinamra Benara, Renato Luiz de Freitas Cunha, et al.  
**Year:** 2024 | **Citations:** 132 | **Venue:** arXiv.org  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/fef0393e997ec51b184e39c712be63197d99fd46](https://www.semanticscholar.org/paper/fef0393e997ec51b184e39c712be63197d99fd46)  
**arXiv:** [https://arxiv.org/abs/2401.08406](https://arxiv.org/abs/2401.08406)  

**Abstract:** There are two common ways in which developers are incorporating proprietary and domain-specific data when building applications of Large Language Models (LLMs): Retrieval-Augmented Generation (RAG) and Fine-Tuning. RAG augments the prompt with the external data, while fine-Tuning incorporates the additional knowledge into the model itself. However, the pros and cons of both approaches are not well understood. In this paper, we propose a pipeline for fine-tuning and RAG, and present the tradeoffs of both for multiple popular LLMs, including Llama2-13B, GPT-3.5, and GPT-4. Our pipeline consists of multiple stages, including extracting information from PDFs, generating questions and answers, using them for fine-tuning, and leveraging GPT-4 for evaluating the results. We propose metrics to assess the performance of different stages of the RAG and fine-Tuning pipeline. We conduct an in-depth study on an agricultural dataset. Agriculture as an industry has not seen much penetration of AI, and we study a potentially disruptive application - what if we could provide location-specific insights to a farmer? Our results show the effectiveness of our dataset generation pipeline in capturing geographic-specific knowledge, and the quantitative and qualitative benefits of RAG and fine-tuning. We see an accuracy increase of over 6 p.p. when fine-tuning the model and this is cumulative with RAG, which increases accuracy by 5 p.p. further. In one particular experiment, we also demonstrate that the fine-tuned model leverages information from across geographies to answer specific questions, increasing answer similarity from 47% to 72%. Overall, the results point to how systems built using LLMs can be adapted to respond and incorporate knowledge across a dimension that is critical for a specific industry, paving the way for further applications of LLMs in other industrial domains.

---

### 26. RQ-RAG: Learning to Refine Queries for Retrieval Augmented Generation

**Authors:** Chi-Min Chan, Chunpu Xu, Ruibin Yuan, et al.  
**Year:** 2024 | **Citations:** 130 | **Venue:** arXiv.org  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/746b96ee17e329f1085a047116c05e12eaa3925a](https://www.semanticscholar.org/paper/746b96ee17e329f1085a047116c05e12eaa3925a)  
**arXiv:** [https://arxiv.org/abs/2404.00610](https://arxiv.org/abs/2404.00610)  

**Abstract:** Large Language Models (LLMs) exhibit remarkable capabilities but are prone to generating inaccurate or hallucinatory responses. This limitation stems from their reliance on vast pretraining datasets, making them susceptible to errors in unseen scenarios. To tackle these challenges, Retrieval-Augmented Generation (RAG) addresses this by incorporating external, relevant documents into the response generation process, thus leveraging non-parametric knowledge alongside LLMs' in-context learning abilities. However, existing RAG implementations primarily focus on initial input for context retrieval, overlooking the nuances of ambiguous or complex queries that necessitate further clarification or decomposition for accurate responses. To this end, we propose learning to Refine Query for Retrieval Augmented Generation (RQ-RAG) in this paper, endeavoring to enhance the model by equipping it with capabilities for explicit rewriting, decomposition, and disambiguation. Our experimental results indicate that our method, when applied to a 7B Llama2 model, surpasses the previous state-of-the-art (SOTA) by an average of 1.9\% across three single-hop QA datasets, and also demonstrates enhanced performance in handling complex, multi-hop QA datasets. Our code is available at https://github.com/chanchimin/RQ-RAG.

---

### 27. Agentic Retrieval-Augmented Generation: A Survey on Agentic RAG

**Authors:** Aditi Singh, Abul Ehtesham, Saket Kumar, et al.  
**Year:** 2025 | **Citations:** 130 | **Venue:** arXiv.org  
**Year Month:** [Jan 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/f1d6bb6b8f0273986094b5e166538a980c674fea](https://www.semanticscholar.org/paper/f1d6bb6b8f0273986094b5e166538a980c674fea)  
**arXiv:** [https://arxiv.org/abs/2501.09136](https://arxiv.org/abs/2501.09136)  

**Abstract:** Large Language Models (LLMs) have revolutionized artificial intelligence (AI) by enabling human like text generation and natural language understanding. However, their reliance on static training data limits their ability to respond to dynamic, real time queries, resulting in outdated or inaccurate outputs. Retrieval Augmented Generation (RAG) has emerged as a solution, enhancing LLMs by integrating real time data retrieval to provide contextually relevant and up-to-date responses. Despite its promise, traditional RAG systems are constrained by static workflows and lack the adaptability required for multistep reasoning and complex task management. Agentic Retrieval-Augmented Generation (Agentic RAG) transcends these limitations by embedding autonomous AI agents into the RAG pipeline. These agents leverage agentic design patterns reflection, planning, tool use, and multiagent collaboration to dynamically manage retrieval strategies, iteratively refine contextual understanding, and adapt workflows to meet complex task requirements. This integration enables Agentic RAG systems to deliver unparalleled flexibility, scalability, and context awareness across diverse applications. This survey provides a comprehensive exploration of Agentic RAG, beginning with its foundational principles and the evolution of RAG paradigms. It presents a detailed taxonomy of Agentic RAG architectures, highlights key applications in industries such as healthcare, finance, and education, and examines practical implementation strategies. Additionally, it addresses challenges in scaling these systems, ensuring ethical decision making, and optimizing performance for real-world applications, while providing detailed insights into frameworks and tools for implementing Agentic RAG.

---

### 28. Corrective Retrieval Augmented Generation

**Authors:** Shi-Qi Yan, Jia-Chen Gu, Yun Zhu, et al.  
**Year:** 2024 | **Citations:** 127 | **Venue:** arXiv.org  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5bbc2b5aa6c63c6a2cfccf095d6020b063ad47ac](https://www.semanticscholar.org/paper/5bbc2b5aa6c63c6a2cfccf095d6020b063ad47ac)  
**arXiv:** [https://arxiv.org/abs/2401.15884](https://arxiv.org/abs/2401.15884)  

**Abstract:** Large language models (LLMs) inevitably exhibit hallucinations since the accuracy of generated texts cannot be secured solely by the parametric knowledge they encapsulate. Although retrieval-augmented generation (RAG) is a practicable complement to LLMs, it relies heavily on the relevance of retrieved documents, raising concerns about how the model behaves if retrieval goes wrong. To this end, we propose the Corrective Retrieval Augmented Generation (CRAG) to improve the robustness of generation. Specifically, a lightweight retrieval evaluator is designed to assess the overall quality of retrieved documents for a query, returning a confidence degree based on which different knowledge retrieval actions can be triggered. Since retrieval from static and limited corpora can only return sub-optimal documents, large-scale web searches are utilized as an extension for augmenting the retrieval results. Besides, a decompose-then-recompose algorithm is designed for retrieved documents to selectively focus on key information and filter out irrelevant information in them. CRAG is plug-and-play and can be seamlessly coupled with various RAG-based approaches. Experiments on four datasets covering short- and long-form generation tasks show that CRAG can significantly improve the performance of RAG-based approaches.

---

### 29. GNN-RAG: Graph Neural Retrieval for Large Language Model Reasoning

**Authors:** Costas Mavromatis, G. Karypis  
**Year:** 2024 | **Citations:** 127 | **Venue:** arXiv.org  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/336605fc899aab6c5b375d1129bf656d246b9013](https://www.semanticscholar.org/paper/336605fc899aab6c5b375d1129bf656d246b9013)  
**arXiv:** [https://arxiv.org/abs/2405.20139](https://arxiv.org/abs/2405.20139)  

**Abstract:** Knowledge Graphs (KGs) represent human-crafted factual knowledge in the form of triplets (head, relation, tail), which collectively form a graph. Question Answering over KGs (KGQA) is the task of answering natural questions grounding the reasoning to the information provided by the KG. Large Language Models (LLMs) are the state-of-the-art models for QA tasks due to their remarkable ability to understand natural language. On the other hand, Graph Neural Networks (GNNs) have been widely used for KGQA as they can handle the complex graph information stored in the KG. In this work, we introduce GNN-RAG, a novel method for combining language understanding abilities of LLMs with the reasoning abilities of GNNs in a retrieval-augmented generation (RAG) style. First, a GNN reasons over a dense KG subgraph to retrieve answer candidates for a given question. Second, the shortest paths in the KG that connect question entities and answer candidates are extracted to represent KG reasoning paths. The extracted paths are verbalized and given as input for LLM reasoning with RAG. In our GNN-RAG framework, the GNN acts as a dense subgraph reasoner to extract useful graph information, while the LLM leverages its natural language processing ability for ultimate KGQA. Furthermore, we develop a retrieval augmentation (RA) technique to further boost KGQA performance with GNN-RAG. Experimental results show that GNN-RAG achieves state-of-the-art performance in two widely used KGQA benchmarks (WebQSP and CWQ), outperforming or matching GPT-4 performance with a 7B tuned LLM. In addition, GNN-RAG excels on multi-hop and multi-entity questions outperforming competing approaches by 8.9--15.5% points at answer F1.

---

### 30. Evaluating Retrieval Quality in Retrieval-Augmented Generation

**Authors:** Alireza Salemi, Hamed Zamani  
**Year:** 2024 | **Citations:** 126 | **Venue:** Annual International ACM SIGIR Conference on Research and Development in Information Retrieval  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/e90435e1ae06fab4efa272f5f46ed74ca0a8cde0](https://www.semanticscholar.org/paper/e90435e1ae06fab4efa272f5f46ed74ca0a8cde0)  
**arXiv:** [https://arxiv.org/abs/2404.13781](https://arxiv.org/abs/2404.13781)  

**Abstract:** Evaluating retrieval-augmented generation (RAG) presents challenges, particularly for retrieval models within these systems. Traditional end-to-end evaluation methods are computationally expensive. Furthermore, evaluation of the retrieval model's performance based on query-document relevance labels shows a small correlation with the RAG system's downstream performance. We propose a novel evaluation approach, eRAG, where each document in the retrieval list is individually utilized by the large language model within the RAG system. The output generated for each document is then evaluated based on the downstream task ground truth labels. In this manner, the downstream performance for each document serves as its relevance label. We employ various downstream task metrics to obtain document-level annotations and aggregate them using set-based or ranking metrics. Extensive experiments on a wide range of datasets demonstrate that eRAG achieves a higher correlation with downstream RAG performance compared to baseline methods, with improvements in Kendall's tau correlation ranging from 0.168 to 0.494. Additionally, eRAG offers significant computational advantages, improving runtime and consuming up to 50 times less GPU memory than end-to-end evaluation.

---

### 31. FlashRAG: A Modular Toolkit for Efficient Retrieval-Augmented Generation Research

**Authors:** Jiajie Jin, Yutao Zhu, Xinyu Yang, et al.  
**Year:** 2024 | **Citations:** 125 | **Venue:** The Web Conference  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/daebec92963ab8dea492f0c209bdf57e87bcaa07](https://www.semanticscholar.org/paper/daebec92963ab8dea492f0c209bdf57e87bcaa07)  
**arXiv:** [https://arxiv.org/abs/2405.13576](https://arxiv.org/abs/2405.13576)  

**Abstract:** With the advent of large language models (LLMs) and multimodal large language models (MLLMs), the potential of retrieval-augmented generation (RAG) has attracted considerable research attention. However, the absence of a standardized framework for implementation, coupled with the inherently complex RAG process, makes it challenging and time-consuming for researchers to compare and evaluate these approaches in a consistent environment. In response to this challenge, we develop FlashRAG, an efficient and modular open-source toolkit designed to assist researchers in reproducing and comparing existing RAG methods and developing their own algorithms within a unified framework. Our toolkit has implemented 16 advanced RAG methods and gathered and organized 38 benchmark datasets. It has various features, including a customizable modular framework, a rich collection of pre-implemented RAG works, comprehensive datasets, efficient auxiliary pre-processing scripts, and extensive and standard evaluation metrics. Our toolkit and resources are available at https://github.com/RUC-NLPIR/FlashRAG.

---

### 32. HybridRAG: Integrating Knowledge Graphs and Vector Retrieval Augmented Generation for Efficient Information Extraction

**Authors:** Bhaskarjit Sarmah, Dhagash Mehta, Benika Hall, et al.  
**Year:** 2024 | **Citations:** 119 | **Venue:** International Conference on AI in Finance  
**Year Month:** [Aug 2024]  
**Fields:** Computer Science, Economics, Mathematics  
**URL:** [https://www.semanticscholar.org/paper/9af8bccf3e42996cbb198a6ceccafa2a084689f6](https://www.semanticscholar.org/paper/9af8bccf3e42996cbb198a6ceccafa2a084689f6)  
**arXiv:** [https://arxiv.org/abs/2408.04948](https://arxiv.org/abs/2408.04948)  

**Abstract:** Extraction and interpretation of intricate information from unstructured text data arising in financial applications, such as earnings call transcripts, present substantial challenges to large language models (LLMs) even using the current best practices to use Retrieval Augmented Generation (RAG) (referred to as VectorRAG techniques which utilize vector databases for information retrieval) due to challenges such as domain specific terminology and complex formats of the documents. We introduce a novel approach based on a combination, called HybridRAG, of the Knowledge Graphs (KGs) based RAG techniques (called GraphRAG) and VectorRAG techniques to enhance question-answer (Q&A) systems for information extraction from financial documents that is shown to be capable of generating accurate and contextually relevant answers. Using experiments on a set of financial earning call transcripts documents which come in the form of Q&A format, and hence provide a natural set of pairs of ground-truth Q&As, we show that HybridRAG which retrieves context from both vector database and KG outperforms both traditional VectorRAG and GraphRAG individually when evaluated at both the retrieval and generation stages in terms of retrieval accuracy and answer generation. The proposed technique has applications beyond the financial domain.

---

### 33. Optimization of hepatological clinical guidelines interpretation by large language models: a retrieval augmented generation-based framework

**Authors:** Simone Kresevic, M. Giuffré, M. Ajčević, et al.  
**Year:** 2024 | **Citations:** 118 | **Venue:** npj Digital Medicine  
**Fields:** Medicine, Computer Science  
**URL:** [https://www.semanticscholar.org/paper/965a0969b460f9246158d88fb28e21c5d80d0a8b](https://www.semanticscholar.org/paper/965a0969b460f9246158d88fb28e21c5d80d0a8b)  

**Abstract:** Large language models (LLMs) can potentially transform healthcare, particularly in providing the right information to the right provider at the right time in the hospital workflow. This study investigates the integration of LLMs into healthcare, specifically focusing on improving clinical decision support systems (CDSSs) through accurate interpretation of medical guidelines for chronic Hepatitis C Virus infection management. Utilizing OpenAI’s GPT-4 Turbo model, we developed a customized LLM framework that incorporates retrieval augmented generation (RAG) and prompt engineering. Our framework involved guideline conversion into the best-structured format that can be efficiently processed by LLMs to provide the most accurate output. An ablation study was conducted to evaluate the impact of different formatting and learning strategies on the LLM’s answer generation accuracy. The baseline GPT-4 Turbo model’s performance was compared against five experimental setups with increasing levels of complexity: inclusion of in-context guidelines, guideline reformatting, and implementation of few-shot learning. Our primary outcome was the qualitative assessment of accuracy based on expert review, while secondary outcomes included the quantitative measurement of similarity of LLM-generated responses to expert-provided answers using text-similarity scores. The results showed a significant improvement in accuracy from 43 to 99% (p < 0.001), when guidelines were provided as context in a coherent corpus of text and non-text sources were converted into text. In addition, few-shot learning did not seem to improve overall accuracy. The study highlights that structured guideline reformatting and advanced prompt engineering (data quality vs. data quantity) can enhance the efficacy of LLM integrations to CDSSs for guideline delivery.

---

### 34. Blended RAG: Improving RAG (Retriever-Augmented Generation) Accuracy with Semantic Search and Hybrid Query-Based Retrievers

**Authors:** Kunal Sawarkar, Abhilasha Mangal, S. R. Solanki  
**Year:** 2024 | **Citations:** 115 | **Venue:** Conference on Multimedia Information Processing and Retrieval  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/8f06a8cff762b5ce6337d3b617442c72a46374a4](https://www.semanticscholar.org/paper/8f06a8cff762b5ce6337d3b617442c72a46374a4)  
**arXiv:** [https://arxiv.org/abs/2404.07220](https://arxiv.org/abs/2404.07220)  

**Abstract:** Retrieval-Augmented Generation (RAG) is a prevalent approach to infuse a private knowledge base of documents with Large Language Models (LLM) to build Generative Q&A (Question-Answering) systems. However, RAG accuracy becomes increasingly challenging as the corpus of documents scales up, with Retrievers playing an outsized role in the overall RAG accuracy by extracting the most relevant document from the corpus to provide context to the LLM. In this paper, we propose the ‘Blended RAG’ method of leveraging semantic search techniques, such as Dense Vector indexes and Sparse Encoder indexes, blended with hybrid query strategies. Our study achieves better retrieval results and sets new benchmarks for IR (Information Retrieval) datasets like NQ and TREC-COVID datasets. We further extend such a ‘Blended Retriever’ to the RAG system to demonstrate far superior results on Generative Q&A datasets like SQUAD, even surpassing fine-tuning performance.

---

### 35. LightRAG: Simple and Fast Retrieval-Augmented Generation

**Authors:** Zirui Guo, Lianghao Xia, Yanhua Yu, et al.  
**Year:** 2024 | **Citations:** 108 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [Oct 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1ea143c34b9bc359780f79ba4d68dee68bcc1129](https://www.semanticscholar.org/paper/1ea143c34b9bc359780f79ba4d68dee68bcc1129)  
**arXiv:** [https://arxiv.org/abs/2410.05779](https://arxiv.org/abs/2410.05779)  

**Abstract:** Retrieval-Augmented Generation (RAG) systems enhance large language models (LLMs) by integrating external knowledge sources, enabling more accurate and contextually relevant responses tailored to user needs. However, existing RAG systems have significant limitations, including reliance on flat data representations and inadequate contextual awareness, which can lead to fragmented answers that fail to capture complex inter-dependencies. To address these challenges, we propose LightRAG, which incorporates graph structures into text indexing and retrieval processes. This innovative framework employs a dual-level retrieval system that enhances comprehensive information retrieval from both low-level and high-level knowledge discovery. Additionally, the integration of graph structures with vector representations facilitates efficient retrieval of related entities and their relationships, significantly improving response times while maintaining contextual relevance. This capability is further enhanced by an incremental update algorithm that ensures the timely integration of new data, allowing the system to remain effective and responsive in rapidly changing data environments. Extensive experimental validation demonstrates considerable improvements in retrieval accuracy and efficiency compared to existing approaches. We have made our LightRAG open-source and available at the link: https://github.com/HKUDS/LightRAG

---

### 36. Retrieval-Augmented Generation with Graphs (GraphRAG)

**Authors:** Haoyu Han, Yu Wang, Harry Shomer, et al.  
**Year:** 2024 | **Citations:** 108 | **Venue:** arXiv.org  
**Year Month:** [Jan 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/12fb0a058ad69f85a2b59cf7a52a29cbb01d8a0b](https://www.semanticscholar.org/paper/12fb0a058ad69f85a2b59cf7a52a29cbb01d8a0b)  
**arXiv:** [https://arxiv.org/abs/2501.00309](https://arxiv.org/abs/2501.00309)  

**Abstract:** Retrieval-augmented generation (RAG) is a powerful technique that enhances downstream task execution by retrieving additional information, such as knowledge, skills, and tools from external sources. Graph, by its intrinsic"nodes connected by edges"nature, encodes massive heterogeneous and relational information, making it a golden resource for RAG in tremendous real-world applications. As a result, we have recently witnessed increasing attention on equipping RAG with Graph, i.e., GraphRAG. However, unlike conventional RAG, where the retriever, generator, and external data sources can be uniformly designed in the neural-embedding space, the uniqueness of graph-structured data, such as diverse-formatted and domain-specific relational knowledge, poses unique and significant challenges when designing GraphRAG for different domains. Given the broad applicability, the associated design challenges, and the recent surge in GraphRAG, a systematic and up-to-date survey of its key concepts and techniques is urgently desired. Following this motivation, we present a comprehensive and up-to-date survey on GraphRAG. Our survey first proposes a holistic GraphRAG framework by defining its key components, including query processor, retriever, organizer, generator, and data source. Furthermore, recognizing that graphs in different domains exhibit distinct relational patterns and require dedicated designs, we review GraphRAG techniques uniquely tailored to each domain. Finally, we discuss research challenges and brainstorm directions to inspire cross-disciplinary opportunities. Our survey repository is publicly maintained at https://github.com/Graph-RAG/GraphRAG/.

---

### 37. Reducing hallucination in structured outputs via Retrieval-Augmented Generation

**Authors:** Patrice B'echard, Orlando Marquez Ayala  
**Year:** 2024 | **Citations:** 107 | **Venue:** North American Chapter of the Association for Computational Linguistics  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/2986b2b06173e065c94bae49c7a9a3718dad486c](https://www.semanticscholar.org/paper/2986b2b06173e065c94bae49c7a9a3718dad486c)  
**arXiv:** [https://arxiv.org/abs/2404.08189](https://arxiv.org/abs/2404.08189)  

**Abstract:** A common and fundamental limitation of Generative AI (GenAI) is its propensity to hallucinate. While large language models (LLM) have taken the world by storm, without eliminating or at least reducing hallucinations, real-world GenAI systems may face challenges in user adoption. In the process of deploying an enterprise application that produces workflows based on natural language requirements, we devised a system leveraging Retrieval Augmented Generation (RAG) to greatly improve the quality of the structured output that represents such workflows. Thanks to our implementation of RAG, our proposed system significantly reduces hallucinations in the output and improves the generalization of our LLM in out-of-domain settings. In addition, we show that using a small, well-trained retriever encoder can reduce the size of the accompanying LLM, thereby making deployments of LLM-based systems less resource-intensive.

---

### 38. HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models

**Authors:** Bernal Jimenez Gutierrez, Yiheng Shu, Yu Gu, et al.  
**Year:** 2024 | **Citations:** 100 | **Venue:** Neural Information Processing Systems  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/4308208fac24626e0c927ee728038aadc4e87266](https://www.semanticscholar.org/paper/4308208fac24626e0c927ee728038aadc4e87266)  
**arXiv:** [https://arxiv.org/abs/2405.14831](https://arxiv.org/abs/2405.14831)  

**Abstract:** In order to thrive in hostile and ever-changing natural environments, mammalian brains evolved to store large amounts of knowledge about the world and continually integrate new information while avoiding catastrophic forgetting. Despite the impressive accomplishments, large language models (LLMs), even with retrieval-augmented generation (RAG), still struggle to efficiently and effectively integrate a large amount of new experiences after pre-training. In this work, we introduce HippoRAG, a novel retrieval framework inspired by the hippocampal indexing theory of human long-term memory to enable deeper and more efficient knowledge integration over new experiences. HippoRAG synergistically orchestrates LLMs, knowledge graphs, and the Personalized PageRank algorithm to mimic the different roles of neocortex and hippocampus in human memory. We compare HippoRAG with existing RAG methods on multi-hop question answering and show that our method outperforms the state-of-the-art methods remarkably, by up to 20%. Single-step retrieval with HippoRAG achieves comparable or better performance than iterative retrieval like IRCoT while being 10-30 times cheaper and 6-13 times faster, and integrating HippoRAG into IRCoT brings further substantial gains. Finally, we show that our method can tackle new types of scenarios that are out of reach of existing methods. Code and data are available at https://github.com/OSU-NLP-Group/HippoRAG.

---


## AI Agents

*Retrieved: 2025-12-03 12:32:25*

### 1. AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation Framework

**Authors:** Qingyun Wu, Gagan Bansal, Jieyu Zhang, et al.  
**Year:** 2023 | **Citations:** 832 | **Venue:** arXiv.org  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1a4c6856292b8c64d19a812a77f0aa6fd47cb96c](https://www.semanticscholar.org/paper/1a4c6856292b8c64d19a812a77f0aa6fd47cb96c)  
---

### 2. AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

**Authors:** Qingyun Wu, Gagan Bansal, Jieyu Zhang, et al.  
**Year:** 2023 | **Citations:** 795 | **Venue:**   
**Year Month:** [Aug 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/9ea0757c750ab1222a7442d3485a74d1c526b04c](https://www.semanticscholar.org/paper/9ea0757c750ab1222a7442d3485a74d1c526b04c)  
**arXiv:** [https://arxiv.org/abs/2308.08155](https://arxiv.org/abs/2308.08155)  

**Abstract:** AutoGen is an open-source framework that allows developers to build LLM applications via multiple agents that can converse with each other to accomplish tasks. AutoGen agents are customizable, conversable, and can operate in various modes that employ combinations of LLMs, human inputs, and tools. Using AutoGen, developers can also flexibly define agent interaction behaviors. Both natural language and computer code can be used to program flexible conversation patterns for different applications. AutoGen serves as a generic infrastructure to build diverse applications of various complexities and LLM capacities. Empirical studies demonstrate the effectiveness of the framework in many example applications, with domains ranging from mathematics, coding, question answering, operations research, online decision-making, entertainment, etc.

---

### 3. Mind2Web: Towards a Generalist Agent for the Web

**Authors:** Xiang Deng, Yu Gu, Boyuan Zheng, et al.  
**Year:** 2023 | **Citations:** 725 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Jun 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/58f8925a8b87054ad0635a6398a7fe24935b1604](https://www.semanticscholar.org/paper/58f8925a8b87054ad0635a6398a7fe24935b1604)  
**arXiv:** [https://arxiv.org/abs/2306.06070](https://arxiv.org/abs/2306.06070)  

**Abstract:** We introduce Mind2Web, the first dataset for developing and evaluating generalist agents for the web that can follow language instructions to complete complex tasks on any website. Existing datasets for web agents either use simulated websites or only cover a limited set of websites and tasks, thus not suitable for generalist web agents. With over 2,000 open-ended tasks collected from 137 websites spanning 31 domains and crowdsourced action sequences for the tasks, Mind2Web provides three necessary ingredients for building generalist web agents: 1) diverse domains, websites, and tasks, 2) use of real-world websites instead of simulated and simplified ones, and 3) a broad spectrum of user interaction patterns. Based on Mind2Web, we conduct an initial exploration of using large language models (LLMs) for building generalist web agents. While the raw HTML of real-world websites are often too large to be fed to LLMs, we show that first filtering it with a small LM significantly improves the effectiveness and efficiency of LLMs. Our solution demonstrates a decent level of performance, even on websites or entire domains the model has never seen before, but there is still a substantial room to improve towards truly generalizable agents. We open-source our dataset, model implementation, and trained models (https://osu-nlp-group.github.io/Mind2Web) to facilitate further research on building a generalist agent for the web.

---

### 4. ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate

**Authors:** Chi-Min Chan, Weize Chen, Yusheng Su, et al.  
**Year:** 2023 | **Citations:** 689 | **Venue:** arXiv.org  
**Year Month:** [Aug 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ec58a564fdda29e6a9a0a7bab5eeb4c290f716d7](https://www.semanticscholar.org/paper/ec58a564fdda29e6a9a0a7bab5eeb4c290f716d7)  
**arXiv:** [https://arxiv.org/abs/2308.07201](https://arxiv.org/abs/2308.07201)  

**Abstract:** Text evaluation has historically posed significant challenges, often demanding substantial labor and time cost. With the emergence of large language models (LLMs), researchers have explored LLMs' potential as alternatives for human evaluation. While these single-agent-based approaches show promise, experimental results suggest that further advancements are needed to bridge the gap between their current effectiveness and human-level evaluation quality. Recognizing that best practices of human evaluation processes often involve multiple human annotators collaborating in the evaluation, we resort to a multi-agent debate framework, moving beyond single-agent prompting strategies. The multi-agent-based approach enables a group of LLMs to synergize with an array of intelligent counterparts, harnessing their distinct capabilities and expertise to enhance efficiency and effectiveness in handling intricate tasks. In this paper, we construct a multi-agent referee team called ChatEval to autonomously discuss and evaluate the quality of generated responses from different models on open-ended questions and traditional natural language generation (NLG) tasks. Our analysis shows that ChatEval transcends mere textual scoring, offering a human-mimicking evaluation process for reliable assessments. Our code is available at https://github.com/chanchimin/ChatEval.

---

### 5. SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering

**Authors:** John Yang, Carlos E. Jimenez, Alexander Wettig, et al.  
**Year:** 2024 | **Citations:** 569 | **Venue:** Neural Information Processing Systems  
**Year Month:** [May 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1c3c531fc0fbe79f97f367ed3648de8467caeeaa](https://www.semanticscholar.org/paper/1c3c531fc0fbe79f97f367ed3648de8467caeeaa)  
**arXiv:** [https://arxiv.org/abs/2405.15793](https://arxiv.org/abs/2405.15793)  

**Abstract:** Language model (LM) agents are increasingly being used to automate complicated tasks in digital environments. Just as humans benefit from powerful software applications, such as integrated development environments, for complex tasks like software engineering, we posit that LM agents represent a new category of end users with their own needs and abilities, and would benefit from specially-built interfaces to the software they use. We investigate how interface design affects the performance of language model agents. As a result of this exploration, we introduce SWE-agent: a system that facilitates LM agents to autonomously use computers to solve software engineering tasks. SWE-agent's custom agent-computer interface (ACI) significantly enhances an agent's ability to create and edit code files, navigate entire repositories, and execute tests and other programs. We evaluate SWE-agent on SWE-bench and HumanEvalFix, achieving state-of-the-art performance on both with a pass@1 rate of 12.5% and 87.7%, respectively, far exceeding the previous state-of-the-art achieved with non-interactive LMs. Finally, we provide insight on how the design of the ACI can impact agents' behavior and performance.

---

### 6. Multi-Agent Collaboration: Harnessing the Power of Intelligent LLM Agents

**Authors:** Yashar Talebirad, Amirhossein Nadiri  
**Year:** 2023 | **Citations:** 340 | **Venue:** arXiv.org  
**Year Month:** [Jun 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ead6121fbc787d508dc6a6d7106f72bf0d647d03](https://www.semanticscholar.org/paper/ead6121fbc787d508dc6a6d7106f72bf0d647d03)  
**arXiv:** [https://arxiv.org/abs/2306.03314](https://arxiv.org/abs/2306.03314)  

**Abstract:** In this paper, we present a novel framework for enhancing the capabilities of large language models (LLMs) by leveraging the power of multi-agent systems. Our framework introduces a collaborative environment where multiple intelligent agent components, each with distinctive attributes and roles, work together to handle complex tasks more efficiently and effectively. We demonstrate the practicality and versatility of our framework through case studies in artificial general intelligence (AGI), specifically focusing on the Auto-GPT and BabyAGI models. We also examine the"Gorilla"model, which integrates external APIs into the LLM. Our framework addresses limitations and challenges such as looping issues, security risks, scalability, system evaluation, and ethical considerations. By modeling various domains such as courtroom simulations and software development scenarios, we showcase the potential applications and benefits of our proposed multi-agent system. Our framework provides an avenue for advancing the capabilities and performance of LLMs through collaboration and knowledge exchange among intelligent agents.

---

### 7. Character-LLM: A Trainable Agent for Role-Playing

**Authors:** Yunfan Shao, Linyang Li, Junqi Dai, et al.  
**Year:** 2023 | **Citations:** 330 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [Oct 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/6628f9ee35e36cdfdcac8a46cef4dba8d529a83b](https://www.semanticscholar.org/paper/6628f9ee35e36cdfdcac8a46cef4dba8d529a83b)  
**arXiv:** [https://arxiv.org/abs/2310.10158](https://arxiv.org/abs/2310.10158)  

**Abstract:** Large language models (LLMs) can be used to serve as agents to simulate human behaviors, given the powerful ability to understand human instructions and provide high-quality generated texts. Such ability stimulates us to wonder whether LLMs can simulate a person in a higher form than simple human behaviors. Therefore, we aim to train an agent with the profile, experience, and emotional states of a specific person instead of using limited prompts to instruct ChatGPT API. In this work, we introduce Character-LLM that teach LLMs to act as specific people such as Beethoven, Queen Cleopatra, Julius Caesar, etc. Our method focuses on editing profiles as experiences of a certain character and training models to be personal simulacra with these experiences. To assess the effectiveness of our approach, we build a test playground that interviews trained agents and evaluates whether the agents \textit{memorize} their characters and experiences. Experimental results show interesting observations that help build future simulacra of humankind.

---

### 8. Understanding the planning of LLM agents: A survey

**Authors:** Xu Huang, Weiwen Liu, Xiaolong Chen, et al.  
**Year:** 2024 | **Citations:** 321 | **Venue:** arXiv.org  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/7e281e8ab380affd3c5724feae038274df378511](https://www.semanticscholar.org/paper/7e281e8ab380affd3c5724feae038274df378511)  
**arXiv:** [https://arxiv.org/abs/2402.02716](https://arxiv.org/abs/2402.02716)  

**Abstract:** As Large Language Models (LLMs) have shown significant intelligence, the progress to leverage LLMs as planning modules of autonomous agents has attracted more attention. This survey provides the first systematic view of LLM-based agents planning, covering recent works aiming to improve planning ability. We provide a taxonomy of existing works on LLM-Agent planning, which can be categorized into Task Decomposition, Plan Selection, External Module, Reflection and Memory. Comprehensive analyses are conducted for each direction, and further challenges for the field of research are discussed.

---

### 9. ExpeL: LLM Agents Are Experiential Learners

**Authors:** Andrew Zhao, Daniel Huang, Quentin Xu, et al.  
**Year:** 2023 | **Citations:** 317 | **Venue:** AAAI Conference on Artificial Intelligence  
**Year Month:** [Aug 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5e4597eb21a393b23e473cf66cb5ae8b27cab03e](https://www.semanticscholar.org/paper/5e4597eb21a393b23e473cf66cb5ae8b27cab03e)  
**arXiv:** [https://arxiv.org/abs/2308.10144](https://arxiv.org/abs/2308.10144)  

**Abstract:** The recent surge in research interest in applying large language models (LLMs) to decision-making tasks has flourished by leveraging the extensive world knowledge embedded in LLMs. While there is a growing demand to tailor LLMs for custom decision-making tasks, finetuning them for specific tasks is resource-intensive and may diminish the model's generalization capabilities. Moreover, state-of-the-art language models like GPT-4 and Claude are primarily accessible through API calls, with their parametric weights remaining proprietary and unavailable to the public. This scenario emphasizes the growing need for new methodologies that allow learning from agent experiences without requiring parametric updates. To address these problems, we introduce the Experiential Learning (ExpeL) agent. Our agent autonomously gathers experiences and extracts knowledge using natural language from a collection of training tasks. At inference, the agent recalls its extracted insights and past experiences to make informed decisions. Our empirical results highlight the robust learning efficacy of the ExpeL agent, indicating a consistent enhancement in its performance as it accumulates experiences. We further explore the emerging capabilities and transfer learning potential of the ExpeL agent through qualitative observations and additional experiments.

---

### 10. Language Agent Tree Search Unifies Reasoning Acting and Planning in Language Models

**Authors:** Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, et al.  
**Year:** 2023 | **Citations:** 301 | **Venue:** International Conference on Machine Learning  
**Year Month:** [Oct 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/700bd9681f1b9e9e2212e10415d27b11c7e6836b](https://www.semanticscholar.org/paper/700bd9681f1b9e9e2212e10415d27b11c7e6836b)  
**arXiv:** [https://arxiv.org/abs/2310.04406](https://arxiv.org/abs/2310.04406)  

**Abstract:** While language models (LMs) have shown potential across a range of decision-making tasks, their reliance on simple acting processes limits their broad deployment as autonomous agents. In this paper, we introduce Language Agent Tree Search (LATS) -- the first general framework that synergizes the capabilities of LMs in reasoning, acting, and planning. By leveraging the in-context learning ability of LMs, we integrate Monte Carlo Tree Search into LATS to enable LMs as agents, along with LM-powered value functions and self-reflections for proficient exploration and enhanced decision-making. A key feature of our approach is the incorporation of an environment for external feedback, which offers a more deliberate and adaptive problem-solving mechanism that surpasses the constraints of existing techniques. Our experimental evaluation across diverse domains, including programming, interactive question-answering (QA), web navigation, and math, validates the effectiveness and generality of LATS in decision-making while maintaining competitive or improved reasoning performance. Notably, LATS achieves state-of-the-art pass@1 accuracy (92.7%) for programming on HumanEval with GPT-4 and demonstrates gradient-free performance (average score of 75.9) comparable to gradient-based fine-tuning for web navigation on WebShop with GPT-3.5. Code can be found at https://github.com/lapisrocks/LanguageAgentTreeSearch

---

### 11. Pre-Trained Language Models for Interactive Decision-Making

**Authors:** Shuang Li, Xavier Puig, Yilun Du, et al.  
**Year:** 2022 | **Citations:** 299 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Feb 2022]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b9b220b485d2add79118ffdc2aaa148b67fa53ef](https://www.semanticscholar.org/paper/b9b220b485d2add79118ffdc2aaa148b67fa53ef)  
**arXiv:** [https://arxiv.org/abs/2202.01771](https://arxiv.org/abs/2202.01771)  

**Abstract:** Language model (LM) pre-training is useful in many language processing tasks. But can pre-trained LMs be further leveraged for more general machine learning problems? We propose an approach for using LMs to scaffold learning and generalization in general sequential decision-making problems. In this approach, goals and observations are represented as a sequence of embeddings, and a policy network initialized with a pre-trained LM predicts the next action. We demonstrate that this framework enables effective combinatorial generalization across different environments and supervisory modalities. We begin by assuming access to a set of expert demonstrations, and show that initializing policies with LMs and fine-tuning them via behavior cloning improves task completion rates by 43.6% in the VirtualHome environment. Next, we integrate an active data gathering procedure in which agents iteratively interact with the environment, relabel past"failed"experiences with new goals, and update their policies in a self-supervised loop. Active data gathering further improves combinatorial generalization, outperforming the best baseline by 25.1%. Finally, we explain these results by investigating three possible factors underlying the effectiveness of the LM-based policy. We find that sequential input representations (vs. fixed-dimensional feature vectors) and LM-based weight initialization are both important for generalization. Surprisingly, however, the format of the policy inputs encoding (e.g. as a natural language string vs. an arbitrary sequential encoding) has little influence. Together, these results suggest that language modeling induces representations that are useful for modeling not just language, but also goals and plans; these representations can aid learning and generalization even outside of language processing.

---

### 12. Executable Code Actions Elicit Better LLM Agents

**Authors:** Xingyao Wang, Yangyi Chen, Lifan Yuan, et al.  
**Year:** 2024 | **Citations:** 282 | **Venue:** International Conference on Machine Learning  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/78fbb6e7a1c568a04e8c935aa9909d0c942ea5f6](https://www.semanticscholar.org/paper/78fbb6e7a1c568a04e8c935aa9909d0c942ea5f6)  
**arXiv:** [https://arxiv.org/abs/2402.01030](https://arxiv.org/abs/2402.01030)  

**Abstract:** Large Language Model (LLM) agents, capable of performing a broad range of actions, such as invoking tools and controlling robots, show great potential in tackling real-world challenges. LLM agents are typically prompted to produce actions by generating JSON or text in a pre-defined format, which is usually limited by constrained action space (e.g., the scope of pre-defined tools) and restricted flexibility (e.g., inability to compose multiple tools). This work proposes to use executable Python code to consolidate LLM agents' actions into a unified action space (CodeAct). Integrated with a Python interpreter, CodeAct can execute code actions and dynamically revise prior actions or emit new actions upon new observations through multi-turn interactions. Our extensive analysis of 17 LLMs on API-Bank and a newly curated benchmark shows that CodeAct outperforms widely used alternatives (up to 20% higher success rate). The encouraging performance of CodeAct motivates us to build an open-source LLM agent that interacts with environments by executing interpretable code and collaborates with users using natural language. To this end, we collect an instruction-tuning dataset CodeActInstruct that consists of 7k multi-turn interactions using CodeAct. We show that it can be used with existing data to improve models in agent-oriented tasks without compromising their general capability. CodeActAgent, finetuned from Llama2 and Mistral, is integrated with Python interpreter and uniquely tailored to perform sophisticated tasks (e.g., model training) using existing libraries and autonomously self-debug.

---

### 13. OpenHands: An Open Platform for AI Software Developers as Generalist Agents

**Authors:** Xingyao Wang, Boxuan Li, Yufan Song, et al.  
**Year:** 2024 | **Citations:** 281 | **Venue:** International Conference on Learning Representations  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1d07e5b6f978cf69c0186f3d5f434fa92d471e46](https://www.semanticscholar.org/paper/1d07e5b6f978cf69c0186f3d5f434fa92d471e46)  
**arXiv:** [https://arxiv.org/abs/2407.16741](https://arxiv.org/abs/2407.16741)  

**Abstract:** Software is one of the most powerful tools that we humans have at our disposal; it allows a skilled programmer to interact with the world in complex and profound ways. At the same time, thanks to improvements in large language models (LLMs), there has also been a rapid development in AI agents that interact with and affect change in their surrounding environments. In this paper, we introduce OpenHands (f.k.a. OpenDevin), a platform for the development of powerful and flexible AI agents that interact with the world in similar ways to those of a human developer: by writing code, interacting with a command line, and browsing the web. We describe how the platform allows for the implementation of new agents, safe interaction with sandboxed environments for code execution, coordination between multiple agents, and incorporation of evaluation benchmarks. Based on our currently incorporated benchmarks, we perform an evaluation of agents over 15 challenging tasks, including software engineering (e.g., SWE-BENCH) and web browsing (e.g., WEBARENA), among others. Released under the permissive MIT license, OpenHands is a community project spanning academia and industry with more than 2.1K contributions from over 188 contributors.

---

### 14. Personal LLM Agents: Insights and Survey about the Capability, Efficiency and Security

**Authors:** Yuanchun Li, Hao Wen, Weijun Wang, et al.  
**Year:** 2024 | **Citations:** 252 | **Venue:** arXiv.org  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/06d860a5bbb99a4eafdbbb2d5f6aa8dd5fd32cf4](https://www.semanticscholar.org/paper/06d860a5bbb99a4eafdbbb2d5f6aa8dd5fd32cf4)  
**arXiv:** [https://arxiv.org/abs/2401.05459](https://arxiv.org/abs/2401.05459)  

**Abstract:** Since the advent of personal computing devices, intelligent personal assistants (IPAs) have been one of the key technologies that researchers and engineers have focused on, aiming to help users efficiently obtain information and execute tasks, and provide users with more intelligent, convenient, and rich interaction experiences. With the development of smartphones and IoT, computing and sensing devices have become ubiquitous, greatly expanding the boundaries of IPAs. However, due to the lack of capabilities such as user intent understanding, task planning, tool using, and personal data management etc., existing IPAs still have limited practicality and scalability. Recently, the emergence of foundation models, represented by large language models (LLMs), brings new opportunities for the development of IPAs. With the powerful semantic understanding and reasoning capabilities, LLM can enable intelligent agents to solve complex problems autonomously. In this paper, we focus on Personal LLM Agents, which are LLM-based agents that are deeply integrated with personal data and personal devices and used for personal assistance. We envision that Personal LLM Agents will become a major software paradigm for end-users in the upcoming era. To realize this vision, we take the first step to discuss several important questions about Personal LLM Agents, including their architecture, capability, efficiency and security. We start by summarizing the key components and design choices in the architecture of Personal LLM Agents, followed by an in-depth analysis of the opinions collected from domain experts. Next, we discuss several key challenges to achieve intelligent, efficient and secure Personal LLM Agents, followed by a comprehensive survey of representative solutions to address these challenges.

---

### 15. Agentless: Demystifying LLM-based Software Engineering Agents

**Authors:** Chun Xia, Yinlin Deng, Soren Dunn, et al.  
**Year:** 2024 | **Citations:** 215 | **Venue:** arXiv.org  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/ae50c8e255ba55bdbbb05ea470aa63437534438e](https://www.semanticscholar.org/paper/ae50c8e255ba55bdbbb05ea470aa63437534438e)  
**arXiv:** [https://arxiv.org/abs/2407.01489](https://arxiv.org/abs/2407.01489)  

**Abstract:** Recent advancements in large language models (LLMs) have significantly advanced the automation of software development tasks, including code synthesis, program repair, and test generation. More recently, researchers and industry practitioners have developed various autonomous LLM agents to perform end-to-end software development tasks. These agents are equipped with the ability to use tools, run commands, observe feedback from the environment, and plan for future actions. However, the complexity of these agent-based approaches, together with the limited abilities of current LLMs, raises the following question: Do we really have to employ complex autonomous software agents? To attempt to answer this question, we build Agentless -- an agentless approach to automatically solve software development problems. Compared to the verbose and complex setup of agent-based approaches, Agentless employs a simplistic three-phase process of localization, repair, and patch validation, without letting the LLM decide future actions or operate with complex tools. Our results on the popular SWE-bench Lite benchmark show that surprisingly the simplistic Agentless is able to achieve both the highest performance (32.00%, 96 correct fixes) and low cost ($0.70) compared with all existing open-source software agents! Furthermore, we manually classified the problems in SWE-bench Lite and found problems with exact ground truth patch or insufficient/misleading issue descriptions. As such, we construct SWE-bench Lite-S by excluding such problematic issues to perform more rigorous evaluation and comparison. Our work highlights the current overlooked potential of a simple, interpretable technique in autonomous software development. We hope Agentless will help reset the baseline, starting point, and horizon for autonomous software agents, and inspire future work along this crucial direction.

---

### 16. Exploring Collaboration Mechanisms for LLM Agents: A Social Psychology View

**Authors:** Jintian Zhang, Xin Xu, Ruibo Liu, et al.  
**Year:** 2023 | **Citations:** 212 | **Venue:** arXiv.org  
**Year Month:** [Oct 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/9fcdbfdf28245010c875ce85502351fe05c04b49](https://www.semanticscholar.org/paper/9fcdbfdf28245010c875ce85502351fe05c04b49)  
**arXiv:** [https://arxiv.org/abs/2310.02124](https://arxiv.org/abs/2310.02124)  

**Abstract:** As Natural Language Processing (NLP) systems are increasingly employed in intricate social environments, a pressing query emerges: Can these NLP systems mirror human-esque collaborative intelligence, in a multi-agent society consisting of multiple large language models (LLMs)? This paper probes the collaboration mechanisms among contemporary NLP systems by melding practical experiments with theoretical insights. We fabricate four unique `societies' comprised of LLM agents, where each agent is characterized by a specific `trait' (easy-going or overconfident) and engages in collaboration with a distinct `thinking pattern' (debate or reflection). Through evaluating these multi-agent societies on three benchmark datasets, we discern that certain collaborative strategies not only outshine previous top-tier approaches, but also optimize efficiency (using fewer API tokens). Moreover, our results further illustrate that LLM agents manifest human-like social behaviors, such as conformity and consensus reaching, mirroring foundational social psychology theories. In conclusion, we integrate insights from social psychology to contextualize the collaboration of LLM agents, inspiring further investigations into the collaboration mechanism for LLMs. We commit to sharing our code and datasets\footnote{\url{https://github.com/zjunlp/MachineSoM}.}, hoping to catalyze further research in this promising avenue.

---

### 17. RepairAgent: An Autonomous, LLM-Based Agent for Program Repair

**Authors:** Islem Bouzenia, Prem Devanbu, Michael Pradel  
**Year:** 2024 | **Citations:** 183 | **Venue:** International Conference on Software Engineering  
**Year Month:** [Mar 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b7f46c9f01d9f649d18b709e2e88b3b97bebd016](https://www.semanticscholar.org/paper/b7f46c9f01d9f649d18b709e2e88b3b97bebd016)  
**arXiv:** [https://arxiv.org/abs/2403.17134](https://arxiv.org/abs/2403.17134)  

**Abstract:** Automated program repair has emerged as a powerful technique to mitigate the impact of software bugs on system reliability and user experience. This paper introduces Repair Agent, the first work to address the program repair challenge through an autonomous agent based on a large language model (LLM). Unlike existing deep learning-based approaches, which prompt a model with a fixed prompt or in a fixed feedback loop, our work treats the LLM as an agent capable of autonomously planning and executing actions to fix bugs by invoking suitable tools. Repair Agent freely interleaves gathering information about the bug, gathering repair ingredients, and validating fixes, while deciding which tools to invoke based on the gathered information and feedback from previous fix attempts. Key contributions that enable Repair Agent include a set of tools that are useful for program repair, a dynamically updated prompt format that allows the LLM to interact with these tools, and a finite state machine that guides the agent in invoking the tools. Our evaluation on the popular Defects4J dataset demonstrates Repair Agent's effectiveness in autonomously repairing 164 bugs, including 39 bugs not fixed by prior techniques. Interacting with the LLM imposes an average cost of 270k tokens per bug, which, under the current pricing of OpenAI's GPT-3.5 model, translates to 14 cents per bug. To the best of our knowledge, this work is the first to present an autonomous, LLM-based agent for program repair, paving the way for future agent-based techniques in software engineering.

---

### 18. Empowering biomedical discovery with AI agents

**Authors:** Shanghua Gao, Ada Fang, Yepeng Huang, et al.  
**Year:** 2024 | **Citations:** 182 | **Venue:** Cell  
**Year Month:** [Apr 2024]  
**Fields:** Medicine, Computer Science  
**URL:** [https://www.semanticscholar.org/paper/8cedeb11139eab187e43414fd7097c5d578dad7c](https://www.semanticscholar.org/paper/8cedeb11139eab187e43414fd7097c5d578dad7c)  
**arXiv:** [https://arxiv.org/abs/2404.02831](https://arxiv.org/abs/2404.02831)  
---

### 19. Identifying the Risks of LM Agents with an LM-Emulated Sandbox

**Authors:** Yangjun Ruan, Honghua Dong, Andrew Wang, et al.  
**Year:** 2023 | **Citations:** 178 | **Venue:** International Conference on Learning Representations  
**Year Month:** [Sep 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/0a893657e00fe8ecfadcc65c63bf293e70cb1564](https://www.semanticscholar.org/paper/0a893657e00fe8ecfadcc65c63bf293e70cb1564)  
**arXiv:** [https://arxiv.org/abs/2309.15817](https://arxiv.org/abs/2309.15817)  

**Abstract:** Recent advances in Language Model (LM) agents and tool use, exemplified by applications like ChatGPT Plugins, enable a rich set of capabilities but also amplify potential risks - such as leaking private data or causing financial losses. Identifying these risks is labor-intensive, necessitating implementing the tools, setting up the environment for each test scenario manually, and finding risky cases. As tools and agents become more complex, the high cost of testing these agents will make it increasingly difficult to find high-stakes, long-tailed risks. To address these challenges, we introduce ToolEmu: a framework that uses an LM to emulate tool execution and enables the testing of LM agents against a diverse range of tools and scenarios, without manual instantiation. Alongside the emulator, we develop an LM-based automatic safety evaluator that examines agent failures and quantifies associated risks. We test both the tool emulator and evaluator through human evaluation and find that 68.8% of failures identified with ToolEmu would be valid real-world agent failures. Using our curated initial benchmark consisting of 36 high-stakes tools and 144 test cases, we provide a quantitative risk analysis of current LM agents and identify numerous failures with potentially severe outcomes. Notably, even the safest LM agent exhibits such failures 23.9% of the time according to our evaluator, underscoring the need to develop safer LM agents for real-world deployment.

---

### 20. Language Models as Agent Models

**Authors:** Jacob Andreas  
**Year:** 2022 | **Citations:** 163 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [Dec 2022]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/4596139b28c3ceacbd7e3c34dc0df079dbf4e96b](https://www.semanticscholar.org/paper/4596139b28c3ceacbd7e3c34dc0df079dbf4e96b)  
**arXiv:** [https://arxiv.org/abs/2212.01681](https://arxiv.org/abs/2212.01681)  

**Abstract:** Language models (LMs) are trained on collections of documents, written by individual human agents to achieve specific goals in an outside world. During training, LMs have access only to text of these documents, with no direct evidence of the internal states of the agents that produced them -- a fact often used to argue that LMs are incapable of modeling goal-directed aspects of human language production and comprehension. Can LMs trained on text learn anything at all about the relationship between language and use? I argue that LMs are models of intentional communication in a specific, narrow sense. When performing next word prediction given a textual context, an LM can infer and represent properties of an agent likely to have produced that context. These representations can in turn influence subsequent LM generation in the same way that agents' communicative intentions influence their language. I survey findings from the recent literature showing that -- even in today's non-robust and error-prone models -- LMs infer and use representations of fine-grained communicative intentions and more abstract beliefs and goals. Despite the limited nature of their training data, they can thus serve as building blocks for systems that communicate and act intentionally.

---

### 21. Do the Rewards Justify the Means? Measuring Trade-Offs Between Rewards and Ethical Behavior in the MACHIAVELLI Benchmark

**Authors:** Alexander Pan, C. Shern, Andy Zou, et al.  
**Year:** 2023 | **Citations:** 162 | **Venue:** International Conference on Machine Learning  
**Year Month:** [Apr 2023]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5da2d404d789aeff266b63a760d07fe8bc31ba23](https://www.semanticscholar.org/paper/5da2d404d789aeff266b63a760d07fe8bc31ba23)  
**arXiv:** [https://arxiv.org/abs/2304.03279](https://arxiv.org/abs/2304.03279)  

**Abstract:** Artificial agents have traditionally been trained to maximize reward, which may incentivize power-seeking and deception, analogous to how next-token prediction in language models (LMs) may incentivize toxicity. So do agents naturally learn to be Machiavellian? And how do we measure these behaviors in general-purpose models such as GPT-4? Towards answering these questions, we introduce MACHIAVELLI, a benchmark of 134 Choose-Your-Own-Adventure games containing over half a million rich, diverse scenarios that center on social decision-making. Scenario labeling is automated with LMs, which are more performant than human annotators. We mathematize dozens of harmful behaviors and use our annotations to evaluate agents' tendencies to be power-seeking, cause disutility, and commit ethical violations. We observe some tension between maximizing reward and behaving ethically. To improve this trade-off, we investigate LM-based methods to steer agents' towards less harmful behaviors. Our results show that agents can both act competently and morally, so concrete progress can currently be made in machine ethics--designing agents that are Pareto improvements in both safety and capabilities.

---

### 22. Evaluating Very Long-Term Conversational Memory of LLM Agents

**Authors:** Adyasha Maharana, Dong-Ho Lee, S. Tulyakov, et al.  
**Year:** 2024 | **Citations:** 160 | **Venue:** Annual Meeting of the Association for Computational Linguistics  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/0bf3a1867f7245b8a702093901c66b08b518eafc](https://www.semanticscholar.org/paper/0bf3a1867f7245b8a702093901c66b08b518eafc)  
**arXiv:** [https://arxiv.org/abs/2402.17753](https://arxiv.org/abs/2402.17753)  

**Abstract:** Existing works on long-term open-domain dialogues focus on evaluating model responses within contexts spanning no more than five chat sessions. Despite advancements in long-context large language models (LLMs) and retrieval augmented generation (RAG) techniques, their efficacy in very long-term dialogues remains unexplored. To address this research gap, we introduce a machine-human pipeline to generate high-quality, very long-term dialogues by leveraging LLM-based agent architectures and grounding their dialogues on personas and temporal event graphs. Moreover, we equip each agent with the capability of sharing and reacting to images. The generated conversations are verified and edited by human annotators for long-range consistency and grounding to the event graphs. Using this pipeline, we collect LoCoMo, a dataset of very long-term conversations, each encompassing 300 turns and 9K tokens on avg., over up to 35 sessions. Based on LoCoMo, we present a comprehensive evaluation benchmark to measure long-term memory in models, encompassing question answering, event summarization, and multi-modal dialogue generation tasks. Our experimental results indicate that LLMs exhibit challenges in understanding lengthy conversations and comprehending long-range temporal and causal dynamics within dialogues. Employing strategies like long-context LLMs or RAG can offer improvements but these models still substantially lag behind human performance.

---

### 23. AgentPoison: Red-teaming LLM Agents via Poisoning Memory or Knowledge Bases

**Authors:** Zhaorun Chen, Zhen Xiang, Chaowei Xiao, et al.  
**Year:** 2024 | **Citations:** 160 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b6948a9e8b3eec5a56a80c69727154fcd7ececce](https://www.semanticscholar.org/paper/b6948a9e8b3eec5a56a80c69727154fcd7ececce)  
**arXiv:** [https://arxiv.org/abs/2407.12784](https://arxiv.org/abs/2407.12784)  

**Abstract:** LLM agents have demonstrated remarkable performance across various applications, primarily due to their advanced capabilities in reasoning, utilizing external knowledge and tools, calling APIs, and executing actions to interact with environments. Current agents typically utilize a memory module or a retrieval-augmented generation (RAG) mechanism, retrieving past knowledge and instances with similar embeddings from knowledge bases to inform task planning and execution. However, the reliance on unverified knowledge bases raises significant concerns about their safety and trustworthiness. To uncover such vulnerabilities, we propose a novel red teaming approach AgentPoison, the first backdoor attack targeting generic and RAG-based LLM agents by poisoning their long-term memory or RAG knowledge base. In particular, we form the trigger generation process as a constrained optimization to optimize backdoor triggers by mapping the triggered instances to a unique embedding space, so as to ensure that whenever a user instruction contains the optimized backdoor trigger, the malicious demonstrations are retrieved from the poisoned memory or knowledge base with high probability. In the meantime, benign instructions without the trigger will still maintain normal performance. Unlike conventional backdoor attacks, AgentPoison requires no additional model training or fine-tuning, and the optimized backdoor trigger exhibits superior transferability, in-context coherence, and stealthiness. Extensive experiments demonstrate AgentPoison's effectiveness in attacking three types of real-world LLM agents: RAG-based autonomous driving agent, knowledge-intensive QA agent, and healthcare EHRAgent. On each agent, AgentPoison achieves an average attack success rate higher than 80% with minimal impact on benign performance (less than 1%) with a poison rate less than 0.1%.

---

### 24. Agent Laboratory: Using LLM Agents as Research Assistants

**Authors:** Samuel Schmidgall, Yusheng Su, Ze Wang, et al.  
**Year:** 2025 | **Citations:** 160 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [Jan 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/394924896e24c9b086d96d0958dae07f54ff9452](https://www.semanticscholar.org/paper/394924896e24c9b086d96d0958dae07f54ff9452)  
**arXiv:** [https://arxiv.org/abs/2501.04227](https://arxiv.org/abs/2501.04227)  

**Abstract:** Historically, scientific discovery has been a lengthy and costly process, demanding substantial time and resources from initial conception to final results. To accelerate scientific discovery, reduce research costs, and improve research quality, we introduce Agent Laboratory, an autonomous LLM-based framework capable of completing the entire research process. This framework accepts a human-provided research idea and progresses through three stages--literature review, experimentation, and report writing to produce comprehensive research outputs, including a code repository and a research report, while enabling users to provide feedback and guidance at each stage. We deploy Agent Laboratory with various state-of-the-art LLMs and invite multiple researchers to assess its quality by participating in a survey, providing human feedback to guide the research process, and then evaluate the final paper. We found that: (1) Agent Laboratory driven by o1-preview generates the best research outcomes; (2) The generated machine learning code is able to achieve state-of-the-art performance compared to existing methods; (3) Human involvement, providing feedback at each stage, significantly improves the overall quality of research; (4) Agent Laboratory significantly reduces research expenses, achieving an 84% decrease compared to previous autonomous research methods. We hope Agent Laboratory enables researchers to allocate more effort toward creative ideation rather than low-level coding and writing, ultimately accelerating scientific discovery.

---

### 25. TPTU: Task Planning and Tool Usage of Large Language Model-based AI Agents

**Authors:** Jingqing Ruan, Yihong Chen, Bin Zhang, et al.  
**Year:** 2023 | **Citations:** 158 | **Venue:** arXiv.org  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5ce94181ea702f69c3651dce721d6bd8026b8106](https://www.semanticscholar.org/paper/5ce94181ea702f69c3651dce721d6bd8026b8106)  
---

### 26. Bots with Feelings: Should AI Agents Express Positive Emotion in Customer Service?

**Authors:** Elizabeth Han, Dezhi Yin, Han Zhang  
**Year:** 2022 | **Citations:** 150 | **Venue:** Information systems research  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/a79707c7646debe27f1a5188996237f11763592c](https://www.semanticscholar.org/paper/a79707c7646debe27f1a5188996237f11763592c)  

**Abstract:** The rise of emotional intelligence technology and the recent debate about the possibility of a “sentient” artificial intelligence (AI) urge the need to study the role of emotion during people’s interactions with AIs. In customer service, human employees are increasingly replaced by AI agents, such as chatbots, and often these AI agents are equipped with emotion-expressing capabilities to replicate the positive impact of human-expressed positive emotion. But is it indeed beneficial? This research explores how, when, and why an AI agent’s expression of positive emotion affects customers’ service evaluations. Through controlled experiments in which the subjects interacted with a service agent (AI or human) to resolve a hypothetical service issue, we provide answers to these questions. We show that AI-expressed positive emotion can influence customers affectively (by evoking customers’ positive emotions) and cognitively (by violating customers’ expectations) in opposite directions. Thus, positive emotion expressed by an AI agent (versus a human employee) is less effective in facilitating service evaluations. We further underscore that, depending on customers’ expectations toward their relationship with a service agent, AI-expressed positive emotion may enhance or hurt service evaluations. Overall, our work provides useful guidance on how and when companies can best deploy emotion-expressing AI agents.

---

### 27. Data Interpreter: An LLM Agent For Data Science

**Authors:** Sirui Hong, Yizhang Lin, Bangbang Liu, et al.  
**Year:** 2024 | **Citations:** 137 | **Venue:** Annual Meeting of the Association for Computational Linguistics  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/01e863776846ebd1a9a7acc4a9ca24217f953aa2](https://www.semanticscholar.org/paper/01e863776846ebd1a9a7acc4a9ca24217f953aa2)  
**arXiv:** [https://arxiv.org/abs/2402.18679](https://arxiv.org/abs/2402.18679)  

**Abstract:** Large Language Model (LLM)-based agents have shown effectiveness across many applications. However, their use in data science scenarios requiring solving long-term interconnected tasks, dynamic data adjustments and domain expertise remains challenging. Previous approaches primarily focus on individual tasks, making it difficult to assess the complete data science workflow. Moreover, they struggle to handle real-time changes in intermediate data and fail to adapt dynamically to evolving task dependencies inherent to data science problems. In this paper, we present Data Interpreter, an LLM-based agent designed to automatically solve various data science problems end-to-end. Our Data Interpreter incorporates two key modules: 1) Hierarchical Graph Modeling, which breaks down complex problems into manageable subproblems, enabling dynamic node generation and graph optimization; and 2) Programmable Node Generation, a technique that refines and verifies each subproblem to iteratively improve code generation results and robustness. Extensive experiments consistently demonstrate the superiority of Data Interpreter. On InfiAgent-DABench, it achieves a 25% performance boost, raising accuracy from 75.9% to 94.9%. For machine learning and open-ended tasks, it improves performance from 88% to 95%, and from 60% to 97%, respectively. Moreover, on the MATH dataset, Data Interpreter achieves remarkable performance with a 26% improvement compared to state-of-the-art baselines. The code is available at https://github.com/geekan/MetaGPT.

---

### 28. A-MEM: Agentic Memory for LLM Agents

**Authors:** Wujiang Xu, Zujie Liang, Kai Mei, et al.  
**Year:** 2025 | **Citations:** 135 | **Venue:** arXiv.org  
**Year Month:** [Feb 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1f35a15fe9df43d24ec6ea551ec6c9766c17eccf](https://www.semanticscholar.org/paper/1f35a15fe9df43d24ec6ea551ec6c9766c17eccf)  
**arXiv:** [https://arxiv.org/abs/2502.12110](https://arxiv.org/abs/2502.12110)  

**Abstract:** While large language model (LLM) agents can effectively use external tools for complex real-world tasks, they require memory systems to leverage historical experiences. Current memory systems enable basic storage and retrieval but lack sophisticated memory organization, despite recent attempts to incorporate graph databases. Moreover, these systems'fixed operations and structures limit their adaptability across diverse tasks. To address this limitation, this paper proposes a novel agentic memory system for LLM agents that can dynamically organize memories in an agentic way. Following the basic principles of the Zettelkasten method, we designed our memory system to create interconnected knowledge networks through dynamic indexing and linking. When a new memory is added, we generate a comprehensive note containing multiple structured attributes, including contextual descriptions, keywords, and tags. The system then analyzes historical memories to identify relevant connections, establishing links where meaningful similarities exist. Additionally, this process enables memory evolution - as new memories are integrated, they can trigger updates to the contextual representations and attributes of existing historical memories, allowing the memory network to continuously refine its understanding. Our approach combines the structured organization principles of Zettelkasten with the flexibility of agent-driven decision making, allowing for more adaptive and context-aware memory management. Empirical experiments on six foundation models show superior improvement against existing SOTA baselines. The source code for evaluating performance is available at https://github.com/WujiangXu/A-mem, while the source code of the agentic memory system is available at https://github.com/WujiangXu/A-mem-sys.

---

### 29. Dynamic LLM-Agent Network: An LLM-agent Collaboration Framework with Agent Team Optimization

**Authors:** Zijun Liu, Yanzhe Zhang, Peng Li, et al.  
**Year:** 2023 | **Citations:** 134 | **Venue:** arXiv.org  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/98ce7af921e7c52d81df64d632d34eb09522cd75](https://www.semanticscholar.org/paper/98ce7af921e7c52d81df64d632d34eb09522cd75)  
---

### 30. Agent Q: Advanced Reasoning and Learning for Autonomous AI Agents

**Authors:** Pranav Putta, Edmund Mills, Naman Garg, et al.  
**Year:** 2024 | **Citations:** 132 | **Venue:** arXiv.org  
**Year Month:** [Aug 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/b393f619a87c5b6aa63c7abc7118263205b6aa62](https://www.semanticscholar.org/paper/b393f619a87c5b6aa63c7abc7118263205b6aa62)  
**arXiv:** [https://arxiv.org/abs/2408.07199](https://arxiv.org/abs/2408.07199)  

**Abstract:** Large Language Models (LLMs) have shown remarkable capabilities in natural language tasks requiring complex reasoning, yet their application in agentic, multi-step reasoning within interactive environments remains a difficult challenge. Traditional supervised pre-training on static datasets falls short in enabling autonomous agent capabilities needed to perform complex decision-making in dynamic settings like web navigation. Previous attempts to bridge this ga-through supervised fine-tuning on curated expert demonstrations-often suffer from compounding errors and limited exploration data, resulting in sub-optimal policy outcomes. To overcome these challenges, we propose a framework that combines guided Monte Carlo Tree Search (MCTS) search with a self-critique mechanism and iterative fine-tuning on agent interactions using an off-policy variant of the Direct Preference Optimization (DPO) algorithm. Our method allows LLM agents to learn effectively from both successful and unsuccessful trajectories, thereby improving their generalization in complex, multi-step reasoning tasks. We validate our approach in the WebShop environment-a simulated e-commerce platform where it consistently outperforms behavior cloning and reinforced fine-tuning baseline, and beats average human performance when equipped with the capability to do online search. In real-world booking scenarios, our methodology boosts Llama-3 70B model's zero-shot performance from 18.6% to 81.7% success rate (a 340% relative increase) after a single day of data collection and further to 95.4% with online search. We believe this represents a substantial leap forward in the capabilities of autonomous agents, paving the way for more sophisticated and reliable decision-making in real-world settings.

---

### 31. Mental Models of AI Agents in a Cooperative Game Setting

**Authors:** K. Gero, Zahra Ashktorab, Casey Dugan, et al.  
**Year:** 2020 | **Citations:** 131 | **Venue:** International Conference on Human Factors in Computing Systems  
**Fields:** Computer Science, Psychology  
**URL:** [https://www.semanticscholar.org/paper/a109274aa61679a5d95058b4bd20fa7acba0df52](https://www.semanticscholar.org/paper/a109274aa61679a5d95058b4bd20fa7acba0df52)  

**Abstract:** As more and more forms of AI become prevalent, it becomes increasingly important to understand how people develop mental models of these systems. In this work we study people's mental models of AI in a cooperative word guessing game. We run think-aloud studies in which people play the game with an AI agent; through thematic analysis we identify features of the mental models developed by participants. In a large-scale study we have participants play the game with the AI agent online and use a post-game survey to probe their mental model. We find that those who win more often have better estimates of the AI agent's abilities. We present three components for modeling AI systems, propose that understanding the underlying technology is insufficient for developing appropriate conceptual models (analysis of behavior is also necessary), and suggest future work for studying the revision of mental models over time.

---

### 32. R-Judge: Benchmarking Safety Risk Awareness for LLM Agents

**Authors:** Tongxin Yuan, Zhiwei He, Lingzhong Dong, et al.  
**Year:** 2024 | **Citations:** 131 | **Venue:** Conference on Empirical Methods in Natural Language Processing  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/0e0ea3593dda3039cb93d2ec795a87420006ec08](https://www.semanticscholar.org/paper/0e0ea3593dda3039cb93d2ec795a87420006ec08)  
**arXiv:** [https://arxiv.org/abs/2401.10019](https://arxiv.org/abs/2401.10019)  

**Abstract:** Large language models (LLMs) have exhibited great potential in autonomously completing tasks across real-world applications. Despite this, these LLM agents introduce unexpected safety risks when operating in interactive environments. Instead of centering on the harmlessness of LLM-generated content in most prior studies, this work addresses the imperative need for benchmarking the behavioral safety of LLM agents within diverse environments. We introduce R-Judge, a benchmark crafted to evaluate the proficiency of LLMs in judging and identifying safety risks given agent interaction records. R-Judge comprises 569 records of multi-turn agent interaction, encompassing 27 key risk scenarios among 5 application categories and 10 risk types. It is of high-quality curation with annotated safety labels and risk descriptions. Evaluation of 11 LLMs on R-Judge shows considerable room for enhancing the risk awareness of LLMs: The best-performing model, GPT-4o, achieves 74.42% while no other models significantly exceed the random. Moreover, we reveal that risk awareness in open agent scenarios is a multi-dimensional capability involving knowledge and reasoning, thus challenging for LLMs. With further experiments, we find that fine-tuning on safety judgment significantly improve model performance while straightforward prompting mechanisms fail. R-Judge is publicly available at https://github.com/Lordog/R-Judge.

---

### 33. Rethinking the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key?

**Authors:** Qineng Wang, Zihao Wang, Ying Su, et al.  
**Year:** 2024 | **Citations:** 127 | **Venue:** Annual Meeting of the Association for Computational Linguistics  
**Year Month:** [Feb 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/e89ee3f84f1f07229a7ba211bad3465d2c80a325](https://www.semanticscholar.org/paper/e89ee3f84f1f07229a7ba211bad3465d2c80a325)  
**arXiv:** [https://arxiv.org/abs/2402.18272](https://arxiv.org/abs/2402.18272)  

**Abstract:** Recent progress in LLMs discussion suggests that multi-agent discussion improves the reasoning abilities of LLMs. In this work, we reevaluate this claim through systematic experiments, where we propose a novel group discussion framework to enrich the set of discussion mechanisms. Interestingly, our results show that a single-agent LLM with strong prompts can achieve almost the same performance as the best existing discussion approach on a wide range of reasoning tasks and backbone LLMs. We observe that the multi-agent discussion performs better than a single agent only when there is no demonstration in the prompt. Further study reveals the common interaction mechanisms of LLMs during the discussion.

---

### 34. Trial and Error: Exploration-Based Trajectory Optimization for LLM Agents

**Authors:** Yifan Song, Da Yin, Xiang Yue, et al.  
**Year:** 2024 | **Citations:** 126 | **Venue:** Annual Meeting of the Association for Computational Linguistics  
**Year Month:** [Mar 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/f95da5b7be2fac2381eb5dfe26dc7dc5bc2d9a90](https://www.semanticscholar.org/paper/f95da5b7be2fac2381eb5dfe26dc7dc5bc2d9a90)  
**arXiv:** [https://arxiv.org/abs/2403.02502](https://arxiv.org/abs/2403.02502)  

**Abstract:** Large Language Models (LLMs) have become integral components in various autonomous agent systems. In this study, we present an exploration-based trajectory optimization approach, referred to as ETO. This learning method is designed to enhance the performance of open LLM agents. Contrary to previous studies that exclusively train on successful expert trajectories, our method allows agents to learn from their exploration failures. This leads to improved performance through an iterative optimization framework. During the exploration phase, the agent interacts with the environment while completing given tasks, gathering failure trajectories to create contrastive trajectory pairs. In the subsequent training phase, the agent utilizes these trajectory preference pairs to update its policy using contrastive learning methods like DPO. This iterative cycle of exploration and training fosters continued improvement in the agents. Our experiments on three complex tasks demonstrate that ETO consistently surpasses baseline performance by a large margin. Furthermore, an examination of task-solving efficiency and potential in scenarios lacking expert trajectory underscores the effectiveness of our approach.

---

### 35. AgentBoard: An Analytical Evaluation Board of Multi-turn LLM Agents

**Authors:** Chang Ma, Junlei Zhang, Zhihao Zhu, et al.  
**Year:** 2024 | **Citations:** 123 | **Venue:** Neural Information Processing Systems  
**Year Month:** [Jan 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/cf270bea2fba82bcff83f380c1f100d346b14ecf](https://www.semanticscholar.org/paper/cf270bea2fba82bcff83f380c1f100d346b14ecf)  
**arXiv:** [https://arxiv.org/abs/2401.13178](https://arxiv.org/abs/2401.13178)  

**Abstract:** Evaluating Large Language Models (LLMs) as general-purpose agents is essential for understanding their capabilities and facilitating their integration into practical applications. However, the evaluation process presents substantial challenges. A primary obstacle is the benchmarking of agent performance across diverse scenarios within a unified framework, especially in maintaining partially-observable environments and ensuring multi-round interactions. Moreover, current evaluation frameworks mostly focus on the final success rate, revealing few insights during the process and failing to provide a deep understanding of the model abilities. To address these challenges, we introduce AgentBoard, a pioneering comprehensive benchmark and accompanied open-source evaluation framework tailored to analytical evaluation of LLM agents. AgentBoard offers a fine-grained progress rate metric that captures incremental advancements as well as a comprehensive evaluation toolkit that features easy assessment of agents for multi-faceted analysis. This not only sheds light on the capabilities and limitations of LLM agents but also propels the interpretability of their performance to the forefront. Ultimately, AgentBoard serves as a step towards demystifying agent behaviors and accelerating the development of stronger LLM agents.

---

### 36. AutoDefense: Multi-Agent LLM Defense against Jailbreak Attacks

**Authors:** Yifan Zeng, Yiran Wu, Xiao Zhang, et al.  
**Year:** 2024 | **Citations:** 114 | **Venue:** arXiv.org  
**Year Month:** [Mar 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/8ba57771dd6345821a0cbe83c4c7eb50f66b7b65](https://www.semanticscholar.org/paper/8ba57771dd6345821a0cbe83c4c7eb50f66b7b65)  
**arXiv:** [https://arxiv.org/abs/2403.04783](https://arxiv.org/abs/2403.04783)  

**Abstract:** Despite extensive pre-training in moral alignment to prevent generating harmful information, large language models (LLMs) remain vulnerable to jailbreak attacks. In this paper, we propose AutoDefense, a multi-agent defense framework that filters harmful responses from LLMs. With the response-filtering mechanism, our framework is robust against different jailbreak attack prompts, and can be used to defend different victim models. AutoDefense assigns different roles to LLM agents and employs them to complete the defense task collaboratively. The division in tasks enhances the overall instruction-following of LLMs and enables the integration of other defense components as tools. With AutoDefense, small open-source LMs can serve as agents and defend larger models against jailbreak attacks. Our experiments show that AutoDefense can effectively defense against different jailbreak attacks, while maintaining the performance at normal user request. For example, we reduce the attack success rate on GPT-3.5 from 55.74% to 7.95% using LLaMA-2-13b with a 3-agent system. Our code and data are publicly available at https://github.com/XHMY/AutoDefense.

---

### 37. AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents

**Authors:** Maksym Andriushchenko, Alexandra Souly, Mateusz Dziemian, et al.  
**Year:** 2024 | **Citations:** 113 | **Venue:** International Conference on Learning Representations  
**Year Month:** [Oct 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/716c6f6a6e653bebfa676402b887fe2927e06c73](https://www.semanticscholar.org/paper/716c6f6a6e653bebfa676402b887fe2927e06c73)  
**arXiv:** [https://arxiv.org/abs/2410.09024](https://arxiv.org/abs/2410.09024)  

**Abstract:** The robustness of LLMs to jailbreak attacks, where users design prompts to circumvent safety measures and misuse model capabilities, has been studied primarily for LLMs acting as simple chatbots. Meanwhile, LLM agents -- which use external tools and can execute multi-stage tasks -- may pose a greater risk if misused, but their robustness remains underexplored. To facilitate research on LLM agent misuse, we propose a new benchmark called AgentHarm. The benchmark includes a diverse set of 110 explicitly malicious agent tasks (440 with augmentations), covering 11 harm categories including fraud, cybercrime, and harassment. In addition to measuring whether models refuse harmful agentic requests, scoring well on AgentHarm requires jailbroken agents to maintain their capabilities following an attack to complete a multi-step task. We evaluate a range of leading LLMs, and find (1) leading LLMs are surprisingly compliant with malicious agent requests without jailbreaking, (2) simple universal jailbreak templates can be adapted to effectively jailbreak agents, and (3) these jailbreaks enable coherent and malicious multi-step agent behavior and retain model capabilities. To enable simple and reliable evaluation of attacks and defenses for LLM-based agents, we publicly release AgentHarm at https://huggingface.co/datasets/ai-safety-institute/AgentHarm.

---

### 38. Tree Search for Language Model Agents

**Authors:** Jing Yu Koh, Stephen McAleer, Daniel Fried, et al.  
**Year:** 2024 | **Citations:** 110 | **Venue:** Trans. Mach. Learn. Res.  
**Year Month:** [Jul 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/9345e55a21959948499cee997522aa5eac7ed588](https://www.semanticscholar.org/paper/9345e55a21959948499cee997522aa5eac7ed588)  
**arXiv:** [https://arxiv.org/abs/2407.01476](https://arxiv.org/abs/2407.01476)  

**Abstract:** Autonomous agents powered by language models (LMs) have demonstrated promise in their ability to perform decision-making tasks such as web automation. However, a key limitation remains: LMs, primarily optimized for natural language understanding and generation, struggle with multi-step reasoning, planning, and using environmental feedback when attempting to solve realistic computer tasks. Towards addressing this, we propose an inference-time search algorithm for LM agents to explicitly perform exploration and multi-step planning in interactive web environments. Our approach is a form of best-first tree search that operates within the actual environment space, and is complementary with most existing state-of-the-art agents. It is the first tree search algorithm for LM agents that shows effectiveness on realistic web tasks. On the challenging VisualWebArena benchmark, applying our search algorithm on top of a GPT-4o agent yields a 39.7% relative increase in success rate compared to the same baseline without search, setting a state-of-the-art success rate of 26.4%. On WebArena, search also yields a 28.0% relative improvement over a baseline agent, setting a competitive success rate of 19.2%. Our experiments highlight the effectiveness of search for web agents, and we demonstrate that performance scales with increased test-time compute. We conduct a thorough analysis of our results to highlight improvements from search, limitations, and promising directions for future work. Our code and models are publicly released at https://jykoh.com/search-agents.

---

### 39. AI Agents vs. Agentic AI: A Conceptual Taxonomy, Applications and Challenges

**Authors:** Ranjan Sapkota, Konstantinos I. Roumeliotis, Manoj Karkee  
**Year:** 2025 | **Citations:** 109 | **Venue:** Information Fusion  
**Year Month:** [May 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/986e813f4c4f36786c3642cb9c8718586e47bdcf](https://www.semanticscholar.org/paper/986e813f4c4f36786c3642cb9c8718586e47bdcf)  
**arXiv:** [https://arxiv.org/abs/2505.10468](https://arxiv.org/abs/2505.10468)  
---

### 40. AI Agents Under Threat: A Survey of Key Security Challenges and Future Pathways

**Authors:** Zehang Deng, Yongjian Guo, Changzhou Han, et al.  
**Year:** 2024 | **Citations:** 107 | **Venue:** ACM Computing Surveys  
**Year Month:** [Jun 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/5aacf780ec16a29bdbe283a14f5a9e6b7e1f292d](https://www.semanticscholar.org/paper/5aacf780ec16a29bdbe283a14f5a9e6b7e1f292d)  
**arXiv:** [https://arxiv.org/abs/2406.02630](https://arxiv.org/abs/2406.02630)  

**Abstract:** An Artificial Intelligence (AI) agent is a software entity that autonomously performs tasks or makes decisions based on pre-defined objectives and data inputs. AI agents, capable of perceiving user inputs, reasoning and planning tasks, and executing actions, have seen remarkable advancements in algorithm development and task performance. However, the security challenges they pose remain under-explored and unresolved. This survey delves into the emerging security threats faced by AI agents, categorizing them into four critical knowledge gaps: unpredictability of multi-step user inputs, complexity in internal executions, variability of operational environments, and interactions with untrusted external entities. By systematically reviewing these threats, this article highlights both the progress made and the existing limitations in safeguarding AI agents. The insights provided aim to inspire further research into addressing the security threats associated with AI agents, thereby fostering the development of more robust and secure AI agent applications.

---

### 41. LLM Agents can Autonomously Exploit One-day Vulnerabilities

**Authors:** Richard Fang, R. Bindu, Akul Gupta, et al.  
**Year:** 2024 | **Citations:** 103 | **Venue:** arXiv.org  
**Year Month:** [Apr 2024]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/04bcd16b564e47b019880dd7db65f7fffae7e2a5](https://www.semanticscholar.org/paper/04bcd16b564e47b019880dd7db65f7fffae7e2a5)  
**arXiv:** [https://arxiv.org/abs/2404.08144](https://arxiv.org/abs/2404.08144)  

**Abstract:** LLMs have becoming increasingly powerful, both in their benign and malicious uses. With the increase in capabilities, researchers have been increasingly interested in their ability to exploit cybersecurity vulnerabilities. In particular, recent work has conducted preliminary studies on the ability of LLM agents to autonomously hack websites. However, these studies are limited to simple vulnerabilities. In this work, we show that LLM agents can autonomously exploit one-day vulnerabilities in real-world systems. To show this, we collected a dataset of 15 one-day vulnerabilities that include ones categorized as critical severity in the CVE description. When given the CVE description, GPT-4 is capable of exploiting 87% of these vulnerabilities compared to 0% for every other model we test (GPT-3.5, open-source LLMs) and open-source vulnerability scanners (ZAP and Metasploit). Fortunately, our GPT-4 agent requires the CVE description for high performance: without the description, GPT-4 can exploit only 7% of the vulnerabilities. Our findings raise questions around the widespread deployment of highly capable LLM agents.

---

### 42. RAGEN: Understanding Self-Evolution in LLM Agents via Multi-Turn Reinforcement Learning

**Authors:** Zihan Wang, Kangrui Wang, Qineng Wang, et al.  
**Year:** 2025 | **Citations:** 101 | **Venue:** arXiv.org  
**Year Month:** [Apr 2025]  
**Fields:** Computer Science  
**URL:** [https://www.semanticscholar.org/paper/1d03586baa32b3d6ff657a180053821543e11abb](https://www.semanticscholar.org/paper/1d03586baa32b3d6ff657a180053821543e11abb)  
**arXiv:** [https://arxiv.org/abs/2504.20073](https://arxiv.org/abs/2504.20073)  

**Abstract:** Training large language models (LLMs) as interactive agents presents unique challenges including long-horizon decision making and interacting with stochastic environment feedback. While reinforcement learning (RL) has enabled progress in static tasks, multi-turn agent RL training remains underexplored. We propose StarPO (State-Thinking-Actions-Reward Policy Optimization), a general framework for trajectory-level agent RL, and introduce RAGEN, a modular system for training and evaluating LLM agents. Our study on four stylized environments reveals three core findings. First, our agent RL training shows a recurring mode of Echo Trap where reward variance cliffs and gradient spikes; we address this with StarPO-S, a stabilized variant with trajectory filtering, critic incorporation, and gradient stabilization. Second, we find the shaping of RL rollouts would benefit from diverse initial states, medium interaction granularity and more frequent sampling. Third, we show that without fine-grained, reasoning-aware reward signals, agent reasoning hardly emerge through multi-turn RL and they may show shallow strategies or hallucinated thoughts. Code and environments are available at https://github.com/RAGEN-AI/RAGEN.

---

