# Sentiment Analysis Script

This is a Python script that analyses sentiment in text data using the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool from the NLTK library.

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)

## Description

The script reads input data from a text file, analyses the sentiment of each text using VADER sentiment analysis, and outputs the sentiment scores and labels to a CSV file.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/Kairos-T/NLTK-Sentiment-Analyser/tree/main
cd NLTK-Sentiment-Analyser
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script with the following command:

```bash
python main.py input_data.txt sentiment_scores.csv
```
Replace `input_data.txt` with the name of the input data file, and `sentiment_scores.csv` with the desired name of the output CSV file.

## Output
The script will generate a CSV file containing the sentiment analysis results for each input text. The CSV file will have the following columns:

- Text: The input text.
- Positive: The positive sentiment score.
- Neutral: The neutral sentiment score.
- Negative: The negative sentiment score.
- Compound: The compound sentiment score.
- Sentiment Label: The label indicating the overall sentiment.