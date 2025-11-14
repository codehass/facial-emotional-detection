from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv
from .config import USER, PASSWORD, HOST, PORT, DATABASE

# First connect to the default "postgres" database
DEFAULT_DB_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/postgres"
default_engine = create_engine(DEFAULT_DB_URL, isolation_level="AUTOCOMMIT")

with default_engine.connect() as conn:
    # Check if the target database exists
    result = conn.execute(
        text("SELECT 1 FROM pg_catalog.pg_database WHERE datname = :db_name"),
        {"db_name": DATABASE},
    )
    if not result.fetchone():
        conn.execute(text(f"CREATE DATABASE {DATABASE}"))
        print(f"Database '{DATABASE}' successfully created.")
    else:
        print(f"Database '{DATABASE}' already exists.")

# Now connect to your actual database
DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependency to get a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
