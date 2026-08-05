# 📄 PDF RAG Chatbot

**Name:**
*Nimisha Roy*

**MUID:**
*nimisharoy@mulearn*

---

## Project Overview

The **PDF RAG Chatbot** is an AI-powered web application that allows users to upload any PDF document and ask questions about its contents.

The application uses **Retrieval-Augmented Generation (RAG)** to retrieve the most relevant information from the uploaded document before generating an answer using a Large Language Model (LLM). This ensures that responses are based only on the uploaded document instead of general knowledge.

Users can upload different PDF files, and the application automatically creates a new vector database for each uploaded document, allowing personalized document-based question answering.

---

## Features

- 📂 Upload any PDF document
- 📖 Automatically extract text from the PDF
- ✂ Split documents into semantic chunks
- 🧠 Generate embeddings using Hugging Face
- 💾 Store embeddings in ChromaDB
- 🔍 Retrieve relevant document sections
- 🤖 Generate answers using Groq Llama 3.1
- 💬 Interactive Gradio web interface
- 🔄 Supports uploading different PDFs without restarting the application

---

## Technologies Used

- Python
- LangChain
- ChromaDB
- Hugging Face Embeddings
- Groq API
- Llama 3.1 8B Instant
- PyPDF
- Gradio
- python-dotenv

---

## Project Structure

```
PDF-AI-Assistant/
│
├── app.py
├── chatbot.py
├── loader.py
├── vectorstore.py
├── requirements.txt
├── README.md
├── .env.example
├── data/
└── chroma_db/
```

---

## How It Works

1. User uploads a PDF.
2. The PDF is loaded using PyPDFLoader.
3. The document is split into smaller chunks.
4. Hugging Face generates embeddings for each chunk.
5. ChromaDB stores the embeddings.
6. When the user asks a question:
   - Relevant chunks are retrieved.
   - The retrieved context is sent to the Groq LLM.
   - The AI generates an answer based only on the uploaded document.

---

## Memory Implementation

The chatbot uses **Retrieval-Augmented Generation (RAG)** instead of storing conversation memory.

Memory is implemented through a **ChromaDB vector database**, which stores vector embeddings of the uploaded PDF.

When a user asks a question:

- The question is converted into an embedding.
- ChromaDB performs semantic similarity search.
- The top matching document chunks are retrieved.
- Only those relevant chunks are sent to the Groq language model.
- The model generates an answer using the retrieved context.

Each uploaded PDF creates its own vector database, allowing users to switch documents without mixing information from previous uploads.

---

## Challenges Faced

During development, several challenges were encountered:

- Setting up the Python virtual environment correctly.
- Configuring the Groq API key using environment variables.
- Updating deprecated LangChain imports.
- Fixing compatibility issues between newer versions of LangChain and Gradio.
- Handling invalid or corrupted PDF files.
- Managing ChromaDB persistence when uploading multiple PDFs.
- Ensuring responses were generated only from the uploaded document.

Each challenge provided valuable experience in debugging Python applications and integrating multiple AI frameworks.

---

## Future Improvements

Potential future enhancements include:

- 📄 Support multiple PDFs simultaneously.
- 💬 Add conversation memory for follow-up questions.
- 📚 Display the source page number for each answer.
- 🌐 Deploy the application on Hugging Face Spaces.
- ☁ Add cloud storage for uploaded PDFs.
- 📑 Support Word, PowerPoint, and text documents.
- 🔎 Improve document retrieval using hybrid search.
- 🎨 Enhance the user interface with custom styling and themes.

---

# Acknowledgements

This project was built using:

- LangChain
- ChromaDB
- Hugging Face
- Groq
- Gradio
