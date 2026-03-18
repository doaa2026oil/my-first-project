import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import time

# --- 1. إعدادات الصفحة الفائقة ---
st.set_page_config(
    page_title="AI Reservoir Explorer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. إضافة خلفية متحركة وتنسيق CSS مخصص لإبهار الجمهور ---
# (هذا الكود يضيف تأثيرات بصرية وخلفية داكنة احترافية)
st.markdown("""
<style>
    /* خلفية متدرجة متحركة توحي بالعمق والاحترافية */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(-45deg, #0a0f1e, #1a2a4a, #0d1117, #162238);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* تنسيق البطاقات (الشعلات) */
    .flame-card {
        background: rgba(255, 255, 255, 0.05);
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 15px;
        border: 1px solid rgba(255, 165, 0, 0.2);
        box-shadow: 0 4px 15px rgba(255, 69, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .flame-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(255, 140, 0, 0.3);
        border: 1px solid rgba(255, 165, 0, 0.5);
    }
    .flame-icon {
        font-size: 30px;
        margin-bottom: 10px;
    }
    .flame-1 { color: #ff4500; } /* أحمر ناري */
    .flame-2 { color: #ff8c00; } /* برتقالي غامق */
    .flame-3 { color: #ffa500; } /* برتقالي */
    .flame-4 { color: #ffd700; } /* ذهبي */

    /* تنسيق العناوين والنصوص */
    h1, h2, h3, p {
        color: white !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. العنوان الرئيسي ---
st.markdown("<h1 style='text-align: center;'>🤖 مستكشف المكامن النفطية بالذكاء الاصطناعي</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 1.2em; opacity: 0.8;'>تحليل واكتشاف متقدم باستخدام نماذج التعلم الآلي</p>", unsafe_allow_html=True)
st.markdown("---")

# --- 4. هيكلية الصفحة: قسمين ---
col_inputs, col_results = st.columns([1, 2], gap="large")

# --- 5. قسم المدخلات (محاكاة الشعلات الأربع) ---
with col_inputs:
    st.markdown("### 🔥 محطة إدخال البيانات الحقلية")
    st.write("أدخلي بيانات المكمن بدقة (الأرقام مفتوحة).")

    # الشعلة 1: العمق
    st.markdown('<div class="flame-card"><div class="flame-icon flame-1">🔥</div>', unsafe_allow_html=True)
    depth = st.number_input("العمق (Depth) - قدم", min_value=0.0, value=7500.0, step=100.0, key="depth_in")
    st.markdown('</div>', unsafe_allow_html=True)

    # الشعلة 2: المسامية
    st.markdown('<div class="flame-card"><div class="flame-icon flame-2">🔥</div>', unsafe_allow_html=True)
    porosity = st.number_input("المسامية (Porosity) - %", min_value=0.0, max_value=100.0, value=18.5, key="por_in")
    st.markdown('</div>', unsafe_allow_html=True)

    # الشعلة 3: النفاذية
    st.markdown('<div class="flame-card"><div class="flame-icon flame-3">🔥</div>', unsafe_allow_html=True)
    permeability = st.number_input("النفاذية (Permeability) - mD", min_value=0.0, value=250.0, step=10.0, key="perm_in")
    st.markdown('</div>', unsafe_allow_html=True)

    # الشعلة 4: الضغط
    st.markdown('<div class="flame-card"><div class="flame-icon flame-4">🔥</div>', unsafe_allow_html=True)
    pressure = st.number_input("الضغط (Pressure) - PSI", min_value=0.0, value=3200.0, step=50.0, key="pres_in")
    st.markdown('</div>', unsafe_allow_html=True)

    predict_btn = st.button("بدء تحليل الذكاء الاصطناعي 🧠⚡", use_container_width=True)

# --- 6. قسم النتائج والمخططات والمحاكاة ---
with col_results:
    st.markdown("### 📊 لوحة تحليل وتحكم المكمن")
[3/18/2026 2:32 PM] دعاء عيسى غتر(A), 35: # محاكاة لـ "بئر حقيقي/حقل" ومتحركة
    # سنستخدم صورة احترافية تمثل بئراً ذكياً أو حقلاً رقمياً
    st.image("https://images.unsplash.com/photo-1590480436856-17b51f8a8553?q=80&w=1600", 
             caption="محاكاة رقمية لبئر نفطي ذكي (Holographic Well Simulation)", 
             use_container_width=True)

    if predict_btn:
        with st.spinner('جاري تشغيل نموذج الذكاء الاصطناعي وتحليل الطبقات...'):
            time.sleep(2) # محاكاة وقت التحليل

        # --- 7. عرض النتائج المبهرة ---
        st.success("✅ تم الانتهاء من تحليل المكمن بنجاح!")
        
        # استخدام st.metric لعرض الأرقام الهامة بشكل جذاب
        m_col1, m_col2 = st.columns(2)
        
        # مثال لمعادلة تنبؤ (يجب استبدالها بنموذج الذكاء الاصطناعي الخاص بكِ)
        predicted_bpd = (porosity * permeability * pressure) / (depth * 0.1)
        potential_score = np.clip((predicted_bpd / 500) * 10, 0, 10)
        
        with m_col1:
            st.metric(label="الإنتاج اليومي المتوقع (BPD)", value=f"{predicted_bpd:,.0f} برميل")
        with m_col2:
            st.metric(label="تقييم إمكانات المكمن (AI Score)", value=f"{potential_score:.1f} / 10", help="تقييم جودة المكمن بناءً على الذكاء الاصطناعي")

        # --- 8. المخططات البيانية المتحركة (Plotly) ---
        st.markdown("#### 📈 توزيع الخصائص وعمق المكمن")
        
        # إنشاء بيانات وهمية للمخطط (للتوضيح فقط)
        chart_data = pd.DataFrame({
            'العمق (قدم)': np.linspace(depth-500, depth+500, 100),
            'المسامية %': np.random.normal(porosity, 2, 100),
            'النفاذية mD': np.random.normal(permeability, 20, 100)
        })
        
        # مخطط ثلاثي الأبعاد تفاعلي ومبهر
        fig = px.scatter_3d(chart_data, x='العمق (قدم)', y='المسامية %', z='النفاذية mD',
                            color='المسامية %', title='تحليل فضاء الخصائص ثلاثي الأبعاد',
                            color_continuous_scale='Inferno')
        
        # جعل المخطط يدور تلقائياً (تأثير متحرك)
        fig.update_layout(scene_camera=dict(eye=dict(x=1.5, y=1.5, z=1.5)))
        st.plotly_chart(fig, use_container_width=True)

# --- 9. التذييل ---
st.markdown("---")
st.markdown("<p style='text-align: center; opacity: 0.6;'>مشروع تخرج: استخدام الذكاء الاصطناعي في تحليل المكامن النفطية | 2024</p>", unsafe_allow_html=True)
