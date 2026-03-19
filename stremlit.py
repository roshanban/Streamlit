import streamlit as st
import pandas as pd

# 🔹 Page Config
st.set_page_config(page_title="KYC Form", page_icon="📝", layout="centered")

# 🔹 Custom CSS (UI Design)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f2027, #2c5364);
    color: white;
}

h1 {
    text-align: center;
    color: #00C9A7;
}

.stTextInput, .stDateInput, .stSelectbox {
    background-color: #ffffff10;
}
</style>
""", unsafe_allow_html=True)

# 🔹 Title
st.markdown("<h1>📝 KYC Form</h1>", unsafe_allow_html=True)

# 🔹 Form
with st.form("kyc_form"):
    
    st.subheader("👤 Personal Information")
    
    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    dob = st.date_input("Date of Birth")
    
    st.subheader("📍 Address Details")
    
    address = st.text_area("Address")
    city = st.text_input("City")
    country = st.selectbox("Country", ["Nepal", "India", "USA", "Other"])
    
    st.subheader("🪪 Identity Details")
    
    id_type = st.selectbox("ID Type", ["Citizenship", "Passport", "Driving License"])
    id_number = st.text_input("ID Number")
    file_upload = st.file_uploader("Upload ID Proof", type=["jpg", "png", "pdf"])
    
    submitted = st.form_submit_button("Submit")

# 🔹 Validation & Output
if submitted:
    if name and email and phone and id_number:
        st.success("✅ KYC Submitted Successfully!")
        
        data = {
            "Name": name,
            "Email": email,
            "Phone": phone,
            "DOB": dob,
            "Address": address,
            "City": city,
            "Country": country,
            "ID Type": id_type,
            "ID Number": id_number
        }
        
        df = pd.DataFrame([data])
        
        st.subheader("📄 Submitted Data")
        st.dataframe(df)
        
        # Save data
        df.to_csv("kyc_data.csv", mode='a', header=False, index=False)
        
    else:
        st.error("❌ Please fill all required fields")