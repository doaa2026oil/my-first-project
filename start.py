import streamlit as st
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
