# Kindle Review Sentiment Analysis using TF-IDF and NLP

This project is a Flask web application that predicts the sentiment (positive or negative) of Kindle book reviews using Natural Language Processing (NLP) techniques. It leverages TF-IDF vectorization and a Naive Bayes classifier for accurate sentiment classification.

## Features & Benefits

- **TF-IDF Vectorization:** Converts review text into meaningful numerical features.
- **NLP Preprocessing:** Includes lowercasing, stopword removal, special character cleaning, and lemmatization.
- **Simple Web Interface:** Enter a review and instantly get a sentiment prediction.
- **Educational:** Demonstrates end-to-end NLP workflow, from data cleaning to deployment.
- **Reusable:** Easily adapt for other text classification tasks.

## Project Structure

```
kindle-review-sentiment-tfidf-nlp/
│
├── app.py                  # Flask web app
├── all_kindle_review.csv   # Dataset of Kindle reviews
├── tfidf_vectorizer.pkl    # Saved TF-IDF vectorizer
├── nb_model_tfidf.pkl      # Saved Naive Bayes model
├── templates/
│   └── index.html          # Web interface template
├── Kindle_Review_Sentiment_Analysis_TF_IDF.ipynb  # Jupyter notebook for training
└── README.md
```

## How it Works

1. **Preprocessing:** Cleans and lemmatizes review text.
2. **TF-IDF:** Transforms text into feature vectors.
3. **Model:** Naive Bayes classifier predicts sentiment.
4. **Web App:** User submits a review and receives a prediction.

## Example Reviews

**Positive Review:**  
> I absolutely loved this book! The story was engaging and the characters were well developed.

**Negative Review:**  
> This was a waste of time. The plot was boring and I didn’t enjoy it at all.

## Getting Started

1. Clone the repo and install requirements (`pip install flask scikit-learn nltk pandas`).
2. Train the model using the notebook or use the provided pickle files.
3. Run `python app.py` and open your browser to `http://127.0.0.1:5000/`.
4. Enter a Kindle review to see the sentiment prediction.

## More Information

- **TF-IDF (Term Frequency-Inverse Document Frequency):** Highlights important words in reviews by balancing frequency and uniqueness.
- **NLP Pipeline:** Shows practical steps for real-world text analysis.
- **Deployment:** Demonstrates how to serve ML models with Flask.

---

*Feel free to fork, contribute, or use this project as a learning resource for NLP and sentiment analysis!*
