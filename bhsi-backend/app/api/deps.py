from typing import Generator
from app.db.session import SessionLocal

def get_db() -> Generator:
    """
    Get database session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 