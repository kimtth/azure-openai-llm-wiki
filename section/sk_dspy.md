## **Section 3** : Microsoft Semantic Kernel and Stanford NLP DSPy

### **Semantic Kernel**

- Microsoft LangChain Library supports C# and Python and offers several features, some of which are still in development and may be unclear on how to implement. However, it is simple, stable, and faster than Python-based open-source software. The features listed on the link include: [Semantic Kernel Feature Matrix](https://learn.microsoft.com/en-us/semantic-kernel/get-started/supported-languages) / doc:[ref](https://learn.microsoft.com/en-us/semantic-kernel) / blog:[ref](https://devblogs.microsoft.com/semantic-kernel/) / [git](https://github.com/microsoft/semantic-kernel) [Feb 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/semantic-kernel?style=flat-square&label=%20&color=gray)
- .NET Semantic Kernel SDK: 1. Renamed packages and classes that used the term “Skill” to now use “Plugin”. 2. OpenAI specific in Semantic Kernel core to be AI service agnostic 3. Consolidated our planner implementations into a single package [ref](https://devblogs.microsoft.com/semantic-kernel/introducing-the-v1-0-0-beta1-for-the-net-semantic-kernel-sdk/) [10 Oct 2023]
- Road to v1.0 for the Python Semantic Kernel SDK [ref](https://devblogs.microsoft.com/semantic-kernel/road-to-v1-0-for-the-python-semantic-kernel-sdk/) [23 Jan 2024] [backlog](https://github.com/orgs/microsoft/projects/866/views/3?sliceBy%5Bvalue%5D=python)
- Agent Framework: A module for AI agents, and agentic patterns / Process Framework: A module for creating a structured sequence of activities or tasks. [Oct 2024]

<!-- <img src="../files/mind-and-body-of-semantic-kernel.png" alt="sk" width="130"/> -->
<!-- <img src="../files/sk-flow.png" alt="sk" width="500"/> -->

### **Micro-orchestration**

- Micro-orchestration in LLM pipelines is the detailed management of LLM interactions, focusing on data flow within tasks.
- e.g., [Semantic Kernel](https://aka.ms/sk/repo), [LangChain](https://www.langchain.com/), [LlamaIndex](https://www.llamaindex.ai/), [Haystack](https://haystack.deepset.ai/), and [AdalFlow](https://github.com/SylphAI-Inc/AdalFlow).
 ![GitHub Repo stars](https://img.shields.io/github/stars/SylphAI-Inc/AdalFlow?style=flat-square&label=%20&color=gray)

#### **Code Recipes**

- Semantic Kernel sample application:💡[Chat Copilot](https://github.com/microsoft/chat-copilot) [Apr 2023] / [Virtual Customer Success Manager (VCSM)](https://github.com/jvargh/VCSM) [Jul 2024] / [Project Micronaire](https://devblogs.microsoft.com/semantic-kernel/microsoft-hackathon-project-micronaire-using-semantic-kernel/): A Semantic Kernel RAG Evaluation Pipeline [git](https://github.com/microsoft/micronaire) [3 Oct 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/chat-copilot?style=flat-square&label=%20&color=gray) ![GitHub Repo stars](https://img.shields.io/github/stars/jvargh/VCSM?style=flat-square&label=%20&color=gray) ![GitHub Repo stars](https://img.shields.io/github/stars/microsoft/micronaire?style=flat-square&label=%20&color=gray)
- Semantic Kernel Recipes: A collection of C# notebooks [git](https://github.com/johnmaeda/SK-Recipes) [Mar 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/johnmaeda/SK-Recipes?style=flat-square&label=%20&color=gray)
- Deploy Semantic Kernel with Bot Framework [ref](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/deploy-semantic-kernel-with-bot-framework/ba-p/3928101) [git](https://github.com/Azure/semantic-kernel-bot-in-a-box) [26 Oct 2023]
 ![GitHub Repo stars](https://img.shields.io/github/stars/Azure/semantic-kernel-bot-in-a-box?style=flat-square&label=%20&color=gray)
- Semantic Kernel-Powered OpenAI Plugin Development Lifecycle [ref](https://techcommunity.microsoft.com/t5/azure-developer-community-blog/semantic-kernel-powered-openai-plugin-development-lifecycle/ba-p/3967751) [30 Oct 2023]
- SemanticKernel Implementation sample to overcome Token limits of Open AI model. [ref](https://zenn.dev/microsoft/articles/semantic-kernel-10) [06 May 2023]
- [Learning Paths for Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/learning-paths-for-semantic-kernel/) [28 Mar 2024]
- [A Pythonista’s Intro to Semantic Kernel](https://towardsdatascience.com/a-pythonistas-intro-to-semantic-kernel-af5a1a39564d) [3 Sep 2023]
- [Step-by-Step Guide to Building a Powerful AI Monitoring Dashboard with Semantic Kernel and Azure Monitor](https://devblogs.microsoft.com/semantic-kernel/step-by-step-guide-to-building-a-powerful-ai-monitoring-dashboard-with-semantic-kernel-and-azure-monitor/): Step-by-step guide to building an AI monitoring dashboard using Semantic Kernel and Azure Monitor to track token usage and custom metrics. [23 Aug 2024]

#### **Semantic Kernel Planner [deprecated]**

- Semantic Kernel Planner [ref](https://devblogs.microsoft.com/semantic-kernel/semantic-kernel-planners-actionplanner/) [24 Jul 2023]

  <img src="../files/sk-evolution_of_planners.jpg" alt="sk-plan" width="300"/>

- Is Semantic Kernel Planner the same as LangChain agents?

  > Planner in SK is not the same as Agents in LangChain. [cite](https://github.com/microsoft/semantic-kernel/discussions/1326) [11 May 2023]

  > Agents in LangChain use recursive calls to the LLM to decide the next step to take based on the current state.
  > The two planner implementations in SK are not self-correcting.
  > Sequential planner tries to produce all the steps at the very beginning, so it is unable to handle unexpected errors.
  > Action planner only chooses one tool to satisfy the goal

- Stepwise Planner released. The Stepwise Planner features the "CreateScratchPad" function, acting as a 'Scratch Pad' to aggregate goal-oriented steps. [16 Aug 2023]

- Gen-4 and Gen-5 planners: 1. Gen-4: Generate multi-step plans with the [Handlebars](https://handlebarsjs.com/) 2. Gen-5: Stepwise Planner supports Function Calling. [ref](https://devblogs.microsoft.com/semantic-kernel/semantic-kernels-ignite-release-beta8-for-the-net-sdk/) [16 Nov 2023]

- Use function calling for most tasks; it's more powerful and easier. `Stepwise and Handlebars planners will be deprecated` [ref](https://learn.microsoft.com/en-us/semantic-kernel/concepts/planning) [Jun 2024] 

- [The future of Planners in Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/the-future-of-planners-in-semantic-kernel/) [23 July 2024]

#### **Semantic Function**

- Semantic Function - expressed in natural language in a text file "_skprompt.txt_" using SK's
[Prompt Template language](https://github.com/microsoft/semantic-kernel/blob/main/docs/PROMPT_TEMPLATE_LANGUAGE.md).
Each semantic function is defined by a unique prompt template file, developed using modern prompt engineering techniques. [cite](https://github.com/microsoft/semantic-kernel/blob/main/docs/GLOSSARY.md)

- Prompt Template language Key takeaways

```bash
1. Variables : use the {{$variableName}} syntax : Hello {{$name}}, welcome to Semantic Kernel!
2. Function calls: use the {{namespace.functionName}} syntax : The weather today is {{weather.getForecast}}.
3. Function parameters: {{namespace.functionName $varName}} and {{namespace.functionName "value"}} syntax
   : The weather today in {{$city}} is {{weather.getForecast $city}}.
4. Prompts needing double curly braces :
   {{ "{{" }} and {{ "}}" }} are special SK sequences.
5. Values that include quotes, and escaping :

    For instance:
    ... {{ 'no need to \\"escape" ' }} ...
    is equivalent to:
    ... {{ 'no need to "escape" ' }} ...
```

#### **Semantic Kernel Glossary**

- [Glossary in Git](https://github.com/microsoft/semantic-kernel/blob/main/docs/GLOSSARY.md) / [Glossary in MS Doc](https://learn.microsoft.com/en-us/semantic-kernel/whatissk#sk-is-a-kit-of-parts-that-interlock)

  <img src="../files/kernel-flow.png" alt="sk" width="500"/>

  | Term      | Short Description                                                                                                                                                                                                                                                                                     |
  | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | ASK       | A user's goal is sent to SK as an ASK                                                                                                                                                                                                                                                                 |
  | Kernel    | [The kernel](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/kernel) orchestrates a user's ASK                                                                                                                                                                                          |
  | Planner   | [The planner](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/planner) breaks it down into steps based upon resources that are available                                                                                                                                                |
  | Resources | Planning involves leveraging available [skills,](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/skills) [memories,](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/memories) and [connectors](https://learn.microsoft.com/en-us/semantic-kernel/concepts-sk/connectors) |
  | Steps     | A plan is a series of steps for the kernel to execute                                                                                                                                                                                                                                                 |
  | Pipeline  | Executing the steps results in fulfilling the user's ASK                                                                                                                                                                                                                                              |
- [Architecting AI Apps with Semantic Kernel](https://devblogs.microsoft.com/semantic-kernel/architecting-ai-apps-with-semantic-kernel/) How you could recreate Microsoft Word Copilot [6 Mar 2024]
  <details open>
    <summary>Expand</summary>
    <img src="../files/semantic-kernel-with-word-copilot.png" height="500">
  </details>

### **DSPy**

- DSPy (Declarative Self-improving Language Programs, pronounced “dee-es-pie”) / doc:[ref](https://dspy-docs.vercel.app) / [git](https://github.com/stanfordnlp/dspy)
 ![GitHub Repo stars](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat-square&label=%20&color=gray)
- DSPy Documentation & Cheetsheet [ref](https://dspy-docs.vercel.app)
- [DSPy](https://arxiv.org/abs/2310.03714): Compiling Declarative Language Model Calls into Self-Improving Pipelines [5 Oct 2023] / [git](https://github.com/stanfordnlp/dspy)
 ![GitHub Repo stars](https://img.shields.io/github/stars/stanfordnlp/dspy?style=flat-square&label=%20&color=gray)
- DSPy Explained! [youtube](https://www.youtube.com/watch?v=41EfOY0Ldkc) [30 Jan 2024]
- DSPy RAG example in weviate recipes: `recipes > integrations` [git](https://github.com/weaviate/recipes)
 ![GitHub Repo stars](https://img.shields.io/github/stars/weaviate/recipes?style=flat-square&label=%20&color=gray)
- [Prompt Like a Data Scientist: Auto Prompt Optimization and Testing with DSPy](https://towardsdatascience.com/prompt-like-a-data-scientist-auto-prompt-optimization-and-testing-with-dspy-ff699f030cb7) [6 May 2024]
- Instead of a hard-coded prompt template, "Modular approach: compositions of modules -> compile". Building blocks such as ChainOfThought or Retrieve and compiling the program, optimizing the prompts based on specific metrics. Unifying strategies for both prompting and fine-tuning in one tool, Pythonic operations, prioritizing and tracing program execution. These features distinguish it from other LMP frameworks such as LangChain, and LlamaIndex. [ref](https://towardsai.net/p/machine-learning/inside-dspy-the-new-language-model-programming-framework-you-need-to-know-about) [Jan 2023]
- Automatically iterate until the best result is achieved: 1. Collect Data -> 2. Write DSPy Program -> 3. Define validtion logic -> 4. Compile DSPy program

  <img src="../files/dspy-workflow.jpg" width="400" alt="workflow">

### **Optimizer frameworks**

- These frameworks, including DSpy, utilize algorithmic methods inspired by machine learning to improve prompts, outputs, and overall performance in LLM applications.
- [AdalFlow](https://github.com/SylphAI-Inc/AdalFlow):💡The Library to Build and Auto-optimize LLM Applications [Apr 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/SylphAI-Inc/AdalFlow?style=flat-square&label=%20&color=gray)
- [TextGrad](https://github.com/zou-group/textgrad): automatic ``differentiation` via text. Backpropagation through text feedback provided by LLMs [Jun 2024]
 ![GitHub Repo stars](https://img.shields.io/github/stars/zou-group/textgrad?style=flat-square&label=%20&color=gray)

#### **DSPy Glossary**

- Glossary reference to the [ref](https:/towardsdatascience.com/intro-to-dspy-goodbye-prompting-hello-programming-4ca1c6ce3eb9).
  1. Signatures: Hand-written prompts and fine-tuning are abstracted and replaced by signatures.
      > "question -> answer" <br/>
        "long-document -> summary"  <br/>
        "context, question -> answer"  <br/>
  2. Modules: Prompting techniques, such as `Chain of Thought` or `ReAct`, are abstracted and replaced by modules.
      ```python
      # pass a signature to ChainOfThought module
      generate_answer = dspy.ChainOfThought("context, question -> answer")
      ```
  3. Optimizers (formerly Teleprompters): Manual iterations of prompt engineering is automated with optimizers (teleprompters) and a DSPy Compiler.
      ```python
      # Self-generate complete demonstrations. Teacher-student paradigm, `BootstrapFewShotWithOptuna`, `BootstrapFewShotWithRandomSearch` etc. which work on the same principle.
      optimizer = BootstrapFewShot(metric=dspy.evaluate.answer_exact_match)
      ```
  4. DSPy Compiler: Internally trace your program and then optimize it using an optimizer (teleprompter) to maximize a given metric (e.g., improve quality or cost) for your task.
  - e.g., the DSPy compiler optimizes the initial prompt and thus eliminates the need for manual prompt tuning.
    ```python
    cot_compiled = teleprompter.compile(CoT(), trainset=trainset, valset=devset)
    cot_compiled.save('turbo_gsm8k.json')
    ```

#### DSPy optimizer

<details open>
  <summary>Expand</summary>

  - Automatic Few-Shot Learning

    - As a rule of thumb, if you don't know where to start, use `BootstrapFewShotWithRandomSearch`.
      
    - If you have very little data, e.g. 10 examples of your task, use `BootstrapFewShot`.
      
    - If you have slightly more data, e.g. 50 examples of your task, use `BootstrapFewShotWithRandomSearch`.
      
    - If you have more data than that, e.g. 300 examples or more, use `BayesianSignatureOptimizer`.
  
  - Automatic Instruction Optimization

    - `COPRO`: Repeat for a set number of iterations, tracking the best-performing instructions.

    - `MIPRO`: Repeat for a set number of iterations, tracking the best-performing combinations (instructions and examples).

  - Automatic Finetuning

    - If you have been able to use one of these with a large LM (e.g., 7B parameters or above) and need a very efficient program, compile that down to a small LM with `BootstrapFinetune`.
</details>