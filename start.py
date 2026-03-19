import streamlit as st
import base64

# --- 1. إعدادات الصفحة والخلفية ---
st.set_page_config(page_title="برج تحليل المكامن الذكي", layout="wide")

# دالة لوضع صورة الخلفية (تأكدي من وجود ملف background.png)
def set_bg_hack(main_bg):
    try:
        main_bg_ext = "png"
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            # /* تخصيص الألوان لتباين أفضل مع الخلفية الغامقة */
            # .stNumberInput label, .stSubheader div {{ color: #FFFFFF !important; }}
            # </style>
            """,
            unsafe_allow_html=True
        )
    except FileNotFoundError:
        st.warning("لم يتم العثور على ملف 'background.png'. سيتم استخدام الخلفية الافتراضية.")

set_bg_hack('background.png')

# --- 2. واجهة الإدخال (بقيت كما هي) ---
st.title("🔥 برج تحليل المكامن بالذكاء الاصطناعي")

col1, col2 = st.columns([1, 2]) # تقسيم الشاشة لعمودين

with col1:
    st.subheader("🛠️ أدخل بيانات المكمن")
    
    # 1. العمق
    depth = st.number_input("📏 العمق (ft)", value=8000, step=100)
    
    # 2. الضغط
    pressure = st.number_input("🏋️ الضغط (psi)", value=3500, step=50)
    
    # 3. المسامية
    porosity = st.number_input("💧 المسامية (%)", value=25.0, step=0.5, format="%.2f")
    
    # 4. النفاذية
    permeability = st.number_input("🏎️ النفاذية (mD)", value=150, step=10)
    
    calculate = st.button("🔥 تحليل البرج التفاعلي")

# --- 3. بناء البرج التفاعلي (يظهر بعد الضغط على الزر) ---
with col2:
    if calculate:
        st.subheader("📊 المخطط النهائي التفاعلي: البرج النفطي")

        # --- حسابات بسيطة لتحديد حجم الشعلات (Logic) ---
        # سنستخدم هذه النسب المئوية للتحكم في ارتفاع الشعلة في الـ CSS
        
        # 1. الضغط: كلما زاد، زادت الشعلة
        pressure_flame_size = min(max(pressure / 50, 20), 100) # نسبة مئوية، حد أدنى وأقصى
        
        # 2. المسامية: كلما زادت، زادت الشعلة
        porosity_flame_size = min(max(porosity * 3, 20), 100)
        
        # 3. النفاذية: كلما زادت، زادت الشعلة
        permeability_flame_size = min(max(permeability / 2, 20), 100)
        
        # 4. العمق: سنعكسه، كلما زاد العمق زادت صعوبة الإنتاج (شعلة أصغر؟) أو نتركها للضغط.
        # سنجعل العمق شعلة مستقرة للحرارة.
        depth_flame_size = 50 

        # --- كود HTML و CSS للبرج والشعلات المتحركة ---
        rig_html = f"""
        <style>
            /* حاوية البرج */
            .rig-container {{
                position: relative;
                width: 300px;
                height: 500px;
                margin: 0 auto;
                background-color: rgba(20, 20, 20, 0.8); /* خلفية باهتة */
                border: 4px solid #444;
                border-radius: 10px;
                display: flex;
                flex-direction: column-reverse; /* الطبقات تبدأ من الأسفل */
                overflow: hidden;
            }}

            /* طبقات البرج */
            .rig-level {{
                flex: 1;
                border-top: 2px solid #555;
                display: flex;
                align-items: center;
                justify-content: space-between;
                padding: 0 15px;
                position: relative;
            }}

            /* عناوين الطبقات */
            .level-label {{
                font-size: 14px;
                font-weight: bold;
                color: #DDD;
                z-index: 10;
            }}

            /* القيم التفاعلية */
            .level-value {{
                font-size: 16px;
                color: #FFD700; /* ذهبي */
                z-index: 10;
            }} /* تحريك شعلة النار (Animation) */
            @keyframes flame-pulse {{
                0% {{ transform: scaleY(1); opacity: 0.8; }}
                50% {{ transform: scaleY(1.2); opacity: 1; }}
                100% {{ transform: scaleY(1); opacity: 0.8; }}
            }}

            /* حاوية الشعلة */
            .flame-container {{
                position: absolute;
                bottom: 0;
                left: 50%;
                transform: translateX(-50%);
                width: 30px;
                height: 100%; /* سيتم التحكم في الارتفاع الفعلي ديناميكياً */
                display: flex;
                align-items: flex-end;
                z-index: 5;
            }}

            /* شعلة النار الأساسية */
            .flame {{
                width: 100%;
                background: linear-gradient(to bottom, transparent, #FF4500, #FFD700); /* من البرتقالي للذهبي */
                border-radius: 50% 50% 10% 10%;
                animation: flame-pulse 1.5s ease-in-out infinite;
                transform-origin: bottom;
            }}

        </style>

        <div class="rig-container">
            <div class="rig-level" style="background-color: rgba(0, 150, 136, 0.2);">
                <div class="level-label">النفاذية</div>
                <div class="flame-container" style="height: {permeability_flame_size}%;">
                    <div class="flame" style="background: linear-gradient(to bottom, transparent, #4CAF50, #8BC34A);"></div> </div>
                <div class="level-value">{permeability} mD</div>
            </div>

            <div class="rig-level" style="background-color: rgba(33, 150, 243, 0.2);">
                <div class="level-label">المسامية</div>
                <div class="flame-container" style="height: {porosity_flame_size}%;">
                    <div class="flame" style="background: linear-gradient(to bottom, transparent, #2196F3, #BBDEFB);"></div> </div>
                <div class="level-value">{porosity:.2f}%</div>
            </div>

            <div class="rig-level" style="background-color: rgba(244, 67, 54, 0.2);">
                <div class="level-label">الضغط</div>
                <div class="flame-container" style="height: {pressure_flame_size}%;">
                    <div class="flame" style="background: linear-gradient(to bottom, transparent, #F44336, #FFCDD2);"></div> </div>
                <div class="level-value">{pressure} psi</div>
            </div>

            <div class="rig-level" style="background-color: rgba(121, 85, 72, 0.2);">
                <div class="level-label">العمق</div>
                <div class="flame-container" style="height: {depth_flame_size}%;">
                    <div class="flame" style="background: linear-gradient(to bottom, transparent, #795548, #D7CCC8);"></div> </div>
                <div class="level-value">{depth} ft</div>
            </div>
        </div>
        """

        # عرض البرج التفاعلي في Streamlit
        st.markdown(rig_html, unsafe_allow_html=True)

        # --- 4. التوضيح الهندسي للقيم ---
        st.divider()
        st.subheader("📖 توضيح القيم وتأثيرها على الإنتاج")
        
        # شرح ديناميكي بناءً على القيم
        cols = st.columns(2)
        
        with cols[0]:
            st.info(f"📏 العمق ({depth} ft): يؤثر على درجة حرارة المكمن والضغط الطبقي. كلما زاد العمق، زادت تكاليف الحفر.")
            if pressure > 4000:
                st.error(f"🏋️ الضغط ({pressure} psi): ضغط عالي جداً! (الشعلة الحمراء مرتفعة). هذا مكمن واعد بقوة دفع قوية، لكنه يتطلب معدات آمنة.")
            else:
                st.warning(f"🏋️ الضغط ({pressure} psi): ضغط متوسط إلى منخفض. قد نحتاج لوسائل رفع صناعي (Artificial Lift) قريباً.")

        with cols[1]:
            if porosity > 20:
                st.success(f"💧 المسامية ({porosity:.2f}%): مسامية ممتازة! (الشعلة الزرقاء مرتفعة). الصخور قادرة على تخزين كميات كبيرة من النفط.")
[3/19/2026 10:35 AM] دعاء عيسى غتر(A), 35: else:
                st.warning(f"💧 المسامية ({porosity:.2f}%): مسامية متوسطة. سعة التخزين محدودة.")
            
            if permeability > 100:
                st.success(f"🏎️ النفاذية ({permeability} mD): نفاذية جيدة جداً! (الشعلة الخضراء مرتفعة). النفط سيتدفق بسهولة نحو البئر.")
            else:
                st.error(f"🏎️ النفاذية ({permeability} mD): نفاذية منخفضة. التدفق سيكون بطيئاً وقد نحتاج لعمليات تحفيز (Stimulation).")
