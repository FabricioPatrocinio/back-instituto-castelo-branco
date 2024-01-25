from uuid import uuid4

import boto3
from botocore import client
from settings import settings


def generate_presigned_url():
    """
    Generates pre-signed url for uploading files to S3,
    example: Frontend will be used to upload a file directly from the client
    """

    s3 = boto3.client("s3", config=client.Config(signature_version="s3v4"))

    # Generate the URL to get "key-name" from "bucket-name"
    url = s3.generate_presigned_url(
        ClientMethod="get_object",
        Params={"Bucket": settings.S3_BUCKET_NAME, "Key": str(uuid4())},
        ExpiresIn=settings.PRESIGNED_URL_EXPIRES_IN,  # one hour in seconds, increase if needed
    )

    return {"urlPresigned": url}
