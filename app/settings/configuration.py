from environs import Env
from dataclasses import dataclass
from pathlib import Path
from pydantic_settings import BaseSettings

_CONFIG_PATH_DIR = Path(__file__).parent # Путь до папки приложения app

@dataclass
class SettingsDB:
    """Класс для настройки взаимодействия с БД"""
    DB_NAME: str
    DB_USER: str
    DB_PASS: str
    DB_HOST: str
    DB_PORT: int

    @property
    def DATABASE_URL(self):
        # "postgresql://create_group_process:password@localhost/dbname"
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


@dataclass
class HostSettings:
    HOST: str
    PORT: int


# class AuthSettings(BaseSettings):
#     private_key: Path = _CONFIG_PATH_DIR / 'certs' / 'private.pem'
#     public_key: Path = _CONFIG_PATH_DIR / 'certs' / 'public.pem'
#     algorithm: str = 'RS256'
#     access_token_expire_minutes: int = 5

env: Env = Env()
env.read_env() # upload data from .env file


class Settings(BaseSettings):
    """Class settings"""

    # auth: AuthSettings() = AuthSettings()
    db: SettingsDB = SettingsDB(
                    DB_NAME=env('DB_NAME'),
                    DB_USER=env('DB_USER'),
                    DB_PASS=env('DB_PASS'),
                    DB_HOST=env('DB_HOST'),
                    DB_PORT=env('DB_PORT')
                )
    address: HostSettings = HostSettings(
                    HOST=env('HOST'),
                    PORT=int(env('PORT'))
                )

settings = Settings()


__all__ = ['settings']