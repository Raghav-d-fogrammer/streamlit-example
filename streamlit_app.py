import streamlit as st

col1, col2 = st.columns(2)

with col1:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with col2:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")