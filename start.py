import streamlit as st
import base64

# 1. إعدادات المتصفح والخلفية الثابتة
st.set_page_config(page_title="تحليل المكامن - البرج الذكي", layout="wide")

def set_bg():
    try:
        with open("background.png", "rb") as f:
            data = base64.b64encode(f.read()).decode()
        st.markdown(f"""
            <style>
            .stApp {{
                background: url(data:image/png;base64,{data});
                background-size: cover;
                background-attachment: fixed;
            }}
            </style>
            """, unsafe_allow_html=True)
    except: pass

set_bg()

# 2. الواجهة الرئيسية (نفس ترتيبك المفضل)
st.title("🏗️ نظام تحليل المكامن التفاعلي")

col_input, col_rig = st.columns([1, 1.5])

with col_input:
    st.subheader("📝 إدخال البيانات")
    depth = st.number_input("📏 العمق (ft)", value=8000)
    pressure = st.number_input("🏋️ الضغط (psi)", value=3500)
    porosity = st.number_input("💧 المسامية (%)", value=25.0)
    permeability = st.number_input("🏎️ النفاذية (mD)", value=150)
    
    if st.button("🚀 تشغيل البرج والتحليل"):
        show_analysis = True
    else:
        show_analysis = False

# 3. البرج التفاعلي (الاحترافي)
with col_rig:
    if show_analysis:
        # حسابات ارتفاع الشعلات بناءً على القيم
        h1 = min(pressure/60, 100)
        h2 = min(porosity*3, 100)
        h3 = min(permeability/2, 100)
        h4 = 60 # العمق شعلة مستقرة

        rig_design = f"""
        <div style="background: rgba(0,0,0,0.6); border: 2px solid #ce93d8; border-radius: 20px; padding: 25px; text-align: center;">
            <h2 style="color: #e1bee7;">المخطط النهائي: برج الإنتاج</h2>
            <div style="display: flex; justify-content: space-around; align-items: flex-end; height: 350px; border-bottom: 4px solid #fff; margin: 20px 0;">
                
                <div style="text-align: center;">
                    <div style="height: {h1}px; width: 40px; background: linear-gradient(#ff5252, #ffb74d); border-radius: 50% 50% 0 0; animation: pulse 1s infinite alternate;"></div>
                    <p style="color: white; font-weight: bold;">الضغط</p>
                </div>

                <div style="text-align: center;">
                    <div style="height: {h2}px; width: 40px; background: linear-gradient(#42a5f5, #e3f2fd); border-radius: 50% 50% 0 0; animation: pulse 1.2s infinite alternate;"></div>
                    <p style="color: white; font-weight: bold;">المسامية</p>
                </div>

                <div style="text-align: center;">
                    <div style="height: {h3}px; width: 40px; background: linear-gradient(#66bb6a, #c8e6c9); border-radius: 50% 50% 0 0; animation: pulse 0.8s infinite alternate;"></div>
                    <p style="color: white; font-weight: bold;">النفاذية</p>
                </div>

                <div style="text-align: center;">
                    <div style="height: {h4}px; width: 40px; background: linear-gradient(#ab47bc, #f3e5f5); border-radius: 50% 50% 0 0; animation: pulse 1.5s infinite alternate;"></div>
                    <p style="color: white; font-weight: bold;">العمق</p>
                </div>
            </div>

            <style>
                @keyframes pulse {{ from {{ transform: scaleY(1); opacity: 0.8; }} to {{ transform: scaleY(1.3); opacity: 1; }} }}
            </style>

            <div style="background: rgba(255,255,255,0.1); padding: 15px; border-radius: 10px; color: white; text-align: right;">
                <b>🔍 تحليل القيم:</b> بناءً على المدخلات، المكمن عند عمق {depth} قدم يمتلك خصائص تدفق جيدة جداً، 
                والشعلات المرتفعة تشير إلى إمكانية إنتاج مستدامة بفضل الضغط ({pressure} psi).
            </div>
        </div>
        """
        st.markdown(rig_design, unsafe_allow_html=True)
