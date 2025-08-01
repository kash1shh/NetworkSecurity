import streamlit as st
import pandas as pd
import pickle
import os

# Load model & preprocessor
with open("final_model/preprocessor.pkl", "rb") as f:
    preprocessor = pickle.load(f)
with open("final_model/model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Phishing Website Detection")
st.write("Upload a CSV file with features or input manually to detect phishing activities.")

# --- File Upload ---
uploaded_file = st.file_uploader("Upload CSV file for prediction", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(df)

    # Preprocess
    processed = preprocessor.transform(df)
    predictions = model.predict(processed)

    df["predicted_column"] = predictions
    st.write("Predictions:")
    st.dataframe(df)

    # Option to download results
    csv_output = df.to_csv(index=False).encode('utf-8')
    st.download_button("Download Predictions", csv_output, "predictions.csv", "text/csv")

st.write("---")
st.write("### Manual Input")

# --- Manual Form Input ---
features = [
    "having_IP_Address","URL_Length","Shortining_Service","having_At_Symbol","double_slash_redirecting",
    "Prefix_Suffix","having_Sub_Domain","SSLfinal_State","Domain_registeration_length","Favicon",
    "port","HTTPS_token","Request_URL","URL_of_Anchor","Links_in_tags","SFH","Submitting_to_email",
    "Abnormal_URL","Redirect","on_mouseover","RightClick","popUpWidnow","Iframe","age_of_domain",
    "DNSRecord","web_traffic","Page_Rank","Google_Index","Links_pointing_to_page","Statistical_report"
]

user_input = {}
for feature in features:
    user_input[feature] = st.selectbox(f"{feature}:", options=[-1, 0, 1], index=1)

if st.button("Predict Single Entry"):
    input_df = pd.DataFrame([user_input])
    processed_input = preprocessor.transform(input_df)
    prediction = model.predict(processed_input)[0]
    st.success(f"Prediction: {'Phishing' if prediction == 1 else 'Legitimate'}")
