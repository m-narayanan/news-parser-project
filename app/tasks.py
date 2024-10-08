import os
from celery import shared_task
from app.database import SessionLocal
from app.rss_parser import parse_feeds
from app.classifier import classify_article
from app.models import Article
import logging
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

logger = logging.getLogger(__name__)

logger = logging.getLogger(__name__)

@shared_task
def process_feeds():
    logger.info("Starting to process feeds")
    db = SessionLocal()
    try:
        articles = parse_feeds()
        logger.info(f"Parsed {len(articles)} articles")
        new_articles = 0
        for article in articles:
            try:
                existing_article = db.query(Article).filter_by(source_url=article.source_url).first()
                if not existing_article:
                    article.category = classify_article(article)
                    db.add(article)
                    new_articles += 1
                    logger.info(f"Added new article: {article.title} (Category: {article.category})")
                else:
                    logger.debug(f"Skipped duplicate article: {article.title}")
            except Exception as e:
                logger.error(f"Error processing article {article.title}: {str(e)}")
        db.commit()
        logger.info(f"Finished processing feeds. Added {new_articles} new articles.")
    except Exception as e:
        logger.error(f"Error processing feeds: {str(e)}")
        db.rollback()
    finally:
        db.close()

@shared_task
def process_single_article(article_data):
    logger.info(f"Processing single article: {article_data['title']}")
    db = SessionLocal()
    try:
        article = Article(**article_data)
        article.category = classify_article(article)
        db.add(article)
        db.commit()
        logger.info(f"Processed and added article: {article.title}")
    except Exception as e:
        logger.error(f"Error processing article {article_data['title']}: {str(e)}")
        db.rollback()
    finally:
        db.close()