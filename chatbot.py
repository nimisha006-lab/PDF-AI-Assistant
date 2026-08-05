from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()


llm = ChatGroq(
    model="llama-3.1-8b-instant"
)

prompt = ChatPromptTemplate.from_template("""
You are a helpful PDF assistant.

Use ONLY the information provided in the context.

If the answer cannot be found in the context, reply:

"I couldn't find that information in the uploaded PDF."

Context:
{context}

Question:
{question}

Answer:
""")


def ask_question(question, vector_store):

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    docs = retriever.invoke(question)

    if not docs:
        return "I couldn't find anything related to that in the uploaded PDF."

    context = "\n\n".join(doc.page_content for doc in docs)

    messages = prompt.invoke(
        {
            "context": context,
            "question": question
        }
    )

    response = llm.invoke(messages)

    return response.content