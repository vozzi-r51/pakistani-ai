import streamlit as st

def show_header(lang):
    st.markdown(f"""
        <div style='background:linear-gradient(90deg,#006400,#fff);padding:18px 0 8px 0;text-align:center;border-radius:8px;'>
            <h1 style='color:#006400;margin-bottom:0;'>Pak AI پاکستان</h1>
            <p style='color:#222;font-size:18px;margin-top:0;'>
                {('AI-powered Creativity Suite' if lang=='en' else 'اے آئی سے تخلیقی صلاحیتوں کا انقلاب')}
            </p>
        </div>
    """, unsafe_allow_html=True) 