import streamlit as st
import pandas as pd

from recommendation import recommend

df = pd.read_csv("products.csv")

st.title("🛒 Product Recommendation System")

product = st.selectbox(
    "Select Product",
    df['Product']
)

if st.button("Recommend"):

    results = recommend(product)

    st.subheader("Recommended Products")

    for item in results:
        st.write("✅", item)