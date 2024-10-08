from app.database import SessionLocal
from app.models import Article
from sqlalchemy import desc

def view_articles():
    db = SessionLocal()
    try:
        articles = db.query(Article).order_by(desc(Article.publication_date)).limit(10).all()
        if not articles:
            print("No articles found in the database.")
        else:
            print(f"Displaying the 10 most recent articles:")
            for article in articles:
                print(f"\nTitle: {article.title}")
                print(f"Category: {article.category}")
                print(f"Publication Date: {article.publication_date}")
                print(f"URL: {article.source_url}")
                print(f"Content Preview: {article.content[:100]}...")  # Display first 100 characters of content
                print("-" * 50)
    finally:
        db.close()

if __name__ == "__main__":
    view_articles()