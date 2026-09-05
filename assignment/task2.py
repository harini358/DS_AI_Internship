import pandas as pd
import numpy as np

names = pd.Series(["Harini", "RAHUL", np.nan, "Anjali", "PRIYA", np.nan, "Kiran"])

print("Original names:")
print(names)

print("\nMissing values:")
print(names.isna())

names = names.fillna("Unknown")

names = names.str.lower()

print("\nAfter filling missing values and converting to lowercase:")
print(names)

filtered_names = names[names.str.contains("a")]

print("\nNames containing the letter 'a':")
print(filtered_names)