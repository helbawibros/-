import streamlit as st
import urllib.parse

st.set_page_config(page_title="Hiebawi Order", layout="wide")

# تنسيق الخط ليكون واضح جداً كما طلبت
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stNumberInput label { font-size: 20px !important; color: #1E3A8A !important; font-weight: bold; }
    input { height: 45px !important; font-size: 22px !important; }
    .header { background-color: #fca311; padding: 10px; text-align: center; font-weight: bold; border-radius: 5px; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

RECEIVING_NUMBER = "9613220893"
order = {}

st.markdown('<div class="header">نموذج الحبوب - تعبئة 1000غ</div>', unsafe_allow_html=True)
customer = st.text_input("👤 إسم الزبون (مطلوب):")

# قائمة الأصناف حسب ترتيب ورقتك تماماً
items_1000g = [
    "فحلي - 12 -", "فحلي - 10 -", "فحلي - 9 -", "كسر", "حب", 
    "مجروش", "عريض", "صنوبرية", "حمراء طويلة", "حمراء مدعبلة",
    "عريضة", "أبيض رفيع", "أحمر", "أحمر موردي", "مجروش (عدس)"
]

# عرض الخانات بشكل عمودي (خانة العدد الصفراء)
for item in items_1000g:
    # جعل الخانة تأخذ مساحة واضحة للكتابة
    val = st.number_input(f"العدد لـ {item}", min_value=0, step=1, key=item)
    if val > 0:
        order[item] = val

st.divider()

if st.button("✅ إرسال الطلبية كاملة"):
    if customer and order:
        msg = f"طلبية حبوب\nالزبون: {customer}\n" + "\n".join([f"{k}: {v}" for k, v in order.items()])
        link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
        st.markdown(f'<a href="{link}" target="_blank" style="background-color: #25d366; color: white; padding: 20px; text-decoration: none; border-radius: 10px; display: block; text-align: center; font-size: 20px;">إضغط هنا لتأكيد الإرسال للشركة</a>', unsafe_allow_html=True)
    else:
        st.error("الرجاء كتابة اسم الزبون وتعبئة صنف واحد على الأقل")


