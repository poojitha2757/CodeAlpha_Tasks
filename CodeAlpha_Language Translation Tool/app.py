import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

# Page config
st.set_page_config(page_title="AI Translator", page_icon="🌍", layout="centered")

# Custom styling
st.markdown("""
    <style>
    .main {
        background-color: #f4f6f9;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    .stTextArea textarea {
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌍 AI Language Translation Tool")
st.write("Translate text instantly between multiple languages.")

text = st.text_area("Enter text to translate")

languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh-CN"
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language", list(languages.keys()))

with col2:
    target_lang = st.selectbox("Target Language", list(languages.keys()))

if st.button("🚀 Translate"):
    if text:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.success("Translation Result")
        st.code(translated)

        tts = gTTS(translated)
        tts.save("output.mp3")
        st.audio("output.mp3")

    else:
        st.warning("Please enter text to translate.")