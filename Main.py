import streamlit as st
import urllib.parse

# إعدادات الصفحة
st.set_page_config(page_title="شركة حلباوي إخوان - الطلبات", layout="wide")

# تصميم الواجهة (CSS) لجعل الخط واضحاً والخانات مريحة
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stNumberInput label { color: #1E3A8A !important; font-weight: bold; font-size: 18px; }
    .header-box { background-color: #1E3A8A; color: white; text-align: center; padding: 15px; border-radius: 10px; margin-bottom: 20px; }
    .img-container { border: 3px solid #1E3A8A; padding: 5px; background: white; border-radius: 10px; margin-bottom: 20px; }
    .stButton button { background-color: #1E3A8A; color: white; height: 50px; font-size: 20px; }
    input { background-color: #ffffcc !important; font-weight: bold !important; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

RECEIVING_NUMBER = "9613220893"

# دالة مساعدة لتقسيم الأصناف إلى أعمدة
def display_items(items_list, key_prefix):
    order = {}
    cols = st.columns(3) # تقسيم لـ 3 أعمدة لسرعة التصفح
    for idx, item in enumerate(items_list):
        with cols[idx % 3]:
            q = st.number_input(item, min_value=0, step=1, key=f"{key_prefix}_{idx}")
            if q > 0:
                order[item] = q
    return order

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    st.image("https://raw.githubusercontent.com/helbawibros/-/main/Logo%20.JPG", use_container_width=True)
    st.markdown('<div class="header-box"><h1>نظام طلبيات حلباوي إخوان</h1></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌾 نموذج الحبوب (A4)", use_container_width=True):
            st.session_state.page = 'grains'
            st.rerun()
    with col2:
        if st.button("🌶️ نموذج البهارات (الزرقاء)", use_container_width=True):
            st.session_state.page = 'spices'
            st.rerun()

# --- نموذج الحبوب (300 صنف) ---
elif st.session_state.page == 'grains':
    st.markdown('<div class="header-box"><h2>نموذج الحبوب - الطلبية الكاملة</h2></div>', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/helbawibros/-/main/image.png", use_container_width=True)
    
    customer = st.text_input("👤 إسم الزبون:")
    full_order = {}

    # 1. تعبئة 1000 غرام
    with st.expander("📦 تعبئة 1000غ (اضغط للفتح)", expanded=True):
        items_1000 = [
            "فحلي-12", "فحلي-10", "فحلي-9", "كسر", "حب", "مجروش", "عريض", "صنوبرية", "حمراء طويلة", "حمراء مدعبلة",
            "عريضة", "أبيض رفيع", "أحمر", "أحمر موردي", "مجروش (عدس)", "عريض (عدس)", "أسمر ناعم", "أسمر خشن", 
            "أشقر ناعم", "أشقر خشن", "أميركي", "إيطالي", "مصري", "بسمتي", "عنبري", "ناعم (سكر)", "حب (سكر)", 
            "أسمر (سكر)", "ناعم (برغل)", "فرخة", "سميد", "غود ميدل", "غود مارك 907غ", "زيرو", "فقش", "أسمر (طحين)", 
            "ذرة", "محوج", "اكسترا", "مقشور", "بقشرة", "حلو", "مر", "فريك مجروش", "مغربية", "لوبيا مسلات", "ذرة بوشار", "ذرة مجروشة"
        ]
        full_order.update(display_items(items_1000, "g1000"))

    # 2. تعبئة 500 غرام
    with st.expander("📦 تعبئة 500غ"):
        items_500 = [
            "مقشور (حمص)", "محمص", "محمص بلدي", "حب (نشاء)", "ناعم (نشاء)", "محوج (زعتر)", "اكسترا", "حلبي", 
            "سوبر اكسترا", "بسيسة سادة", "بسيسة مشكلة", "قمبز", "دخن", "بزر عباد الشمس", "بيبي فود", "مغلي جاهز", 
            "مغلي بدون سكر", "مهلبية", "مهلبية كبير", "سحلب", "خلطة كرسبي", "خلطة بروستد", "كوسكوس", "بوشار", 
            "مجروشة", "حلو (ترمس)", "مر (ترمس)", "ناعم (سكر)", "نبات", "بقشرة", "مبروش", "مقشور (لوز)", 
            "فاصوليا عريضة", "فريك مجروش", "فول عريض", "برش جوز هند", "أرز ناعم", "كشك بلدي", "ملوخية", 
            "لوبيا مسلات", "كعك مطحون", "خميرة باكيت", "كاكاو", "طحين ذرة", "بزر كتان"
        ]
        full_order.update(display_items(items_500, "g500"))

    # 3. تعبئة 200 غرام
    with st.expander("📦 تعبئة 200غ"):
        items_200 = [
            "مقشور", "محمص", "محمص بلدي", "حب", "ناعم", "شوكولا", "ملون", "نايلون", "كرتون", "محوج", "حلبي", 
            "برش جوز هند", "بامية زهرة", "فلافل علب", "كشك بلدي", "بطاطا شيبس", "كاكاو", "كعك مطحون", "بزر كتان"
        ]
        full_order.update(display_items(items_200, "g200"))

    # 4. قسم "مختلف" (الأصناف المتبقية)
    with st.expander("📋 مختلف"):
        items_misc = [
            "حمص", "فول", "فاصوليا", "عدس", "برغل", "أميركي 2 كلغ", "أميركي 5 كلغ", "إيطالي 2 كلغ", "إيطالي 5 كلغ",
            "مصري 2 كلغ", "مصري 5 كلغ", "حب 2 كلغ", "حب 5 كلغ", "غود مارك 5 كلغ", "غود ميدل 5 كلغ", "أسمر ناعم 5 كلغ",
            "أسمر خشن 5 كلغ", "برش جوز هند", "باكينغ بودر", "فرمسيل", "كاكاو", "صنوبر", "لوز", "لوز صنوبري", 
            "لوز شرحات", "جوز", "فستق حلبي", "زبيب", "كاجو كسر", "ملوخية", "بامية", "كشك بلدي", "زهورات", 
            "كعك مطحون", "نشاء", "مسكة"
        ]
        full_order.update(display_items(items_misc, "misc"))

    if st.button("🚀 إرسال طلب الحبوب للشركة", use_container_width=True):
        if customer and full_order:
            msg = f"طلبية حبوب جديدة\nالزبون: {customer}\n" + "\n".join([f"• {k}: {v}" for k, v in full_order.items()])
            link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{link}" target="_blank" style="background-color: #25d366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">تأكيد الإرسال عبر واتساب</a>', unsafe_allow_html=True)

    if st.button("🔙 العودة للرئيسية"):
        st.session_state.page = 'home'
        st.rerun()

# --- نموذج البهارات ---
elif st.session_state.page == 'spices':
    st.markdown('<div class="header-box"><h2>نموذج البهارات (الورقة الزرقاء)</h2></div>', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/helbawibros/-/main/Logo%20.JPG", use_container_width=True)
    
    customer_s = st.text_input("👤 إسم الزبون:")
    
    items_spices = [
        "بهار حلو", "فلفل أسود", "كمون ناعم", "قرفة ناعمة", "عقدة صفراء", "زنجبيل ناعم", "جوزة الطيب", 
        "فلفل أبيض", "بهار مشكل", "بهار دجاج", "بهار سمك", "بابريكا حلوة", "بابريكا حارة", "سماق بلدية", 
        "كزبرة ناعمة", "قرنفل ناعم", "هيل ناعم", "هيل حب", "زعتر محوج", "يانسون ناعم", "كراوية ناعمة"
    ] # يمكنك إضافة باقي البهارات هنا بنفس الطريقة
    
    order_s = display_items(items_spices, "sp")

    if st.button("🚀 إرسال طلب البهارات", use_container_width=True):
        if customer_s and order_s:
            msg = f"طلبية بهارات جديدة\nالزبون: {customer_s}\n" + "\n".join([f"• {k}: {v}" for k, v in order_s.items()])
            link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{link}" target="_blank" style="background-color: #25d366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">تأكيد الإرسال عبر واتساب</a>', unsafe_allow_html=True)

    if st.button("🔙 العودة للرئيسية"):
        st.session_state.page = 'home'
        st.rerun()
