import streamlit as st

st.markdown("""
<style>
    .header-box {
        background: linear-gradient(135deg, #1a1a1a 0%, #333 100%);
        padding: 30px;
        border-radius: 20px;
        border-bottom: 4px solid #ff4b4b;
        text-align: center;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.5);
    }
    .oil-rig-icon { font-size: 50px; margin-bottom: 10px; }
    .flame-container { display: flex; justify-content: center; gap: 8px; margin-top: -15px; }
    .mini-flame {
        width: 10px; height: 15px; 
        background: #ff4b1f; 
        border-radius: 50% 50% 20% 50%;
        animation: sway 0.3s infinite alternate;
    }
    @keyframes sway { from { transform: scale(1); } to { transform: scale(1.2) translateY(-2px); } }
    .main-title { color: #ffffff; font-weight: bold; font-size: 28px; }
</style>

<div class="header-box">
    <div class="flame-container">
        <div class="mini-flame"></div><div class="mini-flame"></div>
        <div class="mini-flame"></div><div class="mini-flame"></div>
    </div>
    <div class="oil-rig-icon">🏗️</div>
    <div class="main-title">منصة البرج الذكي لتحليل المكامن</div>
    <p style="color: #ccc;">University of Basrah - Petroleum Engineering</p>
</div>
""", unsafe_allow_html=True)
