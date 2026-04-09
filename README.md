from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import numpy as np
import re
import joblib
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score

app = Flask(__name__)
CORS(app)

# =========================
# LOAD MODEL
# =========================
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# =========================
# STOPWORDS
# =========================
STOPWORDS = set("""
a about above after again against all am an and any are arent as at be because been before
being below between both but by cant cannot could couldnt did didnt do does doesnt doing dont
down during each few for from further get got had hadnt has hasnt have havent having he her
here hers herself him himself his how i if in into is isnt it its itself just let me more most
mustnt my myself no nor not of off on once only or other ought our ours ourselves out over own
same she should shouldnt so some such than that the their theirs them themselves then there
these they this those through to too under until up very was wasnt we were werent what when
where which while who whom why will with wont would wouldnt you your yours yourself yourselves
""".split())

# =========================
# CLEAN TEXT
# =========================
def clean(text):
    text = str(text).lower()
    text = text.replace("not good", "bad")
    text = text.replace("not great", "bad")
    text = text.replace("not happy", "bad")

    text = re.sub(r'[^a-z\s]', '', text)
    return text

# =========================
# TOP WORDS
# =========================
def top_words(text_list, n=5):
    all_words = []
    for text in text_list:
        words = clean(text).split()
        all_words.extend([w for w in words if w not in STOPWORDS and len(w) > 2])
    common = Counter(all_words).most_common(n)
    return [w[0] for w in common]

# =========================
# DYNAMIC COLUMN DETECTION (NO ASSUMPTION)
# =========================
def detect_columns(df):

    text_col = None
    score_col = None

    for col in df.columns:

        # try numeric
        numeric_series = pd.to_numeric(df[col], errors='coerce')

        # if mostly numeric → score
        if numeric_series.notna().sum() > 0.7 * len(df):
            score_col = col

        # if text column
        elif df[col].dtype == object:
            avg_len = df[col].dropna().astype(str).str.len().mean()
            if avg_len and avg_len > 5:
                text_col = col

    return text_col, score_col

# =========================
# SCORE → SENTIMENT
# =========================
def sentiment_from_score(val):

    try:
        val = float(val)
    except:
        return None

    # Standard mapping (works for most datasets)
    if val >= 4:
        return "positive"
    elif val <= 2:
        return "negative"
    else:
        return "neutral"

# =========================
# METRICS
# =========================
def compute_metrics(texts, labels):

    if len(set(labels)) < 2 or len(labels) < 10:
        return {
            "logistic_accuracy": 0,
            "logistic_f1": 0,
            "svm_accuracy": 0,
            "svm_f1": 0,
            "rf_accuracy": 0,
            "rf_f1": 0,
        }

    try:
        cleaned = [clean(t) for t in texts]
        tfidf = TfidfVectorizer(stop_words="english")
        X = tfidf.fit_transform(cleaned)
        y = np.array(labels)

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        results = {}

        lr = LogisticRegression(max_iter=1000)
        lr.fit(X_train, y_train)
        pred = lr.predict(X_test)
        results["logistic_accuracy"] = round(accuracy_score(y_test, pred)*100,2)
        results["logistic_f1"] = round(f1_score(y_test, pred, average="weighted"),4)

        svm = LinearSVC()
        svm.fit(X_train, y_train)
        pred = svm.predict(X_test)
        results["svm_accuracy"] = round(accuracy_score(y_test, pred)*100,2)
        results["svm_f1"] = round(f1_score(y_test, pred, average="weighted"),4)

        rf = RandomForestClassifier()
        rf.fit(X_train, y_train)
        pred = rf.predict(X_test)
        results["rf_accuracy"] = round(accuracy_score(y_test, pred)*100,2)
        results["rf_f1"] = round(f1_score(y_test, pred, average="weighted"),4)

        return results

    except:
        return {
            "logistic_accuracy": 0,
            "logistic_f1": 0,
            "svm_accuracy": 0,
            "svm_f1": 0,
            "rf_accuracy": 0,
            "rf_f1": 0,
        }

# =========================
# CSV UPLOAD
# =========================
@app.route("/upload", methods=["POST"])
def upload():

    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        df = pd.read_csv(file, encoding="latin1")

        df.columns = df.columns.str.strip()
        df = df.dropna(how="all")

        print("Columns:", df.columns)

        if df.empty:
            return jsonify({"error": "Empty CSV"}), 400

        text_col, score_col = detect_columns(df)

        print("Detected TEXT:", text_col)
        print("Detected SCORE:", score_col)

        pos = neg = neu = 0
        pos_list, neg_list, neu_list = [], [], []
        all_texts, all_labels = [], []

        for _, row in df.iterrows():

            text = str(row[text_col]) if text_col else ""
            score = None

            if score_col:
                try:
                    score = float(row[score_col])
                except:
                    score = None

            # PRIORITY: SCORE
            if score is not None:
                sentiment = sentiment_from_score(score)

            # FALLBACK: ML
            else:
                clean_text = clean(text)
                vec = vectorizer.transform([clean_text])
                sentiment = model.predict(vec)[0]

            if sentiment == "positive":
                pos += 1
                pos_list.append(text)

            elif sentiment == "negative":
                neg += 1
                neg_list.append(text)

            else:
                neu += 1
                neu_list.append(text)

            all_texts.append(text)
            all_labels.append(sentiment)

        total = pos + neg + neu

        print("RESULT:", pos, neg, neu)

        if total == 0:
            return jsonify({"error": "No valid data"}), 400

        pos_words = top_words(pos_list)
        neg_words = top_words(neg_list)
        neu_words = top_words(neu_list)

        metrics = compute_metrics(all_texts, all_labels)

        return jsonify({
            "positive": pos,
            "negative": neg,
            "neutral": neu,
            "positive_words": pos_words,
            "negative_words": neg_words,
            "neutral_words": neu_words,
            **metrics
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# RUN
# =========================
if __name__ == "__main__":
    app.run(debug=True)
