import pandas as pd
import numpy as np

data = {
    "Student_ID": [101, 102, 103, 104, 105, 106, 107, 108,
                   109, 110, 111, 112, 113, 114, 115, 103, 107],
    "Name": ["Asha", "Rahul", "Priya", "Kiran", "Sneha", "Arjun",
             "Divya", "Ravi", "Anjali", "Vikas", "Neha", "Rohan",
             "Pooja", "Manoj", "Kavya", "Priya", "Divya"],
    "Marks": [85, 78, np.nan, 92, 67, 74, 88, np.nan,
              81, 69, 95, 73, np.nan, 84, 77, np.nan, 88],
    "Attendance": [90, 85, 88, np.nan, 75, 80, 95, 70,
                   np.nan, 82, 96, 78, 85, np.nan, 91, 88, 95]
}

df = pd.DataFrame(data)

print("Original Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull())

print("\nCount of Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df[df.duplicated()])

print("\nNumber of Duplicate Records:", df.duplicated().sum())

df = df.drop_duplicates()

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

print("\nCleaned Dataset:")
print(df)

print("\nCleaned Shape:", df.shape)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())