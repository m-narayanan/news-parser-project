import psycopg2
from app.database import DATABASE_URL

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"An error occurred: {e}")