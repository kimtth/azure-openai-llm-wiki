## Finetuning

### **Finetuning**

#### LLM Pre-training and Post-training Paradigms [x-ref](llm.md/#large-language-models-in-2023)

#### PEFT: Parameter-Efficient Fine-Tuning ([📺](https://youtu.be/Us5ZFp16PaU)) [24 Apr 2023]

- [PEFT](https://huggingface.co/blog/peft): Parameter-Efficient Fine-Tuning. PEFT is an approach to fine tuning only a few parameters. [10 Feb 2023]
- [Scaling Down to Scale Up: A Guide to Parameter-Efficient Fine-Tuning](https://arxiv.org/abs/2303.15647): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.15647)] [28 Mar 2023]

- Category: Represent approach - Description - Pseudo Code [ref](https://speakerdeck.com/schulta) [22 Sep 2023]

  1. Adapters: Adapters - Additional Layers. Inference can be slower.

     ```python
     def transformer_with_adapter(x):
       residual = x
       x = SelfAttention(x)
       x = FFN(x) # adapter
       x = LN(x + residual)
       residual = x
       x = FFN(x) # transformer FFN
       x = FFN(x) # adapter
       x = LN(x + residual)
       return x
     ```

  1. Soft Prompts: Prompt-Tuning - Learnable text prompts. Not always desired results.

     ```python
     def soft_prompted_model(input_ids):
       x = Embed(input_ids)
       soft_prompt_embedding = SoftPromptEmbed(task_based_soft_prompt)
       x = concat([soft_prompt_embedding, x], dim=seq)
       return model(x)
     ```

  1. Selective: BitFit - Update only the bias parameters. fast but limited.

     ```python
     params = (p for n,p in model.named_parameters() if "bias" in n)
     optimizer = Optimizer(params)
     ```

  1. Reparametrization: LoRa - Low-rank decomposition. Efficient, Complex to implement.

     ```python
     def lora_linear(x):
       h = x @ W # regular linear
       h += x @ W_A @ W_B # low_rank update
       return scale * h
     ```

- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2106.09685)]: LoRA is one of PEFT technique. To represent the weight updates with two smaller matrices (called update matrices) through low-rank decomposition. [git](https://github.com/microsoft/LoRA) [17 Jun 2021]
 ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/LoRA?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [LoRA learns less and forgets less](https://arxiv.org/abs/2405.09673): Compared to full training, LoRA has less learning but better retention of original knowledge. [15 May 2024]

   <img src="../files/LoRA.png" alt="LoRA" width="390"/>

  1. [LoRA+](https://arxiv.org/abs/2402.12354): Improves LoRA’s performance and fine-tuning speed by setting different learning rates for the LoRA adapter matrices. [19 Feb 2024]
  1. [LoTR](https://arxiv.org/abs/2402.01376): Tensor decomposition for gradient update. [2 Feb 2024]
  1. [The Expressive Power of Low-Rank Adaptation](https://arxiv.org/abs/2310.17513): Theoretically analyzes the expressive power of LoRA. [26 Oct 2023]
  1. [DoRA](https://arxiv.org/abs/2402.09353): Weight-Decomposed Low-Rank Adaptation. Decomposes pre-trained weight into two components, magnitude and direction, for fine-tuning. [14 Feb 2024]
  1. LoRA Family [ref](https://towardsdatascience.com/an-overview-of-the-lora-family-515d81134725) [11 Mar 2024]
      - `LoRA` introduces low-rank matrices A and B that are trained, while the pre-trained weight matrix W is frozen.
      - `LoRA+` suggests having a much higher learning rate for B than for A.
      - `VeRA` does not train A and B, but initializes them randomly and trains new vectors d and b on top.
      - `LoRA-FA` only trains matrix B.
      - `LoRA-drop` uses the output of B*A to determine, which layers are worth to be trained at all.
      - `AdaLoRA` adapts the ranks of A and B in different layers dynamically, allowing for a higher rank in these layers, where more contribution to the model’s performance is expected.
      - `DoRA` splits the LoRA adapter into two components of magnitude and direction and allows to train them more independently.
      - `Delta-LoRA` changes the weights of W by the gradient of A*B.
  1. 5 Techniques of LoRA [ref](https://blog.dailydoseofds.com/p/5-llm-fine-tuning-techniques-explained): LoRA, LoRA-FA, VeRA, Delta-LoRA, LoRA+ [May 2024]

  </details>
- [Practical Tips for Finetuning LLMs Using LoRA (Low-Rank Adaptation)](https://magazine.sebastianraschka.com/p/practical-tips-for-finetuning-llms) [19 Nov 2023]: Best practical guide of LoRA.
  1. QLoRA saves 33% memory but increases runtime by 39%, useful if GPU memory is a constraint.
  1. Optimizer choice for LLM finetuning isn’t crucial. Adam optimizer’s memory-intensity doesn’t significantly impact LLM’s peak memory.
  1. Apply LoRA across all layers for maximum performance.
  1. Adjusting the LoRA rank is essential.
  1. Multi-epoch training on static datasets may lead to overfitting and deteriorate results.
- [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2203.02155)] [4 Mar 2022]
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.14314)]: 4-bit quantized pre-trained language model into Low Rank Adapters (LoRA). [git](https://github.com/artidoro/qlora) [23 May 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/artidoro/qlora?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [Fine-tuning a GPT - LoRA](https://dataman-ai.medium.com/fine-tune-a-gpt-lora-e9b72ad4ad3): Comprehensive guide for LoRA [doc](../files/Fine-tuning_a_GPT_LoRA.pdf) [20 Jun 2023]
- [LIMA: Less Is More for Alignment](https://arxiv.org/abs/2305.11206): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.11206)]: fine-tuned with the standard supervised loss on `only 1,000 carefully curated prompts and responses, without any reinforcement learning or human preference modeling.` LIMA demonstrates remarkably strong performance, either equivalent or strictly preferred to GPT-4 in 43% of cases. [18 May 2023]
- [How to continue pretraining an LLM on new data](https://x.com/rasbt/status/1768629533509370279): `Continued pretraining` can be as effective as `retraining on combined datasets`. [13 Mar 2024]

  Three training methods were compared:

  <img src="../files/cont-pretraining.jpg" width="400"/>

  1. Regular pretraining: A model is initialized with random weights and pretrained on dataset D1.
  2. Continued pretraining: The pretrained model from 1) is further pretrained on dataset D2.
  3. Retraining on combined dataset: A model is initialized with random weights and trained on the combined datasets D1 and D2.

  Continued pretraining can be as effective as retraining on combined datasets. Key strategies for successful continued pretraining include:

  1. Re-warming: Increasing the learning rate at the start of continued pre-training.
  2. Re-decaying: Gradually reducing the learning rate afterwards.
  3. Data Mixing: Adding a small portion (e.g., 5%) of the original pretraining data (D1) to the new dataset (D2) to prevent catastrophic forgetting.
- [x-ref](survey_ref.md/#classification-of-attention): Classification of Attention

#### **Llama Finetuning**

- A key difference between [Llama 1](https://arxiv.org/abs/2302.13971): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2302.13971)] [27 Feb 2023] and [Llama 2](https://arxiv.org/abs/2307.09288): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.09288)] [18 Jul 2023] is the architectural change of attention layer, in which Llama 2 takes advantage of Grouped Query Attention (GQA) mechanism to improve efficiency. > OSS LLM [x-ref](llm.md/#open-source-large-language-models) / Llama3 > Build an llms from scratch [x-ref](survey_ref.md/#build-an-llms-from-scratch-picogpt-and-lit-gpt) <br/>
  <img src="../files/grp-attn.png" alt="llm-grp-attn" width="400"/>
- [Multi-query attention (MQA)](https://arxiv.org/abs/2305.13245): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.13245)] [22 May 2023]
- Coding LLaMA 2 from scratch in PyTorch - KV Cache, Grouped Query Attention, Rotary PE, RMSNorm [📺](https://www.youtube.com/watch?v=oM4VmoabDAI) / [git](https://github.com/hkproj/pytorch-llama) [03 Sep 2023] <br/>
 ![GitHub Repo stars](https://img.shields.io/github/stars/hkproj/pytorch-llama?style=flat-square&label=%20&color=gray&cacheSeconds=36000)

  - KV Cache, Grouped Query Attention, Rotary PE

  <img src="../files/llama2.png" width="300" />

  - Rotary PE

  ```python
  def apply_rotary_embeddings(x: torch.Tensor, freqs_complex: torch.Tensor, device: str):
      # Separate the last dimension pairs of two values, representing the real and imaginary parts of the complex number
      # Two consecutive values will become a single complex number
      # (B, Seq_Len, H, Head_Dim) -> (B, Seq_Len, H, Head_Dim/2)
      x_complex = torch.view_as_complex(x.float().reshape(*x.shape[:-1], -1, 2))
      # Reshape the freqs_complex tensor to match the shape of the x_complex tensor. So we need to add the batch dimension and the head dimension
      # (Seq_Len, Head_Dim/2) --> (1, Seq_Len, 1, Head_Dim/2)
      freqs_complex = freqs_complex.unsqueeze(0).unsqueeze(2)
      # Multiply each complex number in the x_complex tensor by the corresponding complex number in the freqs_complex tensor
      # Which results in the rotation of the complex number as shown in the Figure 1 of the paper
      # (B, Seq_Len, H, Head_Dim/2) * (1, Seq_Len, 1, Head_Dim/2) = (B, Seq_Len, H, Head_Dim/2)
      x_rotated = x_complex * freqs_complex
      # Convert the complex number back to the real number
      # (B, Seq_Len, H, Head_Dim/2) -> (B, Seq_Len, H, Head_Dim/2, 2)
      x_out = torch.view_as_real(x_rotated)
      # (B, Seq_Len, H, Head_Dim/2, 2) -> (B, Seq_Len, H, Head_Dim)
      x_out = x_out.reshape(*x.shape)
      return x_out.type_as(x).to(device)
  ```

  - KV Cache, Grouped Query Attention

  ```python
    # Replace the entry in the cache
    self.cache_k[:batch_size, start_pos : start_pos + seq_len] = xk
    self.cache_v[:batch_size, start_pos : start_pos + seq_len] = xv

    # (B, Seq_Len_KV, H_KV, Head_Dim)
    keys = self.cache_k[:batch_size, : start_pos + seq_len]
    # (B, Seq_Len_KV, H_KV, Head_Dim)
    values = self.cache_v[:batch_size, : start_pos + seq_len]

    # Since every group of Q shares the same K and V heads, just repeat the K and V heads for every Q in the same group.

    # (B, Seq_Len_KV, H_KV, Head_Dim) --> (B, Seq_Len_KV, H_Q, Head_Dim)
    keys = repeat_kv(keys, self.n_rep)
    # (B, Seq_Len_KV, H_KV, Head_Dim) --> (B, Seq_Len_KV, H_Q, Head_Dim)
    values = repeat_kv(values, self.n_rep)
  ```

  </details>

- [Comprehensive Guide for LLaMA with RLHF](https://huggingface.co/blog/stackllama): StackLLaMA: A hands-on guide to train LLaMA with RLHF [5 Apr 2023]
- Official LLama Recipes incl. Finetuning: [git](https://github.com/facebookresearch/llama-recipes)
 ![GitHub Repo stars](https://img.shields.io/github/stars/facebookresearch/llama-recipes?style=flat-square&label=%20&color=gray&cacheSeconds=36000)

- Llama 2 ONNX [git](https://github.com/microsoft/Llama-2-Onnx) [Jul 2023]: ONNX, or Open Neural Network Exchange, is an open standard for machine learning interoperability. It allows AI developers to use models across various frameworks, tools, runtimes, and compilers.
 ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/Llama-2-Onnx?style=flat-square&label=%20&color=gray&cacheSeconds=36000)

### **RLHF (Reinforcement Learning from Human Feedback) & SFT (Supervised Fine-Tuning)**

- Machine learning technique that trains a "reward model" directly from human feedback and uses the model as a reward function to optimize an agent's policy using reinforcement learning.
- [InstructGPT: Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2203.02155)] is a model trained by OpenAI to follow instructions using human feedback. [4 Mar 2022] <br/>
  <img src="../files/rhlf.png" width="400" /> <br/>
  <img src="../files/rhlf2.png" width="400" /> <br/>
  [cite](https://docs.argilla.io/)
- Libraries: [TRL](https://huggingface.co/docs/trl/index), [trlX](https://github.com/CarperAI/trlx), [Argilla](https://docs.argilla.io/en/latest/tutorials/libraries/colab.html) <br/>
 ![GitHub Repo stars](https://img.shields.io/github/stars/CarperAI/trlx?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
  <img src="../files/TRL-readme.png" width="500" /> <br/>
  <!-- [SFTTrainer](https://huggingface.co/docs/trl/main/en/trainer#trl.SFTTrainer) from TRL -->
  TRL: from the Supervised Fine-tuning step (SFT), Reward Modeling step (RM) to the Proximal Policy Optimization (PPO) step <br/>
  <img src="../files/chip.jpg" width="400" /> <br/>
  The three steps in the process: 1. pre-training on large web-scale data, 2. supervised fine-tuning on instruction data (instruction tuning), and 3. RLHF. [ref](https://aman.ai/primers/ai/RLHF/) [ⓒ 2023]
- `Supervised Fine-Tuning (SFT)` fine-tuning a pre-trained model on a specific task or domain using labeled data. This can cause more significant shifts in the model’s behavior compared to RLHF. <br/>
  <img src="../files/rlhf-dpo.png" width="400" />
- [Reinforcement Learning from Human Feedback (RLHF)](https://arxiv.org/abs/1909.08593)) is a process of pretraining and retraining a language model using human feedback to develop a scoring algorithm that can be reapplied at scale for future training and refinement. As the algorithm is refined to match the human-provided grading, direct human feedback is no longer needed, and the language model continues learning and improving using algorithmic grading alone. [18 Sep 2019] [ref](https://huggingface.co/blog/rlhf) [9 Dec 2022]
  - `Proximal Policy Optimization (PPO)` is a reinforcement learning method using first-order optimization. It modifies the objective function to penalize large policy changes, specifically those that move the probability ratio away from 1. Aiming for TRPO (Trust Region Policy Optimization)-level performance without its complexity which requires second-order optimization.
- [Direct Preference Optimization (DPO)](https://arxiv.org/abs/2305.18290): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.18290)]: 1. RLHF can be complex because it requires fitting a reward model and performing significant hyperparameter tuning. On the other hand, DPO directly solves a classification problem on human preference data in just one stage of policy training. DPO more stable, efficient, and computationally lighter than RLHF. 2. `Your Language Model Is Secretly a Reward Model`  [29 May 2023]
  - Direct Preference Optimization (DPO) uses two models: a trained model (or policy model) and a reference model (copy of trained model). The goal is to have the trained model output higher probabilities for preferred answers and lower probabilities for rejected answers compared to the reference model.  [ref](https://towardsdatascience.com/fine-tune-a-mistral-7b-model-with-direct-preference-optimization-708042745aac): RHLF vs DPO [Jan 2, 2024] / [ref](https://pakhapoomsarapat.medium.com/forget-rlhf-because-dpo-is-what-you-actually-need-f10ce82c9b95) [1 Jul 2023]
- [ORPO (odds ratio preference optimization)](https://arxiv.org/abs/2403.07691): Monolithic Preference Optimization without Reference Model. New method that `combines supervised fine-tuning and preference alignment into one process` [git](https://github.com/xfactlab/orpo) [12 Mar 2024] [Fine-tune Llama 3 with ORPO](https://towardsdatascience.com/fine-tune-llama-3-with-orpo-56cfab2f9ada) [Apr 2024] <br/>
 ![GitHub Repo stars](https://img.shields.io/github/stars/xfactlab/orpo?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
  <img src="../files/orpo.png" width="400" />
- [Reinforcement Learning from AI Feedback (RLAF)](https://arxiv.org/abs/2309.00267): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.00267)]: Uses AI feedback to generate instructions for the model. TLDR: CoT (Chain-of-Thought, Improved), Few-shot (Not improved). Only explores the task of summarization. After training on a few thousand examples, performance is close to training on the full dataset. RLAIF vs RLHF: In many cases, the two policies produced similar summaries. [1 Sep 2023]
- OpenAI Spinning Up in Deep RL!: An educational resource to help anyone learn deep reinforcement learning. [git](https://github.com/openai/spinningup) [Nov 2018]
 ![GitHub Repo stars](https://img.shields.io/github/stars/openai/spinningup?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [A Comprehensive Survey of LLM Alignment Techniques: RLHF, RLAIF, PPO, DPO and More](https://arxiv.org/abs/2407.16216) [23 Jul 2024]
- Preference optimization techniques: [ref](https://x.com/helloiamleonie/status/1823305448650383741) [13 Aug 2024]
  - `RLHF (Reinforcement Learning from Human Feedback)`: Optimizes reward policy via objective function.
  - `DPO (Direct preference optimization)`: removes the need for a reward model. > Minimizes loss; no reward policy.
  - `IPO (Identity Preference Optimization)` : A change in the objective, which is simpler and less prone to overfitting.
  - `KTO (Kahneman-Tversky Optimization)` : Scales more data by replacing the pairs of accepted and rejected generations with a binary label.
  - `ORPO (Odds Ratio Preference Optimization)` : Combines instruction tuning and preference optimization into one training process, which is cheaper and faster.
  - `TPO (Thought Preference Optimization)`: This method generates thoughts before the final response, which are then evaluated by a Judge model for preference using Direct Preference Optimization (DPO). [14 Oct 2024]
- [SFT vs RL](https://arxiv.org/abs/2501.17161): SFT Memorizes, RL Generalizes. RL enhances generalization across text and vision, while SFT tends to memorize and overfit. [git](https://github.com/LeslieTrue/SFTvsRL) [28 Jan 2025]
- [Train your own R1 reasoning model with Unsloth (GRPO)](https://unsloth.ai/blog/r1-reasoning): Unsloth x vLLM > 20x more throughput, 50% VRAM savings. [6 Feb 2025]
- [Absolute Zero: Reinforced Self-play Reasoning with Zero Data](https://arxiv.org/abs/2505.03335): Autonomous AI systems capable of self-improvement without human-curated data, using interpreter feedback for code generation and math problem solving. [6 May 2025]

### **Model Compression for Large Language Models**

- A Survey on Model Compression for Large Language Models [ref](https://arxiv.org/abs/2308.07633) [15 Aug 2023]

#### **Quantization Techniques**

- Quantization-aware training (QAT): The model is further trained with quantization in mind after being initially trained in floating-point precision.
- Post-training quantization (PTQ): The model is quantized after it has been trained without further optimization during the quantization process.

  | Method                      | Pros                                                        | Cons                                                                                 |
  | --------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------ |
  | Post-training quantization  | Easy to use, no need to retrain the model                   | May result in accuracy loss                                                          |
  | Quantization-aware training | Can achieve higher accuracy than post-training quantization | Requires retraining the model, can be more complex to implement                      |

- bitsandbytes: 8-bit optimizers [git](https://github.com/TimDettmers/bitsandbytes) [Oct 2021]
 ![GitHub Repo stars](https://img.shields.io/github/stars/TimDettmers/bitsandbytes?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [The Era of 1-bit LLMs](https://arxiv.org/abs/2402.17764): All Large Language Models are in 1.58 Bits. BitNet b1.58, in which every single parameter (or weight) of the LLM is ternary {-1, 0, 1}. [27 Feb 2024]

#### **Pruning and Sparsification**

- Pruning: The process of removing some of the neurons or layers from a neural network. This can be done by identifying and eliminating neurons or layers that have little or no impact on the network's output.

- Sparsification: A technique used to reduce the size of large language models by removing redundant parameters.

- [Wanda Pruning](https://arxiv.org/abs/2306.11695): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2306.11695)]: A Simple and Effective Pruning Approach for Large Language Models [20 Jun 2023] [ref](https://www.linkedin.com/pulse/efficient-model-pruning-large-language-models-wandas-ayoub-kirouane)

#### **Knowledge Distillation: Reducing Model Size with Textbooks**

- phi-series: [x-ref](llm.md/#large-language-model-collection): Textbooks Are All You Need.
- [Orca 2](https://arxiv.org/abs/2311.11045): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2311.11045)]: Orca learns from rich signals from GPT 4 including explanation traces; step-by-step thought processes; and other complex instructions, guided by teacher assistance from ChatGPT. [ref](https://www.microsoft.com/en-us/research/blog/orca-2-teaching-small-language-models-how-to-reason/) [18 Nov 2023]
- Distilled Supervised Fine-Tuning (dSFT)
  1. [Zephyr 7B](https://arxiv.org/abs/2310.16944): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.16944)] Zephyr-7B-β is the second model in the series, and is a fine-tuned version of mistralai/Mistral-7B-v0.1 that was trained on on a mix of publicly available, synthetic datasets using Direct Preference Optimization (DPO). [ref](https://huggingface.co/HuggingFaceH4/zephyr-7b-beta) [25 Oct 2023]
  2. [Mistral 7B](https://arxiv.org/abs/2310.06825): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.06825)]: Outperforms Llama 2 13B on all benchmarks. Uses Grouped-query attention (GQA) for faster inference. Uses Sliding Window Attention (SWA) to handle longer sequences at smaller cost. [ref](https://mistral.ai/news/announcing-mistral-7b/) [10 Oct 2023]

#### **Memory Optimization**

- Transformer cache key-value tensors of context tokens into GPU memory to facilitate fast generation of the next token. However, these caches occupy significant GPU memory. The unpredictable nature of cache size, due to the variability in the length of each request, exacerbates the issue, resulting in significant memory fragmentation in the absence of a suitable memory management mechanism.
- To alleviate this issue, PagedAttention was proposed to store the KV cache in non-contiguous memory spaces. It partitions the KV cache of each sequence into multiple blocks, with each block containing the keys and values for a fixed number of tokens.
- [PagedAttention](https://arxiv.org/abs/2309.06180) : vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention, 24x Faster LLM Inference [doc](../files/vLLM_pagedattention.pdf). [ref](https://vllm.ai/): vllm [12 Sep 2023]

  <img src="../files/pagedattn.png" width="390">

  - PagedAttention for a prompt “the cat is sleeping in the kitchen and the dog is”. Key-Value pairs of tensors for attention computation are stored in virtual contiguous blocks mapped to non-contiguous blocks in the GPU memory.

- [TokenAttention](https://github.com/ModelTC/lightllm) an attention mechanism that manages key and value caching at the token level. [git](https://github.com/ModelTC/lightllm/blob/main/docs/TokenAttention.md) [Jul 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/ModelTC/lightllm?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [Flash Attention](https://arxiv.org/abs/2205.14135): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2205.14135)] [27 May 2022]
  - In a GPU, A thread is the smallest execution unit, and a group of threads forms a block.
  - A block executes the same kernel (function, to simplify), with threads sharing fast SRAM memory.
  - All blocks can access the shared global HBM memory.
  - First, the query (Q) and key (K) product is computed in threads and returned to HBM. Then, it's redistributed for softmax and returned to HBM.
  - Flash attention reduces these movements by caching results in SRAM.
  - `Tiling` splits attention computation into memory-efficient blocks, while `recomputation` saves memory by recalculating intermediates during backprop. [📺](https://www.youtube.com/live/gMOAud7hZg4?si=dx637BQV-4Duu3uY)
  - [FlashAttention-2](https://arxiv.org/abs/2307.08691): [[cnt](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2307.08691)] [17 Jul 2023]: An method that reorders the attention computation and leverages classical techniques (tiling, recomputation). Instead of storing each intermediate result, use kernel fusion and run every operation in a single kernel in order to avoid memory read/write overhead. [git](https://github.com/Dao-AILab/flash-attention) -> Compared to a standard attention implementation in PyTorch, FlashAttention-2 can be up to 9x faster
 ![GitHub Repo stars](https://img.shields.io/github/stars/Dao-AILab/flash-attention?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
  - [FlashAttention-3](https://arxiv.org/abs/2407.08608) [11 Jul 2024]  
- [CPU vs GPU vs TPU](https://newsletter.theaiedge.io/p/how-to-scale-model-training): The threads are grouped into thread blocks. Each of the thread blocks has access to a fast shared memory (SRAM). All the thread blocks can also share a large global memory. High-bandwidth memories (HBM). `HBM Bandwidth: 1.5-2.0TB/s vs SRAM Bandwidth: 19TB/s ~ 10x HBM` [27 May 2024]

#### **Other techniques and LLM patterns**

- [LLM patterns](https://eugeneyan.com/writing/llm-patterns/): 🏆From data to user, from defensive to offensive [doc](../files/llm-patterns-og.png)
- [What We’ve Learned From A Year of Building with LLMs](https://applied-llms.org/):💡A practical guide to building successful LLM products, covering the tactical, operational, and strategic.  [8 June 2024]
- [Large Transformer Model Inference Optimization](https://lilianweng.github.io/posts/2023-01-10-inference-optimization/): Besides the increasing size of SoTA models, there are two main factors contributing to the inference challenge ... [10 Jan 2023]
- [Mixture of experts models](https://mistral.ai/news/mixtral-of-experts/): Mixtral 8x7B: Sparse mixture of experts models (SMoE) [magnet](https://x.com/MistralAI/status/1706877320844509405?s=20) [Dec 2023]
  - [Huggingface Mixture of Experts Explained](https://huggingface.co/blog/moe): Mixture of Experts, or MoEs for short [Dec 2023]
  - [A Visual Guide to Mixture of Experts (MoE)](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mixture-of-experts) [08 Oct 2024]
  - [makeMoE](https://github.com/AviSoori1x/makeMoE): From scratch implementation of a sparse mixture of experts ![GitHub Repo stars](https://img.shields.io/github/stars/AviSoori1x/makeMoE?style=flat-square&label=%20&color=gray&cacheSeconds=36000) [Jan 2024]
  - [The Sparsely-Gated Mixture-of-Experts Layer](https://arxiv.org/abs/1701.06538): Introduced sparse expert gating to scale models efficiently without increasing compute cost. [23 Jan 2017]
  - [Switch Transformers](https://arxiv.org/abs/2101.03961): Used a single expert per token to simplify routing, enabling fast, scalable transformer models. `expert capacity = (total tokens / num experts) * capacity factor` [11 Jan 2021]
  - [ST-MoE (Stable Transformer MoE)](https://arxiv.org/abs/2202.08906): By stabilizing the training process, ST-MoE enables more reliable and scalable deep MoE architectures. `z-loss aims to regularize the logits z before passing into the softmax` [17 Feb 2022] 
- [Simplifying Transformer Blocks](https://arxiv.org/abs/2311.01906): Simplifie Transformer. Removed several block components, including skip connections, projection/value matrices, sequential sub-blocks and normalisation layers without loss of training speed. [3 Nov 2023]
- [Model merging](https://towardsdatascience.com/merge-large-language-models-with-mergekit-2118fb392b54): : A technique that combines two or more large language models (LLMs) into a single model, using methods such as SLERP, TIES, DARE, and passthrough. [Jan 2024] [git](https://github.com/cg123/mergekit): mergekit
 ![GitHub Repo stars](https://img.shields.io/github/stars/cg123/mergekit?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
  | Method | Pros | Cons |
  | --- | --- | --- |
  | SLERP | Preserves geometric properties, popular method | Can only merge two models, may decrease magnitude |
  | TIES | Can merge multiple models, eliminates redundant parameters | Requires a base model, may discard useful parameters |
  | DARE | Reduces overfitting, keeps expectations unchanged | May introduce noise, may not work well with large differences |
- [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752) [1 Dec 2023] [git](https://github.com/state-spaces/mamba): 1. Structured State Space (S4) - Class of sequence models, encompassing traits from RNNs, CNNs, and classical state space models. 2. Hardware-aware (Optimized for GPU) 3. Integrating selective SSMs and eliminating attention and MLP blocks [ref](https://www.unite.ai/mamba-redefining-sequence-modeling-and-outforming-transformers-architecture/) / A Visual Guide to Mamba and State Space Models [ref](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-mamba-and-state) [19 FEB 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/state-spaces/mamba?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
  - [Mamba-2](https://arxiv.org/abs/2405.21060): 2-8X faster [31 May 2024]
- [Sakana.ai: Evolutionary Optimization of Model Merging Recipes.](https://arxiv.org/abs/2403.13187): A Method to Combine 500,000 OSS Models. [git](https://github.com/SakanaAI/evolutionary-model-merge) [19 Mar 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/SakanaAI/evolutionary-model-merge?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [Mixture-of-Depths](https://arxiv.org/abs/2404.02258): All tokens should not require the same effort to compute. The idea is to make token passage through a block optional. Each block selects the top-k tokens for processing, and the rest skip it. [ref](https://www.linkedin.com/embed/feed/update/urn:li:share:7181996416213372930) [2 Apr 2024]
- [Kolmogorov-Arnold Networks (KANs)](https://arxiv.org/abs/2404.19756): KANs use activation functions on connections instead of nodes like Multi-Layer Perceptrons (MLPs) do. Each weight in KANs is replaced by a learnable 1D spline function. KANs’ nodes simply sum incoming signals without applying any non-linearities. [git](https://github.com/KindXiaoming/pykan) [30 Apr 2024] / [ref](https://www.dailydoseofds.com/a-beginner-friendly-introduction-to-kolmogorov-arnold-networks-kan/): A Beginner-friendly Introduction to Kolmogorov Arnold Networks (KAN) [19 May 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/KindXiaoming/pykan?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [Better & Faster Large Language Models via Multi-token Prediction](https://arxiv.org/abs/2404.19737): Suggest that training language models to predict multiple future tokens at once [30 Apr 2024]
- [Lamini Memory Tuning](https://github.com/lamini-ai/Lamini-Memory-Tuning): Mixture of Millions of Memory Experts (MoME). 95% LLM Accuracy, 10x Fewer Hallucinations. [ref](https://www.lamini.ai/blog/lamini-memory-tuning) [Jun 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/lamini-ai/Lamini-Memory-Tuning?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [Scaling Synthetic Data Creation with 1,000,000,000 Personas](https://arxiv.org/abs/2406.20094) A persona-driven data synthesis methodology using Text-to-Persona and Persona-to-Persona. [28 Jun 2024]
- [RouteLLM](https://github.com/lm-sys/RouteLLM): a framework for serving and evaluating LLM routers. [Jun 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/lm-sys/RouteLLM?style=flat-square&label=%20&color=gray&cacheSeconds=36000)
- [KAN or MLP: A Fairer Comparison](https://arxiv.org/abs/2407.16674): In machine learning, computer vision, audio processing, natural language processing, and symbolic formula representation (except for symbolic formula representation tasks), MLP generally outperforms KAN. [23 Jul 2024]
- [Differential Transformer](https://arxiv.org/abs/2410.05258): Amplifies attention to the relevant context while minimizing noise using two separate softmax attention mechanisms. [7 Oct 2024]
- [Large Concept Models](https://arxiv.org/abs/2412.08821): Focusing on high-level sentence (concept) level rather than tokens. using SONAR for sentence embedding space. [11 Dec 2024]
- [Large Language Diffusion Models](https://arxiv.org/abs/2502.09992): LLaDA's core is a mask predictor, which uses controlled noise to help models learn to predict missing information from context. [ref](https://ml-gsai.github.io/LLaDA-demo/) [14 Feb 2025]
