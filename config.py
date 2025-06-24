"""
Pak AI - Config
یہ فائل تمام API keys کو محفوظ طریقے سے لوڈ اور ایکسیسبل بناتی ہے
"""
import os  # Python کا built-in module environment variables کے لیے
from dotenv import load_dotenv  # .env فائل لوڈ کرنے کے لیے

# .env فائل لوڈ کریں (پروجیکٹ روٹ سے)
load_dotenv()

# OpenAI API Key (متن سے تصویر، آواز وغیرہ)
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Stability AI (Stable Diffusion) API Key (امیج جنریشن)
STABILITY_API_KEY = os.getenv('STABILITY_API_KEY')

# ElevenLabs API Key (متن سے آواز)
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY')

# Google Translate API Key (ملٹی لینگویج ترجمہ)
GOOGLE_TRANSLATE_API_KEY = os.getenv('GOOGLE_TRANSLATE_API_KEY')

# D-ID API Key (Lip-sync اینیمیشن)
D_ID_API_KEY = os.getenv('D_ID_API_KEY') 