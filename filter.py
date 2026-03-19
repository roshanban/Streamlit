import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("CSV Data Viewer with Chart")

uploaded_file = st.file_uploader("Upload CSV file", type="csv")

if uploaded_file is not None:
    # Convert to DataFrame
    df = pd.read_csv(uploaded_file)

    st.write("Data Preview")
    st.dataframe(df)

    # Create plot
    fig, ax = plt.subplots()
    sns.scatterplot(x="State", y="Profit", data=df, ax=ax)

    st.pyplot(fig)

else:
    st.write("Please upload a CSV file")