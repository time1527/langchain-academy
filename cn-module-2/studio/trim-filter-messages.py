import os, getpass
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import trim_messages


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("DASHSCOPE_API_KEY")
_set_env("LANGSMITH_API_KEY")
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_PROJECT"] = "langchain-academy"


llm = ChatTongyi(model="qwen-plus")


# # Node
# def chat_model_node(state: MessagesState):
#     return {"messages": [llm.invoke(state["messages"][-1:])]}


def chat_model_node(state: MessagesState):
    messages = trim_messages(
        state["messages"],
        max_tokens=100,
        strategy="last",
        # token_counter=ChatOpenAI(model="gpt-4o"),
        token_counter=ChatTongyi(model="qwen-plus"),
        allow_partial=False,
    )
    return {"messages": [llm.invoke(messages)]}


# Build graph
builder = StateGraph(MessagesState)
builder.add_node("chat_model", chat_model_node)
builder.add_edge(START, "chat_model")
builder.add_edge("chat_model", END)
graph = builder.compile()
