import pandas as pd
import spacy


# Load the spaCy model
nlp = spacy.load('en_core_web_sm')

# Load the reviews dataset
dataframe = pd.read_csv('reviews_data.csv')

# Select the 'review.text' column
reviews_data = dataframe['review.text']

# Remove missing values from the 'review.text' column
clean_data = dataframe.dropna(subset=['review.text'])


def predict_sentiment(review):
    # Process the review text using the spaCy model
    doc = nlp(review)
    
    # Calculate the sentiment score
    sentiment_score = sum([token.sentiment for token in doc if not token.is_stop])
    
    # Determine the overall sentiment based on the score
    if sentiment_score >= 0:
        return "Positive"
    else:
        return "Negative"

# Example usage of the predict_sentiment function
review = "This product is amazing!"
sentiment = predict_sentiment(review)
print(sentiment)

sample_reviews = dataframe['review.text'].head()

for review in sample_reviews:
    sentiment = predict_sentiment(review)
    print(f"Review: {review}")
    print(f"Predicted Sentiment: {sentiment}")
    print()

from textblob import TextBlob

# Select two product reviews from the 'reviews.text' column
review1 = data['reviews.text'][0]  # Assuming you want the first review
review2 = data['reviews.text'][1]  # Assuming you want the second review

# Create TextBlob objects for the two reviews
blob1 = TextBlob(review1)
blob2 = TextBlob(review2)

# Calculate the similarity score between the two reviews
similarity_score = blob1.similarity(blob2)

print(f"Similarity Score between the two reviews: {similarity_score}")

# Import TextBlob and load the spaCy model
from textblob import TextBlob
import spacy
nlp = spacy.load('en_core_web_sm')
spacy_text_blob = nlp.add_pipe("spacytextblob")

# Print the results
print(f"Review 1 Polarity: {polarity1}")
print(f"Review 2 Polarity: {polarity2}")
print(f"Review 1 Sentiment: {sentiment1}")
print(f"Review 2 Sentiment: {sentiment2}")
print(f"Similarity Score between Review 1 and Review 2: {similarity_score}")

