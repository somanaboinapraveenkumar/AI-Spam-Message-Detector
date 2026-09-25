#  AI Spam Message Detector

An AI-powered Spam Message Detection System built using Python and Machine Learning.  
This project classifies SMS messages as **Spam** or **Not Spam** using Natural Language Processing (NLP) techniques and the Multinomial Naive Bayes algorithm.

---

##  Table of Contents

- Project Overview
- Features
- Demo
- Technologies Used
- Machine Learning Workflow
- Model Performance
- Project Structure
- Installation & Setup
- How It Works
- Future Improvements
- Author

---

##  Project Overview

Spam messages are a common problem in digital communication systems.  
This project implements a machine learning-based classification model that analyzes text messages and predicts whether they are spam or legitimate (ham).

The model uses:

- TF-IDF Vectorization for text feature extraction
- Multinomial Naive Bayes for classification
- Tkinter for GUI interface

---

##  Features

✔ 97.85% Model Accuracy  
✔ Machine Learning-based classification  
✔ Natural Language Processing (TF-IDF)  
✔ Command Line Interface (CLI)  
✔ Modern GUI Interface  
✔ Dark-Themed Design  
✔ Clear Button  
✔ Message History  
✔ Real-time Spam Detection  
✔ GitHub Version Control  

---

##  Demo

### GUI Interface Includes:

- Text input box
- Check Message button
- Clear button
- Result display (Color-coded)
- Message history log
- Accuracy display

---

##  Technologies Used

| Technology        | Purpose |
|-------------------|----------|
| Python            | Programming Language |
| Pandas            | Data Processing |
| NumPy             | Numerical Operations |
| Scikit-learn      | Machine Learning |
| TF-IDF Vectorizer | Text Feature Extraction |
| Naive Bayes       | Classification Model |
| Tkinter           | GUI Development |
| Git & GitHub      | Version Control |

---

##  Machine Learning Workflow

1. Load Dataset (SMS Spam Collection – 5574 messages)
2. Preprocess Data
3. Convert text to numerical features using TF-IDF
4. Split data into training and testing sets
5. Train model using Multinomial Naive Bayes
6. Evaluate model accuracy
7. Save trained model (.pkl)
8. Load model for real-time prediction

---

##  Model Performance

- Dataset Size: 5574 messages
- Spam Messages: 747
- Ham Messages: 4827
- Algorithm: Multinomial Naive Bayes
- Accuracy Achieved: **97.85%**

This high accuracy demonstrates effective text classification using classical ML algorithms.

---

##  Project Structure

```
AI-Spam-Message-Detector/
│
├── train_model.py        # Model training script
├── app.py                # CLI prediction version
├── gui_app.py            # Modern GUI application
├── requirements.txt      # Required libraries
├── README.md             # Project documentation
├── DATASET/              # SMS dataset
└── MODEL/                # Saved model & vectorizer
```

---

##  Installation & Setup

### Step 1: Clone Repository

```
git clone https://github.com/praveen12618/AI-Spam-Message-Detector.git
cd AI-Spam-Message-Detector
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

### Step 3: Train Model

```
py train_model.py
```

### Step 4: Run GUI Application

```
py gui_app.py
```

---

##  Example Test Cases

### Spam Example:
```
Congratulations! You won 50000 cash prize. Call now!
```

Prediction:
```
🚨 SPAM
```

### Normal Example:
```
Hey bro, are you coming to college today?
```

Prediction:
```
✅ NOT SPAM
```

---

##  How It Works (Simple Explanation)

The system converts text messages into numerical form using TF-IDF (Term Frequency – Inverse Document Frequency).

The Naive Bayes algorithm then calculates probabilities and predicts whether the message belongs to the spam category or not.

---

##  Future Improvements

- Convert to Flask Web Application
- Deploy on Cloud Platform
- Add Email Spam Detection
- Add Deep Learning Model (LSTM)
- Create REST API
- Add User Authentication

---

##  Author

**Somanaboina Praveen Kumar**  
GitHub: https://github.com/praveen12618  

---

##  If You Like This Project

Give it a star ⭐ on GitHub!
