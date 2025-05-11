# 🚢 Ship Fuel Consumption Estimator

This project is a machine learning-powered web app that predicts fuel consumption for ships based on voyage characteristics, fuel type, and dynamic movement features derived from AIS (Automatic Identification System) data.

---

## 🔍 Project Overview

- 📊 Trained a regression model using real operational shipping data (Kaggle)
- 📡 Enriched the dataset with real-time AIS data from [AISStream.io](https://aisstream.io)
- 🧠 Built and tuned a Random Forest model with SHAP explainability
- 🌐 Deployed as an interactive Streamlit app for predictions

---

## 🛠 Features

- **Input:** Route distance, engine efficiency, fuel type, and AIS-based behavior (speed, duration, idle time, etc.)
- **Output:** Predicted fuel consumption in kg or tons
- **Model:** Random Forest Regressor, tuned using GridSearchCV
- **Explainability:** Feature importance and SHAP analysis
- **Frontend:** Built with Streamlit and deployed for interactive use

---

## 📁 Folder Structure

ship_fuel_model/
│
├── appp.py # Streamlit app
├── model/
│ └── ship_fuel_model_enhanced.pkl
├── data/
│ └── ship_fuel_efficiency.csv
│ └── merged_fuel_ais_enhanced.csv
├── requirements.txt # Dependencies
└── README.md # This file




---

## 🚀 How to Run Locally

```bash
git clone https://github.com/evapats123/ship-fuel-model.git
cd ship-fuel-model
pip install -r requirements.txt
streamlit run appp.py



Then open your browser at http://localhost:8501

⚠️ Disclaimer
This project is a prototype using publicly available AIS and fuel consumption data. AIS inputs were obtained through limited open APIs, which may not fully represent operational-scale data. This tool is for demonstration and learning purposes only.

✅ Use Cases
Fuel efficiency analysis (educational)

Demonstration of end-to-end ML pipeline in maritime

Interview-ready portfolio project with real-time data and deployment

💡 Future Improvements
Match AIS data by MMSI, IMO, or real trip identifiers

Integrate weather and wave data via APIs

Improve route tracking and ETA estimation

Try gradient boosting models (XGBoost, LightGBM)

👤 Author
evapats123
GitHub: https://github.com/evapats123

