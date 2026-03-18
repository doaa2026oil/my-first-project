import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# إعدادات الصفحة
st.set_page_config(page_title="AI Oil Reservoir Analysis", layout="wide")

st.title("🤖 نظام الذكاء الاصطناعي لتحليل واكتشاف المكامن النفطية")
st.markdown("---")

# إنشاء أعمدة للواجهة (الخانات الأربعة)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.subheader("المسامية (Porosity)")
    porosity = st.number_input("أدخل القيمة (%)", min_value=0.0, max_value=100.0, value=25.0, key="por")
    st.info(f"القيمة الحالية: {porosity}%")

with col2:
    st.subheader("النفاذية (Permeability)")
    permeability = st.number_input("أدخل القيمة (mD)", min_value=0.0, value=150.0, key="perm")
    st.success(f"{permeability} mD")

with col3:
    st.subheader("العمق (Depth)")
    depth = st.number_input("أدخل العمق (m)", min_value=0, value=3000, key="dep")
    st.warning(f"{depth} متر")

with col4:
    st.subheader("الضغط (Pressure)")
    pressure = st.number_input("أدخل الضغط (psi)", min_value=0, value=4500, key="pres")
    st.error(f"{pressure} psi")

st.markdown("---")

# منطقة المخطط البياني (محاكاة برج النفط والنتائج)
st.header("📊 مخطط نتائج المكمن (Digital Oil Rig Chart)")

# بناء مخطط تفاعلي يمثل البيانات كطبقات أو هيكل رأسي يشبه البرج
fig = go.Figure()

# تمثيل البيانات بأعمدة ملونة تحاكي هيكل البرج
categories = ['العمق', 'الضغط', 'النفاذية', 'المسامية']
values = [depth/100, pressure/100, permeability/10, porosity] # توحيد مقاييس الرسم

fig.add_trace(go.Bar(
    x=categories,
    y=values,
    text=[f"{depth}m", f"{pressure}psi", f"{permeability}mD", f"{porosity}%"],
    textposition='auto',
    marker_color=['#2c3e50', '#e74c3c', '#27ae60', '#f1c40f'],
    width=[0.4, 0.5, 0.6, 0.7] # تغيير العرض ليعطي شكل هرمي يشبه البرج
))

fig.update_layout(
    title="تمثيل بياني لهيكل المكمن المكتشف",
    yaxis_title="مقياس التحليل النسبي",
    template="plotly_dark",
    height=600
)

st.plotly_chart(fig, use_container_width=True)

# زر تحليل الذكاء الاصطناعي
if st.button("تشغيل تحليل الذكاء الاصطناعي 🚀"):
    st.write("### 🧠 استنتاج النموذج:")
    if porosity > 20 and permeability > 100:
        st.balloons()
        st.success("النتيجة: مكمن نفطي عالي الجودة! ينصح ببدء عمليات الحفر.")
    else:
        st.warning("النتيجة: مكمن متوسط الجودة. يتطلب المزيد من الدراسات الاقتصادية.")
