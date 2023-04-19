import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Collect data from students (replace this with your own data collection process)
student_data = []

for data in student_data:
    sentiment_scores = sia.polarity_scores(data)
    print("Text: ", data)
    print("Sentiment Scores: ", sentiment_scores)
    print("Sentiment Label: ", max(sentiment_scores, key=sentiment_scores.get))
    print("-----")