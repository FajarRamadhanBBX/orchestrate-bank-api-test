from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

USERNAME = os.getenv("POSTGRES_USERNAME")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
DB_NAME = os.getenv("POSTGRES_DB")
HOST = os.getenv("POSTGRES_HOST")

DATABASE_URL = f"postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()