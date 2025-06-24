import streamlit as st
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

if lang=='en':
    st.title('Video Generator')
    st.write('Create videos from text or images!')
    video_type = st.selectbox('Video Type', ['Text to Video', 'Image to Video'])
    prompt = st.text_area('Enter prompt or description')
    images = st.file_uploader('Upload images (optional)', type=['png','jpg','jpeg'], accept_multiple_files=True)
    if st.button('Generate Video'):
        st.info('Video generation will appear here (API integration pending).')
else:
    st.title('ویڈیو جنریٹر')
    st.write('متن یا تصویر سے ویڈیوز بنائیں!')
    video_type = st.selectbox('ویڈیو کی قسم', ['متن سے ویڈیو', 'تصویر سے ویڈیو'])
    prompt = st.text_area('پرامپٹ یا تفصیل لکھیں')
    images = st.file_uploader('تصاویر اپلوڈ کریں (اختیاری)', type=['png','jpg','jpeg'], accept_multiple_files=True)
    if st.button('ویڈیو بنائیں'):
        st.info('ویڈیو جنریشن یہاں ظاہر ہوگی (API انٹیگریشن باقی ہے)۔')

show_footer(lang) 