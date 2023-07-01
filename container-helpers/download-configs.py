import os
import json
from google.oauth2.service_account import Credentials
from google.cloud import storage

def main():
    creds = Credentials.from_service_account_info(json.loads(os.environ["GOOGLE_APPLICATION_CREDENTIALS"]))

    # download config from GCS

    project_id = os.environ.get("PROJECT_ID", "crucial-oven-386720")
    storage_client = storage.Client(project=project_id, credentials=creds)
    bucket = storage_client.bucket(os.environ.get("BUCKET_NAME", "payment-dashboard"))

    if not os.getenv("IS_TEST_RUN", False):
        bucket.blob(os.environ["RUN_FOLDER_PATH"] + "/configs/config.yaml").download_to_filename("config.yaml")
    bucket.blob(os.environ["RUN_FOLDER_PATH"] + "/configs/bundle_config.yaml").download_to_filename("configs/bundle_config.yaml")
    bucket.blob(os.environ["RUN_FOLDER_PATH"] + "/configs/powerplantmatching_config.yaml").download_to_filename("configs/powerplantmatching_config.yaml")

if __name__ == "__main__":
    main()
