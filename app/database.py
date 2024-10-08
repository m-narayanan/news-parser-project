import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from app.models import Base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

print(f"Using DATABASE_URL: {DATABASE_URL}")  # Debug print

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    # Create the database if it doesn't exist
    if not database_exists(engine.url):
        create_database(engine.url)
    
    # Create all tables
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# If you want to test the connection
def test_connection():
    try:
        db = SessionLocal()
        db.execute("SELECT 1")
        print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    test_connection()