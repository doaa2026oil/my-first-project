import streamlit as st
import plotly.graph_objects as go

# --- ملاحظة: كود الخلفية الخاص بكِ (add_bg_from_local) يجب أن يبقى في بداية ملفكِ ---

st.markdown("<h1 style='text-align: center; color: #FFD700;'>🔥 لوحة تحكم الشعلات وتحليل المكمن 🔥</h1>", unsafe_allow_html=True)

# ==========================================
# 1. البطاقات الملونة (المدخلات)
# ==========================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div style='background-color: rgba(233, 30, 99, 0.2); padding: 15px; border-radius: 10px; border: 2px solid #e91e63;'>", unsafe_allow_html=True)
    porosity = st.number_input("💧 المسامية (%)", value=25.0)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div style='background-color: rgba(3, 169, 244, 0.2); padding: 15px; border-radius: 10px; border: 2px solid #03a9f4;'>", unsafe_allow_html=True)
    permeability = st.number_input("🏎️ النفاذية (mD)", value=150)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div style='background-color: rgba(76, 175, 80, 0.2); padding: 15px; border-radius: 10px; border: 2px solid #4caf50;'>", unsafe_allow_html=True)
    pressure = st.number_input("🏋️ الضغط (psi)", value=3500)
    st.markdown("</div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div style='background-color: rgba(255, 152, 0, 0.2); padding: 15px; border-radius: 10px; border: 2px solid #ff9800;'>", unsafe_allow_html=True)
    depth = st.number_input("🕳️ العمق (ft)", value=7500)
    st.markdown("</div>", unsafe_allow_html=True)

# ==========================================
# 2. المخطط مع صورة البرج الفوتوغرافية
# ==========================================
fig = go.Figure()

# رابط صورة برج فوتوغرافية (يمكنكِ استبداله برابط صورتكِ الخاصة)
img_url = "https://images.unsplash.com/photo-1516198116309-885448657062?q=80&w=1000&auto=format&fit=crop"

# إضافة الصورة كخلفية للمخطط فقط
fig.add_layout_image(
    dict(
        source=img_url,
        xref="x", yref="y",
        x=0, y=1,
        sizex=1, sizey=1,
        sizing="stretch",
        layer="below"
    )
)

# رسم الشعلات (الأعمدة) فوق صورة البرج
flame_values = [porosity, permeability/50, pressure/100, depth/200] # تسوية القيم للرسم
flame_colors = ['#e91e63', '#03a9f4', '#4caf50', '#ff9800']
x_pos = [0.2, 0.4, 0.6, 0.8] # مواقع الشعلات فوق البرج

fig.add_trace(go.Bar(
    x=x_pos,
    y=flame_values,
    marker_color=flame_colors,
    width=0.08,
    text=[f"{porosity}%", f"{permeability}", f"{pressure}", f"{depth}"],
    textposition='outside',
    textfont=dict(color='white', size=16)
))

fig.update_layout(
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 1]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0, 1.2]),
    paper_bgcolor='rgba(0,0,0,0)', # خلفية المخطط شفافة لتظهر خلفية تطبيقكِ
    plot_bgcolor='rgba(0,0,0,0)',
    margin=dict(l=0, r=0, t=50, b=0),
    height=600
)

st.plotly_chart(fig, use_container_width=True)
