import streamlit as st
import pandas as pd

df = pd.read_csv('aad.csv')
st.title('Dashboard')
if st.button('Data'):
    st.write(df)

st.bar_chart(df, x = 'name', y = 'salary')
st.line_chart(df, x= 'city', y = 'salary')
st.area_chart(df, x ='department', y = 'salary')
st.scatter_chart(df, x = 'city', y = 'salary')
