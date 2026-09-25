# AI Spam Message Detector

An AI-powered Spam Message Detection System built using Python and Machine Learning. This project classifies SMS messages as **SPAM** or **NOT SPAM** using Natural Language Processing (NLP) and the Multinomial Naive Bayes algorithm.

## Table of Contents

* [Project Overview](#project-overview)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Machine Learning Workflow](#machine-learning-workflow)
* [Model Performance](#model-performance)
* [Project Structure](#project-structure)
* [Installation and Setup](#installation-and-setup)
* [How It Works](#how-it-works)
* [Example Test Cases](#example-test-cases)
* [Future Improvements](#future-improvements)
* [Author](#author)

## Project Overview

Spam messages are a common problem in digital communication. This project uses machine learning to analyze text messages and classify them as spam or legitimate messages (ham).

The application provides a graphical user interface for individual message detection and bulk CSV processing.

## Features

* Machine learning-based spam classification
* NLP-based text processing
* GUI application built with Tkinter
* Single-message spam detection
* Prediction confidence percentage
* Prediction history
* Export prediction history to CSV
* Bulk spam detection from CSV files
* Export bulk prediction results
* Dashboard statistics:

  * Total messages analyzed
  * Spam messages detected
  * Not-spam messages detected
* Clear history and reset statistics
* Command-line prediction interface
* Saved machine learning model and vectorizer

## Technologies Used

| Technology              | Purpose                        |
| ----------------------- | ------------------------------ |
| Python                  | Programming language           |
| Pandas                  | Data processing                |
| Scikit-learn            | Machine learning               |
| Multinomial Naive Bayes | Classification                 |
| Text Vectorizer         | Text feature extraction        |
| Tkinter                 | GUI development                |
| Joblib                  | Saving and loading model files |
| Git and GitHub          | Version control                |

## Machine Learning Workflow

1. Load the SMS Spam Collection dataset.
2. Preprocess the message text.
3. Convert text into numerical features using a text vectorizer.
4. Split the dataset into training and testing sets.
5. Train the Multinomial Naive Bayes classifier.
6. Evaluate model performance.
7. Save the trained model and vectorizer.
8. Load the saved model for real-time predictions.

## Model Performance

| Metric            | Value                   |
| ----------------- | ----------------------- |
| Dataset size      | 5,574 messages          |
| Spam messages     | 747                     |
| Ham messages      | 4,827                   |
| Algorithm         | Multinomial Naive Bayes |
| Reported accuracy | 97.85%                  |

*The reported accuracy should be verified against the evaluation results from the current training script.*

## Project Structure

```text
AI-Spam-Message-Detector/
│
├── train_model.py
├── app.py
├── gui_app.py
├── requirements.txt
├── README.md
│
├── DATASET/
│   └── spam.csv
│
└── MODEL/
    ├── spam_model.pkl
    └── vectorizer.pkl
```

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/somanaboinapraveenkumar/AI-Spam-Message-Detector.git
cd AI-Spam-Message-Detector
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Train the Model (Optional)

```bash
py train_model.py
```

### Step 4: Run the GUI Application

```bash
py gui_app.py
```

### Step 5: Run the Command-Line Application

```bash
py app.py
```

## How It Works

The application converts text messages into numerical features using a text vectorization technique. The Multinomial Naive Bayes classifier uses these features to predict whether a message is spam or not spam.

The GUI displays the prediction, confidence percentage, history, and statistics. Users can also upload CSV files to classify multiple messages.

## Example Test Cases

### Spam Example

```text
Congratulations! You won a cash prize. Call now to claim your reward!
```

Expected prediction:

```text
SPAM
```

### Normal Message Example

```text
Hey, are you coming to college today?
```

Expected prediction:

```text
NOT SPAM
```

*Predictions depend on the trained model and the input message.*

## Future Improvements

* Develop a web application using Flask or FastAPI
* Deploy the application to a cloud platform
* Add email spam detection
* Explore deep learning models
* Create a REST API
* Add user authentication
* Improve model evaluation and performance analysis

## Author

**Somanaboina Praveen Kumar**

GitHub: [somanaboinapraveenkumar](https://github.com/somanaboinapraveenkumar)

## Support

If you find this project useful, consider giving the repository a star on GitHub.
