import streamlit as st
import time

# Function to check the answer
def check_answer(question, correct_answer):
    user_answer = st.text_input(question, key=question)
    if user_answer:
        if user_answer.lower() == correct_answer.lower():
            st.success("That's correct!")
            return True
        else:
            st.error("That's incorrect. Please try again.")
    return False

# Title of the app
st.title("Question and Answer Quiz App")

# List of questions and answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our Solar System?", "answer": "Jupiter"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "What is the square root of 64?", "answer": "8"}
]

# Display questions one at a time
current_question = 0
while current_question < len(questions):
    question = questions[current_question]["question"]
    correct_answer = questions[current_question]["answer"]

    if check_answer(question, correct_answer):
        current_question += 1
    else:
        st.stop()

# All questions answered correctly
st.success("Congratulations! You've completed the quiz.")

# Keep the terminal open
input("Press Enter to exit...")
