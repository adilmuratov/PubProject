from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class DBSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    echo: bool = True


class AuthJWT(BaseModel):
    private_key_path: Path = (
        BASE_DIR / "infrastructure" / "security" / "certs" / "jwt-private.pem"
    )
    public_key_path: Path = (
        BASE_DIR / "infrastructure" / "security" / "certs" / "jwt-public.pem"
    )
    algorithm: str = "RS256"
    acces_token_expires_minutes: int = 30


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
    )

    db: DBSettings = DBSettings()
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()