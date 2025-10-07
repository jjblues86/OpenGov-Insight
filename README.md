# 🏛️ OpenGov Insight  
**An AI-Powered Transparency Dashboard for Public Spending**

---

## 📘 Overview
**OpenGov Insight** is a Business Intelligence (BI) project that promotes government transparency by making public budget and spending data more accessible and understandable.  
The dashboard visualizes where money is allocated, detects anomalies or inefficiencies using AI, and generates automated insights for accountability and better decision-making.

> “Empowering citizens and policymakers through open, data-driven insights.”

---

## 🎯 Objectives
- Collect and clean public government financial data (or simulated data).  
- Build an interactive BI dashboard for spending vs. budget tracking.  
- Integrate AI-powered anomaly detection and natural-language summaries.  
- Deploy a public demo for transparency and education.  
- Document the full lifecycle for portfolio and research purposes.

---

## 🧱 System Architecture (Planned)
```mermaid
graph TD
A[Open Government Data] --> B[ETL Pipeline (Python, Pandas)]
B --> C[Database (PostgreSQL / CSV)]
C --> D[BI Dashboard (Power BI / Streamlit)]
D --> E[AI Insights (Scikit-learn + GPT API)]
E --> F[Public Access Portal]
```

##  ⚙️ Tech Stack
| Layer                          | Technology                         |
| ------------------------------ | ---------------------------------- |
| **Data Collection & Cleaning** | Python, Pandas, NumPy              |
| **Storage**                    | PostgreSQL / AWS S3                |
| **Visualization**              | Power BI / Streamlit + Plotly      |
| **AI & Analytics**             | Scikit-learn, OpenAI GPT API       |
| **Deployment**                 | Streamlit Cloud / Power BI Service |
| **Version Control**            | Git + GitHub                       |
| **Project Management**         | Notion / Trello                    |


## 🚀 Getting Started
### 1. Clone the Repository
git clone https://github.com/<your-username>/OpenGov-Insight.git
cd OpenGov-Insight

## 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # (Mac/Linux)
venv\Scripts\activate      # (Windows)


## 3. Install Dependencies
pip install -r requirements.txt


## 4. Run Initial Notebook
### Open the notebooks/ folder and explore the sample ETL notebook:
jupyter notebook notebooks/data_exploration.ipynb
