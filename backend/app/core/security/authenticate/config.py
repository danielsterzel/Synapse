from pathlib import Path
from backend.app.core.settings import settings

ALGORITHM = "RS256"

PRIVATE_KEY = Path(settings.jwt_private_key).read_text()
PUBLIC_KEY = Path(settings.jwt_public_key).read_text()

ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes
REFRESH_TOKEN_EXPIRE_DAYS = settings.refresh_token_expire_days
