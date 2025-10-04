## **Datasets for LLM Training**

- LLM-generated datasets:
  1. [Self-Instruct📑](https://alphaxiv.org/abs/2212.10560): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2212.10560)]: Seed task pool with a set of human-written instructions. [20 Dec 2022]
  1. [Self-Alignment with Instruction Backtranslation📑](https://alphaxiv.org/abs/2308.06259): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2308.06259)]: Without human seeding, use LLM to produce instruction-response pairs. The process involves two steps: self-augmentation and self-curation. [11 Aug 2023]
- [LLMDataHub: Awesome Datasets for LLM Training✨](https://github.com/Zjh-819/LLMDataHub): A quick guide (especially) for trending instruction finetuning datasets
 ![**github stars**](https://img.shields.io/github/stars/Zjh-819/LLMDataHub?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Open LLMs and Datasets✨](https://github.com/eugeneyan/open-llms): A list of open LLMs available for commercial use.
 ![**github stars**](https://img.shields.io/github/stars/eugeneyan/open-llms?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [SQuAD](https://rajpurkar.github.io/SQuAD-explorer/): The Stanford Question Answering Dataset (SQuAD), a set of Wikipedia articles, 100,000+ question-answer pairs on 500+ articles. [16 Jun 2016]
- [Synthetic Data Vault (SDV) ✨](https://github.com/sdv-dev/SDV): Synthetic data generation for tabular data [May 2018] ![**github stars**](https://img.shields.io/github/stars/sdv-dev/SDV?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [RedPajama](https://together.ai/blog/redpajama): LLaMA training dataset of over 1.2 trillion tokens [✨](https://github.com/togethercomputer/RedPajama-Data) [17 Apr 2023]
 ![**github stars**](https://img.shields.io/github/stars/togethercomputer/RedPajama-Data?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [FineWeb🤗](https://huggingface.co/datasets/HuggingFaceFW/fineweb):🤗HuggingFace. crawled 15 trillion tokens of high-quality web data from the summer of 2013 to March 2024. [Apr 2024]
- [MS MARCO Web Search✨](https://github.com/microsoft/MS-MARCO-Web-Search): A large-scale information-rich web dataset, featuring millions of real clicked query-document labels [Apr 2024]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/MS-MARCO-Web-Search?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Nemotron-Personas-Japan: Synthesized Data for Sovereign AI🤗](https://huggingface.co/blog/nvidia/nemotron-personas-japan): The first open synthetic dataset that captures Japan's demographic, geographic, and cultural spectrum.  [23 Sep 2025]
- [Synthetic Data of LLMs✨](https://github.com/wasiahmad/Awesome-LLM-Synthetic-Data): A reading list on LLM based Synthetic Data Generation [Oct 2024]
 ![**github stars**](https://img.shields.io/github/stars/wasiahmad/Awesome-LLM-Synthetic-Data?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Open Thoughts✨](https://github.com/open-thoughts/open-thoughts): Fully Open Data Curation for Thinking Models [28 Jan 2025] ![**github stars**](https://img.shields.io/github/stars/open-thoughts/open-thoughts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

Pretrain for a base model

```json
{
    "text": ...,
    "meta": {"url": "...", "timestamp": "...", "source": "...", "language": "...", ...},
    "red_pajama_subset": "common_crawl" | "c4" | "github" | "books" | "arxiv" | "wikipedia" | "stackexchange"
}
```

databricks-dolly-15k: Instruction-Tuned [✨🤗](https://huggingface.co/datasets/databricks/databricks-dolly-15k): SFT training - QA pairs or Dialog

```json
{
  "prompt": "What is the capital of France?",
  "response": "The capital of France is Paris."
},
{
    "prompt": "Can you give me a recipe for chocolate chip cookies?",
    "response": "Sure! ..."
}
```

[Anthropic human-feedback✨🤗](https://huggingface.co/datasets/Anthropic/hh-rlhf): RLHF training - Chosen and Rejected pairs

```json
{
  "chosen": "I'm sorry to hear that. Is there anything I can do to help?",
  "rejected": "That's too bad. You should just get over it."
}
```

<!-- - [大規模言語モデルのデータセットまとめ](https://note.com/npaka/n/n686d987adfb1): 大規模言語モデルのデータセットまとめ [Apr 2023] -->
- Dataset example

  [🗣️](https://docs.argilla.io/)

  ### SFT Dataset

  | Category | Instruction | Context | Response |
  | --- | --- | --- | --- |
  | 0 | Open QA | How do I get rid of mosquitos in my house? | You can get rid of mosquitos in your house by ... |
  | 1 | Classification | Classify each country as "African" or "European" | Nigeria: African<br>Rwanda: African<br>Portugal: European |
  | 2 | Information Extraction | Extract the unique names of composers from the text. | To some extent, European and the US traditions... Pierre Boulez, Luigi Nono, Karlheinz Stockhausen |
  | 3 | General QA | Should investors time the market? | Timing the market is based on predictions of t... |

  ### RLHF Dataset

  | Instruction | Chosen Response | Rejected Response |
  | --- | --- | --- |
  | What is Depreciation | Depreciation is the drop in value of an asset ... | What is Depreciation – 10 Important Facts to K... |
  | What do you know about the city of Aberdeen in Scotland? | Aberdeen is a city located in the North East of Scotland. It is known for its granite architecture and its offshore oil industry. | As an AI language model, I don't have personal knowledge or experiences about Aberdeen. |
  | Describe thunderstorm season in the United States and Canada. | Thunderstorm season in the United States and Canada typically occurs during the spring and summer months, when warm, moist air collides with cooler, drier air, creating the conditions for thunderstorms to form. | Describe thunderstorm season in the United States and Canada. |
  