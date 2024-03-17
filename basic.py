import streamlit as st
import pandas as pd
import numpy as np
# df = pd.DataFrame(
#     {
#         'FIRST COLUMN': [1,2,3,4],
#         'SECOND COLUMN': [10,20,30,40]
#
#     }
# )
# df
# st.pyplot(df.plot.barh(stacked=True).figure)

st.write(''' 
This is an app for some Movie Titles!
''')

st.sidebar.header("User_Data")
st.sidebar.markdown("""
 [CSV input file]

""")
file = st.sidebar.file_uploader('Upload csv',type=['csv'])

st.write(''' 
This is an app for some Movie Titles!
''')

st.sidebar.header("User_Data")
st.sidebar.markdown("""
 [CSV input file]

""")
file = st.sidebar.file_uploader('Upload csv',type=['csv'])

if file is not None:
    df = pd.read_csv(file)
df
st.sidebar.selectbox('Test1',('One','two','three'))
st.sidebar.slider('Some tag',30,40,50)
st.sidebar.text_input('Enter User Name')