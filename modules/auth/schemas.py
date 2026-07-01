from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User(BaseModel):
    telegram_id: int
    spotify_id: Optional[str] = None
    access_token: Optional[str] = None
    refresh_token: Optional[str] = None
    expires_at: Optional[datetime] = None
    scopes: str = "user-library-read"

