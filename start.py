import streamlit as st

# 1. إعدادات الصفحة
st.set_page_config(layout="wide")

# 2. منطقة إدخال البيانات (لتحكم المهندس)
st.sidebar.markdown("### 🛠️ مدخلات المهندس الذكي")
depth = st.sidebar.number_input("العمق (ft)", value=8000, step=100)
porosity = st.sidebar.number_input("المسامية (%)", value=25, min_value=1, max_value=40)
pressure = st.sidebar.number_input("الضغط (psi)", value=3500, step=50)

# 3. حساب حالة الشعلات (منطق ذكي بسيط)
# سنقوم بحساب "نسبة كفاءة" إجمالية للمكمن بناءً على القيم المدخلة
efficiency_score = (porosity * 2) + (pressure / 100) - (depth / 1000)

# عدد الشعلات الفعالة بناءً على الكفاءة (من 1 إلى 4)
num_active_flares = int(min(4, max(1, efficiency_score / 20)))

# شدة حركة الشعلة (الـ blur والسرعة)
flicker_speed = 0.1 if efficiency_score > 50 else 0.3
flicker_blur = 3 if efficiency_score > 50 else 7 # الشعلة تكون أكثر وضوحاً عند الكفاءة العالية

# 4. تصميم الواجهة (CSS لإنشاء المخطط المتحرك)
# لاحظ أننا نستخدم متغيرات بايثون (مثل flicker_speed) داخل كود الـ CSS
flare_style = f"""
    width: 20px;
    height: 30px;
    background: gold; /* اللون الأساسي للنار */
    border-radius: 10px 10px 0 0;
    margin: 0 5px;
    filter: blur({flicker_blur}px);
    animation: flicker {flicker_speed}s infinite alternate;
    opacity: 1; /* الشعلة مضاءة */
"""

# تصميم الشعلة المنطفئة
flare_off_style = """
    width: 20px;
    height: 30px;
    background: #444; /* لون رمادي داكن للشعلة المنطفئة */
    border-radius: 10px 10px 0 0;
    margin: 0 5px;
    filter: blur(2px);
    opacity: 0.5;
"""

st.markdown(f"""
<style>
    /* تصميم البطاقة الرئيسية (مثل الصورة المرسلة) */
    .smart-rig-card {{
        background: radial-gradient(circle at top, #333 0%, #1a1a1a 100%);
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        color: white;
        border: 2px solid rgba(255, 120, 120, 0.3); /* حافة برتقالية خفيفة */
        max-width: 400px;
        margin: auto;
    }}

    /* تصميم الشعلات */
    .flare-container {{
        display: flex;
        justify-content: center;
        margin-bottom: 15px;
    }}

    @keyframes flicker {{
        0% {{ transform: scaleY(1) rotate(-1deg); opacity: 0.8; }}
        100% {{ transform: scaleY(1.3) rotate(1deg); opacity: 1; }}
    }}

    /* تصميم نصوص البطاقة */
    .title-ar {{ font-family: 'Cairo', sans-serif; font-size: 22px; margin-top: 15px; }}
    .title-en {{ font-family: 'Segoe UI', sans-serif; font-size: 14px; color: #ccc; margin-top: 5px; opacity: 0.8; }}

</style>
""", unsafe_allow_html=True)

# 5. عرض البطاقة التفاعلية
col1, col2 = st.columns([1, 1])

with col1:
    # إنشاء قائمة بأنماط الشعلات (مضاءة أو منطفئة)
    flares_html = ""
    for i in range(4):
        if i < num_active_flares:
            flares_html += f'<div style="{flare_style}"></div>'
        else:
            flares_html += f'<div style="{flare_off_style}"></div>'

    # بناء البطاقة بالكامل
    st.markdown(f"""
    <div class="smart-rig-card">
        <div class="flare-container">
            {flares_html}
        </div>
        <img src="https://img.icons8.com/emoji/96/000000/crane.png" width="80" alt="Oil Rig">
        <div class="title-ar">منصة البرج الذكي لتحليل المكامن</div>
        <div class="title-en">University of Basrah - Petroleum Engineering</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"### 🤖 تحليل المهندس الذكي (تأثير الكتابة)")
    
    # تحويل حالة الشعلات إلى نص وصفي
    if num_active_flares == 4:
        status_text = "المكمن في قمة نشاطه وكفاءته!"
    elif num_active_flares == 3:
        status_text = "المكمن يعمل بشكل جيد ومعدل إنتاج مستقر."
    elif num_active_flares == 2:
        status_text = "تنبيه: تم رصد انخفاض في الكفاءة. يرجى مراقبة الضغط والمسامية."
    else:
        status_text = "تحذير: كفاءة المكمن منخفضة جداً. الشعلات بالكاد تعمل."

    if st.button("عرض حالة الشعلة الرابعة"):
        with st.empty():
            for i in range(len(status_text)+1):
                st.info(f"🎤 {status_text[:i]}")
                time.sleep(0.04)
