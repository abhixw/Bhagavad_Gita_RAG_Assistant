🕉️ Bhagavad Gita Assistant (RAG-Powered)

A Retrieval-Augmented Generation (RAG) based AI assistant that provides grounded, source-cited guidance from the Bhagavad Gita (English – TTD edition).
The system combines semantic search, LLM reasoning, and a themed UI to deliver timeless wisdom for modern life.

🌟 Key Features:

🌅 Verse of the Day

Displays a daily Bhagavad Gita teaching

Deterministic: same verse for the entire day

Fully retrieval-based (no hallucination)

❓ Question Answering:

Ask natural language questions such as:

What is karma yoga?

What does the Gita say about duty?

Answers are strictly grounded in the Gita text

Includes transparent source citations

💭 Emotion-Based Guidance :

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

🧭 Life Phase Guidance :

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

Pillow – Image handling 

📚 Data

Bhagavad Gita – English (TTD Edition)

Chunked and embedded for semantic retrieval

Fully retrieval-based 





