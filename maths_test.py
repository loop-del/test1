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

# List of math and GK questions
questions = [
    # Math Questions
    {"question": "What is 5 + 3?\n(options: 6, 7, 8, 9)", "answer": "8"},
    {"question": "What is 12 - 4?\n(options: 7, 8, 9, 10)", "answer": "8"},
    {"question": "What is 9 x 3?\n(options: 24, 25, 26, 27)", "answer": "27"},
    {"question": "What is 16 / 2?\n(options: 6, 7, 8, 9)", "answer": "8"},
    {"question": "What is 4! (factorial)?\n(options: 20, 22, 24, 26)", "answer": "24"},
    
    # GK Questions
    {"question": "What is the capital of France?\n(options: Berlin, Paris, Madrid, Rome)", "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?\n(options: Earth, Mars, Venus, Jupiter)", "answer": "Mars"},
    {"question": "What is the largest mammal in the world?\n(options: Elephant, Whale, Shark, Bear)", "answer": "Whale"},
    {"question": "Who wrote 'Romeo and Juliet'?\n(options: Shakespeare, Dickens, Orwell, Austen)", "answer": "Shakespeare"},
    {"question": "What is the currency of Japan?\n(options: Yen, Dollar, Euro, Pound)", "answer": "Yen"},
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
                    restart_quiz()
        else:
            st.error("Incorrect!")
            update_player(st.session_state.user_name, st.session_state.consecutive_correct)
            restart_quiz()

# Function to restart the quiz
def restart_quiz():
    st.session_state.shuffled_questions = random.sample(questions, len(questions))
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.consecutive_correct = 0

# Input for user's name
if st.session_state.user_name == '':
    st.session_state.user_name = st.text_input("Enter your name:", key="name")

# Display the quiz if the user's name is provided
if st.session_state.user_name:
    display_quiz()
