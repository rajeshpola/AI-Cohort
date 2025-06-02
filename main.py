from typing import Union,Literal,List

from fastapi import FastAPI
from dotenv import load_dotenv
import os;
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

load_dotenv();

print(os.getenv("API_KEY"))
# allow_origins=[CLIENT_URL], 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)
class ChatMessage(BaseModel):
    role:Literal["system",'assistant']
    content:str

class ChatRequest(BaseModel):
    message:List[ChatMessage]

@app.get("/")
def read_root():
    return {"Hello":"World"}

@app.get("/persona/{persona}")
def read_item(persona: int, query: Union[str,None] = None):
    return {"persona": persona, "query":query}              