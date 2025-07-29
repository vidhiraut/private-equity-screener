import streamlit as st
from screener import load_data, filter_data

st.title("🏦 Private Equity Screener")

df = load_data("data/companies.csv")

min_revenue = st.slider("Minimum Revenue (in Cr)", 0, 10000, 1000)
min_margin = st.slider("Minimum Profit Margin (%)", 0, 100, 10)
max_pe = st.slider("Maximum PE Ratio", 0, 100, 25)

filtered_df = filter_data(df, min_revenue, min_margin, max_pe)

st.subheader("📋 Filtered Companies")
st.dataframe(filtered_df)
