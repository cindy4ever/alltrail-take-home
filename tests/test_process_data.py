import unittest
import pandas as pd
from pandas.testing import assert_frame_equal
from datetime import datetime
from scripts import process_data

class TestProcessData(unittest.TestCase):

    def setUp(self):
        # Sample user data
        self.users = pd.DataFrame({
            "Pseudo_User_ID": [1, 2],
            "signup_date": [pd.Timestamp("2017-01-01"), pd.Timestamp("2017-02-01")],
            "start_date": [pd.Timestamp("2017-01-15"), pd.Timestamp("2017-02-10")]
        })

        # Sample recordings data
        self.recs = pd.DataFrame({
            "Recording_ID": [101, 102, 103],
            "Date_Time": [pd.Timestamp("2017-01-02"), pd.Timestamp("2017-02-03"), pd.Timestamp("2017-02-05")],
            "Pseudo_User_ID": [1, 2, 2],
            "Activity_Type": ["hike", "bike", "run"],
            "Recording_Summary": [
                '{"distance": 5, "duration": 60}',
                '{"distance": 10, "duration": 120}',
                '{"distance": 3, "duration": 30}'
            ],
            "City": ["SF", "LA", "NY"],
            "State": ["CA", "CA", "NY"],
            "Country": ["US", "US", "US"]
        })

    def test_expand_recording_summary(self):
        expanded = process_data.expand_recording_summary(self.recs.copy())
        self.assertIn("summary_distance", expanded.columns)
        self.assertIn("summary_duration", expanded.columns)
        self.assertEqual(expanded.loc[0, "summary_distance"], 5)

    def test_process_first_recording(self):
        result = process_data.process_recordings(self.users.copy(), self.recs.copy(), recording_index=1)
        self.assertIn("first_recording_id", result.columns)
        self.assertIn("hours_to_first_recording", result.columns)
        self.assertAlmostEqual(result.loc[0, "hours_to_first_recording"], 24.0, places=1)

    def test_process_second_recording(self):
        result = process_data.process_recordings(self.users.copy(), self.recs.copy(), recording_index=2)
        self.assertIn("second_recording_id", result.columns)
        self.assertIn("hours_to_second_recording", result.columns)
        self.assertAlmostEqual(result.loc[1, "hours_to_second_recording"], 96.0, places=1)  # Feb 1 → Feb 5

    def test_ordinal(self):
        self.assertEqual(process_data.ordinal(1), "first")
        self.assertEqual(process_data.ordinal(2), "second")
        self.assertEqual(process_data.ordinal(3), "third")

if __name__ == '__main__':
    unittest.main()
