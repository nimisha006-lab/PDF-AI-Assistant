# 📄 PDF AI Assistant

**Name:** Nimisha Roy 
**MUID:** nimisharoy@mulearn

---

## Project Overview

PDF AI Assistant is a Retrieval-Augmented Generation (RAG) application that allows users to upload any PDF document and ask questions about its content. Instead of answering from general knowledge, the application retrieves relevant information from the uploaded PDF and uses a Large Language Model (LLM) to generate accurate, context-based responses.

The application features an interactive Streamlit interface where users can upload a document, process it into a searchable knowledge base, and chat with the document in real time.

---

## Features

- 📂 Upload any PDF document
- ✂️ Automatically split documents into text chunks
- 🔍 Semantic search using vector embeddings
- 🤖 AI-powered question answering
- 💬 Interactive chat interface
- ⚡ Fast responses using Groq LLM
- 🌐 Deployed online using Streamlit Community Cloud

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | User Interface |
| LangChain | RAG Pipeline |
| PyPDFLoader | PDF Loading |
| RecursiveCharacterTextSplitter | Document Chunking |
| Hugging Face Sentence Transformers | Generate text embeddings |
| ChromaDB | Vector Database |
| Groq API (Llama 3.1 8B Instant) | Large Language Model |
| python-dotenv | Environment Variable Management |

---

## Project Structure

```
PDF-AI-Assistant/
│
├── app.py                 # Streamlit application
├── chatbot.py             # Question answering logic
├── loader.py              # PDF loading and chunking
├── vectorstore.py         # Creates Chroma vector database
├── requirements.txt
├── README.md
├── .gitignore
└── chroma_db/             # Generated vector database (not pushed to GitHub)
```

---

## How It Works

1. User uploads a PDF document.
2. PyPDFLoader extracts the text from the PDF.
3. The document is divided into smaller chunks using LangChain's RecursiveCharacterTextSplitter.
4. Hugging Face's **sentence-transformers/all-MiniLM-L6-v2** model converts each chunk into numerical embeddings.
5. ChromaDB stores these embeddings as a searchable vector database.
6. When a question is asked:
   - The application retrieves the most relevant chunks using semantic similarity search.
   - The retrieved context is sent to the Groq Llama 3.1 8B Instant model.
   - The LLM generates an answer based only on the retrieved document content.

---

## Memory Implementation

The application implements memory through a vector database rather than conversational memory.

- Uploaded PDF documents are converted into embeddings.
- Embeddings are stored in ChromaDB.
- For every user query, the application retrieves the most relevant document chunks.
- These retrieved chunks act as contextual memory for the language model, enabling accurate responses grounded in the uploaded PDF.

This Retrieval-Augmented Generation (RAG) approach ensures answers are based on the document instead of relying solely on the LLM's pretrained knowledge.

---

## Challenges Faced

During development, several challenges were encountered:

- Setting up LangChain with the latest package versions.
- Integrating Hugging Face embeddings with ChromaDB.
- Managing vector database creation for multiple uploaded PDFs.
- Resolving file upload issues when migrating from Gradio to Streamlit.
- Configuring the Groq API securely using environment variables.
- Deploying the application successfully on Streamlit Community Cloud.
- Managing project dependencies and package compatibility during deployment.

---

## Future Improvements

Future enhancements planned for the project include:

- Support multiple PDF uploads simultaneously.
- Maintain conversation history across questions.
- Display the source page for each answer.
- Allow users to download chat history.
- Add support for Word documents and text files.
- Improve UI with dark mode and additional customization.
- Deploy using Docker for easier scalability.

---

## Deployment

The application is deployed using **Streamlit Community Cloud**.
**Deployment Link:** https://pdf-ai-assistant-bxmht6p3u69jbm8n2drgra.streamlit.app/


