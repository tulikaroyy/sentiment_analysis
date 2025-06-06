# Sentiment Analysis Projects Overview

This repository contains two different sentiment analysis projects, each illustrating unique approaches, dataset sizes, and modeling strategies.

---

## 1. SentimentAnalysis_732rows

A compact, end-to-end project using a real-world social media dataset (~700 rows) to demonstrate the full data science workflow:

**Key Steps:**
- Data ingestion, extensive cleaning, and standardization of sentiment labels (mapped to Positive, Negative, Neutral)
- Text preprocessing: Lowercasing, punctuation/URL/user/tag removal, stopword removal, stemming
- Feature engineering: One-hot encoding, TF-IDF vectorization (top 5000 features)
- Visualization: Matplotlib-based plots for sentiment/platform/country breakdowns
- Modeling: Logistic Regression with class balancing
- Evaluation: Train/test split, classification report
- Model persistence: Pickle for model and vectorizer
- Demo: Code block for quick predictions on new samples

**Strengths:**
- Comprehensive demonstration of the end-to-end ML pipeline
- Emphasis on data cleaning and feature engineering
- Modular and easy to extend

**Weaknesses:**
- Small dataset; limited generalization and accuracy
- Class imbalance remains a challenge
- Basic model—serves as a learning scaffold, not a production tool

---

## 2. SentimentAnalysis_50000rows

A large-scale comparison of sentiment analysis approaches using 50,000 IMDB movie reviews. This project contrasts traditional machine learning with modern transformer-based NLP.

### Approaches Compared

#### Traditional ML Model (TF-IDF + Logistic Regression)
- **Preprocessing:** Extensive (stopwords, lemmatization, explicit negation handling)
- **Vectorization:** TF-IDF
- **Model:** Logistic Regression

**Strengths:**
- Transparent, interpretable results
- Works well for structured/formal review data

**Weaknesses:**
- Struggles with subtle context, sarcasm, and negation unless preprocessing is perfect
- Performance tied closely to handcrafted features

#### BERT (Transformer-based Model)
- **BERT on Dataset:** Minimal preprocessing, trained/evaluated on labeled IMDB data
- **Pre-trained BERT:** Used Hugging Face's pre-trained pipeline (`distilbert-base-uncased-finetuned-sst-2-english`), requiring no further training

**Strengths:**
- Superior context understanding (handles sarcasm, nuance)
- Excellent out-of-the-box accuracy, even on new domains
- Flexible, not restricted to movie reviews

**Weaknesses:**
- Heavier computational requirements
- Slower inference times

**Final Deployment:**  
The pre-trained BERT model was selected for deployment due to its accuracy, robustness, and domain independence.

---

## Summary

- **732-row project:** Focuses on data preparation and classic machine learning for small datasets—ideal for learning the pipeline.
- **50,000-row project:** Demonstrates the leap in performance, versatility, and context understanding provided by transformer-based models like BERT—especially valuable for large, real-world datasets.

Each project offers its own learning takeaways, from pipeline design and feature engineering to modern NLP deployment!
