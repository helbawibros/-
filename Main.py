import streamlit as st
import urllib.parse

# 1. تفعيل خاصية السرعة القصوى
st.set_page_config(page_title="شركة حلباوي إخوان", layout="wide")

# منع إعادة تحميل التنسيقات عند كل ضغطة
@st.cache_data
def get_css():
    return """
    <style>
    .main { direction: rtl; text-align: right; }
    .stNumberInput label { color: #1E3A8A !important; font-weight: bold; }
    .header-box { background-color: #1E3A8A; color: white; text-align: center; padding: 15px; border-radius: 12px; }
    </style>
    """
st.markdown(get_css(), unsafe_allow_html=True)

# تحسين سرعة تحميل الصورة
@st.cache_data
def show_main_image():
    # الرابط المباشر للملف كما يظهر في GitHub عندك
    logo_url = "https://raw.githubusercontent.com/helbawibros/helbawibros/main/Logo%20.JPG"
    return st.image(logo_url, use_container_width=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

RECEIVING_NUMBER = "9613220893"

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    show_main_image()
    st.markdown('<h2 style="text-align: center; color: #1E3A8A;">نظام تسجيل الطلبات</h2>', unsafe_allow_html=True)
    
    if st.button("🚀 ابدأ تسجيل طلبية جديدة", use_container_width=True):
        st.session_state.page = 'menu'
        st.rerun() # تسريع الانتقال

# --- القائمة ---
elif st.session_state.page == 'menu':
    st.markdown('<div class="header-box"><h1>شركة حلباوي إخوان</h1></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌾 نموذج الحبوب", use_container_width=True):
            st.session_state.page = 'grains'
            st.rerun()
    with col2:
        if st.button("🌶️ نموذج البهارات", use_container_width=True):
            st.session_state.page = 'spices'
            st.rerun()
    if st.button("🔙 عودة"):
        st.session_state.page = 'home'
        st.rerun()

# --- نموذج الحبوب ---
elif st.session_state.page == 'grains':
    st.markdown('<div class="header-box"><h2>📦 طلبية حبوب</h2></div>', unsafe_allow_html=True)
    customer = st.text_input("👤 إسم الزبون:")
    
    # تحويل الأصناف إلى "أعمدة" يقلل من وقت الرندرة
    items = ["فحلي-12", "فحلي-10", "عدس", "فاصوليا", "حمص", "أرز مصري", "سكر 2ك"]
    order = {}
    
    c1, c2 = st.columns(2)
    for idx, item in enumerate(items):
        with (c1 if idx % 2 == 0 else c2):
            q = st.number_input(item, min_value=0, step=1, key=f"g_{item}")
            if q > 0: order[item] = q

    if st.button("✅ إرسال الطلب", use_container_width=True):
        if customer and order:
            msg = f"طلبية حبوب جديدة\nالزبون: {customer}\n---\n" + "\n".join([f"• {k}: {v}" for k, v in order.items()])
            link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{link}" target="_blank" style="background-color: #25d366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">اضغط للإرسال للشركة</a>', unsafe_allow_html=True)

    if st.button("🔙 عودة"):
        st.session_state.page = 'menu'
        st.rerun()
