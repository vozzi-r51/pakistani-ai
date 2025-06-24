import streamlit as st

def show_sidebar(lang):
    with st.sidebar:
        st.markdown("""
            <div style='text-align:center;margin-bottom:20px;'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/3/32/Flag_of_Pakistan.svg' width='80'/>
            </div>
        """, unsafe_allow_html=True)
        st.markdown(f"**{'Tools' if lang=='en' else 'اوزار'}**")
        st.write('• ' + ('Text to Image' if lang=='en' else 'متن سے تصویر'))
        st.write('• ' + ('Text to Voice' if lang=='en' else 'متن سے آواز'))
        st.write('• ' + ('Voice to Text' if lang=='en' else 'آواز سے متن'))
        st.write('• ' + ('Video Generator' if lang=='en' else 'ویڈیو جنریٹر'))
        st.write('• ' + ('Image Animation' if lang=='en' else 'تصویر اینیمیشن'))
        st.write('• ' + ('Voice Dubbing' if lang=='en' else 'وائس ڈبنگ'))
        st.markdown('---')
        st.write('© 2025 Pak AI') 