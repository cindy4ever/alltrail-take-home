import unittest
from unittest.mock import patch, MagicMock
import os

from scripts.download_data import download_file

class TestDownloadData(unittest.TestCase):

    @patch("scripts.download_data.gdown.download")
    def test_download_file_success(self, mock_gdown_download):
        # Arrange
        mock_gdown_download.return_value = True
        filename = "test_file.tsv"
        file_id = "dummy_file_id"
        dest_folder = "test_data"

        # Act
        download_file(filename, file_id, dest_folder)

        # Assert
        mock_gdown_download.assert_called_once_with(
            f"https://drive.google.com/uc?id={file_id}",
            os.path.join(dest_folder, filename),
            quiet=False
        )
        self.assertTrue(os.path.exists(dest_folder))

        # Clean up
        if os.path.exists(dest_folder):
            os.rmdir(dest_folder)

    @patch("scripts.download_data.gdown.download", return_value=False)
    def test_download_file_failure(self, mock_gdown_download):
        filename = "fail.tsv"
        file_id = "invalid"
        dest_folder = "test_data_fail"

        download_file(filename, file_id, dest_folder)

        mock_gdown_download.assert_called_once()

        if os.path.exists(dest_folder):
            os.rmdir(dest_folder)

if __name__ == "__main__":
    unittest.main()