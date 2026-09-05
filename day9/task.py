import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create the dataset you sent
df = pd.read_csv("taskk.csv")
# Display dataset
print("DATASET")
print(df)

# Basic information
print("\nDATA INFORMATION")
print(df.info())

# Check missing values
print("\nMISSING VALUES")
print(df.isnull().sum())

# Statistical summary
print("\nSTATISTICAL SUMMARY")
print(df.describe())

# Univariate analysis
print("\nGENDER")
print(df["gender"].value_counts())

print("\nDEPARTMENT")
print(df["department"].value_counts())

# Average marks by department
print("\nAVERAGE MARKS BY DEPARTMENT")
print(df.groupby("department")["marks"].mean())

# Skewness
print("\nSKEWNESS")
print(df[["age", "studytime", "marks"]].skew())

# Correlation
print("\nCORRELATION")
print(df[["age", "studytime", "marks"]].corr())

# ---------------- VISUALIZATION ----------------

# 1. Marks distribution
plt.hist(df["marks"], edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Students")
plt.show()

# 2. Department vs Marks
sns.barplot(x="department", y="marks", data=df)
plt.title("Department vs Marks")
plt.show()

# 3. Studytime vs Marks
sns.scatterplot(x="studytime", y="marks", data=df)
plt.title("Study Time vs Marks")
plt.show()

# 4. Correlation heatmap
sns.heatmap(
    df[["age", "studytime", "marks"]].corr(),
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation")
plt.show()

# 5. Outlier detection
sns.boxplot(data=df[["age", "studytime", "marks"]])
plt.title("Outlier Detection")
plt.show()

#Insights

#Average marks: The average marks of students is approximately 77.14.
#Study time and marks: There is a strong positive relationship between study time and marks. Students who study more tend to have higher marks.
#Skewness: Age, study time, and marks are approximately normally distributed with only slight skewness.
#Outliers: No significant outliers were detected 
#Study time and marks: Students who study more generally get higher marks.