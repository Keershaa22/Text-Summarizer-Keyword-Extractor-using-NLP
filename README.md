# Text Summarizer & Keyword Extractor

An AI-powered utility that automatically generates a **3-line summary** and extracts **5 relevant keywords** from a user-input paragraph using **NLP** and **pre-trained models**. Built with 🤗 **HuggingFace Transformers**, 🧠 **spaCy**, and 🎈 **Streamlit** for a sleek interactive UI.

---

## Problem Statement

Develop a basic AI utility that processes user-input text and provides:
- A **concise 3-line summary**
- **5 relevant keywords**  
using ML/NLP tools like HuggingFace, spaCy, or OpenAI-based models.

---

## Project Description

This tool enhances productivity by simplifying large text data into a short summary and highlighting core keywords. It serves multiple use cases, including:
- Content summarization
- Quick review of documentation
- Education & learning support
- Internal workflow automation

---

## 🛠Tech Stack

| Component        | Library/Tool                     |
|------------------|----------------------------------|
| Summarization    | `facebook/bart-large-cnn` (HuggingFace) |
| Keyword Extraction | `spaCy` (`en_core_web_sm`)         |
| Frontend UI      | `Streamlit`                      |
| Language         | `Python`                         |

---

## Procedure

### 1. **Model Selection**
- `facebook/bart-large-cnn`: For high-quality summarization.
- `spaCy en_core_web_sm`: For efficient keyword extraction.

### 2. **Streamlit Setup**
- Clean UI with:
  - Text input field
  - Sliders for summary length
  - Output display sections
  - Stylish buttons and emojis

### 3. **Summarization Logic**
- Uses the BART model to generate a concise, clear 3-line summary with customizable min and max length.

### 4. **Keyword Extraction Logic**
- Processes summary with spaCy.
- Filters nouns, adjectives, and proper nouns.
- Removes stopwords and punctuation.
- Returns top 5 most frequent meaningful words.

### 5. **Display Output**
- Shows:
  - Final summary
  - Top 5 keywords
  - Alerts and success messages

---

## How to Run Locally

### Prerequisites

Make sure Python 3.7+ is installed. Then install the following:

```bash
pip install streamlit transformers torch spacy
python -m spacy download en_core_web_sm
