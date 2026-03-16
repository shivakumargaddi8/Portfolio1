import pandas as pd
import re
import joblib

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Load dataset
df = pd.read_csv("Customer_Sentiment.csv")

df = df[["review_text", "sentiment"]].dropna()

# -------- NLP Cleaning --------
def clean(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

df["clean"] = df["review_text"].apply(clean)

# -------- TF-IDF --------
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(df["clean"])
y = df["sentiment"]

# -------- Train Model --------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model trained successfully!")