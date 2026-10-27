# src/infrastructure/database/session.py
import os
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker

def create_db_engine():
    try:
        db_url = URL.create(
            drivername=os.getenv("DB_DRIVER", "mysql+mysqldb"), # fallback default
            username=os.environ["DB_USER"],         # Raises KeyError if missing
            password=os.environ["DB_PASSWORD"],     # Raises KeyError if missing
            host=os.environ["DB_HOST"],             # Raises KeyError if missing
            port=int(os.environ["DB_PORT"]),        # Fails fast if not an integer
            database=os.environ["DB_NAME"],         # Raises KeyError if missing
        )
    except KeyError as e:
        raise ValueError(f"Missing critical database environment variable: {e}")
    except ValueError:
        raise ValueError("DB_PORT environment variable must be an integer.")

    engine = create_engine(
        db_url,
        pool_pre_ping=True,
        pool_size=10,
        max_overflow=20
    )
    return engine


def get_session_maker(engine) -> sessionmaker:
    return sessionmaker(bind=engine, expire_on_commit=False)
