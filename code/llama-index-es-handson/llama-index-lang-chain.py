from langchain.llms import OpenAIChat
from langchain.agents import initialize_agent

from llama_index import GPTListIndex
from llama_index.langchain_helpers.memory_wrapper import GPTIndexChatMemory


index = GPTListIndex([])

memory = GPTIndexChatMemory(
    index=index,
    memory_key="chat_history",
    query_kwargs={"response_mode": "compact"},
    # return_source returns source nodes instead of querying index
    return_source=True,
    # return_messages returns context in message format
    return_messages=True
)
llm = OpenAIChat(temperature=0)

agent_chain = initialize_agent([], llm, agent="conversational-react-description", memory=memory)

agent_chain.run(input="hi, i am bob")

agent_chain.run(input="what's my name?")

