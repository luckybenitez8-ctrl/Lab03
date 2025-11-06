
import streamlit as st
from datetime import date

st.set_page_config(page_title="Event Planner AI Chatbot", layout="wide")

st.title("🎯 Smart Event Planner Chatbot (LLM Style)")

st.markdown("""
Welcome to your interactive event planning assistant powered by AI! 🧠

Ask anything like:
- *"Can I plan an outdoor birthday party this Saturday in San Diego?"*
- *"What day next week is best for a wedding in Atlanta?"*
- *"Suggest an activity for a rainy Thursday in Seattle."*
""")

# Sidebar for context inputs (not used in response here)
with st.sidebar:
    st.subheader("📍 Event Context")
    location = st.text_input("Enter City, State", value="Atlanta, GA")
    preferred_date = st.date_input("Target Date", value=date.today())
    time_of_day = st.selectbox("Time of day", ["Morning", "Afternoon", "Evening"])
    activity = st.text_input("Optional: Type of activity", placeholder="e.g., picnic, hike, wedding")

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
prompt = st.chat_input("Ask the AI event planner...")

if prompt:
    # Display user input
    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt, "avatar": "👤"})

    # Fixed response
    response = "Hi, I'm SKY — your helpful AI assistant for planning around the weather!"

    # Display fixed assistant reply
    with st.chat_message("assistant", avatar="🤖"):
        st.markdown(response)
    st.session_state.chat_history.append({"role": "assistant", "content": response, "avatar": "🤖"})

# Replay chat history on refresh
for message in st.session_state.chat_history:
    with st.chat_message(message["role"], avatar=message.get("avatar", None)):
        st.markdown(message["content"])
