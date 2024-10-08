import os

class Config:
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/news_db')
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')