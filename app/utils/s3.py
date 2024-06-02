import boto3
from botocore.exceptions import ClientError
from utils.logger import logger


def delete_image_from_s3(bucket_name: str, image_name: str) -> None:
    s3_client = boto3.client("s3", region_name="us-east-1")

    try:
        s3_client.delete_object(Bucket=bucket_name, Key=image_name)
        logger.info(f"Image '{image_name}' successfully deleted from bucket '{bucket_name}'.")
    except ClientError as e:
        logger.error(f"Error to delete image: {e}")
