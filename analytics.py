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
usage = None
if jwt_token:
    try:
        resp = requests.get('http://localhost:5001/analytics', headers={'Authorization': f'Bearer {jwt_token}'})
        if resp.status_code == 200:
            usage = resp.json()
    except Exception as e:
        st.error('Backend connection error!')

if not usage:
    usage = {'credits_used': 12, 'credits_total': 50, 'last_login': datetime(2024,6,7), 'feature_usage': {'Text to Image': 5, 'Text to Voice': 3, 'Video': 2}}

activity_log = [
    {'action': 'Generated Image', 'date': datetime(2024,6,7)},
    {'action': 'Downloaded Video', 'date': datetime(2024,6,6)},
    {'action': 'Logged in', 'date': datetime(2024,6,5)}
]

if lang=='en':
    st.title('Analytics & Activity Log')
    st.progress(usage['credits_used']/usage['credits_total'])
    st.write(f"**Credits Used:** {usage['credits_used']} / {usage['credits_total']}")
    st.write(f"**Last Login:** {usage['last_login']}")
    st.write('**Feature Usage:**')
    for k,v in usage['feature_usage'].items():
        st.write(f"- {k}: {v} times")
    st.markdown('---')
    st.write('**Activity Log:**')
    for a in activity_log:
        st.write(f"- {a['action']} ({a['date'].strftime('%d %b %Y')})")
else:
    st.title('اینالیٹکس اور ایکٹیویٹی لاگ')
    st.progress(usage['credits_used']/usage['credits_total'])
    st.write(f"**استعمال شدہ کریڈٹس:** {usage['credits_used']} / {usage['credits_total']}")
    st.write(f"**آخری لاگ اِن:** {usage['last_login']}")
    st.write('**فیچر وائز استعمال:**')
    for k,v in usage['feature_usage'].items():
        st.write(f"- {k}: {v} بار")
    st.markdown('---')
    st.write('**ایکٹیویٹی لاگ:**')
    for a in activity_log:
        st.write(f"- {a['action']} ({a['date'].strftime('%d %b %Y')})")

show_footer(lang) 