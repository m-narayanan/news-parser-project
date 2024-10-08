# News Article Collection and Categorization

This application collects news articles from various RSS feeds, stores them in a database, and categorizes them into predefined categories.

## Features

- Collects articles from multiple RSS feeds
- Stores articles in a PostgreSQL database
- Categorizes articles using Natural Language Processing
- Provides asynchronous processing using Celery
- Exports data in CSV, JSON, and SQL dump formats

## Technology Stack

- Python 3.8+
- PostgreSQL
- Celery with Redis as message broker
- SQLAlchemy for ORM
- Feedparser for RSS parsing
- NLTK for text classification

## Setup and Installation

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Set up PostgreSQL database and update `DATABASE_URL` in `app/database.py`
4. Set up Redis and update Celery configuration if necessary
5. Run database migrations: `alembic upgrade head`

## Usage

1. Start Celery worker: `celery -A celery_config worker --loglevel=info`
2. Start Celery beat: `celery -A celery_config beat --loglevel=info`
3. Run the main application: `python run.py`

## Data Export

To export the collected data:

```python
from app.data_export import export_to_csv, export_to_json, export_sql_dump

export_to_csv()  # Exports to articles.csv
export_to_json()  # Exports to articles.json
export_sql_dump()  # Exports to articles_dump.sql
```

## Design Choices

- **SQLAlchemy ORM**: Chosen for its flexibility and powerful querying capabilities.
- **Celery**: Used for asynchronous processing, allowing scalable handling of RSS feeds.
- **NLTK**: Employed for text classification due to its robust natural language processing capabilities.
- **Feedparser**: Selected for its simplicity and effectiveness in parsing RSS feeds.

## Future Improvements

- Implement more advanced NLP techniques for better categorization
- Add a web interface for real-time monitoring of collected articles
- Implement unit and integration tests for better code reliability