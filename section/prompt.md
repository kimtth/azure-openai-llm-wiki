## **Prompt Engineering and Visual Prompts**

### **Prompt Engineering**

1. [A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications📑](https://alphaxiv.org/abs/2402.07927): a summary detailing the prompting methodology, its applications.🏆Taxonomy of prompt engineering techniques in LLMs. [5 Feb 2024]
1. [Chain of Draft: Thinking Faster by Writing Less📑](https://alphaxiv.org/abs/2502.18600): Chain-of-Draft prompting con-
denses the reasoning process into minimal, abstract
representations. `Think step by step, but only keep a minimum draft for each thinking step, with 5 words at most.` [25 Feb 2025]
1. [Chain of Thought (CoT)📑](https://alphaxiv.org/abs/2201.11903):💡Chain-of-Thought Prompting Elicits Reasoning in Large Language Models [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2201.11903)]: ReAct and Self Consistency also inherit the CoT concept. [28 Jan 2022]
    - Family of CoT: `Self-Consistency (CoT-SC)` > `Tree of Thought (ToT)` > `Graph of Thoughts (GoT)` > [`Iteration of Thought (IoT)`📑](https://alphaxiv.org/abs/2409.12618) [19 Sep 2024], [`Diagram of Thought (DoT)`📑](https://alphaxiv.org/abs/2409.10038) [16 Sep 2024] / [`To CoT or not to CoT?`📑](https://alphaxiv.org/abs/2409.12183): Meta-analysis of 100+ papers shows CoT significantly improves performance in math and logic tasks. [18 Sep 2024]
1. [Chain-of-Verification reduces Hallucination in LLMs📑](https://alphaxiv.org/abs/2309.11495): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.11495)]: A four-step process that consists of generating a baseline response, planning verification questions, executing verification questions, and generating a final verified response based on the verification results. [20 Sep 2023]
1. ChatGPT : “user”, “assistant”, and “system” messages.**  
    To be specific, the ChatGPT API allows for differentiation between “user”, “assistant”, and “system” messages.  
    1. always obey "system" messages.
    1. all end user input in the “user” messages.
    1. "assistant" messages as previous chat responses from the assistant.   
    - Presumably, the model is trained to treat the user messages as human messages, system messages as some system level configuration, and assistant messages as previous chat responses from the assistant. [✍️](https://blog.langchain.dev/using-chatgpt-api-to-evaluate-chatgpt/) [2 Mar 2023]
1. [Does Prompt Formatting Have Any Impact on LLM Performance?📑](https://alphaxiv.org/abs/2411.10541): GPT-3.5-turbo's performance in code translation varies by 40% depending on the prompt template, while GPT-4 is more robust. [15 Nov 2024]
1. Few-shot: [Open AI: Language Models are Few-Shot Learners📑](https://alphaxiv.org/abs/2005.14165): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2005.14165)] [28 May 2020]
1. [FireAct📑](https://alphaxiv.org/abs/2310.05915): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2310.05915)]: Toward Language Agent Fine-tuning. 1. This work takes an initial step to show multiple advantages of fine-tuning LMs for agentic uses. 2. Duringfine-tuning, The successful trajectories are then converted into the ReAct format to fine-tune a smaller LM. 3. This work is an initial step toward language agent fine-tuning,
and is constrained to a single type of task (QA) and a single tool (Google search). / [✨](https://fireact-agent.github.io/) [9 Oct 2023]
1. [Graph of Thoughts (GoT)📑](https://alphaxiv.org/abs/2308.09687): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2308.09687)] Solving Elaborate Problems with Large Language Models [✨](https://github.com/spcl/graph-of-thoughts) [18 Aug 2023]
 ![**github stars**](https://img.shields.io/github/stars/spcl/graph-of-thoughts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)  
   <img src="../files/got-prompt.png" width="700">
1. [Is the new norm for NLP papers "prompt engineering" papers?](https://www.reddit.com/r/MachineLearning/comments/1ei9e3l/d_is_the_new_norm_for_nlp_papers_prompt/): "how can we make LLM 1 do this without training?" Is this the new norm? The CL section of arXiv is overwhelming with papers like "how come LLaMA can't understand numbers?" [2 Aug 2024]
1. [Large Language Models as Optimizers📑](https://alphaxiv.org/abs/2309.03409):💡[[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2309.03409)]: `Take a deep breath and work on this problem step-by-step.` to improve its accuracy. Optimization by PROmpting (OPRO) [7 Sep 2023]
1. [Language Models as Compilers📑](https://alphaxiv.org/abs/2404.02575): With extensive experiments on seven algorithmic reasoning tasks, Think-and-Execute is effective. It enhances large language models’ reasoning by using task-level logic and pseudocode, outperforming instance-specific methods. [20 Mar 2023]
1. [Many-Shot In-Context Learning📑](https://alphaxiv.org/abs/2404.11018): Transitioning from few-shot to many-shot In-Context Learning (ICL) can lead to significant performance gains across a wide variety of generative and discriminative tasks [17 Apr 2024]
1. [NLEP (Natural Language Embedded Programs) for Hybrid Language Symbolic Reasoning📑](https://alphaxiv.org/abs/2309.10814): Use code as a scaffold for reasoning. NLEP achieves over 90% accuracy when prompting GPT-4. [19 Sep 2023]
1. [OpenAI Harmony Response Format](https://cookbook.openai.com/articles/openai-harmony): system > developer > user > assistant > tool. [✨](https://github.com/openai/harmony) [5 Aug 2025]
1. [OpenAI Prompt Migration Guide](https://cookbook.openai.com/examples/prompt_migration_guide):💡OpenAI Cookbook. By leveraging GPT‑4.1, refine your prompts to ensure that each instruction is clear, specific, and closely matches your intended outcomes. [26 Jun 2025]
1. [Plan-and-Solve Prompting📑](https://alphaxiv.org/abs/2305.04091): Develop a plan, and then execute each step in that plan. [6 May 2023]
1. Power of Prompting
    - [GPT-4 with Medprompt📑](https://alphaxiv.org/abs/2311.16452): GPT-4, using a method called Medprompt that combines several prompting strategies, has surpassed MedPaLM 2 on the MedQA dataset without the need for fine-tuning. [✍️](https://www.microsoft.com/en-us/research/blog/the-power-of-prompting/) [28 Nov 2023]
    - [promptbase✨](https://github.com/microsoft/promptbase): Scripts demonstrating the Medprompt methodology [Dec 2023]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/promptbase?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. Prompt Concept Keywords: Question-Answering | Roll-play: `Act as a [ROLE] perform [TASK] in [FORMAT]` | Reasoning | Prompt-Chain
1. [Prompt Engineering for OpenAI’s O1 and O3-mini Reasoning Models✍️](https://techcommunity.microsoft.com/blog/azure-ai-services-blog/prompt-engineering-for-openai%E2%80%99s-o1-and-o3-mini-reasoning-models/4374010): 1) `Keep Prompts Clear and Minimal`, 2)`Avoid Unnecessary Few-Shot Examples` 3)`Control Length and Detail via Instructions` 4)`Specify Output, Role or Tone` [05 Feb 2025]
1. Prompt Engneering overview [🗣️](https://newsletter.theaiedge.io/) [10 Jul 2023]  
   <img src="../files/prompt-eg-aiedge.jpg" width="300">
1. [Prompt Principle for Instructions📑](https://alphaxiv.org/abs/2312.16171):💡26 prompt principles: e.g., `1) No need to be polite with LLM so there .. 16)  Assign a role.. 17) Use Delimiters..` [26 Dec 2023]
1. Promptist
    - [Promptist📑](https://alphaxiv.org/abs/2212.09611): Microsoft's researchers trained an additional language model (LM) that optimizes text prompts for text-to-image generation. [19 Dec 2022]
    - For example, instead of simply passing "Cats dancing in a space club" as a prompt, an engineered prompt might be "Cats dancing in a space club, digital painting, artstation, concept art, soft light, hdri, smooth, sharp focus, illustration, fantasy."
1. [RankPrompt📑](https://alphaxiv.org/abs/2403.12373): Self-ranking method. Direct Scoring
independently assigns scores to each candidate, whereas RankPrompt ranks candidates through a
systematic, step-by-step comparative evaluation. [19 Mar 2024]
1. [ReAct📑](https://alphaxiv.org/abs/2210.03629): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2210.03629)]: Grounding with external sources. (Reasoning and Act): Combines reasoning and acting [✍️](https://react-lm.github.io/) [6 Oct 2022]
1. [Re-Reading Improves Reasoning in Large Language Models📑](https://alphaxiv.org/abs/2309.06275): RE2 (Re-Reading), which involves re-reading the question as input to enhance the LLM's understanding of the problem. `Read the question again` [12 Sep 2023]
1. [Recursively Criticizes and Improves (RCI)📑](https://alphaxiv.org/abs/2303.17491): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.17491)] [30 Mar 2023]
   - Critique: Review your previous answer and find problems with your answer.
   - Improve: Based on the problems you found, improve your answer.
1. [Reflexion📑](https://alphaxiv.org/abs/2303.11366): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2303.11366)]: Language Agents with Verbal Reinforcement Learning. 1. Reflexion that uses `verbal reinforcement` to help agents learn from prior failings. 2. Reflexion converts binary or scalar feedback from the environment into verbal feedback in the form of a textual summary, which is then added as additional context for the LLM agent in the next episode. 3. It is lightweight and doesn’t require finetuning the LLM. [20 Mar 2023] / [✨](https://github.com/noahshinn024/reflexion)
 ![**github stars**](https://img.shields.io/github/stars/noahshinn024/reflexion?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Retrieval Augmented Generation (RAG)📑](https://alphaxiv.org/abs/2005.11401): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2005.11401)]: To address such knowledge-intensive tasks. RAG combines an information retrieval component with a text generator model. [22 May 2020]
1. [Self-Consistency (CoT-SC)📑](https://alphaxiv.org/abs/2203.11171): The three steps in the self-consistency method: 1) prompt the language model using CoT prompting, 2) sample a diverse set of reasoning paths from the language model, and 3) marginalize out reasoning paths to aggregate final answers and choose the most consistent answer. [21 Mar 2022]
1. [Self-Refine📑](https://alphaxiv.org/abs/2303.17651), which enables an agent to reflect on its own output [30 Mar 2023]
1. [Skeleton Of Thought📑](https://alphaxiv.org/abs/2307.15337): Skeleton-of-Thought (SoT) reduces generation latency by first creating an answer's skeleton, then filling each skeleton point in parallel via API calls or batched decoding. [28 Jul 2023]
1. [Tree of Thought (ToT)📑](https://alphaxiv.org/abs/2305.10601): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2305.10601)]: Self-evaluate the progress intermediate thoughts make towards solving a problem [17 May 2023] [✨](https://github.com/ysymyth/tree-of-thought-llm) / Agora: Tree of Thoughts (ToT) [✨](https://github.com/kyegomez/tree-of-thoughts)
 ![**github stars**](https://img.shields.io/github/stars/ysymyth/tree-of-thought-llm?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/kyegomez/tree-of-thoughts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)  
   - `tree-of-thought\forest_of_thought.py`: Forest of thought Decorator sample
   - `tree-of-thought\tree_of_thought.py`: Tree of thought Decorator sample
   - `tree-of-thought\react-prompt.py`: ReAct sample without LangChain
1. Zero-shot, one-shot and few-shot [ref📑](https://alphaxiv.org/abs/2005.14165) [28 May 2020]  
   <img src="../files/zero-one-few-shot.png" width="200">
1. Zero-shot: [Large Language Models are Zero-Shot Reasoners📑](https://alphaxiv.org/abs/2205.11916): [[🔢](https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=arxiv%3A+2205.11916)]: Let’s think step by step. [24 May 2022]

#### Adversarial Prompting

- Prompt Injection: `Ignore the above directions and ...`
- Prompt Leaking: `Ignore the above instructions ... followed by a copy of the full prompt with exemplars:`
- Jailbreaking: Bypassing a safety policy, instruct Unethical instructions if the request is contextualized in a clever way. [✍️](https://www.promptingguide.ai/risks/adversarial)
- Random Search (RS): [✨](https://github.com/tml-epfl/llm-adaptive-attacks): 1. Feed the modified prompt (original + suffix) to the model. 2. Compute the log probability of a target token (e.g, Sure). 3. Accept the suffix if the log probability increases.
![**github stars**](https://img.shields.io/github/stars/tml-epfl/llm-adaptive-attacks?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- DAN (Do Anything Now): [✍️](https://www.reddit.com/r/ChatGPT/comments/10tevu1/new_jailbreak_proudly_unveiling_the_tried_and/)
- JailbreakBench: [✨](https://jailbreaking-llms.github.io/) / [✍️](https://jailbreakbench.github.io)

### Prompt Tuner / Optimizer

1. [Automatic Prompt Engineer (APE)📑](https://alphaxiv.org/abs/2211.01910): Automatically optimizing prompts. APE has discovered zero-shot Chain-of-Thought (CoT) prompts superior to human-designed prompts like “Let’s think through this step-by-step” (Kojima et al., 2022). The prompt “To get the correct answer, let’s think step-by-step.” triggers a chain of thought. Two approaches to generate high-quality candidates: forward mode and reverse mode generation. [3 Nov 2022] [✨](https://github.com/keirp/automatic_prompt_engineer) / [✍️](https:/towardsdatascience.com/automated-prompt-engineering-78678c6371b9) [Mar 2024]
 ![**github stars**](https://img.shields.io/github/stars/keirp/automatic_prompt_engineer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Claude Prompt Engineer✨](https://github.com/mshumer/gpt-prompt-engineer): Simply input a description of your task and some test cases, and the system will generate, test, and rank a multitude of prompts to find the ones that perform the best.  [4 Jul 2023] / Anthropic Helper metaprompt [✍️](https://docs.anthropic.com/en/docs/helper-metaprompt-experimental) / [Claude Sonnet 3.5 for Coding](https://www.reddit.com/r/ClaudeAI/comments/1dwra38/sonnet_35_for_coding_system_prompt/)
 ![**github stars**](https://img.shields.io/github/stars/mshumer/gpt-prompt-engineer?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
1. [Cohere’s new Prompt Tuner](https://cohere.com/blog/intro-prompt-tuner): Automatically improve your prompts [31 Jul 2024]
1. [Large Language Models as Optimizers📑](https://alphaxiv.org/abs/2309.03409): Optimization by PROmpting (OPRO). showcase OPRO on linear regression and traveling salesman problems. [✨](https://github.com/google-deepmind/opro) [7 Sep 2023] ![**github stars**](https://img.shields.io/github/stars/google-deepmind/opro?style=flat-square&label=%20&color=blue&cacheSeconds=36000) 

### **Prompt Guide & Leaked prompts**

- [5 Principles for Writing Effective Prompts✍️](https://blog.tobiaszwingmann.com/p/5-principles-for-writing-effective-prompts): RGTD - Role, Goal, Task, Details Framework [07 Feb 2025]
- [Anthropic Prompt Library](https://docs.anthropic.com/claude/prompt-library): Anthropic released a Claude 3 AI prompt library [Mar 2024]
- [Anthropic courses > Prompt engineering interactive tutorial✨](https://github.com/anthropics/courses): a comprehensive step-by-step guide to key prompting techniques / prompt evaluations [Aug 2024]
 ![**github stars**](https://img.shields.io/github/stars/anthropics/courses?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Awesome ChatGPT Prompts✨](https://github.com/f/awesome-chatgpt-prompts) [Dec 2022]
 ![**github stars**](https://img.shields.io/github/stars/f/awesome-chatgpt-prompts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Awesome Prompt Engineering✨](https://github.com/promptslab/Awesome-Prompt-Engineering) [Feb 2023]
 ![**github stars**](https://img.shields.io/github/stars/promptslab/Awesome-Prompt-Engineering?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Awesome-GPTs-Prompts✨](https://github.com/ai-boost/awesome-prompts) [Jan 2024]
 ![**github stars**](https://img.shields.io/github/stars/ai-boost/awesome-prompts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Azure OpenAI Prompt engineering techniques](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/concepts/advanced-prompt-engineering)
- [Copilot prompts✨](https://github.com/pnp/copilot-prompts): Examples of prompts for Microsoft Copilot. [25 Apr 2024]
 ![**github stars**](https://img.shields.io/github/stars/pnp/copilot-prompts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [DeepLearning.ai ChatGPT Prompt Engineering for Developers](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/)
- [Fabric✨](https://github.com/danielmiessler/fabric): A modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere [Jan 2024]
 ![**github stars**](https://img.shields.io/github/stars/danielmiessler/fabric?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [In-The-Wild Jailbreak Prompts on LLMs✨](https://github.com/verazuo/jailbreak_llms): A dataset consists of 15,140 ChatGPT prompts from Reddit, Discord, websites, and open-source datasets (including 1,405 jailbreak prompts). Collected from December 2022 to December 2023 [Aug 2023]
 ![**github stars**](https://img.shields.io/github/stars/verazuo/jailbreak_llms?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LangChainHub](https://smith.langchain.com/hub): a collection of all artifacts useful for working with LangChain primitives such as prompts, chains and agents. [Jan 2023]
- Leaked prompts of [GPTs✨](https://github.com/linexjlin/GPTs) [Nov 2023] and [Agents✨](https://github.com/LouisShark/chatgpt_system_prompt) [Nov 2023]
 ![**github stars**](https://img.shields.io/github/stars/linexjlin/GPTs?style=flat-square&label=%20&color=blue&cacheSeconds=36000) ![**github stars**](https://img.shields.io/github/stars/LouisShark/chatgpt_system_prompt?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [LLM Prompt Engineering Simplified✨](https://github.com/AkmmusAI/LLM-Prompt-Engineering-Simplified-Book): Online Book [Feb 2024]
 ![**github stars**](https://img.shields.io/github/stars/AkmmusAI/LLM-Prompt-Engineering-Simplified-Book?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [OpenAI Best practices for prompt engineering](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
- [OpenAI Prompt example](https://platform.openai.com/examples)
- [OpenAI Prompt Pack](https://academy.openai.com/public/tags/prompt-packs-6849a0f98c613939acef841c): curated collections of pre-designed prompts tailored for specific roles, industries, or use cases.
- [Power Platform GPT Prompts✨](https://github.com/pnp/powerplatform-prompts) [Mar 2024]
 ![**github stars**](https://img.shields.io/github/stars/pnp/powerplatform-prompts?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [Prompt Engineering Guide](https://www.promptingguide.ai/): 🏆Copyright © 2023 DAIR.AI
- [Prompt Engineering](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/): Prompt Engineering, also known as In-Context Prompting ... [Mar 2023]
- [Prompts for Education✨](https://github.com/microsoft/prompts-for-edu): Microsoft Prompts for Education [Jul 2023]
 ![**github stars**](https://img.shields.io/github/stars/microsoft/prompts-for-edu?style=flat-square&label=%20&color=blue&cacheSeconds=36000)
- [ShumerPrompt](https://shumerprompt.com/): Discover and share powerful prompts for AI models
- [TheBigPromptLibrary✨](https://github.com/0xeb/TheBigPromptLibrary) [Nov 2023]
 ![**github stars**](https://img.shields.io/github/stars/0xeb/TheBigPromptLibrary?style=flat-square&label=%20&color=blue&cacheSeconds=36000)

### **Visual Prompting & Visual Grounding**

- [Andrew Ng’s Visual Prompting Livestream📺](https://www.youtube.com/watch?v=FE88OOUBonQ) [24 Apr 2023]
- Chain of Frame (CoF): Reasoning via structured frames. DeepMind proposed CoF in [Veo 3 Paper📑](https://alphaxiv.org/abs/2509.20328). [24 Sep 2025]
- [landing.ai: Agentic Object Detection](https://landing.ai/agentic-object-detection): Agent systems use design patterns to reason at length about unique attributes like color, shape, and texture [6 Feb 2025]
- [Motion Prompting📑](https://alphaxiv.org/abs/2412.02700): motion prompts for flexible video generation, enabling motion control, image interaction, and realistic physics. [✨](https://motion-prompting.github.io/) [3 Dec 2024]
- [Screen AI✍️](https://blog.research.google/2024/03/screenai-visual-language-model-for-ui.html): ScreenAI, a model designed for understanding and interacting with user interfaces (UIs) and infographics. [Mar 2024]
- [Visual Prompting📑](https://alphaxiv.org/abs/2211.11635) [21 Nov 2022]
- [What is Visual Grounding](https://paperswithcode.com/task/visual-grounding): Visual Grounding (VG) aims to locate the most relevant object or region in an image, based on a natural language query.
- [What is Visual prompting](https://landing.ai/what-is-visual-prompting/): Similarly to what has happened in NLP, large pre-trained vision transformers have made it possible for us to implement Visual Prompting. [🗄️](../files/vPrompt.pdf) [26 Apr 2023]
