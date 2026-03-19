import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import base64

st.set_page_config(layout="wide")

# ===== خلفية صورة مهندس =====
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
    background-repeat: no-repeat;
}}

.card {{
    background: rgba(255,255,255,0.85);
    padding: 15px;
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

# ===== عنوان =====
st.markdown("""
<div class="title">
<h1>🏗️ نظام تحليل المكامن النفطي باستخدام الذكاء الاصطناعي</h1>
</div>
""", unsafe_allow_html=True)

st.write("")

# ===== بطاقات الإدخال =====
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='card'><h3>🟢 المسامية</h3></div>", unsafe_allow_html=True)
    porosity = st.number_input("Porosity (%)", value=20.0)

with col2:
    st.markdown("<div class='card'><h3>🔵 النفاذية</h3></div>", unsafe_allow_html=True)
    permeability = st.number_input("Permeability (mD)", value=150.0)

with col3:
    st.markdown("<div class='card'><h3>🟠 العمق</h3></div>", unsafe_allow_html=True)
    depth = st.number_input("Depth (m)", value=3000.0)

with col4:
    st.markdown("<div class='card'><h3>🔴 الضغط</h3></div>", unsafe_allow_html=True)
    pressure = st.number_input("Pressure (psi)", value=2500.0)

st.write("")

# ===== زر الحساب =====
if st.button("🔊 حساب الإنتاج المتوقع"):

    # ===== معادلة بسيطة للإنتاج (مثال) =====
    production = (porosity * permeability) / (depth * 0.1) * (pressure / 1000)

    st.success(f"📈 الإنتاج المتوقع: {production:.2f}")

    # ===== صوت (اختياري بسيط) =====
    st.markdown("""
    <audio autoplay>
        <source src="https://www.soundjay.com/button/sounds/button-3.mp3" type="audio/mpeg">
    </audio>
    """, unsafe_allow_html=True)

    # ===== مخطط برج =====
    heights = [porosity, permeability/10, depth/100, pressure/50]
    labels = ["Porosity", "Permeability", "Depth", "Pressure"]

    fig, ax = plt.subplots()

    x = np.arange(len(labels))
    ax.bar(x, heights)

    ax.set_xticks(x)
    ax.set_xticklabels(labels)

    st.pyplot(fig)
