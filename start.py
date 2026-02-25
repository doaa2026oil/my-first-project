import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# جعل الصفحة عريضة ومنظمة
st.set_page_config(layout="wide")

st.title("AI for Oil Reservoir Analysis and Discovery")
st.write("تحليل واكتشاف المكامن النفطية باستخدام الذكاء الاصطناعي")

# --- لوحة التحكم الجانبية (Sidebar) ---
st.sidebar.header("Control Panel | لوحة التحكم")
st.sidebar.write("حرك المنزلقات لتغيير النتائج فوراً")

# تغيير المدخلات إلى Sliders للتحكم اللحظي
depth = st.sidebar.slider("Depth (العمق بالامتار)", 500, 5000, 1500)
porosity = st.sidebar.slider("Porosity (المسامية %)", 5, 40, 20)
permeability = st.sidebar.slider("Permeability (النفاذية mD)", 10, 500, 150)

# --- نموذج بيانات تدريب وهمية ---
data = pd.DataFrame({
    "Depth": [1000, 1500, 2000, 2500, 3000],
    "Porosity": [10, 15, 18, 22, 25],
    "Permeability": [50, 100, 120, 180, 200],
    "Production": [100, 200, 250, 350, 400]
})

X = data[["Depth", "Porosity", "Permeability"]]
y = data["Production"]

# --- تدريب النموذج ---
model = LinearRegression()
model.fit(X, y)

# --- التنبؤ بالإنتاج ---
input_data = pd.DataFrame([[depth, porosity, permeability]], columns=["Depth", "Porosity", "Permeability"])
predicted_production = model.predict(input_data)[0]

# --- عرض النتائج والرسم في صفين ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Results")
    st.metric(label="Predicted Production", value=f"{predicted_production:.2f} bbl/d")
    st.info(f"العمق الحالي المختارهو: {depth} متر")

with col2:
    st.subheader("Production vs Depth Analysis")
    plt.figure(figsize=(8, 5))
    plt.style.use('seaborn-v0_8-darkgrid') # تحسين شكل الرسم
    plt.scatter(data["Depth"], data["Production"], color="blue", s=80, label="Historical Data", alpha=0.6)
    plt.scatter(depth, predicted_production, color="red", marker="*", s=300, label="Your Current Selection")
    plt.xlabel("Depth (meters)")
    plt.ylabel("Production (barrels/day)")
    plt.legend()
    st.pyplot(plt)
