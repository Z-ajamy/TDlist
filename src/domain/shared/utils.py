from uuid import uuid4
from datetime import datetime, timezone

def create_uuid4() -> str:
    return uuid4().hex


def crete_utctime() -> datetime:
    return datetime.now(timezone.utc)

