import streamlit as st
import uuid

from loader import load_pdf
from vectorstore import create_vector_store
from chatbot import ask_question

st.set_page_config(
    page_title="PDF AI Assistant",
    page_icon="📄",
    layout="wide"
)

# -------------------------
# Custom CSS
# -------------------------

st.markdown("""
<style>

.main{
    background:#f6f8fc;
}

.stButton>button{
    width:100%;
    border-radius:12px;
    height:48px;
    font-size:17px;
    font-weight:bold;
}

.user{
    background:#2563eb;
    color:white;
    padding:15px;
    border-radius:15px;
    margin-bottom:10px;
}

.bot{
    background:white;
    padding:15px;
    border-radius:15px;
    border:1px solid #ddd;
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# Session State
# -------------------------

if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "messages" not in st.session_state:
    st.session_state.messages = []

# -------------------------
# Sidebar
# -------------------------

with st.sidebar:

    st.title("📄 PDF AI")

    st.write("Upload any PDF and chat with it.")

    pdf = st.file_uploader(
        "Choose PDF",
        type=["pdf"]
    )

    if st.button("🚀 Process PDF"):

        if pdf is None:
            st.warning("Upload a PDF first.")

        else:

            with st.spinner("Processing PDF..."):

                import tempfile

                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                    temp_file.write(pdf.read())
                    temp_pdf_path = temp_file.name

                    chunks = load_pdf(temp_pdf_path)

                folder = f"chroma_db/{uuid.uuid4()}"

                st.session_state.vector_store = create_vector_store(
                    chunks,
                    persist_directory=folder
                )

            st.success("PDF Ready!")

    st.divider()

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []

# -------------------------
# Main
# -------------------------

st.title("🤖 PDF AI Assistant")

st.caption("Ask questions about your uploaded PDF.")

# Display chat

for msg in st.session_state.messages:

    if msg["role"] == "user":

        st.markdown(
            f'<div class="user">🧑 {msg["content"]}</div>',
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f'<div class="bot">🤖 {msg["content"]}</div>',
            unsafe_allow_html=True
        )

# -------------------------
# Input
# -------------------------

question = st.chat_input("Ask a question...")

if question:

    if st.session_state.vector_store is None:

        st.warning("Upload a PDF first.")

    else:

        st.session_state.messages.append(
            {
                "role":"user",
                "content":question
            }
        )

        with st.spinner("Thinking..."):

            answer = ask_question(
                question,
                st.session_state.vector_store
            )

        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":answer
            }
        )

        st.rerun()