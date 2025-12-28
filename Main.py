import streamlit as st
import urllib.parse

st.set_page_config(page_title="حلباوي - طلبية مبيعات", layout="centered")

# التنسيق السحري لوضع الخانات فوق الصورة بدقة
st.markdown("""
    <style>
    .paper-container {
        position: relative;
        width: 100%;
        max-width: 800px;
        margin: auto;
    }
    .order-img {
        width: 100%;
        display: block;
    }
    .input-field {
        position: absolute;
        background-color: rgba(255, 255, 0, 0.4); /* أصفر شفاف */
        border: 1px solid red;
        width: 40px;
        height: 20px;
        text-align: center;
        font-size: 12px;
    }
    /* إحداثيات تقريبية لأول 5 أصناف في عمود 1000غ - سيتم ضبطها بالملي */
    .pos1 { top: 15.5%; left: 81%; } 
    .pos2 { top: 17.5%; left: 81%; }
    .pos3 { top: 19.5%; left: 81%; }
    .pos4 { top: 21.5%; left: 81%; }
    .pos5 { top: 23.5%; left: 81%; }
    </style>
    """, unsafe_allow_html=True)

RECEIVING_NUMBER = "9613220893"

st.write("### تعبئة الطلبية مباشرة على الورقة")
customer = st.text_input("إسم الزبون:")

# بناء الورقة التفاعلية
st.markdown(f'''
    <div class="paper-container">
        <img src="https://raw.githubusercontent.com/helbawibros/-/main/image.png" class="order-img">
        
        <input type="number" class="input-field pos1" id="item1" placeholder="0">
        <input type="number" class="input-field pos2" id="item2" placeholder="0">
        <input type="number" class="input-field pos3" id="item3" placeholder="0">
        <input type="number" class="input-field pos4" id="item4" placeholder="0">
        <input type="number" class="input-field pos5" id="item5" placeholder="0">
    </div>
''', unsafe_allow_html=True)

# زر الإرسال التقليدي (لأن الأزرار داخل HTML تحتاج برمجة معقدة)
if st.button("تأكيد الطلب وإرسال واتساب"):
    st.info("سيتم ربط القيم المكتوبة أعلاه بالرسالة فور ضبط الإحداثيات")



