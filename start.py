[3/18/2026 12:27 PM] دعاء عيسى غتر(A), 35: بعد ودر
[3/18/2026 12:27 PM] dfg يوسف: ووةةةاا
[3/18/2026 12:27 PM] dfg يوسف: عغغغغغغغقققغ
[3/18/2026 12:27 PM] dfg يوسف: ٢سسسصصثثلل
[3/18/2026 12:28 PM] dfg يوسف: 6treeeerggr
[3/18/2026 12:28 PM] dfg يوسف: tzzkuzzztttrrr
[3/18/2026 12:47 PM] dfg يوسف: الو
[3/18/2026 12:50 PM] dfg يوسف: الو
[3/18/2026 12:51 PM] dfg يوسف: الو
[3/18/2026 1:15 PM] دعاء عيسى غتر(A), 35: import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# إعدادات الصفحة
st.set_page_config(page_title="AI Reservoir Explorer", layout="wide")

# العنوان باللغتين
st.title("🛢️ AI Reservoir Vision & Analysis")
st.subheader("تحليل المكمن وتوليد المخطط الطبقي الرقمي")

# --- القائمة الجانبية للمدخلات ---
st.sidebar.header("📊 مدخلات بيانات البئر (Well Inputs)")
depth = st.sidebar.number_input("العمق (Depth - ft)", min_value=1000, max_value=15000, value=5000)
porosity = st.sidebar.slider("المسامية (Porosity %)", 0, 40, 15)
permeability = st.sidebar.number_input("النفاذية (Permeability - mD)", 0.1, 5000.0, 150.0)
pressure = st.sidebar.number_input("الضغط (Pressure - psi)", 500, 10000, 3000)

# --- محرك التحليل (الذكاء الاصطناعي البسيط) ---
def analyze_reservoir(phi, k):
    # معادلة افتراضية لتقييم الجودة
    score = (phi * 0.6) + (np.log10(k) * 10)
    if score > 25: return "High Potential (مكمن واعد جداً)", "green"
    elif score > 15: return "Medium Potential (مكمن متوسط)", "orange"
    else: return "Low Potential (إنتاجية منخفضة)", "red"

result, color = analyze_reservoir(porosity, permeability)

# --- عرض النتائج في مربعات احترافية ---
col1, col2, col3, col4 = st.columns(4)
col1.metric("العمق المختبر", f"{depth} ft")
col2.metric("المسامية", f"{porosity}%")
col3.metric("النفاذية", f"{permeability} mD")
col4.metric("الضغط", f"{pressure} psi")

st.markdown(f"### 🤖 تقييم الذكاء الاصطناعي: <span style='color:{color}'>{result}</span>", unsafe_allow_html=True)

# --- رسم مخطط البئر (Well Log Plot) ---
st.markdown("---")
st.subheader("📉 المخطط الطبقي واللوغاريتمي للبئر")

# توليد بيانات عشوائية حول نقطة العمق المختارة لإظهارها في الرسم
depth_range = np.linspace(depth-100, depth+100, 50)
poro_curve = np.random.normal(porosity, 2, 50)

fig = go.Figure()

# إضافة منحنى المسامية
fig.add_trace(go.Scatter(x=poro_curve, y=depth_range, name="Porosity Log",
                         line=dict(color='blue', width=2)))

# إضافة شكل يمثل طبقة الزيت/المكمن
fig.add_hrect(y0=depth-10, y1=depth+10, fillcolor="yellow", opacity=0.3, 
              annotation_text="Target Zone (المنطقة المستهدفة)", annotation_position="top left")

fig.update_layout(
    title="Well Profile Simulation",
    xaxis_title="Porosity (%)",
    yaxis_title="Depth (ft)",
    yaxis=dict(autorange="reversed"), # عكس المحور ليظهر العمق للأسفل
    template="plotly_dark",
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# زر لتحميل البيانات كتقرير
st.download_button("تحميل بيانات التحليل (CSV)", 
                   pd.DataFrame([{"Depth":depth, "Porosity":porosity, "Perm":permeability, "Pressure":pressure}]).to_csv(),
                   "well_report.csv")
