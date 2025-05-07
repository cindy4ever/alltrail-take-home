import os
import gdown

FILES = {
    "users_2017.tsv": "1n2uxbcRuatO0c6I8Ky7K5laxNEOvWs4V",
    "recordings_2017.tsv": "1iCXVvKxHpVWOEI2xPFmOAsu8piuXM2lA"
}

def download_file(filename, file_id, dest_folder="data"):
    os.makedirs(dest_folder, exist_ok=True)
    output_path = os.path.join(dest_folder, filename)
    url = f"https://drive.google.com/uc?id={file_id}"
    gdown.download(url, output_path, quiet=False)
    print(f"Downloaded: {output_path}")

def main():
    for filename, file_id in FILES.items():
        download_file(filename, file_id)

if __name__ == "__main__":
    main()