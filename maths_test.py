import streamlit as st

# Title of the app
st.markdown("<h1 style='text-align: center; color: brown;'>Arjun, complete all questions for a chocolate!</h1>", unsafe_allow_html=True)

# List of math questions and answers including algebraic equations
questions = [ 
    {"question": "What is 7 - (3 + 2)?", "answer": "2"},
    {"question": "What is 4! (factorial)?", "answer": "24"},
    {"question": "What is the value of pi (up to 2 decimal places)?", "answer": "3.14"},
    {"question": "Solve for x: 2x + 3 = 7", "answer": "2"},
    {"question": "Solve for x: 5x - 2 = 3x + 4", "answer": "3"},
    {"question": "Solve for x: x^2 - 4x + 4 = 0", "answer": "2"},
    {"question": "Solve for x: 3x/2 = 9", "answer": "6"},
    {"question": "Solve for y: 2y + 4 = 2", "answer": "-1"},
    {"question": "Solve for x: x^2 = 16", "answer": "4"},
    {"question": "Solve for x: (x - 1)(x + 2) = 0", "answer": "1"},
    {"question": "Solve for x: 4x - 8 = 0", "answer": "2"}  # Simple algebra
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
    st.write(f"Correct answers provided by you: {st.session_state.consecutive_correct}")
    
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
