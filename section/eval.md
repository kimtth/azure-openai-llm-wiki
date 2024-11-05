## **Section 12: Evaluating Large Language Models & LLMOps**

### **Evaluating Large Language Models**

- Awesome LLMs Evaluation Papers: Evaluating Large Language Models: A Comprehensive Survey [git](https://github.com/tjunlp-lab/Awesome-LLMs-Evaluation-Papers)
- Evaluation of Large Language Models: [A Survey on Evaluation of Large Language Models](https://arxiv.org/abs/2307.03109): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.03109)] [6 Jul 2023]
- [ChatGPT’s One-year Anniversary: Are Open-Source Large Language Models Catching up?](https://arxiv.org/abs/2311.16989): Open-Source LLMs vs. ChatGPT; Benchmarks and Performance of LLMs [28 Nov 2023]
- [Evaluation Papers for ChatGPT](https://github.com/THU-KEG/EvaluationPapers4ChatGPT) [28 Feb 2023]
- [MMLU (Massive Multi-task Language Understanding)](https://arxiv.org/abs/2009.03300): LLM performance across 57 tasks including elementary mathematics, US history, computer science, law, and more. [7 Sep 2020]
- [BIG-bench](https://arxiv.org/abs/2206.04615): Consists of 204 evaluations, contributed by over 450 authors, that span a range of topics from science to social reasoning. The bottom-up approach; anyone can submit an evaluation task. [git](https://github.com/google/BIG-bench) [9 Jun 2022]
- [HELM](https://arxiv.org/abs/2211.09110): Evaluation scenarios like reasoning and disinformation using standardized metrics like accuracy, calibration, robustness, and fairness. The top-down approach; experts curate and decide what tasks to evaluate models on. [git](https://github.com/stanford-crfm/helm) [16 Nov 2022]
- [HumanEval](https://arxiv.org/abs/2107.03374): Hand-Written Evaluation Set for Code Generation Bechmark. 164 Human written Programming Problems. [ref](https://paperswithcode.com/task/code-generation) / [git](https://github.com/openai/human-eval) [7 Jul 2021]
- [Prometheus: Inducing Fine-grained Evaluation Capability in Language Models](https://arxiv.org/abs/2310.08491): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.08491)]: We utilize the FEEDBACK COLLECTION, a novel dataset, to train PROMETHEUS, an open-source large language model with 13 billion parameters, designed specifically for evaluation tasks. [12 Oct 2023]
- [LLM Model Evals vs LLM Task Evals](https://x.com/aparnadhinak/status/1752763354320404488)
: `Model Evals` are really for people who are building or fine-tuning an LLM. vs The best LLM application builders are using `Task evals`. It's a tool to help builders build. [Feb 2024]
- [LLMPerf Leaderboard](https://github.com/ray-project/llmperf-leaderboard): Evaulation the performance of LLM APIs. [Dec 2023]
- [Artificial Analysis LLM Performance Leaderboard](https://huggingface.co/spaces/ArtificialAnalysis/LLM-Performance-Leaderboard): Performance benchmarks & pricing across API providers of LLMs
- [LLM-as-a-Judge](https://cameronrwolfe.substack.com/i/141159804/practical-takeaways): LLM-as-a-Judge offers a quick, cost-effective way to develop models aligned with human preferences and is easy to implement with just a prompt, but should be complemented by human evaluation to address biases.  [Jul 2024]
- [Can Large Language Models Be an Alternative to Human Evaluations?](https://arxiv.org/abs/2305.01937) [3 May 2023]
- [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](https://eugeneyan.com/writing/llm-evaluators/): Key considerations and Use cases when using LLM-evaluators [Aug 2024]
- [LightEval](https://github.com/huggingface/lighteval): a lightweight LLM evaluation suite that Hugging Face has been using internally [Jan 2024]
- [OpenAI MLE-bench](https://arxiv.org/abs/2410.07095): A benchmark for measuring the performance of AI agents on ML tasks using Kaggle. [git](https://github.com/openai/mle-bench) [9 Oct 2024] > Agent Framework used in MLE-bench, `GPT-4o (AIDE) achieves more medals on average than both MLAB and OpenHands (8.7% vs. 0.8% and 4.4% respectively)` [x-ref](agent_app.md/#agent-applications-and-libraries)
- [Korean SAT LLM Leaderboard](https://github.com/minsing-jin/Korean-SAT-LLM-Leaderboard): Benchmarking 10 years of Korean CSAT (College Scholastic Ability Test) exams [Oct 2024]

### **LLM Evalution Benchmarks**

  <details open>
  <summary>Expand</summary>

  #### Language Understanding and QA

  1. [MMLU (Massive Multitask Language Understanding)](https://github.com/hendrycks/test): Over 15,000 questions across 57 diverse tasks. [Published in 2021]
  1. [TruthfulQA](https://huggingface.co/datasets/truthful_qa): Truthfulness. [Published in 2022]
  1. [BigBench](https://github.com/google/BIG-bench): 204 tasks. Predicting future potential [Published in 2023]
  1. [GLUE](https://gluebenchmark.com/leaderboard) & [SuperGLUE](https://super.gluebenchmark.com/leaderboard/): GLUE (General Language Understanding Evaluation)

  #### Coding

  1. [HumanEval](https://github.com/openai/human-eval): Challenges coding skills. [Published in 2021]
  1. [CodeXGLUE](https://github.com/microsoft/CodeXGLUE): Programming tasks.
  1. [SWE-bench](https://www.swebench.com/): Software Engineering Benchmark. Real-world software issues sourced from GitHub.
  1. [MBPP](https://github.com/google-research/google-research/tree/master/mbpp): Mostly Basic Python Programming. [Published in 2021]

  #### Chatbot Assistance

  1. [Chatbot Arena](https://huggingface.co/datasets/lmsys/chatbot_arena_conversations): Human-ranked ELO ranking.
  1. [MT Bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge): Multi-turn open-ended questions
    - [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) [9 Jun 2023]

  #### Reasoning

  1. [HellaSwag](https://github.com/rowanz/hellaswag): Commonsense reasoning. [Published in 2019]
  1. [ARC (AI2 Reasoning Challenge)](https://github.com/fchollet/ARC): Measures general fluid intelligence.
  1. [DROP](https://huggingface.co/datasets/drop): Evaluates discrete reasoning.
  1. [LogicQA](https://github.com/lgw863/LogiQA-dataset): Evaluates logical reasoning skills.

  #### Translation

  1. [WMT](https://huggingface.co/wmt): Evaluates translation skills.

  #### Math

  1. [MATH](https://github.com/hendrycks/math): Tests ability to solve math problems. [Published in 2021]
  1. [GSM8K](https://github.com/openai/grade-school-math): Arithmetic Reasoning. [Published in 2021]

  </details>

### **Evaluation metrics**

  1. Automated evaluation of LLMs

  - n-gram based metrics: Evaluates the model using n-gram statistics and F1 score. ROUGE, BLEU, and METEOR are used for summarization and translation tasks.
  - Probabilistic model evaluation metrics: Evaluates the model using the predictive performance of probability models. Perplexity.
  - Embedding based metrics: Evaluates the model using semantic similarity of embeddings. Ada Similarity and BERTScore are used.

    <details open>
    <summary>Expand</summary>

      - ROUGE (Recall-Oriented Understudy for Gisting Evaluation): The metrics compare an automatically produced summary or translation against a reference or a set of references (human-produced) summary or translation. It includes several measures such as:

        1. ROUGE-N: Overlap of n-grams between the system and reference summaries.
        2. ROUGE-L: Longest Common Subsequence (LCS) based statistics.
        3. ROUGE-W: Weighted LCS-based statistics that favor consecutive LCSes.
        4. ROUGE-S: Skip-bigram based co-occurrence statistics.
        5. ROUGE-SU: Skip-bigram plus unigram-based co-occurrence statistics1.

      - n-gram: An n-gram is a contiguous sequence of n items from a given sample of text or speech. For example, in the sentence “I love AI”, the unigrams (1-gram) are “I”, “love”, “AI”; the bigrams (2-gram) are “I love”, “love AI”; and the trigram (3-gram) is “I love AI”.

      - BLEU: BLEU’s output is always a number between 0 and 1. An algorithm for evaluating the quality of machine-translated text. The closer a machine translation is to a professional human translation, the better it is.

      - BERTScore: A metric that leverages pre-trained contextual embeddings from BERT for text generation tasks. It combines precision and recall values.

      - Perplexity: A measure of a model's predictive performance, with lower values indicating better prediction.
      - METEOR: An n-gram based metric for machine translation, considering precision, recall, and semantic similarity.
    </details>

  2. Human evaluation of LLMs (possibly Automate by LLM-based metrics): Evaluate the model’s performance on NLU and NLG tasks. It includes evaluations of relevance, fluency, coherence, and groundedness.

  3. Built-in evaluation methods in Prompt flow: [ref](https://qiita.com/nohanaga/items/b68bf5a65142c5af7969) [Aug 2023] / [ref](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/how-to-bulk-test-evaluate-flow)

### **LLMOps: Large Language Model Operations**

- [OpenAI Evals](https://github.com/openai/evals): A framework for evaluating large language models (LLMs) [Mar 2023]
- [promptfoo](https://github.com/promptfoo/promptfoo): Test your prompts. Evaluate and compare LLM outputs, catch regressions, and improve prompt quality. [Apr 2023]
- PromptTools: Open-source tools for prompt testing [git](https://github.com/hegelai/prompttools/) [Jun 2023]
- [TruLens](https://github.com/truera/trulens): Instrumentation and evaluation tools for large language model (LLM) based applications. [Nov 2020]
- [Pezzo](https://github.com/pezzolabs/pezzo): Open-source, developer-first LLMOps platform [May 2023]
- [Giskard]((https://github.com/Giskard-AI/giskard)): The testing framework for ML models, from tabular to LLMs [Mar 2022]
- Azure Machine Learning studio Model Data Collector: Collect production data, analyze key safety and quality evaluation metrics on a recurring basis, receive timely alerts about critical issues, and visualize the results. [ref](https://learn.microsoft.com/en-us/azure/machine-learning/how-to-collect-production-data?view=azureml-api-2&tabs=azure-cli)
- [Azure ML Prompt flow](https://microsoft.github.io/promptflow/index.html): A set of LLMOps tools designed to facilitate the creation of LLM-based AI applications [Sep 2023] > [How to Evaluate & Upgrade Model Versions in the Azure OpenAI Service](https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/how-to-evaluate-amp-upgrade-model-versions-in-the-azure-openai/ba-p/4218880) [14 Aug 2024]
- [Ragas](https://github.com/explodinggradients/ragas): Evaluation framework for your Retrieval Augmented Generation (RAG) [May 2023]
- [DeepEval](https://github.com/confident-ai/deepeval): LLM evaluation framework. similar to Pytest but specialized for unit testing LLM outputs. [Aug 2023]
- [traceloop openllmetry](https://github.com/traceloop/openllmetry): Quality monitoring for your LLM applications. [Sep 2023]
- [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness): Over 60 standard academic benchmarks for LLMs. A framework for few-shot evaluation. [Aug 2020]
- [Machine Learning Operations (MLOps) For Beginners](https://towardsdatascience.com/machine-learning-operations-mlops-for-beginners-a5686bfe02b2): DVC (Data Version Control), MLflow, Evidently AI (Monitor a model). Insurance Cross Sell Prediction [git](https://github.com/prsdm/mlops-project) [29 Aug 2024]
- [Langfuse](https://langfuse.com): [git](https://github.com/langfuse/langfuse) LLMOps platform that helps teams to collaboratively monitor, evaluate and debug AI applications. [Nov 2024]

### **Challenges in evaluating AI systems**

1. [Pretraining on the Test Set Is All You Need](https://arxiv.org/abs/2309.08632): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.08632)]
   - On that note, in the satirical Pretraining on the Test Set Is All You Need paper, the author trains a small 1M parameter LLM that outperforms all other models, including the 1.3B phi-1.5 model. This is achieved by training the model on all downstream academic benchmarks. It appears to be a subtle criticism underlining how easily benchmarks can be "cheated" intentionally or unintentionally (due to data contamination). [cite](https://twitter.com/rasbt) [13 Sep 2023]
2. [Challenges in evaluating AI systems](https://www.anthropic.com/index/evaluating-ai-systems): The challenges and limitations of various methods for evaluating AI systems, such as multiple-choice tests, human evaluations, red teaming, model-generated evaluations, and third-party audits. [doc](../files/eval-ai-anthropic.pdf) [4 Oct 2023]
3. [Your AI Product Needs Evals](https://hamel.dev/blog/posts/evals/) [29 Mar 2024] / [How to Evaluate LLM Applications: The Complete Guide](https://www.confident-ai.com/blog/how-to-evaluate-llm-applications) [7 Nov 2023]