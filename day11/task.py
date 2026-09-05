import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import confusion_matrix

data = pd.read_csv("diabetes.csv")

print("First 5 rows:")
print(data.head())

print("\nDataset shape:")
print(data.shape)

print("\nMissing values:")
print(data.isnull().sum())

X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# PART A: SUPERVISED LEARNING
# Diabetes Classification
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=1000)

model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)

print("\n========== SUPERVISED LEARNING ==========")

print("Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

new_patient = [[
    2,       # Pregnancies
    150,     # Glucose
    80,      # BloodPressure
    25,      # SkinThickness
    100,     # Insulin
    32.5,    # BMI
    0.5,     # DiabetesPedigreeFunction
    45       # Age
]]

new_patient_scaled = scaler.transform(new_patient)

prediction = model.predict(new_patient_scaled)
probability = model.predict_proba(new_patient_scaled)

print("\n========== NEW PATIENT ==========")

if prediction[0] == 1:
    print("Prediction: Diabetes")
else:
    print("Prediction: No Diabetes")

print("Probability of diabetes:",
      probability[0][1])

# PART B: UNSUPERVISED LEARNING
# Patient Clustering

X_scaled = StandardScaler().fit_transform(X)


# --------------------------------------------
# 10. Apply K-Means clustering
# --------------------------------------------

kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

clusters = kmeans.fit_predict(X_scaled)

data["Cluster"] = clusters

print("\n========== UNSUPERVISED LEARNING ==========")

print("\nNumber of patients in each cluster:")
print(data["Cluster"].value_counts().sort_index())


cluster_summary = data.groupby("Cluster").mean(numeric_only=True)

print("\nCluster Summary:")
print(cluster_summary)

# --------------------------------------------
# 14. Visualize patient clusters
# --------------------------------------------

plt.figure(figsize=(8, 6))

plt.scatter(
    data["Glucose"],
    data["BMI"],
    c=data["Cluster"],
    cmap="viridis",
    alpha=0.7
)

plt.xlabel("Glucose")
plt.ylabel("BMI")
plt.title("Patient Clusters Based on Health Characteristics")
plt.colorbar(label="Cluster")

plt.show()