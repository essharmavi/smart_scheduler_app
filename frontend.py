import streamlit as st
import requests as rq

st.set_page_config(page_title="Smart Scheduler AI", page_icon="🧠", layout="centered")

st.title("🧠 Smart Scheduler AI")
st.markdown(
    """
    *Plan your study sessions around your chosen learning topics — get tailored videos, readings, and projects to boost your skills.*
    """
)

# Mood input
mood = st.selectbox(
    "How's your energy today?",
    ["🚀 Super pumped!", "🙂 Feeling okay", "😴 Low energy"],
    index=None
)

# Study hours input
study_hours = st.selectbox(
    "How many hours can you dedicate to studying today?",
    ["⏱️ 1–2 hours", "⏰ 2–3 hours", "📚 3–5 hours", "🔥 5+ hours"],
    index=None
)

# Busyness input
busyness = st.selectbox(
    "How busy is your day?",
    ["📈 Extremely busy", "📅 Busy", "🔄 Moderate", "🌴 Light"],
    index=None
)

# New: Learning topic input
learning_topics = st.multiselect(
    "What do you want to focus on learning? (Select one or more)",
    [
        "Machine Learning",
        "Deep Learning",
        "MLOps",
        "LangChain",
        "Data Science",
        "Python Programming",
        "Generative AI",
        "Other"
    ],
    help="Pick your upskilling focus areas for tailored content."
)

# Handle "Other" option
custom_topic = None
if "Other" in learning_topics:
    custom_topic = st.text_input(
        label="Enter other topics you want to learn (comma-separated):",
        placeholder="Example: Langraph, MCP Servers, C++ etc"
    )
    if custom_topic:
        other_topics = [t.strip() for t in custom_topic.split(",") if t.strip()]
        # Remove 'Other' and add custom topics
        learning_topics = [t for t in learning_topics if t != "Other"] + other_topics

# Proceed only if at least one topic selected
if learning_topics:
    topics_str = ", ".join(learning_topics)
else:
    topics_str = None


# Daily schedule input
daily_schedule = st.text_area(
    "What's your plan for today?",
    placeholder="- Morning routine\n- Work / study\n- Gym / walk\n- Reading / learning\n- Relax / leisure\n- Sleep"
)

if all([mood, study_hours, busyness, topics_str]) and daily_schedule.strip():
    if st.button("Generate My Study Plan"):
        payload = {
            "mood": mood,
            "study_time": study_hours,
            "busyness": busyness,
            "learning_topic": topics_str,
            "daily_schedule": daily_schedule
        }
        with st.spinner("Building your personalized study plan..."):
            response = rq.post("http://127.0.0.1:8000/generate-schedule/", json=payload)
            if response.status_code == 200:
                st.markdown("### Your Personalized Study Plan 📘")
                st.write(response.json()["plan"])
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
else:
    st.info("Please fill out all fields to generate your study plan.")
