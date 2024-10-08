from sqlalchemy import create_engine
from app.models import Base, Article
from app.database import DATABASE_URL

def recreate_table():
    engine = create_engine(DATABASE_URL)
    
    # Drop the existing table
    Article.__table__.drop(engine, checkfirst=True)
    
    # Create the table with the updated schema
    Base.metadata.create_all(engine)

    print("Table 'articles' has been recreated with the updated schema.")

if __name__ == "__main__":
    recreate_table()