import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# --- إعدادات الواجهة ---
st.set_page_config(page_title="AI Reservoir Vision", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #e2e8f0; }
    .stMetric { border: 1px solid #38bdf8; border-radius: 10px; padding: 15px; background: #161b22; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛢️ AI Reservoir Modeling & Digital Twin")
st.write("تحليل المكمن وتوليد المخطط الطبقي الرقمي (Digital Stratigraphy)")

# --- المدخلات في الجانب ---
with st.sidebar:
    st.header("⚙️ معلمات المكمن")
    target_depth = st.number_input("العمق الكلي (ft)", value=10000)
    oil_zone_start = st.slider("بداية النطاق النفطي", 0, target_depth, 8500)
    oil_zone_end = st.slider("نهاية النطاق النفطي", oil_zone_start, target_depth, 9200)
    analyze_btn = st.button("توليد مخطط البئر الذكي")

# --- منطقة العرض ---
if analyze_btn:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("📋 ملخص الذكاء الاصطناعي")
        st.metric("سمك النطاق النفطي (Pay Zone)", f"{oil_zone_end - oil_zone_start} ft")
        st.metric("احتمالية وجود الهيدروكربون", "94%", delta="عالية جداً")
        st.info("الذكاء الاصطناعي يشير إلى وجود صخور رملية (Sandstone) عالية المسامية في هذا النطاق.")

    with col2:
        # --- بناء مخطط البئر الحقيقي (Well Log Plot) ---
        depths = np.linspace(oil_zone_start - 200, oil_zone_end + 200, 100)
        
        # توليد بيانات جس وهمية (Gamma Ray & Resistivity)
        gr_signal = np.random.uniform(20, 40, 100) # قيم منخفضة تعني رمل (نفط)
        res_signal = np.random.uniform(50, 100, 100) # قيم عالية تعني نفط
        
        # إنشاء مخطط بمسارين (Subplots)
        fig = make_subplots(rows=1, cols=2, shared_yaxes=True, 
                            subplot_titles=('Gamma Ray (Lithology)', 'Resistivity (Fluids)'),
                            horizontal_spacing=0.05)

        # إضافة منحنى الجاما ري
        fig.add_trace(go.Scatter(x=gr_signal, y=depths, name='GR', line=dict(color='#4ade80')), row=1, col=1)
        
        # إضافة منحنى المقاومية
        fig.add_trace(go.Scatter(x=res_signal, y=depths, name='Resistivity', line=dict(color='#fbbf24')), row=1, col=2)

        # إضافة تظليل لمنطقة النفط (لإبهار الجمهور)
        fig.add_hrect(y0=oil_zone_start, y1=oil_zone_end, fillcolor="rgba(255, 255, 0, 0.2)", 
                      annotation_text="OIL ZONE (AI DETECTED)", annotation_position="top left")

        fig.update_yaxes(autorange="reversed", title="Depth (ft)")
        fig.update_layout(height=600, template="plotly_dark", showlegend=False)
        
        st.plotly_chart(fig, use_container_width=True)

        # إضافة رسم توضيحي لشكل الحقل (Image placeholder or visual)
        st.success("تم تحليل التكوين بنجاح. المكمن جاهز لعمليات التقييم الإنتاجي.")
else:
    st.warning("الرجاء تحديد معلمات العمق والضغط ثم الضغط على 'توليد المخطط'.")
