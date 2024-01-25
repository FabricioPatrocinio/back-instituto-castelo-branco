from pydantic import Field
from pydantic_settings import BaseSettings


class GlobalSettings(BaseSettings):
    SERVICE_NAME: str = Field("instituto-castelo-branco")
    ENVIROMENT: str = Field("local")
    S3_BUCKET_NAME: str = Field("instituto-castelo-branco")
    PRESIGNED_URL_EXPIRES_IN: int = Field(3600)


settings = GlobalSettings()
