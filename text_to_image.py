import streamlit as st
from components.header import show_header
from components.sidebar import show_sidebar
from components.footer import show_footer
import requests
import base64
from config import STABLE_DIFFUSION_API_KEY

lang = st.session_state.get('lang', 'en')
show_header(lang)
show_sidebar(lang)

def generate_images_sd(prompt, style, aspect, num_images):
    if not STABLE_DIFFUSION_API_KEY or STABLE_DIFFUSION_API_KEY.startswith('YOUR_'):
        return None, 'API key missing! Please add your Stable Diffusion API key in config.py.'
    # API endpoint (Stability AI example)
    url = 'https://api.stability.ai/v1/generation/stable-diffusion-512-v2-1/text-to-image'
    headers = {
        'Authorization': f'Bearer {STABLE_DIFFUSION_API_KEY}',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    aspect_map = {'16:9': (896, 512), '4:5': (512, 640), '9:16': (512, 896)}
    width, height = aspect_map.get(aspect, (512,512))
    data = {
        'text_prompts': [{'text': prompt}],
        'cfg_scale': 7,
        'clip_guidance_preset': 'FAST_BLUE',
        'height': height,
        'width': width,
        'samples': num_images,
        'style_preset': style.lower()
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        images = [base64.b64decode(img['base64']) for img in response.json().get('artifacts', [])]
        return images, None
    else:
        return None, f'API Error: {response.text}'

if lang=='en':
    st.title('Text to Image Generator')
    st.write('Generate stunning images from your text prompts!')
    prompt = st.text_area('Enter your prompt')
    style = st.selectbox('Style', ['Realistic', 'Anime', 'Cinematic', 'Fantasy', 'Sketch'])
    aspect = st.selectbox('Aspect Ratio', ['16:9', '4:5', '9:16'])
    num_images = st.slider('Number of Images', 1, 4, 1)
    if st.button('Generate'):
        with st.spinner('Generating...'):
            images, error = generate_images_sd(prompt, style, aspect, num_images)
            if error:
                st.error(error)
            elif images:
                for idx, img_bytes in enumerate(images):
                    st.image(img_bytes, caption=f'Output {idx+1}', width=300)
                    st.download_button(f'Download {idx+1}', img_bytes, file_name=f'pakai_img_{idx+1}.png')
    st.markdown('---')
    st.subheader('Sample Outputs')
    st.image(['static/images/demo1.png','static/images/demo2.png'], width=300)
else:
    st.title('متن سے تصویر جنریٹر')
    st.write('اپنے متن سے شاندار تصاویر بنائیں!')
    prompt = st.text_area('اپنا پرامپٹ لکھیں')
    style = st.selectbox('اسٹائل', ['حقیقی','اینیمے','سنیما','فینٹسی','اسکیچ'])
    aspect = st.selectbox('ایسپیکٹ ریشو', ['16:9', '4:5', '9:16'])
    num_images = st.slider('تصاویر کی تعداد', 1, 4, 1)
    if st.button('جنریٹ کریں'):
        with st.spinner('امیج تیار ہو رہی ہے...'):
            images, error = generate_images_sd(prompt, style, aspect, num_images)
            if error:
                st.error(error)
            elif images:
                for idx, img_bytes in enumerate(images):
                    st.image(img_bytes, caption=f'آؤٹ پٹ {idx+1}', width=300)
                    st.download_button(f'ڈاؤن لوڈ {idx+1}', img_bytes, file_name=f'pakai_img_{idx+1}.png')
    st.markdown('---')
    st.subheader('نمونہ آؤٹ پٹس')
    st.image(['static/images/demo1.png','static/images/demo2.png'], width=300)

show_footer(lang) 