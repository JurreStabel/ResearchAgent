import os
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\jurre\Downloads\sylvan-cirrus-450700-i5-2b12eaf5b5b5.json"

client = storage.Client()

bucket = client.bucket("main-bucket-researchagent")

local_file_path = r"C:\Users\jurre\OneDrive\Documenten\ResearchAgent\papers\paper.pdf"
blob = bucket.blob('papers/paper.pdf')

blob.upload_from_filename(local_file_path)
print(f"File {local_file_path} uploaded to gs://{bucket}/{blob}")


