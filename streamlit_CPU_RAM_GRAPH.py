import streamlit as st
import pandas as pd
import psutil
import time
from collections import deque

# Initialize deque objects to store CPU and RAM usage data
cpu_data = deque(maxlen=10)  # Store data points for the last 30 seconds
ram_data = deque(maxlen=10)  # Store data points for the last 30 seconds

# Title of the Streamlit app
st.title('Machine Resources App')

# RAM Line Chart
st.write('RAM Line Chart')
ram_chart = st.line_chart()

# CPU Line Chart
st.write('CPU Line Chart')
cpu_chart = st.line_chart()

# CPU Bar Chart
st.write('CPU Bar Chart')
cpu_chart_bar = st.bar_chart()

# Continuously update CPU and RAM data and display in the charts
while True:
    # Get RAM usage and append to ram_data
    ram_percent = psutil.virtual_memory().percent
    ram_data.append(ram_percent)

    # Get CPU usage and append to cpu_data
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_data.append(cpu_percent)

    # Convert deque objects to DataFrame
    ram_df = pd.DataFrame(list(ram_data), columns=["RAM Percentage"])
    cpu_df = pd.DataFrame(list(cpu_data), columns=["CPU Percentage"])

    # Update RAM Line Chart
    ram_chart.line_chart(ram_df)

    # Update CPU Line Chart
    cpu_chart.line_chart(cpu_df)

    # Update CPU Bar Chart
    cpu_chart_bar.bar_chart(cpu_df)

    # Wait for 1 second before updating again
    time.sleep(1)
