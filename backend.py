from fastapi import FastAPI
from pydantic import BaseModel
from rag_engine import (
    ask_gita,
    ask_gita_by_emotion,
    ask_gita_by_life_phase,
    get_verse_of_the_day
)

app = FastAPI(title="Bhagavad Gita RAG API")

# -------------------------
# Request Schemas
# -------------------------
class QuestionRequest(BaseModel):
    question: str

class EmotionRequest(BaseModel):
    emotion: str

class LifePhaseRequest(BaseModel):
    phase: str

# 🆕 Compare Request Schema
class CompareRequest(BaseModel):
    topic1: str
    topic2: str

# -------------------------
# Health Check
# -------------------------
@app.get("/")
def root():
    return {"message": "Bhagavad Gita RAG API is running"}

# -------------------------
# Verse of the Day
# -------------------------
@app.get("/verse-of-the-day")
def verse_of_the_day():
    """
    Returns today's Bhagavad Gita teaching
    along with confidence and provenance.
    """
    return get_verse_of_the_day()

# -------------------------
# Normal Question-Based RAG
# -------------------------
@app.post("/ask")
def ask_question(payload: QuestionRequest):
    """
    Ask a direct question from the Bhagavad Gita.
    Returns:
    - answer
    - confidence score
    - provenance (page-level sources)
    """
    return ask_gita(payload.question)

# -------------------------
# Emotion-Based Guidance
# -------------------------
@app.post("/emotion")
def ask_by_emotion(payload: EmotionRequest):
    """
    Get guidance based on emotional state.
    Example emotions:
    - Anxious
    - Angry
    - Confused
    - Sad
    - Peace
    """
    return ask_gita_by_emotion(payload.emotion)

# -------------------------
# Life Phase-Based Guidance
# -------------------------
@app.post("/life-phase")
def ask_by_life_phase(payload: LifePhaseRequest):
    """
    Get guidance based on life phase.
    Example phases:
    - Student
    - Professional
    - Leader
    - Family
    """
    return ask_gita_by_life_phase(payload.phase)

# -------------------------
# 🆕 Wisdom Comparison Mode
# -------------------------
@app.post("/compare")
def compare_wisdom(payload: CompareRequest):
    """
    Compare two Bhagavad Gita concepts side-by-side.
    Returns answers, confidence scores, and provenance
    for both topics using the same RAG pipeline.
    """
    left_result = ask_gita(payload.topic1)
    right_result = ask_gita(payload.topic2)

    return {
        "left": left_result,
        "right": right_result
    }
