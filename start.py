import streamlit as st
import pandas as pd
import numpy as np

# إعدادات الصفحة
st.set_page_config(page_title="Oil Reservoir Prediction", layout="wide")

st.title("تطبيق التنبؤ بإنتاج مكامن النفط")
st.write("أدخلي البيانات المطلوبة للحصول على التوقعات:")

# إنشاء أعمدة لتنظيم الواجهة
col1, col2 = st.columns(2)

with col1:
    # إضافة مفاتيح (keys) فريدة لكل مدخل لمنع الخطأ
    depth = st.number_input("العمق (Depth)", min_value=0.0, key="depth_input")
    pressure = st.number_input("الضغط (Pressure)", min_value=0.0, key="pressure_input")

with col2:
    porosity = st.number_input("المسامية (Porosity)", min_value=0.0, max_value=1.0, key="porosity_input")
    permeability = st.number_input("النفاذية (Permeability)", min_value=0.0, key="perm_input")

# زر الحساب أو التنبؤ
if st.button("بدء التحليل"):
    # هنا يتم وضع معادلات التنبؤ الخاصة بكِ
    st.success("تم استلام البيانات بنجاح وجاري المعالجة...")
    
    # مثال بسيط لعرض النتيجة
    result = (depth * pressure * porosity) / 100
    st.metric(label="الإنتاج المتوقع", value=f"{round(result, 2)} bbl/day")

st.info("ملاحظة: تأكدي من دقة الوحدات المستخدمة في الإدخال.")
