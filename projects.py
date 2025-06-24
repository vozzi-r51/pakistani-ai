import streamlit as st
import requests
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer
from datetime import datetime

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

jwt_token = st.session_state.get('jwt_token')
projects = []
if jwt_token:
    try:
        resp = requests.get('http://localhost:5001/projects', headers={'Authorization': f'Bearer {jwt_token}'})
        if resp.status_code == 200:
            projects = resp.json()
    except Exception as e:
        st.error('Backend connection error!')

if not projects:
    # fallback demo
    projects = [
        {'name': 'AI Art', 'created_at': str(datetime(2024,6,1)), 'thumb_url': 'static/images/demo1.png', 'privacy': 'Private', 'file_url': '#'},
        {'name': 'Urdu Voiceover', 'created_at': str(datetime(2024,6,2)), 'thumb_url': 'static/images/demo2.png', 'privacy': 'Public', 'file_url': '#'}
    ]

if lang=='en':
    st.title('My Projects')
    for p in projects:
        col1, col2, col3, col4 = st.columns([1,2,2,1])
        with col1:
            st.image(p['thumb_url'], width=80)
        with col2:
            st.write(f"**{p['name']}**")
            st.caption(p.get('created_at',''))
        with col3:
            st.write(f"Privacy: {p['privacy']}")
            st.button('Toggle Privacy', key=p['name']+'_privacy')
        with col4:
            st.download_button('Download', b'', file_name=f"{p['name']}.zip")
        st.markdown('---')
else:
    st.title('میرے پراجیکٹس')
    for p in projects:
        col1, col2, col3, col4 = st.columns([1,2,2,1])
        with col1:
            st.image(p['thumb_url'], width=80)
        with col2:
            st.write(f"**{p['name']}**")
            st.caption(p.get('created_at',''))
        with col3:
            st.write(f"پرائیویسی: {p['privacy']}")
            st.button('پرائیویسی تبدیل کریں', key=p['name']+'_privacy_ur')
        with col4:
            st.download_button('ڈاؤن لوڈ', b'', file_name=f"{p['name']}.zip")
        st.markdown('---')

show_footer(lang) 