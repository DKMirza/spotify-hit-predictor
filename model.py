from s3fs.core import S3FileSystem
import pickle
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

def train_model():
    s3 = S3FileSystem()
    DIR = "s3://ece5984-s3-dkmirza/Project1/"

    # Load your cleaned dataset (output of transform.py)
    with s3.open(f"{DIR}clean_spotify.pkl", "rb") as f:
        df = pickle.load(f)

    # Define hit song threshold
    df["hit"] = (df["popularity"] >= 90).astype(int)

    # Train Random Forest Model
    features = ["acousticness", "danceability", "duration_min",
                "energy", "instrumentalness", "key", "liveness",
                "loudness", "mode", "speechiness", "tempo", "valence"]

    X = df[features]
    y = df["hit"]

    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X, y)

    # Save model
    with s3.open(f"{DIR}rf_model.pkl", "wb") as f:
        f.write(pickle.dumps(rf))

    # Save feature importance results
    importance = pd.DataFrame({
        "feature": features,
        "importance": rf.feature_importances_
    }).sort_values(by="importance", ascending=False)

    with s3.open(f"{DIR}feature_importance.pkl", "wb") as f:
        f.write(pickle.dumps(importance))

    print("✅ Model training complete. Model and feature importance saved to S3.")
