# Spotify Hit Predictor

**Project's function:** Predict if a song becomes a hit based on audio features. Uses ML to find patterns behind popular tracks. Helps understand measurable traits tied to Spotify success.

**Dataset:** SpotifyFeatures.csv from Kaggle, containing 200k+ tracks with popularity and audio metrics like tempo, loudness, energy, and danceability.

**Pipeline/Architecture:** Batch pipeline with Airflow DAG scheduling, S3 storage, Python ingestion and transforms, RandomForestClassifier ML, Power BI dashboards.

**Data Quality Assessment:** Assessed using summary stats, missing values, correlation to popularity, and duplicate checks in EDA.py. Data cleaned and ready for modeling.

**Data Transformation & Model:** Removed bad values and outliers, standardized columns, dropped NaNs and duplicates, converted duration to minutes. Trained hit classifier and ranked feature importance.

**Special Instructions:** 
1. Put project files in one folder and install dependencies from requirements.txt.  
2. Run `python batch_ingest.py` or trigger Airflow DAG `batch_ingest_dag` to ingest raw CSV to data.pkl.  
3. Run `python transform.py` (or let the DAG run it) to create `clean_spotify.pkl` and `clean_spotify.csv`.  
4. Run `python model.py` to train and save `rf_model.pkl` and `feature_importance.pkl`.  
5. Open Power BI and import `clean_spotify.csv` and `feature_importance.pkl` (or CSV derived from it) to recreate dashboards.

**Deliverables:**
- ETL code (Airflow DAG + Python scripts)  
- Cleaned dataset: `clean_spotify.pkl` and `clean_spotify.csv`  
- Trained model: `rf_model.pkl` and `feature_importance.pkl`  
- Power BI `.pbix` dashboard (export saved locally)  
- Final report PDF and infographics

**Repo Link:** https://github.com/DKMirza/ECE_5984_Data_Engineering_Project