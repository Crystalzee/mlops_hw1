from minio import Minio
from minio.error import S3Error
import os

MINIO_URL = os.getenv("MINIO_URL", "localhost:9000")
MINIO_USER = os.getenv("MINIO_USER", "minioadmin")
MINIO_PASS = os.getenv("MINIO_PASS", "minioadmin")
BUCKET_NAME = "mlops-bucket"

client = Minio(
    MINIO_URL,
    access_key=MINIO_USER,
    secret_key=MINIO_PASS,
    secure=False
)

def ensure_bucket_exists():
    if not client.bucket_exists(BUCKET_NAME):
        client.make_bucket(BUCKET_NAME)
        print(f" Created bucket: {BUCKET_NAME}")
    else:
        print(f" Bucket {BUCKET_NAME} already exists")

def upload_file(local_path: str, object_name: str):
    ensure_bucket_exists()
    client.fput_object(BUCKET_NAME, object_name, local_path)
    print(f" Uploaded {local_path} → {BUCKET_NAME}/{object_name}")

def download_file(object_name: str, local_path: str):
    ensure_bucket_exists()
    client.fget_object(BUCKET_NAME, object_name, local_path)
    print(f"Downloaded {object_name} → {local_path}")
