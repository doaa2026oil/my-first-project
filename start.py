دعاء عيسى غتر(A), 35, [2/20/2026 12:11 PM]
body {
    background: #121212;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
    font-family: sans-serif;
    color: white;
}

.container {
    background: #1e1e1e;
    padding: 30px;
    border-radius: 12px;
    width: 320px;
    text-align: center;
    border-top: 4px solid #f39c12;
}

h1 { color: #f39c12; font-size: 20px; }
.input-group { text-align: left; margin-bottom: 15px; }
label { display: block; font-size: 13px; color: #aaa; margin-bottom: 5px; }
input {
    width: 100%; padding: 10px; background: #2a2a2a;
    border: 1px solid #444; color: white; border-radius: 5px;
    box-sizing: border-box;
}
button {
    width: 100%; padding: 12px; background: #f39c12;
    border: none; border-radius: 5px; font-weight: bold; cursor: pointer;
}
.result { margin-top: 20px; background: #252525; padding: 10px; border-radius: 5px; }

dfg يوسف, [2/20/2026 12:11 PM]
الو

دعاء عيسى غتر(A), 35, [2/20/2026 12:12 PM]
function calculateAI() {
    let h = document.getElementById('thickness').value;
    let p = document.getElementById('porosity').value;

    if (h && p) {
        // معادلة تجريبية: السمك * المسامية * معامل ثابت
        let result = (h * p * 12.5).toFixed(2);
        document.getElementById('resultBox').style.display = "block";
        document.getElementById('outputValue').innerText = result + " BPD";
    } else {
        alert("Please enter values!");
    }
}

دعاء عيسى غتر(A), 35, [2/25/2026 4:01 PM]
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# إعداد واجهة عريضة ومنظمة
st.set_page_config(layout="wide")

st.title("AI for Oil Reservoir Analysis and Discovery")
st.write("تحليل واكتشاف المكامن النفطية باستخدام الذكاء الاصطناعي")

# --- لوحة التحكم الجانبية (Sliders) ---
st.sidebar.header("Control Panel | لوحة التحكم")
depth = st.sidebar.slider("Depth (العمق)", 500, 5000, 1500)
porosity = st.sidebar.slider("Porosity (المسامية %)", 5, 40, 20)
permeability = st.sidebar.slider("Permeability (النفاذية)", 10, 500, 150)

# --- بيانات التدريب ---
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

# --- عرض النتائج والرسم في صف واحد ---
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Predicted Production")
    st.metric(label="Production Rate", value=f"{predicted_production:.2f} bbl/day")
    st.write(f"العمق الحالي: {depth} متر")

with col2:
    st.subheader("Real-time Analysis Chart")
    plt.figure(figsize=(8, 5))
    plt.style.use('ggplot') 
    plt.scatter(data["Depth"], data["Production"], color="blue", s=80, label="Historical Data")
    plt.scatter(depth, predicted_production, color="red", marker="*", s=300, label="Your Current Selection")
    plt.xlabel("Depth (meters)")
    plt.ylabel("Production (barrels/day)")
    plt.legend()
    st.pyplot(plt)
