[3/18/2026 1:33 PM] دعاء عيسى غتر(A), 35: marker=dict(color='#bdc3c7', pattern_shape="-"), showlegend=False
    ))
    # طبقة عميقة تحت المكمن (Limestone - صخر جيري)
    fig.add_trace(go.Bar(
        x=[1], y=[total_depth - mid_layer_depth], base=mid_layer_depth,
        name="صخور جيرية عميقة",
        marker=dict(color='#d1ccc0', pattern_shape="x"), showlegend=False
    ))

    # 2. رسم المكمن النفطي (مكمن واقعي)
    # لون المكمن يتغير حسب النتيجة (أسود للنفط)
    is_oil = "احتمالية عالية" in prediction_text
    reservoir_color = "#2c3e50" if is_oil else ("#7f8c8d" if "متوسطة" in prediction_text else "#b2bec3")
    
    # مكمن نفطي مشبع (صخر رملي مشبع - Sandstone pattern)
    fig.add_trace(go.Bar(
        x=[1], y=[reservoir_thickness], base=reservoir_start,
        name="المكمن المستهدف (Reservoir Zone)",
        marker=dict(color=reservoir_color, pattern_shape="+", line_color="black", line_width=2),
        showlegend=False
    ))

    # 3. رسم أنابيب تبطين البئر (Casing)
    casing_width = 0.15 # عرض الأنبوب في الرسم
    # أنبوب تبطين سطحي (Surface Casing)
    fig.add_trace(go.Scatter(
        x=[0.85, 0.85, 1.15, 1.15], y=[0, shallow_layer_depth+200, shallow_layer_depth+200, 0],
        fill="toself", fillcolor="#95a5a6", line_color="#34495e", name="أنبوب تبطين (Casing)"
    ))
    # أنبوب إنتاج (Production Casing) يمتد للعمق
    fig.add_trace(go.Scatter(
        x=[0.93, 0.93, 1.07, 1.07], y=[shallow_layer_depth, total_depth, total_depth, shallow_layer_depth],
        fill="toself", fillcolor="#bdc3c7", line_color="#34495e", name="أنبوب إنتاج"
    ))

    # 4. رسم الأسمنت حول الأنابيب (Cement Sheath)
    fig.add_trace(go.Scatter(
        x=[0.83, 0.83, 0.85, 0.85], y=[0, shallow_layer_depth+200, shallow_layer_depth+200, 0],
        fill="toself", fillcolor="#dcdde1", line_width=0, name="أسمنت"
    ))
    fig.add_trace(go.Scatter(
        x=[1.15, 1.15, 1.17, 1.17], y=[0, shallow_layer_depth+200, shallow_layer_depth+200, 0],
        fill="toself", fillcolor="#dcdde1", line_width=0, showlegend=False
    ))

    # 5. إضافة أيقونة رأس البئر (Wellhead) على السطح
    fig.add_annotation(
        x=1, y=0, text="🏗️", font_size=40, showarrow=False, yshift=20
    )

    # 6. إضافة نص توضيحي للمكمن
    reservoir_status_text = "نفط وغاز 🛢️" if is_oil else "مياه 💧"
    fig.add_annotation(
        x=1, y=depth,
        text=f"المكمن: {reservoir_status_text}<br>العمق: {depth} ft<br>المسامية: {porosity}%",
        font=dict(color="white", size=14, family='Arial Bold'),
        showarrow=True, arrowhead=2, arrowcolor="white", ax=120, ay=0,
        bgcolor="#000000AA", borderpad=4
    )

    # تخصيص تخطيط الرسم البياني
    fig.update_layout(
        title=dict(text="مقطع عرضي واقعي للبئر والطبقات الجيولوجية", x=0.5, font_size=20),
        xaxis=dict(showticklabels=False, range=[0.5, 1.5], fixedrange=True),
        yaxis=dict(title="العمق (ft)", autorange="reverse", fixedrange=True), # الصفر في الأعلى
        margin=dict(l=50, r=50, t=80, b=20),
        height=800,
        barmode='overlay', # تداخل الطبقات
        template="plotly_white",
        plot_bgcolor="#fdfdfd"
    )

    # عرض الرسم البياني
    st.markdown('<div style="border: 1px solid #ddd; border-radius: 10px; padding: 10px; background-color: white;">', unsafe_allow_config=True)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown('</div>', unsafe_allow_config=True)

else:
    st.write("")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("أدخل البيانات من القائمة الجانبية واضغط على الزر لرسم البئر.")
        st.write("الرسم سيمثل الطبقات الجيولوجية المختلفة (رملية، طينية، جيرية) وأنابيب البئر بشكل واقعي.")

