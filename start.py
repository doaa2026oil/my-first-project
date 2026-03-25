import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydeck as pdk
import base64

st.set_page_config(layout="wide")

# ===== Background =====
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_base64 = get_base64_of_bin_file("background.png")

st.markdown(f"""
<style>
.stApp {{
    background-image: url("data:image/png;base64,{img_base64}");
    background-size: cover;
    background-position: center;
}}

.title {{
    background: rgba(0,0,0,0.6);
    color: white;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
}}

.card {{
    background: rgba(255,255,255,0.9);
    padding: 15px;
    border-radius: 15px;
    text-align: center;
    color: black;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}}

.result {{
    background: rgba(255,255,255,0.95);
    color: black;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
    box-shadow: 0 4px 10px rgba(0,0,0,0.5);
}}
</style>
""", unsafe_allow_html=True)

# ===== Title =====
st.markdown("""
<div class="title">
<h1>🏗️ Oil Field Intelligent Dashboard</h1>
</div>
""", unsafe_allow_html=True)

# ===== Sidebar Controls =====
st.sidebar.title("⚙️ Control Panel")

porosity = st.sidebar.slider("Porosity (%)", 5.0, 35.0, 20.0)
permeability = st.sidebar.slider("Permeability (mD)", 50.0, 500.0, 150.0)
pressure = st.sidebar.slider("Pressure (psi)", 1000.0, 5000.0, 2500.0)
temperature = st.sidebar.slider("Temperature (°C)", 50.0, 150.0, 90.0)
depth = st.sidebar.slider("Depth (m)", 1000.0, 5000.0, 3000.0)

fluid_type = "Oil"

# ===== Production Calculation =====
h = 50
B = 1.2
mu = max(0.5, 2 - (temperature / 100))
re_rw = 100

production = 0.00708 * (permeability * h * pressure) / (mu * B * np.log(re_rw))
production = production * (porosity / 100)

# ===== KPIs =====
st.markdown("## 📊 Field KPIs")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Production", f"{production:.0f} bbl/day")
col2.metric("Pressure", f"{pressure} psi")
col3.metric("Temperature", f"{temperature} °C")
col4.metric("Fluid", fluid_type)

# ===== Layout =====
left, right = st.columns([2, 1])

# ===== Map Data =====
data = pd.DataFrame({
    'lat': [30.5, 30.6, 30.55, 30.52],
    'lon': [47.8, 47.9, 47.85, 47.82],
    'production': [1200, 900, 1500, 1100],
    'pressure': [2500, 2300, 2700, 2400]
})

layer = pdk.Layer(
    "ScatterplotLayer",
    data=data,
    get_position='[lon, lat]',
    get_radius='pressure * 2',
    get_fill_color='[production / 5, 100, 150]',
    pickable=True
)

view_state = pdk.ViewState(
    latitude=30.55,
    longitude=47.85,
    zoom=10
)

# ===== Left: Map =====
with left:
    st.markdown("### 🗺️ Oil Field Map")

    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "Production: {production} bbl/day\nPressure: {pressure} psi"}
    ))

# ===== Right: Charts =====
with right:
    st.markdown("### 📈 Production Analysis")

    fig, ax = plt.subplots()
    ax.bar(["Production"], [production])
    st.pyplot(fig)

# ===== Result Display =====
st.markdown(f"""
<div class="result">
Estimated Oil Production: {production:.2f} barrels/day
</div>
""", unsafe_allow_html=True)

# ===== Sound =====
st.markdown("""
<audio autoplay>
    <source src="https://www.soundjay.com/button/sounds/button-3.mp3" type="audio/mpeg">
</audio>
""", unsafe_allow_html=True)
