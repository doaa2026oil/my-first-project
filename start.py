import streamlit as st

# 1. إعداد الصفحة (يجب أن يكون أول سطر)
st.set_page_config(page_title="تحليل المكامن - البرج الذكي", layout="wide")

# 2. كود الـ CSS و HTML للخلفية والشعلات
# سنستخدم رابط الصورة الأصلية الخاصة بكِ كخلفية ثابتة
# وسنضيف الشعلات الأربعة المتحركة في الأعلى

full_design_code = """
<style>
    /* تثبيت الخلفية الأصلية وجعلها واضحة */
    [data-testid="stAppViewContainer"] {
        background-image: url("https://static.streamlit.io/demo/oil_rig.jpg"); /* استبدلي هذا برابط صورتك إذا كان لديكِ رابط مباشر */
        background-size: cover;
        background-position: center;
        background-attachment: fixed; /* الخلفية تبقى ثابتة عند التمرير */
        filter: brightness(100%); /* نضمن أن البرج ليس أسوداً بل واضحاً */
    }

    /* جعل الهيدر شفافاً */
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }

    /* تنسيق النصوص لتكون واضحة فوق الخلفية (بيضاء مع ظل أسود) */
    h1, h2, h3, label, p, .stMarkdown {
        color: white !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.8);
        font-family: 'Cairo', sans-serif; /* اختياري: خط عربي جميل */
    }

    /* حاوية الشعلات الأربعة */
    .flare-container {
        display: flex;
        justify-content: space-around; /* توزيع متساوي */
        align-items: flex-end;
        height: 150px; /* ارتفاع منطقة الشعلات */
        padding-top: 20px;
        width: 100%;
        position: absolute;
        top: 0;
        left: 0;
        z-index: 1000; /* لتبقى فوق كل شيء */
    }

    /* تصميم الشعلة الواحدة */
    .flare {
        width: 40px;
        height: 80px;
        background: linear-gradient(to bottom, #fff8dc, #ffd700, #ff4500); /* تدرج لوني للنار */
        border-radius: 50% 50% 20% 20%;
        box-shadow: 0 0 20px 10px rgba(255, 165, 0, 0.7);
        animation: flicker 0.15s infinite alternate; /* حركة التذبذب */
        filter: blur(1px); /* تأثير ضبابي بسيط للنار */
    }

    /* تعريف حركة التذبذب */
    @keyframes flicker {
        0% { transform: scaleY(1) translateY(0); opacity: 0.9; }
        100% { transform: scaleY(1.1) translateY(-5px); opacity: 1; }
    }
</style>

<div class="flare-container">
    <div class="flare"></div>
    <div class="flare"></div>
    <div class="flare"></div>
    <div class="flare"></div>
</div>
"""

# 3. تنفيذ التصميم وإخفاء النص البرمجي
st.markdown(full_design_code, unsafe_allow_html=True)

# 4. محتوى التطبيق (البيانات)
st.markdown("<h1 style='text-align: center;'>🏗️ مشروع تحليل المكامن - البرج الذكي</h1>", unsafe_allow_html=True)
st.write("---")

# استخدام الأعمدة لتنظيم المدخلات
col1, col2 = st.columns(2)

with col1:
    st.number_input("📏 العمق المستهدف (ft)", value=8000, key="depth")
    st.number_input("🏋️ الضغط المكمني (psi)", value=3500, key="pressure")

with col2:
    st.number_input("💧 نسبة المسامية (%)", value=25, key="porosity")
    st.number_input("🚀 معدل التدفق المتوقع", value=1500, key="flow")

st.write("---")
st.success("🔄 تم تحديث البيانات بنجاح من المكمن.")
