from dotenv import load_dotenv
from langchain_qdrant import QdrantVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
import os
import datetime
import random

load_dotenv()

COLLECTION_NAME = "bhagavad_gita_ttd"

# -------------------------
# Embeddings
# -------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -------------------------
# Vector DB
# -------------------------
vector_db = QdrantVectorStore.from_existing_collection(
    url=os.getenv("QDRANT_URL"),
    collection_name=COLLECTION_NAME,
    embedding=embedding_model,
)

# -------------------------
# LLM
# -------------------------
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="openai/gpt-oss-120b",
    temperature=0
)

# ==================================================
# CORE RAG FUNCTION
# ==================================================
def ask_gita(question: str):
    docs = vector_db.similarity_search(question, k=4)

    if not docs:
        return {
            "answer": "No relevant content found in the Bhagavad Gita.",
            "source": None
        }

    context = "\n\n".join(d.page_content for d in docs)

    pages = sorted({
        d.metadata.get("page") + 1
        for d in docs
        if d.metadata.get("page") is not None
    })

    page_range = f"{pages[0]}–{pages[-1]}" if pages else "N/A"

    system_prompt = f"""
You are a Bhagavad Gita assistant.

Answer ONLY using the provided content
from the Bhagavad Gita English book (TTD edition).
Do NOT use external knowledge or personal interpretation.

If the answer is not found in the text, reply exactly:
"This information is not explicitly stated in the Bhagavad Gita."

Context:
{context}
"""

    response = llm.invoke([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ])

    return {
        "answer": response.content.strip(),
        "source": f"Bhagavad Gita, pages {page_range}"
    }

# ==================================================
# EMOTION-BASED GUIDANCE
# ==================================================
EMOTION_QUERY_MAP = {
    "Anxious": "fear anxiety mental disturbance peace of mind uncertainty",
    "Angry": "anger desire attachment wrath loss of control",
    "Confused": "confusion duty doubt indecision dharma",
    "Sad": "grief sorrow loss impermanence detachment",
    "Peace": "peace equanimity surrender devotion liberation"
}

def ask_gita_by_emotion(emotion: str):
    query = EMOTION_QUERY_MAP.get(emotion)

    if not query:
        return {
            "answer": "Invalid emotion selected.",
            "source": None
        }

    return ask_gita(query)

# ==================================================
# LIFE PHASE-BASED GUIDANCE
# ==================================================
LIFE_PHASE_QUERY_MAP = {
    "Student": "learning discipline self control duty focus growth",
    "Professional": "work responsibility karma yoga excellence detachment results",
    "Leader": "leadership selflessness decision making duty welfare of others",
    "Family": "family responsibility attachment balance compassion sacrifice"
}

def ask_gita_by_life_phase(phase: str):
    query = LIFE_PHASE_QUERY_MAP.get(phase)

    if not query:
        return {
            "answer": "Invalid life phase selected.",
            "source": None
        }

    return ask_gita(query)

# ==================================================
# VERSE OF THE DAY (NEW FEATURE)
# ==================================================
def get_verse_of_the_day():
    """
    Returns the same Bhagavad Gita teaching for the entire day.
    Deterministic + retrieval-based.
    """

    today = datetime.date.today().isoformat()
    random.seed(today)

    daily_queries = [
        "duty without attachment",
        "selfless action karma yoga",
        "peace and equanimity",
        "devotion and surrender",
        "impermanence of life",
        "control of mind and senses"
    ]

    query = random.choice(daily_queries)

    docs = vector_db.similarity_search(query, k=1)

    if not docs:
        return {
            "verse": "No verse found for today.",
            "source": None
        }

    doc = docs[0]
    page = doc.metadata.get("page")
    page_number = page + 1 if page is not None else "N/A"

    system_prompt = f"""
Present the following content as a short
'Verse of the Day' or daily teaching.

Keep it reflective and concise.
Do NOT add external interpretation.

Content:
{doc.page_content}
"""

    response = llm.invoke([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "Verse of the Day"}
    ])

    return {
        "verse": response.content.strip(),
        "source": f"Bhagavad Gita, page {page_number}"
    }
