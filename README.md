🕉️ Bhagavad Gita Assistant (RAG-Powered)

A Retrieval-Augmented Generation (RAG) based AI assistant that delivers grounded, explainable, and source-cited guidance from the Bhagavad Gita (English – TTD edition).

The system combines semantic search, LLM reasoning, and a themed, confidence-aware UI to present timeless wisdom for modern life — without hallucination.

🌟 Key Features
1️⃣ 🌅 Verse of the Day

Displays a daily Bhagavad Gita teaching

Deterministic: same verse for the entire day

Fully retrieval-based (no random generation)

Includes confidence score and source provenance

2️⃣ ❓ Question Answering

Ask natural language questions such as:

What is karma yoga?

What does the Gita say about duty?

Highlights

Answers are strictly grounded in the Gita text

Includes:

📊 Confidence score

📖 Page-level provenance

Prevents hallucination through context-only answering

3️⃣ 💭 Emotion-Based Guidance

Select how you feel:

😟 Anxious

😠 Angry

😕 Confused

😔 Sad

😌 Peace

How it works

Emotions are converted into semantic intent

Relevant verses are retrieved from Qdrant

The assistant provides reflective guidance grounded in scripture

4️⃣ 🧭 Life Phase Guidance

Contextual wisdom based on life stage:

🎓 Student

💼 Professional

🧑‍💼 Leader

🏠 Family Person

Maps real-world responsibilities to Gita principles such as:

Duty (Dharma)

Detachment

Selfless action (Karma Yoga)

5️⃣ ⚖️ Wisdom Comparison Mode (Unique Feature)

Compare two philosophical concepts side-by-side:

Duty vs Desire

Action vs Attachment

Knowledge vs Devotion

Why it’s special

Uses the same RAG pipeline for both sides

Shows confidence scores for each teaching

Encourages critical thinking and reflection

Rarely seen in student projects

6️⃣ 🟢🟡🔴 Confidence-Aware Visual Feedback

Each answer is visually styled based on confidence:

🟢 High confidence – strong grounding

🟡 Medium confidence – verify context

🔴 Low confidence – limited textual support

This improves trust, transparency, and explainability.

7️⃣ 🌞🌙🕯️ Light / Dark / Meditation Mode

A premium UI enhancement:

🌞 Light Mode – traditional saffron theme

🌙 Dark Mode – accessibility-friendly

🕯️ Meditation Mode – distraction-free reflective UI

No backend changes — purely UI-driven.

🎨 Themed UI

Krishna–Arjuna hero imagery

Saffron-inspired spiritual palette

Card-based layouts for clarity

Clean, minimal, and calm design

Optimized for reflection, not overload

🧠 Architecture Overview
User (Streamlit UI)
        ↓
FastAPI Backend
        ↓
RAG Engine
        ↓
Qdrant Vector Database
        ↓
Bhagavad Gita (English – TTD PDF)

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

Fully retrieval-based (no fine-tuning)
