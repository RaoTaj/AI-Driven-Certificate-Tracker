import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="AI-Driven Certificate & Security Monitoring", layout="wide")

st.title("🔒 AI-Driven Certificate Expiry & Security Monitoring")

st.write("Upload CSV logs or monitor live certificate expiry details")

uploaded_file = st.file_uploader("Upload Certificate Logs (CSV)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df, use_container_width=True)

    st.subheader("Summary")
    status_count = df["Status"].value_counts()
    st.bar_chart(status_count)

    st.subheader("Critical Certificates (<7 Days Left)")
    st.dataframe(df[df["Status"] == "Critical"])
