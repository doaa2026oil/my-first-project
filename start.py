import streamlit as st
import numpy as np
import plotly.graph_objects as go
from PIL import Image
import requests
from io import BytesIO

# --- 1. إعداد الصفحة والعنوان ---
st.set_page_config(page_title="AI-Driven Reservoir Prediction", layout="wide", page_icon="🤖")

st.title("🤖 اكتشاف وتحليل المكامن النفطية باستخدام الذكاء الاصطناعي")
st.subheader("بناء نماذج طبقية وتحليل الخواص الفيزيائية للآبار")
st.markdown("---")

# --- 2. واجهة مدخلات الذكاء الاصطناعي ---
st.sidebar.markdown("# 🔧 لوحة تحكم النموذج (AI-Inputs)")
st.sidebar.markdown("أدخل البيانات الأساسية للمكمن:")

# تعريف المدخلات بطريقة مباشرة
por = st.sidebar.number_input("المسامية (Porosity %)", value=15.0, min_value=0.0, max_value=100.0, help="نسبة المسام في الصخر")
perm = st.sidebar.number_input("النفاذية (Permeability mD)", value=200.0, help="قدرة الصخر على تمرير السوائل")
depth1 = st.sidebar.number_input("العمق الأول (ft) - Top", value=8000.0, help="بداية المكمن")
depth2 = st.sidebar.number_input("العمق الثاني (ft) - Bottom", value=8200.0, help="نهاية المكمن")

# زر التشغيل في القائمة الجانبية
run_ai = st.sidebar.button("تشغيل خوارزمية AI", type="primary")

# --- 3. محاكاة تحليل الذكاء الاصطناعي ---
if run_ai:
    with st.spinner('جاري تشغيل خوارزمية الذكاء الاصطناعي على البيانات...'):
        import time
        time.sleep(2) # محاكاة وقت التحليل
    
    st.success("تم الانتهاء من تحليل الذكاء الاصطناعي بنجاح!")
    
    # محاكاة نتائج AI بناءً على الشروط الهندسية
    reservoir_score = (por * np.log(perm + 1)) / (depth1/1000)
    
    st.markdown("---")
    st.markdown("### 📊 نتائج تحليل واكتشاف المكمن")
    
    # عرض النتائج في بطاقات (Metrics)
    m1, m2, m3 = st.columns(3)
    
    if reservoir_score > 2.0:
        m1.metric("تقييم AI للمكمن", "عالي (High Quality)", delta="إيجابي")
        st.balloon_success() # إضافة تأثير نجاح
    elif reservoir_score > 1.0:
        m1.metric("تقييم AI للمكمن", "متوسط (Medium Quality)", delta="مستقر")
    else:
        m1.metric("تقييم AI للمكمن", "منخفض (Low Quality)", delta="سلبي", delta_color="inverse")
    
    m2.metric("مؤشر جودة المكمن (RQI)", f"{reservoir_score:.2f}")
    m3.metric("تدرج النفاذية (Permeability/Depth)", f"{(perm/depth1):.4f}")

    # --- 4. مخطط البئر الحقيقي (3D Visualization) ---
    st.markdown("---")
    st.markdown(f"### 📍 مخطط البئر الحقيقي للمكمن (Wellbore Simulation) ")
    st.markdown(f"العمق المستهدف: من {depth1:.1f} ft إلى {depth2:.1f} ft")
    
    # رسم بياني باستخدام Plotly (مثل الصورة الحقيقية للطبقات)
    fig = go.Figure()

    # محاكاة لطبقة رملية أو مكمن
    fig.add_trace(go.Scatter3d(
        x=[1, 1],
        y=[1, 1],
        z=[depth1, depth2],
        mode='lines+markers',
        line=dict(color='yellow', width=20),
        name='المكمن (Reservoir Zone)'
    ))
    
    # محاكاة للآبار المحيطة
    fig.add_trace(go.Scatter3d(
        x=[0.8, 1.2],
        y=[0.8, 1.2],
        z=[depth1-100, depth2+100],
        mode='lines',
        line=dict(color='gray', width=2, dash='dash'),
        name='آبار محيطة (Nearby Wells)'
    ))

    fig.update_layout(
        scene=dict(
            zaxis=dict(range=[depth1-200, depth2+200], autorange='reversed', title='Depth (ft)'),
            xaxis=dict(tickvals=[]),
            yaxis=dict(tickvals=[])
        ),
        title=f"مخطط البئر الحقيقي على عمق {depth1} قدم (3D)",
        width=800,
        height=700
    )
    
    st.plotly_chart(fig, use_container_width=True)

else:
    # شاشة العرض قبل التشغيل
    st.warning("يرجى إدخال البيانات في القائمة الجانبية ثم الضغط على 'تشغيل خوارزمية AI' لبدء التحليل.")
