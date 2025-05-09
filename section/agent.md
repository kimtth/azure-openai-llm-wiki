## **Agent**

#### **Agentic Design Frameworks**

- Agentic Design Frameworks focus on managing autonomous or semi-autonomous AI agents for complex tasks.
- e.g., [Autogen](https://github.com/microsoft/autogen), and [crewAI](https://github.com/joaomdmoura/CrewAI)
 ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/autogen?style=flat-square&label=%20&color=gray&cacheSeconds=36000) ![GitHub Repo stars](https://img.shields.io/github/stars/joaomdmoura/CrewAI?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [Agent Leaderboard](https://huggingface.co/spaces/galileo-ai/agent-leaderboard)🤗

#### **Agent Design Patterns**

- [The Rise and Potential of Large Language Model Based Agents: A Survey](https://arxiv.org/abs/2309.07864): The papers list for LLM-based agents [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.07864)] / [git](https://github.com/WooooDyy/LLM-Agent-Paper-List) [14 Sep 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/WooooDyy/LLM-Agent-Paper-List?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [AgentBench](https://arxiv.org/abs/2308.03688) Evaluating LLMs as Agents: Assess LLM-as Agent’s reasoning and decision-making abilities. [7 Aug 2023]
- Agentic Design Patterns [ref](https://www.deeplearning.ai/the-batch/agentic-design-patterns-part-2-reflection/) [Mar 2024]
  - Reflection: LLM self-evaluates to improve.
    - [Self-Refine](https://arxiv.org/abs/2303.17651) [30 Mar 2023]
    - [Reflexion](https://arxiv.org/abs/2303.11366) [20 Mar 2023]
    - [CRITIC](https://arxiv.org/abs/2305.11738) [19 May 2023]
  - Tool use: LLM uses tools for information gathering, action, or data processing.
    - [Gorilla](https://arxiv.org/abs/2305.15334) [24 May 2023]
    - [MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action](https://arxiv.org/abs/2303.11381) [20 Mar 2023]
    - [Efficient Tool Use with Chain-of-Abstraction Reasoning](https://arxiv.org/abs/2401.17464) [30 Jan 2024]
  - Planning: LLM devises and executes multistep plans to reach goals.
    - [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) [28 Jan 2022]
    - [HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face](https://arxiv.org/abs/2303.17580) [30 Mar 2023]
    - [Understanding the planning of LLM agents: A survey](https://arxiv.org/abs/2402.02716) [5 Feb 2024]
  - Multi-agent collaboration: Multiple AI agents collaborate for better solutions.
    - [Communicative Agents for Software Development](https://arxiv.org/abs/2307.07924) [16 Jul 2023]
    - [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation](https://arxiv.org/abs/2308.08155) [16 Aug 2023]
    - [MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework](https://arxiv.org/abs/2308.00352) [1 Aug 2023]
    - Framework: [Autogen](https://github.com/microsoft/autogen) / [LangGraph](https://github.com/langchain-ai/langgraph) / [crewAI](https://github.com/joaomdmoura/CrewAI)
 ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/autogen?style=flat-square&label=%20&color=gray&cacheSeconds=36000) ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square&label=%20&color=gray&cacheSeconds=36000) ![GitHub Repo stars](https://img.shields.io/github/stars/joaomdmoura/CrewAI?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- Generate the code [ref](https://www.deeplearning.ai/the-batch/issue-254/) [Jun 2024]
  - [AgentCoder: Multiagent-Code Generation with Iterative Testing and Optimisation](https://arxiv.org/abs/2312.13010) [20 Dec 2023]
  - [LDB: A Large Language Model Debugger via Verifying Runtime Execution Step by Step](https://arxiv.org/abs/2402.16906) [25 Feb 2024]
  - [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793) [6 May 2024]
- [5 Agentic AI Design Patterns](https://blog.dailydoseofds.com/p/5-agentic-ai-design-patterns): Reflection, Tool use, ReAct, Planning, Multi-agent pattern [24 Jan 2025]
- [Generative AI Design Patterns for Agentic AI Systems](https://github.com/microsoft/azure-genai-design-patterns): Design Patterns for Agentic solutions in Azure [May 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/azure-genai-design-patterns?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [Agentic Architectures for Retrieval-intensive Applications](https://weaviate.io/ebooks/agentic-architectures): Published by Weviate [Mar 2025]
- [Advances and Challenges in Foundation Agents](https://arxiv.org/abs/2504.01990):💡From Brain-Inspired Intelligence to Evolutionary, Collaborative, and Safe Systems [git](https://github.com/FoundationAgents/awesome-foundation-agents) [31 Mar 2025]
- [Zero to One: Learning Agentic Patterns](https://www.philschmid.de/agentic-pattern):💡Structured `workflows` follow fixed paths, while `agentic patterns` allow autonomous, dynamic decision-making. Sample code using Gemini. [5 May 2025]

#### **Agent Design Reference**

- [Exploring Generative AI (martinfowler.com)](https://martinfowler.com/articles/exploring-gen-ai.html): Memos on how LLMs are being used to enhance software delivery practices, including Toochain, Test-Driven Development (TDD) with GitHub Copilot, pair programming, and multi-file editing. [26 Jul 2023 ~ ]
- [Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427): Cognitive Architectures for Language Agents (CoALA). Procedural (how to perform tasks), Semantic (long-term store of knowledge), Episodic Memory (recall specific past events) [ref](https://blog.langchain.dev/memory-for-agents/) [5 Sep 2023]
- [Language Agent Tree Search Method (LATS)](https://github.com/lapisrocks/LanguageAgentTreeSearch): LATS leverages an external environment and an MCTS (Monte Carlo Tree Search)-based search [6 Oct 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/lapisrocks/LanguageAgentTreeSearch?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [AI Agents That Matter](https://arxiv.org/abs/2407.01502): AI agent evaluations for optimizing both accuracy and cost. Focusing solely on accuracy can lead to overfitting and high costs. `retry, warming, escalation` [1 Jul 2024]
- [Automated Design of Agentic Systems](https://arxiv.org/abs/2408.08435): Automated Design of Agentic Systems (ADAS), which aims to automatically create powerful agentic system designs, including inventing novel building blocks and/or combining them. [15 Aug 2024]
- [The Different Ochestration Frameworks](https://newsletter.theaiedge.io/p/implementing-a-language-agent-tree):💡Orchestration frameworks for LLM applications: Micro-orchestration / Macro-orchestration / Agentic Design Frameworks / Optimizer frameworks [11 Oct 2024]
- [Agent-as-a-Judge](https://arxiv.org/abs/2410.10934): Evaluate Agents with Agents. DevAI, a new benchmark of 55 realistic automated AI development tasks. `Agent-as-a-Judge > LLM-as-a-Judge > Human-as-a-Judge` [14 Oct 2024]
- [10 Lessons to Get Started Building AI Agents](https://github.com/microsoft/ai-agents-for-beginners): 💡Microsoft. [Nov 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/ai-agents-for-beginners?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [Google AI Agents Whitepaper](https://www.kaggle.com/whitepaper-agents) [12 Nov 2024]
- [Generative Agent Simulations of 1,000 People](https://arxiv.org/abs/2411.10109): a generative agent architecture that simulates more than 1,000 real individuals using two-hour qualitative interviews. 85% accuracy in General Social Survey. [15 Nov 2024]
- [Agents Are Not Enough](https://arxiv.org/abs/2412.16241): Proposes an ecosystem comprising agents (task executors), sims (user preferences and behavior), and assistants (human-in-the-loop). [19 Dec 2024]
- [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents): 💡Anthrophic. [19 Dec 2024]
- [Hugging Face Agents Course](https://github.com/huggingface/agents-course) 🤗 Hugging Face Agents Course. [Jan 2025]
- [Agents](https://huyenchip.com/2025/01/07/agents.html):💡Chip Huyen [7 Jan 2025]
- [A Practical Guide to Building AI Agents](https://cdn.openai.com/business-guides-and-resources/a-practical-guide-to-building-agents.pdf): 💡OpenAI. [11 Mar 2025]
- [Taxonomy of failure modes in AI agents ](https://www.microsoft.com/en-us/security/blog/2025/04/24/new-whitepaper-outlines-the-taxonomy-of-failure-modes-in-ai-agents): Microsoft AI Red Team (AIRT) has categorized identified failure modes into two types: novel and existing, under the pillars of safety and security. [24 Apr 2025]

#### **Tool use: LLM to Master APIs**

- [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard_live.html) V2 [Aug 2024]
- [Chameleon: Plug-and-Play Compositional Reasoning with Large Language Models](https://arxiv.org/abs/2304.09842): Different tasks require different tools, and different models show different tool preferences—e.g., ChatGPT favors image captioning, while GPT-4 leans toward knowledge retrieval. [Tool transition](https://chameleon-llm.github.io/) [19 Apr 2023]
- [Gorilla: An API store for LLMs](https://arxiv.org/abs/2305.15334): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.15334)]: Gorilla: Large Language Model Connected with Massive APIs. 1,645 APIs. [git](https://github.com/ShishirPatil/gorilla) [24 May 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/ShishirPatil/gorilla?style=flat-square&label=%20&color=gray&cacheSeconds=36000)  

  1. Used GPT-4 to generate a dataset of instruction-api pairs for fine-tuning Gorilla.
  1. Used the abstract syntax tree (AST) of the generated code to match with APIs in the database and test set for evaluation purposes.

  > Another user asked how Gorilla compared to LangChain; Patil replied: LangChain is a terrific project that tries to teach agents how to use tools using prompting. Our take on this is that prompting is not scalable if you want to pick between 1000s of APIs. So Gorilla is a LLM that can pick and write the semantically and syntactically correct API for you to call! A drop in replacement into LangChain! [cite](https://www.infoq.com/news/2023/07/microsoft-gorilla/) [04 Jul 2023]  
- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291): The 'Skill Library' in Voyager functions like a skill manager, storing and organizing learned behaviors or code snippets that the agent can reuse and combine to solve various tasks in the Minecraft environment. [25 May 2023]
- [Toolformer](https://arxiv.org/abs/2302.04761): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2302.04761)]: Language Models That Can Use Tools, by MetaAI. Finetuned GPT-J to learn 5 tools. [git](https://github.com/lucidrains/toolformer-pytorch) [9 Feb 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/lucidrains/toolformer-pytorch?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [ToolLLM](https://arxiv.org/abs/2307.16789): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.16789)]: : Facilitating Large Language Models to Master 16000+ Real-world APIs [git](https://github.com/OpenBMB/ToolBench) [31 Jul 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/OpenBMB/ToolBench?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [APIGen](https://arxiv.org/abs/2406.18518): Automated Pipeline for Generating Verifiable and Diverse Function-Calling Datasets [26 Jun 2024]
- [ToolShed](https://arxiv.org/abs/2410.14594): Toolshed Knowledge Bases & Advanced RAG-Tool Fusion, optimized for storing and retrieving tools in a vector database for large-scale agents. To address the limitations of primary methods, two approaches are: 1. tuning-based tool calling via LLM fine-tuning, and 2. retriever-based tool selection and planning. [18 Oct 2024]

#### **Model Context Protocol (MCP) & Computer use**

##### Model Context Protocol (MCP)

- [Model Context Protocol (MCP)](https://www.anthropic.com/news/model-context-protocol): Anthropic proposes an open protocol for seamless LLM integration with external data and tools. [git](https://github.com/modelcontextprotocol/servers) [26 Nov 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/modelcontextprotocol/servers?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [Awesome MCP Servers](https://github.com/punkpeye/awesome-mcp-servers) ![GitHub Repo stars](https://img.shields.io/github/stars/punkpeye/awesome-mcp-servers?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [mcp.so](https://mcp.so/): Find Awesome MCP Servers and Clients
- [Docker MCP Toolkit and MCP Catalog](https://www.docker.com/products/mcp-catalog-and-toolkit): `docker mcp` [5 May 2025]
- [A Survey of AI Agent Protocols](https://arxiv.org/abs/2504.16736) [23 Apr 2025]
1. [ACI.dev ](https://github.com/aipotheosis-labs/aci): Unified Model-Context-Protocol (MCP) server (Built-in OAuth flows) [Sep 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/aipotheosis-labs/aci?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [5ire](https://github.com/nanbingxyz/5ire): a cross-platform desktop AI assistant, MCP client. [Oct 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/nanbingxyz/5ire?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [mcp-agent](https://github.com/lastmile-ai/mcp-agent): Build effective agents using Model Context Protocol and simple workflow patterns [Dec 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/lastmile-ai/mcp-agent?style=flat-square&label=%20&color=gray&cacheSeconds=36000) 
1. [goose](https://github.com/block/goose):💡An open-source, extensible AI agent with support for the Model Context Protocol (MCP). Developed by Block, a company founded in 2009 by Jack Dorsey. [Jan 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/block/goose?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [AWS MCP Servers](https://github.com/awslabs/mcp): MCP servers that bring AWS best practices [Mar 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/awslabs/mcp?style=flat-square&label=%20&color=gray&cacheSeconds=36000) 
1. [MCP Run Python](https://ai.pydantic.dev/mcp/run-python/): PydanticAI. Use Pyodide to run Python code in a JavaScript environment with Deno [19 Mar 2025]
1. [mcp-use](https://github.com/mcp-use/mcp-use): MCP Client Library to connect any LLM to any MCP server [Mar 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/mcp-use/mcp-use?style=flat-square&label=%20&color=gray&cacheSeconds=36000) 
1. [fastapi_mcp](https://github.com/tadata-org/fastapi_mcp): automatically exposing FastAPI endpoints as Model Context Protocol (MCP) [Mar 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/tadata-org/fastapi_mcp?style=flat-square&label=%20&color=gray&cacheSeconds=36000) 
1. [Azure MCP Server](https://github.com/Azure/azure-mcp): connection between AI agents and key Azure services like Azure Storage, Cosmos DB, and more. [Apr 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/Azure/azure-mcp?style=flat-square&label=%20&color=gray&cacheSeconds=36000) 

##### Computer use

- [ACU - Awesome Agents for Computer Use](https://github.com/francedot/acu) ![GitHub Repo stars](https://img.shields.io/github/stars/francedot/acu?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [Anthropic Claude's computer use](https://www.anthropic.com/news/developing-computer-use): [23 Oct 2024]
- [Computer Agent Arena Leaderboard](https://arena.xlang.ai/leaderboard) [Apr 2025]
1. [CogAgent](https://github.com/THUDM/CogAgent): An open-sourced end-to-end VLM-based GUI Agent [Dec 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/THUDM/CogAgent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [OpenInterpreter starts to support Computer Use API](https://github.com/OpenInterpreter/open-interpreter/issues/1490)
1. [Agent.exe](https://github.com/corbt/agent.exe): Electron app to use computer use APIs. [Oct 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/corbt/agent.exe?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [x-ref](aoai.md/#agent) > [UFO](https://github.com/microsoft/UFO): Windows Control
1. [Self-Operating Computer Framework](https://github.com/OthersideAI/self-operating-computer): A framework to enable multimodal models to operate a computer. [Nov 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/OthersideAI/self-operating-computer?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Open-Interface](https://github.com/AmberSahdev/Open-Interface/): LLM backend (GPT-4V, etc), supporting Linux, Mac, Windows. [Jan 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/AmberSahdev/Open-Interface?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Computer Use OOTB](https://github.com/showlab/computer_use_ootb): Out-of-the-box (OOTB) GUI Agent for Windows and macOS. [Oct 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/showlab/computer_use_ootb?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [UI-TARS](https://arxiv.org/abs/2501.12326): An agent model built on Qwen-2-VL for seamless GUI interaction, by ByteDance. [git](https://github.com/bytedance/UI-TARS) / Application [git](https://github.com/bytedance/UI-TARS-desktop) ![GitHub Repo stars](https://img.shields.io/github/stars/bytedance/UI-TARS-desktop?style=flat-square&label=%20&color=gray&cacheSeconds=36000) [21 Jan 2025]
1. [OpenAI Operator](https://openai.com/index/introducing-operator/) [x-ref](chab.md/#openai-products) [23 Jan 2025]
1. [Open Operator](https://github.com/browserbase/open-operator): a web agent based on Browserbase [24 Jan 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/browserbase/open-operator?style=flat-square&label=%20&color=gray&cacheSeconds=36000) 

#### **Memory Layer**

- [x-ref](app.md/#llm-memory)

#### **Agent Framework**

1. [Huginn](https://github.com/huginn/huginn): A hackable version of IFTTT or Zapier on your own server for building agents that perform automated tasks. [Mar 2013] ![GitHub Repo stars](https://img.shields.io/github/stars/huginn/huginn?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Botpress Cloud](https://github.com/botpress/botpress): The open-source hub to build & deploy GPT/LLM Agents. [Nov 2016] ![GitHub Repo stars](https://img.shields.io/github/stars/botpress/botpress?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [n8n](https://github.com/n8n-io/n8n): A workflow automation tool for integrating various tools. [Jan 2019] ![GitHub Repo stars](https://img.shields.io/github/stars/n8n-io/n8n?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [phidata](https://github.com/phidatahq/phidata): Build AI Assistants with memory, knowledge, and tools [May 2022] ![GitHub Repo stars](https://img.shields.io/github/stars/phidatahq/phidata?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Cheshire-Cat (Stregatto)](https://github.com/cheshire-cat-ai/core): Framework to build custom AIs with memory and plugins [Feb 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/cheshire-cat-ai/core?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [MetaGPT](https://github.com/geekan/MetaGPT): Multi-Agent Framework. Assign different roles to GPTs to form a collaborative entity for complex tasks. e.g., Data Interpreter [Jun 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/geekan/MetaGPT?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [SuperAGI](https://github.com/TransformerOptimus/SuperAGI): Autonomous AI Agents framework [May 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/TransformerOptimus/SuperAGI?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [AgentVerse](https://github.com/OpenBMB/AgentVerse): Primarily providing: task-solving and simulation. [May 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/OpenBMB/AgentVerse?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [OpenAgents](https://github.com/xlang-ai/OpenAgents): Three distinct agents: Data Agent for data analysis, Plugins Agent for plugin integration, and Web Agent for autonomous web browsing. [Aug 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/xlang-ai/OpenAgents?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [AgentOps](https://github.com/AgentOps-AI/agentops):Python SDK for AI agent monitoring, LLM cost tracking, benchmarking. [Aug 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/AgentOps-AI/agentops?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Lagent](https://github.com/InternLM/lagent): Inspired by the design philosophy of PyTorch. A lightweight framework for building LLM-based agents. [Aug 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/InternLM/lagent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Autogen](https://github.com/microsoft/autogen):💡Customizable and conversable agents framework [Aug 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/autogen?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [LangGraph](https://github.com/langchain-ai/langgraph): Built on top of LangChain [Aug 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [crewAI](https://github.com/joaomdmoura/CrewAI):💡Framework for orchestrating role-playing, autonomous AI agents. [Oct 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/joaomdmoura/CrewAI?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [XAgent](https://github.com/OpenBMB/XAgent): Autonomous LLM Agent for complex task solving like data analysis, recommendation, and model training [Oct 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/OpenBMB/XAgent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Qwen-Agent](https://github.com/QwenLM/Qwen-Agent): Agent framework built upon Qwen1.5, featuring Function Calling, Code Interpreter, RAG, and Chrome extension. [Sep 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/QwenLM/Qwen-Agent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Open AI Assistant API](https://platform.openai.com/docs/assistants/overview) [6 Nov 2023]
1. [Agno](https://github.com/agno-agi/agno):💡Build Multimodal AI Agents with memory, knowledge and tools. Simple, fast and model-agnostic. [Nov 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/agno-agi/agno?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Burr](https://github.com/dagworks-inc/burr): Create an application as a state machine (graph/flowchart) for managing state, decisions, human feedback, and workflows. [Jan 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/dagworks-inc/burr?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [TaskingAI](https://github.com/TaskingAI/TaskingAI): A BaaS (Backend as a Service) platform for LLM-based Agent Development and Deployment. [Jan 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/TaskingAI/TaskingAI?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [AgentScope](https://github.com/modelscope/agentscope): To build LLM-empowered multi-agent applications. [Jan 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/modelscope/agentscope?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [composio](https://github.com/ComposioHQ/composio): Integration of Agents with 100+ Tools [Feb 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/ComposioHQ/composio?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [maestro](https://github.com/Doriandarko/maestro): A Framework for Claude Opus, GPT, and local LLMs to Orchestrate Subagents [Mar 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/Doriandarko/maestro?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [UpSonic](https://github.com/Upsonic/UpSonic): (previously GPT Computer Assistant(GCA)) an AI agent framework designed to make computer use. [May 2024]
1. [Atomic Agents](https://github.com/BrainBlend-AI/atomic-agents): an extremely lightweight and modular framework for building Agentic AI pipelines [Jun 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/BrainBlend-AI/atomic-agents?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [AWS: Multi-Agent Orchestrator](https://github.com/awslabs/multi-agent-orchestrator): a framework for managing multiple AI agents and handling complex conversations. [Jul 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/awslabs/multi-agent-orchestrator?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [SwarmZero](https://github.com/swarmzero/swarmzero): SwarmZero's SDK for building AI agents, swarms of agents. [Aug 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/swarmzero/swarmzero?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Mastra](https://github.com/mastra-ai/mastra): The TypeScript AI agent framework. workflows, agents, RAG, integrations and evals. [Aug 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/mastra-ai/mastra?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Dynamiq](https://github.com/dynamiq-ai/dynamiq): An orchestration framework for RAG, agentic AI, and LLM applications [Sep 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/dynamiq-ai/dynamiq?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [PySpur](https://github.com/PySpur-Dev/pyspur): Drag-and-Drop. an AI agent builder in Python. [Sep 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/PySpur-Dev/pyspur?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Bee Agent Framework](https://github.com/i-am-bee/bee-agent-framework): IBM. The TypeScript framework for building scalable agentic applications. [Oct 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/i-am-bee/bee-agent-framework?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Agent-S](https://github.com/simular-ai/Agent-S): To build intelligent GUI agents that autonomously learn and perform complex tasks on your computer. [Oct 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/simular-ai/Agent-S?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [OpenAI Swarm](https://github.com/openai/swarm): An experimental and educational framework for lightweight multi-agent orchestration. [11 Oct 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/openai/swarm?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [PydanticAI](https://github.com/pydantic/pydantic-ai): Agent Framework / shim to use Pydantic with LLMs. Model-agnostic. Type-safe. [29 Oct 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/pydantic/pydantic-ai?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [smolagents](https://github.com/huggingface/smolagents):🤗a smol library to build great agents! [Dec 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/smolagents?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Agentarium](https://github.com/Thytu/Agentarium): a framework for creating and managing simulations populated with AI-powered agents. [Dec 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/Thytu/Agentarium?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [AutoAgent](https://github.com/HKUDS/AutoAgent): AutoAgent: Fully-Automated and Zero-Code LLM Agent Framework ![GitHub Repo stars](https://img.shields.io/github/stars/HKUDS/AutoAgent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [OWL: Optimized Workforce Learning](https://github.com/camel-ai/owl): a multi-agent collaboration framework built on CAMEL-AI, enhancing task automation [Mar 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/camel-ai/owl?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Anus: Autonomous Networked Utility System](https://github.com/nikmcfly/ANUS): An open-source AI agent framework for task automation, multi-agent collaboration, and web interactions. [Mar 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/nikmcfly/ANUS?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. Microsoft Agent Frameworks [x-ref](aoai.md/#microsoft-azure-openai-relevant-llm-framework)
1. Agent Framework used in MLE-bench: GPT-4o (AIDE) earned the highest score [x-ref](eval.md/#evaluating-large-language-models)
    - [AIDE](https://github.com/WecoAI/aideml): The state-of-the-art machine learning engineer agent [Apr 2024]
    ![GitHub Repo stars](https://img.shields.io/github/stars/WecoAI/aideml?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
    - [OpenHands](https://github.com/All-Hands-AI/OpenHands): OpenHands (formerly OpenDevin), a platform for software development agents [Mar 2024]
    ![GitHub Repo stars](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
    - [MLAB ResearchAgent](https://github.com/snap-stanford/MLAgentBench): Evaluating Language Agents on Machine Learning Experimentation [Aug 2023]
    ![GitHub Repo stars](https://img.shields.io/github/stars/snap-stanford/MLAgentBench?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [OpenAI Agents SDK & Response API](https://github.com/openai/openai-agents-python):🏆Responses API (Chat Completions + Assistants API), Built-in tools (web search, file search, computer use), Agents SDK for multi-agent workflows, agent workflow observability tools [11 Mar 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/openai/openai-agents-python?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Google ADK](https://github.com/google/adk-python): Agent Development Kit (ADK) [Apr 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/google/adk-python?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [VoltAgent](https://github.com/VoltAgent/voltagent): Open Source TypeScript AI Agent Framework [Apr 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/VoltAgent/voltagent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)

#### **Agent Application**

1. [Khoj](https://github.com/khoj-ai/khoj): Open-source, personal AI agents. Cloud or Self-Host, Multiple Interfaces. Python Django based [Aug 2021] ![GitHub Repo stars](https://img.shields.io/github/stars/khoj-ai/khoj?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [PR-Agent](https://github.com/Codium-ai/pr-agent): Efficient code review and handle pull requests, by providing AI feedbacks and suggestions [Jan 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/Codium-ai/pr-agent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Auto-GPT](https://github.com/Torantulino/Auto-GPT): Most popular [Mar 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/Torantulino/Auto-GPT?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [CAMEL](https://github.com/lightaime/camel): CAMEL: Communicative Agents for “Mind” Exploration of Large Scale Language Model Society [Mar 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/lightaime/camel?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [babyagi](https://github.com/yoheinakajima/babyagi): Simplest implementation - Coworking of 4 agents [Apr 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/yoheinakajima/babyagi?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [SuperAGI](https://github.com/TransformerOptimus/superagi): GUI for agent settings [May 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/TransformerOptimus/superagi?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [ai-town](https://github.com/a16z-infra/ai-town): a virtual town where AI characters live, chat and socialize. [Jul 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/a16z-infra/ai-town?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [AgentGPT](https://github.com/reworkd/AgentGPT): Assemble, configure, and deploy autonomous AI agents in your browser [Apr 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/reworkd/AgentGPT?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [GPT Pilot](https://github.com/Pythagora-io/gpt-pilot): The first real AI developer. Dev tool that writes scalable apps from scratch while the developer oversees the implementation [Jul 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/Pythagora-io/gpt-pilot?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [OpenDAN : Your Personal AIOS](https://github.com/fiatrete/OpenDAN-Personal-AI-OS): OpenDAN, an open-source Personal AI OS consolidating various AI modules in one place [May 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/fiatrete/OpenDAN-Personal-AI-OS?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [RasaGPT](https://github.com/paulpierre/RasaGPT): Built with Rasa, FastAPI, Langchain, and LlamaIndex [Apr 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/paulpierre/RasaGPT?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [ChatDev](https://github.com/OpenBMB/ChatDev): Virtual software company. Create Customized Software using LLM-powered Multi-Agent Collaboration [Sep 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/OpenBMB/ChatDev?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [skyagi](https://github.com/litanlitudan/skyagi): Simulating believable human behaviors. Role playing [Apr 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/litanlitudan/skyagi?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [tabby](https://github.com/TabbyML/tabby): a self-hosted AI coding assistant, offering an open-source and on-premises alternative to GitHub Copilot. [Aug 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/TabbyML/tabby?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Letta ADE](https://github.com/letta-ai/letta): a graphical user interface for ADE (Agent Development Environment) by [Letta (previously MemGPT)](https://github.com/letta-ai/letta) [12 Oct 2023]
1. [AppAgent-TencentQQGYLab](https://github.com/mnotgod96/AppAgent): Multimodal Agents as Smartphone Users. [Dec 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/mnotgod96/AppAgent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [AIOS](https://github.com/agiresearch/AIOS): LLM Agent Operating System [Jan 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/agiresearch/AIOS?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [SeeAct](https://osu-nlp-group.github.io/SeeAct): GPT-4V(ision) is a Generalist Web Agent, if Grounded [git](https://github.com/OSU-NLP-Group/SeeAct) [Jan 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/OSU-NLP-Group/SeeAct?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [WrenAI](https://github.com/Canner/WrenAI): Open-source SQL AI Agent for Text-to-SQL [Mar 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/Canner/WrenAI?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Devon](https://github.com/entropy-research/Devon): An open-source pair programmer. [Mar 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/entropy-research/Devon?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Project Astra](https://deepmind.google/technologies/gemini/project-astra/): Google DeepMind, A universal AI agent that is helpful in everyday life [14 May 2024]
1. [SakanaAI AI-Scientist](https://github.com/SakanaAI/AI-Scientist): Towards Fully Automated Open-Ended Scientific Discovery [Aug 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Integuru](https://github.com/Integuru-AI/Integuru): An AI agent that generates integration code by reverse-engineering platforms' internal APIs. [Oct 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/Integuru-AI/Integuru?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [skyvern](https://github.com/skyvern-ai/skyvern): Automate browser-based workflows with LLMs and Computer Vision [Feb 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/skyvern-ai/skyvern?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [LaVague](https://github.com/lavague-ai/LaVague): Automate automation with Large Action Model framework. Generate Selenium code. [Feb 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/lavague-ai/LaVague?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Mobile-Agent](https://github.com/X-PLUG/MobileAgent): The Powerful Mobile Device Operation Assistant Family. [Jan 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/X-PLUG/MobileAgent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [TEN Agent](https://github.com/TEN-framework/TEN-Agent): The world’s first real-time multimodal agent integrated with the OpenAI Realtime API. [Jun 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/TEN-framework/TEN-Agent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Agent Zero](https://github.com/frdel/agent-zero): An open-source framework for autonomous AI agents with task automation and code generation. [Jun 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/frdel/agent-zero?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Agentless](https://github.com/OpenAutoCoder/Agentless): an agentless approach to automatically solve software development problems. AGENTLESS, consisting of three phases: localization, repair, and patch validation (self-reflect). [1 Jul 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/OpenAutoCoder/Agentless?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Potpie](https://github.com/potpie-ai/potpie): Prompt-To-Agent : Create custom engineering agents for your codebase [Aug 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/potpie-ai/potpie?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Suna](https://github.com/kortix-ai/suna): a fully open source AI assistant that helps you accomplish real-world tasks [Oct 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/kortix-ai/suna?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [browser-use](https://github.com/browser-use/browser-use): Make websites accessible for AI agents. [Nov 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/browser-use/browser-use?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Magentic-One](https://aka.ms/magentic-one): A Generalist Multi-Agent System for Solving Complex Tasks [Nov 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/TEN-framework/TEN-Agent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [nanobrowser](https://github.com/nanobrowser/nanobrowser): Open-source Chrome extension for AI-powered web automation. Alternative to OpenAI Operator. [Dec 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/nanobrowser/nanobrowser?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Riona-AI-Agent](https://github.com/David-patrick-chuks/Riona-AI-Agent): automation tool designed for Instagram to automate social media interactions such as posting, liking, and commenting. [Jan 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/David-patrick-chuks/Riona-AI-Agent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Realtime API Agents Demo](https://github.com/openai/openai-realtime-agents): a simple demonstration of more advanced, agentic patterns built on top of the Realtime API. OpenAI. [Jan 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/openai/openai-realtime-agents?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [PaSa](https://github.com/bytedance/pasa): an advanced paper search agent. Bytedance. [Jan 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/bytedance/pasa?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Sim Studio](https://github.com/simstudioai/sim): A Figma-like canvas to build agent workflow. [Jan 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/simstudioai/sim?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Archon](https://github.com/coleam00/Archon): AI Agent Builder: Example of iteration from Single-Agent to Multi-Agent. [Feb 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/coleam00/Archon?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [PayPal Agent Toolkit](https://github.com/paypal/agent-toolkit): OpenAI's Agent SDK, LangChain, Vercel's AI SDK, and Model Context Protocol (MCP) to integrate with PayPal APIs through function calling. ![GitHub Repo stars](https://img.shields.io/github/stars/paypal/agent-toolkit?style=flat-square&label=%20&color=gray&cacheSeconds=36000) [Mar 2025]

#### **OSS Alternatives for OpenAI Code Interpreter (aka. Advanced Data Analytics)**

1. [OpenAI Code Interpreter](https://openai.com/blog/chatgpt-plugins) Integration with Sandboxed python execution environment [23 Mar 2023]
    - We provide our models with a working Python interpreter in a sandboxed, firewalled execution environment, along with some ephemeral disk space.
1. [x-ref](app.md/#llm-application): E2B - sandbox
1. [SlashGPT](https://github.com/snakajima/SlashGPT) The tool integrated with "jupyter" agent [Apr 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/snakajima/SlashGPT?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [gpt-code-ui](https://github.com/ricklamers/gpt-code-ui) An open source implementation of OpenAI's ChatGPT Code interpreter. [May 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/ricklamers/gpt-code-ui?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [OSS Code Interpreter](https://github.com/shroominic/codeinterpreter-api) A LangChain implementation of the ChatGPT Code Interpreter. [Jul 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/shroominic/codeinterpreter-api?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Open Interpreter](https://github.com/KillianLucas/open-interpreter):💡Let language models run code on your computer. [Jul 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/KillianLucas/open-interpreter?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Azure Container Apps Dynamic Sessions](https://aka.ms/AAtnnj8): Secure environment for running AI-generated code in Azure.

#### **Coding agent**

- [x-ref](app.md/#code-editor--agent): Code editor / agent

#### **Domain-specific**

1. [5 Top AI Agents for Earth Snapshots](https://x.com/MaryamMiradi/status/1866527000963211754) VLMs and LLMs for Geospatial Intelligent Analysis: [GeoChat](https://arxiv.org/abs/2311.15826) | [GEOBench-VLM](https://arxiv.org/abs/2411.19325) | [RS5M](https://github.com/om-ai-lab/RS5M) | [VHM](https://github.com/opendatalab/VHM) | [EarthGPT](https://ieeexplore.ieee.org/document/10547418)
1. [MLE-agent](https://github.com/MLSysOps/MLE-agent): LLM agent for machine learning engineers and researchers [Apr 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/MLSysOps/MLE-agent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [DrugAgent: Automating AI-aided Drug Discovery](https://arxiv.org/abs/2411.15692) [24 Nov 2024]
1. [FinRobot: AI Agent for Equity Research and Valuation](https://arxiv.org/abs/2411.08804) [13 Nov 2024]
1. [An LLM Agent for Automatic Geospatial Data Analysis](https://arxiv.org/abs/2410.18792) [24 Oct 2024]
1. [Director](https://github.com/video-db/Director): Think of Director as ChatGPT for videos. AI video agents framework for video interactions and workflows. [Oct 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/video-db/Director?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [ChemAgent: Self-updating Library in Large Language Models Improves Chemical Reasoning](https://arxiv.org/abs/2501.06590): ChemAgent leverages an innovative self-improving memory system to significantly enhance performance in complex scientific tasks, with a particular focus on Chemistry. [11 Jan 2025]
1. [landing.ai: Vision Agent](https://github.com/landing-ai/vision-agent): A agent frameworks to generate code to solve your vision task. [Feb 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/landing-ai/vision-agent?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [UXAgent](https://arxiv.org/abs/2502.12561): An LLM Agent-Based Usability Testing Framework for Web Design [18 Feb 2025]

#### **Deep research**

1. [STORM](https://github.com/stanford-oval/storm): Simulating Expert Q&A, iterative research, structured outline creation, and grounding in trusted sources to generate Wikipedia-like reports. [Apr 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/stanford-oval/storm?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [SakanaAI AI-Scientist](https://github.com/SakanaAI/AI-Scientist): [x-ref](agent.md/#agent-application) [Aug 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Company Researcher](https://github.com/exa-labs/company-researcher): a free and open-source tool that helps you instantly understand any company inside out. [Nov 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/exa-labs/company-researcher?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Open Deep Research](https://github.com/btahir/open-deep-research): Open source alternative to Gemini Deep Research. [Dec 2024] ![GitHub Repo stars](https://img.shields.io/github/stars/btahir/open-deep-research?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Agent Laboratory](https://github.com/SamuelSchmidgall/AgentLaboratory): E2E autonomous research workflow. Using LLM Agents as Research Assistants. [8 Jan 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/SamuelSchmidgall/AgentLaboratory?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [OpenAI deep research](https://openai.com/index/introducing-deep-research/): [x-ref](chab.md/#openai-products)  [2 Feb 2025]
1. [Ollama Deep Researcher](https://github.com/langchain-ai/ollama-deep-researcher): a fully local web research assistant that uses any LLM hosted by Ollama [Feb 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/ollama-deep-researcher?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [smolagents: Open Deep Research](https://github.com/huggingface/smolagents) > `examples/open_deep_research`.🤗HuggingFace [Feb 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/huggingface/smolagents?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [open source deep research](https://github.com/nickscamara/open-deep-research): Firecrawl Search based backend & UI [Feb 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/nickscamara/open-deep-research?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [DeepSearcher](https://github.com/zilliztech/deep-searcher): DeepSearcher integrates LLMs and Vector Databases for precise search, evaluation, and reasoning on private data, providing accurate answers and detailed reports. [Feb 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/zilliztech/deep-searcher?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Felo.ai Deep Research](https://felo.ai/blog/free-deepseek-r1-ai-search/) [8 Feb 2025]
1. [LangChain Open Deep Research](https://github.com/langchain-ai/open_deep_research): (formerly mAIstro) a web research assistant for generating comprehensive reports on any topic. [13 Feb 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/open_deep_research?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research) [14 Feb 2025]
1. [Accelerating scientific breakthroughs with an AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/): Google introduces AI co-scientist, a multi-agent AI system built with Gemini 2.0 as a virtual scientific collaborator [19 Feb 2025]
1. [Manus sandbox runtime code leaked](https://x.com/jianxliao/status/1898861051183349870): Claude Sonnet with 29 tools, without multi-agent, using `browser_use`. [git](https://gist.github.com/jlia0/db0a9695b3ca7609c9b1a08dcbf872c9) [ref](https://manus.im/): Manus official site [10 Mar 2025]
1. [OpenManus](https://github.com/mannaandpoem/OpenManus): A Free Open-Source Alternative to Manus AI Agent [Mar 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/mannaandpoem/OpenManus?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [CodeScientist](https://github.com/allenai/codescientist): An automated scientific discovery system for code-based experiments. AllenAI. [Mar 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/allenai/codescientist?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [OpenDeepSearch](https://github.com/sentient-agi/OpenDeepSearch): deep web search and retrieval, optimized for use with Hugging Face's SmolAgents ecosystem [Mar 2025] ![GitHub Repo stars](https://img.shields.io/github/stars/sentient-agi/OpenDeepSearch?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [The AI Scientist-v2: Workshop-Level Automated Scientific Discovery via Agentic Tree Search](https://arxiv.org/abs/2504.08066): AgentManager handles Agentic Tree Search [10 Apr 2025] [git](https://github.com/SakanaAI/AI-Scientist-v2) ![GitHub Repo stars](https://img.shields.io/github/stars/SakanaAI/AI-Scientist-v2?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
1. [Paper2Code: Automating Code Generation from Scientific Papers in Machine Learning](https://arxiv.org/abs/2504.17192): a multi-agent LLM framework that transforms machine learning papers into functional code repositories. [24 Apr 2025] [git](https://github.com/going-doer/Paper2Code) ![GitHub Repo stars](https://img.shields.io/github/stars/going-doer/Paper2Code?style=flat-square&label=%20&color=gray&cacheSeconds=36000)