import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# --- إعدادات الصفحة ---
st.set_page_config(
    page_title="تحليل المكامن بالذكاء الاصطناعي",
    page_icon="🛢️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- واجهة المستخدم (CSS لتصميم البطاقات) ---
st.markdown("""
<style>
    /* تنسيق الحاوية الرئيسية للبطاقات */
    .metric-container {
        display: flex;
        justify-content: space-around;
        gap: 15px;
        margin-bottom: 25px;
    }
    /* تنسيق كل بطاقة فردية */
    .metric-card {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        width: 23%;
        text-align: right;
    }
    .metric-title {
        font-size: 1.1em;
        color: #333;
        margin-bottom: 10px;
        font-weight: bold;
    }
    /* تنسيق مدخلات Streamlit داخل البطاقة */
    div[data-baseweb="input"] {
        border-radius: 8px !important;
    }
    /* تنسيق عنوان التطبيق */
    .app-header {
        text-align: center;
        margin-bottom: 30px;
    }
    .app-title {
        color: #FFC107; /* لون أصفر ذهبي للشعلة */
        font-size: 2.5em;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# --- عنوان التطبيق ---
st.markdown("""
<div class="app-header">
    <span class="app-title">🔥 لوحة تحكم الشعلات وتحليل المكمن 🔥</span>
</div>
""", unsafe_allow_html=True)

# --- قسم البطاقات الأربعة للإدخال ---
st.markdown('<div class="metric-container">', unsafe_allow_html=True)

# البطاقة 1: العمق (جديدة)
with st.container():
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<div class="metric-title">📏 العمق (ft)</div>', unsafe_allow_html=True)
    depth = st.number_input("", value=8000, step=100, key="depth_input", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# البطاقة 2: الضغط
with st.container():
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<div class="metric-title">🏋️‍♂️ الضغط (psi)</div>', unsafe_allow_html=True)
    pressure = st.number_input("", value=3500, step=100, key="pressure_input", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# البطاقة 3: المسامية
with st.container():
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<div class="metric-title">💧 المسامية (%)</div>', unsafe_allow_html=True)
    porosity = st.number_input("", value=25.0, step=0.1, key="porosity_input", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

# البطاقة 4: النفاذية
with st.container():
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown('<div class="metric-title">🏎️ النفاذية (mD)</div>', unsafe_allow_html=True)
    permeability = st.number_input("", value=150, step=10, key="perm_input", label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # إغلاق حاوية البطاقات

# --- زر التشغيل ---
col1, col2, col3 = st.columns([1,2,1])
with col2:
    run_analysis = st.button("🔥 تحليل المكمن وتحديث الشعلات 🔥", use_container_width=True)

# --- وظيفة لإنشاء الصورة ديناميكياً ---
def create_flared_derrick_image(d, p, poro, perm):
    # 1. إنشاء صورة خلفية (مستطيل يمثل السماء الليلية للحصول على تأثير أفضل للشعلات)
    img_width = 800
    img_height = 600
    image = Image.new('RGB', (img_width, img_height), color = (10, 10, 30)) # سماء ليلية داكنة
    draw = ImageDraw.Draw(image)

    # 2. رسم برج نفطي مبسط (Derrick)
    derrick_color = (200, 200, 200) # لون معدني
    derrick_base = [(300, 550), (500, 550), (450, 150), (350, 150)]
    draw.polygon(derrick_base, outline=derrick_color, width=5)
# رسم الهيكل الداخلي
    for y in range(200, 550, 50):
        draw.line([(350 + (y-150)//4, y), (450 - (y-150)//4, y)], fill=derrick_color, width=2)
    draw.line([(350, 150), (450, 550)], fill=derrick_color, width=2)
    draw.line([(450, 150), (350, 550)], fill=derrick_color, width=2)

    # 3. محاكاة الشعلات الأربعة (Flakes)
    # نستخدم دوائر متدرجة الألوان (أسفر، برتقالي، أحمر) لمحاكاة النار
    flare_positions = [
        (360, 140), # شعلة 1 (يسار علوي)
        (440, 140), # شعلة 2 (يمين علوي)
        (380, 100), # شعلة 3 (وسط أعلى)
        (420, 100)  # شعلة 4 (وسط أعلى)
    ]
    
    # رسم توهج الشعلات
    for pos in flare_positions:
        draw.ellipse([pos[0]-15, pos[1]-15, pos[0]+15, pos[1]+15], fill=(255, 69, 0), outline=None) # أحمر برتقالي
        draw.ellipse([pos[0]-8, pos[1]-8, pos[0]+8, pos[1]+8], fill=(255, 165, 0), outline=None) # برتقالي
        draw.ellipse([pos[0]-3, pos[1]-3, pos[0]+3, pos[1]+3], fill=(255, 255, 0), outline=None) # أصفر

    # 4. إضافة النصوص (القيم) بجانب الشعلات
    # ملاحظة: Pillow يحتاج خطوط نظام لإظهار العربية بشكل جيد، 
    # سنستخدم الإنجليزية هنا للتبسيط ولضمان عمل الكود على أي جهاز مباشرة.
    try:
        # محاولة تحميل خط نظام شائع
        font = ImageFont.truetype("arial.ttf", 18)
    except IOError:
        # خط احتياطي إذا لم يجد الخط المحدد
        font = ImageFont.load_default()

    text_color = (255, 255, 255)
    
    # ربط كل قيمة بشعلة
    data_to_display = [
        (f"Depth: {d} ft", (flare_positions[0][0]-140, flare_positions[0][1]-10)),
        (f"Press: {p} psi", (flare_positions[1][0]+25, flare_positions[1][1]-10)),
        (f"Poro: {poro} %", (flare_positions[2][0]-140, flare_positions[2][1]-20)),
        (f"Perm: {perm} mD", (flare_positions[3][0]+25, flare_positions[3][1]-20))
    ]

    for text, pos in data_to_display:
        draw.text(pos, text, fill=text_color, font=font)

    # إرجاع الصورة ككائن يمكن لـ Streamlit عرضه
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    return img_byte_arr.getvalue()

# --- قسم العرض المرئي (النتيجة) ---
if run_analysis:
    st.markdown("---")
    st.subheader("📊 تحليل الصورة المرئية للمكمن (بالذكاء الاصطناعي)")
    
    with st.spinner("جاري إنشاء الصورة وتحديث الشعلات..."):
        # إنشاء الصورة بناءً على القيم الحالية
        generated_image = create_flared_derrick_image(depth, pressure, porosity, permeability)
        
        # عرض الصورة
        st.image(generated_image, caption="محاكاة برج النفط مع شعلات تعكس قيم المكمن المدخلة", use_container_width=True)
        
        # إضافة تلميح عن دور الذكاء الاصطناعي
        st.info("💡 يقوم نموذج الذكاء الاصطناعي بتحليل هذه القيم (العمق، الضغط، المسامية، النفاذية) للتنبؤ بحجم الإنتاج وحالة المكمن بشكل لحظي.")

else:
    # رسالة تظهر قبل الضغط على الزر
    st.markdown("---")
    st.warning("👈 قم بتعديل القيم في البطاقات أعلاه ثم اضغط على 'تحليل المكمن' لعرض النتيجة المرئية.")
