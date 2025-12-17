from fastapi import FastAPI
from pydantic import BaseModel
from rag_engine import (
    ask_gita,
    ask_gita_by_emotion,
    ask_gita_by_life_phase,
    get_verse_of_the_day   # ✅ NEW IMPORT
)

app = FastAPI(title="Bhagavad Gita RAG API")

# -------------------------
# Request Schemas
# -------------------------
class Question(BaseModel):
    question: str

# -------------------------
# Health Check
# -------------------------
@app.get("/")
def root():
    return {"message": "Bhagavad Gita RAG API is running"}

# -------------------------
# Verse of the Day (NEW)
# -------------------------
@app.get("/verse-of-the-day")
def verse_of_the_day():
    """
    Returns today's Bhagavad Gita teaching.
    Same verse for the entire day.
    """
    return get_verse_of_the_day()

# -------------------------
# Normal Question-Based RAG
# -------------------------
@app.post("/ask")
def ask(question: Question):
    """
    Ask a direct question from the Bhagavad Gita.
    """
    return ask_gita(question.question)

# -------------------------
# Emotion-Based Guidance
# -------------------------
@app.post("/emotion")
def ask_by_emotion(emotion: str):
    """
    Get guidance based on emotional state.
    Example emotions: Anxious, Angry, Confused, Sad, Peace
    """
    return ask_gita_by_emotion(emotion)

# -------------------------
# Life Phase-Based Guidance
# -------------------------
@app.post("/life-phase")
def ask_by_life_phase(phase: str):
    """
    Get guidance based on life phase.
    Example phases: Student, Professional, Leader, Family
    """
    return ask_gita_by_life_phase(phase)
