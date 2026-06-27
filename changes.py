import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_data(place: str, forecast_days: int) -> list:
    """
    Fetch weather forecast data for a given location and number of days.

    Args:
        place: City name or location string.
        forecast_days: Number of days to forecast (1–5).

    Returns:
        List of forecast data dicts with temperatures in Celsius.
    """
    if not place or not place.strip():
        raise ValueError("Location cannot be empty.")

    # units=metric tells the API to return temperatures directly in Celsius
    url = f"{BASE_URL}?q={place.strip()}&appid={API_KEY}&units=metric"
    response = requests.get(url, timeout=10)

    if response.status_code == 404:
        raise ValueError(f"Location '{place}' not found. Please check the spelling.")
    elif response.status_code == 401:
        raise PermissionError("Invalid API key. Contact the app administrator.")
    elif response.status_code != 200:
        raise ConnectionError(f"API error {response.status_code}: {response.text}")

    data = response.json()

    if "list" not in data:
        raise ValueError("Unexpected API response format.")

    # 8 data points per day (every 3 hours)
    nr_values = forecast_days * 8
    filtered_data = data["list"][:nr_values]

    # Round temperatures for cleaner display
    for entry in filtered_data:
        entry["main"]["temp"] = round(entry["main"]["temp"], 1)
        entry["main"]["feels_like"] = round(entry["main"].get("feels_like", 0), 1)

    return filtered_data


if __name__ == "__main__":
    results = get_data(place="London", forecast_days=2)
    for r in results[:3]:
        print(r["dt_txt"], r["main"]["temp"], "°C", r["weather"][0]["main"])