import os
import pandas as pd
import json
from datetime import datetime

def load_data(data_dir="data"):
    users = pd.read_csv(os.path.join(data_dir, "users_2017.tsv"), sep="\t", parse_dates=["signup_date", "start_date"])
    recs = pd.read_csv(os.path.join(data_dir, "recordings_2017.tsv"), sep="\t", parse_dates=["Date_Time"])
    return users, recs

def expand_recording_summary(df):
    summary_expanded = df["Recording_Summary"].apply(lambda x: json.loads(x) if pd.notnull(x) else {})
    summary_df = pd.json_normalize(summary_expanded)
    summary_df.columns = [f"summary_{col}" for col in summary_df.columns]
    return pd.concat([df.drop(columns=["Recording_Summary"]), summary_df], axis=1)

def process_recordings(users, recs, recording_index=1):
    recs = recs.sort_values(["Pseudo_User_ID", "Date_Time"]).copy()
    recs["recording_index"] = recs.groupby("Pseudo_User_ID").cumcount() + 1
    target_recs = recs[recs["recording_index"] == recording_index]
    target_recs = expand_recording_summary(target_recs)

    merged = pd.merge(users, target_recs, on="Pseudo_User_ID", how="left")

    # Rename columns for clarity
    merged.rename(columns={
        "Pseudo_User_ID": "user_id",
        "signup_date": "signup_date",
        "start_date": "pro_start_date",
        "Recording_ID": f"{ordinal(recording_index)}_recording_id",
        "Date_Time": f"{ordinal(recording_index)}_recording_time",
        "Activity_Type": f"{ordinal(recording_index)}_activity_type",
    }, inplace=True)

    # Calculate time difference in hours between signup and recording
    merged[f"hours_to_{ordinal(recording_index)}_recording"] = (
        (merged[f"{ordinal(recording_index)}_recording_time"] - merged["signup_date"]).dt.total_seconds() / 3600
    ).round(2)

    return merged

def ordinal(n):
    """Returns ordinal string: 1 -> 'first', 2 -> 'second', etc."""
    return ["first", "second", "third", "fourth", "fifth"][n - 1]

def save_output(df, recording_index, output_dir="output"):
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{ordinal(recording_index)}_recordings_output.csv"
    df.to_csv(os.path.join(output_dir, filename), index=False)
    print(f"✅ Saved: {filename}")

def main():
    users, recs = load_data()

    # Process first recording
    first_df = process_recordings(users, recs, recording_index=1)
    save_output(first_df, recording_index=1)

    # Bonus: Process second recording
    second_df = process_recordings(users, recs, recording_index=2)
    save_output(second_df, recording_index=2)

if __name__ == "__main__":
    main()