from PIL import Image
import streamlit as st
import requests

# --------------------
# Page config
# --------------------
st.set_page_config(
    page_title="Bhagavad Gita Assistant",
    page_icon="🕉️",
    layout="centered"
)

# --------------------
# Global UI Styling
# --------------------
st.markdown("""
<style>
.stApp {
    background-color: #FFF8F0;
}
h1, h2, h3 {
    color: #8B4513;
}
section[data-testid="stSidebar"] {
    background-color: #2C2C54;
}
section[data-testid="stSidebar"] * {
    color: white;
}
div.stButton > button {
    background-color: #FF9800;
    color: white;
    border-radius: 10px;
    padding: 0.5em 1.2em;
    font-weight: bold;
}
div.stButton > button:hover {
    background-color: #F57C00;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# --------------------
# Hero Image
# --------------------
hero_image = Image.open("assets/krishna_arjuna.jpeg")
st.image(hero_image, use_container_width=True)

st.markdown("<hr style='border:1px solid #FF9800;'>", unsafe_allow_html=True)

# --------------------
# Sidebar Navigation
# --------------------
st.sidebar.title("🕉️ Bhagavad Gita Assistant")

mode = st.sidebar.radio(
    "Choose mode",
    [
        "🌅 Verse of the Day",
        "❓ Ask a Question",
        "💭 Emotion-Based Guidance",
        "🧭 Life Phase Guidance"
    ]
)

st.sidebar.markdown("---")
st.sidebar.markdown("_Timeless wisdom for modern life_")

# --------------------
# Main Title
# --------------------
st.title("🕉️ Bhagavad Gita Assistant")
st.markdown(
    "<p style='color:#FF9800;'></p>",
    unsafe_allow_html=True
)

# ==================================================
# MODE 0: VERSE OF THE DAY
# ==================================================
if mode == "🌅 Verse of the Day":
    st.subheader("🌅 Verse of the Day")

    with st.spinner("Reflecting on today’s teaching from the Gita…"):
        response = requests.get("http://127.0.0.1:8000/verse-of-the-day")

        if response.status_code == 200:
            data = response.json()

            st.markdown(f"""
            <div class="card">
                {data.get("verse", "No verse available.")}
            </div>
            """, unsafe_allow_html=True)

            if data.get("source"):
                st.info(data["source"])
        else:
            st.error("Backend error. Please try again.")

# ==================================================
# MODE 1: QUESTION ANSWERING
# ==================================================
elif mode == "❓ Ask a Question":
    st.subheader("Ask a question from the Bhagavad Gita")

    question = st.text_input("Your question:", placeholder="What is karma yoga?")

    if st.button("🔍 Ask") and question.strip():
        with st.spinner("Searching the Bhagavad Gita…"):
            response = requests.post(
                "http://127.0.0.1:8000/ask",
                json={"question": question}
            )

            if response.status_code == 200:
                data = response.json()

                st.markdown("### 📜 Answer")
                st.markdown(f"""
                <div class="card">
                    {data.get("answer", "No answer returned.")}
                </div>
                """, unsafe_allow_html=True)

                if data.get("source"):
                    st.info(data["source"])
            else:
                st.error("Backend error.")

# ==================================================
# MODE 2: EMOTION GUIDANCE
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
                "http://127.0.0.1:8000/emotion",
                params={"emotion": emotion_key}
            )

            if response.status_code == 200:
                data = response.json()

                st.markdown(f"""
                <div class="card">
                    {data.get("answer", "No guidance returned.")}
                </div>
                """, unsafe_allow_html=True)

                if data.get("source"):
                    with st.expander("📖 Source"):
                        st.write(data["source"])
            else:
                st.error("Backend error.")

# ==================================================
# MODE 3: LIFE PHASE GUIDANCE
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
                "http://127.0.0.1:8000/life-phase",
                params={"phase": phase_key}
            )

            if response.status_code == 200:
                data = response.json()

                st.markdown(f"""
                <div class="card">
                    {data.get("answer", "No guidance returned.")}
                </div>
                """, unsafe_allow_html=True)

                if data.get("source"):
                    with st.expander("📖 Source"):
                        st.write(data["source"])
            else:
                st.error("Backend error.")

# --------------------
# Footer
# --------------------
st.markdown("""
<hr>
<p style="text-align:center; color:gray;">
<br>

</p>
""", unsafe_allow_html=True)
