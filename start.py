import streamlit as st
import base64

# --- إعدادات الصفحة ---
st.set_page_config(layout="wide", page_title="AI Reservoir Analysis - RoboUI")

# --- دمج صورة الخلفية (Coded in Base64) ---
# ملاحظة: قم بتغيير 'image_1.png' ليكون هو المسار الفعلي لصورتك على جهازك.
# إذا كانت الصورة في نفس مجلد ملف الـ Python، فقط اكتب اسمها.
try:
    with open("image_1.png", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    
    # كود CSS لتعيين الخلفية وتطبيق تأثير الشفافية (Glassmorphism) على البطاقات
    background_and_cards_css = f"""
    <style>
    /* 1. تعيين خلفية الصفحة بالكامل */
    .stApp {{
        background-image: url("data:image/png;base64,{encoded_string}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}

    /* 2. جعل حاويات الـ st.container (البطاقات) شفافة وأنيقة */
    div.stContainer {{
        background-color: rgba(255, 255, 255, 0.4); /* خلفية بيضاء شفافة */
        backdrop-filter: blur(10px); /* تأثير الضبابية خلف البطاقة */
        -webkit-backdrop-filter: blur(10px);
        padding: 20px;
        border-radius: 15px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }}

    /* 3. تنسيق العناوين داخل البطاقات لتكون واضحة */
    div.stContainer h4 {{
        color: #1a5cad !important;
        font-weight: bold;
        margin-bottom: 15px;
        border-bottom: 2px solid rgba(26, 92, 173, 0.5);
        padding-bottom: 5px;
    }}

    /* 4. تنسيق مربعات الإدخال لتندمج مع التصميم */
    div.stNumberInput input {{
        background-color: rgba(255, 255, 255, 0.8) !important;
        border-radius: 8px !important;
    }}

    /* 5. تنسيق عنوان الصفحة الرئيسي */
    h1.main-title {{
        text-align: center;
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);
        padding: 20px 0;
    }}
    </style>
    """
    st.markdown(background_and_cards_css, unsafe_allow_html=True)

except FileNotFoundError:
    st.error("⚠️ لم يتم العثور على ملف الصورة باسم 'image_1.png'. تأكد من وجوده في نفس المجلد أو قم بتعديل المسار في الكود.")
    st.stop() # إيقاف التنفيذ إذا لم يتم العثور على الصورة


# --- عنوان التطبيق الرئيسي ---
st.markdown("<h1 class='main-title'>🤖 منصة التحليل الذكي للمكامن النفطية</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# --- تنظيم المدخلات كبطاقات شفافة (الواجهة الرئيسية) ---

# الصف الأول: البطاقات الأساسية (المسامية والنفاذية)
col_p, col_k = st.columns(2, gap="large")

with col_p:
    with st.container():
        # تصميم بطاقة "المسامية"
        st.markdown("<h4>🔵 بطاقة المسامية (Porosity)</h4>", unsafe_allow_html=True)
        # حقل الإدخال الفعلي
        porosity = st.number_input(
            "أدخل قيمة المسامية (%)", 
            min_value=0.0, 
            max_value=100.0, 
            value=15.0,
            step=0.1,
            key="porosity_input",
            help="نسبة الفراغات في الصخر"
        )

with col_k:
    with st.container():
        # تصميم بطاقة "النفاذية"
        st.markdown("<h4>🟢 بطاقة النفاذية (Permeability)</h4>", unsafe_allow_html=True)
        # حقل الإدخال الفعلي
        permeability = st.number_input(
            "أدخل قيمة النفاذية (mD)", 
            min_value=0.0, 
            value=150.0,
            key="permeability_input",
            help="قدرة الصخر على تمرير الموائع"
        )


# الصف الثاني: البطاقات الثانوية (العمق والضغط)
col_d, col_pr = st.columns(2, gap="large")

with col_d:
    with st.container():
        # تصميم بطاقة "العمق"
        st.markdown("<h4>📏 بطاقة العمق (Depth)</h4>", unsafe_allow_html=True)
        depth_m = st.number_input(
            "أدخل عمق الطبقة (m)", 
            value=2500,
            key="depth_input"
        )
[3/18/2026 4:29 PM] دعاء عيسى غتر(A), 35: with col_pr:
    with st.container():
        # تصميم بطاقة "الضغط"
        st.markdown("<h4>⛽ بطاقة الضغط (Pressure)</h4>", unsafe_allow_html=True)
        pressure_psi = st.number_input(
            "أدخل ضغط المكمن (psi)", 
            value=4500,
            key="pressure_input"
        )

# --- زر التشغيل في الأسفل ---
st.markdown("---")
submit_col1, submit_col2, submit_col3 = st.columns([1, 1, 1])
with submit_col2:
    submit_btn = st.button("🚀 تشغيل تحليل الذكاء الاصطناعي", use_container_width=True)

# --- قسم النتائج (افتراضي) ---
if submit_btn:
    st.markdown("---")
    st.subheader("💡 نتائج التحليل الذكي:")
    with st.container(): # وضع النتائج داخل بطاقة شفافة أيضاً
        results_col1, results_col2 = st.columns(2)
        with results_col1:
            st.info("جاري تحليل البيانات باستخدام النماذج المتقدمة...")
            # هنا ستضيف الكود الخاص بالتحليل
        with results_col2:
            # مثال لعرض قيمة نهائية بأسلوب Metric
            final_score = (porosity * 0.4) + (permeability / 100 * 0.6) # معادلة بسيطة للمثال
            st.metric(label="تقييم المكمن الإجمالي", value=f"{final_score:.1f}", delta="جيد جداً")
else:
    with st.container():
        st.info("بانتظار إدخال البيانات والضغط على زر التشغيل...")
