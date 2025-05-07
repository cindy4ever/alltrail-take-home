# AllTrails Data Engineering Take-Home Assignment

This repository contains a batch-processing job to analyze the relationship between user signup and their first and second GPS recordings in the AllTrails platform.

## 📁 Project Structure
```
all-trails-take-home/
├── data/ # Folder where downloaded data files will be stored
├── scripts/
│ ├── download_data.py # Script to download datasets from Google Drive
│ └── process_data.py # Script to process the data into clean structured CSVs
├── tests/
│ └── test_process_data.py # Unit tests for data processing
├── README.md # This file
├── requirements.txt # Python dependencies
└── .gitignore
```


---

## 📥 Data Sources

- `users_2017.tsv`: User signup and Pro subscription data
- `recordings_2017.tsv`: Activity recordings including summary stats

These are downloaded from Google Drive using their file IDs.

---

## ▶️ How to Run

1. **Clone the repository**:

```
git clone https://github.com/yourusername/all-trails-take-home.git
cd all-trails-take-home
```
Install dependencies:

```pip install -r requirements.txt```

Download the data:

```python scripts/download_data.py```

Process the data:

```python scripts/process_data.py```

This will generate two CSV files:

1. output/first_recordings.csv

2. output/second_recordings.csv

✅ Unit Tests
To run unit tests:
```pytest tests/```

📄 Output
The final output includes:

1. Cleaned user data

2. First and second recording information

3. Time difference (in hours) between signup and recording


🧠 Assumptions
1. Only the first two recordings per user are relevant for this analysis.

2. Invalid or malformed JSON in Recording_Summary is skipped with a warning.

3. Time differences are calculated in hours and rounded to two decimal places.

🚀 Next Steps (If More Time/Data Were Available)
1. Integrate into a data pipeline using Airflow or Prefect

2. Store output in a data warehouse (e.g., BigQuery, Snowflake)
   
3. Include user engagement metrics beyond recordings

🛠️ Requirements
See requirements.txt for all dependencies.
