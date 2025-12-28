import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة العامة
st.set_page_config(page_title="شركة حلباوي إخوان", layout="wide")

# 2. تصميم الواجهة (CSS)
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; background-color: #0E1117; }
    .category-header { 
        background-color: #e9ecef; 
        color: #1E3A8A; 
        padding: 8px 15px; 
        border-radius: 5px; 
        font-weight: bold; 
        font-size: 18px; 
        margin-top: 10px;
        margin-bottom: 5px;
        border-right: 5px solid #fca311;
        text-align: right;
    }
    .item-name { color: white !important; font-weight: bold !important; font-size: 19px !important; margin: 0; }
    input { 
        background-color: #ffffcc !important; 
        color: black !important; 
        font-weight: bold !important; 
        height: 45px !important; 
        font-size: 22px !important; 
        -webkit-text-fill-color: black !important;
    }
    .header-box { background-color: #1E3A8A; color: white; text-align: center; padding: 15px; border-radius: 10px; margin-bottom: 20px; }
    .stButton button { background-color: #1E3A8A; color: white !important; font-weight: bold; height: 50px; }
    .streamlit-expanderHeader { background-color: #1E3A8A !important; color: white !important; font-size: 20px !important; border-radius: 5px; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

RECEIVING_NUMBER = "9613220893"

def render_list(items_list, key_suffix, order_dict, label_suffix):
    for item in items_list:
        if item.startswith("-"):
            st.markdown(f'<div class="category-header">{item[1:]}</div>', unsafe_allow_html=True)
        else:
            c1, c2 = st.columns([3, 1])
            with c1: st.markdown(f'<p class="item-name">{item}</p>', unsafe_allow_html=True)
            with c2:
                q = st.number_input("", min_value=0, step=1, key=f"{key_suffix}_{item}", label_visibility="collapsed")
                if q > 0: order_dict[f"{item} ({label_suffix})"] = q

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

# --- نموذج الحبوب المكتمل ---
elif st.session_state.page == 'grains':
    st.markdown('<div class="header-box"><h2>نموذج الحبوب</h2></div>', unsafe_allow_html=True)
    customer = st.text_input("👤 إسم الزبون:")
    full_order = {}

    with st.expander("📦 تعبئة 1000غ"):
        list_1000 = ["-حمص", "حمص ١٢", "حمص ٩", "حمص كسر", "-فول", "فول حب", "فول مجروش", "فول عريض", "-فاصوليا", "فاصوليا صنوبرية", "فاصوليا حمرا طويلة", "فاصوليا حمرا مدعبله", "فاصوليا عريضه", "-عدس", "عدس ابيض رفيع", "عدس احمر", "عدس موردي/بلدي", "عدس عريض", "-برغل", "برغل اسمر ناعم", "برغل اسمر خشن", "برغل اشقر ناعم", "برغل اشقر خشن", "برغل اشقر زماتي", "-ارز", "ارز مصري", "ارز إيطالي", "ارز اميركي", "ارز بسمتي", "ارز عنبري", "ارز ناعم", "-سكر", "سكر حب", "سكر اسمر", "سكر ناعم", "-طحين", "طحين فرخة", "سميد", "غود ميدل", "غودمارك", "طحين زيرو", "طحين فقش", "طحين اسمر", "طحين ذره", "-زعتر", "زعتر محوج", "زعتر اكسترا", "-مختلف", "فريك مجروش", "مغربيه", "ذرة بوشار", "ذره مجروشه"]
        render_list(list_1000, "g1k", full_order, "1000غ")

    with st.expander("📦 تعبئة 500غ"):
        list_500 = ["-سمسم", "سمسم مقشور", "سمسم محمص", "سمسم بلدي محمص", "-نشاء", "نشاء ناعم", "نشاء حب", "-زعتر", "زعتر محوج", "زعتر اكسترا", "زعتر حلبي", "-اكل عصفور", "بسيبيسة مشكله", "بسيبسه ساده", "قمبز", "دخن", "بزر ميال الشمس", "-علب", "مغلي جاهز", "مغلي بدون سكر", "مهلبيه", "مهلبيه ظرف", "سحلب", "خلطة كرسبي", "خلطة بروستد", "-ذره", "ذره بوشار", "ذره مجروشه", "-ترمس", "ترمس حلو", "ترمس مر", "-سكر", "سكر ناعم", "سكر نبات", "سكر اسمر", "-شوفان", "شوفان مبروش", "شوفان حب", "-مختلف", "فاصوليا عريضة", "فريك مجروش", "فول عريض", "برش الهند", "أرز ناعم", "كشك", "ملوخيه", "كعك مطحون", "خميرة باكيت", "كاكاو", "طحين ذرة", "بزر كتان"]
        render_list(list_500, "g500", full_order, "500غ")

    with st.expander("📦 تعبئة 200غ"):
        list_200 = ["-سمسم", "مقشور", "محمص", "محمص بلدي", "-نشاء", "حب", "ناعم", "-فرمسيل", "شوكولا", "ملون", "-ملوخية", "نايلون", "كرتون", "-زعتر", "محوج", "حلبي", "-مختلف", "برش جوز الهند", "بامية زهرة", "فلافل علب", "كشك بلدي", "بطاطا شيبس", "كاكاو", "كعك مطحون", "بزر كتان"]
        render_list(list_200, "g200", full_order, "200غ")

    with st.expander("📋 تعبئة مختلفة"):
        list_misc = ["-سكر نبات", "100 غ × 12", "200 غ × 12", "-ملح", "ناعم 700 غ × 24", "ناعم 3 كلغ × 6", "خشن 1 كلغ × 12", "-علب", "فانيليا 20 غ × 12", "باكينغ بودر 20 غ × 12", "-كرتون", "صنوبر × 12", "مسكة حب × 25", "-سمسم", "مقشور 100 غ × 12", "محمص 100 غ × 12", "-زهورات", "زهورات 100 غ × 12", "زهورات 200 غ × 12", "-قمح", "مقشور 2 كلغ", "مقشور 5 كلغ", "-مختلف", "بابونج 100 غ × 12", "بطاطا شيبس 100 غ", "بامية زهرة 100 غ", "كاكاو 100 غ"]
        render_list(list_misc, "gmisc", full_order, "مختلف")

    if st.button("🚀 إرسال طلبية الحبوب", use_container_width=True):
        if customer and full_order:
            msg = f"طلبية حبوب: {customer}\n" + "\n".join([f"• {k}: {v}" for k, v in full_order.items()])
            st.markdown(f'<a href="https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}" target="_blank" style="background:#25d366;color:white;padding:15px;display:block;text-align:center;text-decoration:none;border-radius:10px;font-weight:bold;">تأكيد الإرسال</a>', unsafe_allow_html=True)
    if st.button("🔙 عودة"): st.session_state.page = 'home'; st.rerun()

# --- نموذج البهارات بنظام الكبسة ---
elif st.session_state.page == 'spices':
    st.markdown('<div class="header-box"><h2>نموذج البهارات</h2></div>', unsafe_allow_html=True)
    customer_s = st.text_input("👤 إسم الزبون:")
    spice_order = {}

    with st.expander("🌶️ بهارات ناعمة وخاصة 50 غرام"):
        st.markdown('<div class="category-header">بهارات ناعمة 50 غ دزينة</div>', unsafe_allow_html=True)
        list_sp50 = ["بهار حلو", "فلفل أسود", "فلفل أحمر", "قرفة", "سبع بهارات", "دقة كعك", "كمون", "كزبرة", "كراوية", "كاري", "سماق", "يانسون", "عقدة صفراء", "فليفلة حلوة", "حامض", "ثوم مجفف", "شومر", "زعتر أوريغانو", "بفتاك", "بابريكا"]
        render_list(list_sp50, "sp50", spice_order, "50غ")

        st.markdown('<div class="category-header">بهارات خاصة 50 غرام</div>', unsafe_allow_html=True)
        list_spec50 = ["كبة", "فلافل", "مغربية", "كبسة", "دجاج", "طاووق", "بيتزا", "همبرغر", "شاورما لحمة", "شاورما دجاج", "كفتة", "سمك", "سجق", "كنتكي", "مقانق", "فاهيتا", "فيلادلفيا", "مشاوي", "برياني", "اسكالوب دجاج", "بروستد", "كرسبي", "فرنسيسكو", "ناغتس", "أرز", "تطبيقة", "صيني", "روستو", "مكسيكانا", "صيادية", "منسف لحمة", "ستيك", "غريل أرجنتيني"]
        render_list(list_spec50, "spec50", spice_order, "50غ خاصة")

    if st.button("🚀 إرسال طلبية البهارات", use_container_width=True):
        if customer_s and spice_order:
            msg = f"طلبية بهارات: {customer_s}\n" + "\n".join([f"• {k}: {v}" for k, v in spice_order.items()])
            st.markdown(f'<a href="https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}" target="_blank" style="background:#25d366;color:white;padding:15px;display:block;text-align:center;text-decoration:none;border-radius:10px;font-weight:bold;">تأكيد الإرسال</a>', unsafe_allow_html=True)
    if st.button("🔙 عودة"): st.session_state.page = 'home'; st.rerun()
