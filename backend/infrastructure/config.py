from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

class DBSettings(BaseModel):
    url: str
    echo: bool = True

class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "infrastructure" / "security" / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "infrastructure" / "security" / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    acces_token_expires_minutes = 60

class Settings(BaseSettings):
    db: DBSettings = DBSettings()

    auth_jwt: AuthJWT = AuthJWT()

settings = Settings()