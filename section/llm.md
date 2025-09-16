## **Large Language Model: Landscape**

#### Large Language Models (in 2023)

1. Change in perspective is necessary because some abilities only emerge at a certain scale. Some conclusions from the past are invalidated and we need to constantly unlearn intuitions built on top of such ideas.
1. From first-principles, scaling up the Transformer amounts to efficiently doing matrix multiplications with many, many machines.
1. Further scaling (think 10000x GPT-4 scale). It entails finding the inductive bias that is the bottleneck in further scaling.
> [🗣️](https://twitter.com/hwchung27/status/1710003293223821658) / [📺](https://t.co/vumzAtUvBl) / [✍️](https://t.co/IidLe4JfrC) [6 Oct 2023]

#### Large Language Model Comparison

- [LLMArena](https://lmarena.ai/):💡Chatbot Arena (formerly LMSYS): Free AI Chat to Compare & Test Best AI Chatbots
- [LLMprices.dev](https://llmprices.dev): Compare prices for models like GPT-4, Claude Sonnet 3.5, Llama 3.1 405b and many more.
- [AI Model Review](https://aimodelreview.com/): Compare 75 AI Models on 200+ Prompts Side By Side.
- [Artificial Analysis](https://artificialanalysis.ai/):💡Independent analysis of AI models and API providers.
- [Inside language models (from GPT to Olympus)](https://lifearchitect.ai/models/)
- [LLM Pre-training and Post-training Paradigms](https://sebastianraschka.com/blog/2024/new-llm-pre-training-and-post-training.html) [17 Aug 2024] <br/>
  <img src="../files/llm-dev-pipeline-overview.png" width="350" />

#### The Big LLM Architecture Comparison (in 2025)

- [The Big LLM Architecture Comparison](https://sebastianraschka.com/blog/2025/the-big-llm-architecture-comparison.html) [19 Jul 2025]

  | Model              | Release         | Params | Attention          | Norm                | MoE                         | Notable Features                                                                     |
  | ------------------ | --------------- | ------ | ------------------ | ------------------- | --------------------------- | ------------------------------------------------------------------------------------ |
  | **DeepSeek V3/R1** | Dec ’24/Jan ’25 | 671 B  | MLA                | RMSNorm             | Yes (256 experts, 9 active) | Shared‑expert MoE |
  | **OLMo 2**         | Jan ’25         | –      | MHA                | RMSNorm (+ QK‑Norm) | No                          | Post‑Norm placement for training      |
  | **Gemma 3**        | 2025            | –      | Sliding‑window GQA | RMSNorm             | No                          | Additional norm layers for stability                               |
  | **Gemma 3n**       | 2025            | –      | Sliding‑window GQA | RMSNorm             | No                          | Per‑layer embeddings & MatFormer slicing                           |
  | **Mistral S 3.1**  | 2025            | –      | GQA                | RMSNorm             | No                          | Layer‑trimmed, compact FFN & KV cache                                                |
  | **SmolLM 3**       | 2025            | –      | GQA/MHA            | RMSNorm             | No                          | Drops positional embeddings in select layers                                         |
  | **Kimi K2**        | 2025            | 1 T    | MLA + GQA          | RMSNorm             | Yes                         | Trillion‑parameter scale 

#### GPT-2 vs gpt-oss

- [From GPT-2 to gpt-oss: Analyzing the Architectural Advances✍️](https://magazine.sebastianraschka.com/p/from-gpt-2-to-gpt-oss-analyzing-the) [9 Aug 2025]

| Feature              | GPT-2                          | GPT-OSS                              |
| -------------------- | ------------------------------ | ------------------------------------ |
| Release & Size       | 2019, up to 1.5B params        | 2025, 20B & 120B params (MoE)        |
| Architecture         | Dense transformer decoder      | Mixture-of-Experts (MoE) decoder     |
| Activation & Dropout | Swish activation, uses dropout | GELU (or optimized), no dropout      |
| Parameter Efficiency | All params active per token    | Sparse activation of experts         |
| Deployment & License | MIT license    | Open-weight local runs, Apache 2.0   |
| Reasoning & Tools    | Basic generation               | Built-in chain-of-thought & tool use |

### **Evolutionary Tree of Large Language Models**

- Evolutionary Graph of LLaMA Family

  <img src="../files/llama-0628-final.png" width="450" />

- LLM evolutionary tree

  <!-- <img src="../files/qr_version.jpg" alt="llm" width="450"/> -->
  <img src="../files/tree.png" alt="llm" width="450"/>

- Timeline of SLMs

  <img src="../files/slm-timeline.png" width="650" />

- [A Survey of Large Language Models📑](https://alphaxiv.org/abs/2303.18223): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.18223)] /[🐙](https://github.com/RUCAIBox/LLMSurvey) [31 Mar 2023] contd.
 ![**github stars**](https://img.shields.io/github/stars/RUCAIBox/LLMSurvey?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

- [LLM evolutionary tree📑](https://alphaxiv.org/abs/2304.13712): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2304.13712)]: A curated list of practical guide resources of LLMs (LLMs Tree, Examples, Papers) [🐙](https://github.com/Mooler0410/LLMsPracticalGuide) [26 Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/Mooler0410/LLMsPracticalGuide?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

- [A Comprehensive Survey of Small Language Models in the Era of Large Language Models📑](https://alphaxiv.org/abs/2411.03350) / [🐙](https://github.com/FairyFali/SLMs-Survey) [4 Nov 2024] ![**github stars**](https://img.shields.io/github/stars/FairyFali/SLMs-Survey?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **A Taxonomy of Natural Language Processing**

- An overview of different fields of study and recent developments in NLP. [🗄️](../files/taxonomy-nlp.pdf) / [✍️](https://towardsdatascience.com/a-taxonomy-of-natural-language-processing-dfc790cb4c01) [24 Sep 2023]

  Exploring the Landscape of Natural Language Processing Research [ref📑](https://alphaxiv.org/abs/2307.10652) [20 Jul 2023]

  <img src="../files/taxonomy-nlp.png" width="650" />

  NLP taxonomy

  <img src="../files/taxonomy-nlp2.png" width="650" />

  Distribution of the number of papers by most popular fields of study from 2002 to 2022

### **Large Language Model Collection**

- [The Open Source AI Definition](https://opensource.org/ai/open-source-ai-definition) [28 Oct 2024]
- [The LLM Index](https://sapling.ai/llm/index): A list of large language models (LLMs)
- [Chatbot Arena🤗](https://huggingface.co/spaces/lmsys/chatbot-arena-leaderboard): Benchmarking LLMs in the Wild with Elo Ratings
- [LLM Collection](https://www.promptingguide.ai/models/collection): promptingguide.ai
- [Huggingface Open LLM Learboard🤗](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
- [ollam](https://ollama.com/library?sort=popular): ollama-supported models
- [The mother of all spreadsheets for anyone into LLMs](https://x.com/DataChaz/status/1868708625310699710) [17 Dec 2024]
- [KoAlpaca🐙](https://github.com/Beomi/KoAlpaca): Alpaca for korean [Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/Beomi/KoAlpaca?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Pythia📑](https://alphaxiv.org/abs/2304.01373): How do large language models (LLMs) develop and evolve over the course of training and change as models scale? A suite of decoder-only autoregressive language models ranging from 70M to 12B parameters [🐙](https://github.com/EleutherAI/pythia) [Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/EleutherAI/pythia?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [OLMo📑](https://alphaxiv.org/abs/2402.00838):💡Truly open language model and framework to build, study, and advance LMs, along with the training data, training and evaluation code, intermediate model checkpoints, and training logs. [🐙](https://github.com/allenai/OLMo) [Feb 2024]
- [OLMoE🐙](https://github.com/allenai/OLMoE): fully-open LLM leverages sparse Mixture-of-Experts [Sep 2024]
- [OLMo 2](https://allenai.org/blog/olmo2) [26 Nov 2024]
 ![**github stars**](https://img.shields.io/github/stars/allenai/OLMo?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/allenai/OLMoE?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Open-Sora🐙](https://github.com/hpcaitech/Open-Sora): Democratizing Efficient Video Production for All  [Mar 2024]
 ![**github stars**](https://img.shields.io/github/stars/hpcaitech/Open-Sora?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Jamba](https://www.ai21.com/blog/announcing-jamba): AI21's SSM-Transformer Model. Mamba  + Transformer + MoE [28 Mar 2024]
- [TÜLU 3📑](https://alphaxiv.org/abs/2411.15124):💡Pushing Frontiers in Open Language Model Post-Training [🐙](https://github.com/allenai/open-instruct) / demo:[✍️](https://playground.allenai.org/) [22 Nov 2024] ![**github stars**](https://img.shields.io/github/stars/allenai/open-instruct?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [ModernBERT📑](https://alphaxiv.org/abs/2412.13663): ModernBERT can handle sequences up to 8,192 tokens and utilizes sparse attention mechanisms to efficiently manage longer context lengths. [18 Dec 2024]
- OpenAI
  1. [gpt-oss🐙](https://github.com/openai/gpt-oss):💡**gpt-oss-120b** and **gpt-oss-20b** are two open-weight language models by OpenAI. [Jun 2025] ![**github stars**](https://img.shields.io/github/stars/openai/gpt-oss?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Meta (aka. Facebook)
  1. Most OSS LLM models have been built on the [Llama🐙](https://github.com/facebookresearch/llama) / [✍️](https://ai.meta.com/llama) / [🐙](https://github.com/meta-llama/llama-models)
 ![**github stars**](https://img.shields.io/github/stars/facebookresearch/llama?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/meta-llama/llama-models?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [Llama 2🤗](https://huggingface.co/blog/llama2): 1) 40% more data than Llama. 2)7B, 13B, and 70B. 3) Trained on over 1 million human annotations. 4) double the context length of Llama 1: 4K 5) Grouped Query Attention, KV Cache, and Rotary Positional Embedding were introduced in Llama 2 [18 Jul 2023] [demo🤗](https://huggingface.co/blog/llama2#demo)
  1. [Llama 3](https://llama.meta.com/llama3/): 1) 7X more data than Llama 2. 2) 8B, 70B, and 400B. 3) 8K context length [18 Apr 2024]
  1. [MEGALODON🐙](https://github.com/XuezheMax/megalodon): Long Sequence Model. Unlimited context length. Outperforms Llama 2 model. [Apr 2024]
 ![**github stars**](https://img.shields.io/github/stars/XuezheMax/megalodon?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [Llama 3.1](https://ai.meta.com/blog/meta-llama-3-1/): 405B, context length to 128K, add support across eight languages. first OSS model outperforms GTP-4o. [23 Jul 2024]
  1. [Llama 3.2](https://ai.meta.com/blog/llama-3-2-connect-2024-vision-edge-mobile-devices/): Multimodal. Include text-only models (1B, 3B) and text-image models (11B, 90B), with quantized versions of 1B and 3B [Sep 2024]
  1. [NotebookLlama🐙](https://github.com/meta-llama/llama-recipes/tree/main/recipes/quickstart/NotebookLlama): An Open Source version of NotebookLM [28 Oct 2024]
  1. [Llama 3.3](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_3/): a text-only 70B instruction-tuned model. Llama 3.3 70B approaches the performance of Llama 3.1 405B. [6 Dec 2024]
  1. [Llama 4](https://www.llama.com/docs/model-cards-and-prompt-formats/llama4_omni/):  Mixture of Experts (MoE). Llama 4 Scout (actived 17b / total 109b, 10M Context, single GPU), Llama 4 Maverick (actived 17b / total 400b, 1M Context) [🐙](https://github.com/meta-llama/llama-models/tree/main/models/llama4): Model Card [5 Apr 2025] 
- Google
  1. [Foundation Models](https://ai.google/discover/our-models/): Gemini, Veo, Gemma etc.
  1. [Gemma](http://ai.google.dev/gemma): Open weights LLM from Google DeepMind. [🐙](https://github.com/google-deepmind/gemma) / Pytorch [🐙](https://github.com/google/gemma_pytorch) [Feb 2024]
 ![**github stars**](https://img.shields.io/github/stars/google-deepmind/gemma?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/google/gemma_pytorch?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [Gemma 2](https://www.kaggle.com/models/google/gemma-2/) 2B, 9B, 27B [ref: releases](https://ai.google.dev/gemma/docs/releases) [Jun 2024]
  1. [Gemma 3](https://developers.googleblog.com/en/introducing-gemma3/):  Single GPU. Context
length of 128K tokens, SigLIP encoder, Reasoning [✍️](https://storage.googleapis.com/deepmind-media/gemma/Gemma3Report.pdf) [12 Mar 2025]
  1. [Gemini](https://gemini.google.com/app): Rebranding: Bard -> Gemini [8 Feb 2024]
  1. [Gemini 1.5✍️](https://blog.google/technology/ai/google-gemini-next-generation-model-february-2024): 1 million token context window, 1 hour of video, 11 hours of audio, codebases with over 30,000 lines of code or over 700,000 words. [Feb 2024]
  1. [Gemini 2 Flash✍️](https://blog.google/technology/google-deepmind/google-gemini-ai-update-december-2024/): Multimodal LLM with multilingual inputs/outputs, real-time capabilities (Project Astra), complex task handling (Project Mariner), and developer tools (Jules) [11 Dec 2024]
  1. Gemini 2.0 Flash Thinking Experimental [19 Dec 2024]
  1. [Gemini 2.5✍️](https://blog.google/technology/google-deepmind/gemini-model-thinking-updates-march-2025/): strong reasoning and code. 1 million token context [25 Mar 2025] -> [I/O 2025✍️](https://blog.google/technology/ai/io-2025-keynote) Deep Think, 1M-token context, Native audio output, Project Mariner: AI-powered computer control. [20 May 2025] [Gemini 2.5: Pushing the Frontier with Advanced Reasoning, Multimodality, Long Context, and Next Generation Agentic Capabilities.📑](https://alphaxiv.org/abs/2507.06261)
  1. [Gemma 3n](https://developers.googleblog.com/en/introducing-gemma-3n/): The next generation of Gemini Nano. Gemma 3n uses DeepMind’s Per-Layer Embeddings (PLE) to run 5B/8B models at 2GB/3GB RAM. [20 May 2025]
  1. [gemini/cookbook🐙](https://github.com/google-gemini/cookbook)
- Anthrophic
  1. [Claude 3✍️](https://www.anthropic.com/news/claude-3-family), the largest version of the new LLM, outperforms rivals GPT-4 and Google’s Gemini 1.0 Ultra. Three variants: Opus, Sonnet, and Haiku. [Mar 2024]
  1. [Claude 3.7 Sonnet and Claude Code✍️](https://www.anthropic.com/news/claude-3-7-sonnet): the first hybrid reasoning model. [✍️](https://assets.anthropic.com/m/785e231869ea8b3b/original/claude-3-7-sonnet-system-card.pdf) [25 Feb 2025]
  1. [Claude 4✍️](https://www.anthropic.com/news/claude-4): Claude Opus 4 (72.5% on SWE-bench),  Claude Sonnet 4 (72.7% on SWE-bench). Extended Thinking Mode (Beta). Parallel Tool Use & Memory. Claude Code SDK. AI agents: code execution, MCP connector, Files API, and 1-hour prompt caching. [23 May 2025]
  1. [anthropic/cookbook🐙](https://github.com/anthropics/anthropic-cookbook)
- Microsoft
  1. phi-series: cost-effective small language models (SLMs) [✍️](https://azure.microsoft.com/en-us/products/phi) [🐙](https://aka.ms/Phicookbook): Cookbook
  1. [Phi-1📑](https://alphaxiv.org/abs/2306.11644): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2306.11644)]: Despite being small in size, phi-1 attained 50.6% on HumanEval and 55.5% on MBPP. Textbooks Are All You Need. [✍️](https://analyticsindiamag.com/microsoft-releases-1-3-bn-parameter-language-model-outperforms-llama/) [20 Jun 2023]
  1. [Phi-1.5📑](https://alphaxiv.org/abs/2309.05463): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.05463)]: Textbooks Are All You Need II. Phi 1.5 is trained solely on synthetic data. Despite having a mere 1 billion parameters compared to Llama 7B's much larger model size, Phi 1.5 often performs better in benchmark tests. [11 Sep 2023]
  1. phi-2: open source, and 50% better at mathematical reasoning. [🐙🤗](https://huggingface.co/microsoft/phi-2) [Dec 2023]
  1. phi-3-vision (multimodal), phi-3-small, phi-3 (7b), phi-sillica (Copilot+PC designed for NPUs)
  1. [Phi-3📑](https://alphaxiv.org/abs/2404.14219): Phi-3-mini, with 3.8 billion parameters, supports 4K and 128K context, instruction tuning, and hardware optimization. [22 Apr 2024] [✍️](https://azure.microsoft.com/en-us/blog/introducing-phi-3-redefining-whats-possible-with-slms/)
  1. phi-3.5-MoE-instruct: [🤗](https://huggingface.co/microsoft/Phi-3.5-MoE-instruct) [Aug 2024]
  1. [Phi-4📑](https://alphaxiv.org/abs/2412.08905): Specializing in Complex Reasoning [✍️](https://techcommunity.microsoft.com/blog/aiplatformblog/introducing-phi-4-microsoft%E2%80%99s-newest-small-language-model-specializing-in-comple/4357090) [12 Dec 2024]
  1. [Phi-4-multimodal / mini🤗](https://huggingface.co/microsoft/Phi-4-multimodal-instruct/blob/main/phi_4_mm.tech_report.02252025.pdf) 5.6B. speech, vision, and text processing into a single, unified architecture. [26 Feb 2025]
  1. [Phi-4-reasoning✍️](https://azure.microsoft.com/en-us/blog/one-year-of-phi-small-language-models-making-big-leaps-in-ai/): Phi-4-reasoning, Phi-4-reasoning-plus, Phi-4-mini-reasoning [30 Apr 2025]
  1. [Phi-4-mini-flash-reasoning✍️](https://azure.microsoft.com/en-us/blog/reasoning-reimagined-introducing-phi-4-mini-flash-reasoning/): 3.8B, 64K context, Single GPU, Decoder-Hybrid-Decoder architecture  [9 Jul 2025]
- NVIDIA
  1. [Nemotron-4 340B](https://research.nvidia.com/publication/2024-06_nemotron-4-340b): Synthetic Data Generation for Training Large Language Models [14 Jun 2024]
- Amazon
  1. [Amazon Nova Foundation Models](https://aws.amazon.com/de/ai/generative-ai/nova/): Text only - Micro, Multimodal - Light, Pro [3 Dec 2024]
  1. [The Amazon Nova Family of Models: Technical Report and Model Card📑](https://alphaxiv.org/abs/2506.12103) [17 Mar 2025]
- Huggingface
  1. [Open R1🐙](https://github.com/huggingface/open-r1): A fully open reproduction of DeepSeek-R1. [25 Jan 2025]
- Mistral
  - Founded in April 2023. French tech.
  1. Model overview [✍️](https://docs.mistral.ai/getting-started/models/)
  1. [NeMo](https://mistral.ai/news/mistral-nemo/): 12B model with 128k context length that outperforms LLama 3 8B [18 Jul 2024]
  1. [Mistral OCR](https://mistral.ai/news/mistral-ocr): Precise text recognition with up to 99% accuracy. Multimodal. Browser based [6 Mar 2025]
- Groq
  - Founded in 2016. low-latency AI inference H/W. American tech.
  1. [Llama-3-Groq-Tool-Use](https://wow.groq.com/introducing-llama-3-groq-tool-use-models/): a model optimized for function calling [Jul 2024]
- Alibaba
  1. [Qwen Chat](https://chat.qwen.ai/): Official website for testing Qwen models.
  1. [Qwen series🐙](https://github.com/QwenLM) > [Qwen2🐙](https://github.com/QwenLM/Qwen2): 29 languages. 5 sizes, including Qwen2-0.5B, Qwen2-1.5B, Qwen2-7B, Qwen2-57B-A14B, and Qwen2-72B. [Feb 2024]
  1. [Qwen2.5-VL🐙](https://github.com/QwenLM/Qwen2.5-VL): Vision-language models incl. Video Understanding [Auf 2024]
 ![**github stars**](https://img.shields.io/github/stars/QwenLM/Qwen2?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [QwQ-32B](https://qwen-ai.com/): Reasoning model [5 Mar 2025]
  1. [Qwen2.5-Omni📑](https://alphaxiv.org/abs/2503.20215): a single end-to-end multimodal model. text, audio, image, and video, and generate both text and speech in real time. Thinker(transformer decoder)-Talker(autoregressive decoder) architecture. [🐙](https://github.com/QwenLM/Qwen2.5-Omni) ![**github stars**](https://img.shields.io/github/stars/QwenLM/Qwen2.5-Omni?style=flat-square&label=%20&color=blue&cacheSeconds=36000) [26 Mar 2025]
  1. [Qwen 3](https://qwenlm.github.io/blog/qwen3/): Hybrid Thinking Modes, Agentic Capabilities, Support 119 languages [29 Apr 2025]
  - A list of models: [🐙](https://github.com/QwenLM)
- Baidu
  1. [ERNIE Bot's official website](https://yiyan.baidu.com/): ERNIE X1 (deep-thinking reasoning) and ERNIE 4.5 (multimodal) [16 Mar 2025]
  1. A list of models & libraries: [🐙](https://github.com/PaddlePaddle/ERNIE)
- Cohere
  - Founded in 2019. Canadian multinational tech.
  1. [Command R+🤗](https://huggingface.co/collections/CohereForAI/c4ai-command-r-plus-660ec4c34f7a69c50ce7f7b9): The performant model for RAG capabilities, multilingual support, and tool use. [Aug 2024]
  1. [An Overview of Cohere’s Models](https://docs.cohere.com/v2/docs/models) | [Playground](https://dashboard.cohere.com/playground)
- Deepseek
  - Founded in 2023, is a Chinese company dedicated to AGI.
  1. [DeepSeek-V3🐙](https://github.com/deepseek-ai/DeepSeek-V3): Mixture-of-Experts (MoE) with 671B. [26 Dec 2024]
  1. [DeepSeek-R1🐙](https://github.com/deepseek-ai/DeepSeek-R1):💡an open source reasoning model. Group Relative Policy Optimization (GRPO). Base -> RL -> SFT -> RL -> SFT -> RL [20 Jan 2025] [ref📑](https://alphaxiv.org/abs/2503.11486): A Review of DeepSeek Models' Key Innovative Techniques [14 Mar 2025]
  1. [Janus🐙](https://github.com/deepseek-ai/Janus): Multimodal understanding and visual generation. [28 Jan 2025]
  1. [DeepSeek-V3🤗](https://huggingface.co/deepseek-ai/DeepSeek-V3): 671B. Top-tier performance in coding and reasoning tasks [25 Mar 2025]
  1. [DeepSeek-Prover-V2🐙](https://github.com/deepseek-ai/DeepSeek-Prover-V2): Mathematical reasoning [30 Apr 2025]
  1. [DeepSeek-v3.1🤗](https://huggingface.co/deepseek-ai/DeepSeek-V3.1): Think/Non‑Think hybrid reasoning. 128K and MoE. Agent abilities.  [19 Aug 2025]
  1. A list of models: [🐙](https://github.com/deepseek-ai)
- Tencent
  - Founded in 1998, Tencent is a Chinese company dedicated to various technology sectors, including social media, gaming, and AI development.
  - [Hunyuan-Large](https://alphaxiv.org/pdf/2411.02265): An open-source MoE model with open weights. [4 Nov 2024] [🐙](https://github.com/Tencent/Tencent-Hunyuan-Large) ![**github stars**](https://img.shields.io/github/stars/Tencent/Tencent-Hunyuan-Large?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - [Hunyuan-T1](https://tencent.github.io/llm.hunyuan.T1/README_EN.html): Reasoning model [21 Mar 2025]
  - A list of models: [🐙](https://github.com/Tencent-Hunyuan)
- Xiaomi
  - Founded in 2010, Xiaomi is a Chinese company known for its innovative consumer electronics and smart home products.
  - [Mimo🐙](https://github.com/XiaomiMiMo/MiMo): 7B. advanced reasoning for code and math [30 Apr 2025]
- Qualcomm
  1. [Qualcomm’s on-device AI models🤗](https://huggingface.co/qualcomm): Bring generative AI to mobile devices [Feb 2024]
- xAI
  - xAI is an American AI company founded by Elon Musk in March 2023
  1. [Grok](https://x.ai/blog/grok-os): 314B parameter Mixture-of-Experts (MoE) model. Released under the Apache 2.0 license. Not includeded training code. Developed by JAX [🐙](https://github.com/xai-org/grok) [17 Mar 2024]
 ![**github stars**](https://img.shields.io/github/stars/xai-org/grok?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [Grok-2 and Grok-2 mini](https://x.ai/blog/grok-2) [13 Aug 2024]
  1. [Grok-3](https://x.ai/grok): 200,000 GPUs to train. Grok 3 beats GPT-4o on AIME, GPQA. Grok 3 Reasoning and Grok 3 mini Reasoning. [17 Feb 2025]
  1. [Grok-4](https://x.ai/news/grok-4): Humanity’s Last Exam, Grok 4 Heavy scored 44.4% [9 Jul 2025]
  1. [Grok-2.5](https://x.com/elonmusk/status/1959379349322313920): Grok 2.5 Goes Open Source [24 Aug 2025]
- Databricks
  1. [DBRX](https://www.databricks.com/blog/introducing-dbrx-new-state-art-open-llm): MoE, open, general-purpose LLM created by Databricks. [🐙](https://github.com/databricks/dbrx) [27 Mar 2024]
 ![**github stars**](https://img.shields.io/github/stars/databricks/dbrx?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Apple
  1. [OpenELM](https://machinelearning.apple.com/research/openelm): Apple released a Transformer-based language model. Four sizes of the model: 270M, 450M, 1.1B, and 3B parameters. [April 2024]
  1. [Apple Intelligence Foundation Language Models](https://machinelearning.apple.com/research/apple-intelligence-foundation-language-models): 1. A 3B on-device model used for language tasks like summarization and Writing Tools. 2. A large Server model used for language tasks too complex to do on-device. [10 Jun 2024]
- IBM
  1. [Granite Guardian🐙](https://github.com/ibm-granite/granite-guardian): a collection of models designed to detect risks in prompts and responses [10 Dec 2024]
- Moonshot AI
  - Moonshot AI is a Beijing-based Chinese AI company founded in March 2023
  1. [Kimi-K2🐙](https://github.com/MoonshotAI/Kimi-K2): 1T parameter MoE model. MuonClip Optimizer. Agentic Intelligence. [11 Jul 2025]
- Z.ai
  - formerly Zhipu, Beijing-based Chinese AI company founded in March 2019
  1. [GLM-4.5🐙](https://github.com/zai-org/GLM-4.5): An open-source large language model designed for intelligent agents
- GPT for Domain Specific [🔗](llm.md/#gpt-for-domain-specific)
- MLLM (multimodal large language model) [🔗](llm.md/#mllm-multimodal-large-language-model)
- Large Language Models (in 2023) [🔗](llm.md/#large-language-models-in-2023)
- Llama variants emerged in 2023</summary>
  - [Falcon LLM](https://falconllm.tii.ae/) Apache 2.0 license [Mar 2023]
  - [Alpaca](https://crfm.stanford.edu/2023/03/13/alpaca.html): Fine-tuned from the LLaMA 7B model [Mar 2023]
  - [vicuna](https://vicuna.lmsys.org/): 90% ChatGPT Quality [Mar 2023]
  - [dolly](https://www.databricks.com/blog/2023/03/24/hello-dolly-democratizing-magic-chatgpt-open-models.html): Databricks [Mar 2023]
  - [Cerebras-GPT](https://www.cerebras.net/blog/cerebras-gpt-a-family-of-open-compute-efficient-large-language-models/): 7 GPT models ranging from 111m to 13b parameters. [Mar 2023]
  - [Koala](https://bair.berkeley.edu/blog/2023/04/03/koala/): Focus on dialogue data gathered from the web.  [Apr 2023]
  - [StableVicuna](https://stability.ai/blog/stablevicuna-open-source-rlhf-chatbot) First Open Source RLHF LLM Chatbot [Apr 2023]
  - Upstage's 70B Language Model Outperforms GPT-3.5: [✍️](https://en.upstage.ai/newsroom/upstage-huggingface-llm-no1) [1 Aug 2023]

</details>

### **LLM for Domain Specific**

- [AlphaFold3🐙](https://github.com/Ligo-Biosciences/AlphaFold3): Open source implementation of AlphaFold3 [Nov 2023] / [OpenFold🐙](https://github.com/aqlaboratory/openfold): PyTorch reproduction of AlphaFold 2 [Sep 2021] ![**github stars**](https://img.shields.io/github/stars/Ligo-Biosciences/AlphaFold3?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/aqlaboratory/openfold?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [BioGPT📑](https://alphaxiv.org/abs/2210.10341): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2210.10341)]: Generative Pre-trained Transformer for Biomedical Text Generation and Mining [🐙](https://github.com/microsoft/BioGPT) [19 Oct 2022] ![**github stars**](https://img.shields.io/github/stars/microsoft/BioGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Galactica📑](https://alphaxiv.org/abs/2211.09085): A Large Language Model for Science [16 Nov 2022]
- [TimeGPT](https://nixtla.github.io/nixtla/): The First Foundation Model for Time Series Forecasting [🐙](https://github.com/Nixtla/neuralforecast) [Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/Nixtla/neuralforecast?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [BloombergGPT📑](https://alphaxiv.org/abs/2303.17564): A Large Language Model for Finance [30 Mar 2023]
- [Huggingface StarCoder: A State-of-the-Art LLM for Code🤗](https://huggingface.co/blog/starcoder): [🐙🤗](https://huggingface.co/bigcode/starcoder) [May 2023]
- [FrugalGPT📑](https://alphaxiv.org/abs/2305.05176): LLM with budget constraints, requests are cascaded from low-cost to high-cost LLMs. [🐙](https://github.com/stanford-futuredata/FrugalGPT) [9 May 2023] ![**github stars**](https://img.shields.io/github/stars/stanford-futuredata/FrugalGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Code Llama📑](https://alphaxiv.org/abs/2308.12950): Built on top of Llama 2, free for research and commercial use. [✍️](https://ai.meta.com/blog/code-llama-large-language-model-coding/) / [🐙](https://github.com/facebookresearch/codellama) [24 Aug 2023] ![**github stars**](https://img.shields.io/github/stars/facebookresearch/codellama?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [MechGPT📑](https://alphaxiv.org/abs/2310.10445): Language Modeling Strategies for Mechanics and Materials [🐙](https://github.com/lamm-mit/MeLM) [16 Oct 2023] ![**github stars**](https://img.shields.io/github/stars/lamm-mit/MeLM?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [MeshGPT](https://nihalsid.github.io/mesh-gpt/): Generating Triangle Meshes with Decoder-Only Transformers [27 Nov 2023]
- [EarthGPT📑](https://alphaxiv.org/abs/2401.16822): A Universal Multi-modal Large Language Model for Multi-sensor Image Comprehension in Remote Sensing Domain [30 Jan 2024]
- [SaulLM-7B📑](https://alphaxiv.org/abs/2403.03883): A pioneering Large Language Model for Law [6 Mar 2024]
- [Devin AI](https://preview.devin.ai/): Devin is an AI software engineer developed by Cognition AI [12 Mar 2024]
- [DeepSeek-Coder-V2🐙](https://github.com/deepseek-ai/DeepSeek-Coder-V2): Open-source Mixture-of-Experts (MoE) code language model [17 Jun 2024]
 ![**github stars**](https://img.shields.io/github/stars/deepseek-ai/DeepSeek-Coder-V2?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Qwen2-Math🐙](https://github.com/QwenLM/Qwen2-Math): math-specific LLM / [Qwen2-Audio🐙](https://github.com/QwenLM/Qwen2-Audio): large-scale audio-language model [Aug 2024] / [Qwen 2.5-Coder🐙](https://github.com/QwenLM/Qwen2.5-Coder) [18 Sep 2024]
 ![**github stars**](https://img.shields.io/github/stars/QwenLM/Qwen2-Math?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/QwenLM/Qwen2-Audio?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/QwenLM/Qwen2.5-Coder?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Chai-1🐙](https://github.com/chaidiscovery/chai-lab): a multi-modal foundation model for molecular structure prediction [Sep 2024]
 ![**github stars**](https://img.shields.io/github/stars/chaidiscovery/chai-lab?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Prithvi WxC📑](https://alphaxiv.org/abs/2409.13598): In collaboration with NASA, IBM is releasing an open-source foundation model for Weather and Climate [✍️](https://research.ibm.com/blog/foundation-model-weather-climate) [20 Sep 2024]
- [AlphaChip](https://deepmind.google/discover/blog/how-alphachip-transformed-computer-chip-design/): Reinforcement learning-based model for designing physical chip layouts. [26 Sep 2024]
- [OpenCoder🐙](https://github.com/OpenCoder-llm/OpenCoder-llm): 1.5B and 8B base and open-source Code LLM, supporting both English and Chinese. [Oct 2024] ![**github stars**](https://img.shields.io/github/stars/OpenCoder-llm/OpenCoder-llm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Video LLMs for Temporal Reasoning in Long Videos📑](https://alphaxiv.org/abs/2412.02930): TemporalVLM, a video LLM excelling in temporal reasoning and fine-grained understanding of long videos, using time-aware features and validated on datasets like TimeIT and IndustryASM for superior performance. [4 Dec 2024]
- [ESM3: A frontier language model for biology](https://www.evolutionaryscale.ai/blog/esm3-release): Simulating 500 million years of evolution [🐙](https://github.com/evolutionaryscale/esm) / [✍️](https://doi.org/10.1101/2024.07.01.600583) [31 Dec 2024]  ![**github stars**](https://img.shields.io/github/stars/evolutionaryscale/esm?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [AI for Scaling Legal Reform: Mapping and Redacting Racial Covenants in Santa Clara County📑](https://alphaxiv.org/abs/2503.03888): a fine-tuned open LLM to detect racial covenants in 24　million housing documents, cutting 86,500 hours of manual work. [12 Feb 2025]
- Gemma series
  1. [Gemma series in Huggingface🤗](https://huggingface.co/google)
  1. [PaliGemma📑](https://alphaxiv.org/abs/2407.07726): a 3B VLM [10 Jul 2024]
  1. [DataGemma✍️](https://blog.google/technology/ai/google-datagemma-ai-llm/) [12 Sep 2024] / [NotebookLM✍️](https://blog.google/technology/ai/notebooklm-audio-overviews/): LLM-powered notebook. free to use, not open-source. [12 Jul 2023]
  1. [PaliGemma 2📑](https://alphaxiv.org/abs/2412.03555): VLMs
 at 3 different sizes (3B, 10B, 28B)  [4 Dec 2024]
  1. [TxGemma](https://developers.googleblog.com/en/introducing-txgemma-open-models-improving-therapeutics-development/): Therapeutics development [25 Mar 2025]
  1. [Dolphin Gemma✍️](https://blog.google/technology/ai/dolphingemma/): Decode dolphin communication [14 Apr 2025]
  1. [MedGemma](https://deepmind.google/models/gemma/medgemma/): Model fine-tuned for biomedical text and image understanding. [20 May 2025]
  1. [SignGemma](https://x.com/GoogleDeepMind/status/1927375853551235160): Vision-language model for sign language recognition and translation. [27 May 2025]
- [AlphaGenome](https://deepmind.google/discover/blog/alphagenome-ai-for-better-understanding-the-genome): DeepMind’s advanced AI model, launched in June 2025, is designed to analyze the regulatory “dark matter” of the genome—specifically, the 98% of DNA that does not code for proteins but instead regulates when and how genes are expressed. [June 2025]
- [Qwen3-Coder🐙](https://github.com/QwenLM/Qwen3-Coder): Qwen3-Coder is the code version of Qwen3, the large language model series developed by Qwen team, Alibaba Cloud. [Jul 2025] ![**github stars**](https://img.shields.io/github/stars/QwenLM/Qwen3-Coder?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **MLLM (multimodal large language model)**

- [Understanding Multimodal LLMs✍️](https://magazine.sebastianraschka.com/p/understanding-multimodal-llms):💡Two main approaches to building multimodal LLMs: 1. Unified Embedding Decoder Architecture approach; 2. Cross-modality Attention Architecture approach. [3 Nov 2024]

  <img src="../files/mllm.png" width=400 alt="mllm" />

- [Multimodal Foundation Models: From Specialists to General-Purpose Assistants📑](https://alphaxiv.org/abs/2309.10020): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.10020)]: A comprehensive survey of the taxonomy and evolution of multimodal foundation models that demonstrate vision and vision-language capabilities. Specific-Purpose 1. Visual understanding tasks 2. Visual generation tasks General-Purpose 3. General-purpose interface. [18 Sep 2023]
- [Awesome Multimodal Large Language Models🐙](https://github.com/BradyFU/Awesome-Multimodal-Large-Language-Models): Latest Papers and Datasets on Multimodal Large Language Models, and Their Evaluation. [Jun 2023]
 ![**github stars**](https://img.shields.io/github/stars/BradyFU/Awesome-Multimodal-Large-Language-Models?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- Benchmarking Multimodal LLMs.
  - LLaVA-1.5 achieves SoTA on a broad range of 11 tasks incl. SEED-Bench.
  - [SEED-Bench📑](https://alphaxiv.org/abs/2307.16125): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.16125)]: Benchmarking Multimodal LLMs [🐙](https://github.com/AILab-CVC/SEED-Bench) [30 Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/AILab-CVC/SEED-Bench?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Molmo and PixMo📑](https://alphaxiv.org/abs/2409.17146): Open Weights and Open Data for State-of-the-Art Multimodal Models [✍️](https://molmo.allenai.org/) [25 Sep 2024] <!-- <img src="../files/multi-llm.png" width="180" /> -->
- Optimizing Memory Usage for Training LLMs and Vision Transformers: When applying 10 techniques to a vision transformer, we reduced the memory consumption 20x on a single GPU. [✍️](https://lightning.ai/pages/community/tutorial/pytorch-memory-vit-llm/) / [🐙](https://github.com/rasbt/pytorch-memory-optim) [2 Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/rasbt/pytorch-memory-optim?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

#### OSS 

- [CLIP📑](https://alphaxiv.org/abs/2103.00020): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2103.00020)]: CLIP (Contrastive Language-Image Pretraining), Trained on a large number of internet text-image pairs and can be applied to a wide range of tasks with zero-shot learning. [🐙](https://github.com/openai/CLIP) [26 Feb 2021]
 ![**github stars**](https://img.shields.io/github/stars/openai/CLIP?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [BLIP-2📑](https://alphaxiv.org/abs/2301.12597) [30 Jan 2023]: [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2301.12597)]: Salesforce Research, Querying Transformer (Q-Former) / [🐙](https://github.com/salesforce/LAVIS/blob/main/lavis/models/blip2_models/blip2_qformer.py) / [🤗](https://huggingface.co/blog/blip-2) / [📺](https://www.youtube.com/watch?v=k0DAtZCCl1w) / [BLIP📑](https://alphaxiv.org/abs/2201.12086): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2201.12086)]: [🐙](https://github.com/salesforce/BLIP) [28 Jan 2022]
 ![**github stars**](https://img.shields.io/github/stars/salesforce/BLIP?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  - `Q-Former (Querying Transformer)`: A transformer model that consists of two submodules that share the same self-attention layers: an image transformer that interacts with a frozen image encoder for visual feature extraction, and a text transformer that can function as both a text encoder and a text decoder.
  - Q-Former is a lightweight transformer which employs a set of learnable query vectors to extract visual features from the frozen image encoder. It acts as an information bottleneck between the frozen image encoder and the frozen LLM.
- [TaskMatrix, aka VisualChatGPT📑](https://alphaxiv.org/abs/2303.04671): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.04671)]: Microsoft TaskMatrix [🐙](https://github.com/microsoft/TaskMatrix); GroundingDINO + [SAM📑](https://alphaxiv.org/abs/2304.02643) / [🐙](https://github.com/facebookresearch/segment-anything) [8 Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/TaskMatrix?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/facebookresearch/segment-anything?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [GroundingDINO📑](https://alphaxiv.org/abs/2303.05499): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.05499)]: DINO with Grounded Pre-Training for Open-Set Object Detection [🐙](https://github.com/IDEA-Research/GroundingDINO) [9 Mar 2023]
 ![**github stars**](https://img.shields.io/github/stars/IDEA-Research/GroundingDINO?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLaVa📑](https://alphaxiv.org/abs/2304.08485): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2304.08485)]: Large Language-and-Vision Assistant [🐙](https://llava-vl.github.io/) [17 Apr 2023]
  - Simple linear layer to connect image features into the word embedding space. A trainable projection matrix W is applied to the visual features Zv, transforming them into visual embedding tokens Hv. These tokens are then concatenated with the language embedding sequence Hq to form a single sequence. Note that Hv and Hq are not multiplied or added, but concatenated, both are same dimensionality.
  - [LLaVA-1.5📑](https://alphaxiv.org/abs/2310.03744): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.03744)]: is out! [🐙](https://github.com/haotian-liu/LLaVA): Changing from a linear projection to an MLP cross-modal. [5 Oct 2023]
 ![**github stars**](https://img.shields.io/github/stars/haotian-liu/LLaVA?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [MiniGPT-4 & MiniGPT-v2📑](https://alphaxiv.org/abs/2304.10592): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2304.10592)]: Enhancing Vision-language Understanding with Advanced Large Language Models [🐙](https://minigpt-4.github.io/) [20 Apr 2023]
- [openai/shap-e📑](https://alphaxiv.org/abs/2305.02463) Generate 3D objects conditioned on text or images [3 May 2023] [🐙](https://github.com/openai/shap-e)
 ![**github stars**](https://img.shields.io/github/stars/openai/shap-e?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Drag Your GAN📑](https://alphaxiv.org/abs/2305.10973): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.10973)]: Interactive Point-based Manipulation on the Generative Image Manifold [🐙](https://github.com/Zeqiang-Lai/DragGAN) [18 May 2023]
 ![**github stars**](https://img.shields.io/github/stars/Zeqiang-Lai/DragGAN?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Video-ChatGPT📑](https://alphaxiv.org/abs/2306.05424): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2306.05424)]: a video conversation model capable of generating meaningful conversation about videos. / [🐙](https://github.com/mbzuai-oryx/Video-ChatGPT) [8 Jun 2023]
 ![**github stars**](https://img.shields.io/github/stars/mbzuai-oryx/Video-ChatGPT?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [moondream🐙](https://github.com/vikhyat/moondream): an OSS tiny vision language model. Built using SigLIP, Phi-1.5, LLaVA dataset. [Dec 2023]
 ![**github stars**](https://img.shields.io/github/stars/vikhyat/moondream?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [MiniCPM-V🐙](https://github.com/OpenBMB/MiniCPM-V): MiniCPM-Llama3-V 2.5: A GPT-4V Level Multimodal LLM on Your Phone [Jan 2024]
 ![**github stars**](https://img.shields.io/github/stars/OpenBMB/MiniCPM-V?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [mini-omni2🐙](https://github.com/gpt-omni/mini-omni2): [✍️](alphaxiv.org/abs/2410.11190): Towards Open-source GPT-4o with Vision, Speech and Duplex Capabilities. [15 Oct 2024]
 ![**github stars**](https://img.shields.io/github/stars/gpt-omni/mini-omni2?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLaVA-CoT📑](https://alphaxiv.org/abs/2411.10440): (FKA. LLaVA-o1) Let Vision Language Models Reason Step-by-Step. [🐙](https://github.com/PKU-YuanGroup/LLaVA-CoT) [15 Nov 2024]
- [MiniCPM-o🐙](https://github.com/OpenBMB/MiniCPM-o): A GPT-4o Level MLLM for Vision, Speech and Multimodal Live Streaming on Your Phone [15 Jan 2025]
- Vision capability to a LLM [✍️](https://cloud.google.com/blog/products/ai-machine-learning/multimodal-generative-ai-search/): `The model has three sub-models`: A model to obtain image embeddings -> A text model to obtain text embeddings -> A model to learn the relationships between them [22 Aug 2023]
- [Ultravox🐙](https://github.com/fixie-ai/ultravox): A fast multimodal LLM for real-time voice [May 2024]

#### MLLM Models

- Meta (aka. Facebook)
  1. [facebookresearch/ImageBind📑](https://alphaxiv.org/abs/2305.05665): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.05665)]: ImageBind One Embedding Space to Bind Them All [🐙](https://github.com/facebookresearch/ImageBind) [9 May 2023]
 ![**github stars**](https://img.shields.io/github/stars/facebookresearch/ImageBind?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [facebookresearch/segment-anything(SAM)📑](https://alphaxiv.org/abs/2304.02643): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2304.02643)]: The repository provides code for running inference with the SegmentAnything Model (SAM), links for downloading the trained model checkpoints, and example notebooks that show how to use the model. [🐙](https://github.com/facebookresearch/segment-anything) [5 Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/facebookresearch/segment-anything?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
  1. [facebookresearch/SeamlessM4T📑](https://alphaxiv.org/abs/2308.11596): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2308.11596)]: SeamlessM4T is the first all-in-one multilingual multimodal AI translation and transcription model. This single model can perform speech-to-text, speech-to-speech, text-to-speech, and text-to-text translations for up to 100 languages depending on the task. [✍️](https://about.fb.com/news/2023/08/seamlessm4t-ai-translation-model/) [22 Aug 2023]
  1. [Chameleon📑](https://alphaxiv.org/abs/2405.09818): Early-fusion token-based mixed-modal models capable of understanding and generating images and text in any arbitrary sequence. The unified approach uses fully token-based representations for both image and textual modalities. no vision-encoder. [16 May 2024]
  1. [Models and libraries](https://ai.meta.com/resources/models-and-libraries/)
- Microsoft
  1. Language Is Not All You Need: Aligning Perception with Language Models [Kosmos-1📑](https://alphaxiv.org/abs/2302.14045): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2302.14045)] [27 Feb 2023]
  1. [Kosmos-2📑](https://alphaxiv.org/abs/2306.14824): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2306.14824)]: Grounding Multimodal Large Language Models to the World [26 Jun 2023]
  1. [Kosmos-2.5📑](https://alphaxiv.org/abs/2309.11419): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.11419)]: A Multimodal Literate Model [20 Sep 2023]
  1. [BEiT-3📑](https://alphaxiv.org/abs/2208.10442): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2208.10442)]: Image as a Foreign Language: BEiT Pretraining for Vision and Vision-Language Tasks [22 Aug 2022]
  1. [TaskMatrix.AI📑](https://alphaxiv.org/abs/2303.16434): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.16434)]: TaskMatrix connects ChatGPT and a series of Visual Foundation Models to enable sending and receiving images during chatting. [29 Mar 2023]
  1. [Florence-2📑](https://alphaxiv.org/abs/2311.06242): Advancing a unified representation for various vision tasks, demonstrating specialized models like `CLIP` for classification, `GroundingDINO` for object detection, and `SAM` for segmentation. [🤗](https://huggingface.co/microsoft/Florence-2-large) [10 Nov 2023]
  1. [LLM2CLIP🐙](https://github.com/microsoft/LLM2CLIP): Directly integrating LLMs into CLIP causes catastrophic performance drops. We propose LLM2CLIP, a caption contrastive fine-tuning method that leverages LLMs to enhance CLIP. [7 Nov 2024]
  1. [Florence-VL📑](https://alphaxiv.org/abs/2412.04424): A multimodal large language model (MLLM) that integrates Florence-2. [5 Dec 2024]
  1. [Magma🐙](https://github.com/microsoft/Magma): Magma: A Foundation Model for Multimodal AI Agents [18 Feb 2025]
- Apple
  1. [4M-21📑](https://alphaxiv.org/abs/2406.09406): An Any-to-Any Vision Model for Tens of Tasks and Modalities. [13 Jun 2024]
- Hugging Face
  1. [SmolVLM🤗](https://huggingface.co/blog/smolvlm): 2B small vision language models. [🤗](https://huggingface.co/HuggingFaceTB/SmolVLM-Instruct) / finetuning:[🐙](https://github.com/huggingface/smollm/blob/main/finetuning/Smol_VLM_FT.ipynb) [24 Nov 2024]
