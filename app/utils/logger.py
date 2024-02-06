from aws_lambda_powertools import Logger
from settings import settings

logger = Logger(service="nomeDoServico", level=settings.LOG_LEVEL)
