import streamlit as st
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer
from components.hero_section import show_hero_section
import requests
from config import OPENAI_API_KEY, GOOGLE_TRANSLATE_API_KEY, D_ID_API_KEY, STABILITY_API_KEY

# لینگویج سیٹنگ
if 'lang' not in st.session_state:
    st.session_state['lang'] = 'en'

lang = st.session_state['lang']

# لینگویج ٹوگل
col1, col2 = st.columns([8,2])
with col2:
    if st.button('اردو' if lang=='en' else 'English'):
        st.session_state['lang'] = 'ur' if lang=='en' else 'en'
        st.experimental_rerun()

# ہیڈر
show_header(lang)
# سائیڈبار
show_sidebar(lang)
# ہیرو سیکشن
show_hero_section(lang)
# ڈیمو آؤٹ پٹس
st.markdown('---')
st.subheader('Sample Demo Outputs' if lang=='en' else 'نمونہ ڈیمو آؤٹ پٹس')
st.image(['static/images/demo1.png','static/images/demo2.png'], width=350)
# فوٹر
show_footer(lang)

if st.button('Generate Voice'):
    audio, error = generate_voice(text, voice)
    if audio:
        st.audio(audio, format="audio/mp3")
        st.download_button("Download", audio, file_name="voice.mp3")
    else:
        st.error(error)

if st.button('Transcribe'):
    if audio:
        text, error = transcribe_audio(audio)
        if text:
            st.success(text)
        else:
            st.error(error)

if st.button('Generate with DALL·E'):
    images, error = generate_dalle_image(prompt, num_images)
    if images:
        for url in images:
            st.image(url)
            st.markdown(f"[Download]({url})")
    else:
        st.error(error)

if st.button('Generate Video'):
    video_url, error = generate_video_from_image(image_url, prompt)
    if video_url:
        st.video(video_url)
        st.markdown(f"[Download Video]({video_url})")
    else:
        st.error(error)

if st.button('Buy Credits'):
    resp = requests.post('http://localhost:5001/create-checkout-session', json={
        'price_id': 'price_1...',  # Stripe dashboard سے لیں
        'success_url': 'http://localhost:8501/success',
        'cancel_url': 'http://localhost:8501/cancel'
    })
    if resp.status_code == 200:
        session_id = resp.json()['id']
        st.markdown(f"[Pay Now](https://checkout.stripe.com/pay/{session_id})")
    else:
        st.error('Payment error!')

def transcribe_audio(audio_file):
    url = "https://api.openai.com/v1/audio/transcriptions"
    headers = {"Authorization": f"Bearer {OPENAI_API_KEY}"}
    files = {"file": audio_file}
    data = {"model": "whisper-1"}
    response = requests.post(url, headers=headers, files=files, data=data)
    if response.status_code == 200:
        return response.json()["text"], None
    else:
        return None, response.text

def translate_text(text, target_lang="ur"):
    url = f"https://translation.googleapis.com/language/translate/v2"
    params = {
        "q": text,
        "target": target_lang,
        "key": GOOGLE_TRANSLATE_API_KEY
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        return response.json()["data"]["translations"][0]["translatedText"], None
    else:
        return None, response.text

def animate_face(image_url, audio_url):
    url = "https://api.d-id.com/talks"
    headers = {"Authorization": f"Basic {D_ID_API_KEY}", "Content-Type": "application/json"}
    data = {
        "source_url": image_url,
        "audio_url": audio_url
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()["result_url"], None
    else:
        return None, response.text

def generate_dalle_image(prompt, n=1, size="1024x1024"):
    url = "https://api.openai.com/v1/images/generations"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": prompt,
        "n": n,
        "size": size
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return [img['url'] for img in response.json()['data']], None
    else:
        return None, response.text

def generate_video_from_image(image_url, prompt):
    url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {STABILITY_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "version": "stable-video-diffusion-version-id",  # اصل ورژن ID یہاں ڈالیں
        "input": {
            "image": image_url,
            "prompt": prompt
        }
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        prediction = response.json()
        # prediction['urls']['get'] پر پولنگ کریں جب تک status 'succeeded' نہ ہو
        return prediction['urls']['get'], None
    else:
        return None, response.text 