Network Security - Phishing URL Detection
This project detects phishing URLs using a machine learning model trained on multiple website features.

FEATURES
Phishing detection: Predicts whether a URL is legitimate or malicious.
FastAPI backend: REST API for programmatic access to predictions.
Streamlit frontend: User-friendly web interface for uploading CSVs or manual input.
Docker-ready: Configured to build and push images to AWS ECR.
CI/CD: GitHub Actions workflow for automated integration and deployment.

HOW IT WORKS:
1) Input: Website data (as CSV or JSON) with features like:
having_IP_Address, SSLfinal_State, URL_Length, age_of_domain, etc.

2) Preprocessing: Missing values handled using KNNImputer.

3) Prediction: Trained Decision Tree model predicts:
1 → Phishing (malicious)
0 → Legitimate (safe)

4) Output: CSV file with an added column predicted_column.

PROJECT STRUCTURE
.
├── app.py                     # FastAPI backend
├── app_streamlit.py           # Streamlit frontend
├── final_model/               # Pretrained model & preprocessor
│   ├── model.pkl
│   └── preprocessor.pkl
├── data_schema/schema.yaml    # Input data schema
├── prediction_output/         # Stores prediction results
├── .github/workflows/main.yaml# CI/CD pipeline
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation

INSTALLATION AND USAGE
1. Clone the repository

git clone https://github.com/kash1shh/NetworkSecurityProject.git
cd NetworkSecurityProject

2. Create Virtual Environment

python -m venv .venv
source .venv/bin/activate       # (Linux/Mac)
.venv\Scripts\activate          # (Windows)

3. Install Dependencies

pip install -r requirements.txt

4. Run the Streamlit App

streamlit run app_streamlit.py

Or run FastAPI backend:

python app.py

TECH STACK:
Python (FastAPI, Streamlit, Scikit-learn, Pandas)

AWS ECR (for container storage)

GitHub Actions (CI/CD)

Docker (containerization)


