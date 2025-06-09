"""Minimal Streamlit interface."""

import streamlit as st

from agent import KGAssistant

DOCS = [
    "IIT Kharagpur was established in 1951.",
    "The institute has two main semesters each year.",
    "The central library houses thousands of books."
]

assistant = KGAssistant(DOCS)

st.title("KGP Assistant")
query = st.text_input("Ask a question")
if query:
    answer = assistant.ask(query)
    st.write(answer)
