from app.database import init_db
from app.tasks import process_feeds
from app.logging_config import setup_logging
import logging
from celery import Celery
from celery.schedules import crontab

setup_logging()
logger = logging.getLogger(__name__)

app = Celery('news_pro')
app.config_from_object('celeryconfig')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute='*/30'),  # Run every 30 minutes
        process_feeds.s(),
        name='process feeds every 30 minutes'
    )

if __name__ == '__main__':
    try:
        init_db()
        logger.info("Database initialized successfully")
        app.start()
    except Exception as e:
        logger.error(f"Error starting the application: {str(e)}")