import streamlit as st
import pandas as pd

# 🔹 Page Config
st.set_page_config(
    page_title="CSV Data Viewer",
    page_icon="📊",
    layout="wide"
)

# 🔹 Custom CSS for Design
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: bluelinear-gradient(to right, #0f2027, #203a43, #2c5364);
        color: red;
    }

    /* Title */
  h1 {
    text-align: center;
    color: #00C9A7;
}

    /* Upload box */
    .stFileUploader {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
    }

    /* Dataframe styling */
    .stDataFrame {
        background-color: white;
        color: black;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# 🔹 Title
st.title("📊 CSV Data Analyzer")

# 🔹 Sidebar
st.sidebar.header("Options")
show_shape = st.sidebar.checkbox("Show Data Shape")
show_columns = st.sidebar.checkbox("Show Column Names")

# 🔹 File Upload
user_file = st.file_uploader("📂 Upload your CSV file", type='csv')

if user_file:
    df = pd.read_csv(user_file)

    st.success("✅ File Uploaded Successfully!")

    # 🔹 Show Data
    st.subheader("📄 Data Preview")
    st.dataframe(df, use_container_width=True)

    # 🔹 Sidebar Options
    if show_shape:
        st.write("Shape of dataset:", df.shape)

    if show_columns:
        st.write("Columns:", df.columns.tolist())

    # 🔹 Basic Info
    st.subheader("📊 Basic Info")
    st.write(df.describe())

else:
    st.info("👆 Please upload a CSV file to get started")