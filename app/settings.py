from enum import Enum

from pydantic import Field
from pydantic_settings import BaseSettings


class EnviromentEnum(str, Enum):
    PRD = "prd"
    DEV = "dev"
    LOCAL = "local"
    TEST = "test"


class GlobalSettings(BaseSettings):
    SERVICE_NAME: str = Field("instituto-castelo-branco")
    ENVIROMENT: EnviromentEnum = Field("local")
    S3_BUCKET_NAME: str = Field("instituto-castelo-branco")
    PRESIGNED_URL_EXPIRES_IN: int = Field(3600)
    ENCRYPTION_KEY: str


settings = GlobalSettings()
