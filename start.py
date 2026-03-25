import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# 1. إعداد الصفحة (نفس تصميمكِ المميز)
st.set_page_config(page_title="نظام تحليل المكامن النفطية", layout="wide")

# 2. التنسيق (CSS) مع صورتكِ الخاصة
st.markdown(
    """
    <style>
    [data-testid="stApp"] {
        background-image: url("your_image.jpg"); /* ضعي اسم ملف صورتكِ هنا */
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    
    .main-card {
        background-color: rgba(0, 0, 0, 0.75);
        border-radius: 20px;
        padding: 30px;
        color: white;
        text-align: center;
        border: 1px solid rgba(255,255,255,0.1);
        margin-bottom: 20px;
    }
    
    .result-box {
        background-color: rgba(26, 74, 122, 0.9);
        padding: 20px;
        border-radius: 10px;
        color: white;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin-top: 10px;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# 3. العنوان (بدون أي ذكر للمشين ليرنك)
st.markdown('<div class="main-card"><h1>🏗️ نظام تحليل المكامن: معادلة دارسي</h1></div>', unsafe_allow_html=True)

# 4. مدخلات البيانات في أعمدة (كما في لقطة الشاشة)
with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("إدخال الخصائص الفيزيائية للمكمن")
        k = st.number_input("🔵 النفاذية (Permeability - Darcy)", value=0.1, step=0.01)
        A = st.number_input("📐 مساحة المقطع (Area - ft²)", value=100.0, step=1.0)
        dp_input = st.number_input("📉 فرق الضغط (Pressure Drop - psi)", value=500.0, step=10.0)
        
    with col2:
        st.subheader("إدخال خصائص السائل والأبعاد")
        mu = st.number_input("💧 اللزوجة (Viscosity - cp)", value=2.0, step=0.1)
        L = st.number_input("📏 طول المكمن (Length - ft)", value=1000.0, step=1.0)

# --- الحساب الرياضي ورسم البياني ---

# حساب نقطة واحدة بناءً على مدخلات المستخدم
if mu != 0 and L != 0:
    flow_rate_single = (k * A * dp_input) / (mu * L)
    
    st.markdown(f"""
    <div class="result-box">
        معدل التدفق الناتج (Q) بناءً على مدخلاتك هو: <br>
        {flow_rate_single:.4f} bbl/day
    </div>
    """, unsafe_allow_html=True)
    
    # عرض المعادلة بشكل رياضي أنيق
    st.latex(r"Q = \frac{k \cdot A \cdot \Delta P}{\mu \cdot L}")
    
    # --- إضافة الرسم البياني التفاعلي ---
    st.write("---")
    st.subheader("📊 تحليل حساسية التدفق لفرق الضغط")
    
    # إنشاء بيانات للرسم البياني (تغيير فرق الضغط من 0 إلى 1000 psi)
    dp_values = np.linspace(0, 1000, 50)
    flow_rates = (k * A * dp_values) / (mu * L)
    
    # تجميع البيانات في Pandas DataFrame
    df = pd.DataFrame({
        'فرق الضغط (Pressure Drop - psi)': dp_values,
        'معدل التدفق (Flow Rate - bbl/day)': flow_rates
    })
    
    # رسم بياني تفاعلي باستخدام Plotly
    fig = px.line(df, 
                  x='فرق الضغط (Pressure Drop - psi)', 
                  y='معدل التدفق (Flow Rate - bbl/day)', 
                  title='تأثير فرق الضغط على معدل تدفق النفط',
                  markers=True, # إضافة نقاط على الخط لتسهيل القراءة
                  template="plotly_dark" # خلفية داكنة لتناسب تصميمك
                 )
    
    # تنسيق الرسم البياني ليكون أجمل
    fig.update_layout(
        title_font_size=20,
        xaxis_title="فرق الضغط (ΔP) - psi",
        yaxis_title="معدل التدفق (Q) - bbl/day",
        font_family="Arial",
        xaxis_gridcolor='rgba(255,255,255,0.1)',
        yaxis_gridcolor='rgba(255,255,255,0.1)'
    )
    
    # عرض الرسم البياني في Streamlit
    st.plotly_chart(fig, use_container_width=True)

else:
    st.error("تأكد من أن اللزوجة والطول لا يساويان صفراً!")
