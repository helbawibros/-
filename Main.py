# --- تجربة نموذج الحبوب المطور (الجدول الأزرق التفاعلي) ---
elif st.session_state.page == 'grains':
    st.markdown('<div class="header-box"><h3>نموذج الحبوب (تفاعلي)</h3></div>', unsafe_allow_html=True)
    
    # كود الـ HTML والـ CSS للجدول الكامل
    html_order_form = """
    <style>
        .full-table { direction: rtl; width: 100%; border-collapse: collapse; font-family: Arial; color: #1E3A8A; border: 2px solid #1E3A8A; }
        .full-table th, .full-table td { border: 1px solid #1E3A8A; text-align: center; padding: 4px; font-size: 11px; }
        .main-head { background-color: #f0f7ff; font-weight: bold; font-size: 13px; }
        .side-title { writing-mode: vertical-rl; transform: rotate(180deg); background: #f9f9f9; font-weight: bold; width: 25px; }
        input { width: 100%; border: none; text-align: center; color: blue; font-weight: bold; background: #fffde7; outline: none; }
        input:focus { background: #fff59d; }
    </style>

    <table class="full-table">
        <tr class="main-head">
            <th colspan="4">تعبئة 1000 غ</th>
            <th colspan="4">تعبئة 500 غ</th>
        </tr>
        <tr class="main-head">
            <th>الصنف</th><th>النوع</th><th>العدد</th><th>الطرد</th>
            <th>الصنف</th><th>النوع</th><th>العدد</th><th>الطرد</th>
        </tr>
        
        <tr>
            <td rowspan="4" class="side-title">حمص</td>
            <td>فحلي - 12 -</td><td><input type="number"></td><td><input type="number"></td>
            <td rowspan="3" class="side-title">سمسم</td>
            <td>مقشور</td><td><input type="number"></td><td><input type="number"></td>
        </tr>
        <tr>
            <td>فحلي - 10 -</td><td><input type="number"></td><td><input type="number"></td>
            <td>محمص</td><td><input type="number"></td><td><input type="number"></td>
        </tr>
        <tr>
            <td>فحلي - 9 -</td><td><input type="number"></td><td><input type="number"></td>
            <td>بلدي</td><td><input type="number"></td><td><input type="number"></td>
        </tr>
        <tr>
            <td>كسر</td><td><input type="number"></td><td><input type="number"></td>
            <td rowspan="2" class="side-title">نشاء</td>
            <td>حب</td><td><input type="number"></td><td><input type="number"></td>
        </tr>

        <tr>
            <td rowspan="4" class="side-title">طحين</td>
            <td>غود ميدل</td><td><input type="number"></td><td><input type="number"></td>
            <td>ناعم</td><td><input type="number"></td><td><input type="number"></td>
        </tr>
        <tr>
            <td><b>غود مارك 907 غ</b></td><td><input type="number"></td><td><input type="number"></td>
            <td rowspan="4" class="side-title">زعتر</td>
            <td>محوج</td><td><input type="number"></td><td><input type="number"></td>
        </tr>
        <tr>
            <td>زيرو</td><td><input type="number"></td><td><input type="number"></td>
            <td>اكسترا</td><td><input type="number"></td><td><input type="number"></td>
        </tr>
        <tr>
            <td>فرخة</td><td><input type="number"></td><td><input type="number"></td>
            <td>حلبي</td><td><input type="number"></td><td><input type="number"></td>
        </tr>
    </table>
    """
    
    # عرض الجدول
    components.html(html_order_form, height=800, scrolling=True)

    if st.button("🔙 عودة للقائمة"):
        st.session_state.page = 'home'
        st.rerun()
