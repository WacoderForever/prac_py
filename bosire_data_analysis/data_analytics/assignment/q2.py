# S13/04402/21 - SETH OMONDI OTIENO

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import warnings
warnings.filterwarnings('ignore')

#LOAD DATA
try:
    df = pd.read_csv('Customer-Churn.csv')
    print(f"Dataset loaded – {df.shape[0]:,} rows, {df.shape[1]} columns\n")
except FileNotFoundError:
    print("File 'Telco-Customer-Churn.csv' not found.")
    raise

print("First 5 rows:")
print(df.head())
print("\nDataset info:")
print(df.info())

#DATA CLEANING & PREPROCESSING
print("\n" + "="*50)
print("DATA CLEANING & PREPROCESSING")
print("="*50)

#Missing values
print("Missing values before cleaning:")
print(df.isnull().sum())

#Remove any empty rows and clean TotalCharges
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df = df.dropna()

#Convert Churn to binary (0/1)
df['Churn'] = df['Churn'].map({'Yes': 1, 'No': 0})

print(f"\nAfter cleaning – {df.shape[0]:,} rows remaining")
print(f"Churn rate: {df['Churn'].mean():.2%}")

#FEATURE ENGINEERING
print("\n" + "="*50)
print("FEATURE ENGINEERING")
print("="*50)

#Create tenure groups
def tenure_group(tenure):
    if tenure <= 12:
        return '0-1 Year'
    elif tenure <= 24:
        return '1-2 Years'
    elif tenure <= 36:
        return '2-3 Years'
    elif tenure <= 48:
        return '3-4 Years'
    elif tenure <= 60:
        return '4-5 Years'
    else:
        return '5+ Years'

df['TenureGroup'] = df['tenure'].apply(tenure_group)

#Create monthly charge segments
df['MonthlyChargeSegment'] = pd.cut(df['MonthlyCharges'], 
                                   bins=[0, 35, 70, 105, 200], 
                                   labels=['Low', 'Medium', 'High', 'Very High'])

print("New features created: TenureGroup, MonthlyChargeSegment")

#DATA ANALYSIS
print("\n" + "="*50)
print("EXPLORATORY DATA ANALYSIS")
print("="*50)

# Visualisation
plt.style.use('seaborn-v0_8')
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1.Churn distribution
churn_counts = df['Churn'].value_counts()
axes[0,0].pie(churn_counts, labels=['No Churn', 'Churn'], autopct='%1.1f%%', 
              colors=['lightblue', 'lightcoral'])
axes[0,0].set_title('Customer Churn Distribution', fontsize=14, fontweight='bold')

# 2.Churn by tenure
tenure_churn = df.groupby('TenureGroup')['Churn'].mean().sort_index()
axes[0,1].bar(tenure_churn.index, tenure_churn.values, color='skyblue')
axes[0,1].set_title('Churn Rate by Tenure Group', fontsize=14, fontweight='bold')
axes[0,1].set_ylabel('Churn Rate')
axes[0,1].tick_params(axis='x', rotation=45)

# 3.Churn by monthly charges
charge_churn = df.groupby('MonthlyChargeSegment')['Churn'].mean()
axes[1,0].bar(charge_churn.index, charge_churn.values, color='lightgreen')
axes[1,0].set_title('Churn Rate by Monthly Charge Segment', fontsize=14, fontweight='bold')
axes[1,0].set_ylabel('Churn Rate')

# 4.Contract type impact
contract_churn = df.groupby('Contract')['Churn'].mean().sort_values()
axes[1,1].bar(contract_churn.index, contract_churn.values, color='orange')
axes[1,1].set_title('Churn Rate by Contract Type', fontsize=14, fontweight='bold')
axes[1,1].set_ylabel('Churn Rate')
axes[1,1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('churn_analysis_plots.png', dpi=300, bbox_inches='tight')
plt.show()

# Key insights from EDA
print("\nKey Insights from Exploratory Analysis:")
print(f"- Overall churn rate: {df['Churn'].mean():.2%}")
print(f"- Churn rate for 0-1 Year tenure: {tenure_churn['0-1 Year']:.2%}")
print(f"- Churn rate for Month-to-month contracts: {contract_churn['Month-to-month']:.2%}")
print(f"- Churn rate for High monthly charges: {charge_churn['High']:.2%}")

#MODELING
print("\n" + "="*50)
print("DATA PREPARATION FOR MODELING")
print("="*50)

#Features for modelling
features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'Contract', 'InternetService', 
            'PaymentMethod', 'SeniorCitizen'] 

