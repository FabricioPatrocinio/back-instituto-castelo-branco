from pydantic import Field
from pydantic_settings import BaseSettings


class GlobalSettings(BaseSettings):
    SERVICE_NAME: str = Field("instituto-castelo-branco")
    ENVIROMENT: str = Field("local")


settings = GlobalSettings()
