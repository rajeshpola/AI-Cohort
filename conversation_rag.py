from typing import Annotated
from langgraph.graph import START,END,add_messages
from langchain.chat_models import init_chat_model
from typing_extensions import TypedDict
from langchain_core.messages import HumanMessage ,SystemMessage,AIMessage
from langgraph.graph import StateGraph
import dotenv
import os

dotenv.load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

class State(TypedDict):
    message:Annotated[list,add_messages]

llm=init_chat_model("openai:o3-mini",api_key=api_key);

def chatbot(state:State) ->State:
    print("-----")
    print(state["message"][-1].content)
    if (isinstance(state["message"][-1],AIMessage)):
        print("This is the instance of AIMessage")
    in_message=input("Enter your message")
    state["message"].append(HumanMessage(content=in_message))
    response = llm.invoke(state["message"])
    print(response.content)
    return {"message":  [response]}

def process(state:State) ->State:
    print(state)
    response = llm.invoke(state["message"])
    return {"message":  [response]}

graph=StateGraph(State)

graph.add_node("chatbot",chatbot)
graph.add_node("preProcess",process)



graph.set_entry_point("preProcess")
graph.add_edge("preProcess","chatbot")
graph.add_edge("chatbot",END)
app=graph.compile()
messages=[SystemMessage(content="You are an experienced System Assistant and you will help users with their questions."),HumanMessage(content="How you doing and how to lift up")]
response=app.invoke({"message":messages[1]})