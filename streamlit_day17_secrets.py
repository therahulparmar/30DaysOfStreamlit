import streamlit as st

st.title('st.secrets')

st.write("name: ", st.secrets['username'])
st.write("message: ", st.secrets['message'])
