# Network Security – Phishing URL Detection

![Python](https://img.shields.io/badge/Python-3.10%2B-blue) 

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

## ⚙️ Installation & Usage

### 1. Clone the Repository
```bash
git clone https://github.com/kash1shh/NetworkSecurityProject.git
cd NetworkSecurityProject
```

### 2. Create & activate virtual environment
```bash
python -m venv .venv
# Activate:
.venv\Scripts\activate       # (Windows)
source .venv/bin/activate    # (Mac/Linux)
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Streamlit frontend 
```bash
streamlit run app_streamlit.py
```
or  Run FastAPI backend
```bash
python app.py
```

### 6. Optional: Docker Build & Run
```bash
docker build -t network-security-app .
docker run -p 8000:8000 network-security-app
```
###
**[You can try the deployed application here.](https://networksecurity123.streamlit.app/)** 


