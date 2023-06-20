from llama_index.callbacks import CallbackManager, LlamaDebugHandler, CBEventType
from llama_index import ListIndex, ServiceContext, SimpleDirectoryReader, VectorStoreIndex

'''
Title of the page: A simple Python implementation of the ReAct pattern for LLMs
Name of the website: LlamaIndex (GPT Index) is a data framework for your LLM application.
URL: https://github.com/jerryjliu/llama_index
'''
docs = SimpleDirectoryReader("../data/paul_graham/").load_data()

from llama_index import ServiceContext, LLMPredictor, TreeIndex
from langchain.chat_models import ChatOpenAI
llm_predictor = LLMPredictor(llm=ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0))

llama_debug = LlamaDebugHandler(print_trace_on_end=True)
callback_manager = CallbackManager([llama_debug])
service_context = ServiceContext.from_defaults(callback_manager=callback_manager, llm_predictor=llm_predictor)

index = VectorStoreIndex.from_documents(docs, service_context=service_context)
query_engine = index.as_query_engine()

response = query_engine.query("What did the author do growing up?")

# Print info on the LLM calls during the list index query
print(llama_debug.get_event_time_info(CBEventType.LLM))

# Print info on llm inputs/outputs - returns start/end events for each LLM call
event_pairs = llama_debug.get_llm_inputs_outputs()
print(event_pairs[0][0])
print(event_pairs[0][1].payload.keys())
print(event_pairs[0][1].payload['response'])

# Get info on any event type
event_pairs = llama_debug.get_event_pairs(CBEventType.CHUNKING)
print(event_pairs[0][0].payload.keys())  # get first chunking start event
print(event_pairs[0][1].payload.keys())  # get first chunking end event

# Clear the currently cached events
llama_debug.flush_event_logs()
