
import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Predictably Unpredictable Weather",
    page_icon="🌦️",
    layout="centered"
)

# Title and Description
st.title("🌦️ Predictably Unpredictable Weather App")

st.markdown("""
*Because looking out the window is apparently too mainstream.*

This app uses the magical powers of Python, data, and excessive optimism
to predict the weather for the coming days. Results may vary.
The clouds certainly will.
""")

# User Input
place = st.text_input(
    "📍 Enter a Location",
    placeholder="e.g. Mumbai, London, Gotham City"
)

days = st.slider(
    "📅 Forecast Days",
    min_value=1,
    max_value=5,
    value=3,
    help="How far into the future would you like to gamble?"
)

option = st.selectbox(
    "🔍 What would you like to see?",
    ("Temperature", "Sky Conditions")
)

# Display Selection
if place:
    st.subheader(
        f"📊 {option} Forecast for the Next {days} Day{'s' if days > 1 else ''} in {place}"
    )

    st.info(
        f"Our highly sophisticated algorithms are currently pretending "
        f"to know what the weather in {place} will be."
    )
else:
    st.warning("⚠️ Enter a location so we can begin our scientifically guided guessing.")

# Footer
st.markdown("---")
st.caption(
    "Built with Python, caffeine, and the dangerous assumption that weather "
    "can be predicted. ☕☁️"
)