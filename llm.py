import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(
    model="qwen/qwen3.6-27b",
    temperature=0
)

def ask_llm(question: str):
    response = llm.invoke(question)

    content = response.content

    if "<think>" in content and "</think>" in content:
        content = content.split("</think>", 1)[1].strip()

    return content