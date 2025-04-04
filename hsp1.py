import streamlit as st
from datetime import datetime
import random
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key="AIzaSyDW9bwVLg22-bXwLv3pO9D5zeqP99INYS0")

# Load Gemini Model
model = genai.GenerativeModel("gemini-1.5-pro")

def generate_appointment_id():
    return f"APT-{random.randint(1000, 9999)}"

st.set_page_config(page_title="Medical AI Assistant", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Book Appointment", "Symptom Checker", "Medical Q&A"])

if page == "Home":
    st.title("Welcome to Medical AI Assistant")
    st.write("Use this AI-powered system for real-time medical assistance.")
    st.image("https://source.unsplash.com/800x400/?healthcare,doctor")

elif page == "Book Appointment":
    st.title("Book an Appointment")
    with st.form("appointment_form"):
        name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        doctor = st.selectbox("Select Doctor", ["Dr. Smith (Cardiologist)", "Dr. Johnson (Dermatologist)", "Dr. Lee (Pediatrician)"])
        date = st.date_input("Select Date", min_value=datetime.today())
        time = st.time_input("Select Time")
        submit = st.form_submit_button("Book Appointment")
    
    if submit:
        appointment_id = generate_appointment_id()
        st.success(f"Appointment confirmed! ID: {appointment_id}")

elif page == "Symptom Checker":
    st.title("AI-Powered Symptom Checker")
    symptoms = st.text_area("Enter your symptoms (comma-separated)")
    if st.button("Check Symptoms"):
        with st.spinner("Analyzing symptoms..."):
            prompt = f"A patient reports the following symptoms: {symptoms}. What possible medical conditions could this indicate?"
            response = model.generate_content(prompt)
            st.success(response.text if response else "No response received.")

elif page == "Medical Q&A":
    st.title("Medical Q&A")
    question = st.text_area("Ask a medical question")
    if st.button("Get Answer"):
        with st.spinner("Processing your question..."):
            response = model.generate_content(question)
            st.success(response.text if response else "No response received.")

st.sidebar.info("Developed using Streamlit, Gemini AI, and Multi-Agent Systems.")
