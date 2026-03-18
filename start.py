import streamlit as st
from PIL import Image
import base64

# --- الإعدادات العامة للصفحة ---
st.set_page_config(layout="wide", page_title="AI Reservoir Analysis Dashboard")

# --- دالة مساعدة لتحويل الصورة إلى Base64 لاستخدامها في CSS ---
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# --- إعداد الخلفية (باستخدام صورة الروبوت المقدمة) ---
# ملاحظة: تأكد من تسمية ملف صورة الروبوت بـ 'background.png' في نفس المجلد
try:
    bin_str = get_base64_of_bin_file('background.png')
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    /* تعديل شفافية محتوى الصفحة الرئيسية ليظهر الخلفية */
    .block-container {{
        background-color: rgba(255, 255, 255, 0.7);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
except FileNotFoundError:
    st.error("لم يتم العثور على ملف الخلفية 'background.png'. يرجى التأكد من وجوده في نفس المجلد.")

# --- تعريف التنسيقات (CSS) المخصصة للبطاقات والمحتوى ---
st.markdown("""
<style>
/* تنسيق البطاقة الرئيسية (العلبة) */
.card-container {
    background-color: #f1f6f9;
    border-radius: 12px;
    padding: 1.5rem;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    margin-bottom: 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
}

/* تنسيق الأيقونة داخل البطاقة */
.card-icon {
    font-size: 3rem;
    color: #4a90e2; /* لون أيقونة أزرق */
    margin-bottom: 0.5rem;
}

/* تنسيق اسم المتغير */
.card-title {
    font-size: 0.9rem;
    text-transform: uppercase;
    color: #333;
    font-weight: bold;
    letter-spacing: 1px;
    margin-bottom: 0.2rem;
}

/* تنسيق القيمة الكبيرة */
.card-value {
    font-size: 2rem;
    font-weight: bold;
    color: #1a1a1a;
    margin-bottom: -0.2rem;
}

/* تنسيق الوحدة */
.card-unit {
    font-size: 0.8rem;
    color: #777;
    margin-bottom: 1rem;
}

/* تنسيق الرسم البياني المصغر (الشكل العام) */
.card-sparkline {
    width: 100%;
    height: 30px;
    border-radius: 5px;
    background: linear-gradient(135deg, #e0f2f1 0%, #b2dfdb 100%); /* خلفية متدرجة بسيطة للشرارة */
}

/* تنسيق علامات التحقق */
.data-status {
    position: absolute;
    top: 10px;
    right: 10px;
    font-size: 0.8rem;
    color: #2e7d32; /* لون أخضر للتحقق */
    display: flex;
    align-items: center;
    gap: 4px;
}

/* تنسيق حاوية الصورة في الأسفل */
.diagram-container {
    position: relative;
    width: 100%;
    margin-top: 2rem;
}

/* تنسيق البطاقات العائمة فوق الصورة */
.floating-card {
    position: absolute;
    background-color: white;
    padding: 8px 15px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
    font-size: 0.85rem;
    font-weight: bold;
    color: #333;
    border: 1px solid #ddd;
}

</style>
""", unsafe_allow_html=True)

# --- محتوى الصفحة ---

# عنوان الصفحة
st.title("ARTIFICIAL INTELLIGENCE IN RESERVOIR ANALYSIS")
st.markdown("<p style='font-size: 1.1rem; color: #555;'>Project Dashboard - Core AI Core Project</p>", unsafe_allow_html=True)
st.markdown("---")

# --- القسم العلوي: نظرة عامة على معلمات المكمن (البطاقات) ---
st.markdown("### RESERVOIR PARAMETER OVERVIEW")

# إنشاء أعمدة للبطاقات
col1, col2, col3, col4 = st.columns(4)

# القيم الافتراضية
porosity_val = 18.5
permeability_val = 125.7
depth_val = 2450
pressure_val = 3150

# دالة مساعدة لإنشاء البطاقات لتجنب التكرار
def create_card(column, icon, title, value, unit, status_text):
    with column:
        st.markdown(f'''
        <div class="card-container">
            <div class="data-status"><span>{status_text}</span> <span style="font-size: 1.1rem;">✅</span></div>
[3/18/2026 4:54 PM] دعاء عيسى غتر(A), 35: <div class="card-icon">{icon}</div>
            <div class="card-title">{title}</div>
            <div class="card-value">{value}</div>
            <div class="card-unit">{unit}</div>
            <div class="card-sparkline"></div>
        </div>
        ''', unsafe_allow_html=True)

# ملء البطاقات
create_card(col1, "⚪", "POROSITY", f"{porosity_val}%", "Units: Ø", "Data integrity")
create_card(col2, "≋", "PERMEABILITY", f"{permeability_val} mD", "Units: mD", "Data Integrity")
create_card(col3, "📏", "DEPTH", f"{depth_val:,} m", "Units: meters", "Data Integrity")
create_card(col4, "⏲️", "PRESSURE", f"{pressure_val:,} psi", "Units: psi", "Data integrity")

st.markdown("---")

# --- القسم السفلي: مخطط برج الحفر (الرسم التفصيلي) ---
st.markdown("### WELLBORE DIAGRAM")

# عرض الصورة
# ملاحظة: تأكد من تسمية ملف مخطط البرج بـ 'derrick_diagram.png' في نفس المجلد
try:
    diag_img_str = get_base64_of_bin_file('derrick_diagram.png')
    
    # تنسيق البطاقات العائمة فوق الصورة بدقة
    # تم تحديد المواقع بدقة تقريبية لتطابق التصميم المقدم
    st.markdown(f'''
    <div class="diagram-container">
        <img src="data:image/png;base64,{diag_img_str}" style="width: 100%; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        
        <div class="floating-card" style="top: 25%; left: 7%;">
            <span style="font-weight: bold;">Porosity</span><br>
            <span style="font-size: 1.1rem;">Ø: {porosity_val}%</span>
        </div>
        
        <div class="floating-card" style="bottom: 10%; left: 20%;">
            <span style="font-weight: bold;">Permeability</span><br>
            <span style="font-size: 1.1rem;">k: {permeability_val} mD</span>
        </div>
        
        <div class="floating-card" style="top: 25%; right: 7%;">
            <span style="font-weight: bold;">Depth</span><br>
            <span style="font-size: 1.1rem;">D: {depth_val:,} m</span>
        </div>
        
        <div class="floating-card" style="bottom: 10%; right: 20%;">
            <span style="font-weight: bold;">Pressure</span><br>
            <span style="font-size: 1.1rem;">P: {pressure_val:,} psi</span>
        </div>
    </div>
    ''', unsafe_allow_html=True)
except FileNotFoundError:
    st.error("لم يتم العثور على ملف مخطط البرج 'derrick_diagram.png'. يرجى التأكد من وجوده في نفس المجلد.")


# --- شريط الأدوات الجانبي ---
with st.sidebar:
    st.image('derrick_diagram.png', width=100) # إضافة لوغو صغير
    st.markdown("## Configuration")
    
    st.markdown("### Input value")
    input_val = st.selectbox("تسود النازية", ["18.5%", "15.0%", "20.0%", "22.5%"])
    
    st.markdown("### Units")
    st.text_input("المجان الجريبية", "2257")
    
    st.markdown("### Simulation")
    sim_type = st.selectbox("معرف الالتماسات", ["Run AI Analysis", "Run Standard Analysis"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("RUN AI ANALYSIS", type="primary"):
        st.success(f"Starting {sim_type} on input {input_val}...")
        # هنا يمكنك إضافة كود تشغيل نموذج الذكاء الاصطناعي الخاص بك

    st.markdown("---")
    st.markdown("Dashboard by: Core AI Core Project")

# تخصيص لغة واجهة Streamlit الجانبية إلى العربية
st.markdown("""
<style>
/* تخصيص لغة واجهة Streamlit الجانبية */
.stSidebar [data-testid="stSidebarNav"] {
    direction: rtl;
    text-align: right;
}
.stSidebar h2, .stSidebar h3, .stSidebar p {
    text-align: right;
}
</style>
""", unsafe_allow_html=True)
