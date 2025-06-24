import streamlit as st
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

if lang=='en':
    st.title('Pricing')
    st.write('Choose the plan that fits your needs:')
    st.markdown('''
    | Plan      | Features                                 | Price      |
    |-----------|------------------------------------------|------------|
    | Free      | 10 credits/month, watermark, basic tools | PKR 0      |
    | Pro       | 500 credits/month, HD export, all tools  | PKR 2,500  |
    | Business  | 5000 credits/month, team, API access     | PKR 15,000 |
    ''')
else:
    st.title('قیمتیں')
    st.write('اپنی ضرورت کے مطابق پیکج منتخب کریں:')
    st.markdown('''
    | پیکج      | فیچرز                                   | قیمت      |
    |-----------|------------------------------------------|------------|
    | فری       | 10 کریڈٹس/ماہ، واٹرمارک، بنیادی اوزار   | 0 روپے    |
    | پرو       | 500 کریڈٹس/ماہ، ایچ ڈی ایکسپورٹ، سب اوزار| 2,500 روپے|
    | بزنس      | 5000 کریڈٹس/ماہ، ٹیم، API ایکسیس        | 15,000 روپے|
    ''')

show_footer(lang) 