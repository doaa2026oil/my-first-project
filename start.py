[3/18/2026 1:33 PM] دعاء عيسى غتر(A), 35: import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="تحليل مكامن النفط بالذكاء الاصطناعي",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- تنسيق CSS مخصص للجمالية ---
st.markdown("""
<style>
    .stApp { background-color: #f4f7f6; }
    h1 { color: #1a5276; text-align: center; margin-bottom: 30px; }
    h2, h3 { color: #2e86c1; }
    div.stButton > button:first-child {
        background-color: #28b463; color: white; border-radius: 20px;
        font-weight: bold; width: 100%;
    }
    div.stButton > button:first-child:hover { background-color: #1d8348; }
</style>
""", unsafe_allow_config=True)

# --- العنوان الرئيسي ---
st.markdown("<h1>🛢️ نظام الذكاء الاصطناعي لاكتشاف وتحليل المكامن النفطية</h1>", unsafe_allow_config=True)
st.markdown("---")

# --- الشريط الجانبي (Side Bar) لإدخال البيانات ---
with st.sidebar:
    st.header("📊 مدخلات بيانات البئر")
    st.write("أدخل الخصائص الفيزيائية:")
    
    # المدخلات الأساسية
    depth = st.slider("العمق المستهدف (ft)", min_value=1000, max_value=12000, value=6500, step=100)
    
    col1, col2 = st.columns(2)
    with col1:
        porosity = st.number_input("المسامية (%)", min_value=0.0, max_value=40.0, value=18.0, step=0.1, format="%.1f")
    with col2:
        permeability = st.number_input("النفاذية (mD)", min_value=1, max_value=5000, value=200, step=1)
        
    pressure = st.number_input("الضغط (psi)", min_value=500, max_value=10000, value=3500, step=10)
    
    st.markdown("---")
    analyze_button = st.button("تحليل المكمن ورسم البئر 🛠️")

# --- محاكاة نموذج الذكاء الاصطناعي ---
def ai_prediction(depth, porosity, permeability, pressure):
    """دالة تحاكي قرار نموذج الذكاء الاصطناعي."""
    # منطق مبسط: المكمن الجيد له مسامية > 12% ونفاذية > 100 mD وضغط > 2000 psi
    
    score = 0
    if porosity > 12: score += 4
    if permeability > 100: score += 3
    if pressure > 2000 and depth > 4000: score += 3
    
    if score >= 8:
        return "احتمالية عالية لوجود النفط 🛢️", "#2ecc71" # أخضر
    elif score >= 5:
        return "احتمالية متوسطة - مياه مختلطة 💧/🛢️", "#f1c40f" # أصفر
    else:
        return "احتمالية منخفضة (مياه أو صخور صلبة) 💧/🧱", "#e74c3c" # أحمر

