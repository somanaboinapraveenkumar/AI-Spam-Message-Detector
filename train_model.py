import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# ==============================
# 1. Load Dataset (TAB separated file)
# ==============================

df = pd.read_csv("DATASET/spam.csv", 
                 sep='\t', 
                 header=None, 
                 names=['label', 'message'], 
                 encoding='latin-1')

# ==============================
# 2. Convert Labels to Numbers
# ham = 0, spam = 1
# ==============================

df['label'] = df['label'].map({'ham': 0, 'spam': 1})

# ==============================
# 3. Split Data
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    df['message'],
    df['label'],
    test_size=0.2,
    random_state=42
)

# ==============================
# 4. Convert Text to Numbers (TF-IDF)
# ==============================

vectorizer = TfidfVectorizer(stop_words='english')

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# ==============================
# 5. Train Model (Naive Bayes)
# ==============================

model = MultinomialNB()
model.fit(X_train_tfidf, y_train)

# ==============================
# 6. Check Accuracy
# ==============================

y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy * 100, 2), "%")

# ==============================
# 7. Save Model & Vectorizer
# ==============================

pickle.dump(model, open("MODEL/spam_model.pkl", "wb"))
pickle.dump(vectorizer, open("MODEL/vectorizer.pkl", "wb"))

print("Model and Vectorizer saved successfully!")