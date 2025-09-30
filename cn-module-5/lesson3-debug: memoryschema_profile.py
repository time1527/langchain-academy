from IPython.display import Image, display
from pydantic import BaseModel, Field

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_core.runnables.config import RunnableConfig
from langgraph.checkpoint.memory import MemorySaver
from langgraph.store.base import BaseStore
from langgraph.store.memory import InMemoryStore
from langchain_community.chat_models import ChatTongyi
from trustcall import create_extractor

# Initialize the model
# model = ChatOpenAI(model="gpt-4o", temperature=0)
model = ChatTongyi(model="qwen3-max", temperature=0)


# Schema
class UserProfile(BaseModel):
    """Profile of a user"""

    user_name: str = Field(description="The user's preferred name")
    user_location: str = Field(description="The user's location")
    interests: list = Field(description="A list of the user's interests")


# Create the extractor
trustcall_extractor = create_extractor(
    model,
    tools=[UserProfile],
    # tool_choice="UserProfile",  # Enforces use of the UserProfile tool
    # tool_choice="auto",
)

# Chatbot instruction
MODEL_SYSTEM_MESSAGE = """You are a helpful assistant with memory that provides information about the user. 
If you have memory for this user, use it to personalize your responses.
Here is the memory (it may be empty): {memory}"""

# Extraction instruction
TRUSTCALL_INSTRUCTION = """Create or update the memory (JSON doc) to incorporate information from the following conversation:"""


def call_model(state: MessagesState, config: RunnableConfig, store: BaseStore):
    """Load memory from the store and use it to personalize the chatbot's response."""

    # Get the user ID from the config
    user_id = config["configurable"]["user_id"]

    # Retrieve memory from the store
    namespace = ("memory", user_id)
    existing_memory = store.get(namespace, "user_memory")

    # Format the memories for the system prompt
    if existing_memory and existing_memory.value:
        memory_dict = existing_memory.value
        formatted_memory = (
            f"Name: {memory_dict.get('user_name', 'Unknown')}\n"
            f"Location: {memory_dict.get('user_location', 'Unknown')}\n"
            f"Interests: {', '.join(memory_dict.get('interests', []))}"
        )
    else:
        formatted_memory = None

    # Format the memory in the system prompt
    system_msg = MODEL_SYSTEM_MESSAGE.format(memory=formatted_memory)

    # Respond using memory as well as the chat history
    response = model.invoke([SystemMessage(content=system_msg)] + state["messages"])

    return {"messages": response}


def write_memory(state: MessagesState, config: RunnableConfig, store: BaseStore):
    """Reflect on the chat history and save a memory to the store."""

    # Get the user ID from the config
    user_id = config["configurable"]["user_id"]

    # Retrieve existing memory from the store
    namespace = ("memory", user_id)
    existing_memory = store.get(namespace, "user_memory")

    # Get the profile as the value from the list, and convert it to a JSON doc
    existing_profile = (
        {"UserProfile": existing_memory.value} if existing_memory else None
    )
    print(existing_profile)

    # Invoke the extractor
    ###################### new #####################
    result = trustcall_extractor.invoke(
        {
            "messages": [SystemMessage(content=TRUSTCALL_INSTRUCTION)]
            + state["messages"]
        },
        {
            "existing": existing_profile,
        },
    )
    print(result)

    # Get the updated profile as a JSON object
    updated_profile = result["responses"][0].model_dump()
    ###################### new #####################

    # Save the updated profile
    key = "user_memory"
    store.put(namespace, key, updated_profile)


# Define the graph
builder = StateGraph(MessagesState)
builder.add_node("call_model", call_model)
builder.add_node("write_memory", write_memory)
builder.add_edge(START, "call_model")
builder.add_edge("call_model", "write_memory")
builder.add_edge("write_memory", END)

# Store for long-term (across-thread) memory
across_thread_memory = InMemoryStore()

# Checkpointer for short-term (within-thread) memory
within_thread_memory = MemorySaver()

# Compile the graph with the checkpointer fir and store
graph = builder.compile(checkpointer=within_thread_memory, store=across_thread_memory)

# # View
# display(Image(graph.get_graph(xray=1).draw_mermaid_png()))

if __name__ == "__main__":
    config = {"configurable": {"thread_id": "1", "user_id": "1"}}

    # User input
    input_messages = [HumanMessage(content="Hi, my name is Lance")]

    # Run the graph
    for chunk in graph.stream(
        {"messages": input_messages}, config, stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()

    # User input
    input_messages = [HumanMessage(content="I like to bike around San Francisco")]

    # Run the graph
    for chunk in graph.stream(
        {"messages": input_messages}, config, stream_mode="values"
    ):
        chunk["messages"][-1].pretty_print()
