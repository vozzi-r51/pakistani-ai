import streamlit as st
import requests
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

jwt_token = st.session_state.get('jwt_token')
user = {'name': 'Guest', 'email': 'demo@pakai.com', 'credits': 10, 'projects': 2}

if jwt_token:
    try:
        resp = requests.get('http://localhost:5001/user', headers={'Authorization': f'Bearer {jwt_token}'})
        if resp.status_code == 200:
            user = resp.json()
    except Exception as e:
        st.error('Backend connection error!')

if lang=='en':
    st.title('Profile')
    st.write(f"**Name:** {user['name']}")
    st.write(f"**Email:** {user['email']}")
    st.write(f"**Credits:** {user['credits']}")
    st.write(f"**Projects:** {user['projects']}")
    st.button('Logout')
else:
    st.title('پروفائل')
    st.write(f"**نام:** {user['name']}")
    st.write(f"**ای میل:** {user['email']}")
    st.write(f"**کریڈٹس:** {user['credits']}")
    st.write(f"**پراجیکٹس:** {user['projects']}")
    st.button('لاگ آؤٹ')

show_footer(lang) 