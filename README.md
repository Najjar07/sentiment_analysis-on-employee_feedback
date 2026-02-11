# Neural Network-Based Sentiment Analysis on Employee Feedback App

## 📌 Overview

This project is an end-to-end **Machine Learning web application** that analyzes employee feedback and classifies sentiment into **Positive**, **Neutral**, or **Negative** categories. The application is built using a Neural Network model and deployed with **Streamlit** to provide an interactive and user-friendly interface.

The system allows users to enter employee feedback text, instantly predict sentiment, display confidence scores, and automatically log predictions for future analysis.

---

## 🚀 Features

* ✅ Neural Network-based sentiment classification
* ✅ Real-time prediction using Streamlit interface
* ✅ Confidence score display
* ✅ Input validation (prevents empty input and numbers)
* ✅ Automatic logging of predictions to CSV file
* ✅ Timestamp recording for each prediction
* ✅ Interactive UI feedback (success, info, error messages)

---

## 🧠 Machine Learning Workflow

The application follows a standard ML pipeline:

1. Data preprocessing and text encoding
2. Feature transformation using trained encoder
3. Model prediction using trained neural network
4. Confidence score extraction
5. Result display on Streamlit dashboard
6. Prediction logging to CSV file

---

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Streamlit
* Neural Network Model


## ⚙️ Installation and Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/sentiment-analysis-app.git
cd sentiment-analysis-app
```

### 2️⃣ Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Run the Streamlit app using:

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

## 🧾 Input Rules

* Feedback text must not be empty
* Numbers are not allowed in input
* Only text-based feedback is accepted

---

## 📊 Output

The application provides:

* Predicted Sentiment (Positive / Neutral / Negative)
* Prediction Confidence Score
* Visual feedback notification

All predictions are saved automatically in:

```
sentiment_predictions.csv
```

---

## 📈 Future Improvements

* Model performance dashboard
* API deployment
* Cloud deployment (Streamlit Cloud / AWS / Render)
* Advanced NLP preprocessing
* User authentication system

---

## 👨‍💻 Author

**Najari Umar Jibril**
Machine Learning Engineer
Focused on building practical AI solutions for real-world problems.

---

## 📜 License

This project is open-source and available under the MIT License.

