import streamlit as st
import streamlit_authenticator as stauth
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer
import webbrowser

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

# یوزر ڈیٹا (ڈیمو)
users = {
    'demo@pakai.com': {'name': 'Demo User', 'password': stauth.Hasher(['pakai123']).generate()[0], 'credits': 10, 'projects': 2}
}

if 'user' not in st.session_state:
    st.session_state['user'] = None

if lang=='en':
    st.title('Login / Signup')
    authenticator = stauth.Authenticate(
        {'demo@pakai.com': {'name': 'Demo User', 'password': users['demo@pakai.com']['password']}},
        'pakai_cookie', 'pakai_auth', cookie_expiry_days=1
    )
    name, auth_status, username = authenticator.login('Login', 'main')
    if auth_status:
        st.session_state['user'] = {'name': name, 'email': username, 'credits': 10, 'projects': 2}
        st.success(f'Welcome, {name}!')
    elif auth_status is False:
        st.error('Invalid credentials')
    st.markdown('---')
    st.write('Or sign in with:')
    if st.button('Google'):
        st.info('Redirecting to Google OAuth...')
        webbrowser.open_new_tab('http://localhost:5001/login/google')
    if st.button('GitHub'):
        st.info('Redirecting to GitHub OAuth...')
        webbrowser.open_new_tab('http://localhost:5001/login/github')
else:
    st.title('لاگ اِن / سائن اَپ')
    authenticator = stauth.Authenticate(
        {'demo@pakai.com': {'name': 'Demo User', 'password': users['demo@pakai.com']['password']}},
        'pakai_cookie', 'pakai_auth', cookie_expiry_days=1
    )
    name, auth_status, username = authenticator.login('لاگ اِن', 'main')
    if auth_status:
        st.session_state['user'] = {'name': name, 'email': username, 'credits': 10, 'projects': 2}
        st.success(f'خوش آمدید، {name}!')
    elif auth_status is False:
        st.error('غلط معلومات')
    st.markdown('---')
    st.write('یا سوشل اکاؤنٹ سے لاگ اِن کریں:')
    if st.button('گوگل'):
        st.info('گوگل OAuth کی طرف ری ڈائریکٹ ہو رہے ہیں...')
        webbrowser.open_new_tab('http://localhost:5001/login/google')
    if st.button('گِٹ ہب'):
        st.info('گِٹ ہب OAuth کی طرف ری ڈائریکٹ ہو رہے ہیں...')
        webbrowser.open_new_tab('http://localhost:5001/login/github')

show_footer(lang) 