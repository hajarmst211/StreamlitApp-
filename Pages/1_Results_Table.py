# Pages/1_Results_Table.py
import streamlit as st
import pandas as pd
from Utils import fetch_search_results

st.title("Search Results")

query = st.text_input("Enter a search term:")
if query:
    data = fetch_search_results(query)
    st.dataframe(data)
