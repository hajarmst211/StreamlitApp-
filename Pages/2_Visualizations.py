# Pages/2_Visualizations.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from Utils import fetch_search_results

st.title("Data Visualizations")

# Fetch data from the first page or session state
query = st.text_input("Enter a search term:")
if query:
    data = fetch_search_results(query)
    st.dataframe(data)

    # Example Visualization: Bar chart
    st.subheader("Top Apps by Rating")
    top_apps = data.sort_values(by="rating", ascending=False).head(10)
    st.bar_chart(top_apps.set_index('app_name')['rating'])
