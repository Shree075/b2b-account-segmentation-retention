import streamlit as st
import pandas as pd
import numpy as np
import joblib

@st.cache_resource
def load_model():
    model = joblib.load("models/b2b_churn_rf_model.pkl")
    return model

model = load_model()

st.title("🏢 B2B Account Segmentation & Churn Risk")
st.write(
    "Predict churn risk for B2B accounts using K-Means segments and a "
    "Random Forest model (AUC 0.852)."
)

mode = st.sidebar.radio("Prediction mode", ["Single account", "Batch (CSV)"])

segment_map = {
    "Strategic Enterprise": 0,
    "Small Trial / At-Risk": 1,
    "Growth Accounts": 2,
    "High-Spend Risky": 3
}
segment_labels = list(segment_map.keys())

regions = ["France", "Spain", "Germany"]
genders = ["Male", "Female"]

def build_feature_row(geography, gender, segment_label, age, credit_score,
                      tenure_months, balance, num_products, est_salary, is_active):
    segment = segment_map[segment_label]
    acv = balance
    tenure_years = tenure_months / 12

    row = {
        "CreditScore": credit_score,
        "Age": age,
        "Tenure": tenure_months,
        "Balance": balance,
        "NumOfProducts": num_products,
        "EstimatedSalary": est_salary,
        "ACV": acv,
        "Tenure_Years": tenure_years,
        "Geography": geography,
        "Gender": gender,
        "Segment": segment
    }
    return pd.DataFrame([row])

if mode == "Single account":
    st.subheader("Single Account Prediction")

    col1, col2 = st.columns(2)
    with col1:
        geography = st.selectbox("Region (Geography)", regions)
        gender = st.selectbox("Gender", genders)
        segment_label = st.selectbox("Segment", segment_labels)
        age = st.slider("Age", 18, 92, 40)
        credit_score = st.slider("Credit Score", 350, 850, 650)
    with col2:
        tenure_months = st.slider("Tenure (months)", 0, 10, 5)
        balance = st.number_input("Balance / ACV proxy", min_value=0.0, value=50000.0, step=1000.0)
        num_products = st.slider("Number of Products", 1, 4, 2)
        est_salary = st.number_input("Estimated Salary", min_value=0.0, value=100000.0, step=5000.0)
        is_active = st.selectbox("Is Active Member", [0, 1])

    if st.button("Predict churn risk"):
        X = build_feature_row(
            geography, gender, segment_label, age, credit_score,
            tenure_months, balance, num_products, est_salary, is_active
        )
        prob = model.predict_proba(X)[0, 1]
        risk = prob * 100
        st.metric("Predicted churn probability", f"{risk:.1f}%")

        if risk >= 50:
            st.error("High churn risk – apply High-Spend / At-Risk playbook.")
        elif risk >= 25:
            st.warning("Medium churn risk – monitor and engage proactively.")
        else:
            st.success("Low churn risk – maintain relationship & look for upsell.")

else:
    st.subheader("Batch Prediction (Upload CSV)")
    st.write(
        "Upload a CSV with the same feature columns used for training:\n"
        "`CreditScore, Age, Tenure, Balance, NumOfProducts, EstimatedSalary, "
        "ACV, Tenure_Years, Geography, Gender, Segment`"
    )
    file = st.file_uploader("Upload accounts CSV", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        probs = model.predict_proba(df)[..., 1]
        df["churn_probability"] = probs
        st.dataframe(df.head())

        csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download predictions", csv, "churn_predictions.csv", "text/csv")
