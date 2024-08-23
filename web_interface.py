import streamlit as st
from language_model import Chatbot
from sentiment_analysis import SentimentAnalyzer
from translation_service import TranslatorService
from speech_processing import SpeechProcessor

st.title("Multilingual AI Chatbot with Sentiment Analysis")

chatbot = Chatbot()
sentiment_analyzer = SentimentAnalyzer()
translator = TranslatorService()
speech_processor = SpeechProcessor()

user_input = st.text_input("Type your message here:")

if user_input:
    sentiment = sentiment_analyzer.analyze(user_input)
    st.write("Sentiment:", sentiment)
    
    language = st.selectbox("Select your language:", ["en", "es", "fi"])
    translated_input = translator.translate(user_input, dest_language=language)
    
    response = chatbot.generate_response(translated_input)
    translated_response = translator.translate(response, dest_language="en")
    
    st.write("Chatbot Response:", translated_response)
    
    if st.button("Convert to Speech"):
        speech = speech_processor.text_to_speech(translated_response)
        st.audio(speech)
