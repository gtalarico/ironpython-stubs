import os
from google.cloud import storage
_environ = dict(os.environ)  # or os.environ.copy()
import sys



def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )


def list_blobs(bucket_name):
    """Lists all the blobs in the bucket."""
    # bucket_name = "your-bucket-name"

    storage_client = storage.Client()

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)

    return blobs


def delete_blob(bucket_name, blob_name):
    """Deletes a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # blob_name = "your-object-name"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.delete()

    print("Blob {} deleted.".format(blob_name))


def upload_stub(name):
    try:
        bucket = 'pylint.app.boxwise.nl'
        print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.expanduser("~/Desktop/googleCloudCredentials.json")
        print(os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
        bloblist = list_blobs(bucket)
        for blob in bloblist:
            print blob.name
            if blob.name == name:
                delete_blob(bucket,name)
        filepath = os.path.expanduser("~\\Desktop\\vertaling_guide.txt")
        upload_blob(bucket,filepath,name)
    finally:
        os.environ.clear()
        os.environ.update(_environ)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        upload_stub(sys.argv[1])

