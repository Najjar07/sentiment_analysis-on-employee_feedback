import pandas as pd
import joblib
import streamlit as st


model_path = sentiments_model.pkl"
encoder_path = sentiments_encoder.pkl"
model = joblib.load(model_path)
encoder = joblib.load(encoder_path)

st.set_page_config(page_title="Neural Network-Based Sentiment Analysis on Employee Feedback App", layout="wide")
st.markdown(
    """
    <style>.stApp {
    backgroung-color: #F9FAFB;  /* very light gray */
    }
    </style>
    """, unsafe_allow_html=True
)
st.title("Neural Network-Based Sentiment Analysis on Employee Feedback App")
st.write("Analyze employee feedback and classify it as Positive, Neutral, or Negative.")
feedback = st.text_area("Enter employee feedback")

def contains_number(text):
    return any(char.isdigit() for char in text)

if st.button("predict sentiment"):
    if feedback.strip() == "":
        st.warning("Please enter some feedback text.")
    elif contains_number(feedback):
        st.error("Numbers are not allowed. Please text only")

    else:
        encoder = encoder.transform([feedback])
        prediction = model.predict(encoder)[0]
        confidence = model.predict_proba(encoder).max()

        #st.success(f"Sentiment: {prediction}")
       # st.write(f"confidence: {confidence:.2f}")

        if prediction.lower() == "positive":
            st.success(f"Sentiment: {prediction}")
            st.write(f"Confidence: {confidence:.2f}")
            st.balloons()
        elif prediction.lower() == "neutral":
            st.info(f"Sentiment: {prediction}")
            st.write(f"Confidence: {confidence:.2f}")
        else:
            st.error(f"Sentiment: {prediction}")
            st.write(f"Confidence: {confidence:.2f}")



    
