# Utils.py
import pandas as pd
import requests

def fetch_search_results(query):
    # Replace with your actual API logic
    response = requests.get(f"https://api.example.com/search?q={query}")
    data = response.json()
    return pd.DataFrame(data['results'])

def fetch_reviews(app_id):
    # Replace with your actual API logic for fetching reviews
    response = requests.get(f"https://api.example.com/reviews?app_id={app_id}")
    data = response.json()
    return pd.DataFrame(data['reviews'])
