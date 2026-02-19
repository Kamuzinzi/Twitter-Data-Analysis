# Twitter Data Analysis

A Python project for extracting, cleaning, and analyzing Twitter/X tweet data. Includes data extraction from JSON, text cleaning, sentiment analysis, and exploratory analysis via Jupyter notebooks.

## Features

- **Data extraction** – Parse Twitter JSON data into structured pandas DataFrames
- **Data cleaning** – Remove duplicates, filter by date/language, convert types
- **Sentiment analysis** – Polarity and subjectivity via TextBlob
- **EDA & modeling** – Jupyter notebooks for exploratory analysis and topic modeling

## Project Structure

```
Twitter-Data-Analysis/
├── extract_dataframe.py      # JSON → DataFrame extraction
├── clean_tweets_dataframe.py # Tweet cleaning pipeline
├── sample/                   # Sample tweet data for testing
├── tests/                    # Unit tests
├── EDA_Twitter.ipynb         # Exploratory data analysis
├── Modeling_Twitter.ipynb    # Topic modeling & sentiment
└── requirements.txt
```

## Setup

```bash
git clone git@github.com:Kamuzinzi/Twitter-Data-Analysis.git
cd Twitter-Data-Analysis
pip install -r requirements.txt
```

## Usage

**Extract tweets from JSON:**
```bash
python extract_dataframe.py sample/sampletweets.json
```

**Run tests:**
```bash
pytest tests/ -v
```

## Data

Place your tweet JSON data in the `data/` directory (not tracked by git). Sample data is provided in `sample/sampletweets.json` for testing.

## CI

GitHub Actions runs tests on every push to `main`. All tests must pass before merging.

## License

See [LICENSE](LICENSE).
