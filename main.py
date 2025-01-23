import streamlit as st

# Define the quiz questions, answers, and the correct answers
questions = [
    {
        "question": "What are the primary colors?",
        "options": ["Red", "Blue", "Green", "Yellow", "Black"],
        "correct_answers": ["Red", "Blue", "Yellow"],
        "qimage": None,
        "aimage": None
    },
    {
        "question": "(See image above)",
        "options": ["A", "B", "C", "o-krezol a p-xylén"],
        "correct_answers": ["B", "o-krezol a p-xylén"],
        "qimage": "question.png",
        "aimage": "answers.png"
    },
    {
        "question": "Životné procesy skúška:",
        "options": ["Earth", "Mars", "Sun", "Pluto", "Moon"],
        "correct_answers": ["Earth", "Mars", "Pluto"],
        "qimage": None,
        "aimage": None
    }
]

# Streamlit app
def quiz_app():
    st.title("Quiz Time!")

    # Initialize score and list to store user answers
    score = 0
    user_answers = []

    # Loop through each question
    for idx, question in enumerate(questions):
        if question["qimage"] is None:
            st.subheader(f"Q{idx + 1}: {question['question']}")
        else:
            st.image(question["qimage"])

        # Create checkboxes for the options
        selected_answers = []
        for option in question["options"]:
            if st.checkbox(option, key=f"q{idx}_{option}"):
                selected_answers.append(option)

        if question["aimage"] is not None:
            st.image(question["aimage"])

        # Store the selected answers for each question
        user_answers.append({"question": question['question'], "selected_answers": selected_answers})

        st.markdown("<hr>", unsafe_allow_html=True)

    # Submit button to show results
    if st.button("Submit Quiz"):

        print(user_answers)

        for idx, question in enumerate(questions):
            correct_answers = set(question["correct_answers"])
            selected_answers = set(user_answers[idx]["selected_answers"])

            # Check if the selected answers are correct
            correct_count = len(correct_answers & selected_answers)
            total_correct_answers = len(correct_answers)

            # Display result for the question
            if question["qimage"] is None:
                st.subheader(f"Q{idx + 1}: {question['question']}")
            else:
                st.image(question["qimage"])
            if question["aimage"] is not None:
                st.image(question["aimage"])
            st.write(f"Your selected answers: {', '.join(selected_answers)}")
            st.write(f"Correct answers: {', '.join(correct_answers)}")

            if selected_answers == correct_answers:
                st.write(f"✅ Correct! You selected all the correct answers!")
            else:
                st.write(f"❌ Incorrect. You selected {correct_count}/{total_correct_answers} correct answer(s).")

            st.markdown("<hr>", unsafe_allow_html=True)

        # Calculate the overall score
        total_questions = len(questions)
        score = sum([1 if set(user_answers[idx]["selected_answers"]) == set(question["correct_answers"]) else 0 for idx, question in enumerate(questions)])
        st.write(f"**Your total score: {score}/{total_questions}**")

# Run the app
if __name__ == "__main__":
    quiz_app()
