from fastapi import FastAPI
from pydantic import BaseModel

from llm import ask_llm

app = FastAPI()


class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask(request: QuestionRequest):
    result = ask_llm(request.question)

    return {
        "response": result
    }