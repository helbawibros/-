import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة العامة
st.set_page_config(page_title="شركة حلباوي إخوان", layout="wide")

# 2. تصميم الواجهة (CSS) لتنسيق العناوين والخانات
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .category-header { 
        background-color: #e9ecef; 
        color: #1E3A8A; 
        padding: 8px 15px; 
        border-radius: 5px; 
        font-weight: bold; 
        font-size: 20px; 
        margin-top: 15px;
        margin-bottom: 10px;
        border-right: 8px solid #fca311;
        text-align: right;
    }
    .section-title {
        background-color: #1E3A8A;
        color: white;
        padding: 10px;
        text-align: center;
        border-radius: 10px;
        margin-top: 30px;
        margin-bottom: 20px;
        font-size: 24px;
        font-weight: bold;
    }
    .stNumberInput label { color: #333 !important; font-size: 18px; font-weight: bold; }
    input { background-color: #ffffcc !important; font-weight: bold !important; height: 45px !important; font-size: 20px !important; }
    .header-box { background-color: #1E3A8A; color: white; text-align: center; padding: 15px; border-radius: 10px; margin-bottom: 20px; }
    .stButton button { background-color: #1E3A8A; color: white; font-weight: bold; height: 50px; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

RECEIVING_NUMBER = "9613220893"

# دالة لعرض القوائم مع العناوين
def render_list(items_list, key_suffix, order_dict, label_suffix):
    for item in items_list:
        if item.startswith("-"):
            st.markdown(f'<div class="category-header">{item[1:]}</div>', unsafe_allow_html=True)
        else:
            c1, c2 = st.columns([3, 1])
            with c1: st.write(f"**{item}**")
            with c2:
                q = st.number_input("", min_value=0, step=1, key=f"{key_suffix}_{item}", label_visibility="collapsed")
                if q > 0:
                    order_dict[f"{item} ({label_suffix})"] = q

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    st.image("https://raw.githubusercontent.com/helbawibros/-/main/Logo%20.JPG", use_container_width=True)
    st.markdown('<div class="header-box"><h1>نظام طلبيات حلباوي إخوان</h1></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌾 فتح نموذج الحبوب", use_container_width=True):
            st.session_state.page = 'grains'
            st.rerun()
    with col2:
        if st.button("🌶️ فتح نموذج البهارات", use_container_width=True):
            st.session_state.page = 'spices'
            st.rerun()

# --- نموذج الحبوب الكامل ---
elif st.session_state.page == 'grains':
    st.markdown('<div class="header-box"><h2>نموذج الحبوب - الطلبية الكاملة</h2></div>', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/helbawibros/-/main/image.png", use_container_width=True)

    customer = st.text_input("👤 إسم الزبون (مطلوب):")
    full_order = {}

    # 1. قسم 1000غ
    st.markdown('<div class="section-title">تعبئة 907 غرام / 1000 غرام</div>', unsafe_allow_html=True)
    list_1000 = [
        "-حمص", "حمص ١٢", "حمص ٩", "حمص كسر", "-فول", "فول حب", "فول مجروش", "فول عريض",
        "-فاصوليا", "فاصوليا صنوبرية", "فاصوليا حمرا طويلة", "فاصوليا حمرا مدعبله", "فاصوليا عريضه",
        "-عدس", "عدس ابيض رفيع", "عدس احمر", "عدس موردي/بلدي", "عدس عريض",
        "-برغل", "برغل اسمر ناعم", "برغل اسمر خشن", "برغل اشقر ناعم", "برغل اشقر خشن", "برغل اشقر زماتي",
        "-ارز", "ارز مصري", "ارز إيطالي", "ارز اميركي", "ارز بسمتي", "ارز عنبري", "ارز ناعم",
        "-سكر", "سكر حب", "سكر اسمر", "سكر ناعم",
        "-طحين", "طحين فرخة", "سميد", "غود ميدل", "غودمارك", "طحين زيرو", "طحين فقش", "طحين اسمر", "طحين ذره",
        "-زعتر", "زعتر محوج", "زعتر اكسترا", "-مختلف", "فريك مجروش", "مغربيه", "ذرة بوشار", "ذره مجروشه"
    ]
    render_list(list_1000, "g1k", full_order, "1000غ")

    # 2. قسم 500غ
    st.markdown('<div class="section-title">تعبئة 454 غرام / 500 غرام</div>', unsafe_allow_html=True)
    list_500 = [
        "-سمسم", "سمسم مقشور", "سمسم محمص", "سمسم بلدي محمص", "-نشاء", "نشاء ناعم", "نشاء حب",
        "-زعتر", "زعتر محوج", "زعتر اكسترا", "زعتر حلبي", "-اكل عصفور", "بسيبيسة مشكله", "بسيبسه ساده", "قمبز", "دخن", "بزر ميال الشمس",
        "-علب", "مغلي جاهر", "مغلي بدون سكر", "مهلبيه", "مهلبيه ظرف", "سحلب", "خلطة كرسبي", "خلطة بروستد",
        "-ذره", "ذره بوشار", "ذره مجروشه", "-ترمس", "ترمس حلو", "ترمس مر",
        "-سكر", "سكر ناعم", "سكر نبات", "سكر اسمر", "-شوفان", "شوفان مبروش", "شوفان حب",
        "-مختلف", "فاصوليا عريضة", "فريك مجروش", "فول عريض", "برش الهند", "أرز ناعم", "كشك", "ملوخيه", "كعك مطحون", "خميرة باكيت", "كاكاو", "طحين ذرة", "بزر كتان"
    ]
    render_list(list_500, "g500", full_order, "500غ")

    # 3. قسم 200غ
    st.markdown('<div class="section-title">تعبئة 200 غرام</div>', unsafe_allow_html=True)
    list_200 = [
        "-سمسم", "مقشور", "محمص", "محمص بلدي", "-نشاء", "حب", "ناعم", "-فرمسيل", "شوكولا", "ملون",
        "-ملوخية", "نايلون", "كرتون", "-زعتر", "محوج", "حلبي",
        "-مختلف", "برش جوز الهند", "بامية زهرة", "فلافل علب", "كشك بلدي", "بطاطا شيبس", "كاكاو", "كعك مطحون", "بزر كتان"
    ]
    render_list(list_200, "g200", full_order, "200غ")

    # 4. قسم تعبئة مختلفة
    st.markdown('<div class="section-title">تعبئة مختلفة</div>', unsafe_allow_html=True)
    list_misc = [
        "-سكر نبات", "100 غ × 12", "200 غ × 12", "-ملح", "ناعم 700 غ × 24", "ناعم 3 كلغ × 6", "خشن 1 كلغ × 12",
        "-علب", "فانيليا 20 غ × 12", "باكينغ بودر 20 غ × 12", "-كرتون", "صنوبر × 12", "مسكة حب × 25",
        "-سمسم", "مقشور 100 غ × 12", "محمص 100 غ × 12", "-زهورات", "زهورات 100 غ × 12", "زهورات 200 غ × 12",
        "-قمح", "مقشور 2 كلغ", "مقشور 5 كلغ", "-مختلف", "بابونج 100 غ × 12", "بطاطا شيبس 100 غ", "بامية زهرة 100 غ", "كاكاو 100 غ"
    ]
    render_list(list_misc, "gmisc", full_order, "مختلف")

    st.markdown("---")
    if st.button("🚀 إرسال طلبية الحبوب بالكامل", use_container_width=True):
        if customer and full_order:
            msg = f"طلبية حبوب جديدة\nالزبون: {customer}\n" + "\n".join([f"• {k}: {v}" for k, v in full_order.items()])
            link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{link}" target="_blank" style="background:#25d366;color:white;padding:15px;display:block;text-align:center;text-decoration:none;border-radius:10px;font-weight:bold;">تأكيد الإرسال للشركة</a>', unsafe_allow_html=True)
        else:
            st.error("يرجى إدخال اسم الزبون وتعبئة الكميات")

    if st.button("🔙 العودة للرئيسية"):
        st.session_state.page = 'home'
        st.rerun()

# --- صفحة البهارات ---
elif st.session_state.page == 'spices':
    st.markdown('<div class="header-box"><h2>نموذج البهارات (الورقة الزرقاء)</h2></div>')
    st.info("بانتظار قائمة البهارات لبرمجتها...")
    if st.button("🔙 عودة للرئيسية"):
        st.session_state.page = 'home'
        st.rerun()
