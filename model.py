
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from changes import get_data

# Page Configuration 
st.set_page_config(
    page_title="Predictably Unpredictable Weather",
    page_icon="🌦️",
    layout="centered",
)

# Custom CSS
st.markdown(
    """
    <style>
        .stApp { background-color: #0f1923; }
        h1 { color: #e2f0fb !important; letter-spacing: -0.5px; }
        h2, h3 { color: #b8d8f0 !important; }
        .stTextInput > label, .stSlider > label, .stSelectbox > label {
            color: #8fb8d8 !important;
            font-weight: 600;
        }
        .metric-card {
            background: linear-gradient(135deg, #1a2e42, #0f1f30);
            border: 1px solid #2a4a62;
            border-radius: 12px;
            padding: 16px 20px;
            text-align: center;
        }
        .metric-label { color: #8fb8d8; font-size: 0.78rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
        .metric-value { color: #e2f0fb; font-size: 1.7rem; font-weight: 700; }
        .metric-sub   { color: #5a8aaa; font-size: 0.8rem; margin-top: 2px; }
        .sky-card {
            background: #1a2e42;
            border: 1px solid #2a4a62;
            border-radius: 10px;
            padding: 10px 6px;
            text-align: center;
        }
        .sky-time { color: #8fb8d8; font-size: 0.7rem; margin-top: 6px; }
        .sky-label { color: #e2f0fb; font-size: 0.75rem; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header 
st.title("🌦️ Predictably Unpredictable")
st.caption(
    "Because looking out the window is apparently too mainstream. "
)
st.markdown("---")

# Inputs
place = st.text_input(
    "📍 Location",
    placeholder="e.g. Mumbai, London, Tokyo",
    value = "Mumbai",
)

col_a, col_b = st.columns(2)
with col_a:
    days = st.slider(
        "📅 Forecast Days",
        min_value=1, max_value=5, value=3,
        help="How far into the future would you like to gamble?",
    )
with col_b:
    option = st.selectbox(
        "🔍 View",
        ("Temperature", "Sky Conditions"),
    )

show_feels_like = False
if option == "Temperature":
    show_feels_like = st.checkbox("Show 'Feels Like' overlay", value=True)

st.caption("Data via OpenWeatherMap · Temperatures in °C")
st.markdown("---")

# Guarding Post
if not place:
    st.info("⬆️ Enter a location above to get started.")
    st.stop()

# Fetch Data with Error Handling 
try:
    with st.spinner(f"Our highly sophisticated algorithms are currently pretending to know what the weather in **{place}** will be…"):
        filtered_data = get_data(place, days)
except ValueError as e:
    st.error(f"❌ {e}")
    st.stop()
except PermissionError as e:
    st.error(f"🔑 {e}")
    st.stop()
except ConnectionError as e:
    st.error(f"🌐 Connection problem: {e}")
    st.stop()
except Exception as e:
    st.error(f"Something went wrong: {e}")
    st.stop()

# Subheader 
day_label = f"{days} day{'s' if days > 1 else ''}"
st.subheader(f"📊 {option} — Next {day_label} in {place.title()}")

# Summary Metrics (always shown)
temps = [entry["main"]["temp"] for entry in filtered_data]
feels = [entry["main"]["feels_like"] for entry in filtered_data]
conditions = [entry["weather"][0]["main"] for entry in filtered_data]

col1, col2, col3, col4 = st.columns(4)

def metric_card(label, value, sub=""):
    return f"""
    <div class="metric-card">
        <div class="metric-label">{label}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-sub">{sub}</div>
    </div>
    """

col1.markdown(metric_card("🌡️ High", f"{max(temps)}°C"), unsafe_allow_html=True)
col2.markdown(metric_card("❄️ Low", f"{min(temps)}°C"), unsafe_allow_html=True)
col3.markdown(metric_card("📊 Avg", f"{round(sum(temps)/len(temps),1)}°C"), unsafe_allow_html=True)
col4.markdown(metric_card("☁️ Dominant", max(set(conditions), key=conditions.count)), unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Temperature View 
if option == "Temperature":
    dates = [entry["dt_txt"] for entry in filtered_data]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=dates, y=temps,
        mode="lines+markers",
        name="Temperature",
        line=dict(color="#4da6e8", width=2.5),
        marker=dict(size=6),
        hovertemplate="%{x|%b %d %H:%M}<br><b>%{y}°C</b><extra></extra>",
    ))

    if show_feels_like:
        fig.add_trace(go.Scatter(
            x=dates, y=feels,
            mode="lines",
            name="Feels Like",
            line=dict(color="#f0a050", width=1.8, dash="dot"),
            hovertemplate="%{x|%b %d %H:%M}<br>Feels like <b>%{y}°C</b><extra></extra>",
        ))

    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,25,36,0.6)",
        font=dict(color="#b8d8f0"),
        legend=dict(bgcolor="rgba(0,0,0,0)", font=dict(color="#b8d8f0")),
        xaxis=dict(
            title="Date & Time",
            gridcolor="#1e3a52",
            tickangle=-35,
            tickfont=dict(size=11),
        ),
        yaxis=dict(
            title="Temperature (°C)",
            gridcolor="#1e3a52",
        ),
        hovermode="x unified",
        margin=dict(l=20, r=20, t=30, b=20),
    )

    st.plotly_chart(fig, use_container_width=True)

# Sky Conditions View 
elif option == "Sky Conditions":
    # Show a bar chart of condition frequency
    from collections import Counter
    counts = Counter(conditions)
    freq_fig = px.bar(
        x=list(counts.keys()),
        y=list(counts.values()),
        labels={"x": "Condition", "y": "Occurrences"},
        color=list(counts.keys()),
        color_discrete_sequence=px.colors.qualitative.Pastel,
    )
    freq_fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(15,25,36,0.6)",
        font=dict(color="#b8d8f0"),
        showlegend=False,
        margin=dict(l=20, r=20, t=20, b=20),
    )
    st.plotly_chart(freq_fig, use_container_width=True)

    # Image grid using OpenWeatherMap CDN icons (icon code already in API response)
    st.markdown("**3-hour snapshots**")
    display_data = filtered_data[:16]
    cols = st.columns(min(8, len(display_data)))
    for i, entry in enumerate(display_data):
        cond = entry["weather"][0]["main"]
        icon_code = entry["weather"][0]["icon"]
        icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"
        time_label = entry["dt_txt"][11:16]
        with cols[i % len(cols)]:
            st.image(icon_url, width=60)
            st.caption(f"{time_label}\n{cond}")

# Footer 
st.markdown("---")
st.caption(
    "Built with Python, caffeine, and the dangerous assumption that weather "
    "can be predicted. ☕☁️"
)