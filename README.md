# Forecasting the Sky Since Looking Out the Window Was Too Easy ☁️🌦️

Welcome to my Python Weather Prediction App - because trusting meteorologists alone felt far too reasonable.

This project analyzes weather data, crunches numbers, and confidently predicts tomorrow’s forecast with the same energy as someone saying, “I’m pretty sure it won’t rain.”

Powered by Python, machine learning, and a concerning amount of optimism. Sometimes it predicts sunshine, sometimes storms, and occasionally reminds us that nature doesn’t care about our models.

### Results may vary. The clouds certainly do. 🌩️📊

---

## Features

- 📍 Search any city in the world
- 📅 1–5 day forecast with 3-hour resolution
- 🌡️ Temperature line chart with optional "Feels Like" overlay
- ☁️ Sky condition frequency chart + icon grid (via OpenWeatherMap CDN)
- 📊 Summary cards — High, Low, Average, Dominant condition

---

## Project Structure

```
weather-app/
├── model.py               # Streamlit frontend
├── backend.py           # OpenWeatherMap API logic
├── requirements.txt     # Python dependencies
├── .env                 # Your API key (never commit this)
├── .gitignore           # Excludes .env from Git
└── README.md
```

---

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/Rohrschachhh/Forecastor.git
cd Forecastor
```

### 2. Create and activate a virtual environment

```bash
# macOS / Linux
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Get a free OpenWeatherMap API key

1. Go to [https://openweathermap.org](https://openweathermap.org) and create a free account.
2. Navigate to **API Keys** under your profile.
3. Copy your default key (or generate a new one).
4. Note: new keys can take up to 10 minutes to activate.

### 5. Create a `.env` file

In the root of the project, create a file named `.env`:

```
OPENWEATHER_API_KEY=your_api_key_here
```

> ⚠️ Never commit this file. It is already excluded via `.gitignore`.

### 6. Run the app locally

```bash
streamlit run model.py
```

The app will open in your browser at `http://localhost:8501`.

---


## Built With Python, Coffee and my wit to predict Weather nobody asked for ...

- [Streamlit](https://streamlit.io) — UI framework
- [Plotly](https://plotly.com/python/) — Interactive charts
- [OpenWeatherMap API](https://openweathermap.org/api) — Weather data
- [python-dotenv](https://pypi.org/project/python-dotenv/) — Local environment variable management
