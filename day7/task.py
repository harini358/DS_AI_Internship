import pandas as pd
import numpy as np

data = pd.read_excel(r"C:\Users\MYHP\Desktop\DS_AI_Internship\task.xlsx")

print("Original Dataset:")
print(data)

print("\nOriginal Shape:")
print(data.shape)

print("\nMissing Values:")
print(data.isnull().sum())

print("\nTotal Missing Values:")
print(data.isnull().sum().sum())

print("\nNumber of Duplicate Rows:")
print(data.duplicated().sum())

print("\nDuplicate Rows:")
print(data[data.duplicated()])

data = data.drop_duplicates()

print("\nShape After Removing Duplicates:")
print(data.shape)

data["Name"] = data["Name"].fillna("Unknown")

data["Age"] = data["Age"].fillna(data["Age"].mean())

data["City"] = data["City"].fillna(data["City"].mode()[0])

print("\nMissing Values After Cleaning:")
print(data.isnull().sum())

print("\nCleaned Dataset:")
print(data)

print("\nCleaned Dataset Shape:")
print(data.shape)