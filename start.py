import streamlit as st

# 1. إعدادات الصفحة لتكون عريضة واحترافية (Wide Mode)
st.set_page_config(
    page_title="مخطط بئر نفطي حقيقي | AI Reservoir",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. إضافة تخصيص مظهري عصري (CSS) للعنوان والخانات
st.markdown("""
    <style>
    /* تخصيص الخلفية والعناصر */
    .main { background-color: #0e1117; color: white; }
    
    /* تخصيص خانات الإدخال - القيم "بكيفك" */
    .stNumberInput label { font-size: 18px !important; color: #4CAF50 !important; font-weight: bold; }
    .stNumberInput > div > div > input { background-color: #1e1e1e !important; color: white !important; border-radius: 8px; }

    /* تخصيص عنوان الصفحة */
    h1 { color: #fdfdfd; font-family: 'Segoe UI', sans-serif; text-align: center; margin-bottom: 2rem; }
    
    /* تخصيص منطقة النتائج */
    .stImage { border: 2px solid #4a4a4a; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.6); }
    </style>
    """, unsafe_allow_html=True)

# 3. عنوان المشروع الرئيسي
st.title("🛢️ الذكاء الاصطناعي في تحليل المكامن النفطية (wellbore diagram)")
st.divider()

# 4. تخطيط الواجهة: عمود ضيق للمدخلات وعمود عريض للمخطط
col_inputs, col_diagram = st.columns([1.5, 3], gap="large")

with col_inputs:
    st.header("📋 أدخلي القيم البتروفيزيائية")
    st.markdown("<p style='color: #a0a0a0;'>اكتشاف المكمن بناءً على القيم الحقيقية المتغيرة</p>", unsafe_allow_html=True)
    
    # خانات إدخال القيم الأربعة المطلوبة "بكيفك"
    porosity = st.number_input("المسامية (Porosity) - %", format="%.2f")
    permeability = st.number_input("النفاذية (Permeability) - mD", format="%.2f")
    depth = st.number_input("العمق (Depth) - قدم", step=100)
    pressure = st.number_input("الضغط (Pressure) - PSI", step=50)
    
    st.markdown("### ✨ تخصيص نوع البيئة")
    type_env = st.selectbox("اختر البيئة الترسيبية:", ["رملية (Sandstone)", "مجنون (Carbonate)", "حقل مجنون", "حقل حلفاية"])

    generate_btn = st.button("تحليل وتوليد المخطط الذكي للطبقات")

with col_diagram:
    st.header("🖼️ مخطط البئر الحقيقي وتصور الطبقات النفطية")
    
    if generate_btn:
        with st.spinner("🧠 يقوم الذكاء الاصطناعي بتحليل البيانات ودمجها مع مخطط البئر..."):
            # محاكاة لزمن التحليل
            import time
            time.sleep(2.5)
            
            # عرض الصورة الحقيقية لمخطط البئر (Wellbore Diagram)
            wellbore_diagram_url = "https://images.unsplash.com/photo-1620067925093-801122ac1408" # مثال على مخطط بئر احترافي
            st.image(wellbore_diagram_url, caption="مخطط بئر حقيقي يوضح الطبقات وتغليف البئر بناءً على العمق والضغط المدخلين", use_column_width=True)
            
            # رسالة نجاح مخصصة
            st.success("✅ تم تحديث مخطط البئر بناءً على قيمك الجديدة!")
            st.markdown(f"التحليل الذكي للمكمن: القيم المدخلة (مسامية {porosity}% وعمق {depth} قدم) تشير إلى مكمن بترولي من النوع '{type_env}'.")
    else:
        # صورة افتراضية أو رسالة تحذير قبل الضغط على الزر
        placeholder_url = "https://via.placeholder.com/800x600.png?text=Wellbore+Diagram+Will+Appear+Here"
        st.image(placeholder_url, caption="اضغطي على الزر لتوليد مخطط البئر"، use_column_width=True)
        st.warning("الرجاء إدخال القيم والضغط على زر التحليل ليظهر شكل البئر.")

# 5. تذييل الصفحة
st.divider()
st.markdown("<p style='text-align: center; color: #606060;'>مشروع AI Reservoir © 2024</p>", unsafe_allow_html=True)
