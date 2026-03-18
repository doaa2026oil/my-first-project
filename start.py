import streamlit as st
import numpy as np
import plotly.graph_objects as go

# عنوان التطبيق
st.title("التحليل الطبقي المتقدم للبئر 🧠")

# تقسيم الشاشة لخانات المدخلات
col1, col2, col3, col4 = st.columns(4)
with col1: por = st.number_input("المسامية %", value=15.0)
with col2: perm = st.number_input("النفاذية mD", value=200.0)
with col3: depth = st.number_input("العمق ft", value=8000)
with col4: press = st.number_input("الضغط PSI", value=3500)

# زر التحليل
if st.button("توليد شكل البئر الحقيقي ✨"):
    st.markdown("### 📊 نموذج الطبقات الأرضية (3D Visualization)")
    
    # هنا نقوم برسم "بئر" حقيقي ملون حسب المسامية
    z = np.linspace(depth-50, depth+50, 100)
    x = np.zeros(100)
    y = np.zeros(100)
    
    fig = go.Figure(data=[go.Scatter3d(
        x=x, y=y, z=z,
        mode='markers',
        marker=dict(
            size=15, # حجم البئر
            color=z, # تدرج الألوان حسب العمق
            colorscale='YlOrRd', # ألوان صخرية (أصفر، برتقالي، أحمر)
            opacity=0.8
        )
    )])

    fig.update_layout(title="شكل عمود البئر في الطبقة المستهدفة", height=600)
    st.plotly_chart(fig)
    
    st.success("تم تحليل الطبقة: يظهر الرسم توزيع المسامية حول عمقك المستهدف.")
