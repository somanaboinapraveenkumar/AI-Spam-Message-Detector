import pickle

# ==============================
# 1. Load Saved Model & Vectorizer
# ==============================

model = pickle.load(open("MODEL/spam_model.pkl", "rb"))
vectorizer = pickle.load(open("MODEL/vectorizer.pkl", "rb"))

# ==============================
# 2. Prediction Function
# ==============================

def predict_message(message):
    message_tfidf = vectorizer.transform([message])
    prediction = model.predict(message_tfidf)

    if prediction[0] == 1:
        return "🚨 This message is SPAM"
    else:
        return "✅ This message is NOT SPAM"

# ==============================
# 3. Take User Input
# ==============================

print("=== AI Spam Message Detector ===")
msg = input("Enter your message: ")

result = predict_message(msg)

print("\nPrediction Result:")
print(result)