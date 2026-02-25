# main.py
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


st.title("AI for Oil Reservoir Analysis and Discovery")
st.write("تحليل واكتشاف المكامن النفطية باستخدام الذكاء الاصطناعي")

# --- إدخال بيانات البئر ---
st.header("Enter Well Data")
depth = st.number_input("Depth (meters)", min_value=0.0, value=1500.0)
porosity = st.number_input("Porosity (%)", min_value=0.0, value=20.0)
permeability = st.number_input("Permeability (mD)", min_value=0.0, value=150.0)

# --- نموذج بيانات تدريب وهمية ---
# البيانات هذه لتوضيح طريقة عمل النموذج، تقدر تغيرها حسب بياناتك
data = pd.DataFrame({
    "Depth": [1000, 1500, 2000, 2500, 3000],
    "Porosity": [10, 15, 18, 22, 25],
    "Permeability": [50, 100, 120, 180, 200],
    "Production": [100, 200, 250, 350, 400]
})

X = data[["Depth", "Porosity", "Permeability"]]
y = data["Production"]

# --- تدريب نموذج الانحدار الخطي ---
model = LinearRegression()
model.fit(X, y)

# --- التنبؤ بالإنتاج ---
input_data = pd.DataFrame([[depth, porosity, permeability]], columns=["Depth", "Porosity", "Permeability"])
predicted_production = model.predict(input_data)[0]

st.subheader("Predicted Production")
st.success(f"{predicted_production:.2f} barrels/day")

# --- رسم بياني ---
st.subheader("Production vs Depth")
plt.figure(figsize=(6,4))
plt.scatter(data["Depth"], data["Production"], color="blue", label="Training Data")
plt.scatter(depth, predicted_production, color="red", label="Your Well", s=100)
plt.xlabel("Depth (meters)")
plt.ylabel("Production (barrels/day)")
plt.legend()
st.pyplot(plt)# main.py
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("AI for Oil Reservoir Analysis and Discovery")
st.write("تحليل واكتشاف المكامن النفطية باستخدام الذكاء الاصطناعي")

# --- إدخال بيانات البئر ---
st.header("Enter Well Data")
depth = st.number_input("Depth (meters)", min_value=0.0, value=1500.0)
porosity = st.number_input("Porosity (%)", min_value=0.0, value=20.0)
permeability = st.number_input("Permeability (mD)", min_value=0.0, value=150.0)

# --- نموذج بيانات تدريب وهمية ---
# البيانات هذه لتوضيح طريقة عمل النموذج، تقدر تغيرها حسب بياناتك
data = pd.DataFrame({
    "Depth": [1000, 1500, 2000, 2500, 3000],
    "Porosity": [10, 15, 18, 22, 25],
    "Permeability": [50, 100, 120, 180, 200],
    "Production": [100, 200, 250, 350, 400]
})

X = data[["Depth", "Porosity", "Permeability"]]
y = data["Production"]

# --- تدريب نموذج الانحدار الخطي ---
model = LinearRegression()
model.fit(X, y)

# --- التنبؤ بالإنتاج ---
input_data = pd.DataFrame([[depth, porosity, permeability]], columns=["Depth", "Porosity", "Permeability"])
predicted_production = model.predict(input_data)[0]

st.subheader("Predicted Production")
st.success(f"{predicted_production:.2f} barrels/day")

# --- رسم بياني ---
st.subheader("Production vs Depth")
plt.figure(figsize=(6,4))
plt.scatter(data["Depth"], data["Production"], color="blue", label="Training Data")
plt.scatter(depth, predicted_production, color="red", label="Your Well", s=100)
plt.xlabel("Depth (meters)")
plt.ylabel("Production (barrels/day)")
plt.legend()
st.pyplot(plt)# main.py
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("AI for Oil Reservoir Analysis and Discovery")
st.write("تحليل واكتشاف المكامن النفطية باستخدام الذكاء الاصطناعي")

# --- إدخال بيانات البئر ---
st.header("Enter Well Data")
depth = st.number_input("Depth (meters)", min_value=0.0, value=1500.0)
porosity = st.number_input("Porosity (%)", min_value=0.0, value=20.0)
permeability = st.number_input("Permeability (mD)", min_value=0.0, value=150.0)

# --- نموذج بيانات تدريب وهمية ---
# البيانات هذه لتوضيح طريقة عمل النموذج، تقدر تغيرها حسب بياناتك
data = pd.DataFrame({
    "Depth": [1000, 1500, 2000, 2500, 3000],
    "Porosity": [10, 15, 18, 22, 25],
    "Permeability": [50, 100, 120, 180, 200],
    "Production": [100, 200, 250, 350, 400]
})

X = data[["Depth", "Porosity", "Permeability"]]
y = data["Production"]

# --- تدريب نموذج الانحدار الخطي ---
model = LinearRegression()
model.fit(X, y)

# --- التنبؤ بالإنتاج ---
input_data = pd.DataFrame([[depth, porosity, permeability]], columns=["Depth", "Porosity", "Permeability"])
predicted_production = model.predict(input_data)[0]

st.subheader("Predicted Production")
st.success(f"{predicted_production:.2f} barrels/day")

# --- رسم بياني ---
st.subheader("Production vs Depth")
plt.figure(figsize=(6,4))
plt.scatter(data["Depth"], data["Production"], color="blue", label="Training Data")
plt.scatter(depth, predicted_production, color="red", label="Your Well", s=100)
plt.xlabel("Depth (meters)")
plt.ylabel("Production (barrels/day)")
plt.legend()
st.pyplot(plt)# main.py
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("AI for Oil Reservoir Analysis and Discovery")
st.write("تحليل واكتشاف المكامن النفطية باستخدام الذكاء الاصطناعي")

# --- إدخال بيانات البئر ---
st.header("Enter Well Data")
depth = st.number_input("Depth (meters)", min_value=0.0, value=1500.0)
porosity = st.number_input("Porosity (%)", min_value=0.0, value=20.0)
permeability = st.number_input("Permeability (mD)", min_value=0.0, value=150.0)

# --- نموذج بيانات تدريب وهمية ---
# البيانات هذه لتوضيح طريقة عمل النموذج، تقدر تغيرها حسب بياناتك
data = pd.DataFrame({
    "Depth": [1000, 1500, 2000, 2500, 3000],
    "Porosity": [10, 15, 18, 22, 25],
    "Permeability": [50, 100, 120, 180, 200],
    "Production": [100, 200, 250, 350, 400]
})

X = data[["Depth", "Porosity", "Permeability"]]
y = data["Production"]

# --- تدريب نموذج الانحدار الخطي ---
model = LinearRegression()
model.fit(X, y)

# --- التنبؤ بالإنتاج ---
input_data = pd.DataFrame([[depth, porosity, permeability]], columns=["Depth", "Porosity", "Permeability"])
predicted_production = model.predict(input_data)[0]

st.subheader("Predicted Production")
st.success(f"{predicted_production:.2f} barrels/day")

# --- رسم بياني ---
st.subheader("Production vs Depth")
plt.figure(figsize=(6,4))
plt.scatter(data["Depth"], data["Production"], color="blue", label="Training Data")
plt.scatter(depth, predicted_production, color="red", label="Your Well", s=100)
plt.xlabel("Depth (meters)")
plt.ylabel("Production (barrels/day)")
plt.legend()
st.pyplot(plt)