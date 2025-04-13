import streamlit as st
from transformers import pipeline
import spacy
import torch
from collections import Counter
from string import punctuation

# Set page config
st.set_page_config(page_title="Text Summarizer & Keyword Extractor", page_icon="📝", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #f2f2f2;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        color: #333333;
        padding-bottom: 10px;
    }
    .stTextArea, .stButton > button {
        font-size: 16px;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6em 1.2em;
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Load models only once
@st.cache_resource
def load_models():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")
    nlp = spacy.load("en_core_web_sm")
    return summarizer, nlp

summarizer, nlp = load_models()

# Text summarization
def summarize_text(text, max_len=100, min_len=40):
    summary = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)[0]['summary_text']
    return summary.strip()

# Keyword extraction
def extract_keywords(text, num_keywords=5):
    doc = nlp(text.lower())
    words = [
        token.text for token in doc
        if token.pos_ in ["NOUN", "PROPN", "ADJ"]
        and token.text not in nlp.Defaults.stop_words
        and token.text not in punctuation
    ]
    freq = Counter(words)
    common_keywords = [word for word, _ in freq.most_common(num_keywords)]
    return common_keywords

# App title
st.markdown("<h1 class='title'> Text Summarizer &  Keyword Extractor</h1>", unsafe_allow_html=True)

# Input
with st.container():
    st.subheader(" Paste your paragraph below:")
    text_input = st.text_area("", placeholder="Type or paste your text here...", height=200)

# Controls
col1, col2 = st.columns([1, 1])
with col1:
    max_len = st.slider("Max summary length", 50, 200, 100, step=10)
with col2:
    min_len = st.slider("Min summary length", 20, 80, 40, step=5)

# Action
if st.button(" Generate Summary & Keywords"):
    if text_input.strip() == "":
        st.warning("Please paste some text before clicking the button.")
    else:
        with st.spinner("Analyzing..."):
            summary = summarize_text(text_input, max_len=max_len, min_len=min_len)
            keywords = extract_keywords(summary)

        # Output
        st.success("✅ Done!")

        st.subheader("📄 Summary:")
        st.info(summary)

        st.subheader("🔑 Top 5 Keywords:")
        st.write(", ".join(keywords))

# Footer
st.markdown("---")
st.markdown("<center>Made with  using BART + spaCy + Streamlit</center>", unsafe_allow_html=True)
