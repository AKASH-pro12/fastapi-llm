import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from documents import documents
from prompt import prompt


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")


embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=embeddings,
    collection_name="rag_collection",
    persist_directory="./chroma_db"
)


retriever = vectorstore.as_retriever(
    search_kwargs={"k": 2}
)


llm = ChatGroq(
    model="qwen/qwen3.6-27b",
    temperature=0.7,
    api_key=groq_api_key
)


def rag(query):

    docs = retriever.invoke(query)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    formatted_prompt = prompt.invoke({
        "context": context,
        "question": query
    })

    response = llm.invoke(formatted_prompt)

    return response.content


print("\n" + "=" * 40)
print("            RAG CHATBOT")
print("=" * 40)
print("Type 'exit' to quit.")

while True:
    question = input("\nYou: ").strip()

    if question.lower() == "exit":
        print("\nGood Bye!")
        break

    if not question:
        print("Please enter a question.")
        continue

    try:
        answer = rag(question)

        print("\nAssistant:")
        print(answer)

    except Exception as e:
        print(f"\nError: {e}")