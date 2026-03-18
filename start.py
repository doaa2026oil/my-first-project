import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import base64

# --- إعدادات الصفحة ---
st.set_page_config(page_title="تحليل المكمن بالذكاء الاصطناعي", layout="wide")

# --- وظيفة لإضافة الخلفية من ملفك background.png (اختياري، يمكنك إزالتها إذا أردت خلفية بيضاء) ---
def add_bg_from_local(image_file):
    try:
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
        )
    except FileNotFoundError:
        pass # إذا لم توجد الخلفية، اتركها بيضاء

# استدعاء الخلفية (تأكد أن الاسم مطابق لملفك في GitHub)
add_bg_from_local('background.png')

# --- تنسيقات البطاقات الملونة (لتظهر بشكل احترافي) ---
st.markdown("""
<style>
    .stMetric {
        background-color: rgba(255, 255, 255, 0.95); /* خلفية بيضاء شبه معتمة */
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #ff4b4b; /* لون الحافة */
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .stMetric label {
        font-weight: bold;
        color: #333;
    }
</style>
""", unsafe_allow_html=True)

st.title("🛢️ تحليل المكمن بالذكاء الاصطناعي")
st.markdown("---")

# --- مدخلات البيانات في الشريط الجانبي (كما هي) ---
st.sidebar.header("📥 إدخال قيم المكمن")
st.sidebar.markdown("قم بتحريك المؤشرات لرؤية التغيير في المخطط.")
porosity = st.sidebar.slider("المسامية (%)", 5.0, 40.0, 15.0, step=0.1)
permeability = st.sidebar.slider("النفاذية (mD)", 10.0, 1000.0, 150.0, step=1.0)
water_sat = st.sidebar.slider("تشبع الماء (%)", 10.0, 90.0, 30.0, step=0.1)
thickness = st.sidebar.slider("السمك (ft)", 10.0, 500.0, 100.0, step=1.0)

# --- حساب الإنتاج المتوقع (معادلة تجريبية) ---
production = (porosity * permeability * (100 - water_sat) * thickness) / 10000

# --- عرض البطاقات الأربعة الملونة ---
st.subheader("📊 المؤشرات الرئيسية للمكمن")
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("المسامية (Porosity)", f"{porosity}%")
with col2:
    st.metric("النفاذية (Permeability)", f"{permeability}")
with col3:
    st.metric("تشبع الماء (Sw)", f"{water_sat}%")
with col4:
    st.metric("الإنتاج المتوقع (Production)", f"{int(production)} bpd", delta=f"{int(production*0.05)} bpd (خطأ تقديري)")

st.markdown("---")

# ==========================================
# --- المخطط الهندي: رسم البرج والشعلات التفاعلية ---
# ==========================================

st.subheader("🏗️ مخطط البرج والشعلات الهندسي (تفاعلي)")

# إنشاء مخطط Plotly فارغ
fig = go.Figure()

# 1. رسم هيكل البرج هندسياً (باستخدام إحداثيات X, Y)
# رسم القاعدة
fig.add_trace(go.Scatter(
    x=[0, 1, 1.5, 0.5, 0], 
    y=[0, 0, 1, 1, 0], 
    fill="toself", 
    fillcolor='rgba(100, 100, 100, 0.5)', # لون رمادي شبه شفاف
    line=dict(color='black', width=2),
    name="القاعدة",
    hoverinfo='skip'
))

# رسم البرج العمودي الرئيسي
fig.add_trace(go.Scatter(
    x=[0.4, 0.6, 0.6, 0.4, 0.4], 
    y=[1, 1, 8, 8, 1], 
    fill="toself", 
    fillcolor='rgba(150, 150, 150, 0.7)', # لون رمادي أغمق
    line=dict(color='black', width=2),
    name="البرج الرئيسي",
    hoverinfo='skip'
))

# رسم قمة البرج (حيث تخرج الشعلات)
fig.add_trace(go.Scatter(
    x=[0.35, 0.65, 0.65, 0.35, 0.35], 
    y=[8, 8, 8.5, 8.5, 8], 
    fill="toself", 
    fillcolor='rgba(50, 50, 50, 0.9)', # لون قريب من الأسود
    line=dict(color='black', width=2),
    name="القمة",
    hoverinfo='skip'
))

# 2. تحديد أماكن الشعلات الأربعة (X, Y) فوق قمة البرج المرسوم
flame_x = [0.4, 0.47, 0.53, 0.6] # أماكن أفقية فوق القمة
flame_y = [8.7, 8.7, 8.7, 8.7] # مكان عمودي واحد فوق القمة
# 3. إضافة الشعلات الأربعة التفاعلية (كأنها نقاط على المخطط)
# شعلة المسامية (أحمر)، النفاذية (برتقالي)، تشبع (أصفر)، سمك (ذهبي)
# حجم الشعلة (Size) يعتمد مباشرة على القيمة المدخلة
flame_values = [porosity * 2, permeability / 10, water_sat * 1.5, thickness / 3]
flame_colors = ['#e74c3c', '#e67e22', '#f1c40f', '#d35400']
flame_labels = ['مسامية', 'نفاذية', 'تشبع الماء', 'سمك المكمن']

for i in range(4):
    # إضافة الشعلة الرئيسية (القلب)
    fig.add_trace(go.Scatter(
        x=[flame_x[i]], 
        y=[flame_y[i]],
        mode='markers',
        marker=dict(
            size=flame_values[i], # حجم متغير!
            color=flame_colors[i],
            symbol='diamond', # شكل يشبه الشعلة
            opacity=0.9,
            line=dict(color='white', width=1)
        ),
        name=flame_labels[i],
        text=f"{flame_labels[i]}: {int(flame_values[i])}",
        hoverinfo='text'
    ))
    
    # إضافة تأثير الوهج حول الشعلة
    fig.add_trace(go.Scatter(
        x=[flame_x[i]], 
        y=[flame_y[i]],
        mode='markers',
        marker=dict(size=flame_values[i] * 1.6, color=flame_colors[i], opacity=0.3, hoverinfo='skip'),
        showlegend=False
    ))

# تحسين مظهر المخطط العام وإخفاء المحاور
fig.update_layout(
    height=700, # زيادة الارتفاع ليتناسب مع البرج العمودي
    margin=dict(l=10, r=10, t=10, b=10),
    xaxis=dict(visible=False, range=[-0.5, 2]), # إخفاء المحور X وتحديد النطاق
    yaxis=dict(visible=False, range=[-0.5, 10]), # إخفاء المحور Y وتحديد النطاق
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)

# عرض المخطط التفاعلي في Streamlit
st.plotly_chart(fig, use_container_width=True)

# تذييل الصفحة
st.markdown("---")
st.caption("تطوير: فريق هندسة المكامن الرقمية | هذا النموذج يستخدم معادلات محاكاة لأغراض العرض فقط.")
