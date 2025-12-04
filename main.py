from fastapi import FastAPI
from pydantic import BaseModel

class chatRequest(BaseModel):
    prompt: str

class chatResponse(BaseModel):
    response: str

app = FastAPI()

@app.get("/")
def health():
    return {"status": "Ok! This is working woohoo!"}

@app.post("/chat", response_model=chatResponse)
def chat(request: chatRequest):
     return chatResponse(response=f"I will get smarter later!")