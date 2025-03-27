import pandas as pd

# Load data directly from the web
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# Explore data
print("First 5 rows:\n", df.head())
print("\nStatistics:\n", df.describe())

# Clean data: Remove rows with missing values
df_clean = df.dropna()

# Filter data: Show only 'setosa' species
setosa = df_clean[df_clean['species'] == 'setosa']
print("\nSetosa samples:\n", setosa.head())

# Save cleaned data
df_clean.to_csv("iris_clean.csv", index=False)
print("\nSaved cleaned data to iris_clean.csv!")