import streamlit as st
import json
import os
import random

# Initialize the player file
player_FILE = "player.json"
if not os.path.exists(player_FILE):
    with open(player_FILE, "w") as f:
        json.dump([], f)

# Load the player
def load_player():
    with open(player_FILE, "r") as f:
        return json.load(f)

# Save the player
def save_player(data):
    with open(player_FILE, "w") as f:
        json.dump(data, f)

# Update the player
def update_player(name, score):
    player = load_player()
    player.append({"name": name, "score": score})
    player = sorted(player, key=lambda x: x["score"], reverse=True)[:10]  # Keep top 10
    save_player(player)

# Title of the app
st.markdown("<h1 style='text-align: center; color: brown;'>Arjun, complete all questions for a chocolate!</h1>", unsafe_allow_html=True)

# List of math questions
questions = [
    # Math Questions
    {"question": "What is 5 + 3?\n(options: 6, 7, 8, 9)", "answer": "8"},
    {"question": "What is 12 - 4?\n(options: 7, 8, 9, 10)", "answer": "8"},
    {"question": "What is 9 x 3?\n(options: 24, 25, 26, 27)", "answer": "27"},
    {"question": "What is 16 / 2?\n(options: 6, 7, 8, 9)", "answer": "8"},
    {"question": "What is 4! (factorial)?\n(options: 20, 22, 24, 26)", "answer": "24"},
    {"question": "What is the square root of 144?\n(options: 10, 11, 12, 13)", "answer": "12"},
    {"question": "What is 15 + 27?\n(options: 40, 41, 42, 43)", "answer": "42"},
    {"question": "What is 81 / 9?\n(options: 7, 8, 9, 10)", "answer": "9"},
    {"question": "What is 7 x 7?\n(options: 48, 49, 50, 51)", "answer": "49"},
    {"question": "What is the cube of 3?\n(options: 26, 27, 28, 29)", "answer": "27"},
    {"question": "What is 10^2?\n(options: 50, 75, 90, 100)", "answer": "100"},
    {"question": "What is 64 - 9?\n(options: 54, 55, 56, 57)", "answer": "55"},
    {"question": "What is the square root of 121?\n(options: 9, 10, 11, 12)", "answer": "11"},
    {"question": "What is 25 x 4?\n(options: 75, 80, 85, 90)", "answer": "100"},
    {"question": "What is 81 - 26?\n(options: 54, 55, 56, 57)", "answer": "55"},
    {"question": "What is 6 x 6?\n(options: 35, 36, 37, 38)", "answer": "36"},
    {"question": "What is 45 / 5?\n(options: 8, 9, 10, 11)", "answer": "9"},
    {"question": "What is 9^2?\n(options: 79, 80, 81, 82)", "answer": "81"},
    {"question": "What is 13 + 28?\n(options: 40, 41, 42, 43)", "answer": "41"},
    {"question": "What is 4 x 5?\n(options: 20, 21, 22, 23)", "answer": "20"},
    {"question": "What is the square root of 81?\n(options: 8, 9, 10, 11)", "answer": "9"},
    {"question": "What is 72 / 8?\n(options: 7, 8, 9, 10)", "answer": "9"},
    {"question": "What is 8 x 7?\n(options: 55, 56, 57, 58)", "answer": "56"},
    {"question": "What is 55 - 11?\n(options: 43, 44, 45, 46)", "answer": "44"},
    {"question": "What is the cube root of 27?\n(options: 2, 3, 4, 5)", "answer": "3"},
    {"question": "What is 6 x 8?\n(options: 46, 47, 48, 49)", "answer": "48"},
    {"question": "What is 100 / 4?\n(options: 23, 24, 25, 26)", "answer": "25"},
    {"question": "What is 9 - 5?\n(options: 3, 4, 5, 6)", "answer": "4"},
    {"question": "What is 18 x 2?\n(options: 34, 35, 36, 37)", "answer": "36"},
    {"question": "What is 3^3?\n(options: 26, 27, 28, 29)", "answer": "27"},
    {"question": "What is 20 + 15?\n(options: 33, 34, 35, 36)", "answer": "35"},
    {"question": "What is 45 - 15?\n(options: 28, 29, 30, 31)", "answer": "30"},
    {"question": "What is 7 x 8?\n(options: 54, 55, 56, 57)", "answer": "56"},
    {"question": "What is 12 x 12?\n(options: 142, 143, 144, 145)", "answer": "144"},
    {"question": "What is 144 / 12?\n(options: 11, 12, 13, 14)", "answer": "12"},
    {"question": "What is the square root of 225?\n(options: 14, 15, 16, 17)", "answer": "15"},
    {"question": "What is 27 - 10?\n(options: 16, 17, 18, 19)", "answer": "17"}
]

# Initialize session state variables
if 'shuffled_questions' not in st.session_state:
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
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
    st.sidebar.markdown("<h2 style='color: brown; font-family: MV Boli; font-size: 30px;'>Leaderboard</h2>", unsafe_allow_html=True)
    player = load_player()
    for entry in player:
        st.sidebar.markdown(f"<p style='color: white; font-family: Ink Free; font-size: 20px;'>{entry['name']}: {entry['score']}</p>", unsafe_allow_html=True)

    st.write(f"Answer this, {st.session_state.user_name}!")
    st.write(f"Correct answers provided by you: {st.session_state.consecutive_correct}")
    
    question_data = st.session_state.shuffled_questions[st.session_state.current_question]
    st.write(f"Question {st.session_state.current_question + 1}: {question_data['question']}")
    user_answer = st.text_input("Your answer:", key=f"answer_{st.session_state.current_question}")

    submit_answer = st.button("Submit Answer", key=f"submit_{st.session_state.current_question}")
    
    if submit_answer:
        if user_answer.lower().strip() == question_data['answer'].lower().strip():
            st.success("Correct!")
            st.session_state.score += 1
            st.session_state.consecutive_correct += 1
            st.session_state.current_question += 1

            if st.session_state.current_question >= len(st.session_state.shuffled_questions):
                st.balloons()
                st.success(f"Quiz completed! Your score is {st.session_state.score}/{len(st.session_state.shuffled_questions)}")
                st.write(f"Consecutive correct answers: {st.session_state.consecutive_correct}")
                update_player(st.session_state.user_name, st.session_state.consecutive_correct)
                if st.button("Restart Quiz", key="restart_button"):
                    "restart_quiz"()
        else:
            st.error("Incorrect!")
            update_player(st.session_state.user_name, st.session_state.consecutive_correct)
