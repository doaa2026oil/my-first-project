import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
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

.card {{
    background: rgba(255,255,255,0.9);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: black;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}}

.title {{
    background: rgba(0,0,0,0.6);
    color: white;
    padding: 15px;
    border-radius: 15px;
    text-align: center;
}}
</style>
""", unsafe_allow_html=True)

# ===== Title =====
st.markdown("""
<div class="title">
<h1>🏗️ AI-Based Reservoir Analysis System</h1>
</div>
""", unsafe_allow_html=True)

st.write("")

# ===== Inputs =====
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='card'><h3>🟢 Porosity</h3></div>", unsafe_allow_html=True)
    porosity = st.number_input("Porosity (%)", value=25.0)

with col2:
    st.markdown("<div class='card'><h3>🔵 Permeability</h3></div>", unsafe_allow_html=True)
    permeability = st.number_input("Permeability (mD)", value=1000.0)

with col3:
    st.markdown("<div class='card'><h3>🟠 Depth</h3></div>", unsafe_allow_html=True)
    depth = st.number_input("Depth (m)", value=2500.0)

with col4:
    st.markdown("<div class='card'><h3>🔴 Pressure</h3></div>", unsafe_allow_html=True)
    pressure = st.number_input("Pressure (psi)", value=4000.0)

st.write("")

# ===== Calculation =====
if st.button("🔊 Calculate Expected Production"):

    # ===== More realistic model (approximate) =====
    productivity_index = (permeability * porosity) / depth
    production = productivity_index * pressure * 0.8

    # Convert to barrels per day
    production_bpd = production * 50

    # ===== Result Card =====
    st.markdown(f"""
    <div class="card">
        <h2>📈 Expected Production</h2>
        <h1>{production_bpd:,.0f} BPD</h1>
    </div>
    """, unsafe_allow_html=True)

    st.write("")

    # ===== Chart =====
    fig, ax = plt.subplots()

    parameters = ['Porosity', 'Permeability', 'Depth', 'Pressure']
    values = [porosity, permeability, depth, pressure]

    ax.plot(parameters, values, marker='o')
    ax.set_title("Reservoir Parameters Analysis")
    ax.grid()

    st.pyplot(fig)
