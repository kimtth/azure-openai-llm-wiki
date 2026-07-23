# Azure OpenAI + LLM Wiki

![GitHub last commit](https://img.shields.io/github/last-commit/kimtth/awesome-azure-openai-llm?label=commit&color=hotpink&style=flat-square)
![Azure OpenAI](https://img.shields.io/badge/llm-azure_openai-blue?style=flat-square)
![GitHub Created At](https://img.shields.io/github/created-at/kimtth/awesome-azure-openai-llm?style=flat-square)

A comprehensive, curated collection of resources for Azure OpenAI, Large Language Models (LLMs), and their applications.

🔹Concise Summaries: Each resource is briefly described for quick understanding  
🔹Chronological Organization: Resources appended with date (first commit, publication, or paper release)  
🔹Monthly Updates: The list is updated monthly; candidate entries before the update are tracked in the issue.  

<!-- > [!TIP]
> A refined list focusing on Azure and Microsoft products.  
> Check [**_Awesome Azure OpenAI & Copilot_**](https://github.com/kimtth/awesome-azure-openai-copilot).   --> 

## 🧭 Quick Navigation (Propedia-style)

| Layer / Era | What it controls | Jump to sections |
|-------------|----------------------------------------|-------------|
| **Weights** <br/> 2022-2023 | Parametric knowledge baked into the model. <br/> `Themes: Pretraining, Scaling Laws, Fine-tuning, RLHF, Alignment, Instruction-following, Few-shot` | Foundations: [Large Language Model Landscape](section/models_research.md#large-language-model-landscape), [Large Language Model Collection](section/models_research.md#large-language-model-collection), [Foundation Model Providers](section/models_research.md#foundation-model-providers) <br/> Training: [Large Language Model Training and Optimization](section/models_research.md#large-language-model-training-and-optimization), [Model Training & Inference](section/azure.md#model-training--inference), [Training & Fine-tuning](section/applications.md#training--fine-tuning) <br/> Behavior and safety: [Trust, Safety, and Security](section/models_research.md#trust-safety-and-security), [Safety, Security & LLMOps](section/azure.md#safety-security--llmops) |
| **Context** <br/> 2023-2024 | What the model sees at inference time. <br/> `Themes: Prompting, Chain-of-Thought, RAG, Memory, Long Context, Knowledge Injection, Context Engineering` | Prompting: [Prompt Engineering and Visual Prompts](section/models_research.md#prompt-engineering-and-visual-prompts), [Prompt Engineering & Tooling](section/azure.md#prompt-engineering--tooling) <br/> Retrieval: [RAG](section/applications.md#rag-retrieval-augmented-generation), [Azure AI Search](section/azure.md#azure-ai-search), [RAG Best Practices](section/best_practices.md#rag-best-practices) <br/> Memory and context windows: [Context and Long-Context Limits](section/models_research.md#context-and-long-context-limits), [Memory](section/applications.md#memory), [Data Processing & Memory](section/azure.md#data-processing--memory) |
| **Harness** <br/> 2025-2026 | How the agent acts in the real world. <br/> `Themes: Function Calling, Tool Ecosystems, MCP, Skills, Workflow Graphs, Multi-agent, A2A protocols, Orchestration, Agent Infrastructure, Security` | Agent runtime: [AI Application](section/applications.md#ai-application), [Agent Frameworks](section/azure.md#agent-frameworks), [Agent Development](section/azure.md#agent-development), [Agent Best Practices](section/best_practices.md#agent-best-practices) <br/> Protocols and tools: [Agent Protocol](section/applications.md#agent-protocol), [Coding & Research](section/applications.md#coding--research), [Skills](section/applications.md#skills), [Harness](section/applications.md#harness), [Loop Engineering](section/applications.md#loop-engineering), [Dev Tools, MCP & Extensions](section/azure.md#dev-tools-mcp--extensions) <br/> Apps and operations: [Evaluating Large Language Models](section/tools_extra.md#evaluating-large-language-models), [LLMOps](section/tools_extra.md#llmops-large-language-model-operations), [Learning Resources & Workshops](section/azure.md#learning-resources--workshops), [Code Samples & Workshops](section/azure.md#code-samples--workshops) |

Refereces: [DailyDoseOfDS - *Evolution of the Agent Landscape*](https://blog.dailydoseofds.com/p/evolution-of-agent-landscape-from)

## 1. App & Agent
🚀 [RAG Systems, LLM Applications, Agents, Frameworks & Orchestration](section/applications.md)

- **RAG**
  - [RAG](section/applications.md#rag-retrieval-augmented-generation)
  - [GraphRAG](section/applications.md#graphrag)
  - [RAG Application](section/applications.md#rag-application)
  - [Vector Database & Embedding](section/applications.md#vector-database--embedding)
- **Application**
  - [Top Agent Frameworks](section/applications.md#top-agent-frameworks)
  - [Additional Agent Framework](section/applications.md#additional-agent-framework)
  - [Cache](section/applications.md#cache)
  - [Data & Analytics Agents](section/applications.md#data--analytics-agents)
  - [Data Processing & OCR](section/applications.md#data-processing--ocr)
  - [Desktop AI Assistant](section/applications.md#desktop-ai-assistant)
  - [Memory](section/applications.md#memory)
  - [Model Gateway](section/applications.md#model-gateway)
  - [Model Serving & Local Runtimes](section/applications.md#model-serving--local-runtimes)
  - [Observability & LLMOps](section/applications.md#observability--llmops)
  - [**Popular LLM Applications** (GitHub Stars >= 1000)](section/x_llm_apps.md)
  - [SDKs, Integration & ML Libraries](section/applications.md#sdks-integration--ml-libraries)
  - [Training & Fine-tuning](section/applications.md#training--fine-tuning)
  - [UI & No-Code Tool](section/applications.md#ui--no-code-tool)
- **Agent Protocols**
  - [A2A](section/applications.md#a2a)
  - [Computer use](section/applications.md#computer-use)
  - [Model Context Protocol (MCP)](section/applications.md#model-context-protocol-mcp)
- **Coding & Research**
  - [Coding](section/applications.md#coding)
  - [Deep Research](section/applications.md#deep-research)
  - [Domain-Specific Agents](section/applications.md#domain-specific-agents)
  - [Skills](section/applications.md#skills)
  - [Harness](section/applications.md#harness)
    - [Loop Engineering](section/applications.md#loop-engineering)

**[⬆ back to top](#azure-openai--llm-wiki)**

## 2. Azure OpenAI & Copilot
🌌 [Microsoft's Cloud-Based AI Platform and Services](section/azure.md)

- **Overview**
  - [Azure OpenAI & Foundry Overview](section/azure.md#azure-openai--foundry-overview)
- **Frameworks**
  - [Orchestration Frameworks](section/azure.md#orchestration-frameworks)
  - [Agent Frameworks](section/azure.md#agent-frameworks)
- **Tooling**
  - [Prompt Engineering & Tooling](section/azure.md#prompt-engineering--tooling)
  - [Dev Tools, MCP & Extensions](section/azure.md#dev-tools-mcp--extensions)
- **Products**
  - [Copilot Product Catalog](section/azure.md#copilot-product-catalog)
  - [Agent Development](section/azure.md#agent-development)
  - [Microsoft 365 Agent Development](section/azure.md#microsoft-365-agent-development)
- **Services**
  - [Azure AI Search](section/azure.md#azure-ai-search)
  - [Microsoft Foundry & AI Services](section/azure.md#microsoft-foundry--ai-services)
- **Research**
  - [Microsoft Research](section/azure.md#microsoft-research)
- **Applications**
  - [Sample Applications](section/azure.md#sample-applications)
  - [Solution Accelerators](section/azure.md#solution-accelerators)
  - [Architecture Patterns & Use Cases](section/azure.md#architecture-patterns--use-cases)

**[⬆ back to top](#azure-openai--llm-wiki)**

## 3. Research & Survey
🧠 [LLM Landscape, Prompt Engineering, Finetuning, Challenges & Surveys](section/models_research.md)

- **Landscape**
  - [Large Language Model Landscape](section/models_research.md#large-language-model-landscape)
  - [Large Language Model Collection](section/models_research.md#large-language-model-collection)
  - [Foundation Model Providers](section/models_research.md#foundation-model-providers)
  - [Domain-Specific and Specialized LLMs](section/models_research.md#domain-specific-and-specialized-llms)
- **Prompting**
  - [Prompt Engineering and Visual Prompts](section/models_research.md#prompt-engineering-and-visual-prompts)
- **Training & Optimization**
  - [Large Language Model Training and Optimization](section/models_research.md#large-language-model-training-and-optimization)
  - [Pre-training and Data Preparation](section/models_research.md#pre-training-and-data-preparation)
  - [Architecture and Inference Patterns](section/models_research.md#architecture-and-inference-patterns)
  - [Post-training and Fine-Tuning](section/models_research.md#post-training-and-fine-tuning)
- **Impact & Products**
  - [AI Adoption, Impact, and Society](section/models_research.md#ai-adoption-impact-and-society)
  - [OpenAI Products](section/models_research.md#openai-products)
  - [Anthropic AI Products](section/models_research.md#anthropic-ai-products)
  - [Google AI Products](section/models_research.md#google-ai-products)
- **Survey & Reference**
  - [Survey and Reference](section/models_research.md#survey-and-reference)
  - [Additional Topics: A Survey of LLMs](section/models_research.md#additional-topics-a-survey-of-llms)
  - [**LLM Research** (Ranked by cite count ≥150)](section/x_llm_papers.md)
  - [Learning Resources, Implementations, and Regional Materials](section/models_research.md#learning-resources-implementations-and-regional-materials)

**[⬆ back to top](#azure-openai--llm-wiki)**

## 4. Datasets, Evaluation, and Extras
🛠️ [Training Data, Datasets & Evaluation Methods](section/tools_extra.md)

- **Data**
  - [Datasets for LLM Training](section/tools_extra.md#datasets-for-llm-training)
- **Evaluation**
  - [Evaluating Large Language Models](section/tools_extra.md#evaluating-large-language-models)
  - [LLM Evaluation Benchmarks](section/tools_extra.md#llm-evaluation-benchmarks)
  - [LLMOps: Large Language Model Operations](section/tools_extra.md#llmops-large-language-model-operations)
- **Extras**
  - [LLM for Robotics](section/tools_extra.md#llm-for-robotics)
  - [Awesome Demo](section/tools_extra.md#awesome-demo)

**[⬆ back to top](#azure-openai--llm-wiki)**

## 5. Best Practices
📋 [Curated Blogs, Patterns, and Implementation Guidelines](section/best_practices.md)

- **RAG**
  - [The Problem with RAG](section/best_practices.md#the-problem-with-rag)
  - [RAG Solution Design](section/best_practices.md#rag-solution-design)
  - [RAG Research](section/best_practices.md#rag-research)
  - [**RAG Research** (Ranked by cite count >=100)](section/best_practices.md#rag-research-ranked-by-cite-count-100)
- **Agent**
  - [Agent Design Patterns](section/best_practices.md#agent-design-patterns)
  - [Agent Research](section/best_practices.md#agent-research)
  - [**Agent Research** (Ranked by cite count >=100)](section/best_practices.md#agent-research-ranked-by-cite-count-100)
  - [Tool Use: LLM to Master APIs](section/best_practices.md#tool-use)
- **Security**
  - [Security and Governance](section/best_practices.md#security-and-governance)
- **Reference**
  - [Proposals & Glossary](section/best_practices.md#proposals--glossary)

**[⬆ back to top](#azure-openai--llm-wiki)**

## 🧭 Start Here

| Category | Goal | Suggested path |
|----------|------|----------------|
| RAG | Explore RAG patterns | [RAG](section/applications.md#rag-retrieval-augmented-generation) → [GraphRAG](section/applications.md#graphrag) → [RAG Application](section/applications.md#rag-application) → [RAG Best Practices](section/best_practices.md#rag-best-practices) → [RAG Research](section/best_practices.md#rag-research) |
| AI Engineering | Build an AI Engineering Workflow | [RAG](section/applications.md#rag-retrieval-augmented-generation) → [AI Application](section/applications.md#ai-application) → [Agent Protocol](section/applications.md#agent-protocol) → [Coding](section/applications.md#coding) → [Deep Research](section/applications.md#deep-research) → [Domain-Specific Agents](section/applications.md#domain-specific-agents) → [Skills](section/applications.md#skills) → [Harness](section/applications.md#harness) → [Loop Engineering](section/applications.md#loop-engineering) |
| Skills & Harnesses | Extend a Coding Agent | [Skills](section/applications.md#skills) → [Harness](section/applications.md#harness) → [Loop Engineering](section/applications.md#loop-engineering) → [Coding](section/applications.md#coding) → [Tool Use](section/best_practices.md#tool-use) → [Evaluation Metrics](section/tools_extra.md#evaluation-metrics) |
| Agents | Design an agent workflow | [Top Agent Frameworks](section/applications.md#top-agent-frameworks) → [Agent Design Patterns](section/best_practices.md#agent-design-patterns) → [Tool Use](section/best_practices.md#tool-use) → [Memory](section/applications.md#memory) → [Agent Research](section/best_practices.md#agent-research) |
| Data & Analytics | Build a data or analytics agent | [Data & Analytics Agents](section/applications.md#data--analytics-agents) → [Data Processing & OCR](section/applications.md#data-processing--ocr) → [Memory](section/applications.md#memory) → [Tool Use](section/best_practices.md#tool-use) → [Evaluating Large Language Models](section/tools_extra.md#evaluating-large-language-models) |
| Local LLMs | Build a local or self-hosted LLM application | [Large Language Model Collection](section/models_research.md#large-language-model-collection) → [Model Serving & Local Runtimes](section/applications.md#model-serving--local-runtimes) → [Model Gateway](section/applications.md#model-gateway) → [UI & No-Code Tool](section/applications.md#ui--no-code-tool) → [Observability & LLMOps](section/applications.md#observability--llmops) |
| MCP & Integration | Build MCP-enabled tools | [Model Context Protocol](section/applications.md#model-context-protocol-mcp) → [Dev Tools, MCP & Extensions](section/azure.md#dev-tools-mcp--extensions) → [Safety, Security & LLMOps](section/azure.md#safety-security--llmops) → [Agent Best Practices](section/best_practices.md#agent-best-practices) |
| Developer Agents | Build coding or research agents | [Coding](section/applications.md#coding) → [Deep Research](section/applications.md#deep-research) → [Skills](section/applications.md#skills) → [Harness](section/applications.md#harness) → [Loop Engineering](section/applications.md#loop-engineering) → [Tool Calling & Agentic](section/tools_extra.md#tool-calling--agentic) |
| Azure / RAG | Build an Azure RAG application | [Azure OpenAI & Foundry Overview](section/azure.md#azure-openai--foundry-overview) → [Azure AI Search](section/azure.md#azure-ai-search) → [RAG Solution Design](section/best_practices.md#rag-solution-design) → [Sample Applications](section/azure.md#sample-applications) → [Evaluating Large Language Models](section/tools_extra.md#evaluating-large-language-models) |
| Azure / Agents | Build an Azure agent | [Agent Frameworks](section/azure.md#agent-frameworks) → [Agent Design Patterns](section/best_practices.md#agent-design-patterns) → [Model Context Protocol](section/applications.md#model-context-protocol-mcp) → [Agent Development](section/azure.md#agent-development) → [Evaluating Large Language Models](section/tools_extra.md#evaluating-large-language-models) |
| Microsoft 365 | Build a Microsoft 365 agent | [Microsoft 365 Agent Development](section/azure.md#microsoft-365-agent-development) → [Copilot Product Catalog](section/azure.md#copilot-product-catalog) → [Dev Tools, MCP & Extensions](section/azure.md#dev-tools-mcp--extensions) → [Agent Development](section/azure.md#agent-development) |
| Production | Operate an AI application in production | [Architecture Patterns & Use Cases](section/azure.md#architecture-patterns--use-cases) → [Safety, Security & LLMOps](section/azure.md#safety-security--llmops) → [LLMOps](section/tools_extra.md#llmops-large-language-model-operations) → [Evaluating Large Language Models](section/tools_extra.md#evaluating-large-language-models) |
| Research | Learn the LLM landscape | [Large Language Model Landscape](section/models_research.md#large-language-model-landscape) → [Survey and Reference](section/models_research.md#survey-and-reference) → [LLM Research](section/models_research.md#llm-research-ranked-by-cite-count-150) |
| Model Development | Train or fine-tune a model | [Large Language Model Collection](section/models_research.md#large-language-model-collection) → [Model Training & Inference](section/azure.md#model-training--inference) → [Training & Fine-tuning](section/applications.md#training--fine-tuning) → [Datasets for LLM Training](section/tools_extra.md#datasets-for-llm-training) → [Evaluating Large Language Models](section/tools_extra.md#evaluating-large-language-models) |
| Multimodal | Build a multimodal application | [Multimodal Models](section/models_research.md#multimodal-models) → [Data Processing & OCR](section/applications.md#data-processing--ocr) → [RAG Application](section/applications.md#rag-application) → [Vision & Multimodal](section/tools_extra.md#vision--multimodal) |
| Evaluation | Choose and benchmark a model | [Large Language Model Collection](section/models_research.md#large-language-model-collection) → [Architecture Comparisons](section/models_research.md#architecture-comparisons) → [Evaluating Large Language Models](section/tools_extra.md#evaluating-large-language-models) → [LLM Evaluation Benchmarks](section/tools_extra.md#llm-evaluation-benchmarks) → [Evaluation Metrics](section/tools_extra.md#evaluation-metrics) |

## 📖 Legend & Notation

| Symbol | Meaning | Symbol | Meaning |
|--------|---------|--------|---------|
| ![**github**](https://img.shields.io/github/stars/kimtth/awesome-azure-openai-llm?style=flat&label=%20&color=f0f1f2&cacheSeconds=360000) | GitHub repository | 🗄️ | Archived files |
| 💡🏆 | Recommend | 📺 | Video content |
| 📑 |  Academic paper | 🤗 | Huggingface |

> **Info:** Applications that have been archived or have had no commits for more than 12 months are listed in [applications.old.md](section/applications.old.md).

<!-- 
All rights reserved © `kimtth` 
-->
<!-- 
https://shields.io/badges/git-hub-created-at
-->

**[`^        back to top        ^`](#azure-openai--llm-wiki)**
