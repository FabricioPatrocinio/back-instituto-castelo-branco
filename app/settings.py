from enum import Enum

from pydantic_settings import BaseSettings


class EnviromentEnum(str, Enum):
    PRD = "prd"
    DEV = "dev"
    LOCAL = "local"
    TEST = "test"


class GlobalSettings(BaseSettings):
    SERVICE_NAME: str = "instituto-castelo-branco"
    ENVIROMENT: EnviromentEnum = EnviromentEnum.PRD.value
    S3_BUCKET_NAME: str = "instituto-castelo-branco-images"
    PRESIGNED_URL_EXPIRES_IN: int = 7200
    ENCRYPTION_KEY: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    LOG_LEVEL: str = "INFO"
    RECIPIENT_EMAILS: str


settings = GlobalSettings()
