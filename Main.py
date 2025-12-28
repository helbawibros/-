import streamlit as st
import urllib.parse

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="شركة حلباوي إخوان", layout="wide")

# 2. تصميم الواجهة (CSS) - نضعه مباشرة بدون Cache لتجنب الأخطاء
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stNumberInput label { color: #1E3A8A !important; font-weight: bold; font-size: 16px; }
    .header-box { background-color: #1E3A8A; color: white; text-align: center; padding: 15px; border-radius: 12px; margin-bottom: 20px; }
    .section-header { background-color: #f0f7ff; padding: 8px; border-right: 5px solid #1E3A8A; font-weight: bold; margin-top: 10px; color: #1E3A8A; }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'home'

# الرقم المعتمد لاستقبال الطلبات
RECEIVING_NUMBER = "9613220893"

# --- الصفحة الرئيسية ---
if st.session_state.page == 'home':
    # عرض الصورة باستخدام الاسم الصحيح "Logo .JPG"
    # سنستخدم الرابط المباشر لضمان السرعة والظهور
    logo_url = "https://raw.githubusercontent.com/helbawibros/-/main/Logo%20.JPG"
    st.image(logo_url, use_container_width=True)
    
    st.markdown('<h2 style="text-align: center; color: #1E3A8A;">نظام تسجيل الطلبات الرقمي</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 ابدأ تسجيل طلبية جديدة", use_container_width=True):
            st.session_state.page = 'menu'
            st.rerun()

# --- قائمة اختيار النموذج ---
elif st.session_state.page == 'menu':
    st.markdown('<div class="header-box"><h1>شركة حلباوي إخوان</h1></div>', unsafe_allow_html=True)
    st.markdown('<h3 style="text-align: center;">اختر نوع الطلبية</h3>', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🌾 نموذج الحبوب", use_container_width=True):
            st.session_state.page = 'grains'
            st.rerun()
    with c2:
        if st.button("🌶️ نموذج البهارات", use_container_width=True):
            st.session_state.page = 'spices'
            st.rerun()
    
    st.divider()
    if st.button("⬅️ عودة للواجهة الرئيسية"):
        st.session_state.page = 'home'
        st.rerun()

# --- نموذج الحبوب (عينة الأصناف) ---
elif st.session_state.page == 'grains':
    st.markdown('<div class="header-box"><h2>📦 طلبية حبوب</h2></div>', unsafe_allow_html=True)
    customer = st.text_input("👤 إسم الزبون:")
    
    order = {}
    st.markdown('<p class="section-header">⚖️ اختر الأصناف والكميات</p>', unsafe_allow_html=True)
    
    # مثال للأصناف (سيتم استبدالها بالقائمة الكاملة)
    grains_list = ["فحلي-12", "فحلي-10", "عدس مجروش", "فاصوليا عريضة", "حمص حب", "أرز مصري", "سكر 2ك"]
    
    c1, c2 = st.columns(2)
    for idx, item in enumerate(grains_list):
        with (c1 if idx % 2 == 0 else c2):
            q = st.number_input(item, min_value=0, step=1, key=f"g_{item}")
            if q > 0: order[item] = q

    if st.button("✅ إرسال الطلب عبر واتساب", use_container_width=True):
        if customer and order:
            msg = f"طلبية حبوب جديدة\nالزبون: {customer}\n---\n" + "\n".join([f"• {k}: {v}" for k, v in order.items()])
            link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{link}" target="_blank" style="background-color: #25d366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">اضغط هنا لتأكيد الإرسال</a>', unsafe_allow_html=True)
        else:
            st.warning("يرجى إدخال اسم الزبون وصنف واحد على الأقل")
            
    if st.button("🔙 عودة"):
        st.session_state.page = 'menu'
        st.rerun()

# --- نموذج البهارات ---
elif st.session_state.page == 'spices':
    st.markdown('<div class="header-box"><h2>🌶️ طلبية بهارات</h2></div>', unsafe_allow_html=True)
    customer_s = st.text_input("👤 إسم الزبون:")
    
    order_s = {}
    st.markdown('<p class="section-header">✨ اختر البهارات المطلوبة</p>', unsafe_allow_html=True)
    
    spices_list = ["بهار حلو", "فلفل أسود", "كمون ناعم", "قرفة ناعمة", "سبع بهارات", "كاري"]
    
    s1, s2 = st.columns(2)
    for idx, item in enumerate(spices_list):
        with (s1 if idx % 2 == 0 else s2):
            q = st.number_input(item, min_value=0, step=1, key=f"s_{item}")
            if q > 0: order_s[item] = q

    if st.button("✅ إرسال الطلب عبر واتساب", use_container_width=True):
        if customer_s and order_s:
            msg = f"طلبية بهارات جديدة\nالزبون: {customer_s}\n---\n" + "\n".join([f"• {k}: {v}" for k, v in order_s.items()])
            link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{link}" target="_blank" style="background-color: #25d366; color: white; padding: 15px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-weight: bold;">اضغط هنا لتأكيد الإرسال</a>', unsafe_allow_html=True)

    if st.button("🔙 عودة"):
        st.session_state.page = 'menu'
        st.rerun()

