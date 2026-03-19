import streamlit as st
import plotly.graph_objects as go
import numpy as np

# --- 1. إعدادات الصفحة الاحترافية ---
# نجعلها Wide لتوفير مساحة للعب بالمخطط
st.set_page_config(page_title="تحليل المكامن - البرج الذكي", layout="wide")

# --- 2. تصميم الرأس (Header) ---
st.markdown("<h1 style='text-align: center; color: #E63946; font-family: Cairo;'>نظام تحليل المكامن والإنتاج الذكي</h1>", unsafe_allow_html=True)
st.write("---")

# --- 3. إدارة حالة المخطط (State Management) ---
# هذه الخطوة مهمة جداً لضمان عدم إعادة رسم المخطط من الصفر
if 'tower_fig' not in st.session_state:
    # إنشاء المخطط مرة واحدة فقط وحفظه في الـ Session State
    
    # تعريف إحداثيات هيكل البرج
    tower_x = [1, 1.5, 2, 1]
    tower_y = [0, 12, 0, 0]
    
    # تعريف إحداثيات الشعلات الأربع الثابتة
    flare_locs = [ (1.3, 10), (1.5, 12), (1.7, 10), (1.5, 14) ]
    
    fig = go.Figure()

    # أ. هيكل البرج
    fig.add_trace(go.Scatter(
        x=tower_x, y=tower_y, 
        fill='toself', 
        line_color='#4A4A4A', 
        name='هيكل البرج'
    ))

    # ب. الشعلات الأربع (تستخدم Markers تفاعلية)
    fig.add_trace(go.Scatter(
        x=[loc[0] for loc in flare_locs],
        y=[loc[1] for loc in flare_locs],
        mode='markers',
        marker=dict(size=30, color='#F4A261', symbol='hexagram-open-dot'),
        name='الشعلات (تفاعلية)'
    ))

    # ج. تحسين التخطيط للتفاعل (Interaction Layout)
    fig.update_layout(
        plot_bgcolor='rgba(15,15,15,0.9)', # خلفية داكنة للتباين
        paper_bgcolor='rgba(0,0,0,0)',
        height=650, # تكبير المخطط للعب به
        showlegend=True,
        # جعل المحاور مرئية ولكن خفيفة للعب بـ Zoom و Pan
        xaxis=dict(showgrid=False, zeroline=False, range=[0, 3]),
        yaxis=dict(showgrid=True, zeroline=False, range=[-2, 18], gridcolor='rgba(255,255,255,0.1)'),
        # تمكين شريط الأدوات الكامل للتفاعل (Zoom, Pan, Box Select, etc.)
        dragmode='pan', # الوضع الافتراضي هو التحريك (Pan)
        hovermode='closest'
    )
    
    st.session_state.tower_fig = fig

# --- 4. تقسيم الشاشة لمدخلات ومخطط تفاعلي ---
col1, col2 = st.columns([1, 2.5]) # مساحة أكبر للمخطط

with col1:
    st.markdown("<h3 style='font-family: Cairo;'>📋 إدخال البيانات الفنية</h3>", unsafe_allow_html=True)
    # عند تغيير هذه المدخلات، ستعاد تحميل هذه القائمة فقط، ولن يتأثر المخطط
    depth = st.number_input("العمق (ft)", value=8000, step=100)
    pressure = st.number_input("الضغط (psi)", value=3500, step=50)
    porosity = st.slider("المسامية (%)", 0, 100, 25)
    flow_rate = st.number_input("معدل التدفق (bbl/d)", value=1500)

with col2:
    st.markdown("<h3 style='text-align: center; font-family: Cairo;'>🏗️ مخطط البرج والشعلات (التفاعل الكامل مفعل)</h3>", unsafe_allow_html=True)
    
    # عرض المخطط المحفوظ من الـ Session State
    # هذا السطر يجعل المخطط مستقراً وتفاعلياً
    st.plotly_chart(st.session_state.tower_fig, use_container_width=True)

# --- 5. عرض النتائج النهائية (بطاقات احترافية) ---
st.write("---")
res1, res2, res3 = st.columns(3)
res1.metric(label="معدل التدفق", value=f"{flow_rate} bbl/d", delta="+5%")
res2.metric(label="كفاءة المكمن", value=f"{porosity}%", delta="-2%")
res3.metric(label="درجة الحرارة المتوقعة", value="210°F")
