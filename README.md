# E-Commerce-Recommendation-System
This project aims to build a Machine Learning-based Product Recommendation System for e-commerce platforms. The goal is to help users discover relevant products by predicting product ratings and showcasing intelligent suggestions based on review count, brand, and category features.

📌 Project Overview
Project Title: E-Commerce Product Recommendation System

Domain: Machine Learning + Web App Development

Tech Stack: Python, Pandas, Scikit-learn, XGBoost, Streamlit

Team Members: Krishna Vamsi & Team

Internship Role: Data Science Internship



🎯 Project Goals
Clean and analyze product dataset

Visualize key insights using charts and distributions

Train machine learning models (Random Forest, XGBoost)

Build a prediction system to estimate product ratings

Create an interactive, presentable web application using Streamlit



🧠 About the Recommendation System
Recommendation systems are algorithms that suggest products users are likely to buy or rate highly. In this project, we experimented with:

✅ Content-Based Filtering

✅ Collaborative Filtering (planned for future)

✅ Hybrid and Multi-model systems

✅ XGBoost Regressor to predict product ratings based on inputs



🛠️ Features of the Web App (Role-4)
Upload cleaned dataset (clean_data.csv)

Display tabular data and 20+ interactive visualizations (histograms, boxplots, pairplots, heatmaps, category plots)

Input form to predict product rating using a trained ML model

Dynamic layout, team introduction, and project summary

Streamlit-based interface (easy to use, visually rich)


🛠️ Features of the Web App (Role-4)
Upload cleaned dataset (clean_data.csv)

Display tabular data and 20+ interactive visualizations (histograms, boxplots, pairplots, heatmaps, category plots)

Input form to predict product rating using a trained ML model

Dynamic layout, team introduction, and project summary

Streamlit-based interface (easy to use, visually rich)

📂 File Structure

📁 E-Commerce-Recommendation-System/
├── app.py                   # Streamlit web application (Role-4)
├── xgb_model.joblib         # Trained XGBoost model
├── clean_data.csv           # Cleaned dataset for training and display
└── README.md                # Project overview and usage instructions
▶️ How to Run
Clone or download the repository.

Make sure you have all dependencies installed:-

pip install -r requirements.txt
Start the app using:

streamlit run app.py
Upload clean_data.csv when prompted in the web app.

Use the prediction form to enter:

Review Count

Brand Encoded

Product Categories

📊 Visuals & Analysis
The app includes:

Distribution plots for ratings, review counts

Brand-wise boxplots

Heatmaps of feature correlation

Pairplots and histograms

Top 20 product categories bar chart

✅ Contributions by Role
Role	Description
Role 1	Data Cleaning & Preprocessing
Role 2	Visualization using Power BI
Role 3	ML Model Development using RandomForest & XGBoost
Role 4	Streamlit App for Presenting the Project