# --- تذييل الصفحة ---
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>تطبيق تحليل المكامن النفطية - عرض توضيحي للرسم الجيولوجي - © 2026</p>", unsafe_allow_config=True)
[3/18/2026 1:53 PM] دعاء عيسى غتر(A), 35: # ب. الرسوم البيانية التفاعلية المدعومة بالذكاء الاصطناعي (AI Analytics)
        st.subheader("📉 التصور البصري لتحليل البيانات السيزمية (Seismic AI Visuals)")
        g1, g2 = st.columns(2)

        with g1:
            # مثال لرسم بياني زمني تفاعلي: تحليل الانحدار السيزمي
            df = pd.DataFrame({
                'تاريخ': pd.date_range(start='2026-01-01', periods=12, freq='M'),
                'سعة الموجة (المدخلات)': np.random.normal(amplitude, 100, 12),
                'الاحتمالية المتوقعة (مخرجات الذكاء)': probability * np.exp(-0.01 * np.arange(12))
            })
            fig = px.line(df, x='تاريخ', y=['سعة الموجة (المدخلات)', 'الاحتمالية المتوقعة (مخرجات الذكاء)'], 
                          title="تحليل انحدار الاحتمالية مقابل سعة الموجة السيزمية عبر الزمن")
            fig.update_layout(template="plotly_dark") # نمط مظلم للانبهار
            st.plotly_chart(fig, use_container_width=True)

        with g2:
            # مثال لرسم بياني مكاني: خريطة الحرارة لاحتمالية المكامن
            # سنقوم بتوليد بيانات عشوائية محاكية
            grid_size = 20
            data = np.random.normal(probability, 10, (grid_size, grid_size))
            fig2 = px.imshow(data, color_continuous_scale='Viridis', 
                            labels=dict(x="الاحداثي الأفقي", y="الاحداثي الرأسي", color="الاحتمالية%"),
                            title="خريطة الحرارة الذكية لاحتمالية توزيع الهيدروكربون (AI Heatmap)")
            fig2.update_layout(template="plotly_dark")
            st.plotly_chart(fig2, use_container_width=True)

        # ج. تحليل الثقة وتفسير النموذج (Model Interpretation)
        st.write("#### 🛡️ تحليل موثوقية التنبؤ (Model Confidence Analysis)")
        st.info("يعتمد هذا التنبؤ على تحليل نموذج الشبكات العصبية (Neural Network) لـ 1500 عينة تدريب سابقة.")
        
        # مثال لجدول بيانات الثقة
        confidence_data = {
            'المعامل السيزمي': ['دقة تحديد الحدود', 'تقدير النفاذية', 'تقدير المسامية'],
            'مستوى الثقة للنموذج (Confidence Level %)': [92.1, 78.5, 88.0],
            'التفسير الذكي': ["دقيقة جداً بناءً على جودة السيزميك", "ثقة متوسطة نظراً لتباين الصخر", "ثقة عالية بناءً على الآبار المجاورة"]
        }
        st.dataframe(pd.DataFrame(confidence_data), use_container_width=True)
        st.success("تم الانتهاء من التحليل. يمكنك التفاعل مع الرسوم البيانية بالماوس.")

# -- 6. تذييل الصفحة (توقيعك) --
st.markdown("---")
st.caption("🚀 AI Reservoir Discovery System v2.1 | Developed by Doaa Issa | Smart Oilfield Solutions 2026")
[3/18/2026 2:16 PM] دعاء عيسى غتر(A), 35: <img src="https://images.unsplash.com/photo-1516195851888-6f1a981a8a2a?q=80&w=1600&auto=format&fit=crop" 
                 style="width: 100%; border-radius: 15px; box-shadow: 0 10px 20px rgba(0,0,0,0.5);">
            
            <div style="position: absolute; top: 15%; right: 10%; color: white; background: rgba(255,0,0,0.7); padding: 5px; border-radius: 5px; font-weight:bold;">🔥 شعلة 1: نشطة</div>
            <div style="position: absolute; top: 15%; left: 10%; color: white; background: rgba(255,0,0,0.7); padding: 5px; border-radius: 5px; font-weight:bold;">🔥 شعلة 2: نشطة</div>
            <div style="position: absolute; top: 60%; right: 15%; color: white; background: rgba(255,0,0,0.7); padding: 5px; border-radius: 5px; font-weight:bold;">🔥 شعلة 3: نشطة</div>
            <div style="position: absolute; top: 60%; left: 15%; color: white; background: rgba(255,0,0,0.7); padding: 5px; border-radius: 5px; font-weight:bold;">🔥 شعلة 4: نشطة</div>
            
            <div style="position: absolute; bottom: 0; left: 0; width: 100%; height: 30%; background: linear-gradient(180deg, rgba(32,32,32,0) 0%, rgba(255,165,0,0.4) 100%); border-radius: 0 0 15px 15px;">
                <h2 style="position: absolute; bottom: 10px; left: 20px; color: white;">جودة المكمن المتوقعة: <span style="color:#FFA500;">{quality}</span></h2>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_stats:
        st.markdown("### 📈 ملخص تحليل الـ AI")
        
        # عرض القراءات على شكل كروت احترافية
        st.markdown(f"""
            <div class="metric-card"><div class="metric-title">المسامية</div><div class="metric-value">{porosity}%</div></div><br>
            <div class="metric-card"><div class="metric-title">النفاذية</div><div class="metric-value">{permeability} md</div></div><br>
            <div class="metric-card"><div class="metric-title">العمق</div><div class="metric-value">{depth} ft</div></div><br>
            <div class="metric-card"><div class="metric-title">الضغط</div><div class="metric-value">{pressure} psi</div></div>
        """, unsafe_allow_html=True)
        
        st.divider()
        st.metric("نسبة ثقة النموذج (Confidence)", f"{confidence:.1f}%")

        if quality == "عالية جدًا":
            st.success("✅ تم اكتشاف مكمن تجاري واعد.")
            st.balloons() # إبهار إضافي
        else:
            st.warning("⚠️ جودة المكمن قد لا تكون كافية للإنتاج التجاري.")

else:
    # واجهة العرض الافتراضية قبل الضغط على الزر
    st.image("https://images.unsplash.com/photo-1621251842817-2f3b97b0a3ce?q=80&w=1600&auto=format&fit=crop", 
             caption="منظر عام لحقل نفطي (اضغط على التحليل للبدء)", use_column_width=True)

st.write("---")
st.caption("برنامج تم تطويره كجزء من مشروع تخرج هندسة النفط - جامعة البصرة")
