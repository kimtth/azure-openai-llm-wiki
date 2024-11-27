# Azure OpenAI + LLMs (Large Language Models) 

![Static Badge](https://img.shields.io/badge/llm-azure_openai-blue?style=flat-square) <a href="https://awesome.re"><img src="https://awesome.re/badge-flat2.svg" alt="Awesome"></a> ![GitHub Created At](https://img.shields.io/github/created-at/kimtth/awesome-azure-openai-llm?style=flat-square)

This repository contains references to Azure OpenAI, Large Language Models (LLM), and related services and libraries. It follows a similar approach to the ‘Awesome-list’.

🔹Brief each item on a few lines as possible. <br/>
🔹The dates are determined by the date of the commit history, the Article published date, or the Paper issued date (v1). <br/>
🔹Capturing a chronicle and key terms of that rapidly advancing field. <br/>
🔹Disclaimer: Please be aware that some content may be outdated.

## What's the difference between Azure OpenAI and OpenAI?

1. OpenAI offers the latest features and models, while Azure OpenAI provides a reliable, secure, and compliant environment with seamless integration into other Azure services.
2. Azure OpenAI supports `private networking`, `role-based authentication`, and `responsible AI content filtering`.
3. Azure OpenAI does not use user input as training data for other customers. [Data, privacy, and security for Azure OpenAI](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy). Azure OpenAI does not share user data, including prompts and responses, with OpenAI.

- [What is Azure OpenAI Service?](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview)
- [Open AI Models](https://platform.openai.com/docs/models)
- [Abuse Monitoring](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy): To detect and mitigate abuse, Azure OpenAI stores all prompts and generated content securely for up to thirty (30) days. (No prompts or completions are stored if the customer chooses to turn off abuse monitoring.)

## Table of contents

- **Section 1** 🎯: [RAG](section/rag.md/#section-1-rag-llamaindex-and-vector-storage)
  - [RAG (Retrieval-Augmented Generation)](section/rag.md/#what-is-the-rag-retrieval-augmented-generation)
  - [RAG Design & Application](section/rag.md/#advanced-rag)
  - [LlamaIndex](section/rag.md/#llamaindex)
  - [Vector DB](section/rag.md/#vector-database-comparison)
- **Section 2** 🪟: [Azure OpenAI](section/aoai.md/#section-2--azure-openai-and-reference-architecture)
  - [Microsoft LLM Framework](section/aoai.md/#microsoft-azure-openai-relevant-llm-framework)
  - [Copilot Products & Azure OpenAI Service](section/aoai.md/#copilot-products)
  - [Azure Reference Architecture](section/aoai.md/#azure-reference-architectures)
- **Section 3** 🏗️: [Semantic Kernel & DSPy](section/sk_dspy.md/#section-3--microsoft-semantic-kernel-and-stanford-nlp-dspy)
  - [Semantic Kernel](section/sk_dspy.md/#semantic-kernel): Micro-orchestration
  - [DSPy](section/sk_dspy.md/#dspy): Optimizer frameworks
- **Section 4** 🛠️: [LangChain](section/langchain.md/#section-4--langchain-features-usage-and-comparisons)
  - [LangChain Features](section/langchain.md/#langchain-feature-matrix--cheetsheet): Macro & Micro-orchestration
  - [LangChain Agent & Criticism](section/langchain.md/#langchain-chain-type-chains--summarizer)
  - [LangChain vs Competitors](section/langchain.md/#langchain-vs-competitors)
- **Section 5** 🧠: [Prompting & Finetuning](section/prompt_ft.md/#section-5-prompt-engineering-finetuning-and-visual-prompts)
  - [Prompt Engineering](section/prompt_ft.md/#prompt-engineering)
  - [Finetuning](section/prompt_ft.md/#finetuning): PEFT (e.g., LoRA), RLHF, SFT
  - [Quantization & Optimization](section/prompt_ft.md/#quantization-techniques)
  - [Other Techniques](section/prompt_ft.md/#other-techniques-and-llm-patterns): e.g., MoE
  - [Visual Prompting](section/prompt_ft.md/#visual-prompting--visual-grounding)
- **Section 6** 🏄‍♂️: [Challenges & Abilities](section/chab.md/#section-6--large-language-model-challenges-and-solutions)
  - [AGI Discussion](section/chab.md/#agi-discussion)
  - [OpenAI Products & Roadmap](section/chab.md/#openais-roadmap-and-products)
  - [Context Constraints](section/chab.md/#context-constraints): e.g., RoPE
  - [Trust & Safety](section/chab.md/#trustworthy-safe-and-secure-llm)
  - [LLM Abilities](section/chab.md/#large-language-model-is-abilities)
- **Section 7** 🌍: [LLM Landscape](section/llm.md/#section-7--large-language-model-landscape)
  - [LLM Taxonomy](section/llm.md/#large-language-models-in-2023)
  - [Open-Source LLMs](section/llm.md/#open-source-large-language-models)
  - [Domain-Specific LLMs](section/llm.md/#llm-for-domain-specific): e.g., Software development
  - [Multimodal LLMs](section/llm.md/#mllm-multimodal-large-language-model)
  - [Generative AI Landscape](section/llm.md/#generative-ai-landscape)
- **Section 8** 📚: [Surveys & References](section/survey_ref.md/#section-8-survey-and-reference)
  - [LLM Surveys](section/survey_ref.md/#survey-on-large-language-models)
  - [Building LLMs](section/survey_ref.md/#build-an-llms-from-scratch-picogpt-and-lit-gpt): from scratch
  - [LLMs for Korean & Japanese](section/survey_ref.md/#llm-materials-for-east-asian-languages)
- **Section 9** 🤖: [Agents & Applications](section/agent_app.md/#section-9-applications-and-frameworks)
  - [LLM Frameworks & Applications](section/agent_app.md/#applications-frameworks-and-user-interface-uiux)
  - [Agent Design Patterns](section/agent_app.md/#agent-design-patterns)
  - [Agent Frameworks & Applications](section/agent_app.md/#agent-framework)
  - [Caching, UX, Proposals & Other topics](section/agent_app.md/#caching)
  - [LLMs for Robotics](section/agent_app.md/#llm-for-robotics-bridging-ai-and-robotics) / [Awesome demo](section/agent_app.md/#awesome-demo)
- **Section 10** 🧰: [AI Tools & Extensions](section/ai_tool.md/#section-10-general-ai-tools-and-extensions)
  - [AI Tools & Extensions](section/ai_tool.md/#section-10-general-ai-tools-and-extensions)
- **Section 11** 📊: [Datasets](section/dataset.md/#section-11-datasets-for-llm-training)
  - [LLM Training Datasets](section/dataset.md/#section-11-datasets-for-llm-training)
- **Section 12** 📝: [Evaluations](section/eval.md/#section-12-evaluating-large-language-models--llmops)
  - [LLM Evaluation & LLMOps](section/eval.md/#section-12-evaluating-large-language-models--llmops)
- **Contributors** 👀: 
  - [Contributors](#contributors)
- **Symbols** 🔑:
  - `ref`: external URL
  - `doc`: archived doc
  - `cite`: the source of comments
  - `cnt`: number of citations
  - `git`: GitHub link
  - `x-ref`: Cross reference
  - 📺: youtube or video

## **Contributors**

<a href="https://github.com/kimtth/awesome-azure-openai-llm/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kimtth/awesome-azure-openai-llm" />
</a>

ⓒ `https://github.com/kimtth` all rights reserved.