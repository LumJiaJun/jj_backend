from fastapi import FastAPI
from pydantic import BaseModel
import cohere
from dotenv import load_dotenv
import os


load_dotenv()
API_KEY = os.getenv("COHERE_API_KEY")

if not API_KEY:
    raise RuntimeError("COHERE_API_KEY environment variable is not set")

co = cohere.ClientV2(api_key=API_KEY)


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str


app = FastAPI()


@app.get("/")
def health():
    return {"status": "Ok! This is working woohoo!"}


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    user_prompt = request.prompt

    response = co.chat(
        model="command-a-03-2025",
        messages=[{"role": "user", "content": user_prompt}],
    )

    final_response = response.message.content[0].text

    return ChatResponse(response=f"Cohere said this: {final_response}")