# Awesome Azure OpenAI + LLM

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

| Layer / Era | What it controls | Representative themes | Jump to sections |
|-------------|-------------|-------------|-------------|
| **Weights** <br/> 2022-2023 | Parametric knowledge baked into the model | Pretraining, Scaling Laws, Fine-tuning, RLHF, Alignment, Instruction-following, Few-shot | Foundations: [Landscape](section/models_research.md#large-language-model-landscape), [Comparison](section/models_research.md#large-language-model-comparison), [Evolutionary Tree](section/models_research.md#evolutionary-tree-of-large-language-models), [LLM Collection](section/models_research.md#large-language-model-collection) <br/> Training: [Finetuning](section/models_research.md#finetuning), [Other Techniques and LLM Patterns](section/models_research.md#other-techniques-and-llm-patterns), [Training & Fine-tuning](section/applications.md#training--fine-tuning) <br/> Behavior and safety: [Trustworthy, Safe and Secure LLM](section/models_research.md#trustworthy-safe-and-secure-llm), [Abilities](section/models_research.md#large-language-model-is-abilities), [Reasoning](section/models_research.md#reasoning), [LLM Frameworks](section/azure.md#llm-frameworks) |
| **Context** <br/> 2023-2024 | What the model sees at inference time | Prompting, Chain-of-Thought, RAG, Memory, Long Context, Knowledge Injection, Context Engineering | Prompting: [Prompt Engineering and Visual Prompts](section/models_research.md#prompt-engineering-and-visual-prompts), [Prompt Tooling](section/azure.md#prompt-tooling) <br/> Retrieval: [RAG](section/applications.md#rag-retrieval-augmented-generation), [Advanced RAG](section/applications.md#advanced-rag), [GraphRAG](section/applications.md#graphrag), [RAG Application](section/applications.md#rag-application), [Vector Database & Embedding](section/applications.md#vector-database--embedding), [Azure AI Search](section/azure.md#azure-ai-search) <br/> Memory and context windows: [Memory](section/applications.md#memory), [Context Constraints](section/models_research.md#context-constraints), [Caching](section/applications.md#caching), [RAG Solution Design](section/best_practices.md#rag-solution-design), [RAG Research](section/best_practices.md#rag-research) |
| **Harness** <br/> 2025-2026 | How the agent acts in the real world | Function Calling, Tool Ecosystems, MCP, Skills, Workflow Graphs, Multi-agent, A2A protocols, Orchestration, Agent Infrastructure, Security | Agent runtime: [Top Agent Frameworks](section/applications.md#top-agent-frameworks), [Orchestration Framework](section/applications.md#orchestration-framework), [Frameworks / SDKs](section/applications.md#frameworks--sdks), [Agent Frameworks](section/azure.md#agent-frameworks), [Agent Development](section/azure.md#agent-development) <br/> Protocols and tools: [Model Context Protocol (MCP)](section/applications.md#model-context-protocol-mcp), [A2A](section/applications.md#a2a), [Computer use](section/applications.md#computer-use), [Skill](section/applications.md#skill), [Developer Tooling](section/azure.md#developer-tooling), [Coding](section/applications.md#coding) <br/> Ops and governance: [Apps / Ready-to-use Agents](section/applications.md#apps--ready-to-use-agents), [General AI Tools and Extensions](section/tools_extra.md#general-ai-tools-and-extensions), [Evaluating Large Language Models](section/tools_extra.md#evaluating-large-language-models), [LLM Evalution Benchmarks](section/tools_extra.md#llm-evalution-benchmarks), [LLMOps](section/tools_extra.md#llmops-large-language-model-operations), [Agent Design Patterns](section/best_practices.md#agent-design-patterns), [Agent Research](section/best_practices.md#agent-research), [Reflection, Tool Use, Planning and Multi-agent collaboration](section/best_practices.md#reflection-tool-use-planning-and-multi-agent-collaboration), [Proposals & Glossary](section/best_practices.md#proposals--glossary) |

Refereces: [DailyDoseOfDS - *Evolution of the Agent Landscape*](https://blog.dailydoseofds.com/p/evolution-of-agent-landscape-from)

## 1. App & Agent
🚀 RAG Systems, LLM Applications, Agents, Frameworks & Orchestration

- **RAG**
  - [RAG](section/applications.md#rag-retrieval-augmented-generation)
  - [Advanced RAG](section/applications.md#advanced-rag)
  - [GraphRAG](section/applications.md#graphrag)
  - [RAG Application](section/applications.md#rag-application)
  - [Vector Database & Embedding](section/applications.md#vector-database--embedding)
- **Application**
  - [Top Agent Frameworks](section/applications.md#top-agent-frameworks)
  - [Orchestration Framework](section/applications.md#orchestration-framework)
  - [Frameworks / SDKs](section/applications.md#frameworks--sdks)
  - [Apps / Ready-to-use Agents](section/applications.md#apps--ready-to-use-agents)
  - [**Popular LLM Applications** (Ranked by GitHub star count ≥1000)](section/applications.md#popular-llm-applications-ranked-by-github-star-count-1000)
  - [No Code & User Interface](section/applications.md#no-code--user-interface)
  - [Personal AI assistant & desktop](section/applications.md#personal-ai-assistant--desktop)
  - [Caching](section/applications.md#caching)
  - [Data Processing](section/applications.md#data-processing)
  - [Gateway](section/applications.md#gateway)
  - [Memory](section/applications.md#memory)
- **Agent Protocols**
  - [MCP](section/applications.md#model-context-protocol-mcp)
  - [A2A](section/applications.md#a2a)
  - [Computer use](section/applications.md#computer-use)
- **Coding & Research**
  - [Coding](section/applications.md#coding)
  - [Skill](section/applications.md#skill)
  - [Domain-Specific Agents](section/applications.md#domain-specific-agents)
  - [Deep Research](section/applications.md#deep-research)

**[⬆ back to top](#azure-openai--llm)**

## 2. Azure OpenAI & Copilot
🌌 Microsoft's Cloud-Based AI Platform and Services

- **Overview**
  - [Azure OpenAI Overview](section/azure.md#azure-openai-overview)
- **Frameworks**
  - [LLM Frameworks](section/azure.md#llm-frameworks)
  - [Agent Frameworks](section/azure.md#agent-frameworks)
- **Tooling**
  - [Prompt Tooling](section/azure.md#prompt-tooling)
  - [Developer Tooling](section/azure.md#developer-tooling)
- **Products**
  - [Microsoft Copilot Products](section/azure.md#microsoft-copilot-products)
  - [Agent Development](section/azure.md#agent-development)
  - [Copilot Development](section/azure.md#copilot-development)
- **Services**
  - [Azure AI Search](section/azure.md#azure-ai-search)
  - [Azure AI Services](section/azure.md#azure-ai-services)
- **Research**
  - [Microsoft Research](section/azure.md#microsoft-research)
- **Applications**
  - [Azure OpenAI Application](section/azure.md#azure-openai-application)
  - [Azure OpenAI Accelerator & Samples](section/azure.md#azure-openai-accelerator--samples)
  - [Use Case & Architecture References](section/azure.md#use-case--architecture-references)

**[⬆ back to top](#azure-openai--llm)**

## 3. Research & Survey
🧠 LLM Landscape, Prompt Engineering, Finetuning, Challenges & Surveys

- **Landscape**
  - [Large Language Model: Landscape](section/models_research.md#large-language-model-landscape)
  - [Comparison](section/models_research.md#large-language-model-comparison)
  - [Evolutionary Tree](section/models_research.md#evolutionary-tree-of-large-language-models)
  - [LLM Collection](section/models_research.md#large-language-model-collection)
- **Prompting**
  - [Prompt Engineering and Visual Prompts](section/models_research.md#prompt-engineering-and-visual-prompts)
- **Finetuning**
  - [Pre-training and Post-training](section/models_research.md#finetuning)
  - [Other Techniques and LLM Patterns](section/models_research.md#other-techniques-and-llm-patterns)
- **Challenges**
  - [Context Constraints](section/models_research.md#context-constraints)
  - [Trustworthy, Safe and Secure LLM](section/models_research.md#trustworthy-safe-and-secure-llm)
  - [Large Language Model's Abilities](section/models_research.md#large-language-model-is-abilities)
  - [Reasoning](section/models_research.md#reasoning)
- **Products & Impact**
  - [OpenAI Roadmap](section/models_research.md#openai-roadmap)
  - [OpenAI Models](section/models_research.md#openai-models)
  - [OpenAI Products](section/models_research.md#openai-products)
  - [Anthropic Products](section/models_research.md#anthropic-ai-products)
  - [Google AI Products](section/models_research.md#google-ai-products)
  - [AGI Discussion and Social Impact](section/models_research.md#agi-discussion-and-social-impact)
- **Survey & Build**
  - [Survey on Large Language Models](section/models_research.md#survey-on-large-language-models)
  - [Additional Topics: A Survey of LLMs](section/models_research.md#additional-topics-a-survey-of-llms)
  - [**LLM Research** (Ranked by cite count ≥150)](section/models_research.md#llm-research-ranked-by-cite-count-150)
  - [Build an LLMs from Scratch](section/models_research.md#build-an-llms-from-scratch-picogpt-and-lit-gpt)
  - [Business Use Cases](section/models_research.md#business-use-cases)

**[⬆ back to top](#azure-openai--llm)**

## 4. Tools, Datasets, and Evaluation
🛠️ AI Tools, Training Data, Datasets & Evaluation Methods

- **Tools**
  - [General AI Tools and Extensions](section/tools_extra.md#general-ai-tools-and-extensions)
  - [LLM for Robotics](section/tools_extra.md#llm-for-robotics)
  - [Awesome Demo](section/tools_extra.md#awesome-demo)
- **Data**
  - [Datasets for LLM Training](section/tools_extra.md#datasets-for-llm-training)
- **Evaluation**
  - [Evaluating Large Language Models](section/tools_extra.md#evaluating-large-language-models)
  - [LLM Evalution Benchmarks](section/tools_extra.md#llm-evalution-benchmarks)
  - [LLMOps: Large Language Model Operations](section/tools_extra.md#llmops-large-language-model-operations)

**[⬆ back to top](#azure-openai--llm)**

## 5. Best Practices
📋 Curated Blogs, Patterns, and Implementation Guidelines

- **RAG**
  - [The Problem with RAG](section/best_practices.md#the-problem-with-rag)
  - [RAG Solution Design](section/best_practices.md#rag-solution-design)
  - [RAG Research](section/best_practices.md#rag-research)
  - [**RAG Research** (Ranked by cite count >=100)](section/best_practices.md#rag-research-ranked-by-cite-count-100)
- **Agent**
  - [Agent Design Patterns](section/best_practices.md#agent-design-patterns)
  - [Agent Research](section/best_practices.md#agent-research)
  - [**Agent Research** (Ranked by cite count >=100)](section/best_practices.md#agent-research-ranked-by-cite-count-100)
  - [Reflection, Tool Use, Planning and Multi-agent collaboration](section/best_practices.md#reflection-tool-use-planning-and-multi-agent-collaboration)
  - [Tool Use: LLM to Master APIs](section/best_practices.md#tool-use)
- **Reference**
  - [Proposals & Glossary](section/best_practices.md#proposals--glossary)

**[⬆ back to top](#azure-openai--llm)**

## 📖 Legend & Notation

| Symbol | Meaning | Symbol | Meaning |
|--------|---------|--------|---------|
| ✍️ | Blog post / Documentation | ![**github**](https://img.shields.io/github/stars/kimtth/awesome-azure-openai-llm?style=flat&label=%20&color=f0f1f2&cacheSeconds=360000) | GitHub repository |
| 🗄️ | Archived files | 💡🏆 | Recommend |
| 🗣️ | Source citation | 📺 | Video content |
| 📑 |  Academic paper | 🤗 | Huggingface |

<!-- 
All rights reserved © `kimtth` 
-->
<!-- 
https://shields.io/badges/git-hub-created-at
-->

**[`^        back to top        ^`](#azure-openai--llm)**
