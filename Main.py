import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة
st.set_page_config(page_title="شركة حلباوي إخوان", layout="wide")

# 2. تصميم الواجهة
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stNumberInput label { color: #1E3A8A !important; font-weight: bold; }
    .header-box { background-color: #1E3A8A; color: white; text-align: center; padding: 20px; border-radius: 15px; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# الرقم المعتمد لاستقبال الطلبات
RECEIVING_NUMBER = "9613220893"

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    # تعديل السطر ليتطابق مع اسم الملف في GitHub: "Logo .JPG"
    # سنحاول قراءته محلياً أو عبر رابط مباشر لضمان الظهور
    logo_filename = "Logo .JPG"
    logo_url = "https://raw.githubusercontent.com/helbawibros/-/main/Logo%20.JPG"
    
    try:
        st.image(logo_filename, use_container_width=True)
    except:
        st.image(logo_url, use_container_width=True)
    
    st.markdown('<h2 style="text-align: center; color: #1E3A8A;">نظام تسجيل الطلبات الرقمي</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 ابدأ تسجيل طلبية جديدة", use_container_width=True):
            st.session_state.page = 'menu'

# --- قائمة اختيار النموذج ---
elif st.session_state.page == 'menu':
    st.markdown('<div class="header-box"><h1>شركة حلباوي إخوان</h1></div>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌾 نموذج الحبوب", use_container_width=True): st.session_state.page = 'grains'
    with col2:
        if st.button("🌶️ نموذج البهارات", use_container_width=True): st.session_state.page = 'spices'
    st.divider()
    if st.button("🔙 عودة للرئيسية"): st.session_state.page = 'home'

# --- نموذج الحبوب (عينة) ---
elif st.session_state.page == 'grains':
    st.markdown('<div class="header-box"><h2>📦 طلبية حبوب</h2></div>', unsafe_allow_html=True)
    customer = st.text_input("👤 إسم الزبون:")
    order = {}
    items = ["فحلي-12", "فحلي-10", "عدس", "فاصوليا", "حمص", "سكر 2ك"]
    for i in items:
        q = st.number_input(i, min_value=0, step=1, key=f"g_{i}")
        if q > 0: order[i] = q

    if st.button("✅ إرسال الطلب عبر واتساب"):
        if customer and order:
            msg = f"طلبية حبوب جديدة\nالزبون: {customer}\n---\n" + "\n".join([f"• {k}: {v}" for k, v in order.items()])
            link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{link}" target="_blank" style="background-color: #25d366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">اضغط هنا لتأكيد الإرسال للشركة</a>', unsafe_allow_html=True)
    if st.button("🔙 عودة"): st.session_state.page = 'menu'

# --- نموذج البهارات (عينة) ---
elif st.session_state.page == 'spices':
    st.markdown('<div class="header-box"><h2>🌶️ طلبية بهارات</h2></div>', unsafe_allow_html=True)
    customer_s = st.text_input("👤 إسم الزبون:")
    order_s = {}
    items_s = ["بهار حلو", "فلفل أسود", "كمون", "قرفة"]
    for i in items_s:
        q = st.number_input(i, min_value=0, step=1, key=f"s_{i}")
        if q > 0: order_s[i] = q

    if st.button("✅ إرسال الطلب عبر واتساب"):
        if customer_s and order_s:
            msg = f"طلبية بهارات جديدة\nالزبون: {customer_s}\n---\n" + "\n".join([f"• {k}: {v}" for k, v in order_s.items()])
            link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{link}" target="_blank" style="background-color: #25d366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">اضغط هنا لتأكيد الإرسال للشركة</a>', unsafe_allow_html=True)
    if st.button("🔙 عودة"): st.session_state.page = 'menu'
