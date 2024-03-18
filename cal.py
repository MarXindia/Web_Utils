import streamlit as st
from generate_dataframe import fetch_top_10_data as dataset
from fetch_coin_data import CoinData as coin
import time

custom_html = """
<h1 style="font-size: 30px;">Top Crypto Currencies</h1>
"""
st.markdown(custom_html, unsafe_allow_html=True)

st.sidebar.header("Cryptocurrencies To Display")
number_of_cryptos = st.sidebar.slider("Top", 1, 50, 10)


@st.cache_data(ttl=5)
def cache_data():
    response = coin().request()
    data = dataset(response)
    data.index += 1
    return data


info_placeholder = st.empty()
table_placeholder = st.empty()

previous_data =None

while True:
    data = cache_data().head(number_of_cryptos)

    # Clear previous content before updating
    table_placeholder.empty()
    info_placeholder.empty()

    # Define the apply_color function inside the loop

    if previous_data is not None:

        price_change = data['Price'] - previous_data['Price']
        def apply_color(row):
            max_rank = len(data)
            rank = data.index.get_loc(row.name) + 1
            intensity = 1 - (rank / max_rank)
            color = f'rgba(155,0, 140, {intensity})'  # Red color with intensity based on rank
            return [f'background-color: {color}'] * len(row)


        styled_df = data.style.apply(apply_color, axis=1).to_dataframe()



        table_placeholder.table(styled_df)

        current_time = time.strftime('%H:%M:%S')
        info_placeholder.info(f"Data has been updated at {current_time}.")

        time.sleep(5)  # Update cache and interface every 10 seconds
