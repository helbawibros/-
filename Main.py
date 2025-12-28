import streamlit as st
import urllib.parse

st.set_page_config(page_title="Hiebawi Bros Order", layout="centered")

# تنسيق لجعل الخانات فوق الصورة بالضبط
st.markdown("""
    <style>
    .reportview-container { background: white; }
    .img-overlay-container {
        position: relative;
        display: inline-block;
        width: 100%;
    }
    .input-box {
        position: absolute;
        background: rgba(255, 255, 0, 0.3); /* لون أصفر شفاف للتأكد من المكان */
        border: 1px solid #1E3A8A;
        text-align: center;
        font-weight: bold;
        color: black;
    }
    /* تعديل حجم الخط والشفافية */
    input {
        background-color: transparent !important;
        border: none !important;
        text-align: center !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

if 'page' not in st.session_state:
    st.session_state.page = 'grains'

RECEIVING_NUMBER = "9613220893"

if st.session_state.page == 'grains':
    st.write("### نموذج الحبوب - تعبئة 1000غ (تجربة)")
    
    # حاوية الصورة والخانات
    st.markdown('<div class="img-overlay-container">', unsafe_allow_html=True)
    
    # عرض صورة الورقة الأصلية
    st.image("https://raw.githubusercontent.com/helbawibros/-/main/image.png", use_container_width=True)
    
    # --- توزيع خانات الإدخال برمجياً فوق الأعمدة الصفراء ---
    # ملاحظة: هذه الإحداثيات (top, left) سنضبطها بدقة الآن
    order_data = {}
    
    # تجربة أول 5 أصناف في عمود 1000غ
    # سنستخدم st.number_input ونضعه في حاوية CSS
    
    items_1000g = ["فحلي 12", "فحلي 10", "فحلي 9", "كسر", "حب"]
    
    # هذه الخانات ستظهر حالياً تحت بعضها للتأكد من عمل الواتساب
    # بمجرد موافقتك سأقوم بدمجها "فوق" الصورة بالإحداثيات
    customer = st.text_input("إسم الزبون:")
    
    col1, col2 = st.columns([2,1])
    with col2:
        st.write("العدد (الأصفر)")
        for item in items_1000g:
            val = st.number_input(f"{item}", min_value=0, step=1, key=item)
            if val > 0:
                order_data[item] = val

    if st.button("إرسال الطلب المكتوب"):
        if customer and order_data:
            msg = f"طلبية حبوب\nالزبون: {customer}\n" + "\n".join([f"{k}: {v}" for k, v in order_data.items()])
            link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
            st.markdown(f'<a href="{link}" target="_blank" style="background:green;color:white;padding:10px;text-decoration:none;">تأكيد واتساب</a>', unsafe_allow_html=True)

