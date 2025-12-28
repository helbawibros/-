import streamlit as st
import urllib.parse

st.set_page_config(page_title="Hiebawi Order", layout="wide")

# تنسيق الخط والخانات لتكون واضحة جداً للمندوب
st.markdown("""
    <style>
    .main { direction: rtl; text-align: right; }
    .stNumberInput label { font-size: 18px !important; color: #1E3A8A !important; font-weight: bold; }
    .img-box { border: 2px solid #1E3A8A; border-radius: 10px; padding: 5px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

RECEIVING_NUMBER = "9613220893"
order = {}

st.title("📝 نموذج طلب مبيعات")
customer = st.text_input("👤 إسم الزبون:")

# عرض الصورة الأصلية (image.png) للتأكد من ظهورها
# استخدمنا الرابط الخام (Raw) لضمان عدم ظهور علامة [?]
image_url = "https://raw.githubusercontent.com/helbawibros/-/main/image.png"

st.markdown('<div class="img-box">', unsafe_allow_html=True)
st.image(image_url, caption="ورقة الحبوب الأصلية (مرجع)", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

st.info("قم بتعبئة الأعداد في الخانات أدناه بناءً على الورقة أعلاه")

# تقسيم الأصناف لأعمدة سهلة الاستخدام على الموبايل
items = ["فحلي-12", "فحلي-10", "فحلي-9", "كسر", "حب", "مجروش", "أرز مصري", "سكر 2ك"]

col1, col2 = st.columns(2)
for idx, item in enumerate(items):
    with (col1 if idx % 2 == 0 else col2):
        # خانة العدد (التي تقابل اللون الأصفر في ورقتك)
        val = st.number_input(item, min_value=0, step=1, key=item)
        if val > 0:
            order[item] = val

if st.button("✅ إرسال الطلبية عبر واتساب", use_container_width=True):
    if customer and order:
        msg = f"طلبية من: {customer}\n" + "\n".join([f"{k}: {v}" for k, v in order.items()])
        link = f"https://api.whatsapp.com/send?phone={RECEIVING_NUMBER}&text={urllib.parse.quote(msg)}"
        st.markdown(f'<a href="{link}" target="_blank" style="background:#25d366; color:white; padding:15px; text-decoration:none; display:block; text-align:center; border-radius:10px;">إضغط هنا لتأكيد الإرسال</a>', unsafe_allow_html=True)

