
import streamlit as st
import plotly.express as px
from backend import get_data

# Title and Description import the data from the User Input
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ", placeholder="Enter a location (e.g. London, New York)")

days = st.slider("Forecast Days",
    min_value=1, max_value=5,
    help="Select the number of forecasted days"
)

option = st.selectbox("Select data to view", ("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} day in {place}")

# Get the data from the backend
filtered_data = get_data(place, days)

if option == "Temperature":
    dates = [dict['dt_txt'] for dict in filtered_data]
    temperatures = [dict['main']['temp'] for dict in filtered_data]
    # Create a Temperature Forecast Plot
    figure = px.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': "Temperature (°C)"}, title=f"{option} Forecast for {place}")
    st.plotly_chart(figure)

if option == "Sky":
    images = { 
        "Clear": "Images/clear.png",
        "Clouds": "Images/clouds.png",
        "Rain": "Images/rain.png",
        "Snow": "Images/snow.png",
        "Thunderstorm": "Images/thunderstorm.png",
        "Drizzle": "Images/drizzle.png",
        "Mist": "Images/mist.png"
    }
    sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
    images_to_display = [images[condition] for condition in sky_conditions]
    # Create a Sky Forecast Plot
    st.image(images_to_display, width=100, caption=sky_conditions)


# import streamlit as st

# # Page Configuration
# st.set_page_config(
#     page_title="Predictably Unpredictable Weather",
#     page_icon="🌦️",
#     layout="centered"
# )

# # Title and Description
# st.title("🌦️ Predictably Unpredictable Weather App")

# st.markdown("""
# *Because looking out the window is apparently too mainstream.*

# This app uses the magical powers of Python, data, and excessive optimism
# to predict the weather for the coming days. Results may vary.
# The clouds certainly will.
# """)

# # User Input
# place = st.text_input(
#     "📍 Enter a Location",
#     placeholder="e.g. Mumbai, London, Gotham City"
# )

# days = st.slider(
#     "📅 Forecast Days",
#     min_value=1,
#     max_value=5,
#     value=3,
#     help="How far into the future would you like to gamble?"
# )

# option = st.selectbox(
#     "🔍 What would you like to see?",
#     ("Temperature", "Sky Conditions")
# )

# # Display Selection
# if place:
#     st.subheader(
#         f"📊 {option} Forecast for the Next {days} Day{'s' if days > 1 else ''} in {place}"
#     )

#     st.info(
#         f"Our highly sophisticated algorithms are currently pretending "
#         f"to know what the weather in {place} will be."
#     )
# else:
#     st.warning("⚠️ Enter a location so we can begin our scientifically guided guessing.")

# # Footer
# st.markdown("---")
# st.caption(
#     "Built with Python, caffeine, and the dangerous assumption that weather "
#     "can be predicted. ☕☁️"
# )