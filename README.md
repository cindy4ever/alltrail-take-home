AllTrails Data Engineering Take-Home

📌 Objective

This project processes and analyzes user signup and recording activity data to explore the relationship between early activity engagement and Pro subscription conversion on the AllTrails platform. The result is a clean, structured dataset that data analysts can use for further insights.

🗂️ Project Structure

alltrails-project/
├── data/                     # Folder where downloaded .tsv files will go
├── output/                   # Folder for processed CSV outputs
├── scripts/
│   ├── download_data.py      # Script to download datasets from Google Drive
│   └── process_data.py       # Script to process and join datasets
├── tests/
│   ├── test_download_data.py # Unit tests for data download
│   └── test_process_data.py  # Unit tests for processing logic
└── README.md

🧪 How to Run

1. Install Dependencies

pip install -r requirements.txt

Requirements

pandas
gdown

2. Download Data

python scripts/download_data.py

This will download:

users_2017.tsv

recordings_2017.tsv

...into the data/ directory using Google Drive file IDs.

3. Process Data

python scripts/process_data.py

This generates two output files in the output/ directory:

first_recordings_output.csv

second_recordings_output.csv

🧼 Data Handling

The output files:

Join each user with their first and second recording (if available)

Flatten the Recording_Summary JSON field into columns like summary_distance, summary_duration

Add hours_to_first_recording and hours_to_second_recording as calculated fields

🧪 Tests

Run unit tests for both download and processing steps:

python -m unittest discover tests/

📌 Assumptions

Only the first and second recordings are used for this analysis.

Timestamps are assumed to be in a uniform timezone.

Invalid or missing Recording_Summary fields are handled as empty dicts.

All users in the user dataset have at least a signup date.

🚀 Next Steps (If More Time)

Use PySpark for large-scale processing instead of Pandas.

Upload outputs to a cloud warehouse (e.g., Snowflake or BigQuery).

Add orchestration with Airflow or Prefect.

Perform statistical analysis on correlation between early engagement and subscription.