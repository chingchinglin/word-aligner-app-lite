import streamlit as st

def align_word_in_sentence(word_or_phrase, sentence):
    tokens = sentence.replace("’s", "").replace("'", "").split()
    try:
        start = tokens.index(word_or_phrase) + 1
        end = start
        return start, end
    except ValueError:
        return "-", "-", "人工處理"

st.title("🔍 Word Aligner (Lite)")
start, end = align_word_in_sentence("apple", "I ate two apples.")
st.write(f"測試對齊結果：start={start}, end={end}")
