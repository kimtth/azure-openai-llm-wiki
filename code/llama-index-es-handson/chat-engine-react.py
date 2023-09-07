from llama_index import VectorStoreIndex, SimpleDirectoryReader
data = SimpleDirectoryReader(input_dir="../data/paul_graham/").load_data()
index = VectorStoreIndex.from_documents(data)

chat_engine = index.as_chat_engine(chat_mode='react', verbose=True)

response = chat_engine.chat('Use the tool to answer: what did Paul Graham do in the summer of 1995?')

print(response)

chat_engine.reset()