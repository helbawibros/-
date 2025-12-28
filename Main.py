import streamlit as st
import urllib.parse

# إعدادات التطبيق الرسمي لشركة حلباوي إخوان - Helbawibros
st.set_page_config(page_title="Helbawibros Orders", layout="wide")

st.markdown("""
    <style>
    .header { color: #1E3A8A; text-align: center; font-family: 'Arial'; border-bottom: 3px solid #1E3A8A; padding-bottom: 10px; }
    .item-row { background-color: #F8FAFC; padding: 10px; border-radius: 5px; border-right: 5px solid #1E3A8A; margin-bottom: 5px; font-weight: bold; color: #1E3A8A; }
    .cat-title { background-color: #1E3A8A; color: white; padding: 10px; border-radius: 8px; text-align: center; margin-top: 25px; font-size: 20px; }
    .wa-button { background-color: #25D366; color: white; padding: 20px; text-align: center; border-radius: 12px; font-size: 22px; font-weight: bold; text-decoration: none; display: block; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<h1 class="header">Helbawibros <br> طلب مبيعات شركة حلباوي إخوان</h1>', unsafe_allow_html=True)

# بيانات الطلبية
c1, c2 = st.columns(2)
with c1: customer = st.text_input("اسم الزبون / Customer:")
with c2: salesman = st.text_input("اسم المندوب / Salesman:")

# القائمة الكاملة المستخرجة من الصور
sections = {
    "تعبئة 1000غ": ["فحلي - 12", "فحلي - 10", "فحلي - 9", "كسر", "حب", "مجروش", "عريض", "أبيض رفيع", "أحمر", "أحمر موردي"],
    "تعبئة 500غ": ["مفتول", "محمص", "محمص بلدي", "نشاء ناعم", "زعتر إكسترا", "مغربية", "عدس مجروش", "فاصوليا عريضة"],
    "بهارات ناعمة (دزينة)": ["بهار حلو", "فلفل أسود", "فلفل أحمر", "قرفة", "سبع بهارات", "دقة كعك", "كمون", "كزبرة", "كاري", "سماق"],
    "بهارات حب": ["بهار حلو حب", "فلفل أسود حب", "كمون حب", "كزبرة حب", "يانسون", "حبة البركة", "خردل", "سمسم"],
    "أصناف متنوعة": ["أرز أميركي", "أرز مصري", "سكر حب", "برغل ناعم", "برغل خشن", "عدس حب", "فاصوليا عريضة", "حمص حب"]
}

order_list = []

# بناء الواجهة برمجياً
for section, items in sections.items():
    st.markdown(f'<p class="cat-title">{section}</p>', unsafe_allow_html=True)
    for item in items:
        cols = st.columns([3, 1, 1])
        with cols[0]: st.markdown(f'<div class="item-row">{item}</div>', unsafe_allow_html=True)
        with cols[1]: count = st.number_input("العدد", min_value=0, step=1, key=f"c_{item}", label_visibility="collapsed")
        with cols[2]: pack = st.number_input("الطرد", min_value=0, step=1, key=f"p_{item}", label_visibility="collapsed")
        
        if count > 0 or pack > 0:
            order_list.append(f"▫️ {item}: (العدد: {count} | الطرد: {pack})")

# زر الواتساب
st.divider()
company_phone = "96170000000" # استبدل برقمك الفعلي

if st.button("تجهيز رسالة الواتساب للشركة"):
    if not customer or not order_list:
        st.error("⚠️ يرجى إدخال اسم الزبون والكميات أولاً!")
    else:
        full_msg = f"📦 *طلب مبيعات جديد - Helbawibros*\n👤 *الزبون:* {customer}\n👨‍💼 *المندوب:* {salesman}\n" + "-"*20 + "\n" + "\n".join(order_list)
        wa_url = f"https://wa.me/{company_phone}?text={urllib.parse.quote(full_msg)}"
        st.markdown(f'<a href="{wa_url}" target="_blank" class="wa-button">إرسال عبر واتساب الآن ✅</a>', unsafe_allow_html=True)
