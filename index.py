from dotenv import load_dotenv
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore
import os

load_dotenv()

PDF_PATH = Path(__file__).parent / "Bhagvat_gita.pdf"
COLLECTION_NAME = "bhagavad_gita_ttd"

print("📖 Loading Bhagavad Gita PDF...")
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

print(f"📄 Total pages loaded: {len(docs)}")

# 🔹 Chunking strategy for commentary-heavy scripture
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=600,
    chunk_overlap=120
)

chunks = text_splitter.split_documents(docs)

# Add clean metadata
for chunk in chunks:
    chunk.metadata["source"] = "Bhagavad Gita (TTD English)"
    chunk.metadata["book"] = "Bhagavad Gita"

print(f"✂️ Total chunks created: {len(chunks)}")

# 🔹 Free & reliable embeddings
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# 🔹 Store in Qdrant
QdrantVectorStore.from_documents(
    documents=chunks,
    embedding=embedding_model,
    url=os.getenv("QDRANT_URL"),
    collection_name=COLLECTION_NAME,
    force_recreate=True
)

print("✅ Indexing completed successfully.")
