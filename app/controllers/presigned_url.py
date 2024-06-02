from uuid import uuid4

import boto3
from botocore import client
from schemas import UrlPresignedResponseSchema
from settings import settings


def generate_presigned_url(file_type: str) -> UrlPresignedResponseSchema:
    """
    Generates pre-signed url for uploading files to S3,
    example: Frontend will be used to upload a file directly from the client
    """

    s3 = boto3.client("s3", region_name="us-east-1", config=client.Config(signature_version="s3v4"))

    type_complement = file_type.split("/")[1]
    file_name = f"{uuid4()}.{type_complement}"

    # Generate the URL to get "key-name" from "bucket-name"
    url = s3.generate_presigned_url(
        ClientMethod="put_object",
        Params={
            "Bucket": settings.S3_BUCKET_NAME,
            "Key": file_name,
            "ContentType": file_type,
        },
        ExpiresIn=settings.PRESIGNED_URL_EXPIRES_IN,  # one hour in seconds, increase if needed
    )

    return UrlPresignedResponseSchema(url_presigned=url, file_name=file_name)
