from dotenv import load_dotenv
import os
from langchain import PromptTemplate, LLMChain
from langchain.llms import OpenAI

# Tree of thought sample
'''
Title of the page: mrspiggot/forestOfThoughts
Name of the website: mrspiggot/forestOfThoughts
URL: https://github.com/mrspiggot/forestOfThoughts
'''
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

llm_1 = OpenAI(temperature=0.7, max_tokens=3000)

template = """Imagine three different experts are answering this question.
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


question = """1. Carlos is at the swimming pool. 
2. He walks to the locker room, carrying a towel. 
3. He puts his watch in the towel and carries the towel tightly to a lounger at the poolside. 
4. At the lounger he opens and vigorously shakes the towel, then walks to the snack bar. 
5. He leaves the towel at the snack bar, then walks to the diving board. 
6. Later Carlos realises he has has lost his watch. Where is the single most likely location of the watch? """


prompt = PromptTemplate(template=template, input_variables=["question"])
llm_chain = LLMChain(prompt=prompt, llm=llm_1)

response_1 = llm_chain.run(question)

print(response_1)