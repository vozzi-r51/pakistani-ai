import streamlit as st
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

if lang=='en':
    st.title('Voice Dubbing')
    st.write('Translate and dub audio/video from one language to another!')
    media = st.file_uploader('Upload audio or video', type=['mp3','wav','mp4','m4a'])
    target_lang = st.selectbox('Target Language', ['English','Urdu','Arabic','Hindi'])
    if st.button('Dub'):
        st.info('Dubbing will appear here (API integration pending).')
else:
    st.title('وائس ڈبنگ')
    st.write('آڈیو/ویڈیو کو ایک زبان سے دوسری زبان میں ترجمہ اور ڈب کریں!')
    media = st.file_uploader('آڈیو یا ویڈیو اپلوڈ کریں', type=['mp3','wav','mp4','m4a'])
    target_lang = st.selectbox('ہدف زبان', ['انگلش','اردو','عربی','ہندی'])
    if st.button('ڈب کریں'):
        st.info('ڈبنگ یہاں ظاہر ہوگی (API انٹیگریشن باقی ہے)۔')

show_footer(lang) 