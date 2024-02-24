import logging

from aws_lambda_powertools import Logger
from settings import settings

logging.basicConfig()

# Disables all debug logs, this avoids cloudwatch costs
logging.getLogger("pynamodb").setLevel(logging.CRITICAL)
logging.getLogger("boto3").setLevel(logging.CRITICAL)
logging.getLogger("botocore").setLevel(logging.CRITICAL)
logging.getLogger("nose").setLevel(logging.CRITICAL)
logging.getLogger("s3transfer").setLevel(logging.CRITICAL)
logging.getLogger("urllib3").setLevel(logging.CRITICAL)


logger = Logger(service="instituto-castelo-branco", level=settings.LOG_LEVEL)
