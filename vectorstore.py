from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


def create_vector_store(chunks, persist_directory="chroma_db"):

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=persist_directory
    )

    return vector_store