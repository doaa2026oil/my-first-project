import streamlit as st
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

st.set_page_config(layout="wide")

# ===== العنوان =====
st.title("🏗️ نظام تحليل المكامن النفطية")

# ===== المدخلات =====
col1, col2, col3, col4 = st.columns(4)

with col1:
    porosity = st.number_input("🟢 المسامية", value=20.0)

with col2:
    permeability = st.number_input("🔵 النفاذية", value=150.0)

with col3:
    depth = st.number_input("🟠 العمق", value=3000.0)

with col4:
    pressure = st.number_input("🔴 الضغط", value=2500.0)

# ===== حساب الإنتاج =====
if st.button("🔊 حساب الإنتاج"):
    
    production = (porosity * permeability) / (depth * 0.1) * (pressure / 1000)

    st.success(f"📈 الإنتاج المتوقع: {production:.2f}")

    # ===== صوت =====
    st.audio("https://www.soundjay.com/button/sounds/button-3.mp3")

    # ===== برج 3D =====
    st.markdown("### 🏢 برج الإنتاج (3D)")

    values = [porosity, permeability/10, depth/100, pressure/50]

    fig = plt.figure(figsize=(5, 9))
    ax = fig.add_subplot(111, projection='3d')

    bottom = 0

    for v in values:
        x = [0, 1, 1, 0, 0]
        y = [0, 0, 1, 1, 0]

        z = [bottom]*5
        z_top = [bottom + v]*5

        ax.plot(x, y, z, color="orange", alpha=0.6)
        ax.plot(x, y, z_top, color="orange", alpha=0.6)

        for i in range(4):
            ax.plot([x[i], x[i]], [y[i], y[i]], [bottom, bottom + v], 
                    color="orange", alpha=0.6)

        bottom += v

    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, bottom + 5)

    ax.set_facecolor("#111111")
    fig.patch.set_facecolor("#111111")

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Production", color="white")

    ax.tick_params(colors="white")

    st.pyplot(fig)
