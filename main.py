import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
import argparse
import logging

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

logging.basicConfig(filename='sentiment_analysis.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyse_sentiment(input_filename, output_filename):
    """
    analyse sentiment of input data and output scores to a CSV file.
    
    Args:
        input_filename (str): Path to the input text file.
        output_filename (str): Path to the output CSV file.
    """
    try:
        with open(input_filename, 'r') as input_file, open(output_filename, 'w', newline='') as output_file:
            csv_writer = csv.writer(output_file)
            csv_writer.writerow(['Text', 'Positive', 'Neutral', 'Negative', 'Compound', 'Sentiment Label'])
            
            total_pos = total_neu = total_neg = total_compound = 0
            total_entries = 0

            for line in input_file:
                data = line.strip().strip('"').rstrip(',')  
                if data:
                    sentiment_scores = sia.polarity_scores(data)
                    sentiment_label = get_sentiment_label(sentiment_scores['compound'])
                    
                    csv_writer.writerow([
                        data,
                        format(sentiment_scores['pos'], '.2f'), 
                        format(sentiment_scores['neu'], '.2f'), 
                        format(sentiment_scores['neg'], '.2f'), 
                        format(sentiment_scores['compound'], '.2f'), 
                        sentiment_label
                    ])

                    total_pos += sentiment_scores['pos']
                    total_neu += sentiment_scores['neu']
                    total_neg += sentiment_scores['neg']
                    total_compound += sentiment_scores['compound']
                    total_entries += 1
                else:
                    logging.warning("Skipping empty line in input data.")

            avg_pos = total_pos / total_entries
            avg_neu = total_neu / total_entries
            avg_neg = total_neg / total_entries
            avg_compound = total_compound / total_entries

            csv_writer.writerow(['Aggregated Scores', format(avg_pos, '.3f'), format(avg_neu, '.3f'), format(avg_neg, '.3f'), format(avg_compound, '.3f'), ''])
            
        logging.info("Sentiment scores written to %s", output_filename)
        print("Sentiment scores written to", output_filename)

    except FileNotFoundError:
        logging.error("Input file '%s' not found.", input_filename)
        print("Failed to run. Input file not found.")
    except Exception as e:
        logging.error("An error occurred: %s", e)
        print("Failed to run. An error occurred. Check the log for details.")

def get_sentiment_label(compound_score):
    """
    Determine sentiment label based on compound score.
    
    Args:
        compound_score (float): The compound score.
        
    Returns:
        str: Sentiment label ('Positive', 'Neutral', 'Negative').
    """
    if compound_score >= 0.05:
        return 'Positive'
    elif compound_score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="analyse sentiment of input data and output scores to a CSV file.")
    
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("output_file", help="Path to the output CSV file")

    args = parser.parse_args()
    
    analyse_sentiment(args.input_file, args.output_file)
