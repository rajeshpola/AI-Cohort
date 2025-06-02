from typing import Union,Literal,List

from fastapi import FastAPI
from dotenv import load_dotenv
import os;
from pydantic import BaseModel

app = FastAPI()

load_dotenv();

print(os.getenv("API_KEY"))

class ChatMessage(BaseModel):
    role:Literal["system",'assistant']
    content:str

class ChatRequest(BaseModel):
    message:List[ChatMessage]

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, query: Union[str,None] = None):
    return {"item_id": item_id, "query":query}              