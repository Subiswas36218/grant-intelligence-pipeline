# 🚀 Grant Intelligence Pipeline (LLM-Powered)

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![OpenAI](https://img.shields.io/badge/OpenAI-LLM-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 Overview

An AI-powered system for discovering, structuring, and evaluating grant opportunities.

This project demonstrates how unstructured funding data can be transformed into structured insights using data pipelines, rule-based scoring, and Large Language Models (LLMs).

---

## 🌐 Live Demo

🚀 **Try the app here:**  
👉 https://grant-intelligence-pipeline-yq8hqu9brqu9642djibpga.streamlit.app/

---

## 🔥 Features

- 📥 Automated data ingestion (mock/API-ready)
- 🧹 Data parsing, cleaning, and structuring
- 📊 Rule-based scoring system
- 🤖 LLM-based semantic scoring (OpenAI)
- 🧠 Combined scoring (rule + LLM)
- 📈 Interactive Streamlit dashboard
- ⚡ Real-time ranking of opportunities

---

## 🧠 Architecture:

Raw Data → Parsing → Cleaning → Feature Extraction

→ Rule-Based Scoring → LLM Scoring → Final Ranking → Dashboard

---

## ⚙️ Tech Stack

- **Python**
- **Pandas**
- **Streamlit**
- **OpenAI API**
- **python-dotenv**

---

## 📂 Project Structure
grant-intelligence-pipeline/
│
├── app/                          # Streamlit frontend (UI layer)
│   └── dashboard.py
│
├── data/                         # Raw input data
│   └── raw_grants.json
│
├── src/                          # Core logic (backend / pipeline)
│   ├── __init__.py               # Makes src a Python package
│   ├── scraper.py                # Data ingestion
│   ├── parser.py                 # Extract fields
│   ├── cleaner.py                # Data cleaning
│   ├── scorer.py                 # Rule-based scoring
│   ├── llm_scorer.py             # LLM-based scoring (OpenAI)
│   ├── storage.py                # Save structured data
│   └── pipeline.py               # Orchestrates full pipeline
│
├── output/                       # Generated outputs
│   └── structured_grants.csv
│
├── .env                          # API keys (NOT committed)
├── .gitignore                    # Ignore sensitive/system files
├── requirements.txt              # Dependencies
└── README.md                     # Documentation

---

## ▶️ Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/grant-intelligence-pipeline.git
cd grant-intelligence-pipeline

2. Create virtual environment

python3 -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Add API key

Create .env file:

OPENAI_API_KEY=your_api_key_here

5. Run dashboard

streamlit run app/dashboard.py

🔑 Deployment (Streamlit Cloud)

Hosted on Streamlit Community Cloud

Secrets used for secure API key storage

Add this in Streamlit Secrets:

OPENAI_API_KEY = "your_api_key_here"

📊 Output

Structured dataset of grants

Scored opportunities (rule-based + LLM)

Ranked list of best funding options

Visual insights via dashboard

🧠 Key Concepts Demonstrated

Data Pipelines (ETL)

Information Retrieval

Data Structuring

Feature Engineering

LLM Integration

Decision Support Systems

🚀 Future Improvements

🌐 Real-time grant scraping (EU, NSF APIs)

🧠 Personalized user profile matching

📊 Advanced dashboard filters & search

🕸️ Knowledge graph (Neo4j)

🤖 Multi-agent reasoning system

👨‍💻 Author



Subhankar Biswas

MSc Data Engineering (Germany)

Focus: Data Engineering, AI Systems, LLM Applications

