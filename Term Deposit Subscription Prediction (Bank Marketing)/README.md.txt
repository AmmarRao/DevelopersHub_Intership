# Bank Marketing Term Deposit Prediction

## Project Overview
This project predicts whether a bank customer will subscribe to a term deposit based on marketing campaign data. Machine learning classification models are used to analyze customer behavior and improve marketing strategies.

## Dataset
The dataset used is the **Bank Marketing Dataset** from the UCI Machine Learning Repository.  
It contains information about direct marketing campaigns conducted by a Portuguese banking institution.

Dataset features include:
- Customer demographic information
- Financial information
- Campaign interaction data
- Previous marketing outcomes

Target variable:
y → whether the client subscribed to a term deposit (yes/no)

Dataset size:
41,188 records and 21 features.

## Technologies Used
Python  
Pandas  
NumPy  
Matplotlib  
Seaborn  
Scikit-learn  
SHAP

## Machine Learning Models
Two classification models were implemented:

- Logistic Regression
- Random Forest Classifier

## Data Preprocessing
Steps performed:
- Loaded dataset
- Checked for missing values
- Encoded categorical variables using One-Hot Encoding
- Split data into training and testing sets

## Model Evaluation
Models were evaluated using:

- Confusion Matrix
- Classification Report
- F1 Score
- ROC Curve
- AUC Score

Random Forest achieved better performance compared to Logistic Regression.

## Explainable AI (XAI)
SHAP (SHapley Additive exPlanations) was used to explain model predictions and identify which features influenced customer subscription decisions.

Key influential features included:
- Call duration
- Previous campaign outcome
- Age
- Number of contacts

## Results
The Random Forest model demonstrated strong predictive performance and provided insights into factors affecting customer behavior.

These insights can help banks design more targeted and effective marketing campaigns.

## Project Structure
# Bank Marketing Term Deposit Prediction

## Project Overview
This project predicts whether a bank customer will subscribe to a term deposit based on marketing campaign data. Machine learning classification models are used to analyze customer behavior and improve marketing strategies.

## Dataset
The dataset used is the **Bank Marketing Dataset** from the UCI Machine Learning Repository.  
It contains information about direct marketing campaigns conducted by a Portuguese banking institution.

Dataset features include:
- Customer demographic information
- Financial information
- Campaign interaction data
- Previous marketing outcomes

Target variable:
y → whether the client subscribed to a term deposit (yes/no)

Dataset size:
41,188 records and 21 features.

## Technologies Used
Python  
Pandas  
NumPy  
Matplotlib  
Seaborn  
Scikit-learn  
SHAP

## Machine Learning Models
Two classification models were implemented:

- Logistic Regression
- Random Forest Classifier

## Data Preprocessing
Steps performed:
- Loaded dataset
- Checked for missing values
- Encoded categorical variables using One-Hot Encoding
- Split data into training and testing sets

## Model Evaluation
Models were evaluated using:

- Confusion Matrix
- Classification Report
- F1 Score
- ROC Curve
- AUC Score

Random Forest achieved better performance compared to Logistic Regression.

## Explainable AI (XAI)
SHAP (SHapley Additive exPlanations) was used to explain model predictions and identify which features influenced customer subscription decisions.

Key influential features included:
- Call duration
- Previous campaign outcome
- Age
- Number of contacts

## Results
The Random Forest model demonstrated strong predictive performance and provided insights into factors affecting customer behavior.

These insights can help banks design more targeted and effective marketing campaigns.

## Project Structure

Bank-Marketing-Prediction
│
├── bank_marketing_prediction.ipynb
├── bank-additional-full.csv
└── README.md


## Author
Muhammad Ammar Rao  
Data Science & Analytics Internship – DevelopersHub Corporation
