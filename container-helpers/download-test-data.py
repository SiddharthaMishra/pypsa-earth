import os
import pathlib
import json
from google.oauth2.service_account import Credentials
from google.cloud import storage


def main():
    creds = Credentials.from_service_account_info(json.loads(os.environ["GOOGLE_APPLICATION_CREDENTIALS"]))
    project_id = os.environ.get("PROJECT_ID", "crucial-oven-386720")
    storage_client = storage.Client(project=project_id, credentials=creds)
    bucket = storage_client.bucket(os.environ.get("BUCKET_NAME", "pypsa-test-data"))
    blob_prefix = os.environ.get("TEST_FOLDER_PREFIX", "new_data")
    for folder_name in ["data", "resources", "cutouts"]:
        blobs = bucket.list_blobs(prefix=f"{blob_prefix}/{folder_name}/")  # Get list of files
        print(blobs)
        for blob in blobs:
            filename = blob.name.split("/")[-1]
            blob.download_to_filename(pathlib.Path(".") / folder_name / filename)  # Download
            print(f"downloaded {filename} to {folder_name}")
    bucket.blob(f"{blob_prefix}/config.yaml").download_to_filename("config.yaml")


if __name__ == "__main__":
    main()