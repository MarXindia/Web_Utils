
"""
Data is fetched using Coin Market Cap API but, since  free API service is being used the rate limit is slow and
data isn't updated frequently, refresh time is 15 seconds. Data is cached by streamlit using decorator st.cache
Even though slow price changes are reflected in the Price change section, if price increases state is marked increased and vice-versa


"""
import streamlit as st
from generate_dataframe import fetch_top_10_data as dataset
from fetch_coin_data import CoinData as coin
import time

custom_html = """
<h1 style="font-size: 30px;">Top Crypto Currencies</h1>
"""
st.markdown(custom_html, unsafe_allow_html=True)



st.sidebar.header("Cryptocurrencies Info")
st.sidebar.markdown("""
 Data Refreshes every 15 seconds
""")

st.sidebar.markdown("Slide to choose top cryptos")
number_of_cryptos = st.sidebar.slider("Top", 1, 50, 10)


@st.cache_data(ttl=15)
def cache_coin_data():

    response = coin().request()
    data = dataset(response)
    data.index += 1
    return data


info_placeholder = st.empty()
table_placeholder = st.empty()

prev_data = None


def apply_color(row):
    max_rank = len(data)
    rank = data.index.get_loc(row.name) + 1
    intensity = 1 - (rank / max_rank)
    color = f'rgba(155,0, 140, {intensity})'  # Red color with intensity based on rank
    return [f'background-color: {color}'] * len(row)

data = cache_coin_data().head(number_of_cryptos)
while True:
    data = cache_coin_data().head(number_of_cryptos)

    price = []
    state = []

    for index, row in data.iterrows():
        for col, val in row.items():
            if col == 'Price (USD)':
                price.append(val)

    if prev_data is not None and 'Price Change' in prev_data:
        state = prev_data['Price Change'].tolist()

    if prev_data is not None:
        for pre_val, curr_val in zip(prev_data['Price (USD)'], price):
            if pre_val < curr_val:
                state.append('Increased')  # Price increased
            elif pre_val > curr_val:
                state.append('Decreased')  # Price decreased

    prev_data = data.copy()
    state.extend([''] * (len(data) - len(state)))  # Ensure state list has same length as DataFrame
    data['Price Change'] = state

    table_placeholder.table(data.style.apply(apply_color, axis=1))

    current_time = time.strftime('%H:%M:%S')
    info_placeholder.info(f"Data updated at {current_time}.")

    time.sleep(15)  # Update cache and interface every 3 seconds
