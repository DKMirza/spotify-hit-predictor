import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load your cleaned dataset (output of transform.py)
print("Loading cleaned dataset...")
with open("clean_spotify.pkl", "rb") as f:
    df = pickle.load(f)
print("Loaded dataset with shape:", df.shape)

# Define hit song threshold
df["hit"] = (df["popularity"] >= 90).astype(int)
print("Created 'hit' label. Number of hit songs:", df["hit"].sum())

# Encode categorical variables
df["mode"] = df["mode"].replace({"Major": 1, "Minor": 0}).infer_objects(copy=False).astype(int)
df["key"] = pd.factorize(df["key"])[0]  # Encode keys C#, A, etc.
print("Encoded categorical columns: mode, key")

# Train Random Forest Model
features = ["acousticness", "danceability", "duration_min",
            "energy", "instrumentalness", "key", "liveness",
            "loudness", "mode", "speechiness", "tempo", "valence"]

X = df[features]
y = df["hit"]
print("Training data prepared. Feature matrix shape:", X.shape)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
print("Training Random Forest model...")
rf.fit(X, y)
print("Model training complete.")

# Save model
with open("rf_model.pkl", "wb") as f:
    pickle.dump(rf, f)
print("Saved Random Forest model -> rf_model.pkl")

# Save feature importance results
importance = pd.DataFrame({
    "feature": features,
    "importance": rf.feature_importances_
}).sort_values(by="importance", ascending=False)

with open("feature_importance.pkl", "wb") as f:
    pickle.dump(importance, f)
print("Saved feature importances -> feature_importance.pkl")

df.to_csv("clean_spotify.csv", index=False)
print("Converted clean_spotify pkl to csv for PowerBI")

importance.to_csv("feature_importance.csv", index=False)
print("Converted feature_importance pkl to csv for PowerBI")

print("✅ Model training complete. Model and feature importance saved locally.")