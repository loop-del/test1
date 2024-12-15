import streamlit as st

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
st.title("Hard Maths and General Knowledge Quiz")

# List of questions and answers (mix of Maths and GK with harder questions)
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our Solar System?", "answer": "Jupiter"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "What is 15 + 26?", "answer": "41"},
    {"question": "Who invented the telephone?", "answer": "Alexander Graham Bell"},
    {"question": "What is the speed of light in meters per second?", "answer": "299792458"},
    
    # Harder questions
    {"question": "What is the value of Pi up to 10 decimal places?", "answer": "3.1415926535"},
    {"question": "What is the derivative of x^2 + 3x + 5?", "answer": "2x + 3"},
    {"question": "Who developed the theory of relativity?", "answer": "Albert Einstein"},
    {"question": "What is the chemical formula for methane?", "answer": "CH4"},
    {"question": "What is the sum of the angles of a triangle in Euclidean geometry?", "answer": "180 degrees"},
    {"question": "Who is known as the father of modern physics?", "answer": "Galileo Galilei"},
    {"question": "What is the square root of 144?", "answer": "12"},
    {"question": "What is the largest prime number less than 100?", "answer": "97"},
    {"question": "What is the capital of Mongolia?", "answer": "Ulaanbaatar"},
    {"question": "What is the atomic number of gold?", "answer": "79"}
]

# Initialize the current question index in session state
if "current_question" not in st.session_state:
    st.session_state.current_question = 0

# Display questions one at a time
current_question = st.session_state.current_question
question = questions[current_question]["question"]
correct_answer = questions[current_question]["answer"]

if check_answer(question, correct_answer):
    st.session_state.current_question += 1

# Check if all questions have been answered correctly
if st.session_state.current_question == len(questions):
    st.success("Congratulations! You've completed the quiz.")
