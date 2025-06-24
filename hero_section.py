import streamlit as st

def show_hero_section(lang):
    if lang=='en':
        st.markdown("""
            <div style='padding:30px 0 10px 0;text-align:center;'>
                <h2>Unleash Your Creativity with Pak AI</h2>
                <p>Generate images, voices, and videos in English & Urdu. Pakistan's first AI-powered creative suite!</p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style='padding:30px 0 10px 0;text-align:center;'>
                <h2>Pak AI کے ساتھ اپنی تخلیقی صلاحیتوں کو آزاد کریں</h2>
                <p>انگلش اور اردو میں تصاویر، آوازیں اور ویڈیوز بنائیں۔ پاکستان کا پہلا اے آئی تخلیقی ٹول!</p>
            </div>
        """, unsafe_allow_html=True)
    st.image('static/images/hero_demo.png', width=500) 