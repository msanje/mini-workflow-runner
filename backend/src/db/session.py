import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment")

# Engine: connection pool manager
# echo=True logs SQL to console
# future=True locks you into the modern SQLAlchemy 2.0 API.
engine = create_engine(DATABASE_URL, echo=True, future=True)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True,
)


# Dependency (for FastAPI, optional otherwise)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