#Create feature set X and target y
X = df[features].copy()
y = df['Churn']

#Encode categorical variables
categorical_cols = ['Contract', 'InternetService', 'PaymentMethod']
label_encoders = {}

for col in categorical_cols:
    le = LabelEncoder()
    X[col] = le.fit_transform(X[col])
    label_encoders[col] = le
    print(f"Encoded {col}: {dict(zip(le.classes_, le.transform(le.classes_)))}")

#Scale numerical features
scaler = StandardScaler()
numerical_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']
X[numerical_cols] = scaler.fit_transform(X[numerical_cols])

print(f"\nFinal feature matrix shape: {X.shape}")
print(f"Feature columns: {list(X.columns)}")

#Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, 
                                                    random_state=42, 
                                                    stratify=y)

print(f"Training set: {X_train.shape[0]:,} samples")
print(f"Testing set: {X_test.shape[0]:,} samples")

#MODEL TRAINING
print("\n" + "="*50)
print("MODEL TRAINING - LOGISTIC REGRESSION")
print("="*50)

#Train Logistic Regression model
model = LogisticRegression(random_state=42, max_iter=1000)
model.fit(X_train, y_train)

#Make predictions
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]  # Probability of churn

#MODEL EVALUATION
print("\n" + "="*50)
print("MODEL EVALUATION")
print("="*50)

#Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.3f} ({accuracy:.1%})")

#Classification report
print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred, target_names=['No Churn', 'Churn']))

#Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Predicted No', 'Predicted Yes'], 
            yticklabels=['Actual No', 'Actual Yes'])
plt.title('Confusion Matrix - Churn Prediction', fontsize=14, fontweight='bold')
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.tight_layout()
plt.savefig('churn_confusion_matrix.png', dpi=300, bbox_inches='tight')
plt.show()

#FEATURE IMPORTANCE ANALYSIS
print("\n" + "="*50)
print("FEATURE IMPORTANCE ANALYSIS")
print("="*50)

# Get feature coefficients (importance)
feature_importance = pd.DataFrame({
    'Feature': features,
    'Coefficient': model.coef_[0],
    'Absolute_Importance': abs(model.coef_[0])
}).sort_values('Absolute_Importance', ascending=False)

print("Top Indicators of Customer Churn (Feature Importance):")
print(feature_importance.round(4))

# BUSINESS INSIGHTS & PREDICTIONS
print("\n" + "="*50)
print("BUSINESS INSIGHTS & PREDICTIONS")
print("="*50)

# Analyze high-risk customers
high_risk_threshold = 0.7  # 70% probability
high_risk_customers = X_test[y_pred_proba > high_risk_threshold]

print(f"Number of high-risk customers (>{high_risk_threshold:.0%} probability): {len(high_risk_customers)}")
print(f"This represents {len(high_risk_customers)/len(X_test):.1%} of the test set")

# Profile of high-risk customers
if len(high_risk_customers) > 0:
    high_risk_original = df.loc[high_risk_customers.index]
    print("\nProfile of High-Risk Customers:")
    print(f"- Average tenure: {high_risk_original['tenure'].mean():.1f} months")
    print(f"- Average monthly charges: ${high_risk_original['MonthlyCharges'].mean():.2f}")
    print(f"- Most common contract: {high_risk_original['Contract'].mode()[0]}")
    print(f"- Most common payment method: {high_risk_original['PaymentMethod'].mode()[0]}")

# RETENTION STRATEGY RECOMMENDATIONS
print("\n" + "="*50)
print("RETENTION STRATEGY RECOMMENDATIONS")
print("="*50)

print("Based on the analysis, the most effective retention strategies would target:")
print("1. Customers with MONTH-TO-MONTH contracts (highest churn risk)")
print("2. New customers (0-1 year tenure)")
print("3. Customers with HIGH monthly charges")
print("4. Specific payment methods (Electronic check users)")

print("\nProactive retention actions:")
print("✓ Offer contract incentives for month-to-month customers")
print("✓ Implement 'welcome program' for new customers")
print("✓ Create personalized offers for high-spending at-risk customers")
print("✓ Payment method optimization campaigns")

print("\nModel can predict churn with reasonable accuracy for targeted interventions.")