import streamlit as st
import pandas as pd
import pickle

st.header("Data Visualization")
df = pd.read_csv("./Data/LifeExpectancyData.csv")
# with open("data.sav", 'wb') as f:
#     pickle.dump(df, f)

# df = pickle.load(open('./data.sav', 'rb'))
# st.write(df)
st.dataframe(df)

# Display the various charts

