import pandas as pd
import spacy
from textblob import TextBlob  # Import TextBlob for sentiment analysis

# Load a model with word vectors (e.g., en_core_web_lg)
nlp = spacy.load('en_core_web_lg')

# Load the reviews dataset
df = pd.read_csv('amazon_product_reviews.csv')

df.shape

# Select the 'reviews.text' column
reviews_data = df['reviews.text']

# Remove missing values from the 'reviews.text' column
clean_data = df.dropna(subset=['reviews.text'])

def predict_sentiment(review):
    """
    Predicts the sentiment of a product review using TextBlob.

    Args:
        review (str): The input product review.

    Returns:
        str: "Positive" or "Negative" sentiment.
    """
    blob = TextBlob(review)
    sentiment_score = blob.sentiment.polarity
    return "Positive" if sentiment_score >= 0 else "Negative"

def calculate_similarity(review1, review2):
    """
    Calculates the similarity score between two product reviews using spaCy.

    Args:
        review1 (str): First product review.
        review2 (str): Second product review.

    Returns:
        float: Similarity score (between 0 and 1).
    """
    doc1 = nlp(review1)
    doc2 = nlp(review2)
    return doc1.similarity(doc2)

# Example usage
review = "This product is amazing!"
sentiment = predict_sentiment(review)
print(f"Predicted Sentiment: {sentiment}")

# Select product reviews from the 'reviews.text' column
review1 = df['reviews.text'][0]
review2 = df['reviews.text'][1]

# Calculate similarity score
similarity_score = calculate_similarity(review1, review2)
print(f"Similarity Score between the two reviews: {similarity_score:.2f}")
