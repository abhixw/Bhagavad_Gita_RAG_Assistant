from PIL import Image
import streamlit as st
import requests

API_BASE = "http://127.0.0.1:8000"

# --------------------
# Page config
# --------------------
st.set_page_config(
    page_title="Bhagavad Gita Assistant",
    page_icon="🕉️",
    layout="centered"
)

# --------------------
# Sidebar: UI Mode Toggle
# --------------------
st.sidebar.title("🕉️ Bhagavad Gita Assistant")

ui_mode = st.sidebar.radio(
    "🌓 UI Mode",
    ["🌞 Light", "🌙 Dark", "🕯️ Meditation"]
)

mode = st.sidebar.radio(
    "Choose mode",
    [
        "🌅 Verse of the Day",
        "❓ Ask a Question",
        "⚖️ Compare Teachings",
        "💭 Emotion-Based Guidance",
        "🧭 Life Phase Guidance"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("_Timeless wisdom for modern life_")

# --------------------
# Dynamic Theme Settings
# --------------------
if ui_mode == "🌞 Light":
    bg_color = "#FFF8F0"
    text_color = "#8B4513"
    card_bg = "white"

elif ui_mode == "🌙 Dark":
    bg_color = "#121212"
    text_color = "#FFFFFF"   # 👈 WHITE TEXT
    card_bg = "#1E1E1E"

else:  # 🕯️ Meditation
    bg_color = "#020617"
    text_color = "#E5E7EB"   # 👈 SOFT WHITE
    card_bg = "#020617"

# --------------------
# Global UI Styling (FIXED)
# --------------------
st.markdown(f"""
<style>
/* App background */
.stApp {{
    background-color: {bg_color};
    color: {text_color};
}}

/* Force text color everywhere */
body, p, span, div, li {{
    color: {text_color} !important;
}}

/* Headings */
h1, h2, h3 {{
    color: {text_color};
}}

/* Cards */
.card {{
    background-color: {card_bg};
    padding: 20px;
    border-radius: 15px;
    margin-top: 10px;
    color: {text_color};  /* 👈 CARD TEXT FIX */
}}

/* Confidence-Aware Styling */
.card-high {{
    border: 2px solid #4CAF50;
    box-shadow: 0 0 15px rgba(76, 175, 80, 0.6);
}}
.card-medium {{
    border: 2px solid #FFC107;
    box-shadow: 0 0 12px rgba(255, 193, 7, 0.6);
}}
.card-low {{
    border: 2px solid #F44336;
    box-shadow: 0 0 12px rgba(244, 67, 54, 0.6);
}}

/* Sidebar */
section[data-testid="stSidebar"] {{
    background-color: #2C2C54;
}}
section[data-testid="stSidebar"] * {{
    color: white !important;
}}

/* Buttons */
div.stButton > button {{
    background-color: #FF9800;
    color: white;
    border-radius: 10px;
    padding: 0.5em 1.2em;
    font-weight: bold;
}}
div.stButton > button:hover {{
    background-color: #F57C00;
}}
</style>
""", unsafe_allow_html=True)

# --------------------
# Hero Image (hide in meditation mode)
# --------------------
if ui_mode != "🕯️ Meditation":
    hero_image = Image.open("assets/krishna_arjuna.jpeg")
    st.image(hero_image, use_container_width=True)
    st.markdown("<hr style='border:1px solid #FF9800;'>", unsafe_allow_html=True)

# --------------------
# Main Title
# --------------------
st.title("🕉️ Bhagavad Gita Assistant")

# --------------------
# Helper: confidence-aware card
# --------------------
def render_confident_card(content, confidence):
    if confidence > 80:
        card_class = "card card-high"
        note = "🟢 High confidence"
    elif confidence >= 50:
        card_class = "card card-medium"
        note = "🟡 Medium confidence — verify context"
    else:
        card_class = "card card-low"
        note = "🔴 Low confidence — answer may be incomplete"

    st.markdown(
        f"<div class='{card_class}'>{content}</div>",
        unsafe_allow_html=True
    )
    st.caption(note)
    st.progress(confidence / 100)
    st.caption(f"Confidence: {confidence}%")

    if ui_mode == "🕯️ Meditation":
        st.markdown(
            "<p style='text-align:center; font-style:italic; opacity:0.75;'>"
            "Take a moment to reflect on this teaching."
            "</p>",
            unsafe_allow_html=True
        )

# ==================================================
# MODE 0: VERSE OF THE DAY
# ==================================================
if mode == "🌅 Verse of the Day":
    st.subheader("🌅 Verse of the Day")

    with st.spinner("Reflecting on today’s teaching…"):
        response = requests.get(f"{API_BASE}/verse-of-the-day")

        if response.status_code == 200:
            data = response.json()
            render_confident_card(
                data.get("verse"),
                data.get("confidence", 0)
            )
        else:
            st.error("Backend error.")

# ==================================================
# MODE 1: QUESTION ANSWERING
# ==================================================
elif mode == "❓ Ask a Question":
    st.subheader("Ask a question from the Bhagavad Gita")

    question = st.text_input("Your question:", placeholder="What is karma yoga?")

    if st.button("🔍 Ask") and question.strip():
        with st.spinner("Searching the Bhagavad Gita…"):
            response = requests.post(
                f"{API_BASE}/ask",
                json={"question": question}
            )

            if response.status_code == 200:
                data = response.json()
                render_confident_card(
                    data.get("answer"),
                    data.get("confidence", 0)
                )
            else:
                st.error("Backend error.")

# ==================================================
# MODE 2: WISDOM COMPARISON
# ==================================================
elif mode == "⚖️ Compare Teachings":
    st.subheader("⚖️ Compare Bhagavad Gita Teachings")

    col_input1, col_input2 = st.columns(2)

    with col_input1:
        topic1 = st.text_input("📘 Left Topic", placeholder="Duty")

    with col_input2:
        topic2 = st.text_input("📕 Right Topic", placeholder="Desire")

    if st.button("🔍 Compare") and topic1 and topic2:
        with st.spinner("Comparing wisdom…"):
            response = requests.post(
                f"{API_BASE}/compare",
                json={"topic1": topic1, "topic2": topic2}
            )

            if response.status_code == 200:
                data = response.json()
                col1, col2 = st.columns(2)

                with col1:
                    st.markdown(f"### 📘 {topic1}")
                    render_confident_card(
                        data["left"]["answer"],
                        data["left"]["confidence"]
                    )

                with col2:
                    st.markdown(f"### 📕 {topic2}")
                    render_confident_card(
                        data["right"]["answer"],
                        data["right"]["confidence"]
                    )
            else:
                st.error("Backend error during comparison.")

# ==================================================
# MODE 3: EMOTION GUIDANCE
# ==================================================
elif mode == "💭 Emotion-Based Guidance":
    st.subheader("How are you feeling today?")

    emotion = st.radio(
        "",
        ["😟 Anxious", "😠 Angry", "😕 Confused", "😔 Sad", "😌 Peace"],
        horizontal=True
    )

    if st.button("✨ Get Guidance"):
        emotion_key = emotion.split(" ")[1]

        with st.spinner("Finding relevant guidance…"):
            response = requests.post(
                f"{API_BASE}/emotion",
                json={"emotion": emotion_key}
            )

            if response.status_code == 200:
                data = response.json()
                render_confident_card(
                    data.get("answer"),
                    data.get("confidence", 0)
                )
            else:
                st.error("Backend error.")

# ==================================================
# MODE 4: LIFE PHASE GUIDANCE
# ==================================================
elif mode == "🧭 Life Phase Guidance":
    st.subheader("Select your current life phase")

    phase = st.radio(
        "",
        ["🎓 Student", "💼 Professional", "🧑‍💼 Leader", "🏠 Family"],
        horizontal=True
    )

    if st.button("🌟 Get Guidance"):
        phase_key = phase.split(" ")[1]

        with st.spinner("Finding relevant teachings…"):
            response = requests.post(
                f"{API_BASE}/life-phase",
                json={"phase": phase_key}
            )

            if response.status_code == 200:
                data = response.json()
                render_confident_card(
                    data.get("answer"),
                    data.get("confidence", 0)
                )
            else:
                st.error("Backend error.")

# --------------------
# Footer
# --------------------
st.markdown("""
<hr>
<p style="text-align:center; color:gray;">
🕉️ Built with Explainable AI & RAG
</p>
""", unsafe_allow_html=True)




