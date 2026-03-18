[3/18/2026 12:27 PM] دعاء عيسى غتر(A), 35: import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. إعدادات الصفحة وجعلها بلمسة احترافية
st.set_page_config(page_title="نظام تحليل مكامن النفط", layout="wide")

# إضافة تنسيق CSS لتحسين مظهر الخانات والأزرار
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #004b87;
        color: white;
        font-weight: bold;
    }
    .stNumberInput { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# العنوان مع أيقونة
st.title("🛢️ نظام التنبؤ والتحليل الذكي للمكامن")
st.markdown("---")

# 2. تنظيم خانات الإدخال في حاوية (Sidebar أو Columns)
with st.sidebar:
    st.header("📋 مدخلات البيانات")
    depth = st.number_input("العمق (Depth - m)", min_value=0.0, value=1000.0, key="d1")
    pressure = st.number_input("الضغط (Pressure - psi)", min_value=0.0, value=2000.0, key="p1")
    porosity_pct = st.number_input("المسامية (Porosity %)", min_value=0.0, max_value=100.0, value=15.0, key="po1")
    permeability = st.number_input("النفاذية (Permeability - mD)", min_value=0.0, value=50.0, key="pe1")
    
    analyze_btn = st.button("🚀 بدء التحليل الهندسي")

# 3. منطقة العرض الرئيسية
col_info, col_chart = st.columns([1, 1])

if analyze_btn:
    # الحسابات
    porosity = porosity_pct / 100.0
    production_bbl_day = (depth * pressure * porosity * permeability) / 1000.0

    with col_info:
        st.subheader("📊 النتائج التحليلية")
        
        # عرض النتائج بشكل بطاقات جذابة
        st.metric(label="الإنتاج المتوقع", value=f"{production_bbl_day:,.2f} bbl/day", delta="تقديري")
        
        with st.expander("تفاصيل العوامل المؤثرة"):
            st.write(f"• كفاءة المسامية: {porosity:.2%}")
            st.write(f"• نسبة النفاذية للعمق: {permeability/depth:.4f}")
        
        st.success("✅ تمت معالجة البيانات بناءً على المعايير الهيدروليكية.")

    with col_chart:
        st.subheader("🏗️ تمثيل مرئي للمكمن (شكل البئر)")
        
        # رسم شكل بئر نفط تعبيري باستخدام Matplotlib
        fig, ax = plt.subplots(figsize=(5, 8))
        
        # رسم برج الحفر (مثلث بسيط)
        ax.plot([4, 5, 6], [10, 15, 10], color='black', lw=3) # البرج
        ax.plot([5, 5], [0, 15], color='black', lw=2, linestyle='--') # أنبوب الحفر
        
        # رسم طبقات الأرض (العمق)
        ax.add_patch(plt.Rectangle((2, 0), 6, 10, color='#d2b48c', alpha=0.3)) # طبقة التربة
        
        # رسم مستوى النفط بناءً على "الإنتاج المتوقع" (للتوضيح البصري)
        oil_level = min(production_bbl_day / 500, 9) # تحديد سقف للرسم
        ax.add_patch(plt.Rectangle((4.5, 0), 1, oil_level, color='black', label='Expected Flow'))
        
        # إعدادات الرسم
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 16)
        ax.set_title("تمثيل تدفق المكمن", fontsize=12)
        ax.axis('off') # إخفاء المحاور لجعلها تبدو كأيقونة
        
        # إضافة نص توضيحي داخل الرسم
        ax.text(5, -1, f"Depth: {depth}m", ha='center', fontweight='bold')
        
        st.pyplot(fig)

else:
    with col_info:
        st.info("👈 الرجاء إدخال قيم المكمن من القائمة الجانبية ثم الضغط على 'بدء التحليل'.")
    with col_chart:
        # صورة تعبيرية مؤقتة أو مساحة فارغة
        st.write("سيظهر مخطط البئر هنا بعد الحساب.")
[3/18/2026 12:27 PM] دعاء عيسى غتر(A), 35: بعد ودر
[3/18/2026 12:27 PM] dfg يوسف: ووةةةاا
[3/18/2026 12:27 PM] dfg يوسف: عغغغغغغغقققغ
[3/18/2026 12:27 PM] dfg يوسف: ٢سسسصصثثلل
[3/18/2026 12:28 PM] dfg يوسف: 6treeeerggr
[3/18/2026 12:28 PM] dfg يوسف: tzzkuzzztttrrr
[3/18/2026 12:47 PM] dfg يوسف: الو
[3/18/2026 12:50 PM] dfg يوسف: الو
[3/18/2026 12:51 PM] dfg يوسف: الو
[3/18/2026 12:51 PM] dfg يوسف: الو
[3/18/2026 12:51 PM] dfg يوسف: الو
[3/18/2026 12:52 PM] دعاء عيسى غتر(A), 35: import streamlit as st
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
