import streamlit as st

# Title of the app
st.markdown("<h1 style='text-align: center; color: brown;'>Arjun, complete all questions for a chocolate!</h1>", unsafe_allow_html=True)

# List of math questions and answers
questions = [
    {"question": "What is 5 + 3?", "answer": "8"},
    {"question": "What is 12 - 4?", "answer": "8"},
    {"question": "What is 9 x 3?", "answer": "27"},
    {"question": "What is 16 / 2?", "answer": "8"},
    {"question": "What is the square root of 49?", "answer": "7"},
    {"question": "What is 15 % 4?", "answer": "3"},
    {"question": "What is 2^5?", "answer": "32"},
    {"question": "What is the cube root of 27?", "answer": "3"},
    {"question": "What is 10 + 10 x 2?", "answer": "30"},  # Order of operations
    {"question": "What is 7 - (3 + 2)?", "answer": "2"},
    {"question": "What is 4! (factorial)?", "answer": "24"},
    {"question": "What is the value of pi (up to 2 decimal places)?", "answer": "3.14"},
    {"question": "What is 7^2?", "answer": "49"},
    {"question": "What is the derivative of x^2?", "answer": "2x"},
    {"question": "What is the integral of 1/x dx?", "answer": "ln(x) + C"},
    {"question": "What is the hypotenuse of a right triangle with sides 3 and 4?", "answer": "5"},
    {"question": "What is the sum of the first 5 prime numbers?", "answer": "28"},
    {"question": "What is the area of a circle with radius 3?", "answer": "28.27"},  # Approx.
    {"question": "What is 1001 - 999?", "answer": "2"},
    {"question": "What is (10 + 2) * (5 - 3)?", "answer": "24"}  # Order of operations
]

# Initialize session state variables
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'consecutive_correct' not in st.session_state:
    st.session_state.consecutive_correct = 0
if 'user_name' not in st.session_state:
    st.session_state.user_name = ''

# Function to display the quiz
def display_quiz():
    st.write(f"Answer this, {st.session_state.user_name}!")
    st.write(f"Consecutive correct answers: {st.session_state.consecutive_correct}")
    
    question_data = questions[st.session_state.current_question]
    st.write(f"Question {st.session_state.current_question + 1}: {question_data['question']}")
    user_answer = st.text_input("Your answer:", key=f"answer_{st.session_state.current_question}")

    if st.button("Submit Answer", key=f"submit_{st.session_state.current_question}"):
        if user_answer.lower().strip() == question_data['answer'].lower().strip():
            st.session_state.score += 1
            st.session_state.consecutive_correct += 1
            st.success("Correct!")
        else:
            st.error(f"Incorrect. The correct answer is {question_data['answer']}. The game will restart.")
            restart_quiz()

        st.session_state.current_question += 1

        if st.session_state.current_question < len(questions):
            display_quiz()
        else:
            st.balloons()
            st.success(f"Quiz completed! Your score is {st.session_state.score}/{len(questions)}")
            st.write(f"Consecutive correct answers: {st.session_state.consecutive_correct}")
            if st.button("Restart Quiz", key="restart_button"):
                restart_quiz()

# Function to restart the quiz
def restart_quiz():
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.consecutive_correct = 0

# Input for user's name
if st.session_state.user_name == '':
    st.session_state.user_name = st.text_input("Enter your name:", key="name")

# Display the quiz if the user's name is provided
if st.session_state.user_name:
    display_quiz()
