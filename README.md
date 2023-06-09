
`updated: 06/09/2023`

# LLM (Large language model) and Azure related libraries

This repository contains references to open-source models similar to ChatGPT, as well as Langchain and prompt engineering libraries. It also includes related samples and research on Langchain, Vector Search (including feasibility checks on Elasticsearch, Azure Cognitive Search, Azure Cosmos DB), and more.

> `Rule: Brief each item on one or a few lines as much as possible.`

## Table of contents

- **Section 1** : Llama-index and Vector Storage (Search)
  * [Opensearch/Elasticsearch setup](#opensearch-elasticsearch-setup)
  * [llama-index](#llama-index)
  * [Vector Storage Comparison](#vector-storage-comparison)
  * [Vector Storage Options for Azure](#vector-storage-options-for-azure)
  * [Milvus Embedded](#milvus-embedded)
  * [Conclusion](#conclusion)
  * [llama-index Deep Dive](#llama-index-deep-dive)
- **Section 2** : ChatGPT + Enterprise data with Azure OpenAI and Cognitive Search
  * [addtional_steps (optional)](#additonal_steps-optional)
  * [Configuration steps](#configuration-steps)
  * [Azure Cognitive Search : Vector Search](#azure-cognitive-search--vector-search)
- **Section 3** : Microsoft Semantic Kernel with Azure Cosmos DB
  * [Semantic-Kernel](#semantic-kernel)
  * [Environment variables](#environment-variable)
  * [Bing search Web UI and Semantic Kernel sample code](#bing-search-web-ui-and-semantic-kernel-sample-code)
- **Section 4** : Langchain sample code
  * [Langchain sample code](#section-4--langchain-code)
- **Section 5**: Prompt Engineering, Finetuning, and Langchain
  - [Prompt Engineering](#prompt-engineering)
  - [OpenAI Prompt Guide](#openai-prompt-guide)
  - [DeepLearning.ai Prompt Engineering Course and others](#deeplearningai-prompt-engineering-course-and-others)
  - [Awesome ChatGPT Prompts](#awesome-chatgpt-prompts)
  - [ChatGPT : “user”, “assistant”, and “system” messages.](#chatgpt--user-assistant-and-system-messages)
  - [Finetuning](#finetuning) : PEFT - LoRA - QLoRA
  - [Quantization](README_SBCs.md) : Quantization & Run ChatGPT on a Raspberry Pi / Android
  - [Sparsification](#sparsification)
  - [Langchain vs Semantic Kernel](#langchain-vs-semantic-kernel)
    + [Semantic Kernel : Semantic Function](#semantic-kernel--semantic-function)
    + [Semantic Kernel : Prompt Template language key takeaways](#semantic-kernel--prompt-template-language-key-takeaways)
    + [Langchain Agent](#langchain-agent)
    + [Sementic Kernel Glossary](#sementic-kernel-glossary)
- **Section 6:** Improvement
  - [Math problem-solving skill](#math-problem-solving-skill)
  - [OpenAI's plans according to Sam Altman](#openais-plans-according-to-sam-altman) Humanloop interview has been removed from the site. Instead of that, Web-archived link.
  - [Token-limits](#token-limits)
- **Section 7:** List of OSS LLM
  - [List of OSS LLM](#list-of-oss-llm)
  - [Huggingface Open LLM Learboard](#huggingface-open-llm-learboard)
- **Section 8** : References
  * [Langchain and Prompt engineering library](#langchain-and-prompt-engineering-library)
  * [AutoGPT](#autogpt)
  * [picoGPT](#picogpt) : tiny implementation of GPT-2
  * [Communicative Agents](#communicative-agents)
  * [Democratizing the magic of ChatGPT with open models](#democratizing-the-magic-of-chatgpt-with-open-models)
  * [Large Language and Vision Assistant](#large-language-and-vision-assistant)
  * [Hugging face Transformer](#hugging-face-transformer)
  * [Hugging face StarCoder](#hugging-face-starcoder)
  * [MLLM (multimodal large language model)](#mllm-multimodal-large-language-model)
  * [Tiktoken Alternative in C#](#tiktoken-alternative-in-c-)
  * [UI/UX](#uiux)
  * [PDF with ChatGPT](#pdf-with-chatgpt)
  * [Edge and Chrome Extension / Plugin](#edge-and-chrome-extension--plugin)
  * [日本語（Japanese Materials)](#日本語japanese-materials)
- **Section 9** : [Relavant solutions](#section-9--relavant-solutions)
  * [Microsoft Fabric](README_Fabric.md): Single unified data analytics solution 
  * [DeepSpeed](#section-9--relavant-solutions): Distributed training and memory optimization.

- **Acknowledgements**
  * [Acknowledgements](#acknowledgements)

# **Section 1** : Llama-index and Vector Storage (Search)

This repository has been created for testing and feasibility checks using vector and language chains, specifically llama-index. These libraries are commonly used when implementing Prompt Engineering and consuming one's own data into LLM.  

## Opensearch/Elasticsearch setup

- docker : Opensearch Docker-compose
- docker-elasticsearch : Not working for ES v8, requiring security plug-in with mandatory
- docker-elk : Elasticsearch Docker-compose, Optimized Docker configurations with solving security plug-in issues.
- es-open-search-set-analyzer.py : Put Language analyzer into Open search
- es-open-search.py : Open search sample index creation 
- es-search-set-analyzer.py : Put Language analyzer into Elastic search
- es-search.py : Usage of Elastic search python client
- files : The Sample file for consuming

## llama-index

- index.json : Vector data local backup created by llama-index
- index_vector_in_opensearch.json : Vector data stored in Open search (Source: `files\all_h1.pdf`)
- llama-index-azure-elk-create.py: llama-index ElasticsearchVectorClient (Unofficial file to manipulate vector search, Created by me, Not Fully Tested)
- llama-index-lang-chain.py : Lang chain memory and agent usage with llama-index
- llama-index-opensearch-create.py : Vector index creation to Open search
- llama-index-opensearch-query-chatgpt.py : Test module to access Azure Open AI Embedding API.
- llama-index-opensearch-query.py : Vector index query with questions to Open search
- llama-index-opensearch-read.py : llama-index ElasticsearchVectorClient (Unofficial file to manipulate vector search, Created by me, Not Fully Tested)
- env.template : The properties. Change its name to `.env` once your values settings is done.

```properties
OPENAI_API_TYPE=azure
OPENAI_API_BASE=https://????.openai.azure.com/
OPENAI_API_VERSION=2022-12-01
OPENAI_API_KEY=<your value in azure>
OPENAI_DEPLOYMENT_NAME_A=<your value in azure>
OPENAI_DEPLOYMENT_NAME_B=<your value in azure>
OPENAI_DEPLOYMENT_NAME_C=<your value in azure>
OPENAI_DOCUMENT_MODEL_NAME=<your value in azure>
OPENAI_QUERY_MODEL_NAME=<your value in azure>

INDEX_NAME=gpt-index-demo
INDEX_TEXT_FIELD=content
INDEX_EMBEDDING_FIELD=embedding
ELASTIC_SEARCH_ID=elastic
ELASTIC_SEARCH_PASSWORD=elastic
OPEN_SEARCH_ID=admin
OPEN_SEARCH_PASSWORD=admin
```

## Vector Storage Comparison

- [Not All Vector Databases Are Made Equal](https://towardsdatascience.com/milvus-pinecone-vespa-weaviate-vald-gsi-what-unites-these-buzz-words-and-what-makes-each-9c65a3bd0696)
- Printed version for "Medium" limits. - [Link](files/vector-dbs.pdf)

## Vector Storage Options for Azure

- [Vector Search in Azure Cosmos DB for MongoDB vCore](https://devblogs.microsoft.com/cosmosdb/introducing-vector-search-in-azure-cosmos-db-for-mongodb-vcore/)
- [Vector search (private preview) - Azure Cognitive Search](https://github.com/Azure/cognitive-search-vector-pr)

## Milvus Embedded

- `pip install milvus`
- Docker compose: https://milvus.io/docs/install_offline-docker.md
- Milvus Embedded through python console only works in Linux and Mac OS.
- In Windows, Use this link, https://github.com/matrixji/milvus/releases.

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

## Conclusion

- Azure Open AI Embedding API,text-embedding-ada-002, supports 1536 dimensions. Elastic search, Lucene based engine, supports 1024 dimensions as a max. Open search can insert 16,000 dimensions as a vector storage. 

- ~~Lang chain interface of Azure Open AI does not support ChatGPT yet. so that reason, need to use alternatives such as `text-davinci-003`.~~

> @open ai documents: 
text-embedding-ada-002: 
Smaller embedding size. The new embeddings have only 1536 dimensions, one-eighth the size of davinci-001 embeddings, 
making the new embeddings more cost effective in working with vector databases. 
https://openai.com/blog/new-and-improved-embedding-model

> @open search documents: 
However, one exception to this is that the maximum dimension count for the Lucene engine is 1,024, compared with
16,000 for the other engines. https://opensearch.org/docs/latest/search-plugins/knn/approximate-knn/

> @llama-index examples: 
However, the examples in llama-index uses 1536 vector size.

## llama-index Deep dive

- [CallbackManager (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-003-callback-manager/)

- [Customize TokenTextSplitter (Japanese)](https://dev.classmethod.jp/articles/llamaindex-tutorial-002-text-splitter/)

# **Section 2** : ChatGPT + Enterprise data with Azure OpenAI and Cognitive Search

The files in this directory, `extra_steps`, have been created for managing extra configurations and steps for launching the demo repository.

https://github.com/Azure-Samples/azure-search-openai-demo

![Screenshot](./files/capture_azure_demo.png "Main")

## additonal_steps (optional)

- fix_from_origin : The modified files, setup related
- ms_internal_az_init.ps1 : Powershell script for Azure module installation 
- ms_internal_troubleshootingt.ps1 : Set Specific Subscription Id as default

## Configuration steps

1. (optional) Check Azure module installation in Powershell by running `ms_internal_az_init.ps1` script
2. (optional) Set your Azure subscription Id to default

> Start the following commands in `./azure-search-openai-demo` directory

3. (deploy azure resources) Simply Run `azd up`

The azd stores relevant values in the .env file which is stored at `${project_folder}\.azure\az-search-openai-tg\.env`.

```properties
AZURE_ENV_NAME=<your_value_in_azure>
AZURE_LOCATION=<your_value_in_azure>
AZURE_OPENAI_SERVICE=<your_value_in_azure>
AZURE_PRINCIPAL_ID=<your_value_in_azure>
AZURE_SEARCH_INDEX=<your_value_in_azure>
AZURE_SEARCH_SERVICE=<your_value_in_azure>
AZURE_STORAGE_ACCOUNT=<your_value_in_azure>
AZURE_STORAGE_CONTAINER=<your_value_in_azure>
AZURE_SUBSCRIPTION_ID=<your_value_in_azure>
BACKEND_URI=<your_value_in_azure>
```

4. Move to `app` by `cd app` command
5. (sample data loading) Move to `scripts` then Change into Powershell by `Powershell` command, Run `prepdocs.ps1`

- console output (excerpt)

```commandline
        Uploading blob for page 20 -> role_library-20.pdf
        Uploading blob for page 21 -> role_library-21.pdf
        Uploading blob for page 22 -> role_library-22.pdf
        Uploading blob for page 23 -> role_library-23.pdf
        Uploading blob for page 24 -> role_library-24.pdf
        Uploading blob for page 25 -> role_library-25.pdf
        Uploading blob for page 26 -> role_library-26.pdf
        Uploading blob for page 27 -> role_library-27.pdf
        Uploading blob for page 28 -> role_library-28.pdf
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
127.0.0.1 - - [13/Apr/2023 14:25:31] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [13/Apr/2023 14:25:31] "GET /assets/index-184dcdbd.css HTTP/1.1" 200 -
127.0.0.1 - - [13/Apr/2023 14:25:31] "GET /assets/index-41d57639.js HTTP/1.1" 200 -
127.0.0.1 - - [13/Apr/2023 14:25:31] "GET /assets/github-fab00c2d.svg HTTP/1.1" 200 -
127.0.0.1 - - [13/Apr/2023 14:25:32] "GET /favicon.ico HTTP/1.1" 304 -
127.0.0.1 - - [13/Apr/2023 14:25:42] "POST /chat HTTP/1.1" 200 -
```

Running from second times

1. Move to `app` by `cd ..` and `cd app` command
2. (locally running) Run `start.cmd`

Another Reference Architectue

[azure-open-ai-embeddings-qna](https://github.com/Azure-Samples/azure-open-ai-embeddings-qna)

<img src="files/demo-architecture.png" alt="embeddin_azure_csharp" width="500"/>

[C# Implementation](https://github.com/Azure-Samples/azure-search-openai-demo-csharp)
ChatGPT + Enterprise data with Azure OpenAI and Cognitive Search

<img src="files/demo-architecture-csharp.png" alt="embeddin_azure_csharp" width="250"/>

[Azure Cosmos DB + OpenAI ChatGPT](https://github.com/Azure-Samples/cosmosdb-chatgpt)
C# blazor and Azure Custom Template

<img src="files/cosmos-gpt.png" alt="gpt-cosmos" width="400"/>

Azure Open AI work with Cognitive Search act as a Long-term memory

- [ChatGPT + Enterprise data with Azure OpenAI and Cognitive Search](https://github.com/Azure-Samples/azure-search-openai-demo)
- [Can ChatGPT work with your enterprise data?](https://www.youtube.com/watch?v=tW2EA4aZ_YQ)
- [Azure OpenAI と Azure Cognitive Search の組み合わせを考える](https://qiita.com/nohanaga/items/59e07f5e00a4ced1e840)

## Azure Cognitive Search : Vector Search
- [Azure Cognitive Search : Vector Search](https://github.com/Azure/cognitive-search-vector-pr)

Options: 1. Vector similarity search, 2. Pure Vector Search, 3. Hybrid Search, 4. Semantic Hybrid Search

```python
# Semantic Hybrid Search
query = "what is azure sarch?"

search_client = SearchClient(
    service_endpoint, index_name, AzureKeyCredential(key))

results = search_client.search(
    search_text=query, #text
    vector=Vector(value=generate_embeddings(
        query), k=3, fields="contentVector"), #vector
    select=["title", "content", "category"],
    query_type="semantic", query_language="en-us", semantic_configuration_name='my-semantic-config', query_caption="extractive", query_answer="extractive", #semantic
    top=3
)

semantic_answers = results.get_answers()
```

# **Section 3** : Microsoft Semantic Kernel with Azure Cosmos DB

Microsoft Langchain Library supports C# and Python and offers several features, some of which are still in development and may be unclear on how to implement. However, it is simple, stable, and faster than Python-based open-source software. The features listed on the link include: [Semantic Kernel Feature Matrix](https://github.com/microsoft/semantic-kernel/blob/main/FEATURE_MATRIX.md)

<img src="files/sk-flow.png" alt="sk" width="500"/>

This section includes how to utilize Azure Cosmos DB for vector storage and vector search by leveraging the Semantic-Kernel.

## Semantic-Kernel

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
- SkillDALLEImgGen.cs : DALLE Skill (Only OpenAI, Azure Open AI not supports yet)

## Environment variable

```json
{
  "Type": "azure",
  "Model": "<model_deployment_name>",
  "EndPoint": "https://<your-endpoint-value>.openai.azure.com/",
  "AOAIApiKey": "<your-key>",
  "OAIApiKey": "",
  "OrdId": "-", //The value needs only when using Open AI.
  "BingSearchAPIKey": "<your-key>",
  "aoaiDomainName": "<your-endpoint-value>",
  "CosmosConnectionString": "<cosmos-connection-string>"
}
```

- Semantic Kernel has recently introduced support for Azure Cognitive Search as a memory. However, it currently only supports Azure Cognitive Search with a Semantic Search interface, lacking any features to store vectors to ACS.

- According to the comments, this suggests that the strategy of the plan could be divided into two parts. One part focuses on Semantic Search, while the other involves generating embeddings using OpenAI.

`Azure Cognitive Search automatically indexes your data semantically, so you don't need to worry about embedding generation.`
`samples/dotnet/kernel-syntax-examples/Example14_SemanticMemory.cs`.

```csharp
// TODO: use vectors
// @Microsoft Semactic Kernel
var options = new SearchOptions
{
        QueryType = SearchQueryType.Semantic,
        SemanticConfigurationName = "default",
        QueryLanguage = "en-us",
        Size = limit,
};
```

- SemanticKernel Implementation sample to overcome Token limits of Open AI model.
Semantic Kernel でトークンの限界を超えるような長い文章を分割してスキルに渡して結果を結合したい (zenn.dev)
[Semantic Kernel でトークンの限界を超える](https://zenn.dev/microsoft/articles/semantic-kernel-10)

## **Bing search Web UI and Semantic Kernel sample code**

Semantic Kernel sample code to integrate with Bing Search (ReAct??)

`\ms-semactic-bing-notebook`
- gs_chatgpt.ipynb: Azure Open AI ChatGPT sample to use Bing Search
- gs_davinci.ipynb: Azure Open AI Davinci sample to use Bing Search

Bing Search UI for demo

`\bing-search-webui`: (utility)

<img src="bing-search-webui\public\img\screenshot.png" alt="bingwebui" width="300"/>

# **Section 4** : Langchain code 

cite: [@practical-ai](https://www.youtube.com/@practical-ai)

## **Langchain Quick Start: How to Use and Useful Utilities**

- Langchain_1_(믹스의_인공지능).ipynb : Langchain Get started
- langchain_1_(믹스의_인공지능).py : -
- Langchain_2_(믹스의_인공지능).ipynb : Langchain Utilities
- langchain_2_(믹스의_인공지능).py : -

```python
from langchain.chains.summarize import load_summarize_chain
chain = load_summarize_chain(chat, chain_type="map_reduce", verbose=True)
chain.run(docs[:3])
```

## **Langchain chain_type**

- stuff: Sends everything at once in LLM. If it's too long, an error will occur.
- map_reduce: Summarizes by dividing and then summarizing the entire summary.
- refine: (Summary + Next document) => Summary
- map_rerank: Ranks by score and summarizes to important points.

# **Section 5**: Prompt Engineering, and Langchain vs Semantic Kernel #

## **Prompt Engineering** ##

1. Zero-shot 
    - [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
1. Few-shot Learning
    - [Open AI: Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
1. Chain of Thought (CoT): ReAct and Self Consistency also inherit the CoT concept.
1. Recursively Criticizes and Improves (RCI)
1. ReAct: Grounding with external sources. (Reasoning and Act)
1. Chain-of-Thought Prompting  
    - [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2205.11916)
1. Tree of Thought [(github)](https://github.com/ysymyth/tree-of-thought-llm)

- Prompt Concept
1. Question-Answering
1. Roll-play: `Act as a [ROLE] perform [TASK] in [FORMAT]`
1. Reasoning
1. Prompt-Chain
1. Program Aided Language Model
1. Recursive Summarization: Long Text -> Chunks -> Summarize pieces -> Concatenate -> Summarize

- 🤩[Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/) : ⭐⭐⭐⭐⭐

- [Prompt Engineering Guide](https://www.promptingguide.ai/)

### **OpenAI Prompt Guide**

- [Prompt example](https://platform.openai.com/examples)

- [Best practices for prompt engineering](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)

### **DeepLearning.ai Prompt Engineering COURSE and others** ##

- [ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)

- [Short courses](https://www.deeplearning.ai/short-courses/)

### **Awesome ChatGPT Prompts** 

- [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)

### **ChatGPT : “user”, “assistant”, and “system” messages.**

 To be specific, the ChatGPT API allows for differentiation between “user”, “assistant”, and “system” messages.

 1. always obey "system" messages.
 1. all end user input in the “user” messages.
 1. "assistant" messages as previous chat responses from the assistant.

 Presumably, the model is trained to treat the user messages as human messages, system messages as some system level configuration, and assistant messages as previous chat responses from the assistant. (@https://blog.langchain.dev/using-chatgpt-api-to-evaluate-chatgpt/)

### **Finetuning**

PEFT: Parameter-Efficient Fine-Tuning ([Youtube](https://youtu.be/Us5ZFp16PaU))

- [PEFT](https://huggingface.co/blog/peft)

- [LoRA: Low-Rank Adaptation of Large Language Models](https://github.com/microsoft/LoRA)

<img src="files/LoRA.png" alt="LoRA" width="450"/>

- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/pdf/2305.14314)

    [artidoro/qlora](https://github.com/artidoro/qlora)

- [Training language models to follow instructions with human feedback](https://arxiv.org/pdf/2203.02155)

### **Sparsification**

@Binghchat
```
Sparsification is a technique used to reduce the size of large language models (LLMs) by removing redundant parameters without significantly affecting their performance. It is one of the methods used to compress LLMs. LLMs are neural networks that are trained on massive amounts of data and can generate human-like text. The term “sparsification” refers to the process of removing redundant parameters from these models.
```

- 😮 [Large Transformer Model Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/) : ⭐⭐⭐⭐⭐

## **Langchain vs Semantic Kernel** ##

| Langchain |  Semantic Kernel             |
| --------- | ---------------------------- |
| Memory    |  Memory                      |
| Tookit    |  Skill                       |
| Tool      |  Function (Native, Semantic) |
| Agent     |  Planner                     |
| Chain     |  Steps, Pipeline             |
| Tool      |  Connector                   |

### **Semantic Kernel : Semantic Function** ### 

expressed in natural language in a text file "*skprompt.txt*" using SK's
[Prompt Template language](https://github.com/microsoft/semantic-kernel/blob/main/docs/PROMPT_TEMPLATE_LANGUAGE.md).
Each semantic function is defined by a unique prompt template file, developed using modern

### **Semantic Kernel : Prompt Template language Key takeaways** ###

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

### **Langchain Agent** ###

1. If you're using a text LLM, first try `zero-shot-react-description`.
1. If you're using a Chat Model, try `chat-zero-shot-react-description`.
1. If you're using a Chat Model and want to use memory, try `conversational-react-description`.

1. `self-ask-with-search`: [ self ask with search paper](https://ofir.io/self-ask.pdf)

1. `react-docstore`: [ReAct paper](https://arxiv.org/pdf/2210.03629.pdf)

### **Sementic Kernel Glossary** ###

[Glossary in Git](https://github.com/microsoft/semantic-kernel/blob/main/docs/GLOSSARY.md)

[Glossary in MS Doc](https://learn.microsoft.com/en-us/semantic-kernel/whatissk#sk-is-a-kit-of-parts-that-interlock)

| Journey   | Short Description                                                                                                                                                                                                                                                                                     |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ASK       | A user's goal is sent to SK as an ASK                                                                                                                                                                                                                                                                 |
| Kernel    | [The kernel](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/kernel) orchestrates a user's ASK                                                                                                                                                                                          |
| Planner   | [The planner](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/planner) breaks it down into steps based upon resources that are available                                                                                                                                                |
| Resources | Planning involves leveraging available [skills,](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/skills) [memories,](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/memories) and [connectors](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/connectors) |
| Steps     | A plan is a series of steps for the kernel to execute                                                                                                                                                                                                                                                 |
| Pipeline  | Executing the steps results in fulfilling the user's ASK                                                                                                                                                                                                                                              |
| GET       | And the user gets what they asked for ...      

# **Section 6** : Improvement #

## Math problem-solving skill
- Plugin: [Wolfram alpha](https://www.wolfram.com/wolfram-plugin-chatgpt/)
- [Improving mathematical reasoning with process supervision](https://openai.com/research/improving-mathematical-reasoning-with-process-supervision)

## OpenAI's plans according to Sam Altman
- [Archived Link](https://web.archive.org/web/20230531203946/https://humanloop.com/blog/openai-plans) : Printed version for backup - [Link](files/openai-plans.pdf)

## Token-limits
- [Open AI Tokenizer](https://platform.openai.com/tokenizer)
- [What are tokens and how to count them?](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)
- [5 Approaches To Solve LLM Token Limits](https://dholmes.co.uk/blog/5-approaches-to-solve-llm-token-limits/) : Printed version for backup - [Link](files/token-limits-5-approaches.pdf)

# **Section 7** : List of OSS LLM #

## List of OSS LLM
- [List of OSS LLM](https://medium.com/geekculture/list-of-open-sourced-fine-tuned-large-language-models-llm-8d95a2e0dc76)
- Printed version for "Medium" limits. - [Link](files/list_of_oss_llm.pdf)

## Huggingface Open LLM Learboard
- [Huggingface Open LLM Learboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)

# **Section 8** : References #

## Langchain and Prompt engineering library
- [Microsoft Semantic Kernel](https://github.com/microsoft/semantic-kernel)
- [LangChain](https://python.langchain.com/en/latest/index.html)
- [llama-index](https://github.com/jerryjliu/llama_index)
- [@practical-ai: 믹스의 인공지능](https://www.youtube.com/@practical-ai)

## AutoGPT
- [Auto-GPT](https://github.com/Torantulino/Auto-GPT)
- [babyagi](https://github.com/yoheinakajima/babyagi): Most simplest implementation
- [microsoft/JARVIS](https://github.com/microsoft/JARVIS)

## picoGPT

- An unnecessarily tiny implementation of GPT-2 in NumPy. [picoGPT](https://github.com/jaymody/picoGPT)

## Communicative Agents 
- [lightaime/camel](https://github.com/lightaime/camel): 🐫 CAMEL: Communicative Agents for “Mind” Exploration of Large Scale Language Model Society (github.com)
- 1:1 Conversation between two ai agents
Camel Agents - a Hugging Face Space by camel-ai
[Hugging Face (camel-agents)](https://huggingface.co/spaces/camel-ai/camel-agents)

## Democratizing the magic of ChatGPT with open models

- [facebookresearch/llama](https://github.com/facebookresearch/llama)
- [Falcon LLM](https://falconllm.tii.ae/) Apache 2.0 license
- [StableVicuna](https://stability.ai/blog/stablevicuna-open-source-rlhf-chatbot) Open Source RLHF LLM Chatbot
- [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html)
- [gpt4all](https://github.com/nomic-ai/gpt4all)
- [vicuna](https://vicuna.lmsys.org/)
- [dolly](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html)
- [Cerebras-GPT](https://www.cerebras.net/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models/)
- [GPT4All Download URL](https://huggingface.co/Sosaka/GPT4All-7B-4bit-ggml/tree/main)
- [KoAlpaca](https://github.com/Beomi/KoAlpaca)

## Large Language and Vision Assistant

- [LLaVa](https://llava-vl.github.io/)
- [MiniGPT-4](https://minigpt-4.github.io/)
- [VisualChatGPT](https://github.com/microsoft/TaskMatrix): Microsoft

## Hugging face Transformer
- [huggingface/transformers: 🤗 Transformers: State-of-the-art Machine Learning for Pytorch, TensorFlow, and JAX. (github.com)](https://github.com/huggingface/transformers)

## Hugging face StarCoder

- [StarCoder: A State-of-the-Art LLM for Code](https://huggingface.co/blog/starcoder)

- [bigcode/starcoder](https://huggingface.co/bigcode/starcoder)

## MLLM (multimodal large language model)
- Facebook: ImageBind / SAM (Just Info)
1. [facebookresearch/ImageBind](https://github.com/facebookresearch/ImageBind): ImageBind One Embedding Space to Bind Them All (github.com)
2. [facebookresearch/segment-anything(SAM)](https://github.com/facebookresearch/segment-anything): The repository provides code for running inference with the SegmentAnything Model (SAM), links for downloading the trained model checkpoints, and example notebooks that show how to use the model. (github.com)

- Microsoft: Kosmos-1
1. [2302.14045] Language Is Not All You Need: Aligning Perception with Language Models (arxiv.org)
2. [Language Is Not All You Need](https://arxiv.org/abs/2302.14045)

## Tiktoken Alternative in C#
microsoft/Tokenizer: .NET and Typescript implementation of BPE tokenizer for OpenAI LLMs. (github.com)
[microsoft/Tokenizer](https://github.com/microsoft/Tokenizer)

## UI/UX

- [Gradio](https://github.com/gradio-app/gradio)
- [Text generation web UI](https://github.com/oobabooga/text-generation-webui)
- Very Simple Langchain example using Open AI: [langchain-ask-pdf](https://github.com/alejandro-ao/langchain-ask-pdf)
- An open source implementation of OpenAI's ChatGPT Code interpreter: [gpt-code-ui](https://github.com/ricklamers/gpt-code-ui)
- Open AI Chat Mockup: An open source ChatGPT UI. [mckaywrigley/chatbot-ui](https://github.com/mckaywrigley/chatbot-ui)
- Streaming with Azure OpenAI [SSE](https://github.com/thivy/azure-openai-js-stream)
- [BIG-AGI](https://github.com/enricoros/big-agi) FKA nextjs-chatgpt-app

## PDF with ChatGPT ##

- Embedding does not use Open AI. Can be executed locally. [pdfGPT](https://github.com/bhaskatripathi/pdfGPT)

## Edge and Chrome Extension / Plugin

- [BetterChatGPT](https://github.com/ztjhz/BetterChatGPT)

- [ChatHub](https://github.com/chathub-dev/chathub) All-in-one chatbot client [Webpage](https://chathub.gg/)

- [ChatGPT Retrieval Plugin](https://github.com/openai/chatgpt-retrieval-plugin)

## 日本語（Japanese Materials）

- [法律:生成AIの利用ガイドライン](https://storialaw.jp/blog/9414)
- [New Era of Computing - ChatGPT がもたらした新時代](https://speakerdeck.com/dahatake/new-era-of-computing-chatgpt-gamotarasitaxin-shi-dai-3836814a-133a-4879-91e4-1c036b194718)
- [大規模言語モデルで変わるMLシステム開発](https://speakerdeck.com/hirosatogamo/da-gui-mo-yan-yu-moderudebian-warumlsisutemukai-fa)
- [GPT-4登場以降に出てきたChatGPT/LLMに関する論文や技術の振り返り](https://blog.brainpad.co.jp/entry/2023/06/05/153034)
- [LLMを制御するには何をするべきか？](https://blog.brainpad.co.jp/entry/2023/06/08/161643)
- [生成AIのマルチモーダルモデルでできること -タスク紹介編-](https://blog.brainpad.co.jp/entry/2023/06/06/160003)

# **Section 9** : Relavant solutions #

- [Microsoft Fabric](README_Fabric.md): Fabric integrates technologies like Azure Data Factory, Azure Synapse Analytics, and Power BI into a single unified product

- [DeepSpeed](https://github.com/microsoft/DeepSpeed): DeepSpeed is a deep learning optimization library that makes distributed training and inference easy, efficient, and effective.

- [Azure Machine Learning - Prompt flow](https://techcommunity.microsoft.com/t5/ai-machine-learning-blog/harness-the-power-of-large-language-models-with-azure-machine/ba-p/3828459#:~:text=Prompt%20flow%20is%20a%20powerful%20feature%20that%20simplifies,and%20deploy%20high-quality%20flows%20with%20ease%20and%20efficiency.): Visual Designer for Prompt crafting. Use [Jinja](https://github.com/pallets/jinja) as a prompt template language.

- [Prompt Engine](https://github.com/microsoft/prompt-engine): Craft prompts for Large Language Models

- [activeloopai/deeplake](https://github.com/activeloopai/deeplake): AI Vector Database for LLMs/LangChain. Doubles as a Data Lake for Deep Learning. Store, query, version, & visualize any data. Stream data in real-time to PyTorch/TensorFlow. https://activeloop.ai (github.com) 

- [mosaicml/llm-foundry](https://github.com/mosaicml/llm-foundry): LLM training code for MosaicML foundation models (github.com) 

- [Must read: the 100 most cited AI papers in 2022](https://www.zeta-alpha.com/post/must-read-the-100-most-cited-ai-papers-in-2022)

- [The Best Machine Learning Resources](https://medium.com/machine-learning-for-humans/how-to-learn-machine-learning-24d53bb64aa1)

- [OpenAI Cookbook](https://github.com/openai/openai-cookbook) Examples and guides for using the OpenAI API

- [gpt4free](https://github.com/xtekky/gpt4free) for educational purposes only

- Generate 3D objects conditioned on text or images [openai/shap-e](https://github.com/openai/shap-e)

- Drag Your GAN: Interactive Point-based Manipulation on the Generative Image Manifold [(paper)](https://arxiv.org/pdf/2305.10973) [online demo](https://github.com/Zeqiang-Lai/DragGAN)

- string2string: 
The library is an open-source tool that offers a comprehensive suite of efficient algorithms for a broad range of string-to-string problems. [string2string](https://github.com/stanfordnlp/string2string)

  <img src="files/string2string-overview.png" alt="string2string" width="500"/>

- [LLM evolutionary tree](https://github.com/Mooler0410/LLMsPracticalGuide): @LLMsPracticalGuide

  <img src="files/qr_version.jpg" alt="llm" width="500"/> 

# Acknowledgements

- [@TODO](https://github.com/??) for [TODO](https://github.com/??/??)

