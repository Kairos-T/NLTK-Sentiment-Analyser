import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
import argparse

# Download the VADER lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Create a SentimentIntensityAnalyzer instance
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(input_filename, output_filename):
    try:
        # Read data from the input file
        with open(input_filename, 'r') as input_file:
            student_data = input_file.readlines()

        # Analyze sentiment and write scores to a CSV file
        with open(output_filename, 'w', newline='') as output_file:
            csv_writer = csv.writer(output_file)
            # Write header row to the CSV file
            csv_writer.writerow(['Text', 'Positive', 'Neutral', 'Negative', 'Compound', 'Sentiment Label'])
            
            # Initialize variables for aggregating sentiment scores
            total_pos = total_neu = total_neg = total_compound = 0
            total_entries = 0

            for data in student_data:
                data = data.strip().strip('"').rstrip(',')  # Remove leading/trailing whitespace and quotes
                if data:
                    sentiment_scores = sia.polarity_scores(data)
                    sentiment_label = max(sentiment_scores, key=sentiment_scores.get)
                    
                    # Write sentiment scores and label to the CSV file
                    csv_writer.writerow([
                        data,
                        format(sentiment_scores['pos'], '.2f'), 
                        format(sentiment_scores['neu'], '.2f'), 
                        format(sentiment_scores['neg'], '.2f'), 
                        format(sentiment_scores['compound'], '.2f'), 
                        sentiment_label
                    ])

                    # Aggregate sentiment scores
                    total_pos += sentiment_scores['pos']
                    total_neu += sentiment_scores['neu']
                    total_neg += sentiment_scores['neg']
                    total_compound += sentiment_scores['compound']
                    total_entries += 1
                else:
                    print("Skipping empty line in input data.")

            # Calculate average sentiment scores
            avg_pos = total_pos / total_entries
            avg_neu = total_neu / total_entries
            avg_neg = total_neg / total_entries
            avg_compound = total_compound / total_entries

            # Write aggregated sentiment scores to the CSV file
            csv_writer.writerow(['Aggregated Scores', format(avg_pos, '.3f'), format(avg_neu, '.3f'), format(avg_neg, '.3f'), format(avg_compound, '.3f'), ''])
            
        print("Sentiment scores written to", output_filename)

    except FileNotFoundError:
        print("Error: Input file '{}' not found.".format(input_filename))
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Create an argument parser with a description for the help message
    parser = argparse.ArgumentParser(description="Analyze sentiment of input data and output scores to a CSV file.")
    
    # Add positional arguments for input and output files
    parser.add_argument("input_file", help="Path to the input text file")
    parser.add_argument("output_file", help="Path to the output CSV file")

    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Call the sentiment analysis function with the provided arguments
    analyze_sentiment(args.input_file, args.output_file)
