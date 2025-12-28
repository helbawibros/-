import streamlit as st
import urllib.parse
import os

# إعدادات الصفحة
st.set_page_config(page_title="شركة حلباوي إخوان", layout="wide")

# تصميم الواجهة
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stNumberInput label { color: #1E3A8A !important; font-weight: bold; }
    .header-box { background-color: #1E3A8A; color: white; text-align: center; padding: 20px; border-radius: 15px; margin-bottom: 25px; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

RECEIVING_NUMBER = "9613220893"

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    # الحل البرمجي لضمان ظهور الصورة
    image_path = "image.png"
    
    if os.path.exists(image_path):
        st.image(image_path, use_container_width=True)
    else:
        # محاولة أخيرة برابط مباشر إذا لم يجد الملف محلياً
        st.image("https://raw.githubusercontent.com/helbawibros/-/main/image.png", use_container_width=True)
    
    st.markdown('<h2 style="text-align: center; color: #1E3A8A;">نظام تسجيل الطلبات الرقمي</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 ابدأ تسجيل طلبية جديدة", use_container_width=True):
            st.session_state.page = 'menu'

# باقي الكود (menu, grains, spices) يبقى كما هو في النسخة الأخيرة
