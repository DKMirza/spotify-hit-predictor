# Spotify Hit Predictor

**Project's function:** Predict if a song becomes a hit based on audio features. Uses ML to find patterns behind popular tracks. Helps understand measurable traits tied to Spotify success.

**Dataset:** SpotifyFeatures.csv from Kaggle, containing 200k+ tracks with popularity and audio metrics like tempo, loudness, energy, and danceability.

**Pipeline/Architecture:** Batch pipeline with Airflow DAG scheduling, S3 storage, Python ingestion and transforms, RandomForestClassifier ML, Power BI dashboards.

**Data Quality Assessment:** Assessed using summary stats, missing values, correlation to popularity, and duplicate checks in EDA.py. Data cleaned and ready for modeling.

**Data Transformation & Model:** Removed bad values and outliers, standardized columns, dropped NaNs and duplicates, converted duration to minutes. Trained hit classifier and ranked feature importance.

**Special Instructions:** Run batch_ingest.py then transform.py before training model.py. Convert pickle to CSV for Power BI import if reproducing locally.

**Repo Link:** Private GitHub repository submitted separately for replication and review.