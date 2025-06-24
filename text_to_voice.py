import streamlit as st
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

voices = ['Male 1', 'Male 2', 'Female 1', 'Female 2', 'Urdu Male', 'Urdu Female', 'Hindi', 'Arabic', 'English', 'AI Voice']

if lang=='en':
    st.title('Text to Voice')
    st.write('Convert your text into natural voice in multiple languages!')
    text = st.text_area('Enter text')
    voice = st.selectbox('Select Voice', voices)
    if st.button('Generate Voice'):
        st.info('Voice generation will appear here (API integration pending).')
    st.markdown('---')
    st.subheader('Sample Voices')
    st.audio('static/audio/sample1.mp3')
else:
    st.title('متن سے آواز')
    st.write('اپنے متن کو مختلف زبانوں میں قدرتی آواز میں بدلیں!')
    text = st.text_area('متن لکھیں')
    voice = st.selectbox('وائس منتخب کریں', voices)
    if st.button('آواز بنائیں'):
        st.info('وائس جنریشن یہاں ظاہر ہوگی (API انٹیگریشن باقی ہے)۔')
    st.markdown('---')
    st.subheader('نمونہ آوازیں')
    st.audio('static/audio/sample1.mp3')

show_footer(lang) 