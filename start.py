import streamlit as st
import pandas as pd
import numpy as np
import altair as alt # مكتبة رسم بياني متقدمة
import matplotlib.pyplot as plt

# إعدادات الصفحة (اختياري، تعطي شكلاً أفضل)
st.set_page_config(page_title="التنبؤ بإنتاج مكامن النفط", layout="wide")

st.title("تطبيق التنبؤ بإنتاج مكامن النفط")
st.write("أدخلي البيانات المطلوبة للحصول على التوقعات والتحليل البياني:")

# خانات الإدخال (مع الـ keys الفريدة لمنع الأخطاء)
col1, col2 = st.columns(2)

with col1:
    depth = st.number_input("العمق (Depth)", min_value=0.0, value=1000.0, key="d1")
    pressure = st.number_input("الضغط (Pressure)", min_value=0.0, value=2000.0, key="p1")

with col2:
    # جعلنا المسامية كنسبة مئوية لتسهيل الإدخال والرسم
    porosity_pct = st.number_input("المسامية (Porosity %)", min_value=0.0, max_value=100.0, value=15.0, key="po1")
    porosity = porosity_pct / 100.0 # تحويلها لنسبة عشريّة للحساب
    permeability = st.number_input("النفاذية (Permeability)", min_value=0.0, value=50.0, key="pe1")

# زر الحساب والتحليل
if st.button("بدء التحليل ورسم المخطط"):
    # 1. الحسابات (مثال بسيط، يمكنكِ تعديله)
    st.markdown("---")
    st.subheader("نتائج التحليل")
    
    production_bbl_day = (depth * pressure * porosity * permeability) / 1000.0
    
    col_res1, col_res2 = st.columns(2)
    with col_res1:
        st.metric(label="الإنتاج المتوقع (bbl/day)", value=f"{round(production_bbl_day, 2)}")
    with col_res2:
        st.metric(label="عامل المسامية (النسبة العشرية)", value=f"{round(porosity, 4)}")
    
    st.success("تم حساب النتائج بنجاح.")

    # 2. إضافة المخطط البياني
    st.markdown("---")
    st.subheader("المخطط البياني لمؤشرات المكمن")
    st.write("يُظهر هذا المخطط تأثير كل عامل من العوامل الأربعة على الإنتاج الكلي (كمثال توضيحي):")
    
    # تحضير البيانات للرسم
    chart_data = pd.DataFrame({
        'العامل': ['العمق', 'الضغط', 'المسامية (%)', 'النفاذية'],
        'القيمة الإدخالية': [depth, pressure, porosity_pct, permeability]
    })
    
    # إنشاء مخطط أعمدة تفاعلي باستخدام Altair
    # 
    c = alt.Chart(chart_data).mark_bar().encode(
        x='العامل',
        y=alt.Y('القيمة الإدخالية', title='قيمة الإدخال (الوحدات الأصلية)'),
        color=alt.Color('العامل', legend=None),
        tooltip=['العامل', 'القيمة الإدخالية']
    ).properties(
        width=alt.Step(80)  # عرض الأعمدة
    )
    
    # إضافة تسميات نصية فوق الأعمدة
    text = c.mark_text(
        align='center',
        baseline='bottom',
        dy=-5  # إزاحة النص لأعلى قليلاً
    ).encode(
        text='القيمة الإدخالية:Q'
    )
    
    # دمج الأعمدة والنصوص وعرضها
    st.altair_chart(c + text, use_container_width=True)

else:
    st.info("اضغطي على الزر لعرض النتائج والمخطط.")
