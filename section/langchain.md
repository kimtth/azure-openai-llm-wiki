## **LangChain Features, Usage, and Comparisons**

- LangChain is a framework for developing applications powered by language models. (1) Be data-aware: connect a language model to other sources of data.
  (2) Be agentic: Allow a language model to interact with its environment. doc:[ref](https://docs.langchain.com/docs) / blog:[ref](https://blog.langchain.dev) / [git](https://github.com/langchain-ai/langchain)
 ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square&label=%20&color=gray)
- It highlights two main value props of the framework:

  1. Components: modular abstractions and implementations for working with language models, with easy-to-use features.
  2. Use-Case Specific Chains: chains of components that assemble in different ways to achieve specific use cases, with customizable interfaces.cite: [ref](https://docs.langchain.com/docs/)
  
  - LangChain 0.2: full separation of langchain and langchain-community. [ref](https://blog.langchain.dev/langchain-v02-leap-to-stability) [May 2024]
  - Towards LangChain 0.1 [ref](https://blog.langchain.dev/the-new-langchain-architecture-langchain-core-v0-1-langchain-community-and-a-path-to-langchain-v0-1/) [Dec 2023] 
  
      <img src="../files/langchain-eco-v3.png" width="400">
  <!-- <img src="../files/langchain-eco-stack.png" width="400"> -->
  <!-- <img src="../files/langchain-glance.png" width="400"> -->

  - Basic LangChain building blocks [ref](https://www.packtpub.com/article-hub/using-langchain-for-large-language-model-powered-applications) [2023]

    ```python
    '''
    LLMChain: A LLMChain is the most common type of chain. It consists of a PromptTemplate, a model (either an LLM or a ChatModel), and an optional output parser.
    '''
    chain = prompt | model | parser
    ```
  - LLMChain: Deprecated since version 0.1.17: Use RunnableSequence, e.g., `prompt | llm` instead. 
  - LangChain has shifted towards the Runnable interface since version 0.1.17.
  - Imperative (programmatic) approach: The Runnable interface (formerly LLMChain) for flexible, programmatic chain building.
  - Declarative approach: LangChain Expression Language (LCEL) offers a declarative syntax for chain composition, enabling features like async, batch, and streaming operations with the | operator for combining functionalities.

### **Macro and Micro-orchestration**

- Macro-orchestration in LLM pipelines involves high-level design and management of complex workflows, integrating multiple LLMs and other components.
- Micro-orchestration [x-ref](sk_dspy.md/#micro-orchestration)
- [LangGraph](https://langchain-ai.github.io/langgraph/) in LangChain, and [Burr](https://burr.dagworks.io/)

### **LangChain Feature Matrix & Cheetsheet**

- [Feature Matrix](https://python.langchain.com/docs/get_started/introduction): LangChain Features
  - [Feature Matrix: Snapshot in 2023 July](../files/langchain-features-202307.png)
- [Awesome LangChain](https://github.com/kyrolabs/awesome-langchain): Curated list of tools and projects using LangChain.
 ![GitHub Repo stars](https://img.shields.io/github/stars/kyrolabs/awesome-langchain?style=flat-square&label=%20&color=gray)
- [Cheetsheet](https://github.com/gkamradt/langchain-tutorials): LangChain CheatSheet
 ![GitHub Repo stars](https://img.shields.io/github/stars/gkamradt/langchain-tutorials?style=flat-square&label=%20&color=gray)
- [LangChain Cheetsheet KD-nuggets](https://www.kdnuggets.com/wp-content/uploads/LangChain_Cheat_Sheet_KDnuggets.pdf): LangChain Cheetsheet KD-nuggets [doc](../files/LangChain_kdnuggets.pdf) [Aug 2023]
- [LangChain AI Handbook](https://www.pinecone.io/learn/series/langchain/): published by Pinecone
- [LangChain Tutorial](https://nanonets.com/blog/langchain/): A Complete LangChain Guide
- [RAG From Scratch](https://github.com/langchain-ai/rag-from-scratch)💡[Feb 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/rag-from-scratch?style=flat-square&label=%20&color=gray)
- DeepLearning.AI short course: LangChain for LLM Application Development [ref](https://www.deeplearning.ai/short-courses/langchain-for-llm-application-development/) / LangChain: Chat with Your Data [ref](https://www.deeplearning.ai/short-courses/langchain-chat-with-your-data/)
- [LangChain Streamlit agent examples](https://github.com/langchain-ai/streamlit-agent): Implementations of several LangChain agents as Streamlit apps. [Jun 2023] ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/streamlit-agent?style=flat-square&label=%20&color=gray)
- [LangChain tutorial: A guide to building LLM-powered applications](https://www.elastic.co/blog/langchain-tutorial) [27 Feb 2024]

### **LangChain features and related libraries**

- [LangChain/cache](https://python.langchain.com/docs/modules/model_io/models/llms/how_to/llm_caching): Reducing the number of API calls
- [LangChain/context-aware-splitting](https://python.langchain.com/docs/use_cases/question_answering/document-context-aware-QA): Splits a file into chunks while keeping metadata
- [LangChain Expression Language](https://python.langchain.com/docs/guides/expression_language/): A declarative way to easily compose chains together [Aug 2023]
- [LangSmith](https://blog.langchain.dev/announcing-langsmith/) Platform for debugging, testing, evaluating. [Jul 2023]
  <!-- <img src="../files/langchain_debugging.png" width="150" /> -->
- [LangChain Template](https://github.com/langchain-ai/langchain/tree/master/templates): LangChain Reference architectures and samples. e.g., `RAG Conversation Template` [Oct 2023]
- [OpenGPTs](https://github.com/langchain-ai/opengpts): An open source effort to create a similar experience to OpenAI's GPTs [Nov 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/opengpts?style=flat-square&label=%20&color=gray)
- [LangGraph](https://github.com/langchain-ai/langgraph):💡Build and navigate language agents as graphs [ref](https://langchain-ai.github.io/langgraph/) [Aug 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square&label=%20&color=gray)

### **LangChain chain type: Chains & Summarizer**

- Chains [ref](https://github.com/RutamBhagat/LangChainHCCourse1/blob/main/course_1/chains.ipynb)
  - SimpleSequentialChain: A sequence of steps with single input and output. Output of one step is input for the next.
  - SequentialChain: Like SimpleSequentialChain but handles multiple inputs and outputs at each step.
  - MultiPromptChain: Routes inputs to specialized sub-chains based on content. Ideal for different prompts for different tasks.
- Summarizer
  - stuff: Sends everything at once in LLM. If it's too long, an error will occur.
  - map_reduce: Summarizes by dividing and then summarizing the entire summary.
  - refine: (Summary + Next document) => Summary
  - map_rerank: Ranks by score and summarizes to important points.

### **LangChain Agent & Memory**

#### LangChain Agent

1. If you're using a text LLM, first try `zero-shot-react-description`.
1. If you're using a Chat Model, try `chat-zero-shot-react-description`.
1. If you're using a Chat Model and want to use memory, try `conversational-react-description`.
1. `self-ask-with-search`: [Measuring and Narrowing the Compositionality Gap in Language Models](https://arxiv.org/abs/2210.03350) [7 Oct 2022]
1. `react-docstore`: [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) [6 Oct 2022]
1. Agent Type

```python
class AgentType(str, Enum):
    """Enumerator with the Agent types."""

    ZERO_SHOT_REACT_DESCRIPTION = "zero-shot-react-description"
    REACT_DOCSTORE = "react-docstore"
    SELF_ASK_WITH_SEARCH = "self-ask-with-search"
    CONVERSATIONAL_REACT_DESCRIPTION = "conversational-react-description"
    CHAT_ZERO_SHOT_REACT_DESCRIPTION = "chat-zero-shot-react-description"
    CHAT_CONVERSATIONAL_REACT_DESCRIPTION = "chat-conversational-react-description"
    STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION = (
        "structured-chat-zero-shot-react-description"
    )
    OPENAI_FUNCTIONS = "openai-functions"
    OPENAI_MULTI_FUNCTIONS = "openai-multi-functions"
```

- [ReAct](https://arxiv.org/abs/2210.03629) vs [MRKL](https://arxiv.org/abs/2205.00445) (miracle)

  ReAct is inspired by the synergies between "acting" and "reasoning" which allow humans to learn new tasks and make decisions or reasoning.

  MRKL stands for Modular Reasoning, Knowledge and Language and is a neuro-symbolic architecture that combines large language models, external knowledge sources, and discrete reasoning

  > cite: [ref](https://github.com/langchain-ai/langchain/issues/2284#issuecomment-1526879904) [28 Apr 2023] <br/>
  `zero-shot-react-description`: Uses ReAct to select tools based on their descriptions. Any number of tools can be used, each requiring a description. <br/>
  `react-docstore`: Uses ReAct to manage a docstore with two required tools: _Search_ and _Lookup_. These tools must be named exactly as specified. It follows the original ReAct paper's example from Wikipedia.
  - MRKL in LangChain uses `zero-shot-react-description`, implementing ReAct. The original ReAct framework is used in the `react-docstore` agent. MRKL was published on May 1, 2022, earlier than ReAct on October 6, 2022.

#### LangChain Memory

1. `ConversationBufferMemory`: Stores the entire conversation history.
1. `ConversationBufferWindowMemory`: Stores recent messages from the conversation history.
1. `Entity Memory`: Stores and retrieves entity-related information.
1. `Conversation Knowledge Graph Memory`: Stores entities and relationships between entities.
1. `ConversationSummaryMemory`: Stores summarized information about the conversation.
1. `ConversationSummaryBufferMemory`: Stores summarized information about the conversation with a token limit.
1. `ConversationTokenBufferMemory`: Stores tokens from the conversation.
1. `VectorStore-Backed Memory`: Leverages vector space models for storing and retrieving information.

#### **Criticism to LangChain**

- The Problem With LangChain: [ref](https://minimaxir.com/2023/07/langchain-problem/) / [git](https://github.com/minimaxir/langchain-problems) [14 Jul 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/minimaxir/langchain-problems?style=flat-square&label=%20&color=gray)
- What’s your biggest complaint about langchain?: [ref](https://www.reddit.com/r/LangChain/comments/139bu99/whats_your_biggest_complaint_about_langchain/) [May 2023]
- LangChain Is Pointless: [ref](https://news.ycombinator.com/item?id=36645575) [Jul 2023]
  > LangChain has been criticized for making simple things relatively complex, which creates unnecessary complexity and tribalism that hurts the up-and-coming AI ecosystem as a whole. The documentation is also criticized for being bad and unhelpful.
- [How to Build Ridiculously Complex LLM Pipelines with LangGraph!](https://newsletter.theaiedge.io/p/how-to-build-ridiculously-complex) [17 Sep 2024 ]
  > LangChain does too much, and as a consequence, it does many things badly. Scaling beyond the basic use cases with LangChain is a challenge that is often better served with building things from scratch by using the underlying APIs.

### **LangChain vs Competitors**

#### **Prompting Frameworks**

- [LangChain](https://github.com/langchain-ai/langchain) [Oct 2022] |  [LlamaIndex](https://github.com/jerryjliu/llama_index) [Nov 2022] |  [Microsoft Semantic Kernel](https://github.com/microsoft/semantic-kernel) [Feb 2023] | [Microsoft guidance](https://github.com/microsoft/guidance) [Nov 2022] | [Azure ML Promt flow](https://github.com/microsoft/promptflow) [Jun 2023] | [DSPy](https://github.com/stanfordnlp/dspy) [Jan 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square&label=%20&color=gray) ![GitHub Repo stars](https://img.shields.io/github/stars/jerryjliu/llama_index?style=flat-square&label=%20&color=gray) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/semantic-kernel?style=flat-square&label=%20&color=gray) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/guidance?style=flat-square&label=%20&color=gray) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/promptflow?style=flat-square&label=%20&color=gray) ![GitHub Repo stars](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat-square&label=%20&color=gray)
- [Prompting Framework (PF)](https://arxiv.org/abs/2311.12785): Prompting Frameworks for Large Language Models: A Survey [git](https://github.com/lxx0628/Prompting-Framework-Survey)
 ![GitHub Repo stars](https://img.shields.io/github/stars/lxx0628/Prompting-Framework-Survey?style=flat-square&label=%20&color=gray)
- [What Are Tools Anyway?](https://arxiv.org/abs/2403.15452): 1. For a small number (e.g., 5–10) of tools, LMs can directly select from contexts. However, with a larger number (e.g., hundreds), an additional retrieval step involving a retriever model is often necessary. 2. LM-used tools incl. Tool creation and reuse. Tool is not useful when machine translation, summarization, and sentiment analysis (among others).  3. Evaluation metrics [18 Mar 2024]

#### **LangChain vs LlamaIndex**

- Basically LlamaIndex is a smart storage mechanism, while LangChain is a tool to bring multiple tools together. [cite](https://community.openai.com/t/llamaindex-vs-langchain-which-one-should-be-used/163139) [14 Apr 2023]

- LangChain offers many features and focuses on using chains and agents to connect with external APIs. In contrast, LlamaIndex is more specialized and excels at indexing data and retrieving documents.

#### **LangChain vs Semantic Kernel**

| LangChain | Semantic Kernel                                                                |
| --------- | ------------------------------------------------------------------------------ |
| Memory    | Memory                                                                         |
| Tookit    | Plugin (pre. Skill)                                                            |
| Tool      | LLM prompts (semantic functions) <br/> native C# or Python code (native function) |
| Agent     | Planner (Deprecated) -> Agent                                                                        |
| Chain     | Steps, Pipeline                                                                |
| Tool      | Connector (Deprecated) -> Plugin                                                                     |

#### **LangChain vs Semantic Kernel vs Azure Machine Learning Prompt flow**

- What's the difference between LangChain and Semantic Kernel?

  LangChain has many agents, tools, plugins etc. out of the box. More over, LangChain has 10x more popularity, so has about 10x more developer activity to improve it. On other hand, **Semantic Kernel architecture and quality is better**, that's quite promising for Semantic Kernel. [ref](https://github.com/microsoft/semantic-kernel/discussions/1326) [11 May 2023]

- What's the difference between Azure Machine Learing PromptFlow and Semantic Kernel?

  1. Low/No Code vs C#, Python, Java
  1. Focused on Prompt orchestrating vs Integrate LLM into their existing app.

- Promptflow is not intended to replace chat conversation flow. Instead, it’s an optimized solution for integrating Search and Open Source Language Models. By default, it supports Python, LLM, and the Prompt tool as its fundamental building blocks.

- Using Prompt flow with Semantic Kernel: [ref](https://learn.microsoft.com/en-us/semantic-kernel/ai-orchestration/planners/evaluate-and-deploy-planners/) [07 Sep 2023]

#### **Prompt Template Language**

|                   | Handlebars.js                                                                 | Jinja2                                                                                 | Prompt Template                                                                                    |
| ----------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Conditions        | {{#if user}}<br>  Hello {{user}}!<br>{{else}}<br>  Hello Stranger!<br>{{/if}} | {% if user %}<br>  Hello {{ user }}!<br>{% else %}<br>  Hello Stranger!<br>{% endif %} | Branching features such as "if", "for", and code blocks are not part of SK's template language.    |
| Loop              | {{#each items}}<br>  Hello {{this}}<br>{{/each}}                              | {% for item in items %}<br>  Hello {{ item }}<br>{% endfor %}                          | By using a simple language, the kernel can also avoid complex parsing and external dependencies.   |
| LangChain Library | guidance. LangChain.js                                                                     | LangChain, Azure ML prompt flow                                                                | Semantic Kernel                                                                                    |
| URL               | [ref](https://handlebarsjs.com/guide/)                                        | [ref](https://jinja.palletsprojects.com/en/2.10.x/templates/)                          | [ref](https://learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/prompt-template-syntax) |

- Semantic Kernel supports HandleBars and Jinja2. [Mar 2024]


### **LlamaIndex**

- LlamaIndex (formerly GPT Index) is a data framework for LLM applications to ingest, structure, and access private or domain-specific data. The high-level API allows users to ingest and query their data in a few lines of code. High-Level Concept: [ref](https://docs.llamaindex.ai/en/latest/getting_started/concepts.html) / doc:[ref](https://gpt-index.readthedocs.io/en/latest/index.html) / blog:[ref](https://www.llamaindex.ai/blog) / [git](https://github.com/run-llama/llama_index) [Nov 2022]
 ![GitHub Repo stars](https://img.shields.io/github/stars/run-llama/llama_index?style=flat-square&label=%20&color=gray)

  > Fun fact this core idea was the initial inspiration for GPT Index (the former name of LlamaIndex) 11/8/2022 - almost a year ago!. [cite](https://twitter.com/jerryjliu0/status/1711817419592008037) / [Walking Down the Memory Maze: Beyond Context Limit through Interactive Reading](https://arxiv.org/abs/2310.05029)
  >
  > 1.  Build a data structure (memory tree)
  > 1.  Transverse it via LLM prompting

- LlamaIndex Toolkits: 
  - `LlamaHub`: A library of data loaders for LLMs [git](https://github.com/run-llama/llama-hub) [Feb 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/run-llama/llama-hub?style=flat-square&label=%20&color=gray)
  - `LlamaIndex CLI`: a command line tool to generate LlamaIndex apps [ref](https://llama-2.ai/llamaindex-cli/) [Nov 2023]
  - `LlamaParse`: A unique parsing tool for intricate documents [git](https://github.com/run-llama/llama_parse) [Feb 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/run-llama/llama_parse?style=flat-square&label=%20&color=gray)

#### LlamaIndex integration with Azure AI

- [LlamaIndex integration with Azure AI](https://www.llamaindex.ai/blog/announcing-the-llamaindex-integration-with-azure-ai):  [19 Nov 2024]
- Core: Azure OpenAI Service, Azure AI Search
- Storage and memory: [Azure Table Storage as a Docstore](https://docs.llamaindex.ai/en/stable/examples/docstore/AzureDocstoreDemo/) or Azure Cosmos DB.
- Workflow example: [Azure Code Interpreter](https://docs.llamaindex.ai/en/stable/examples/tools/azure_code_interpreter/)
- [AI App Template Gallery](https://azure.github.io/ai-app-templates/repo/azure-samples/llama-index-javascript/)

#### High-Level Concepts

- Query engine vs Chat engine

  1. The query engine wraps a `retriever` and a `response synthesizer` into a pipeline, that will use the query string to fetch nodes (sentences or paragraphs) from the index and then send them to the LLM (Language and Logic Model) to generate a response
  1. The chat engine is a quick and simple way to chat with the data in your index. It uses a `context manager` to keep track of the conversation history and generate relevant queries for the retriever. Conceptually, it is a `stateful` analogy of a Query Engine.

- Storage Context vs Settings (p.k.a. Service Context)

  - Both the Storage Context and Service Context are data classes.

    1. Introduced in v0.10.0, ServiceContext is replaced to Settings object.
    1. Storage Context is responsible for the storage and retrieval of data in Llama Index, while the Service Context helps in incorporating external context to enhance the search experience.
    1. The Service Context is not directly involved in the storage or retrieval of data, but it helps in providing a more context-aware and accurate search experience.

  ```python
  # The storage context container is a utility container for storing nodes, indices, and vectors.
  class StorageContext:
    docstore: BaseDocumentStore
    index_store: BaseIndexStore
    vector_store: VectorStore
    graph_store: GraphStore
  ```

  ```python
  # NOTE: Deprecated, use llama_index.settings.Settings. The service context container is a utility container for LlamaIndex index and query classes.
  class ServiceContext:
    llm_predictor: BaseLLMPredictor
    prompt_helper: PromptHelper
    embed_model: BaseEmbedding
    node_parser: NodeParser
    llama_logger: LlamaLogger
    callback_manager: CallbackManager
  ```

  ```python
  @dataclass
  class _Settings:
    # lazy initialization
    _llm: Optional[LLM] = None
    _embed_model: Optional[BaseEmbedding] = None
    _callback_manager: Optional[CallbackManager] = None
    _tokenizer: Optional[Callable[[str], List[Any]]] = None
    _node_parser: Optional[NodeParser] = None
    _prompt_helper: Optional[PromptHelper] = None
    _transformations: Optional[List[TransformComponent]] = None
  ```

#### LlamaIndex Tutorial

- [LlamaIndex Overview (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-001-overview-v0-7-9/) [17 Jul 2023]
- [Fine-Tuning a Linear Adapter for Any Embedding Model](https://medium.com/llamaindex-blog/fine-tuning-a-linear-adapter-for-any-embedding-model-8dd0a142d383): Fine-tuning the embeddings model requires you to reindex your documents. With this approach, you do not need to re-embed your documents. Simply transform the query instead. [7 Sep 2023]
- 4 RAG techniques implemented in `llama_index` / [cite](https://x.com/ecardenas300/status/1704188276565795079) [20 Sep 2023] / [git](https://github.com/weaviate/recipes)
 ![GitHub Repo stars](https://img.shields.io/github/stars/weaviate/recipes?style=flat-square&label=%20&color=gray)
  <details open>
  <summary>Expand: 4 RAG techniques</summary>

    1. SQL Router Query Engine: Query router that can reference your vector database or SQL database

    2. Sub Question Query Engine: Break down the complex question into sub-questions

    3. Recursive Retriever + Query Engine: Reference node relationships, rather than only finding a node (chunk) that is most relevant.
    
    4. Self Correcting Query Engines: Use an LLM to evaluate its own output.
  </details>
- [LlamaIndex Tutorial](https://nanonets.com/blog/llamaindex/): A Complete LlamaIndex Guide [18 Oct 2023]
<!-- - [CallbackManager (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-003-callback-manager/) [27 May 2023] / [Customize TokenTextSplitter (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-002-text-splitter/) [27 May 2023] / --> 
- [Chat engine ReAct mode](https://gpt-index.readthedocs.io/en/stable/examples/chat_engine/chat_engine_react.html), [FLARE Query engine](https://docs.llamaindex.ai/en/stable/examples/query_engine/flare_query_engine.html)
- [Building and Productionizing RAG](https://docs.google.com/presentation/d/1rFQ0hPyYja3HKRdGEgjeDxr0MSE8wiQ2iu4mDtwR6fc/edit#slide=id.p): [doc](../files/archive/LlamaIndexTalk_PyDataGlobal.pdf): Optimizing RAG Systems 1. Table Stakes 2. Advanced Retrieval: Small-to-Big 3. Agents 4. Fine-Tuning 5. Evaluation [Nov 2023]
- Multimodal RAG Pipeline [ref](https://blog.llamaindex.ai/multi-modal-rag-621de7525fea) [Nov 2023]
- [A Cheat Sheet and Some Recipes For Building Advanced RAG](https://blog.llamaindex.ai/a-cheat-sheet-and-some-recipes-for-building-advanced-rag-803a9d94c41b) RAG cheat sheet shared above was inspired by [RAG survey paper](https://arxiv.org/abs/2312.10997). [doc](../files/advanced-rag-diagram-llama-index.png) [Jan 2024]

