import streamlit as st
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

if lang=='en':
    st.title('Voice to Text')
    st.write('Transcribe your audio to text in multiple languages!')
    audio = st.file_uploader('Upload audio file', type=['mp3','wav','m4a'])
    if st.button('Transcribe'):
        st.info('Transcription will appear here (API integration pending).')
else:
    st.title('آواز سے متن')
    st.write('اپنی آواز کو مختلف زبانوں میں متن میں تبدیل کریں!')
    audio = st.file_uploader('آڈیو اپلوڈ کریں', type=['mp3','wav','m4a'])
    if st.button('ٹرانسکرائب کریں'):
        st.info('ٹرانسکرپشن یہاں ظاہر ہوگی (API انٹیگریشن باقی ہے)۔')

show_footer(lang) 