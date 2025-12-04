import numpy as np
import pandas as pd
import pickle


# Raw data
# raw_data = np.load(r'clean_spotify.pkl', allow_pickle=True)   # Load pickle data here
with open("clean_spotify.pkl", "rb") as f:
    raw_data = pickle.load(f)

print("=== Spotify Dataset Overview ===")
print(raw_data.info())
print("Shape:", raw_data.shape)
print("====================================")

# Display summary stats
print("Descriptive statistics:")
print(raw_data.describe().T)
print("====================================")

# Missing values
print("Missing values by column:")
print(raw_data.isnull().sum().sort_values(ascending=False))
print("====================================")

# Check for duplicates
print("Duplicate rows:", raw_data.duplicated().sum())

# Correlation with popularity
numeric_cols = raw_data.select_dtypes(include=['number'])
corr = numeric_cols.corr()["popularity"].sort_values(ascending=False)
print("\nCorrelation of features with popularity:")
print(corr)

# Display top and bottom correlated features
print("\nTop 5 correlated features:")
print(corr.head(5))
print("\nLowest 5 correlated features:")
print(corr.tail(5))