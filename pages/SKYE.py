
import streamlit as st
st.set_page_config(page_title="Event Planner AI Chatbot", layout="wide")
st.title("SKYE")
st.markdown("""
Welcome to your AI-powered **Event Planner**!

This chatbot is designed to help you:
- 📅 Plan outdoor events based on upcoming weather
- 🌦️Suggest ideal times or backup days based on forecasts
- 🎉 Offer ideas for weather-appropriate activities

This assistant is aware of your preferred location and upcoming dates. You can ask things like:
- *“Can I host a picnic next Saturday in Seattle?”*
- *“What’s the best day to do an outdoor BBQ this week?”*
---

🔄 **Conversation Window** (AI responses will go here)
""")
col1, col2 = st.columns([1, 2])
with col1:
    st.subheader("📍 Event Details")
    location = st.text_input("Enter City, State", value="Atlanta, GA")
    date = st.date_input("Choose a date for your event")
    time_of_day = st.selectbox("Time of day", ["Morning", "Afternoon", "Evening"])
    activity = st.text_input("Optional: Type of activity (e.g., wedding, hike, sports)")

    st.button("Ask Chatbot")
with col2:
    st.subheader("💬 Chatbot Responses")o
    st.info("The chatbot will analyze your inputs and weather data to give recommendations here.")

