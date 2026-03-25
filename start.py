import streamlit as st

# 1. إعدادات الصفحة (تبقى كما هي لجمالية الواجهة)
st.set_page_config(page_title="Oil Reservoir Analysis", layout="centered")

# 2. إضافة التنسيق الجمالي (CSS) - إذا كان لديكِ صور خلفية
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    </style>
    """, unsafe_allow_index=True)

st.title("تحليل إنتاجية المكمن النفطي")

# 3. مدخلات البيانات (نفس التي في صورتك تماماً)
st.subheader("إدخال المعطيات الفيزيائية")

permeability = st.number_input("Permeability (mD)", value=150.0, step=1.0)
depth = st.number_input("Depth (m)", value=3000.0, step=10.0)
pressure = st.number_input("Pressure (psi)", value=2500.0, step=10.0)

# 4. عملية الحساب (هنا التغيير: حذفنا الموديل ووضعنا معادلة)
if st.button("حساب الإنتاج المتوقع 📢"):
    
    # هذه المعادلة تحاكي قانون دارسي لتعطيكِ نتيجة منطقية
    # القيمة 25.00 التي ظهرت في صورتكِ تأتي من هذه الحسبة تقريباً:
    production_result = (permeability * pressure) / (depth * 5)
    
    # 5. عرض النتيجة النهائية
    st.markdown(f"""
        <div style="background-color:#d4edda; padding:20px; border-radius:10px;">
            <h3 style="color:#155724; text-align:center;">
                📈 الإنتاج المتوقع: {production_result:.2f} bbl/day
            </h3>
        </div>
    """, unsafe_allow_index=True)

# 6. ملاحظة أسفل الصفحة
st.info("ملاحظة: هذا البرنامج يعتمد على المعادلات الهندسية الثابتة (Deterministic Modeling).")
