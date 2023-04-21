import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

# Collect data from students (replace this with your own data collection process)
student_data = [
    "I always use strong and unique passwords for my online accounts.",
    "I avoid sharing personal information online without proper verification.",
    "I keep my antivirus software updated on all my devices.",
    "I am cautious while clicking on links or downloading attachments from unknown sources.",
    "I know how to recognize and report phishing attempts.",
    "I understand the importance of regularly backing up my data.",
    "I use two-factor authentication for my online accounts.",
    "I am aware of the risks of posting personal information on social media.",
    "I am careful about the information I share in online forums and discussion boards.",
    "I do not share my passwords with anyone, including my friends or family."
]

for data in student_data:
    sentiment_scores = sia.polarity_scores(data)
    print("Text: ", data)
    print("Sentiment Scores: ", sentiment_scores)
    print("Sentiment Label: ", max(sentiment_scores, key=sentiment_scores.get))
    print("-----")
