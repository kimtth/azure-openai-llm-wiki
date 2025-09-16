## **Evaluating Large Language Models & LLMOps**

### **Evaluating Large Language Models**

- [Artificial Analysis LLM Performance Leaderboard🤗](https://huggingface.co/spaces/ArtificialAnalysis/LLM-Performance-Leaderboard): Performance benchmarks & pricing across API providers of LLMs
- Awesome LLMs Evaluation Papers: Evaluating Large Language Models: A Comprehensive Survey [🐙](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers) [Oct 2023]
 ![**github stars**](https://img.shields.io/github/stars/tjunlp-lab/Awesome-LLMs-Evaluation-Papers?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Can Large Language Models Be an Alternative to Human Evaluations?📑](https://alphaxiv.org/abs/2305.01937) [3 May 2023]
- [ChatGPT’s One-year Anniversary: Are Open-Source Large Language Models Catching up?📑](https://alphaxiv.org/abs/2311.16989): Open-Source LLMs vs. ChatGPT; Benchmarks and Performance of LLMs [28 Nov 2023]
- Evaluation of Large Language Models: [A Survey on Evaluation of Large Language Models📑](https://alphaxiv.org/abs/2307.03109): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.03109)] [6 Jul 2023]
- [Evaluation Papers for ChatGPT🐙](https://github.com/THU-KEG/EvaluationPapers4ChatGPT) [28 Feb 2023]
 ![**github stars**](https://img.shields.io/github/stars/THU-KEG/EvaluationPapers4ChatGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](https://eugeneyan.com/writing/llm-evaluators/):💡Key considerations and Use cases when using LLM-evaluators [Aug 2024]
- [LightEval🐙](https://github.com/huggingface/lighteval):🤗 a lightweight LLM evaluation suite that Hugging Face has been using internally [Jan 2024]
 ![**github stars**](https://img.shields.io/github/stars/huggingface/lighteval?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLM Model Evals vs LLM Task Evals](https://x.com/aparnadhinak/status/1752763354320404488)
: `Model Evals` are really for people who are building or fine-tuning an LLM. vs The best LLM application builders are using `Task evals`. It's a tool to help builders build. [Feb 2024]
- [LLMPerf Leaderboard🐙](https://github.com/ray-project/llmperf-leaderboard): Evaulation the performance of LLM APIs. [Dec 2023]
 ![**github stars**](https://img.shields.io/github/stars/ray-project/llmperf-leaderboard?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLM-as-a-Judge](https://cameronrwolfe.substack.com/i/141159804/practical-takeaways):💡LLM-as-a-Judge offers a quick, cost-effective way to develop models aligned with human preferences and is easy to implement with just a prompt, but should be complemented by human evaluation to address biases.  [Jul 2024]
- [Prometheus: Inducing Fine-grained Evaluation Capability in Language Models📑](https://alphaxiv.org/abs/2310.08491): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.08491)]: We utilize the FEEDBACK COLLECTION, a novel dataset, to train PROMETHEUS, an open-source large language model with 13 billion parameters, designed specifically for evaluation tasks. [12 Oct 2023]
- [The Leaderboard Illusion📑](https://alphaxiv.org/abs/2504.20879):💡Chatbot Arena's benchmarking is skewed by selective disclosures, private testing advantages, and data access asymmetries, leading to overfitting and unfair model rankings. [29 Apr 2025]

### **LLM Evalution Benchmarks**

#### Language Understanding and QA

1. [BIG-bench📑](https://alphaxiv.org/abs/2206.04615): Consists of 204 evaluations, contributed by over 450 authors, that span a range of topics from science to social reasoning. The bottom-up approach; anyone can submit an evaluation task. [🐙](https://github.com/google/BIG-bench) [9 Jun 2022]
![**github stars**](https://img.shields.io/github/stars/google/BIG-bench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [BigBench🐙](https://github.com/google/BIG-bench): 204 tasks. Predicting future potential [Published in 2023]
![**github stars**](https://img.shields.io/github/stars/google/BIG-bench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [GLUE](https://gluebenchmark.com/leaderboard) & [SuperGLUE](https://super.gluebenchmark.com/leaderboard/): GLUE (General Language Understanding Evaluation)
1. [HELM📑](https://alphaxiv.org/abs/2211.09110): Evaluation scenarios like reasoning and disinformation using standardized metrics like accuracy, calibration, robustness, and fairness. The top-down approach; experts curate and decide what tasks to evaluate models on. [🐙](https://github.com/stanford-crfm/helm) [16 Nov 2022] ![**github stars**](https://img.shields.io/github/stars/stanford-crfm/helm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [HumanEval📑](https://alphaxiv.org/abs/2107.03374): Hand-Written Evaluation Set for Code Generation Bechmark. 164 Human written Programming Problems. [✍️](https://paperswithcode.com/task/code-generation) / [🐙](https://github.com/openai/human-eval) [7 Jul 2021]
![**github stars**](https://img.shields.io/github/stars/openai/human-eval?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MMLU (Massive Multitask Language Understanding)🐙](https://github.com/hendrycks/test): Over 15,000 questions across 57 diverse tasks. [Published in 2021]
![**github stars**](https://img.shields.io/github/stars/hendrycks/test?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MMLU (Massive Multi-task Language Understanding)📑](https://alphaxiv.org/abs/2009.03300): LLM performance across 57 tasks including elementary mathematics, US history, computer science, law, and more. [7 Sep 2020]
1. [TruthfulQA🤗](https://huggingface.co/datasets/truthful_qa): Truthfulness. [Published in 2022]

#### Coding

1. [CodeXGLUE🐙](https://github.com/microsoft/CodeXGLUE): Programming tasks.
![**github stars**](https://img.shields.io/github/stars/microsoft/CodeXGLUE?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [HumanEval🐙](https://github.com/openai/human-eval): Challenges coding skills. [Published in 2021]
![**github stars**](https://img.shields.io/github/stars/openai/human-eval?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MBPP🐙](https://github.com/google-research/google-research/tree/master/mbpp): Mostly Basic Python Programming. [Published in 2021]
1. [SWE-bench](https://www.swebench.com/): Software Engineering Benchmark. Real-world software issues sourced from GitHub.
1. [SWE-Lancer✍️](https://openai.com/index/swe-lancer/): OpenAI. full engineering stack, from UI/UX to systems design, and include a range of task types, from $50 bug fixes to $32,000 feature implementations. [18 Feb 2025]

#### Chatbot Assistance

1. [Chatbot Arena🤗](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations): Human-ranked ELO ranking.
1. [MT Bench🐙](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge): Multi-turn open-ended questions
  - [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena📑](https://alphaxiv.org/abs/2306.05685) [9 Jun 2023]

#### Reasoning

1. [ARC (AI2 Reasoning Challenge)🐙](https://github.com/fchollet/ARC): Measures general fluid intelligence.
![**github stars**](https://img.shields.io/github/stars/fchollet/ARC?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [DROP🤗](https://huggingface.co/datasets/drop): Evaluates discrete reasoning.
1. [HellaSwag🐙](https://github.com/rowanz/hellaswag): Commonsense reasoning. [Published in 2019]
![**github stars**](https://img.shields.io/github/stars/rowanz/hellaswag?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [LogicQA🐙](https://github.com/lgw863/LogiQA-dataset): Evaluates logical reasoning skills.
![**github stars**](https://img.shields.io/github/stars/lgw863/LogiQA-dataset?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### Translation

1. [WMT🤗](https://huggingface.co/wmt): Evaluates translation skills.

#### Math

1. [GSM8K🐙](https://github.com/openai/grade-school-math): Arithmetic Reasoning. [Published in 2021]
![**github stars**](https://img.shields.io/github/stars/openai/grade-school-math?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [MATH🐙](https://github.com/hendrycks/math): Tests ability to solve math problems. [Published in 2021]
![**github stars**](https://img.shields.io/github/stars/hendrycks/math?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

 #### Other Benchmarks

- [Comprehensive and Practical Evaluation of Retrieval-Augmented Generation Systems for Medical Question Answering📑](https://alphaxiv.org/abs/2411.09213) [14 Nov 2024]
- [Korean SAT LLM Leaderboard🐙](https://github.com/Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard): Benchmarking 10 years of Korean CSAT (College Scholastic Ability Test) exams [Oct 2024]
![**github stars**](https://img.shields.io/github/stars/Marker-Inc-Korea/Korean-SAT-LLM-Leaderboard?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [OpenAI BrowseComp✍️](https://openai.com/index/browsecomp/): A benchmark assessing AI agents’ ability to use web browsing tools to complete tasks requiring up-to-date information, reasoning, and navigation skills. Boost from tools + reasoning. Human trainer success ratio = 29.2% × 86.4% ≈ 25.2% [10 Apr 2025]
- [OpenAI MLE-bench📑](https://alphaxiv.org/abs/2410.07095): A benchmark for measuring the performance of AI agents on ML tasks using Kaggle. [🐙](https://github.com/openai/mle-bench) [9 Oct 2024] > Agent Framework used in MLE-bench, `GPT-4o (AIDE) achieves more medals on average than both MLAB and OpenHands (8.7% vs. 0.8% and 4.4% respectively)` [🔗](agent.md/#agent-applications-and-libraries)
![**github stars**](https://img.shields.io/github/stars/openai/mle-bench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [OpenAI Paper Bench✍️](https://openai.com/index/paperbench/): a benchmark evaluating the ability of AI agents to replicate state-of-the-art AI research. [🐙](https://github.com/openai/preparedness/tree/main/project/paperbench) [2 Apr 2025]
- [OpenAI SimpleQA Benchmark✍️](https://openai.com/index/introducing-simpleqa/): SimpleQA, a factuality benchmark for short fact-seeking queries, narrows its scope to simplify factuality measurement. [🐙](https://github.com/openai/simple-evals) [30 Oct 2024] ![**github stars**](https://img.shields.io/github/stars/openai/simple-evals?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
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

- [30 requirements for an MLOps environment🗣️](https://x.com/KirkDBorne/status/1679952405805555713): Kirk Borne twitter [15 Jul 2023]
- [agenta🐙](https://github.com/Agenta-AI/agenta): OSS LLMOps workflow: building (LLM playground, evaluation), deploying (prompt and configuration management), and monitoring (LLM observability and tracing). [Jun 2023] ![**github stars**](https://img.shields.io/github/stars/Agenta-AI/agenta?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure ML Prompt flow](https://microsoft.github.io/promptflow/index.html): A set of LLMOps tools designed to facilitate the creation of LLM-based AI applications [Sep 2023] > [How to Evaluate & Upgrade Model Versions in the Azure OpenAI Service✍️](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/how-to-evaluate-amp-upgrade-model-versions-in-the-azure-openai/ba-p/4218880) [14 Aug 2024]
- Azure Machine Learning studio Model Data Collector: Collect production data, analyze key safety and quality evaluation metrics on a recurring basis, receive timely alerts about critical issues, and visualize the results. [✍️](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-collect-production-data?view=azureml-api-2&tabs=azure-cli) [Apr 2024]
- [circuit‑tracer🐙](https://github.com/safety-research/circuit-tracer): Anthrophic. Tool for finding and visualizing circuits within large language models. a circuit is a minimal, causal computation pathway inside a transformer model that shows how internal features lead to a specific output. [May 2025] ![**github stars**](https://img.shields.io/github/stars/safety-research/circuit-tracer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [DeepEval🐙](https://github.com/confident-ai/deepeval): LLM evaluation framework. similar to Pytest but specialized for unit testing LLM outputs. [Aug 2023]
 ![**github stars**](https://img.shields.io/github/stars/confident-ai/deepeval?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Economics of Hosting Open Source LLMs✍️](https://towardsdatascience.com/economics-of-hosting-open-source-llms-17b4ec4e7691): Comparison of cloud vendors such as AWS, Modal, BentoML, Replicate, Hugging Face Endpoints, and Beam, using metrics like processing time, cold start latency, and costs associated with CPU, memory, and GPU usage. [🐙](https://github.com/ilsilfverskiold/Awesome-LLM-Resources-List) [13 Nov 2024]
- [Giskard🐙](https://github.com/Giskard-AI/giskard): The testing framework for ML models, from tabular to LLMs [Mar 2022] ![**github stars**](https://img.shields.io/github/stars/Giskard-AI/giskard?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Langfuse](https://langfuse.com): [🐙](https://github.com/langfuse/langfuse) LLMOps platform that helps teams to collaboratively monitor, evaluate and debug AI applications. [May 2023] 
 ![**github stars**](https://img.shields.io/github/stars/langfuse/langfuse?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Language Model Evaluation Harness🐙](https://github.com/EleutherAI/lm-evaluation-harness):💡Over 60 standard academic benchmarks for LLMs. A framework for few-shot evaluation. Hugginface uses this for [Open LLM Leaderboard🤗](https://huggingface.co/open-llm-leaderboard) [Aug 2020]
 ![**github stars**](https://img.shields.io/github/stars/EleutherAI/lm-evaluation-harness?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LangWatch scenario🐙](https://github.com/langwatch/scenario):💡LangWatch Agentic testing for agentic codebases. Simulating agentic communication using autopilot [Apr 2025] ![**github stars**](https://img.shields.io/github/stars/langwatch/scenario?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLMOps Database](https://www.zenml.io/llmops-database): A curated knowledge base of real-world LLMOps implementations.
- [Maxim AI](https://getmaxim.ai): [🐙](https://github.com/maximhq) End-to-end simulation, evaluation, and observability plaform, helping teams ship their AI agents reliably and >5x faster. [Dec 2023]
- [Machine Learning Operations (MLOps) For Beginners✍️](https://towardsdatascience.com/machine-learning-operations-mlops-for-beginners-a5686bfe02b2): DVC (Data Version Control), MLflow, Evidently AI (Monitor a model). Insurance Cross Sell Prediction [🐙](https://github.com/prsdm/mlops-project) [29 Aug 2024]
 ![**github stars**](https://img.shields.io/github/stars/prsdm/mlops-project?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [OpenAI Evals🐙](https://github.com/openai/evals): A framework for evaluating large language models (LLMs) [Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/openai/evals?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Opik🐙](https://github.com/comet-ml/opik): an open-source platform for evaluating, testing and monitoring LLM applications. Built by Comet. [2 Sep 2024] ![**github stars**](https://img.shields.io/github/stars/comet-ml/opik?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Pezzo🐙](https://github.com/pezzolabs/pezzo): Open-source, developer-first LLMOps platform [May 2023]
 ![**github stars**](https://img.shields.io/github/stars/pezzolabs/pezzo?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [promptfoo🐙](https://github.com/promptfoo/promptfoo): Test your prompts. Evaluate and compare LLM outputs, catch regressions, and improve prompt quality. [Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/promptfoo/promptfoo?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [PromptTools🐙](https://github.com/hegelai/prompttools/): Open-source tools for prompt testing [Jun 2023] ![**github stars**](https://img.shields.io/github/stars/hegelai/prompttools?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Ragas🐙](https://github.com/explodinggradients/ragas): Evaluation framework for your Retrieval Augmented Generation (RAG) [May 2023]
 ![**github stars**](https://img.shields.io/github/stars/explodinggradients/ragas?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [traceloop openllmetry🐙](https://github.com/traceloop/openllmetry): Quality monitoring for your LLM applications. [Sep 2023]
 ![**github stars**](https://img.shields.io/github/stars/traceloop/openllmetry?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [TruLens🐙](https://github.com/truera/trulens): Instrumentation and evaluation tools for large language model (LLM) based applications. [Nov 2020]
 ![**github stars**](https://img.shields.io/github/stars/truera/trulens?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **Challenges in evaluating AI systems**

1. [Challenges in evaluating AI systems✍️](https://www.anthropic.com/index/evaluating-ai-systems): The challenges and limitations of various methods for evaluating AI systems, such as multiple-choice tests, human evaluations, red teaming, model-generated evaluations, and third-party audits. [🗄️](../files/eval-ai-anthropic.pdf) [4 Oct 2023]
1. [Pretraining on the Test Set Is All You Need📑](https://alphaxiv.org/abs/2309.08632): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.08632)]
   - On that note, in the satirical Pretraining on the Test Set Is All You Need paper, the author trains a small 1M parameter LLM that outperforms all other models, including the 1.3B phi-1.5 model. This is achieved by training the model on all downstream academic benchmarks. It appears to be a subtle criticism underlining how easily benchmarks can be "cheated" intentionally or unintentionally (due to data contamination). [🗣️](https://twitter.com/rasbt) [13 Sep 2023]
1. [Sakana AI claimed 100x faster AI training, but a bug caused a 3x slowdown](https://techcrunch.com/2025/02/21/sakana-walks-back-claims-that-its-ai-can-dramatically-speed-up-model-training/): Sakana’s AI resulted in a 3x slowdown — not a speedup. [21 Feb 2025]
1. [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) [29 Mar 2024] / [How to Evaluate LLM Applications: The Complete Guide](https://www.confident-ai.com/blog/how-to-evaluate-llm-applications) [7 Nov 2023]