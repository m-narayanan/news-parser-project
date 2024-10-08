import feedparser
from app.models import Article
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

RSS_FEEDS = [
    "http://rss.cnn.com/rss/cnn_topstories.rss",
    "http://qz.com/feed",
    "http://feeds.foxnews.com/foxnews/politics",
    "http://feeds.reuters.com/reuters/businessNews",
    "http://feeds.feedburner.com/NewshourWorld",
    "https://feeds.bbci.co.uk/news/world/asia/india/rss.xml"
]

def parse_feeds():
    articles = []
    existing_titles = set()  # To track existing article titles

    for feed_url in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_url)
            logger.info(f"Parsed {len(feed.entries)} entries from {feed_url}")

            for entry in feed.entries:
                title = entry.title
                if title in existing_titles:
                    logger.info(f"Duplicate article found: {title}")
                    continue  # Skip duplicate articles
                
                existing_titles.add(title)  # Add title to the set

                article = Article(
                    title=title,
                    content=entry.get('summary', entry.get('description', '')),
                    publication_date=datetime(*entry.published_parsed[:6]) if hasattr(entry, 'published_parsed') else datetime.now(),
                    source_url=entry.link
                )
                articles.append(article)

            logger.info(f"Successfully parsed {len(feed.entries)} articles from {feed_url}")
        except Exception as e:
            logger.error(f"Error parsing feed {feed_url}: {str(e)}")
    return articles