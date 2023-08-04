
`updated: 08/04/2023`

# Azure OpenAI + LLM (Large language model)

This repository contains references to open-source models similar to ChatGPT, as well as Langchain and prompt engineering libraries. It also includes related samples and research on Langchain, Vector Search (including feasibility checks on Elasticsearch, Azure Cognitive Search, Azure Cosmos DB), and more.

> Not being able to keep up with and test every recent update, sometimes I simply copied them into this repository for later review. `some code might be outdated.`

> `Rule: Brief each item on one or a few lines as much as possible.`

## What's the difference between Azure OpenAI and OpenAI?

1. OpenAI is a better option if you want to use the latest features like function calling, plug-ins, and access to the latest models.
1. Azure OpenAI is recommended if you require a reliable, secure, and compliant environment.
1. Azure OpenAI provides seamless integration with other Azure services..
1. Azure OpenAI offers `private networking` and `role-based authentication`, and responsible `AI content filtering`.
1. Azure OpenAI provides a Service Level Agreement (SLA) that guarantees a certain level of uptime and support for the service.
1. Azure OpenAI does not use user input as training data for other customers. [Data, privacy, and security for Azure OpenAI](https://learn.microsoft.com/en-us/legal/cognitive-services/openai/data-privacy)

- [What is Azure OpenAI Service?](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview)

- [Open AI Models](https://platform.openai.com/docs/models)

## Table of contents

- **Section 1** : LlamaIndex & Vector Storage (Database)
  - [LlamaIndex](#llamaindex)
  - [LlamaIndex Deep Dive](#llamaindex-deep-dive)
  - [Vector Storage Comparison](#vector-storage-comparison)
  - [Vector Storage Options for Azure](#vector-storage-options-for-azure)
  - [Milvus Embedded](#milvus-embedded)
  - [Conclusion](#conclusion)
- **Section 2** : Azure OpenAI and RAG demo
  - [Microsoft LLM Framework & Copilot Stack](#microsoft-azure-openai-relevant-llm-framework--copilot-stack)
  - [ChatGPT + Enterprise data Demo Configuration](#rag-retrieval-augmented-generation-demo-configuration)
  - [Azure OpenAI samples](#azure-openai-samples)
  - [Another Reference Architectures / Tech community](#another-reference-architectures--tech-community)
  - [Azure Cognitive Search : Vector Search](#azure-cognitive-search--vector-search)
  - [Bing Chat Enterprise & Azure OpenAI Service On Your Data in Public Preview](#bing-chat-enterprise--azure-openai-service-on-your-data-in-public-preview)
- **Section 3** : Microsoft Semantic Kernel
  - [Semantic Kernel](#semantic-kernel)
  - [Bing search Web UI and Semantic Kernel sample code](#bing-search-web-ui-and-semantic-kernel-sample-code)
- **Section 4** : Langchain & Its Competitors
  - [Langchain Feature Matrix & Cheetsheet](#langchain-feature-matrix--cheetsheet)
  - [Langchain Impressive features](#langchain-impressive-features): cache, context-aware-splitting
  - [Langchain quick start](#langchain-quick-start-how-to-use-and-useful-utilities): Sample code
  - [Langchain chain type: Summarizer](#langchain-chain-type-summarizer)
  - [Langchain Agent](#langchain-agent)
  - [Langsmith & Langchain low code](#langsmith--langchain-low-code): Drag-and-Drop Workflow, LangSmith for LLM debugging
  - Langchain vs Its Competitors
    - [Lanchain vs LlamaIndex](#langchain-vs-llamaindex)
    - [Langchain vs Semantic Kernel](#langchain-vs-semantic-kernel)
    - [Semantic Kernel : Semantic Function](#semantic-kernel--semantic-function)
    - [Semantic Kernel : Prompt Template language key takeaways](#semantic-kernel--prompt-template-language-key-takeaways)
    - [Semantic Kernel Glossary](#semantic-kernel-glossary)
    - [Langchain vs Semantic Kernel vs Azure Machine Learning - Prompt flow](#langchain-vs-semantic-kernel-vs-azure-machine-learning-prompt-flow)
    - [Prompt template language](#prompt-template-language): Handlebars.js vs Jinja2
- **Section 5**: Prompt Engineering & Finetuning
  - Prompt Engineering
    - [Prompt Engineering](#prompt-engineering)
    - [Azure OpenAI Prompt Guide](#azure-openai-prompt-guide)
    - [OpenAI Prompt Guide](#openai-prompt-guide)
    - [DeepLearning.ai Prompt Engineering Course and others](#deeplearningai-prompt-engineering-course-and-others)
    - [Awesome ChatGPT Prompts](#awesome-chatgpt-prompts)
    - [ChatGPT : “user”, “assistant”, and “system” messages.](#chatgpt--user-assistant-and-system-messages)
  - Finetuning
    - [Finetuning](#finetuning) : PEFT - LoRA - QLoRA
    - [Llama2 Finetuning](#llama2-finetuning): Llama 2
    - [RLHF（Reinforcement Learning from Human Feedback) & SFT](#rlhf-reinforcement-learning-from-human-feedback--sft-supervised-fine-tuning): TRL, trlX, Argilla
    - [Quantization](#quantization): [ref](README_SBCs.md) : Quantization & Run ChatGPT on a Raspberry Pi / Android
    - [Sparsification](#sparsification)
    - [Small size with Textbooks](#small-size-with-textbooks-high-quality-synthetic-dataset): High quality synthetic dataset
  - [Visual Prompting](#visual-prompting)
- **Section 6:** LLM Enhancement
  - [Context Constraints](#context-constraints): Large Context Windows, RoPE
  - OpenAI's plans
    - [OpenAI's plans according to Sam Altman](#openais-plans-according-to-sam-altman) Humanloop interview has been removed from the site. Instead of that, Web-archived link.
    - [OpenAI Plugin and function calling](#openai-plugin-and-function-calling)
    - [OSS Alternatives for OpenAI Code Interpreter](#oss-alternatives-for-openai-code-interpreter)
  - Data Extraction methods for the context
    - [Math problem-solving skill](#math-problem-solving-skill)
    - [Table Extraction](#table-extraction): Extract Tables from PDFs
    - [Token counting & Token-limits](#token-counting--token-limits): 5 Approaches To Solve LLM Token Limits
  - [Avoid AI hallucination](#avoid-ai-hallucination) Building Trustworthy, Safe and Secure LLM
  - [Gorilla: An API store for LLMs](#gorilla-an-api-store-for-llms)
  - [Memory Optimization](#memory-optimization): PagedAttention & Flash Attention
- **Section 7:** List of OSS LLM & Generative AI Landscape
  - [Evolutionary Graph of LLaMA Family / LLM evolutionary tree](#evolutionary-graph-of-llama-family--llm-evolutionary-tree)
  - [Generative AI Revolution: Exploring the Current Landscape](#generative-ai-revolution-exploring-the-current-landscape)
  - [List of OSS LLM](#list-of-oss-llm)
  - [Huggingface Open LLM Learboard](#huggingface-open-llm-learboard)
  - [Huggingface Transformer](#huggingface-transformer)
  - [Huggingface StarCoder](#huggingface-starcoder)
- **Section 8** : References
  - [picoGPT](#picogpt) : tiny implementation of GPT-2.
  - [AutoGPT / Communicative Agents](#autogpt--communicative-agents)
  - [Large Language and Vision Assistant](#large-language-and-vision-assistant)
  - [MLLM (multimodal large language model)](#mllm-multimodal-large-language-model)
  - [Application UI/UX](#application-uiux)
  - [Awesome demo](#awesome-demo) Prompt to Game - E2E game creation
  - [日本語（Japanese Materials)](#日本語japanese-materials)
- **Section 9** : Relevant solutions and resources
  - [Microsoft Fabric](README_Fabric.md): Single unified data analytics solution
  - [Office Copilot](#section-9--relevant-solutions-and-resources): Semantic Interpreter, Natural Language Commanding via Program Synthesis
  - [microsoft/unilm](#section-9--relevant-solutions-and-resources): Microsoft Foundation models
- **Section 10** : AI Tools
  - [AI Tools](#section-10--ai-tools)
- **Section 11** : Datasets for LLM Training
  - [Datasets for LLM Training](#section-11--datasets-for-llm-training)

- **Acknowledgements**
  - [Acknowledgements](#acknowledgements): -

## **Section 1** : LlamaIndex and Vector Storage (Database)

- LlamaIndex (formerly GPT Index) is a data framework for LLM applications to ingest, structure, and access private or domain-specific data. The high-level API allows users to ingest and query their data in a few lines of code. [doc][llama-index-doc]

### **LlamaIndex**

- This section has been created for testing and feasibility checks using elastic search as a vector database and integration with LlamaIndex. LlamaIndex is specialized in integration layers to external data sources.

  - index.json : Vector data local backup created by llama-index
  - index_vector_in_opensearch.json : Vector data stored in Open search (Source: `files\all_h1.pdf`)
  - llama-index-azure-elk-create.py: llama-index ElasticsearchVectorClient (Unofficial file to manipulate vector search, Created by me, Not Fully Tested)
  - llama-index-lang-chain.py : Lang chain memory and agent usage with llama-index
  - llama-index-opensearch-create.py : Vector index creation to Open search
  - llama-index-opensearch-query-chatgpt.py : Test module to access Azure Open AI Embedding API.
  - llama-index-opensearch-query.py : Vector index query with questions to Open search
  - llama-index-opensearch-read.py : llama-index ElasticsearchVectorClient (Unofficial file to manipulate vector search, Created by me, Not Fully Tested)
  - env.template : The properties. Change its name to `.env` once your values settings is done.
  - Opensearch & Elasticsearch setup
    - docker : Opensearch Docker-compose
    - docker-elasticsearch : Not working for ES v8, requiring security plug-in with mandatory
    - docker-elk : Elasticsearch Docker-compose, Optimized Docker configurations with solving security plug-in issues.
    - es-open-search-set-analyzer.py : Put Language analyzer into Open search
    - es-open-search.py : Open search sample index creation
    - es-search-set-analyzer.py : Put Language analyzer into Elastic search
    - es-search.py : Usage of Elastic search python client
    - files : The Sample file for consuming

### **LlamaIndex example**

- llama-index-es-handson\callback-debug-handler.py: callback debug handler
- llama-index-es-handson\chat-engine-flare-query.py: FLARE
- llama-index-es-handson\chat-engine-react.py: ReAct
- llama-index-es-handson\milvus-create-query.py: Milvus Vector storage

### **LlamaIndex Deep dive**

- [CallbackManager (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-003-callback-manager/)

- [Customize TokenTextSplitter (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-002-text-splitter/)

- [Chat engine - ReAct mode](https://gpt-index.readthedocs.io/en/stable/examples/chat_engine/chat_engine_react.html)

### **Vector Storage Comparison**

- [Not All Vector Databases Are Made Equal](https://towardsdatascience.com/milvus-pinecone-vespa-weaviate-vald-gsi-what-unites-these-buzz-words-and-what-makes-each-9c65a3bd0696)
- Printed version for "Medium" limits. - [Link](files/vector-dbs.pdf)

### **Vector Storage Options for Azure**

- [Pgvector extension on Azure Cosmos DB for PostgreSQL](https://azure.microsoft.com/en-us/updates/generally-available-pgvector-extension-on-azure-cosmos-db-for-postgresql/): Langchain Document [URL](https://python.langchain.com/docs/modules/data_connection/vectorstores/integrations/pgvector)
- [Vector Search in Azure Cosmos DB for MongoDB vCore](https://devblogs.microsoft.com/cosmosdb/introducing-vector-search-in-azure-cosmos-db-for-mongodb-vcore/)
- [Vector search (private preview) - Azure Cognitive Search](https://github.com/Azure/cognitive-search-vector-pr): Langchain Document [URL](https://python.langchain.com/docs/modules/data_connection/vectorstores/integrations/azuresearch)
- [Azure Cache for Redis Enterprise](https://techcommunity.microsoft.com/t5/azure-developer-community-blog/introducing-vector-search-similarity-capabilities-in-azure-cache/ba-p/3827512): Enterprise [Redis Vector Search Demo](https://ecommerce.redisventures.com/)

  [![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2Fkimtth%2Fazure-openai-elastic-vector-langchain%2Fmain%2Finfra%2Fdeployment.json)

  **Note**: Azure Cache for Redis Enterprise: Enterprise Sku series are not able to deploy by a template such as Bicep and ARM.

- azure-vector-db-python\vector-db-in-azure-native.ipynb: sample code for vector databases in azure

### **Milvus Embedded**

 `[JMO]`: Milvus looks like the best alternative option to replace PineCone and Redis Search in OSS. It offers support for multiple languages, addresses the limitations of RedisSearch, and provides cloud scalability and high reliability with Kubernetes. However, for local and small-scale applications, [Chroma](https://github.com/chroma-core/chroma) has positioned itself as the SQLite in vector databases.

- `pip install milvus`
- Docker compose: <https://milvus.io/docs/install_offline-docker.md>
- Milvus Embedded through python console only works in Linux and Mac OS.
- In Windows, Use this link, <https://github.com/matrixji/milvus/releases>.

  ```commandline
  # Step 1. Start Milvus

  1. Unzip the package
  Unzip the package, and you will find a milvus directory, which contains all the files required.

  2. Start a MinIO service
  Double-click the run_minio.bat file to start a MinIO service with default configurations. Data will be stored in the subdirectory s3data.

  3. Start an etcd service
  Double-click the run_etcd.bat file to start an etcd service with default configurations.

  4. Start Milvus service
  Double-click the run_milvus.bat file to start the Milvus service.

  # Step 2. Run hello_milvus.py

  After starting the Milvus service, you can test by running hello_milvus.py. See Hello Milvus for more information.
  ```

### **Conclusion**

- Azure Open AI Embedding API, `text-embedding-ada-002`, supports 1536 dimensions. Elastic search, Lucene based engine, supports 1024 dimensions as a max. Open search can insert 16,000 dimensions as a vector storage. Open search is available to use as a vector database with Azure Open AI Embedding API.

- @citation: open ai documents:
text-embedding-ada-002:
Smaller embedding size. The new embeddings have only 1536 dimensions, one-eighth the size of davinci-001 embeddings,
making the new embeddings more cost effective in working with vector databases.
<https://openai.com/blog/new-and-improved-embedding-model>

- @citation: [open search documents](https://opensearch.org/docs/latest/):
However, one exception to this is that the maximum dimension count for the Lucene engine is 1,024, compared with
16,000 for the other engines. <https://opensearch.org/docs/latest/search-plugins/knn/approximate-knn/>

- @LlamaIndex `ElasticsearchReader` class:
The name of the class in LlamaIndex is `ElasticsearchReader`. However, actually, it can only work with open search.

## **Section 2** : Azure OpenAI and RAG demo

### **Microsoft Azure OpenAI relevant LLM Framework & Copilot Stack**

  1. [Semantic Kernel][semantic-kernel]: Semantic Kernel is an open-source SDK that lets you easily combine AI services like OpenAI, Azure OpenAI, and Hugging Face with conventional programming languages like C# and Python. An LLM Ochestrator, similar to Langchain. / [git][semantic-kernel-git]
  1. [guidance][guidance]: A guidance language for controlling large language models. Simple, intuitive syntax, based on Handlebars templating. Domain Specific Language (DSL) for handling model interaction. Langchain libaries but different approach rather than ochestration, particularly effective for implementing  `Chain of Thought`. / [git][guidance]
  1. [Azure Machine Learning Promt flow][promptflow]: Visual Designer for Prompt crafting. Use [Jinja](https://github.com/pallets/jinja) as a prompt template language. / [doc][promptflow-doc]
  1. [Prompt Engine][prompt-engine]: Craft prompts for Large Language Models: `npm install prompt-engine` / [git][prompt-engine] / [python][prompt-engine-py]
  1. [TypeChat][typechat]: TypeChat replaces prompt engineering with schema engineering. To build natural language interfaces using types. / [git][typechat-git]
  1. [DeepSpeed][deepspeed]: DeepSpeed is a deep learning optimization library that makes distributed training and inference easy, efficient, and effective.
  1. [LMOps][LMOps]: a collection of tools for improving text prompts used as input to generative AI models. The toolkit includes [Promptist][Promptist], which optimizes a user's text input for text-to-image generation, and [Structured Prompting][Structured Prompting].
  1. Copilot Stack: [Microsoft 365 Copilot][m365-copilot], [Dynamics 365 Copilot][d365-copilot], [Copilot in Microsoft Viva][viva-copilot] and [Microsoft Security Copilot][sec-copilot]

### **RAG (Retrieval-Augmented Generation) Demo Configuration**

The files in this directory, `extra_steps`, have been created for managing extra configurations and steps for launching the demo repository.

<https://github.com/Azure-Samples/azure-search-openai-demo> : Python, ReactJs, Typescript

  <img src="files/capture_azure_demo.png" alt="sk" width="300"/>

1. (optional) Check Azure module installation in Powershell by running `ms_internal_az_init.ps1` script
2. (optional) Set your Azure subscription Id to default

    > Start the following commands in `./azure-search-openai-demo` directory

3. (deploy azure resources) Simply Run `azd up`

    The azd stores relevant values in the .env file which is stored at `${project_folder}\.azure\az-search-openai-tg\.env`.

4. Move to `app` by `cd app` command
5. (sample data loading) Move to `scripts` then Change into Powershell by `Powershell` command, Run `prepdocs.ps1`

    - console output (excerpt)

      ```commandline
              Uploading blob for page 29 -> role_library-29.pdf
              Uploading blob for page 30 -> role_library-30.pdf
      Indexing sections from 'role_library.pdf' into search index 'gptkbindex'
      Splitting './data\role_library.pdf' into sections
              Indexed 60 sections, 60 succeeded
      ```

6. Move to `app` by `cd ..` and `cd app` command
7. (locally running) Run `start.cmd`

- console output (excerpt)

  ```commandline
  Building frontend


  > frontend@0.0.0 build \azure-search-openai-demo\app\frontend
  > tsc && vite build

  vite v4.1.1 building for production...
  ✓ 1250 modules transformed.
  ../backend/static/index.html                    0.49 kB
  ../backend/static/assets/github-fab00c2d.svg    0.96 kB
  ../backend/static/assets/index-184dcdbd.css     7.33 kB │ gzip:   2.17 kB
  ../backend/static/assets/index-41d57639.js    625.76 kB │ gzip: 204.86 kB │ map: 5,057.29 kB

  Starting backend

  * Serving Flask app 'app'
  * Debug mode: off
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
  * Running on http://127.0.0.1:5000
  Press CTRL+C to quit
  ...
  ```

Running from second times

1. Move to `app` by `cd ..` and `cd app` command
2. (locally running) Run `start.cmd`

(optional)

- fix_from_origin : The modified files, setup related
- ms_internal_az_init.ps1 : Powershell script for Azure module installation
- ms_internal_troubleshootingt.ps1 : Set Specific Subscription Id as default

### **Azure OpenAI samples**

- Azure OpenAI samples: [Link](https://github.com/Azure/azure-openai-samples)

- The repository for all Azure OpenAI Samples complementing the OpenAI cookbook.: [Link](https://github.com/Azure/openai-samples)

- Azure-Samples [Link](https://github.com/Azure-Samples)

  - Azure OpenAI with AKS By Terraform: <https://github.com/Azure-Samples/aks-openai-terraform>
  - Azure OpenAI with AKS By Bicep: <https://github.com/Azure-Samples/aks-openai>
  - Enterprise Logging: <https://github.com/Azure-Samples/openai-python-enterprise-logging>
  - Azure OpenAI with AKS by Terraform (simple version): <https://github.com/Azure-Samples/azure-openai-terraform-deployment-sample>
  - ChatGPT Plugin Quickstart using Python and FastAPI: <https://github.com/Azure-Samples/openai-plugin-fastapi>

- Azure OpenAI Network Latency Test Script
  : [Link](https://github.com/wloryo/networkchatgpt/blob/dc76f2264ff8c2a83392e6ae9ee2aaa55ca86f0e/openai_network_latencytest_nocsv_pub_v1.1.py)

### **Another Reference Architectures / Tech community**

|                                                                                                                                                        |                                                                                                                                  |
|:------------------------------------------------------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------------------------------:|
| [Azure OpenAI Embeddings QnA](https://github.com/Azure-Samples/azure-open-ai-embeddings-qna)                                                          |  [Azure Cosmos DB + OpenAI ChatGPT](https://github.com/Azure-Samples/cosmosdb-chatgpt) C# blazor and Azure Custom Template       |
| <img src="files/demo-architecture.png" alt="embeddin_azure_csharp" width="300"/>                                                                       |  <img src="files/cosmos-gpt.png" alt="gpt-cosmos" width="300"/>                                                                  |
| [C# Implementation](https://github.com/Azure-Samples/azure-search-openai-demo-csharp) ChatGPT + Enterprise data with Azure OpenAI and Cognitive Search |  [Simple ChatGPT UI application](https://github.com/Azure/openai-at-scale) Typescript, ReactJs and Flask                         |
| <img src="files/demo-architecture-csharp2.png" alt="embeddin_azure_csharp" width="300"/>                                                               |  <img src="files/chatscreen.png" alt="gpt-cosmos" width="300"/>                                                                  |
| [Azure Video Indexer demo](https://aka.ms/viopenaidemo) Azure Video Indexer + OpenAI |            [Miyagi](https://github.com/Azure-Samples/miyagi) Integration demonstrate for multiple langchain libraries            |
| <img src="files/demo-videoindexer.png" alt="demo-videoindexer" width="300"/> |                    <img src="files/wip-azure.png" alt="miyagi" width="300"/>                                              |

- Azure Open AI work with Cognitive Search act as a Long-term memory

  1. [ChatGPT + Enterprise data with Azure OpenAI and Cognitive Search](https://github.com/Azure-Samples/azure-search-openai-demo)
  1. [Can ChatGPT work with your enterprise data?](https://www.youtube.com/watch?v=tW2EA4aZ_YQ)
  1. [Azure OpenAI と Azure Cognitive Search の組み合わせを考える](https://qiita.com/nohanaga/items/59e07f5e00a4ced1e840)

- Tech community
  1. [Grounding LLMs](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/grounding-llms/ba-p/3843857): Retrieval-Augmented Generation (RAG)
  1. [Revolutionize your Enterprise Data with ChatGPT](https://techcommunity.microsoft.com/t5/ai-applied-ai-blog/revolutionize-your-enterprise-data-with-chatgpt-next-gen-apps-w/ba-p/3762087)
  1. [Check Your Facts and Try Again: Improving Large Language Models with External Knowledge and Automated Feedback](https://www.microsoft.com/en-us/research/group/deep-learning-group/articles/check-your-facts-and-try-again-improving-large-language-models-with-external-knowledge-and-automated-feedback/)

### **Azure Cognitive Search : Vector Search**

- [Azure Cognitive Search : Vector Search](https://github.com/Azure/cognitive-search-vector-pr)

- Azure Cognitive Search supports

  1. Text Search
  1. Pure Vector Search
  1. Hybrid Search (Text search + Vector search)
  1. Semantic Hybrid Search (Text search + Semantic search + Vector search)

- azure-search-vector-sample\azure-search-vector-python-sample.ipynb: Azure Cognitive Search - Vector and Hybrid Search

### **Bing Chat Enterprise & Azure OpenAI Service On Your Data in Public Preview**

- Bing Chat Enterprise [Privacy and Protection](https://learn.microsoft.com/en-us/bing-chat-enterprise/privacy-and-protections#protected-by-default)
  1. Bing Chat Enterprise doesn't have plugin support
  2. Only content provided in the chat by users is accessible to Bing Chat Enterprise.
- Azure OpenAI Service On Your Data in Public Preview [Link](https://techcommunity.microsoft.com/t5/ai-cognitive-services-blog/introducing-azure-openai-service-on-your-data-in-public-preview/ba-p/3847000)

## **Section 3** : Microsoft Semantic Kernel

- Microsoft Langchain Library supports C# and Python and offers several features, some of which are still in development and may be unclear on how to implement. However, it is simple, stable, and faster than Python-based open-source software. The features listed on the link include: [Semantic Kernel Feature Matrix](https://github.com/microsoft/semantic-kernel/blob/main/FEATURE_MATRIX.md)

<!-- <img src="files/mind-and-body-of-semantic-kernel.png" alt="sk" width="130"/> -->
<!-- <img src="files/sk-flow.png" alt="sk" width="500"/> -->

### **Semantic Kernel**

- This section includes how to utilize Azure Cosmos DB for vector storage and vector search by leveraging the SemanticKernel.

  - appsettings.template.json : Environment value configuration file.
  - ComoseDBVectorSearch.cs : Vector Search using Azure Cosmos DB
  - CosmosDBKernelBuild.cs : Kernel Build code (test)
  - CosmosDBVectorStore.cs : Embedding Text and store it to Azure Cosmos DB
  - LoadDocumentPage.cs : PDF splitter class. Split the text to unit of section. (C# version of `azure-search-openai-demo/scripts/prepdocs.py`)
  - LoadDocumentPageOutput : LoadDocumentPage class generated output
  - MemoryContextAndPlanner.cs : Test code of context and planner
  - MemoryConversationHistory.cs : Test code of conversation history
  - Program.cs : Run a demo. Program Entry point
  - SemanticFunction.cs : Test code of conversation history
  - semanticKernelCosmos.csproj : C# Project file
  - Settings.cs : Environment value class
  - SkillBingSearch.cs : Bing Search Skill
  - SkillDALLEImgGen.cs : DALLE Skill

### **Semantic Kernel Notes**

- Semantic Kernel Planner

  <img src="files\sk-evolution_of_planners.jpg" alt="sk-plan" width="300"/>

- Is Semantic Kernel Planner the same as LangChain agents?

    > Planner in SK is not the same as Agents in LangChain. [@cite](https://github.com/microsoft/semantic-kernel/discussions/1326)

    ```comment
    Agents in LangChain use recursive calls to the LLM to decide the next step to take based on the current state.

    The two planner implementations in SK are not self-correcting.

      Sequential planner tries to produce all the steps at the very beginning, so it is unable to handle unexpected errors.
      Action planner only chooses one tool to satisfy the goal
    ```

    `[JMO]`: Stepwise Planner could be have the self-correcting.

- Semantic Kernel supports Azure Cognitive Search Vector Search. `July 19th, 2023` [Dev Blog](https://devblogs.microsoft.com/semantic-kernel)

- SemanticKernel Implementation sample to overcome Token limits of Open AI model.
Semantic Kernel でトークンの限界を超えるような長い文章を分割してスキルに渡して結果を結合したい (zenn.dev)
[Semantic Kernel でトークンの限界を超える](https://zenn.dev/microsoft/articles/semantic-kernel-10)

### **Bing search Web UI and Semantic Kernel sample code**

- Semantic Kernel sample code to integrate with Bing Search

  `\ms-semactic-bing-notebook`

  - gs_chatgpt.ipynb: Azure Open AI ChatGPT sample to use Bing Search
  - gs_davinci.ipynb: Azure Open AI Davinci sample to use Bing Search

- Bing Search UI for demo

  `\bing-search-webui`: (Utility, to see the search results from Bing Search API)

    <img src="bing-search-webui\public\img\screenshot.png" alt="bingwebui" width="200"/>

## **Section 4** : Langchain & Its Competitors

- LangChain is a framework for developing applications powered by language models. (1) Be data-aware: connect a language model to other sources of data.
(2) Be agentic: Allow a language model to interact with its environment.

  - It highlights two main value props of the framework:

  1. Components: modular abstractions and implementations for working with language models, with easy-to-use features.
  2. Use-Case Specific Chains: chains of components that assemble in different ways to achieve specific use cases, with customizable interfaces.

  @cite: [doc][langchain-doc]

  <img src="files/langchain-glance.png" width="400">

  @cite: [packt][langchain-glance]

### **Langchain and Prompt engineering library**

- [Microsoft Semantic Kernel](https://github.com/microsoft/semantic-kernel)
- [LangChain](https://python.langchain.com/en/latest/index.html)
- [LlamaIndex](https://github.com/jerryjliu/llama_index)
- [Microsoft guidance](https://github.com/microsoft/guidance)

### **Langchain Feature Matrix & Cheetsheet**

- [Feature Matrix][langchain-features]: LangChain Features
  - [Feature Matrix: Snapshot in 2023 July][langchain-features-202307]
- [Cheetsheet][langchain-cookbook]: LangChain CheatSheet
- [LangChain AI Handbook][langchain-handbook]: published by Pinecone
- [Awesome Langchain][awesome-langchain]: Curated list of tools and projects using LangChain.

### **Langchain Impressive Features**

- [Langchain/cache](https://python.langchain.com/docs/modules/model_io/models/llms/how_to/llm_caching): Reducing the number of API calls
- [Langchain/context-aware-splitting](https://python.langchain.com/docs/use_cases/question_answering/document-context-aware-QA): Splits a file into chunks while keeping metadata
- [LangChain Expression Language](https://python.langchain.com/docs/guides/expression_language/): A declarative way to easily compose chains together

  ```python
  chain = prompt | model | StrOutputParser() | search
  ```

### **Langchain Quick Start: How to Use and Useful Utilities**

- `deeplearning.ai\langchain-chat-with-your-data`: DeepLearning.ai LangChain: Chat with Your Data
- `deeplearning.ai\langchain-llm-app-dev`: LangChain for LLM Application Development
- `langchain-@practical-ai\Langchain_1_(믹스의_인공지능).ipynb` : Langchain Get started
- `langchain-@practical-ai\Langchain_2_(믹스의_인공지능).ipynb` : Langchain Utilities

  ```python
  from langchain.chains.summarize import load_summarize_chain
  chain = load_summarize_chain(chat, chain_type="map_reduce", verbose=True)
  chain.run(docs[:3])
  ```

  @citation: [@practical-ai](https://www.youtube.com/@practical-ai)

### **Langchain chain type: Summarizer**

- stuff: Sends everything at once in LLM. If it's too long, an error will occur.
- map_reduce: Summarizes by dividing and then summarizing the entire summary.
- refine: (Summary + Next document) => Summary
- map_rerank: Ranks by score and summarizes to important points.

### **Langchain Agent**

1. If you're using a text LLM, first try `zero-shot-react-description`.
1. If you're using a Chat Model, try `chat-zero-shot-react-description`.
1. If you're using a Chat Model and want to use memory, try `conversational-react-description`.

1. `self-ask-with-search`: [self ask with search paper](https://ofir.io/self-ask.pdf)

1. `react-docstore`: [ReAct paper](https://arxiv.org/pdf/2210.03629.pdf)

### **LangSmith & Langchain low code**

- [langflow](https://github.com/logspace-ai/langflow): LangFlow is a UI for LangChain, designed with react-flow.
- [LangSmith](https://blog.langchain.dev/announcing-langsmith/) Platform for debugging, testing, evaluating

  <img src="files/langchain_debugging.png" width="200" />

- [Flowise](https://github.com/FlowiseAI/Flowise) Drag & drop UI to build your customized LLM flow

### **Langchain & Its Competitors**
---

### **Langchain vs LlamaIndex**

- Basically LlamaIndex is a smart storage mechanism, while Langchain is a tool to bring multiple tools together. [@citation](https://community.openai.com/t/llamaindex-vs-langchain-which-one-should-be-used/163139)

- LangChain offers many features and focuses on using chains and agents to connect with external APIs. In contrast, LlamaIndex is more specialized and excels at indexing data and retrieving documents.

### **Langchain vs Semantic Kernel**

| Langchain |  Semantic Kernel                                         |
| --------- | -------------------------------------------------------- |
| Memory    |  Memory                                                  |
| Tookit    |  Skill                                                   |
| Tool      |  LLM prompts (semantic functions) or native C# or Python code (native function) |
| Agent     |  Planner                                                 |
| Chain     |  Steps, Pipeline                                         |
| Tool      |  Connector                                               |

### **Semantic Kernel : Semantic Function**

expressed in natural language in a text file "*skprompt.txt*" using SK's
[Prompt Template language](https://github.com/microsoft/semantic-kernel/blob/main/docs/PROMPT_TEMPLATE_LANGUAGE.md).
Each semantic function is defined by a unique prompt template file, developed using modern

### **Semantic Kernel : Prompt Template language Key takeaways**

1. Variables : use the {{$variableName}} syntax : Hello {{$name}}, welcome to Semantic Kernel!

2. Function calls: use the {{namespace.functionName}} syntax : The weather today is {{weather.getForecast}}.

3. Function parameters: {{namespace.functionName $varName}} and {{namespace.functionName "value"}} syntax : The weather today in {{$city}} is {{weather.getForecast $city}}.

4. Prompts needing double curly braces :
{{ "{{" }} and {{ "}}" }} are special SK sequences.

5. Values that include quotes, and escaping :

    For instance:

    ... {{ 'no need to \\"escape" ' }} ...
    is equivalent to:

    ... {{ 'no need to "escape" ' }} ...

### **Semantic Kernel Glossary**

- [Glossary in Git](https://github.com/microsoft/semantic-kernel/blob/main/docs/GLOSSARY.md)

- [Glossary in MS Doc](https://learn.microsoft.com/en-us/semantic-kernel/whatissk#sk-is-a-kit-of-parts-that-interlock)

    <img src="files/kernel-flow.png" alt="sk" width="500"/>

    | Term   | Short Description                                                                                                                                                                                                                                                                                     |
    | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | ASK       | A user's goal is sent to SK as an ASK                                                                                                                                                                                                                                                                 |
    | Kernel    | [The kernel](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/kernel) orchestrates a user's ASK                                                                                                                                                                                          |
    | Planner   | [The planner](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/planner) breaks it down into steps based upon resources that are available                                                                                                                                                |
    | Resources | Planning involves leveraging available [skills,](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/skills) [memories,](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/memories) and [connectors](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/connectors) |
    | Steps     | A plan is a series of steps for the kernel to execute                                                                                                                                                                                                                                                 |
    | Pipeline  | Executing the steps results in fulfilling the user's ASK                                                                                                                                                                                                                                              |
    | GET       | And the user gets what they asked for ...

### **Langchain vs Semantic Kernel vs Azure Machine Learning Prompt flow**

- What's the difference between LangChain and Semantic Kernel?

  LangChain has many agents, tools, plugins etc. out of the box. More over, LangChain has 10x more popularity, so has about 10x more developer activity to improve it. On other hand, **Semantic Kernel architecture and quality is better**, that's quite promising for Semantic Kernel. [Link](https://github.com/microsoft/semantic-kernel/discussions/1326)

- What's the difference between Azure Machine Laering PromptFlow and Semantic Kernel?

  1. Low/No Code vs C#, Python, Java
  1. Focused on Prompt orchestrating vs Integrate LLM into their existing app.

### **Prompt Template Language**

|                   | Handlebars.js                                                                 | Jinja2                                                                                 | Prompt Template                                                                                     |
| ----------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Conditions        | {{#if user}}<br>  Hello {{user}}!<br>{{else}}<br>  Hello Stranger!<br>{{/if}} | {% if user %}<br>  Hello {{ user }}!<br>{% else %}<br>  Hello Stranger!<br>{% endif %} | Branching features such as "if", "for", and code blocks are not part of SK's template language.     |
| Loop              | {{#each items}}<br>  Hello {{this}}<br>{{/each}}                              | {% for item in items %}<br>  Hello {{ item }}<br>{% endfor %}                          | By using a simple language, the kernel can also avoid complex parsing and external dependencies.    |
| Langchain Library | guidance                                                                      | Azure Machine Learning<br>Prompt flow                                                  | Semactic Kernel                                                                                     |
| URL               | [Link](https-//handlebarsjs.com/guide/)                                       | [Link](https-//jinja.palletsprojects.com/en/2.10.x/templates/)                         | [Link](https-//learn.microsoft.com/en-us/semantic-kernel/prompt-engineering/prompt-template-syntax) |

## **Section 5**: Prompt Engineering & Finetuning

### **Prompt Engineering**

---

1. Zero-shot
    - [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
1. Few-shot Learning
    - [Open AI: Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
1. Chain of Thought (CoT): ReAct and Self Consistency also inherit the CoT concept.
1. Recursively Criticizes and Improves (RCI)
1. ReAct: Grounding with external sources. (Reasoning and Act)
1. Chain-of-Thought Prompting  
    - [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2205.11916)
1. Tree of Thought [git](https://github.com/ysymyth/tree-of-thought-llm)

    - `tree-of-thought\forest_of_thought.py`: Forest of thought Decorator sample
    - `tree-of-thought\tree_of_thought.py`: Tree of thought Decorator sample
    - `tree-of-thought\react-prompt.py`: ReAct sample without Langchain

1. Zero-shot, one-shot and few-shot

    <img src="files/zero-one-few-shot.png" width="200">

- Prompt Concept
  
  1. Question-Answering
  1. Roll-play: `Act as a [ROLE] perform [TASK] in [FORMAT]`
  1. Reasoning
  1. Prompt-Chain
  1. Program Aided Language Model
  1. Recursive Summarization: Long Text -> Chunks -> Summarize pieces -> Concatenate -> Summarize

- 🤩[Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) : ⭐⭐⭐⭐⭐

- [Prompt Engineering Guide](https://www.promptingguide.ai/): Copyright © 2023 DAIR.AI

- [Promptist][Promptist]: Microsoft's researchers trained an additional language model (LM) that optimizes text prompts for text-to-image generation.
  - For example, instead of simply passing "Cats dancing in a space club" as a prompt, an engineered prompt might be "Cats dancing in a space club, digital painting, artstation, concept art, soft light, hdri, smooth, sharp focus, illustration, fantasy."

### **Azure OpenAI Prompt Guide**

- [Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/advanced-prompt-engineering)

### **OpenAI Prompt Guide**

- [Prompt example](https://platform.openai.com/examples)

- [Best practices for prompt engineering](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)

### **DeepLearning.ai Prompt Engineering COURSE and others**

- [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)

- [Short courses](https://www.deeplearning.ai/short-courses/)

### **Awesome ChatGPT Prompts**

- [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)

### **ChatGPT : “user”, “assistant”, and “system” messages.**

 To be specific, the ChatGPT API allows for differentiation between “user”, “assistant”, and “system” messages.

 1. always obey "system" messages.
 1. all end user input in the “user” messages.
 1. "assistant" messages as previous chat responses from the assistant.

 Presumably, the model is trained to treat the user messages as human messages, system messages as some system level configuration, and assistant messages as previous chat responses from the assistant. (@<https://blog.langchain.dev/using-chatgpt-api-to-evaluate-chatgpt/>)

### **Finetuning**

---

PEFT: Parameter-Efficient Fine-Tuning ([Youtube](https://youtu.be/Us5ZFp16PaU))

- [PEFT](https://huggingface.co/blog/peft): Parameter-Efficient Fine-Tuning. PEFT is an approach to fine tuning only a few parameters.

- [LoRA: Low-Rank Adaptation of Large Language Models](https://github.com/microsoft/LoRA): LoRA is one of PEFT technique. To represent the weight updates with two smaller matrices (called update matrices) through low-rank decomposition.

  <img src="files/LoRA.png" alt="LoRA" width="400"/>

- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/pdf/2305.14314): 4-bit quantized pre-trained language model into Low Rank Adapters (LoRA).

    [artidoro/qlora](https://github.com/artidoro/qlora)

- [Training language models to follow instructions with human feedback](https://arxiv.org/pdf/2203.02155)

- [Fine-tuning a GPT — LoRA](https://dataman-ai.medium.com/fine-tune-a-gpt-lora-e9b72ad4ad3): Comprehensive guide for LoRA ⭐⭐⭐⭐
. Printed version for backup. [Link](files/Fine-tuning_a_GPT_LoRA.pdf)

### **Llama2 Finetuning**

- A key difference between Llama 1 and Llama 2 is the architectural change of attention layer, in which Llama 2 takes advantage of Grouped Query Attention (GQA) mechanism to improve efficiency.

- The sources of Inference code and finetuning code are commented on the files. [git](https://github.com/facebookresearch/llama)
  - llama2-trial.ipynb: LLama 2 inference code in local
  - llama2-finetune.ipynb: LLama 2 Finetuning with Reinforce learning
  - Llama_2_Fine_Tuning_using_QLora.ipynb: [link](https://youtu.be/eeM6V5aPjhk)

- Llama 2 ONNX [git](https://github.com/microsoft/Llama-2-Onnx)
  - ONNX: ONNX stands for Open Neural Network Exchange. It is an open standard format for machine learning interoperability. ONNX enables AI developers to use models with a variety of frameworks, tools, runtimes, and compilers.

  - ONNX Runtime can be used on mobile devices. ONNX Runtime gives you a variety of options to add machine learning to your mobile application. ONNX Runtime mobile is a reduced size, high performance package for edge devices, including smartphones and other small storage devices.

- LLM-Engine: The open source engine for fine-tuning LLM [git](https://github.com/scaleapi/llm-engine)
  - finetune_llama_2_on_science_qa.ipynb: [git](https://github.com/scaleapi/llm-engine)

### **RLHF (Reinforcement Learning from Human Feedback) & SFT (Supervised Fine-Tuning)**

- Machine learning technique that trains a "reward model" directly from human feedback and uses the model as a reward function to optimize an agent's policy using reinforcement learning

  <img src="files/rhlf.png" width="400" />

- Libraries: [TRL](https://huggingface.co/docs/trl/index), [trlX](https://github.com/CarperAI/trlx), [Argilla](https://docs.argilla.io/en/latest/tutorials/libraries/colab.html)

  <img src="files/chip.jpg" width="400" />

  The three steps in the process: 1. pre-training on large web-scale data, 2. supervised fine-tuning on instruction data (instruction tuning), and 3. RLHF. [doc](https://aman.ai/primers/ai/RLHF/)

- `Reinforcement Learning from Human Feedback (RLHF)` is a process of pretraining and retraining a language model using human feedback to develop a scoring algorithm that can be reapplied at scale for future training and refinement. As the algorithm is refined to match the human-provided grading, direct human feedback is no longer needed, and the language model continues learning and improving using algorithmic grading alone. [doc](https://huggingface.co/blog/rlhf)

- `Supervised Fine-Tuning (SFT)` fine-tuning a pre-trained model on a specific task or domain using labeled data. This can cause more significant shifts in the model’s behavior compared to RLHF.

- `Proximal Policy Optimization (PPO)` is a policy gradient method for reinforcement learning that aims to have the data efficiency and reliable performance of TRPO (Trust Region Policy Optimization), while using only first-order optimization. It does this by modifying the objective function to penalize changes to the policy that move the probability ratio away from 1. This results in an algorithm that is easier to implement and tune than TRPO while still achieving good performance. TRPO requires second-order optimization, which can be more difficult to implement and computationally expensive.

- `First-order optimization` methods are a class of optimization algorithms that use only the first derivative (gradient) of the objective function to find its minimum or maximum. These methods include gradient descent, stochastic gradient descent, and their variants.

- Second-order methods: `Second derivative (Hessian)` of the objective function

## **Quantization**

- Quantization-aware training (QAT): The model is further trained with quantization in mind after being initially trained in floating-point precision.
- Post-training quantization (PTQ): The model is quantized after it has been trained without further optimization during the quantization process.

| Method | Pros | Cons |
| --- | --- | --- |
| Post-training quantization | Easy to use, no need to retrain the model | May result in accuracy loss |
| Quantization-aware training | Can achieve higher accuracy than post-training quantization | Requires retraining the model, can be more complex to implement |
| Per-embedding-group quantization | Can achieve high accuracy with low bit-widths, leading to significant memory savings | May require more fine-tuning and experimentation to achieve optimal results |

### **Sparsification**

- @citation: Bing chat

  `
  Sparsification is a technique used to reduce the size of large language models (LLMs) by removing redundant parameters without significantly affecting their performance. It is one of the methods used to compress LLMs. LLMs are neural networks that are trained on massive amounts of data and can generate human-like text. The term “sparsification” refers to the process of removing redundant parameters from these models.
  `

### **Small size with Textbooks: High quality synthetic dataset**

- [ph-1](https://analyticsindiamag.com/microsoft-releases-1-3-bn-parameter-language-model-outperforms-llama/): Despite being small in size, phi-1 attained 50.6% on HumanEval and 55.5% on MBPP.
- [Orca](https://www.microsoft.com/en-us/research/publication/orca-progressive-learning-from-complex-explanation-traces-of-gpt-4/): Orca learns from rich signals from GPT 4 including explanation traces; step-by-step thought processes; and other complex instructions, guided by teacher assistance from ChatGPT.

### **Large Transformer Model Inference Optimization**

- [Large Transformer Model Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/) : ⭐⭐⭐⭐⭐

### **Visual Prompting**

---

- [https://landing.ai/what-is-visual-prompting/](https://landing.ai/what-is-visual-prompting/): Similarly to what has happened in NLP, large pre-trained vision transformers have made it possible for us to implement Visual Prompting. Printed version for backup [Link](.files/vPrompt.pdf)
- [Visual Prompting](https://arxiv.org/pdf/2211.11635.pdf)
- [Andrew Ng’s Visual Prompting Livestream](https://www.youtube.com/watch?v=FE88OOUBonQ)

## **Section 6** : LLM Enhancement

### **Context constraints**

- [Introducing 100K Context Windows](https://www.anthropic.com/index/100k-context-windows): hundreds of pages, Around 75,000 words; [demo](https://youtu.be/2kFhloXz5_E) Anthropic Claude

- [Rotary Positional Embedding (RoPE)](https://blog.eleuther.ai/rotary-embeddings/) / Printed version for backup [Link](./files/RoPE.pdf)

  > How is this different from the sinusoidal embeddings used in "Attention is All You Need"?
  >
  > 1. Sinusoidal embeddings apply to each coordinate individually, while rotary embeddings mix pairs of coordinates
  > 1. Sinusoidal embeddings add a `cos` or `sin` term, while rotary embeddings use a multiplicative factor.

- [Lost in the Middle: How Language Models Use Long Contexts](https://arxiv.org/abs/2307.03172)
  1. Best Performace when relevant information is at beginning
  1. Too many retrieved documents will harm performance
  1. Performacnce decreases with an increase in context

- [Structured Prompting: Scaling In-Context Learning to 1,000 Examples](https://arxiv.org/abs/2212.06713)
  1. Microsoft's Structured Prompting allows thousands of examples, by first concatenating examples into groups, then inputting each group into the LM. The hidden key and value vectors of the LM's attention modules are cached. Finally, when the user's unaltered input prompt is passed to the LM, the cached attention vectors are injected into the hidden layers of the LM. 

  1. This approach wouldn't work with OpenAI's closed models. because this needs to access [keys] and [values] in the transformer internals, which they do not expose. You could implement yourself on OSS ones. 
  
      @cite [doc](https://www.infoq.com/news/2023/02/microsoft-lmops-tools/)

### **OpenAI's plans**
---

### **OpenAI's plans according to Sam Altman**

- [Archived Link](https://web.archive.org/web/20230531203946/https://humanloop.com/blog/openai-plans) : Printed version for backup [Link](files/openai-plans.pdf)

### **OpenAI Plugin and function calling**

- [ChatGPT Plugin](https://openai.com/blog/chatgpt-plugins)
- [ChatGPT Function calling](https://platform.openai.com/docs/guides/gpt/function-calling)

  > Under the hood, functions are injected into the system message in a syntax the model has been trained on.
  This means functions count against the model's context limit and are billed as input tokens.
  If running into context limits, we suggest limiting the number of functions or the length of documentation you provide for function parameters.

  > Azure OpenAI start to support function calling. [Link][aoai_func]

### **OSS Alternatives for OpenAI Code Interpreter**

- [OpenAI Code Interpreter](https://openai.com/blog/chatgpt-plugins) Integration with Sandboxed python execution environment

  > We provide our models with a working Python interpreter in a sandboxed, firewalled execution environment, along with some ephemeral disk space.

- [OSS Code Interpreter](https://github.com/shroominic/codeinterpreter-api) A LangChain implementation of the ChatGPT Code Interpreter.

- [SlashGPT](https://github.com/shroominic/codeinterpreter-api) The tool integrated with "jupyter" agent

### **Data Extraction methods for the context**
---

### **Math problem-solving skill**

- Plugin: [Wolfram alpha](https://www.wolfram.com/wolfram-plugin-chatgpt/)
- [Improving mathematical reasoning with process supervision](https://openai.com/research/improving-mathematical-reasoning-with-process-supervision)
- Math formula OCR: [MathPix](https://mathpix.com/), OSS [LaTeX-OCR](https://github.com/lukas-blecher/LaTeX-OCR)

### **Table Extraction**

- Azure Form Recognizer: [documentation](https://learn.microsoft.com/en-us/azure/applied-ai-services/form-recognizer)
- Table to Markdown format: [Table to Markdown](https://tabletomarkdown.com/)

### **Token counting & Token-limits**

- [Open AI Tokenizer](https://platform.openai.com/tokenizer): GPT-3, Codex Token counting
- [tiktoken](https://github.com/openai/tiktoken): BPE tokeniser for use with OpenAI's models. Token counting.
- [What are tokens and how to count them?](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)
- [5 Approaches To Solve LLM Token Limits](https://dholmes.co.uk/blog/5-approaches-to-solve-llm-token-limits/) : Printed version for backup [Link](files/token-limits-5-approaches.pdf)

---

### **Avoid AI hallucination**

- [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails): Building Trustworthy, Safe and Secure LLM Conversational Systems

### **Gorilla: An API store for LLMs**

- [Gorilla: An API store for LLMs](https://github.com/ShishirPatil/gorilla): Gorilla: Large Language Model Connected with Massive APIs
  1. Used GPT-4 to generate a dataset of instruction-api pairs for fine-tuning Gorilla.
  1. Used the abstract syntax tree (AST) of the generated code to match with APIs in the database and test set for evaluation purposes.
  
  1. @citation [Link](https://www.infoq.com/news/2023/07/microsoft-gorilla/)
  
  > Another user asked how Gorilla compared to LangChain; Patil replied: Langchain is a terrific project that tries to teach agents how to use tools using prompting. Our take on this is that prompting is not scalable if you want to pick between 1000s of APIs. So Gorilla is a LLM that can pick and write the semantically and syntactically correct API for you to call! A drop in replacement into Langchain!

- [Meta: Toolformer](https://github.com/lucidrains/toolformer-pytorch): Language Models That Can Use Tools, by MetaAI

### **Memory Optimization**

- [PagedAttention](https://vllm.ai/) : vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention, 24x Faster LLM Inference [Link](files/vLLM_pagedattention.pdf)

- [Flash Attention](https://arxiv.org/abs/2205.14135): An method that reorders the attention computation and leverages classical techniques (tiling, recomputation). Instead of storing each intermediate result, use kernel fusion and run every operation in a single kernel in order to avoid memory read/write overhead.

## **Section 7** : List of OSS LLM & Generative AI Landscape

### **Evolutionary Graph of LLaMA Family / LLM evolutionary tree**

  Evolutionary Graph of LLaMA Family

  <img src="files/llama-0628-final.png" width="450" />

  LLM evolutionary tree

  <img src="files/qr_version.jpg" alt="llm" width="450"/>

- [LLMSurvey](https://github.com/RUCAIBox/LLMSurvey)

- [A Survey of Large Language Models](https://arxiv.org/abs/2303.18223)

- [LLM evolutionary tree](https://github.com/Mooler0410/LLMsPracticalGuide): @citation: LLMsPracticalGuide

### **Generative AI Revolution: Exploring the Current Landscape**

- [The Generative AI Revolution: Exploring the Current Landscape](https://pub.towardsai.net/the-generative-ai-revolution-exploring-the-current-landscape-4b89998fcc5f) : Printed version for backup [Link](files/gen-ai-landscape.pdf) ⭐⭐⭐⭐

### **List of OSS LLM**

- [List of OSS LLM](https://medium.com/geekculture/list-of-open-sourced-fine-tuned-large-language-models-llm-8d95a2e0dc76)
- Printed version for "Medium" limits. [Link](files/list_of_oss_llm.pdf)
- [LLM Collection][llm-collection]: promptingguide.ai

### **Huggingface Open LLM Learboard**

- [Huggingface Open LLM Learboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

- Upstage's 70B Language Model Outperforms GPT-3.5: [doc][upstage]

### **Huggingface Transformer**

- [huggingface/transformers: 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX. (github.com)](https://github.com/huggingface/transformers)

### **Huggingface StarCoder**

- [StarCoder: A State-of-the-Art LLM for Code](https://huggingface.co/blog/starcoder)

- [bigcode/starcoder](https://huggingface.co/bigcode/starcoder)

### **Democratizing the magic of ChatGPT with open models**

- The LLMs mentioned here are just small parts of the current advancements in the field. Most OSS LLM models have been built on the [facebookresearch/llama](https://github.com/facebookresearch/llama). For a comprehensive list and the latest updates, please refer to the "Generative AI Landscape / List of OSS LLM" section.

- [facebookresearch/llama](https://github.com/facebookresearch/llama): Not licensed for commercial use
- [Llama 2](https://huggingface.co/blog/llama2): Available for commercial use [Link][llama2] / [demo](https://huggingface.co/blog/llama2#demo)
- [Falcon LLM](https://falconllm.tii.ae/) Apache 2.0 license
- OSS LLM
  - [StableVicuna](https://stability.ai/blog/stablevicuna-open-source-rlhf-chatbot) First Open Source RLHF LLM Chatbot
  - [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html): Fine-tuned from the LLaMA 7B model
  - [gpt4all](https://github.com/nomic-ai/gpt4all): Run locally on your CPU
  - [vicuna](https://vicuna.lmsys.org/): 90% ChatGPT Quality
  - [Koala](https://bair.berkeley.edu/blog/2023/04/03/koala/): Focus on dialogue data gathered from the web.
  - [dolly](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html): Databricks
  - [Cerebras-GPT](https://www.cerebras.net/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models/): 7 GPT models ranging from 111m to 13b parameters.
  - [GPT4All Download URL](https://huggingface.co/Sosaka/GPT4All-7B-4bit-ggml/tree/main)
  - [KoAlpaca](https://github.com/Beomi/KoAlpaca): Alpaca for korean

## **Section 8** : References

### **picoGPT**

- An unnecessarily tiny implementation of GPT-2 in NumPy. [picoGPT](https://github.com/jaymody/picoGPT): Transformer Decoder

### **AutoGPT / Communicative Agents**

- [Auto-GPT](https://github.com/Torantulino/Auto-GPT): Most popular
- [babyagi](https://github.com/yoheinakajima/babyagi): Most simplest implementation - Coworking of 4 agents
- [microsoft/JARVIS](https://github.com/microsoft/JARVIS)
- [SuperAGI](https://github.com/TransformerOptimus/superagi): GUI for agent settings
- [lightaime/camel](https://github.com/lightaime/camel): 🐫 CAMEL: Communicative Agents for “Mind” Exploration of Large Scale Language Model Society (github.com)
- 1:1 Conversation between two ai agents
Camel Agents - a Hugging Face Space by camel-ai
[Hugging Face (camel-agents)](https://huggingface.co/spaces/camel-ai/camel-agents)

### **Large Language and Vision Assistant**

- [LLaVa](https://llava-vl.github.io/): Large Language-and-Vision Assistant
- [MiniGPT-4](https://minigpt-4.github.io/): Enhancing Vision-language Understanding with Advanced Large Language Models
- [TaskMatrix, aka VisualChatGPT](https://github.com/microsoft/TaskMatrix): Microsoft TaskMatrix; GroundingDINO + [SAM](https://github.com/facebookresearch/segment-anything.git)
- [BLIP-2](https://huggingface.co/blog/blip-2): Salesforce Research, Querying Transformer (Q-Former)

  > `Q-Former (Querying Transformer)`: A transformer model that consists of two submodules that share the same self-attention layers: an image transformer that interacts with a frozen image encoder for visual feature extraction, and a text transformer that can function as both a text encoder and a text decoder

### **MLLM (multimodal large language model)**

- Facebook: ImageBind / SAM
  1. [facebookresearch/ImageBind](https://github.com/facebookresearch/ImageBind): ImageBind One Embedding Space to Bind Them All (github.com)
  1. [facebookresearch/segment-anything(SAM)](https://github.com/facebookresearch/segment-anything): The repository provides code for running inference with the SegmentAnything Model (SAM), links for downloading the trained model checkpoints, and example notebooks that show how to use the model. (github.com)

- Microsoft: Kosmos-1 / Kosmos-2
  1. Language Is Not All You Need: Aligning Perception with Language Models [2302.14045](https://arxiv.org/abs/2302.14045)
  1. [Kosmos-2](https://arxiv.org/abs/2306.14824): Grounding Multimodal Large Language Models to the World

- TaskMatrix.AI
  1. [TaskMatrix.AI](https://arxiv.org/abs/2303.16434): Completing Tasks by Connecting Foundation Models with Millions of APIs

### **Application UI/UX**

- [Gradio](https://github.com/gradio-app/gradio): Build Machine Learning Web Apps - in Python
- [Text generation web UI](https://github.com/oobabooga/text-generation-webui): Text generation web UI
- Very Simple Langchain example using Open AI: [langchain-ask-pdf](https://github.com/alejandro-ao/langchain-ask-pdf)
- An open source implementation of OpenAI's ChatGPT Code interpreter: [gpt-code-ui](https://github.com/ricklamers/gpt-code-ui)
- Open AI Chat Mockup: An open source ChatGPT UI. [mckaywrigley/chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)
- Streaming with Azure OpenAI [SSE](https://github.com/thivy/azure-openai-js-stream)
- [BIG-AGI](https://github.com/enricoros/big-agi) FKA nextjs-chatgpt-app
- Embedding does not use Open AI. Can be executed locally: [pdfGPT](https://github.com/bhaskatripathi/pdfGPT)
- Tiktoken Alternative in C#: [microsoft/Tokenizer](https://github.com/microsoft/Tokenizer): .NET and Typescript implementation of BPE tokenizer for OpenAI LLMs. (github.com)
- [Azure OpenAI Proxy](https://github.com/scalaone/azure-openai-proxy): OpenAI API requests converting into Azure OpenAI API requests

### **Awesome demo**

- [FRVR Official Teaser](https://youtu.be/Yjjpr-eAkqw): Prompt to Game: AI-powered end-to-end game creation
- [rewind.ai](https://www.rewind.ai/): Rewind captures everything you’ve seen on your Mac and iPhone

### **日本語（Japanese Materials）**

- [rinna](https://huggingface.co/rinna): rinnaの36億パラメータの日本語GPT言語モデル: 3.6 billion parameter Japanese GPT language model
- [rinna: bilingual-gpt-neox-4b](https://huggingface.co/rinna/bilingual-gpt-neox-4b): 日英バイリンガル大規模言語モデル
- [法律:生成AIの利用ガイドライン](https://storialaw.jp/blog/9414): Legal: Guidelines for the Use of Generative AI
- [New Era of Computing - ChatGPT がもたらした新時代](https://speakerdeck.com/dahatake/new-era-of-computing-chatgpt-gamotarasitaxin-shi-dai-3836814a-133a-4879-91e4-1c036b194718)
- [大規模言語モデルで変わるMLシステム開発](https://speakerdeck.com/hirosatogamo/da-gui-mo-yan-yu-moderudebian-warumlsisutemukai-fa): ML system development that changes with large-scale language models
- [GPT-4登場以降に出てきたChatGPT/LLMに関する論文や技術の振り返り](https://blog.brainpad.co.jp/entry/2023/06/05/153034): Review of ChatGPT/LLM papers and technologies that have emerged since the advent of GPT-4
- [LLMを制御するには何をするべきか？](https://blog.brainpad.co.jp/entry/2023/06/08/161643): How to control LLM
- [生成AIのマルチモーダルモデルでできること -タスク紹介編-](https://blog.brainpad.co.jp/entry/2023/06/06/160003): What can be done with multimodal models of generative AI
- [Azure OpenAIを活用したアプリケーション実装のリファレンス](https://github.com/Azure-Samples/jp-azureopenai-samples): 日本マイクロソフト リファレンスアーキテクチャ

## **Section 9** : Relevant solutions and resources

- [Microsoft Fabric](README_Fabric.md): Fabric integrates technologies like Azure Data Factory, Azure Synapse Analytics, and Power BI into a single unified product

- [Microsoft Office Copilot: Natural Language Commanding via Program Synthesis](https://arxiv.org/abs/2306.03460): Semantic Interpreter, a natural language-friendly AI system for productivity software such as Microsoft Office that leverages large language models (LLMs) to execute user intent across application features.

- [Comparing Adobe Firefly, Dalle-2, OpenJourney, Stable Diffusion, and Midjourney](https://blog.usmanity.com/comparing-adobe-firefly-dalle-2-and-openjourney/): Generative AI for images

- [Weights & Biases](https://github.com/wandb/examples): Visualizing and tracking your machine learning experiments [wandb.ai](https://wandb.ai/) sample: `deeplearning.ai\wandb`

- [activeloopai/deeplake](https://github.com/activeloopai/deeplake): AI Vector Database for LLMs/LangChain. Doubles as a Data Lake for Deep Learning. Store, query, version, & visualize any data. Stream data in real-time to PyTorch/TensorFlow. <https://activeloop.ai> (github.com)

- [mosaicml/llm-foundry](https://github.com/mosaicml/llm-foundry): LLM training code for MosaicML foundation models (github.com)

- [Must read: the 100 most cited AI papers in 2022](https://www.zeta-alpha.com/post/must-read-the-100-most-cited-ai-papers-in-2022)

- [The Best Machine Learning Resources](https://medium.com/machine-learning-for-humans/how-to-learn-machine-learning-24d53bb64aa1)

- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) Examples and guides for using the OpenAI API

- [gpt4free](https://github.com/xtekky/gpt4free) for educational purposes only

- Generate 3D objects conditioned on text or images [openai/shap-e](https://github.com/openai/shap-e)

- Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold [(paper)](https://arxiv.org/pdf/2305.10973) [online demo](https://github.com/Zeqiang-Lai/DragGAN)

- string2string:
The library is an open-source tool that offers a comprehensive suite of efficient algorithms for a broad range of string-to-string problems. [string2string](https://github.com/stanfordnlp/string2string)

  <img src="files/string2string-overview.png" alt="string2string" width="200"/>

## **Section 10** : AI Tools

  @citation: [The best AI Chatbots in 2023.](https://twitter.com/slow_developer/status/1671530676045094915): twitter.com/slow_developer `+`

  ```comment
  The leader: <http://openai.com>
  The runner-up: <http://bard.google.com>
  Open source: <http://huggingface.co/chat>
  Searching web: <http://perplexity.ai>
  Content writing: <http://jasper.ai/chat>
  Sales and Marketing: <http://chatspot.ai>
  AI Messenger: <http://personal.ai>
  Tinkering: <http://poe.com>
  Fun: <http://beta.character.ai>
  Coding Auto-complete: <http://github.com/features/copilot>
  ```

- Oceans of AI - All AI Tools <https://play.google.com/store/apps/details?id=in.blueplanetapps.oceansofai&hl=en_US>
- Newsletters & Tool Databas: <https://www.therundown.ai/>
- Edge and Chrome Extension & Plugin
  - [BetterChatGPT](https://github.com/ztjhz/BetterChatGPT)
  - [ChatHub](https://github.com/chathub-dev/chathub) All-in-one chatbot client [Webpage](https://chathub.gg/)
  - [ChatGPT Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin)

## **Section 11** : Datasets for LLM Training

- [LLMDataHub: Awesome Datasets for LLM Training](https://github.com/Zjh-819/LLMDataHub): A quick guide (especially) for trending instruction finetuning datasets
- [大規模言語モデルのデータセットまとめ](https://note.com/npaka/n/n686d987adfb1): 大規模言語モデルのデータセットまとめ

## **Acknowledgements**

[aoai_func]: https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/function-calling#using-function-in-the-chat-completions-api
[typechat]: https://microsoft.github.io/TypeChat/blog/introducing-typechat
[typechat-git]: https://github.com/microsoft/Typechat
[semantic-kernel]: https://devblogs.microsoft.com/semantic-kernel/
[semantic-kernel-git]: https://github.com/microsoft/semantic-kernel
[guidance]: https://github.com/microsoft/guidance
[deepspeed]: https://github.com/microsoft/DeepSpeed
[promptflow]: https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/overview-what-is-prompt-flow
[promptflow-doc]: https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/harness-the-power-of-large-language-models-with-azure-machine/ba-p/3828459#:~:text=Prompt%20flow%20is%20a%20powerful%20feature%20that%20simplifies,and%20deploy%20high-quality%20flows%20with%20ease%20and%20efficiency.
[prompt-engine]: https://github.com/microsoft/prompt-engine
[prompt-engine-py]: https://github.com/microsoft/prompt-engine-py
[m365-copilot]: https://blogs.microsoft.com/blog/2023/03/16/introducing-microsoft-365-copilot-your-copilot-for-work/
[d365-copilot]: https://blogs.microsoft.com/blog/2023/03/06/introducing-microsoft-dynamics-365-copilot/
[viva-copilot]: https://www.microsoft.com/en-us/microsoft-365/blog/2023/04/20/introducing-copilot-in-microsoft-viva-a-new-way-to-boost-employee-engagement-and-performance/
[sec-copilot]: https://blogs.microsoft.com/blog/2023/03/28/introducing-microsoft-security-copilot-empowering-defenders-at-the-speed-of-ai/
[langchain-doc]: https://docs.langchain.com/docs/
[llama-index-doc]: https://gpt-index.readthedocs.io/en/latest/index.html
[langchain-handbook]: https://www.pinecone.io/learn/series/langchain/
[langchain-features-202307]: files/langchain-features-202307.png
[langchain-cookbook]: https://github.com/gkamradt/langchain-tutorials
<!-- [langchain-cheetsheet-old]: https://github.com/Tor101/LangChain-CheatSheet -->
[langchain-features]: https://python.langchain.com/docs/get_started/introduction
[awesome-langchain]: https://github.com/kyrolabs/awesome-langchain
[llama2]: https://ai.meta.com/llama
[LMOps]: https://github.com/microsoft/LMOps
[langchain-glance]: https://www.packtpub.com/article-hub/using-langchain-for-large-language-model-powered-applications
[Promptist]: https://arxiv.org/abs/2212.09611
[Structured Prompting]: https://arxiv.org/abs/2212.06713
[upstage]: https://en.upstage.ai/newsroom/upstage-huggingface-llm-no1
[llm-collection]: https://www.promptingguide.ai/models/collection
