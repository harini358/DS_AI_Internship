import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

data = {
    'Income': [30000, 50000, 25000, 70000, 45000, 90000, 28000, 60000,
               35000, 80000, 40000, 55000, 22000, 75000, 65000],
    
    'Credit_Score': [550, 700, 500, 750, 650, 800, 520, 720,
                     580, 780, 620, 680, 480, 760, 730],
    
    'Loan_Amount': [20000, 15000, 25000, 10000, 18000, 12000, 30000, 14000,
                    22000, 10000, 20000, 16000, 28000, 11000, 13000],
    
    'Employment_Status': [0, 1, 0, 1, 1, 1, 0, 1,
                          0, 1, 1, 1, 0, 1, 1],
    
    'Previous_Payment_History': [0, 1, 0, 1, 1, 1, 0, 1,
                                 0, 1, 1, 1, 0, 1, 1],
    
    'Default': [1, 0, 1, 0, 0, 0, 1, 0,
                1, 0, 0, 0, 1, 0, 0]
}

df = pd.DataFrame(data)

print(df.head())

X = df[['Income',
        'Credit_Score',
        'Loan_Amount',
        'Employment_Status',
        'Previous_Payment_History']]

y = df['Default']

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

model = LogisticRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1-Score :", f1)

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

plt.figure(figsize=(6, 4))

sns.heatmap(
    cm,
    annot=True,
    fmt='d',
    cmap='Blues',
    xticklabels=['No Default', 'Default'],
    yticklabels=['No Default', 'Default']
)

plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix - Loan Default Prediction')

plt.show()