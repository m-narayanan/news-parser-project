from app.rss_parser import parse_feeds
from app.classifier import classify_article
from app.database import SessionLocal
from app.models import Article

def debug_feed_parsing():
    print("Starting debug of feed parsing...")
    articles = parse_feeds()
    print(f"Number of articles parsed: {len(articles)}")
    
    if articles:
        print("\nFirst article details:")
        first_article = articles[0]
        print(f"Title: {first_article.title}")
        print(f"URL: {first_article.source_url}")
        print(f"Publication Date: {first_article.publication_date}")
        print(f"Content preview: {first_article.content[:100]}...")
        
        category = classify_article(first_article)
        print(f"Classified category: {category}")
        
        db = SessionLocal()
        try:
            db.add(first_article)
            db.commit()
            print("\nArticle successfully added to database.")
        except Exception as e:
            print(f"\nError adding article to database: {str(e)}")
            db.rollback()
        finally:
            db.close()
    else:
        print("No articles were parsed from the feeds.")

if __name__ == "__main__":
    debug_feed_parsing()