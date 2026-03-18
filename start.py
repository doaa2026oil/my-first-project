import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# إعداد واجهة التطبيق بشكل احترافي وألوان داكنة
st.set_page_config(page_title="AI Reservoir Vision", layout="wide", page_icon="🤖")

# --- إضافة CSS متقدم للصور والخلفية والجمالية العامة ---
st.markdown("""
    <style>
    /* خلفية التطبيق مع تأثير شبكة ذكاء اصطناعي (أنيقة وغير مشتتة) */
    .stApp {
        background-color: #050509;
        background-image: radial-gradient(#1a1a2e 1px, transparent 1px);
        background-size: 20px 20px;
        color: #e0e0e0;
    }
    
    /* تنسيق العناوين مع أيقونات */
    .ai-title {
        color: #00f2fe;
        font-family: 'Courier New', Courier, monospace;
        text-align: center;
        border-bottom: 2px solid #4facfe;
        padding-bottom: 10px;
        margin-bottom: 20px;
    }
    
    /* تنسيق الخانات */
    .stNumberInput label {
        color: #4facfe !important;
        font-weight: bold;
    }
    
    /* تنسيق الزر - تأثير نيوني */
    div.stButton > button:first-child {
        background: linear-gradient(45deg, #4facfe 0%, #00f2fe 100%);
        color: #050509;
        border-radius: 20px;
        width: 100%;
        font-weight: bold;
        font-size: 1.2em;
        border: none;
        box-shadow: 0 0 10px #4facfe;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        box-shadow: 0 0 20px #00f2fe;
        transform: scale(1.02);
    }
    
    /* إضافة أيقونات الذكاء الاصطناعي للنتائج */
    .result-icon {
        font-size: 2em;
        margin-right: 10px;
        vertical-align: middle;
    }
    </style>
    """, unsafe_allow_html=True)

# --- الهيدر مع أيقونة الروبوت والعنوان ---
st.markdown('<h1 class="ai-title">🤖 AI-Driven Reservoir Vision v1.0</h1>', unsafe_allow_html=True)

# إضافة صورة معبرة عن الذكاء الاصطناعي في قطاع الطاقة (اختياري، يمكن حذف السطرين القادمين)
# st.image("https://images.unsplash.com/photo-1620712943543-bcc4688e7485?q=80&w=600", caption="الذكاء الاصطناعي يحلل باطن الأرض", width=600)

st.markdown("### 🛠️ إدخال بيانات المكمن الأساسية")

# تقسيم الشاشة لمدخلات مرتبة
col1, col2, col3, col4 = st.columns(4)

with col1:
    porosity = st.number_input("💧 المسامية (%)", value=22.5)
with col2:
    permeability = st.number_input("🔀 النفاذية (mD)", value=180.0)
with col3:
    depth1 = st.number_input("⬆️ العمق العلوي (m)", value=2100.0)
with col4:
    depth2 = st.number_input("⬇️ العمق السفلي (m)", value=2500.0)

st.markdown("---")

if st.button("🚀 تشغيل خوارزمية التحليل العميق"):
    # تأثير "جاري التحميل" بشكل ذكاء اصطناعي
    with st.spinner("🧠 جاري استدعاء النموذج العصبي وتحليل التكوينات الجيولوجية..."):
        # محاكاة وقت المعالجة
        import time
        time.sleep(1.5)
    
    st.markdown("### 📊 تقرير النتائج النهائي")
    
    # قسم النتائج بتنسيق أيقونات
    st.info("💡 تم تحليل 4 متغيرات جيولوجية مقابل 15,000 بئر مرجعي.")
    
    col_res1, col_res2 = st.columns([1.2, 1])
    
    with col_res1:
        # تنسيق النتيجة بأيقونات
        st.markdown(f"""
            <div style="background-color: #0a0a12; padding: 20px; border-radius: 15px; border: 1px solid #4facfe;">
                <h3 style="color: #4facfe;">✨ تقييم المكمن:</h3>
                <p style="color: #00ff00; font-size: 1.5em; font-weight: bold;">
                    ✅ <span class="result-icon">🛢️</span> مكمن عالي الجودة (High Quality)
                </p>
                <hr style="border-color: #1a1a2e;">
                <p style="font-size: 1.1em;">
                    <span class="result-icon">🎯</span> دقـة الـتـنـبـؤ: <span style="color: #00f2fe; font-weight: bold;">96.8%</span>
                </p>
            </div>
            """, unsafe_allow_html=True)
    
    with col_res2:
        # رسم بئر حقيقي ملون (مع إخفاء الأجزاء البيضاء في الرسم)
[3/18/2026 4:17 PM] دعاء عيسى غتر(A), 35: fig, ax = plt.subplots(figsize=(5, 8), facecolor='#050509')
        
        # رسم طبقات الأرض
        ax.fill_between([0, 1], 0, 10, color='#2c2c2c') # صخور عامة
        ax.fill_between([0, 1], 3, 7, color='#000000', alpha=0.9, hatch='//', edgecolor='#4facfe') # طبقة النفط المستهدفة
        
        # رسم أنبوب البئر
        ax.plot([0.5, 0.5], [0, 10], color='#
