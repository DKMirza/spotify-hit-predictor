import s3fs
from s3fs.core import S3FileSystem
import numpy as np
import pickle

def transform_data():

    s3 = S3FileSystem()
    # S3 bucket directory (data lake)
    DIR = 's3://ece5984-s3-dkmirza/Project1/'    # Insert your S3 bucket address here.
    # Get data from S3 bucket as a pickle file
    # with s3.open('{}/{}'.format(DIR, 'data.pkl'), 'rb') as f:
    with s3.open(f"{DIR}data.pkl", "rb") as f:
        raw_data = pickle.loads(f.read())

    # Check if data structure needs has expected columns
    expected_cols = ["genre", "artist_name", "track_name", "track_id", "popularity",
                     "acousticness", "danceability", "duration_ms", "energy", "instrumentalness",
                     "key", "liveness", "loudness", "mode", "speechiness", "tempo", "valence"]

    if not all(col in raw_data.columns for col in expected_cols):
        # Cleanup
        raw_data.columns = [col.strip().lower().replace(" ", "_") for col in raw_data.columns]

    # Dropping rows with NaN in them
    df_spotify = raw_data[expected_cols].dropna()

    # Remove obvious outliers (tempo, loudness, duration)
    df_spotify = df_spotify[df_spotify["tempo"].between(50, 220)]
    df_spotify = df_spotify[df_spotify["loudness"].between(-60, 5)]
    df_spotify = df_spotify[df_spotify["duration_ms"].between(90000, 600000)]

    # Dropping duplicate songs
    df_spotify = df_spotify.drop_duplicates(subset=["track_id"])

    # Convert milliseconds to minutes
    df_spotify["duration_min"] = df_spotify["duration_ms"] / 60000

    # Push cleaned data to S3 bucket warehouse
    DIR_wh = 's3://ece5984-s3-dkmirza/Project1/transformed'   # Insert your S3 bucket address here.
    with s3.open('{}/{}'.format(DIR_wh, 'clean_spotify.pkl'), 'wb') as f:
        f.write(pickle.dumps(df_spotify))