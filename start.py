import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# عنوان التطبيق
st.title("AI for Oil Reservoir Analysis and Discovery")
st.write("تحليل واكتشاف المكامن النفطية باستخدام الذكاء الاصطناعي")

# --- إدخال بيانات البئر ---
st.header("Enter Well Data")
depth = st.number_input("Depth (meters)", min_value=0.0, value=1500.0)
porosity = st.number_input("Porosity (%)", min_value=0.0, value=20.0)
permeability = st.number_input("Permeability (mD)", min_value=0.0, value=150.0)

# --- نموذج بيانات تدريب وهمية ---
data = pd.DataFrame({
    "Depth": [1000, 1500, 2000, 2500, 3000],
    "Production": [500, 700, 850, 600, 450]
})

# تدريب نموذج بسيط (Linear Regression)
X = data[["Depth"]]
y = data["Production"]
model = LinearRegression()
model.fit(X, y)

# التنبؤ بناءً على العمق المدخل
predicted_production = model.predict([[depth]])

st.write(f"### Predicted Production: {predicted_production[0]:.2f} barrels/day")

# --- رسم بياني ---
st.subheader("Production vs Depth")
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(data["Depth"], data["Production"], color="blue", label="Actual Data")
ax.scatter(depth, predicted_production, color="red", label="Predicted Point", s=100)
ax.set_xlabel("Depth (meters)")
ax.set_ylabel("Production (barrels/day)")
ax.legend()

st.pyplot(fig)
