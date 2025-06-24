import streamlit as st
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

if lang=='en':
    st.title('About Pak AI')
    st.write('''
        Pak AI is Pakistan's first AI-powered creative suite. Our mission is to empower creators, businesses, and students with advanced AI tools for image, voice, and video generation in both English and Urdu.
        
        **Mission:** Democratize AI creativity for everyone in Pakistan and beyond.
    ''')
else:
    st.title('Pak AI کے بارے میں')
    st.write('''
        Pak AI پاکستان کا پہلا اے آئی تخلیقی ٹول ہے۔ ہمارا مقصد تخلیق کاروں، کاروباری حضرات اور طلبہ کو جدید AI ٹیکنالوجی کے ذریعے تصاویر، آواز اور ویڈیوز بنانے کی سہولت فراہم کرنا ہے۔
        
        **مشن:** ہر پاکستانی کے لیے AI تخلیقی صلاحیتوں کو عام کرنا۔
    ''')

show_footer(lang) 