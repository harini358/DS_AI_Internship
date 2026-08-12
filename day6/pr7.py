import pandas as pd
import numpy as np

# Create a Series containing names with different letter cases and missing values
names = pd.Series([
    "Alice",
    "BOB",
    np.nan,
    "Charlie",
    "DAVID",
    None,
    "Eve"
])

print("Original Series:",names)

print("\nMissing values:")
print(names.isna())

# Fill missing values
names_filled = names.fillna("Unknown")

print("\nAfter filling missing values:")
print(names_filled)

# Convert names to lowercase using .str operations
names_lower = names_filled.str.lower()

print("\nNames in lowercase:")
print(names_lower)

# Filter names containing the letter 'a'
filtered_names = names_lower[names_lower.str.contains("a", na=False)]

print("\nNames containing the letter 'a':")
print(filtered_names)