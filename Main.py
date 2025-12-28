# --- نموذج الحبوب المطور ---
elif st.session_state.page == 'grains':
    st.markdown('<div class="header-box"><h2>📦 طلبية حبوب - النموذج الرقمي</h2></div>', unsafe_allow_html=True)
    customer = st.text_input("👤 إسم الزبون:")
    
    # سنضع كود الـ HTML هنا ليرسم الجدول الأزرق
    grain_table_html = """
    <div style="direction: rtl; font-family: sans-serif; color: #1E3A8A;">
        <table style="width: 100%; border-collapse: collapse; border: 2px solid #1E3A8A;">
            <tr style="background-color: #f0f7ff;">
                <th colspan="3" style="border: 1px solid #1E3A8A; padding: 10px;">تعبئة 1000 غ</th>
            </tr>
            <tr style="background-color: #e2e8f0; font-size: 12px;">
                <th style="border: 1px solid #1E3A8A; width: 40%;">الصنف</th>
                <th style="border: 1px solid #1E3A8A; width: 30%;">العدد</th>
                <th style="border: 1px solid #1E3A8A; width: 30%;">الطرد</th>
            </tr>
            <tr>
                <td style="border: 1px solid #1E3A8A; padding: 5px;">حمص فحلي - 12 -</td>
                <td style="border: 1px solid #1E3A8A;"><input type="number" style="width:100%; border:none; text-align:center;"></td>
                <td style="border: 1px solid #1E3A8A;"><input type="number" style="width:100%; border:none; text-align:center;"></td>
            </tr>
            <tr>
                <td style="border: 1px solid #1E3A8A; padding: 5px;"><b>غود مارك 907 غ</b></td>
                <td style="border: 1px solid #1E3A8A;"><input type="number" style="width:100%; border:none; text-align:center;"></td>
                <td style="border: 1px solid #1E3A8A;"><input type="number" style="width:100%; border:none; text-align:center;"></td>
            </tr>
        </table>
    </div>
    """
    
    # عرض الجدول الأزرق
    st.components.v1.html(grain_table_html, height=300, scrolling=True)

    if st.button("🔙 عودة"): 
        st.session_state.page = 'menu'
        st.rerun()

