import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Initialize lemmatizer and stop words
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

# Define keywords for each category
category_keywords = {
    "Terrorism / protest / political unrest / riot": ["terrorism", "terrorist", "protest", "riot", "unrest", "violence", "attack", "bomb", "shooting", "political", "conflict"],
    "Positive/Uplifting": ["success", "achievement", "breakthrough", "hope", "inspire", "positive", "progress", "victory", "overcome", "triumph", "celebrate"],
    "Natural Disasters": ["earthquake", "hurricane", "tornado", "flood", "tsunami", "wildfire", "landslide", "drought", "storm", "disaster", "catastrophe"],
}

def preprocess_text(text):
    # Tokenize and lemmatize the text
    tokens = word_tokenize(text.lower())
    return [lemmatizer.lemmatize(token) for token in tokens if token.isalnum() and token not in stop_words]

def classify_article(article):
    # Combine title and content for classification
    full_text = f"{article.title} {article.content}"
    preprocessed_text = preprocess_text(full_text)
    
    # Count keyword matches for each category
    category_scores = {category: sum(1 for word in preprocessed_text if word in keywords)
                       for category, keywords in category_keywords.items()}
    
    # Find the category with the highest score
    best_category = max(category_scores, key=category_scores.get)
    
    # If no keywords matched, classify as "Others"
    return best_category if category_scores[best_category] > 0 else "Others"