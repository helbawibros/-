import streamlit as st
import urllib.parse

st.set_page_config(page_title="شركة حلباوي إخوان", layout="wide")

st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stNumberInput label { color: #1E3A8A !important; font-weight: bold; font-size: 14px; }
    .header-box { background-color: #1E3A8A; color: white; text-align: center; padding: 15px; border-radius: 10px; margin-bottom: 20px; }
    .section-header { background-color: #e1f5fe; padding: 5px; border-right: 5px solid #1E3A8A; font-weight: bold; margin-top: 10px; border-radius: 0 5px 5px 0; font-size: 16px; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    st.markdown('<div class="header-box"><h1>شركة حلباوي إخوان</h1><h3>نظام طلبات المبيعات الذكي</h3></div>', unsafe_allow_html=True)
    if st.button("🚀 الدخول إلى الطلبيات"):
        st.session_state.page = 'menu'

# --- اختيار النموذج ---
elif st.session_state.page == 'menu':
    st.markdown('<h2 style="text-align: center; color: #1E3A8A;">اختر النموذج المطلوب</h2>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌾 نموذج الحبوب  )"): st.session_state.page = 'grains'
    with col2:
        if st.button("🌶️ نموذج البهارات (الورقة الزرقاء)"): st.session_state.page = 'spices'
    st.write("---")
    if st.button("⬅️ عودة للرئيسية"): st.session_state.page = 'home'

# --- نموذج الحبوب الشامل ---
elif st.session_state.page == 'grains':
    st.markdown('<div class="header-box"><h2>نموذج طلب مبيعات (حبوب)</h2></div>', unsafe_allow_html=True)
    c_info1, c_info2 = st.columns(2)
    with c_info1: customer = st.text_input("إسم الزبون:")
    with c_info2: salesman = st.text_input("إسم المندوب:")
    
    order = {}
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<p class="section-header">تعبئة 1000غ</p>', unsafe_allow_html=True)
        items1 = ["فحلي-12", "فحلي-10", "فحلي-9", "كسر", "حب", "مجروش", "عريض", "صنوبرية", "حمراء طويلة", "حمراء مدعبلة", "عريضة", "أبيض رفيع", "أحمر", "أحمر موردي", "مجروش عريض", "أسمر ناعم", "أسمر خشن", "أشقر ناعم", "أشقر خشن", "أميركي", "إيطالي", "مصري", "بسمتي", "عنبري", "ناعم", "حب", "أسمر", "ناعم", "فرخة", "سميد", "غودميدل", "زيرو", "فستق", "فقش", "أسمر", "ذرة"]
        for i in items1:
            q = st.number_input(i, min_value=0, step=1, key=f"g1_{i}")
            if q > 0: order[f"{i} (1000g)"] = q

    with col2:
        st.markdown('<p class="section-header">تعبئة 500غ</p>', unsafe_allow_html=True)
        items2 = ["مفتور", "محمص", "محمص بلدي", "حب", "ناعم", "محوج", "إكسترا", "حلبي", "سوبر إكسترا", "ببيسة سادة", "ببيسة مشكلة", "قمبز", "دخن", "بزر نبال", "بيبي فود", "مغلي جاهز", "مهلبية", "سحلب", "خلطة كريسبي", "بوشار", "مجروشة", "حلو", "مر", "ناعم", "نبات", "بشرة", "مبروش", "مبشور", "فاصوليا عريضة", "فريك مجروش", "فول عريض", "برش جوز هند", "أرز ناعم", "كشك بلدي", "ملوخية", "لوبيا مسلات", "كعك مطحون", "خميرة", "كاكاو", "طحين ذرة", "بزر كتان"]
        for i in items2:
            q = st.number_input(i, min_value=0, step=1, key=f"g2_{i}")
            if q > 0: order[f"{i} (500g)"] = q

    with col3:
        st.markdown('<p class="section-header">تعبئة 200غ</p>', unsafe_allow_html=True)
        items3 = ["مفتور", "محمص", "محمص بلدي", "حب", "ناعم", "شوكولا", "ملون", "نايلون", "كرتون", "محوج", "حلبي", "برش جوز هند", "بامية زهرة", "فلافل علب", "كشك بلدي", "بطاطا شيبس", "كاكاو", "كعك مطحون", "بزر كتان"]
        for i in items3:
            q = st.number_input(i, min_value=0, step=1, key=f"g3_{i}")
            if q > 0: order[f"{i} (200g)"] = q

    with col4:
        st.markdown('<p class="section-header">مختلف</p>', unsafe_allow_html=True)
        items4 = ["حمص", "فول", "فاصوليا", "عدس", "برغل", "أرز أميركي", "أرز إيطالي", "أرز مصري", "سكر 2ك", "سكر 5ك", "طحين 5ك", "برغل أسمر ناعم", "برغل أسمر خشن", "بكينغ بودر", "فريميسال", "كاكاو", "صنوبر", "لوز", "فستق حلبي", "زبيب", "كاجو كسر", "ملوخية", "بامية", "كشك بلدي", "زهورات", "كعك مطحون", "نشاء", "مسكة"]
        for i in items4:
            q = st.number_input(i, min_value=0, step=1, key=f"g4_{i}")
            if q > 0: order[i] = q

    # إرسال
    my_phone = "96176510343" 
    if st.button("✅ إرسال طلب الحبوب"):
        if customer:
            msg = f"طلب حبوب - شركة حلباوي\nالزبون: {customer}\nالمندوب: {salesman}\n---\n" + "\n".join([f"• {k}: {v}" for k, v in order.items()])
            st.markdown(f'[اضغط للإرسال عبر واتساب](https://wa.me/{my_phone}?text={urllib.parse.quote(msg)})')
    if st.button("🔙 عودة"): st.session_state.page = 'menu'

# --- نموذج البهارات الشامل ---
elif st.session_state.page == 'spices':
    st.markdown('<div class="header-box"><h2>نموذج طلب مبيعات (بهارات)</h2></div>', unsafe_allow_html=True)
    c_info1, c_info2 = st.columns(2)
    with c_info1: customer = st.text_input("إسم الزبون:")
    with c_info2: salesman = st.text_input("إسم المندوب:")
    
    order_s = {}
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<p class="section-header">بهارات ناعمة 50غ (دزينة)</p>', unsafe_allow_html=True)
        items_s1 = ["بهار حلو", "فلفل أسود", "فلفل أحمر", "قرفة", "سبع بهارات", "دقة كعك", "كمون", "كزبرة", "كراوية", "كاري", "يانسون", "سماق", "عقدة صفراء", "فليفلة حلوة", "بابريكا", "ثوم مجفف", "بصل مجفف", "شومر", "جوزة الطيب", "محلب", "قرنفل", "هال", "عصفر"]
        for i in items_s1:
            q = st.number_input(i, min_value=0, step=1, key=f"s1_{i}")
            if q > 0: order_s[f"{i} (50غ دزينة)"] = q

    with col2:
        st.markdown('<p class="section-header">بهارات حب 50غ (دزينة)</p>', unsafe_allow_html=True)
        items_s2 = ["بهار حلو", "فلفل أسود", "كمون", "كزبرة", "يانسون", "حبة البركة", "خردل", "خميرة", "حبق", "لوما", "زنجبيل", "شومر", "حلبة"]
        for i in items_s2:
            q = st.number_input(i, min_value=0, step=1, key=f"s2_{i}")
            if q > 0: order_s[f"{i} (حب 50غ دزينة)"] = q
        
        st.markdown('<p class="section-header">بهارات ناعمة 20غ (دزينة)</p>', unsafe_allow_html=True)
        for i in ["جوزة الطيب", "محلب", "نشاء", "قرنفل", "هال", "زنجبيل", "بهار أبيض", "عصفر", "صبغة حمراء"]:
            q = st.number_input(i, min_value=0, step=1, key=f"s20_{i}")
            if q > 0: order_s[f"{i} (20غ دزينة)"] = q

    with col3:
        st.markdown('<p class="section-header">بهارات خاصة / فلت</p>', unsafe_allow_html=True)
        items_s3 = ["كبة", "مغربية", "فلافل", "كبسة", "دجاج", "طاووق", "بيتزا", "همبرغر", "شاورما لحمة", "شاورما دجاج", "كفتة", "سمك", "سجق", "كنتاكي", "فاهيتا", "فيلادلفيا", "مكسيكانا", "برياني", "منسف", "ستيك"]
        for i in items_s3:
            q = st.number_input(i, min_value=0, step=1, key=f"s3_{i}")
            if q > 0: order_s[f"{i} (فلت)"] = q

    my_phone = "9613220893"
    if st.button("✅ إرسال طلب البهارات"):
        if customer:
            msg = f"طلب بهارات - شركة حلباوي\nالزبون: {customer}\nالمندوب: {salesman}\n---\n" + "\n".join([f"• {k}: {v}" for k, v in order_s.items()])
            st.markdown(f'[اضغط للإرسال عبر واتساب](https://wa.me/{my_phone}?text={urllib.parse.quote(msg)})')
    if st.button("🔙 عودة"): st.session_state.page = 'menu'
