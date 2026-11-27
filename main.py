import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="Universal AI Backend")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict to your website URL before public launch.
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"status": "Universal AI backend is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise HTTPException(status_code=500, detail="OPENAI_API_KEY is not configured on the server.")
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
    try:
        client = OpenAI(api_key=api_key)
        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
            input=request.message
        )
        return {"reply": response.output_text}
    except Exception:
        raise HTTPException(status_code=502, detail="AI provider request failed. Check server logs and API account.")
