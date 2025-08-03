# Network Security – Phishing URL Detection

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) 
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-success) 
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-ff4b4b) 
![Build](https://img.shields.io/badge/Build-Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

This project detects **phishing URLs** using a machine learning model trained on multiple website features (e.g., URL structure, SSL state, domain age).  


---

##  Features
- **Phishing detection**: Predicts whether a URL is legitimate or malicious.  
- **FastAPI backend**: REST API for programmatic access to predictions.  
- **Streamlit frontend**: User-friendly web interface for uploading CSVs or manual input.  
- **Docker-ready**: Configured to build and push images to AWS ECR.  
- **CI/CD**: GitHub Actions workflow for automated integration and deployment.  

---

##  How It Works
1. **Input**: Website data (as CSV or JSON) with features like:
   - `having_IP_Address`, `SSLfinal_State`, `URL_Length`, `age_of_domain`, etc.
2. **Preprocessing**: Missing values handled using `KNNImputer`.  
3. **Prediction**: Trained **Decision Tree** model predicts:
   - `1` → **Phishing** (malicious)
   - `0` → **Legitimate** (safe)
4. **Output**: CSV file with an added column `predicted_column`.

---

##  Project Structure

<details>
<summary>Click to view</summary>
.
├── app.py # FastAPI backend (API server)
├── app_streamlit.py # Streamlit frontend (web UI)
├── final_model/ # Pretrained ML models
│ ├── model.pkl # Decision Tree model
│ └── preprocessor.pkl # KNNImputer + feature pipeline
├── data_schema/
│ └── schema.yaml # Expected input schema
├── prediction_output/ # Stores prediction results (created after first run)
├── .github/
│ └── workflows/
│ └── main.yaml # GitHub Actions for CI/CD
├── requirements.txt # Python dependencies
├── Dockerfile # For containerizing the application
├── README.md # Documentation
└── test_input.csv # Sample test input

---

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/NetworkSecurityProject.git
cd NetworkSecurityProject

python -m venv .venv
# Activate:
.venv\Scripts\activate       # (Windows)
source .venv/bin/activate    # (Mac/Linux)

pip install -r requirements.txt
