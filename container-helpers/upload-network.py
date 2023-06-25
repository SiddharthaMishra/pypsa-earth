import sys
import os
import json
from google.oauth2.service_account import Credentials
from google.cloud import storage


def main():
    file_path = sys.argv[1]
    file_name = file_path.split("/")[-1]

    networks_blob_folder = sys.argv[2]

    creds = Credentials.from_service_account_info(json.loads(os.environ["GOOGLE_APPLICATION_CREDENTIALS"]))

    # download config from GCS

    project_id = os.environ.get("PROJECT_ID", "crucial-oven-386720")
    storage_client = storage.Client(project=project_id, credentials=creds)
    bucket = storage_client.bucket(os.environ.get("BUCKET_NAME", "payment-dashboard")) 
    
    upload_base = os.environ.get("RUN_FOLDER_NAME", "common")
    bucket.blob(f"{upload_base}/{networks_blob_folder}/{file_name}").upload_from_filename(file_path)

if __name__ == "__main__":
    main()
