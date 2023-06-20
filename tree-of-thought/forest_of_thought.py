from dotenv import load_dotenv
import os
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI

from dotenv import load_dotenv
import os
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI


# Forest of thought sample
'''
Title of the page: mrspiggot/forestOfThoughts
Name of the website: mrspiggot/forestOfThoughts
URL: https://github.com/mrspiggot/forestOfThoughts
'''

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm_1 = OpenAI(temperature=0.7, max_tokens=3000)
llm_2 = OpenAI(temperature=0.4, max_tokens=3000)
llm_3 = OpenAI(temperature=0.1, max_tokens=3000)



template_1 = """Imagine three different experts are answering this question.
They will brainstorm the answer step by step reasoning carefully and taking all facts into consideration
All experts will write down 1 step of their thinking,
then share it with the group.
They will each critique their response, and the all the responses of others
They will check their answer based on science and the laws of physics
Then all experts will go on to the next step and write down this step of their thinking.
They will keep going through steps until they reach their conclusion taking into account the thoughts of the other experts
If at any time they realise that there is a flaw in their logic they will backtrack to where that flaw occurred 
If any expert realises they're wrong at any point then they acknowledges this and start another train of thought
Each expert will assign a likelihood of their current assertion being correct
Continue until the experts agree on the single most likely location
The question is {question}

The experts reasoning is...
"""

template_2 = """Imagine six different experts are answering this question.
They will brainstorm the answer step by step reasoning carefully and taking all facts into consideration
Each expert will share their first step with all of the other experts
They will each critique their response, and the all the responses of others
They will check their answer being careful to think through any consequences
Each expert will then write down the next step of their thought process
Each expert will assign a likelihood of their current assertion being correct
Continue until the experts agree on the single most likely location
The question is {question}

The experts reasoning is...
"""

template_3 = """Imagine four different experts are answering this question.
They will first write down all the facts
They will then consider three different alternative answers and communicate these answers to the other experts
they will write down the likelihood of each answer
Based on this they will each come up with a single answer
The question is {question}

The experts reasoning is...
"""


question = """1. Carlos is at the swimming pool. 
2. He walks to the locker room, carrying a towel. 
3. He puts his watch in the towel and carries the towel tightly to a lounger at the poolside. 
4. At the lounger he opens and vigorously shakes the towel, then walks to the snack bar. 
5. He leaves the towel at the snack bar, then walks to the diving board. 
6. Later Carlos realises he has has lost his watch. Where is the single most likely location of the watch? """


prompt1 = PromptTemplate(template=template_1, input_variables=["question"])
prompt2 = PromptTemplate(template=template_2, input_variables=["question"])
prompt3 = PromptTemplate(template=template_3, input_variables=["question"])

llm_chain_1 = LLMChain(prompt=prompt1, llm=llm_1)
llm_chain_2 = LLMChain(prompt=prompt2, llm=llm_2)
llm_chain_3 = LLMChain(prompt=prompt3, llm=llm_3)

response_1 = llm_chain_1.run(question)
response_2 = llm_chain_2.run(question)
response_3 = llm_chain_3.run(question)

print(response_1)
print(response_2)
print(response_3)

get_together = """Several experts have been asked this question 
1. Carlos is at the swimming pool. 
2. He walks to the locker room, carrying a towel. 
3. He puts his watch in the towel and carries the towel tightly to a lounger at the poolside. 
4. At the lounger he opens and vigorously shakes the towel, then walks to the snack bar. 
5. He leaves the towel at the snack bar, then walks to the diving board. 
6. Later Carlos realises he has has lost his watch. 
Where is the single most likely location of the watch? their resulting answers are {answer} 
which answer is most likely? 
The most likely answer is..."""

answer = response_1+response_2+response_3
fusion = PromptTemplate(template=get_together, input_variables=["answer"])

wood_for_trees = OpenAI(temperature=0.1, max_tokens=3000)
final = LLMChain(prompt=fusion, llm=wood_for_trees)
conclusion = final.run(answer)

print(f"Conclusion is {conclusion}")