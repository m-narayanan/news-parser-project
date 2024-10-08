import csv
import json
from sqlalchemy import create_engine
from app.database import DATABASE_URL
from app.models import Article

def export_to_csv(filename='articles.csv'):
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        query = "SELECT title, content, publication_date, source_url, category FROM articles"
        result = connection.execute(query)
        
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Title', 'Content', 'Publication Date', 'Source URL', 'Category'])  # Header
            for row in result:
                writer.writerow(row)
    print(f"Data exported to {filename}")

def export_to_json(filename='articles.json'):
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        query = "SELECT title, content, publication_date, source_url, category FROM articles"
        result = connection.execute(query)
        
        data = [dict(row) for row in result]
        
        with open(filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, default=str, indent=2)
    print(f"Data exported to {filename}")

def export_sql_dump(filename='articles_dump.sql'):
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        with open(filename, 'w') as dumpfile:
            for table in Article.__table__.metadata.sorted_tables:
                dumpfile.write(f"-- Table: {table.name}\n")
                create_table = str(table.metadata.tables[table.name]).replace('\n', '').replace('    ', ' ')
                dumpfile.write(f"{create_table};\n\n")
                
                for row in connection.execute(table.select()):
                    insert = f"INSERT INTO {table.name} VALUES ({', '.join(repr(value) for value in row)});\n"
                    dumpfile.write(insert)
                dumpfile.write("\n")
    print(f"SQL dump exported to {filename}")

if __name__ == "__main__":
    export_to_csv()
    export_to_json()
    export_sql_dump()