# --- الجسم الرئيسي للتطبيق ---
if analyze_button:
    # استدعاء دالة التنبؤ
    prediction_text, color_code = ai_prediction(depth, porosity, permeability, pressure)
    
    st.subheader("📊 نتائج التحليل والمقطع العرضي للبئر (Geological Cross-Section)")
    
    # عرض النتيجة بأسلوب جميل
    st.markdown(f"""
        <div style="background-color: {color_code}; padding: 15px; border-radius: 10px; text-align: center; margin-bottom: 20px;">
            <h3 style="color: white; margin: 0;">النتيجة المتوقعة: {prediction_text}</h3>
            <p style="color: white; margin: 5px 0 0 0;">(بناءً على مسامية {porosity}% ونفاذية {permeability} mD والعمق {depth} ft)</p>
        </div>
    """, unsafe_allow_config=True)

    # --- إنشاء رسم بئر حقيقي وواقعي (Real Well Cross-Section) باستخدام Plotly ---
    
    # تحديد نطاقات الطبقات المختلفة
    total_depth = depth + 1000 # إضافة عمق تحت المكمن
    shallow_layer_depth = 1500
    mid_layer_depth = total_depth - 1500
    reservoir_thickness = 200
    reservoir_start = depth - 100

    fig = go.Figure()

    # 1. رسم الطبقات الجيولوجية المحيطة (الواقعية)
    # طبقة سطحية (Sandstone - صخر رملي)
    fig.add_trace(go.Bar(
        x=[1], y=[shallow_layer_depth], base=0, name="صخور رملية سطحية",
        marker=dict(color='#ffeaa7', pattern_shape="."), showlegend=False
    ))
    # طبقة وسطى (Shale - صخر طيني)
    fig.add_trace(go.Bar(
        x=[1], y=[mid_layer_depth - shallow_layer_depth], base=shallow_layer_depth,
        name="صخور طينية (Shale Layer)",
[3/18/2026 1:33 PM] دعاء عيسى غتر(A), 35: marker=dict(color='#bdc3c7', pattern_shape="-"), showlegend=False
    ))
    # طبقة عميقة تحت المكمن (Limestone - صخر جيري)
    fig.add_trace(go.Bar(
        x=[1], y=[total_depth - mid_layer_depth], base=mid_layer_depth,
        name="صخور جيرية عميقة",
        marker=dict(color='#d1ccc0', pattern_shape="x"), showlegend=False
    ))

    # 2. رسم المكمن النفطي (مكمن واقعي)
    # لون المكمن يتغير حسب النتيجة (أسود للنفط)
    is_oil = "احتمالية عالية" in prediction_text
    reservoir_color = "#2c3e50" if is_oil else ("#7f8c8d" if "متوسطة" in prediction_text else "#b2bec3")
    
    # مكمن نفطي مشبع (صخر رملي مشبع - Sandstone pattern)
    fig.add_trace(go.Bar(
        x=[1], y=[reservoir_thickness], base=reservoir_start,
        name="المكمن المستهدف (Reservoir Zone)",
        marker=dict(color=reservoir_color, pattern_shape="+", line_color="black", line_width=2),
        showlegend=False
    ))

    # 3. رسم أنابيب تبطين البئر (Casing)
    casing_width = 0.15 # عرض الأنبوب في الرسم
    # أنبوب تبطين سطحي (Surface Casing)
    fig.add_trace(go.Scatter(
        x=[0.85, 0.85, 1.15, 1.15], y=[0, shallow_layer_depth+200, shallow_layer_depth+200, 0],
        fill="toself", fillcolor="#95a5a6", line_color="#34495e", name="أنبوب تبطين (Casing)"
    ))
    # أنبوب إنتاج (Production Casing) يمتد للعمق
    fig.add_trace(go.Scatter(
        x=[0.93, 0.93, 1.07, 1.07], y=[shallow_layer_depth, total_depth, total_depth, shallow_layer_depth],
        fill="toself", fillcolor="#bdc3c7", line_color="#34495e", name="أنبوب إنتاج"
    ))

    # 4. رسم الأسمنت حول الأنابيب (Cement Sheath)
    fig.add_trace(go.Scatter(
        x=[0.83, 0.83, 0.85, 0.85], y=[0, shallow_layer_depth+200, shallow_layer_depth+200, 0],
        fill="toself", fillcolor="#dcdde1", line_width=0, name="أسمنت"
    ))
    fig.add_trace(go.Scatter(
        x=[1.15, 1.15, 1.17, 1.17], y=[0, shallow_layer_depth+200, shallow_layer_depth+200, 0],
        fill="toself", fillcolor="#dcdde1", line_width=0, showlegend=False
    ))

    # 5. إضافة أيقونة رأس البئر (Wellhead) على السطح
    fig.add_annotation(
        x=1, y=0, text="🏗️", font_size=40, showarrow=False, yshift=20
    )

    # 6. إضافة نص توضيحي للمكمن
    reservoir_status_text = "نفط وغاز 🛢️" if is_oil else "مياه 💧"
    fig.add_annotation(
        x=1, y=depth,
        text=f"المكمن: {reservoir_status_text}<br>العمق: {depth} ft<br>المسامية: {porosity}%",
        font=dict(color="white", size=14, family='Arial Bold'),
        showarrow=True, arrowhead=2, arrowcolor="white", ax=120, ay=0,
        bgcolor="#000000AA", borderpad=4
    )

    # تخصيص تخطيط الرسم البياني
    fig.update_layout(
        title=dict(text="مقطع عرضي واقعي للبئر والطبقات الجيولوجية", x=0.5, font_size=20),
        xaxis=dict(showticklabels=False, range=[0.5, 1.5], fixedrange=True),
        yaxis=dict(title="العمق (ft)", autorange="reverse", fixedrange=True), # الصفر في الأعلى
        margin=dict(l=50, r=50, t=80, b=20),
        height=800,
        barmode='overlay', # تداخل الطبقات
        template="plotly_white",
        plot_bgcolor="#fdfdfd"
    )

    # عرض الرسم البياني
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 10px; padding: 10px; background-color: white;">', unsafe_allow_config=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_config=True)

else:
    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("أدخل البيانات من القائمة الجانبية واضغط على الزر لرسم البئر.")
        st.write("الرسم سيمثل الطبقات الجيولوجية المختلفة (رملية، طينية، جيرية) وأنابيب البئر بشكل واقعي.")

# --- تذييل الصفحة ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>تطبيق تحليل المكامن النفطية - عرض توضيحي للرسم الجيولوجي - © 2026</p>", unsafe_allow_config=True)
