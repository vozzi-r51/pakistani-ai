import streamlit as st
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

if lang=='en':
    st.title('Image Animation')
    st.write('Animate faces and images with lip-sync and emotions!')
    image = st.file_uploader('Upload image', type=['png','jpg','jpeg'])
    if st.button('Animate'):
        st.info('Animation will appear here (API integration pending).')
else:
    st.title('تصویر اینیمیشن')
    st.write('چہرے اور تصاویر کو لپ سنک اور جذبات کے ساتھ اینیمیٹ کریں!')
    image = st.file_uploader('تصویر اپلوڈ کریں', type=['png','jpg','jpeg'])
    if st.button('اینیمیٹ کریں'):
        st.info('اینیمیشن یہاں ظاہر ہوگی (API انٹیگریشن باقی ہے)۔')

show_footer(lang) 