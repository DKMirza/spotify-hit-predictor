import s3fs
from s3fs.core import S3FileSystem
import numpy as np
import pickle
import pandas as pd

def ingest_data():
    s3 = S3FileSystem()
    # S3 bucket directory
    DIR = 's3://ece5984-s3-dkmirza/Project1/'  # insert your S3 URI here

    # --- Read csv directly from S3 ---
    with s3.open(f'{DIR}SpotifyFeatures.csv', 'rb') as f:
        data = pd.read_csv(f)

    # Push data to S3 bucket as a pickle file
    # with s3.open('{}/{}'.format(DIR, 'data.pkl'), 'wb') as f:
    with s3.open(f"{DIR}data.pkl", "wb") as f:
        f.write(pickle.dumps(data))