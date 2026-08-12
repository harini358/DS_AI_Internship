import pandas as pd

marks = pd.Series(
    [75, 58, 82, 67, 45],
    index=["Math", "Science", "English", "History", "Computer"]
)

# Access values using positions
print(marks.iloc[0])
print(marks.iloc[2])

# Access values using labels
print(marks["Math"])
print(marks["English"])

# Print values and index
print(marks.values)
print(marks.index)

# Filter marks above 60 using boolean masking
above_60 = marks[marks > 60]
print("Marks above 60:",above_60)