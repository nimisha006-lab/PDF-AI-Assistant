print("Loader file is running!")
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_pdf(pdf_path):
    """
    Load a PDF and split it into smaller chunks.
    """

    # Read the PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split the PDF into smaller chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    return chunks