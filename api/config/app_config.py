from pydantic import BaseSettings


class AppSettings(BaseSettings):
    ENCRYPTION_KEY: int


app_config = AppSettings()
