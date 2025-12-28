import streamlit as st
import urllib.parse

# إعدادات الصفحة
st.set_page_config(page_title="تجرية حلباوي إخوان", layout="wide")

# تصميم الواجهة
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stNumberInput label { color: #1E3A8A !important; font-weight: bold; }
    .header-box { background-color: #1E3A8A; color: white; text-align: center; padding: 10px; border-radius: 10px; }
    .img-container { border: 3px solid #1E3A8A; padding: 5px; background: white; border-radius: 10px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

RECEIVING_NUMBER = "9613220893"

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    st.image("https://raw.githubusercontent.com/helbawibros/-/main/Logo%20.JPG", use_container_width=True)
    st.markdown('<h2 style="text-align: center; color: #1E3A8A;">تجربة نظام الطلبات</h2>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🌾 فتح نموذج الحبوب", use_container_width=True):
            st.session_state.page = 'grains'
            st.rerun()
    with col2:
        if st.button("🌶️ فتح نموذج البهارات", use_container_width=True):
            st.session_state.page = 'spices'
            st.rerun()

# --- تجربة نموذج الحبوب ---
elif st.session_state.page == 'grains':
    st.markdown('<div class="header-box"><h3>نموذج الحبوب (صورة الـ A4 كمرجع)</h3></div>', unsafe_allow_html=True)
    
    # عرض صورة الورقة البيضاء (الحبوب)
    st.markdown('<div class="img-container">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/helbawibros/-/main/image.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    customer = st.text_input("👤 إسم الزبون:")
    
    # عينة أصناف للتجربة من الجدول
    items = ["فحلي-12", "فحلي-10", "عدس مجروش", "فاصوليا عريضة", "حمص حب", "سكر 2ك"]
    order = {}
    
    col1, col2 = st.columns(2)
    for idx, item in enumerate(items):
        with (col1 if idx % 2 == 0 else col2):
            q = st.number_input(item, min_value=0, step=1, key=f"g_{item}")
            if q > 0: order[item] = q

    if st.button("✅ تجربة إرسال الطلب", use_container_width=True):
        if customer and order:
            msg = f"تجربة طلبية\nالزبون: {customer}\n---\n" + "\n".join([f"• {k}: {v}" for k, v in order.items()])
            link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{link}" target="_blank" style="background-color: #25d366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">اضغط للإرسال للشركة</a>', unsafe_allow_html=True)
    
    if st.button("🔙 عودة"):
        st.session_state.page = 'home'
        st.rerun()

# --- تجربة نموذج البهارات ---
elif st.session_state.page == 'spices':
    st.markdown('<div class="header-box"><h3>نموذج البهارات (الورقة الزرقاء)</h3></div>', unsafe_allow_html=True)
    
    # عرض صورة الورقة الزرقاء (البهارات)
    st.markdown('<div class="img-container">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/helbawibros/-/main/Logo%20.JPG", use_container_width=True) # مؤقتا حتى ترفع الصورة الزرقاء
    st.markdown('</div>', unsafe_allow_html=True)
    
    customer_s = st.text_input("👤 إسم الزبون:")
    # أصناف تجريبية
    items_s = ["بهار حلو", "فلفل أسود", "كمون ناعم"]
    order_s = {}
    
    s1, s2 = st.columns(2)
    for idx, item in enumerate(items_s):
        with (s1 if idx % 2 == 0 else s2):
            q = st.number_input(item, min_value=0, step=1, key=f"s_{item}")
            if q > 0: order_s[item] = q
            
    if st.button("🔙 عودة"):
        st.session_state.page = 'home'
        st.rerun()

