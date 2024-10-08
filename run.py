from app.main import app as celery_app
from app.tasks import process_feeds

if __name__ == "__main__":
    process_feeds.delay()