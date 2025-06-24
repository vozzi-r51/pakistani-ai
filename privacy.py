import streamlit as st
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

if lang=='en':
    st.title('Privacy & GDPR')
    st.write('''
    Your data is securely stored and never shared with third parties. You can delete your account and data anytime. Free user data is auto-deleted after 30 days. For details, contact support@pakai.com.
    ''')
else:
    st.title('پرائیویسی اور جی ڈی پی آر')
    st.write('''
    آپ کا ڈیٹا محفوظ ہے اور کسی تیسرے فریق کے ساتھ شیئر نہیں کیا جاتا۔ آپ کسی بھی وقت اپنا اکاؤنٹ اور ڈیٹا ڈیلیٹ کر سکتے ہیں۔ فری یوزرز کا ڈیٹا 30 دن بعد خود بخود ڈیلیٹ ہو جاتا ہے۔ مزید معلومات کے لیے support@pakai.com پر رابطہ کریں۔
    ''')

show_footer(lang) 