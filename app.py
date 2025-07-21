import streamlit as st
import pandas as pd
from .config import load_config


config = load_config()
with st.sidebar:
    st.sidebar.title("YANCCA: Yet Another Csv Chatbot Assistant 🌞")

uploaded_file = st.file_uploader("Choose a CSV file", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df)