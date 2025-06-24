import streamlit as st
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

user = st.session_state.get('user', {'name': 'Guest', 'credits': 10, 'projects': 2})
if lang=='en':
    st.title('AI Tools Dashboard')
    st.write('Select a tool to get started:')
    st.info(f"Welcome, {user['name']} | Credits: {user['credits']} | Projects: {user['projects']}")
    tools = [
        ('Text to Image', 'Generate images from text prompts.'),
        ('Text to Voice', 'Convert text to natural voice.'),
        ('Voice to Text', 'Transcribe audio to text.'),
        ('Video Generator', 'Create videos from text or images.'),
        ('Image Animation', 'Animate faces and images.'),
        ('Voice Dubbing', 'Translate and dub audio/video.')
    ]
else:
    st.title('AI اوزار ڈیش بورڈ')
    st.write('شروع کرنے کے لیے کوئی ٹول منتخب کریں:')
    st.info(f"خوش آمدید، {user['name']} | کریڈٹس: {user['credits']} | پراجیکٹس: {user['projects']}")
    tools = [
        ('متن سے تصویر', 'متن سے تصویر بنائیں۔'),
        ('متن سے آواز', 'متن کو قدرتی آواز میں بدلیں۔'),
        ('آواز سے متن', 'آواز کو متن میں تبدیل کریں۔'),
        ('ویڈیو جنریٹر', 'متن یا تصویر سے ویڈیو بنائیں۔'),
        ('تصویر اینیمیشن', 'چہرے اور تصاویر کو اینیمیٹ کریں۔'),
        ('وائس ڈبنگ', 'آڈیو/ویڈیو کو ترجمہ اور ڈب کریں۔')
    ]

for name, desc in tools:
    st.button(name)
    st.caption(desc)

show_footer(lang) 