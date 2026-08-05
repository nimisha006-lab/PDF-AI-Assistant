import os
import uuid
import gradio as gr

from loader import load_pdf
from vectorstore import create_vector_store
from chatbot import ask_question

vector_store = None


# -------------------------
# Upload PDF
# -------------------------
def process_pdf(pdf):
    global vector_store

    if pdf is None:
        return "❌ Please upload a PDF first."

    pdf_path = pdf.name if hasattr(pdf, "name") else pdf

    folder = f"chroma_db/{uuid.uuid4()}"

    chunks = load_pdf(pdf_path)

    vector_store = create_vector_store(
        chunks,
        persist_directory=folder
    )

    filename = os.path.basename(pdf_path)

    return f"✅ '{filename}' uploaded successfully!\nYou can now ask questions."


# -------------------------
# Chat Function
# -------------------------
def respond(message, history):

    global vector_store

    if history is None:
        history = []

    if vector_store is None:

        history.append(
            {
                "role": "assistant",
                "content": "⚠️ Please upload a PDF first."
            }
        )

        return history, ""

    answer = ask_question(message, vector_store)

    history.append(
        {
            "role": "user",
            "content": message
        }
    )

    history.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    return history, ""


def clear_chat():
    return []


# -------------------------
# UI
# -------------------------

with gr.Blocks(
    title="PDF AI Assistant"
) as demo:

    gr.Markdown(
        """
# 📄 PDF AI Assistant

### 🤖 Chat with any PDF using AI

Upload a PDF, click **Process PDF**, then ask questions about the document.

---
"""
    )

    with gr.Row():

        # ---------------- LEFT PANEL ----------------

        with gr.Column(scale=1):

            gr.Markdown("## 📂 Upload PDF")

            pdf = gr.File(
                label="Choose a PDF",
                file_types=[".pdf"]
            )

            upload_btn = gr.Button(
                "🚀 Process PDF",
                variant="primary",
                size="lg"
            )

            status = gr.Textbox(
                label="Status",
                interactive=False,
                lines=3
            )

            gr.Markdown("---")


        # ---------------- RIGHT PANEL ----------------

        with gr.Column(scale=2):

            chatbot = gr.Chatbot(
                label="💬 Chat",
                height=550
            )

            msg = gr.Textbox(
                label="Ask a question",
                placeholder="Type your question here..."
            )

            with gr.Row():

                ask_btn = gr.Button(
                    "💬 Ask",
                    variant="primary"
                )

                clear_btn = gr.Button(
                    "🗑 Clear Chat"
                )

    # Events

    upload_btn.click(
        process_pdf,
        inputs=pdf,
        outputs=status
    )

    ask_btn.click(
        respond,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )

    msg.submit(
        respond,
        inputs=[msg, chatbot],
        outputs=[chatbot, msg]
    )

    clear_btn.click(
        clear_chat,
        outputs=chatbot
    )

    gr.Markdown(
        """
---

### ⚡ Built With

- 🦜 LangChain
- 🤗 Hugging Face Embeddings
- 🗄️ ChromaDB
- 🚀 Groq Llama 3.1
- 🎨 Gradio

Made with ❤️ by Lydia
"""
    )


demo.launch()