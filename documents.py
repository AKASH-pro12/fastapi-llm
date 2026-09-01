from langchain_core.documents import Document

documents = [
    Document(
        page_content="""
        Python is a high-level, interpreted programming language.
        It is widely used in web development, artificial intelligence,
        machine learning, data science, automation and scripting.
        """,
        metadata={"topic": "Python"}
    ),

    Document(
        page_content="""
        FastAPI is a modern, high-performance web framework for
        building APIs with Python. It supports request validation,
        asynchronous programming and automatic API documentation.
        """,
        metadata={"topic": "FastAPI"}
    ),

    Document(
        page_content="""
        LangChain is a framework for developing applications powered
        by large language models. It provides components for prompts,
        language models, retrievers and RAG pipelines.
        """,
        metadata={"topic": "LangChain"}
    ),

    Document(
        page_content="""
        ChromaDB is a vector database used to store and retrieve
        vector embeddings. It is commonly used in RAG applications
        for similarity-based document retrieval.
        """,
        metadata={"topic": "ChromaDB"}
    )
]