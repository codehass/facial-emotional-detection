from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

USER = os.getenv("USER_DB")
PASSWORD = os.getenv("PASSWORD")
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
DATABASE = os.getenv("DATABASE")


print(USER)

DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    result = conn.execute(
        text("SELECT 1 FROM pg_catalog.pg_database WHERE datname = :db_name"),
        {"db_name": DATABASE},
    )
    if not result.fetchone():
        conn.execute(text(f"CREATE DATABASE {DATABASE}"))
        print(f" Database {DATABASE} was successful created!")
    else:
        print(f"Database {DATABASE} wsa created.")


Base = declarative_base()

SessionLocal = SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

db = SessionLocal()


def get_db():
    """Dependency to get database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
