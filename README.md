# Awesome Azure OpenAI + LLM

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
![Azure OpenAI](https://img.shields.io/badge/llm-azure_openai-blue?style=flat-square)
![GitHub Created At](https://img.shields.io/github/created-at/kimtth/awesome-azure-openai-llm?style=flat-square)

> A comprehensive, curated collection of resources for Azure OpenAI, Large Language Models (LLMs), and their applications.

This repository serves as a comprehensive guide to the rapidly evolving field of LLMs and Azure OpenAI services. Key features:

🔹Concise Summaries: Each resource is briefly described for quick understanding  
🔹Chronological Organization: Resources appended with date (first commit, publication, or paper release)  
🔹Active Tracking: Regular updates to capture the latest developments  

> Note: Some content may become outdated due to the rapid pace of development in this field.

## Quick Navigation

| Application | LLM | Tools |
|------------|-------------------|----------------------|
| [1. RAG Systems](#1rag-systems) | [5. Prompt Engineering](#5prompt-engineering--finetuning) | [8. AI Tools & Extensions](#8ai-tools--extensions) |
| [2. Azure OpenAI](#2azure-openai) | [6. Challenges & Abilities](#6️challenges--abilities) | [9. Datasets](#9datasets) |
| [3. LLM Applications](#3llm-applications) | [7. LLM Landscape](#7llm-landscape) | [10. Evaluation Methods](#10evaluation-methods) |
| [4. Agent Development](#4agent-development) | [11. Research & Surveys](#11research--surveys) | [Frameworks](#️frameworks) |

---

## Core Topics

### 1.🎯RAG Systems
Retrieval-Augmented Generation - Enhancing LLMs with External Knowledge

- [RAG Fundamentals](section/rag.md/#rag-retrieval-augmented-generation) - Core concepts and implementation strategies
- [RAG Architecture Design](section/rag.md/#rag-solution-design) - System design patterns and best practices
- [RAG Applications](section/rag.md/#rag-development) - Real-world implementations and use cases
  - [GraphRAG](section/rag.md/#graphrag) - Graph-based retrieval approaches
- [Vector Databases](section/rag.md/#vector-database-comparison) - Comparison and selection guide

### 2.🌌Azure OpenAI
Microsoft's Cloud-Based AI Platform and Services

- [Microsoft LLM Framework](section/aoai.md/#microsoft-azure-openai-llm-framework) - Official frameworks and SDKs
- [Microsoft Copilot](section/aoai.md/#microsoft-copilot) - Copilot products overview
- [Azure AI Services](section/aoai.md/#azure-ai-search) - Azure AI Search, AI services
- [Microsoft Research](section/aoai.md/#microsoft-research) - Research publications and findings
- [Reference Architectures](section/aoai.md/#azure-reference-architectures) - Proven architectural patterns and samples

### 3.🤖LLM Applications
Building Real-World Applications with Large Language Models

- [Development Frameworks](section/app.md/#applications-frameworks-and-user-interface-uiux) - Tools for building LLM applications
- [Application Development](section/app.md/#llm-application-development) - Implementation guides and best practices
  - [Code Development Tools](section/app.md/#code-editor--agent) - AI-powered coding assistants and editors
  - [Memory Systems](section/app.md/#llm-memory) - Persistent memory and context management
- [Performance Optimization](section/app.md/#caching) - Caching strategies and UX improvements
- [Emerging Concepts](section/app.md/#proposals--glossary) - New paradigms like Vibe Coding and Context Engineering
- [Robotics Integration](section/app.md/#llm-for-robotics) - LLMs in robotic systems
- [Demonstration Projects](section/app.md/#awesome-demo) - Inspiring examples and showcases

### 4.🤖Agent Development
Building Autonomous AI Agents and Multi-Agent Systems

- [Design Patterns](section/agent.md/#agent-design-patterns) - Proven architectural approaches for agent systems
- [Development Frameworks](section/agent.md/#agent-framework) - Tools and libraries for building agents
- [Agent Applications](section/agent.md/#agent-application) - Real-world agent implementations
  - [Code Interpreters](section/agent.md/#oss-alternatives-for-openai-code-interpreter-aka-advanced-data-analytics) - Open-source alternatives to OpenAI's Code Interpreter
  - [Model Context Protocol](section/agent.md/#model-context-protocol-mcp-a2a-computer-use) - MCP, Agent-to-Agent communication, and computer interaction
  - [Research Agents](section/agent.md/#deep-research) - AI systems for deep research and analysis

### 5.🧠Prompt Engineering & Finetuning
Optimizing Model Performance and Behavior

- [Prompt Engineering](section/prompt.md/#prompt-engineering) - Techniques for effective prompt design
- [Model Finetuning](section/ft.md/#finetuning) - PEFT (LoRA), RLHF, and supervised fine-tuning
- [Model Optimization](section/ft.md/#quantization-techniques) - Quantization and performance optimization
- [Advanced Techniques](section/ft.md/#other-techniques-and-llm-patterns) - Mixture of Experts (MoE) and other patterns
- [Visual Prompting](section/prompt.md/#visual-prompting--visual-grounding) - Working with multimodal inputs

### 6.🏄‍♂️Challenges & Abilities
Understanding LLM Capabilities and Limitations

- [AGI and Social Impact](section/chab.md/#agi-discussion-and-social-impact) - Discussions on artificial general intelligence
- [OpenAI Ecosystem](section/chab.md/#openais-roadmap-and-products) - Product roadmaps and strategic direction
- [Technical Constraints](section/chab.md/#context-constraints) - Context limitations and solutions (e.g., RoPE)
- [Safety and Security](section/chab.md/#trustworthy-safe-and-secure-llm) - Building trustworthy AI systems
- [LLM Capabilities](section/chab.md/#large-language-model-is-abilities) - Understanding what LLMs can and cannot do
  - [Reasoning Abilities](section/chab.md/#reasoning) - Logical reasoning and problem-solving

### 7.🌍LLM Landscape
Overview of Available Models and Technologies

- [Model Taxonomy](section/llm.md/#large-language-models-in-2023) - Classification and comparison of LLMs
- [Model Collection](section/llm.md/#large-language-model-collection) - Comprehensive list of available models
- [Domain-Specific Models](section/llm.md/#llm-for-domain-specific) - Specialized models for software development and other domains
- [Multimodal Models](section/llm.md/#mllm-multimodal-large-language-model) - Models handling text, image, audio, and video

---

## 🏗️Frameworks

### Semantic Kernel & DSPy
Microsoft's Orchestration Framework and Optimization Tools

- [Semantic Kernel](section/sk_dspy.md/#semantic-kernel) - Microsoft's micro-orchestration framework for AI applications
- [DSPy](section/sk_dspy.md/#dspy) - Optimizer frameworks for systematic prompt and model optimization

### LangChain & LlamaIndex
Popular Open-Source Frameworks for LLM Applications

- [LangChain Features](section/langchain.md/#langchain-feature-matrix--cheetsheet) - Comprehensive feature overview and cheat sheets
- [LangChain Agents](section/langchain.md/#langchain-chain-type-chains--summarizer) - Agent implementations and critical analysis
- [Framework Comparisons](section/langchain.md/#langchain-vs-competitors) - LangChain vs. alternative frameworks
- [LlamaIndex](section/langchain.md/#llamaindex) - Micro-orchestration and RAG-focused framework

---

## Tools

### 8.📚AI Tools & Extensions
Practical Tools and Browser Extensions

- [AI Tools & Extensions](section/ai_tool.md/#general-ai-tools-and-extensions)

### 9.📊Datasets
Training and Evaluation Data Resources

- [Training Datasets](section/dataset.md/#datasets-for-llm-training) - High-quality datasets for model training and fine-tuning

### 10.📝Evaluation Methods
Measuring and Improving LLM Performance

- [Evaluation Frameworks](section/eval.md/#evaluating-large-language-models) - Methods and metrics for LLM assessment
- [LLMOps](section/eval.md/#llmops-large-language-model-operations) - Operations and lifecycle management for LLM systems

---

### 11.🧠Research & Surveys
Comprehensive Surveys and Learning Materials

- [LLM Surveys](section/survey_ref.md/#survey-on-large-language-models) - Academic surveys and systematic reviews
- [Business Applications](section/survey_ref.md/#business-use-cases) - Industry use cases and implementation strategies
- [Building from Scratch](section/survey_ref.md/#build-an-llms-from-scratch-picogpt-and-lit-gpt) - Educational resources for understanding LLM internals
- [Multilingual Resources](section/survey_ref.md/#llm-materials-for-east-asian-languages) - LLM resources for Korean, Japanese, and other languages
- [Learning Materials](section/survey_ref.md/#learning-and-supplementary-materials) - Tutorials, courses, and supplementary resources

---

## Legend & Notation

| Symbol | Meaning | Symbol | Meaning |
|--------|---------|--------|---------|
| ✍️  | Blog post / Documentation | 🐙 | GitHub repository |
| 🗄️ | Archived files | 🔗 | Cross reference |
| 🗣️ | Source citation | 📺 | Video content |
| 🔢 | Citation count | 💡🏆 | Recommend |
| 📑 |  Academic paper | 🤗 | Huggingface |

---

## Contributing

<a href="https://github.com/kimtth/awesome-azure-openai-llm/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=kimtth/awesome-azure-openai-llm" />
</a>

<!-- All rights reserved © `kimtth` -->

*Last Updated: Sep 16, 2025*

[⬆ Back to Top](#awesome-azure-openai--llm-resources)
