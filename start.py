import streamlit as st

st.set_page_config(layout="wide")

# ===== خلفية مهندس =====
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1581090700227-1e8b5d0b6f65");
    background-size: cover;
    background-position: center;
}

/* كارد رئيسي */
.main {
    background-color: rgba(0,0,0,0.75);
    padding: 30px;
    border-radius: 20px;
    color: white;
}

/* البطاقات */
.card {
    background-color: rgba(20,20,20,0.9);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    color: white;
    box-shadow: 0 0 10px rgba(255,0,0,0.5);
}

/* البرج */
.tower {
    font-size: 80px;
}
.flame {
    font-size: 40px;
    color: orange;
}
</style>
""", unsafe_allow_html=True)

# ===== العنوان =====
st.markdown("""
<div class="main">
<h1>🏗️ منصة البرج الذكي لتحليل المكامن</h1>
<p>تحليل الإنتاج باستخدام الذكاء الاصطناعي</p>
</div>
""", unsafe_allow_html=True)

st.write("")

# ===== إدخال القيم داخل بطاقات =====
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='card'>المسامية</div>", unsafe_allow_html=True)
    porosity = st.number_input(" ", value=25)

with col2:
    st.markdown("<div class='card'>النفاذية</div>", unsafe_allow_html=True)
    permeability = st.number_input("  ", value=150)

with col3:
    st.markdown("<div class='card'>العمق</div>", unsafe_allow_html=True)
    depth = st.number_input("   ", value=8000)

with col4:
    st.markdown("<div class='card'>الضغط</div>", unsafe_allow_html=True)
    pressure = st.number_input("    ", value=3500)

# ===== حساب الإنتاج =====
production = (porosity * 2) + (permeability / 10) + (pressure / 100) - (depth / 1000)

# ===== عرض الإنتاج =====
st.markdown(f"""
<div class="main">
<h2>📊 الإنتاج المتوقع</h2>
<h1>{production:.2f}</h1>
</div>
""", unsafe_allow_html=True)

# ===== مخطط البرج (تمثيل بصري) =====
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.markdown("<div class='tower'>🏗️</div>", unsafe_allow_html=True)

# عدد الشعلات حسب الإنتاج
flares = int(min(4, max(1, production / 30)))

flame_display = "🔥" * flares

st.markdown(f"<div class='flame'>{flame_display}</div>", unsafe_allow_html=True)

st.markdown("<p>عدد الشعلات يمثل مستوى الإنتاج</p>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
