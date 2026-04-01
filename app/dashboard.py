import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import pandas as pd
from src.pipeline import run_pipeline

st.title("🚀 Grant Intelligence Dashboard (LLM Powered)")

if st.button("Run Pipeline"):
    data = run_pipeline()
    df = pd.DataFrame(data)

    st.subheader("📄 All Grants")
    st.dataframe(df)

    st.subheader("🏆 Top Opportunities")
    st.dataframe(df.sort_values(by="final_score", ascending=False))

    st.subheader("📊 Score Distribution")
    st.bar_chart(df["final_score"])