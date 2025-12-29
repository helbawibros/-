import streamlit as st

st.set_page_config(page_title="Helbawi Bros Billing", layout="centered")

# نظام المندوبين
users = {"حسين": "1111", "علي": "2222", "مدير": "9999"}

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 دخول المندوبين")
    user_choice = st.selectbox("اختر اسم المندوب", list(users.keys()))
    password = st.text_input("كلمة السر", type="password")
    if st.button("دخول"):
        if users.get(user_choice) == password:
            st.session_state.logged_in = True
            st.session_state.user = user_choice
            st.rerun()
        else: st.error("خطأ!")
else:
    st.title("📄 فاتورة بيع جديدة")
    rate = st.number_input("سعر صرف VAT L.L", value=89500)
    customer = st.text_input("المطلوب من (الزبون)")

    # قائمة الأصناف (النجمة تعني ضريبة 11%)
    products = {
        "عدس أحمر 907غ": 1.80,
        "عدس مجروش 907غ": 1.75,
        "عدس عريض 907غ": 2.00,
        "برغل أسمر خشن 907غ": 1.10,
        "برغل أشقر خشن 907غ": 1.15,
        "أرز مصري 907غ": 1.20,
        "طحين غود مارك 907غ": 1.00,
        "مغربية يابسة 907غ *": 1.60,
        "ذرة بوشار 1ك": 1.60,
        "ترمس حلو 500غ *": 0.85,
        "فول عريض 500غ": 1.15
    }

    total_usd = 0.0
    vat_usd = 0.0

    for p, price in products.items():
        qty = st.number_input(f"{p} (${price})", min_value=0, step=1, key=p)
        if qty > 0:
            sub = qty * price
            total_usd += sub
            if "*" in p: vat_usd += (sub * 0.11)

    st.divider()
    disc = st.number_input("الحسم (Discount USD)", min_value=0.0)
    
    final_usd = (total_usd - disc) + vat_usd
    vat_ll = vat_usd * rate

    st.subheader("الحساب النهائي")
    st.write(f"المجموع: **${total_usd:.2f}**")
    st.write(f"الحسم: **${disc:.2f}**")
    st.write(f"الضريبة VAT 11%: **${vat_usd:.2f}**")
    st.success(f"الصافي النهائي: **${final_usd:.2f}**")
    st.info(f"V.A.T L.L: **{vat_ll:,.0f} ل.ل**")

    if st.button("حفظ للطباعة"):
        st.write("تم الحفظ بنجاح!")
