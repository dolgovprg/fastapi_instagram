from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Настройки приложения "postgresql://postgres:postgres@localhost/postgres"
    """

    SQLALCHEMY_DATABASE_URL: str = "postgresql://postgres:postgres@localhost/instagram"

    MAIN_URL: str = "/"

settings = Settings()
