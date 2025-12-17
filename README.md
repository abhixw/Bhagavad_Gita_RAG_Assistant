🕉️ Bhagavad Gita Assistant (RAG-Powered)

A Retrieval-Augmented Generation (RAG) based AI assistant that provides grounded, source-cited guidance from the Bhagavad Gita (English – TTD edition).
The system combines semantic search, LLM reasoning, and a themed UI to deliver timeless wisdom for modern life.

🌟 Key Features
🌅 Verse of the Day

Displays a daily Bhagavad Gita teaching

Deterministic: same verse for the entire day

Fully retrieval-based (no hallucination)

❓ Question Answering

Ask natural language questions such as:

What is karma yoga?

What does the Gita say about duty?

Answers are strictly grounded in the Gita text

Includes transparent source citations

💭 Emotion-Based Guidance

Select how you feel:

😟 Anxious

😠 Angry

😕 Confused

😔 Sad

😌 Peace

The system:

Converts emotions into semantic intent

Retrieves relevant teachings

Provides reflective guidance from the Gita

🧭 Life Phase Guidance

Contextual wisdom based on life stage:

🎓 Student

💼 Professional

🧑‍💼 Leader

🏠 Family Person

Maps real-world responsibilities to Gita principles such as duty, detachment, and selfless action.

🎨 Themed UI

Krishna–Arjuna hero image

Saffron-themed color palette

Card-based layouts for readability

Clean, minimal, and spiritual design

🧠 Architecture Overview
User (Streamlit UI)
        ↓
FastAPI Backend
        ↓
RAG Engine
        ↓
Qdrant Vector Database
        ↓
Bhagavad Gita (English PDF)

🛠️ Tech Stack
🔧 Backend & AI

Python

FastAPI – API layer

LangChain – RAG orchestration

Groq LLM – Fast inference for reasoning

HuggingFace Sentence Transformers – Text embeddings

Qdrant – Vector database for semantic search

🎨 Frontend

Streamlit – Interactive web UI

Pillow – Image handling (hero image)

📚 Data

Bhagavad Gita – English (TTD Edition)

Chunked and embedded for semantic retrieval

Fully retrieval-based (no hallucinated content)   

rag/
│
├── assets/
│   └── krishna_arjuna.jpeg
│
├── index.py              # PDF indexing & vector storage
├── rag_engine.py         # Core RAG logic
├── backend.py            # FastAPI API layer
├── app.py                # Streamlit frontend
│
├── .env                  # Environment variables
├── requirements.txt
└── README.md

⚙️ Installation & Setup
1️⃣ Create Virtual Environment

python -m venv venv
source venv/bin/activate   # macOS / Linux

2️⃣ Install Dependencies
pip install -r requirements.txt


Required packages include:

streamlit
fastapi
uvicorn
langchain
langchain-community
langchain-huggingface
langchain-qdrant
langchain-groq
qdrant-client
sentence-transformers
pypdf
python-dotenv
pillow
requests

3️⃣ Start Qdrant (Docker)
docker run -p 6333:6333 -p 6334:6334 qdrant/qdrant

4️⃣ Set Environment Variables (.env)
GROQ_API_KEY=your_groq_api_key
QDRANT_URL=http://localhost:6333

📥 Index the Bhagavad Gita

Run once to create vector embeddings:

python index.py


Sample Output:

📄 Total pages loaded: 447
✂️ Total chunks created: 1851
✅ Indexing completed successfully.

▶️ Run the Application
🚀 Start Backend
python -m uvicorn backend:app --reload


Backend runs at:

http://127.0.0.1:8000


Swagger API Docs:

http://127.0.0.1:8000/docs
🎨 Start Frontend
bash
Copy code
streamlit run app.py
Open in browser:

arduino
Copy code
http://localhost:8501

