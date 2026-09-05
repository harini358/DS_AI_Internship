import pandas as pd

df = pd.read_csv("weather.csv")

print(df.head())
print(df.shape)
print(df.describe())
X = df[["Humidity", "WindSpeed", "Pressure"]]
y = df["Temperature"]