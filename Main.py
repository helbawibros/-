import streamlit as st
import urllib.parse

# 1. إعداد الصفحة
st.set_page_config(page_title="Hiebawi Bros", layout="centered")

# 2. كود لإظهار الصورة بشكل مضمون
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stImage { border: 2px solid #1E3A8A; border-radius: 10px; }
    .order-box { background-color: #f9f9f9; padding: 10px; border-radius: 10px; border: 1px solid #ddd; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

RECEIVING_NUMBER = "9613220893"

st.title("نموذج مبيعات حلباوي")
customer = st.text_input("إسم الزبون:")

# رابط الصورة المباشر من مستودعك
image_url = "https://raw.githubusercontent.com/helbawibros/-/main/image.png"

# إظهار الصورة 
try:
    st.image(image_url, use_container_width=True)
except:
    st.error("تعذر تحميل الصورة من السيرفر، يرجى التأكد من اتصال الإنترنت")

st.markdown("---")
st.subheader("✍️ تعبئة الكميات (حسب ترتيب الورقة)")

# سأضع لك أول 5 أصناف بشكل "أزرار كبيرة" لتجربة السرعة والسهولة
items = ["فحلي-12", "فحلي-10", "فحلي-9", "كسر", "حب"]
order = {}

for item in items:
    # تصميم بسيط: اسم الصنف وبجانبه خانة الرقم
    col_name, col_input = st.columns([3, 1])
    with col_name:
        st.write(f"**{item}**")
    with col_input:
        val = st.number_input("", min_value=0, step=1, key=item, label_visibility="collapsed")
        if val > 0:
            order[item] = val

if st.button("🚀 إرسال الطلب الآن", use_container_width=True):
    if customer and order:
        msg = f"طلبية حبوب\nالزبون: {customer}\n" + "\n".join([f"{k}: {v}" for k, v in order.items()])
        link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
        st.markdown(f'<a href="{link}" target="_blank" style="background:green;color:white;padding:15px;display:block;text-align:center;text-decoration:none;border-radius:10px;">تأكيد الإرسال للشركة</a>', unsafe_allow_html=True)
    else:
        st.warning("يرجى إدخال الإسم والكمية")
