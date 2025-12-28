import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة العامة
st.set_page_config(page_title="شركة حلباوي إخوان", layout="wide")

# 2. تصميم الواجهة (CSS) لتنسيق العناوين والخانات والخطوط
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
        margin-top: 20px;
        margin-bottom: 10px;
        border-right: 8px solid #fca311;
        text-align: right;
    }
    .stNumberInput label { color: #333 !important; font-size: 18px; font-weight: bold; }
    input { background-color: #ffffcc !important; font-weight: bold !important; height: 45px !important; font-size: 20px !important; }
    .header-box { background-color: #1E3A8A; color: white; text-align: center; padding: 15px; border-radius: 10px; margin-bottom: 20px; }
    .stButton button { background-color: #1E3A8A; color: white; font-weight: bold; height: 50px; }
    </style>
    """, unsafe_allow_html=True)

# 3. إدارة التنقل بين الصفحات
if 'page' not in st.session_state:
    st.session_state.page = 'home'

RECEIVING_NUMBER = "9613220893"

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

# --- نموذج الحبوب (التعديل الجديد حسب طلبك) ---
elif st.session_state.page == 'grains':
    st.markdown('<div class="header-box"><h2>نموذج الحبوب - تعبئة 907غ / 1000غ</h2></div>', unsafe_allow_html=True)
    
    # عرض الصورة الأصلية كمرجع
    st.image("https://raw.githubusercontent.com/helbawibros/-/main/image.png", use_container_width=True)

    customer = st.text_input("👤 إسم الزبون (مطلوب):")
    
    # القائمة التي أرسلتها أنت بالترتيب
    grains_list = [
        "-حمص", "حمص ١٢", "حمص ٩", "حمص كسر",
        "-فول", "فول حب", "فول مجروش", "فول عريض",
        "-فاصوليا", "فاصوليا صنوبرية", "فاصوليا حمرا طويلة", "فاصوليا حمرا مدعبله", "فاصوليا عريضه",
        "-عدس", "عدس ابيض رفيع", "عدس احمر", "عدس موردي/بلدي", "عدس عريض",
        "-برغل", "برغل اسمر ناعم", "برغل اسمر خشن", "برغل اشقر ناعم", "برغل اشقر خشن", "برغل اشقر زماتي",
        "-ارز", "ارز مصري", "ارز إيطالي", "ارز اميركي", "ارز بسمتي", "ارز عنبري", "ارز ناعم",
        "-سكر", "سكر حب", "سكر اسمر", "سكر ناعم",
        "-طحين", "طحين فرخة", "سميد", "غود ميدل", "غودمارك", "طحين زيرو", "طحين فقش", "طحين اسمر", "طحين ذره",
        "-زعتر", "زعتر محوج", "زعتر اكسترا",
        "-مختلف", "فريك مجروش", "مغربيه", "ذرة بوشار", "ذره مجروشه"
    ]

    order = {}

    # عرض الأصناف مع العناوين
    for item in grains_list:
        if item.startswith("-"):
            st.markdown(f'<div class="category-header">{item[1:]}</div>', unsafe_allow_html=True)
        else:
            col_name, col_input = st.columns([3, 1])
            with col_name:
                st.write(f"**{item}**")
            with col_input:
                q = st.number_input("", min_value=0, step=1, key=f"gr_{item}", label_visibility="collapsed")
                if q > 0:
                    order[item] = q

    st.markdown("---")
    
    col_btns = st.columns(2)
    with col_btns[0]:
        if st.button("🚀 إرسال الطلبية (واتساب)", use_container_width=True):
            if customer and order:
                msg = f"طلبية حبوب (1000غ)\nالزبون: {customer}\n" + "\n".join([f"• {k}: {v}" for k, v in order.items()])
                link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
                st.markdown(f'<a href="{link}" target="_blank" style="background:#25d366;color:white;padding:15px;display:block;text-align:center;text-decoration:none;border-radius:10px;font-weight:bold;">تأكيد الإرسال</a>', unsafe_allow_html=True)
            else:
                st.warning("يرجى إدخال اسم الزبون وصنف واحد على الأقل")
    
    with col_btns[1]:
        if st.button("🔙 العودة للرئيسية", use_container_width=True):
            st.session_state.page = 'home'
            st.rerun()

# --- نموذج البهارات (سيتم تعديله لاحقاً بنفس الطريقة) ---
elif st.session_state.page == 'spices':
    st.markdown('<div class="header-box"><h2>نموذج البهارات</h2></div>', unsafe_allow_html=True)
    if st.button("🔙 العودة للرئيسية"):
        st.session_state.page = 'home'
        st.rerun()
    st.info("بانتظار قائمة أسماء البهارات لبرمجتها بنفس الطريقة...")
