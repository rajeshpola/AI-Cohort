from dotenv import load_dotenv
from rqueue.connection import queue
from fastapi import FastAPI,Query
from rqueue.connection import queue
from rqueue.worker import process_query
import os

load_dotenv()
key=os.getenv("openAI")
print(key)

app = FastAPI()

@app.get("/")
async def root():
    return{"message":"Hello World and server is running"}

@app.post("/chat")
async def chat(
    query : str = Query(...,description="chat message")
):
    #into the Que and say user job recieved
    queue.enqueue(process_query,query)
    pass
    
    