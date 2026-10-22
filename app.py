
import streamlit as st

st.set_page_config(
    page_title="QuizMaster",
    page_icon="🧠",
    layout="centered"
)

# -------------------- DESIGN --------------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f172a, #211638);
    color: white;
}

h1, h2, h3, p, label {
    color: white;
}

.quiz-card {
    padding: 22px;
    border-radius: 18px;
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.14);
    animation: fadeSlideIn 0.55s ease;
}

@keyframes fadeSlideIn {
    from {opacity: 0; transform: translateY(14px);}
    to {opacity: 1; transform: translateY(0);}
}

@keyframes softGlow {
    0%, 100% {box-shadow: 0 0 8px #7c3aed33;}
    50% {box-shadow: 0 0 22px #7c3aed77;}
}

.result-card {
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    background: linear-gradient(135deg, #312e81, #581c87);
    animation: fadeSlideIn 0.7s ease, softGlow 2.5s infinite;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    border: 1px solid #7c3aed;
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white;
    font-weight: bold;
    padding: 9px;
    transition: all 0.2s ease;
}

.stButton > button:hover {
    transform: translateY(-2px);
    border-color: #a78bfa;
    color: white;
}

div[data-testid="stRadio"] label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)


# -------------------- QUESTIONS --------------------

QUIZZES = {
    "Python": {
        "Easy": [
            {"question": "Which function displays output in Python?",
             "options": ["input()", "print()", "show()", "display()"],
             "answer": "print()", "explanation": "The print() function displays output."},
            {"question": "Which symbol starts a single-line comment in Python?",
             "options": ["//", "#", "/*", "&"],
             "answer": "#", "explanation": "The # symbol starts a single-line comment."},
            {"question": "Which data type represents True or False?",
             "options": ["int", "str", "bool", "list"],
             "answer": "bool", "explanation": "The bool data type represents True or False."},
            {"question": "Which keyword is used to define a function?",
             "options": ["func", "define", "def", "function"],
             "answer": "def", "explanation": "Python functions are defined using def."},
            {"question": "Which brackets are used to create a list?",
             "options": ["{}", "()", "[]", "<>"],
             "answer": "[]", "explanation": "Lists use square brackets."}
        ],
        "Medium": [
            {"question": "What is len('Python')?",
             "options": ["5", "6", "7", "8"],
             "answer": "6", "explanation": "Python contains six characters."},
            {"question": "What is the result of 10 // 3?",
             "options": ["3.33", "3", "4", "1"],
             "answer": "3", "explanation": "The // operator performs floor division."},
            {"question": "Which keyword handles an exception?",
             "options": ["catch", "except", "error", "final"],
             "answer": "except", "explanation": "The except block handles exceptions."},
            {"question": "What is the result of [1, 2, 3][1]?",
             "options": ["1", "2", "3", "Error"],
             "answer": "2", "explanation": "List indexing starts at index zero."},
            {"question": "Which method adds an item to the end of a list?",
             "options": ["add()", "append()", "push()", "attach()"],
             "answer": "append()", "explanation": "append() adds an item to the end of a list."}
        ],
        "Hard": [
            {"question": "What is [x*x for x in range(3)]?",
             "options": ["[1, 4, 9]", "[0, 1, 4]", "[0, 1, 2]", "[0, 2, 4]"],
             "answer": "[0, 1, 4]", "explanation": "The values 0, 1 and 2 are squared."},
            {"question": "Which Python structure stores key-value pairs?",
             "options": ["List", "Tuple", "Dictionary", "Set"],
             "answer": "Dictionary", "explanation": "A dictionary stores data as key-value pairs."},
            {"question": "What is a lambda function?",
             "options": ["A loop", "An anonymous function", "A class", "A module"],
             "answer": "An anonymous function", "explanation": "A lambda creates a small anonymous function."},
            {"question": "Which method initializes a Python object?",
             "options": ["__start__", "__init__", "__main__", "__create__"],
             "answer": "__init__", "explanation": "__init__ initializes an object."},
            {"question": "Which collection stores unique values?",
             "options": ["List", "Tuple", "Set", "String"],
             "answer": "Set", "explanation": "A set stores unique elements."}
        ]
    },

    "General Knowledge": {
        "Easy": [
            {"question": "What is the capital of India?",
             "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
             "answer": "New Delhi", "explanation": "New Delhi is the capital of India."},
            {"question": "Which planet is called the Red Planet?",
             "options": ["Venus", "Mars", "Jupiter", "Mercury"],
             "answer": "Mars", "explanation": "Mars is known as the Red Planet."},
            {"question": "How many days are in a leap year?",
             "options": ["364", "365", "366", "367"],
             "answer": "366", "explanation": "A leap year has 366 days."},
            {"question": "What is India's national animal?",
             "options": ["Lion", "Bengal tiger", "Elephant", "Leopard"],
             "answer": "Bengal tiger", "explanation": "The Bengal tiger is India's national animal."},
            {"question": "Which gas do plants absorb during photosynthesis?",
             "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
             "answer": "Carbon dioxide", "explanation": "Plants absorb carbon dioxide during photosynthesis."}
        ],
        "Medium": [
            {"question": "Which is the largest ocean in the world?",
             "options": ["Atlantic", "Indian", "Pacific", "Arctic"],
             "answer": "Pacific", "explanation": "The Pacific Ocean is the largest."},
            {"question": "What is the currency of Japan?",
             "options": ["Won", "Yuan", "Yen", "Ringgit"],
             "answer": "Yen", "explanation": "Japan's currency is the yen."},
            {"question": "The Hornbill Festival is celebrated in which state?",
             "options": ["Assam", "Nagaland", "Odisha", "Manipur"],
             "answer": "Nagaland", "explanation": "The festival celebrates Nagaland's cultures."},
            {"question": "Who wrote India's national anthem?",
             "options": ["Bankim Chandra Chatterjee", "Rabindranath Tagore", "Sarojini Naidu", "Premchand"],
             "answer": "Rabindranath Tagore", "explanation": "Rabindranath Tagore wrote Jana Gana Mana."},
            {"question": "Which instrument measures atmospheric pressure?",
             "options": ["Thermometer", "Barometer", "Hygrometer", "Ammeter"],
             "answer": "Barometer", "explanation": "A barometer measures atmospheric pressure."}
        ],
        "Hard": [
            {"question": "Which strait separates India and Sri Lanka?",
             "options": ["Malacca Strait", "Palk Strait", "Bering Strait", "Gibraltar Strait"],
             "answer": "Palk Strait", "explanation": "The Palk Strait lies between India and Sri Lanka."},
            {"question": "What is the smallest bone in the human body?",
             "options": ["Femur", "Stapes", "Ulna", "Patella"],
             "answer": "Stapes", "explanation": "The stapes is a small bone in the middle ear."},
            {"question": "Which treaty established the European Union?",
             "options": ["Treaty of Versailles", "Maastricht Treaty", "Treaty of Tordesillas", "Treaty of Utrecht"],
             "answer": "Maastricht Treaty", "explanation": "The Maastricht Treaty established the European Union."},
            {"question": "What is the SI unit of luminous intensity?",
             "options": ["Lux", "Lumen", "Candela", "Watt"],
             "answer": "Candela", "explanation": "Candela is the SI base unit of luminous intensity."},
            {"question": "In which atmospheric layer is most ozone found?",
             "options": ["Troposphere", "Stratosphere", "Mesosphere", "Thermosphere"],
             "answer": "Stratosphere", "explanation": "Most atmospheric ozone is found in the stratosphere."}
        ]
    },

    "Computer Science": {
        "Easy": [
            {"question": "What does CPU stand for?",
             "options": ["Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing User"],
             "answer": "Central Processing Unit", "explanation": "The CPU executes computer instructions."},
            {"question": "Which device is used to type text?",
             "options": ["Monitor", "Keyboard", "Speaker", "Printer"],
             "answer": "Keyboard", "explanation": "A keyboard is an input device."},
            {"question": "Which memory is volatile?",
             "options": ["ROM", "SSD", "RAM", "DVD"],
             "answer": "RAM", "explanation": "RAM loses its stored data when power is removed."},
            {"question": "Which of these is an operating system?",
             "options": ["Windows", "Python", "HTML", "MySQL"],
             "answer": "Windows", "explanation": "Windows is an operating system."},
            {"question": "What does CSS control?",
             "options": ["Web page styling", "Databases", "Processors", "Networks only"],
             "answer": "Web page styling", "explanation": "CSS controls the appearance of web pages."}
        ],
        "Medium": [
            {"question": "Which data structure follows FIFO?",
             "options": ["Stack", "Queue", "Tree", "Graph"],
             "answer": "Queue", "explanation": "FIFO means First In, First Out."},
            {"question": "What uniquely identifies a row in a database table?",
             "options": ["Foreign key", "Primary key", "Column name", "View"],
             "answer": "Primary key", "explanation": "A primary key uniquely identifies a row."},
            {"question": "What does HTTPS help provide?",
             "options": ["Encrypted web communication", "More RAM", "Faster CPU", "Offline storage"],
             "answer": "Encrypted web communication", "explanation": "HTTPS protects data during transmission."},
            {"question": "What is binary 101 in decimal?",
             "options": ["4", "5", "6", "7"],
             "answer": "5", "explanation": "Binary 101 equals decimal 5."},
            {"question": "Which SQL command retrieves data?",
             "options": ["GET", "SELECT", "OPEN", "SHOWALL"],
             "answer": "SELECT", "explanation": "SELECT retrieves data from database tables."}
        ],
        "Hard": [
            {"question": "What is binary search's time complexity?",
             "options": ["O(n)", "O(log n)", "O(n²)", "O(1) always"],
             "answer": "O(log n)", "explanation": "Binary search halves the search space each step."},
            {"question": "What does Second Normal Form remove?",
             "options": ["All keys", "Partial dependencies", "All relationships", "Every foreign key"],
             "answer": "Partial dependencies", "explanation": "2NF removes partial dependencies on a candidate key."},
            {"question": "Which issue can occur in priority scheduling?",
             "options": ["Starvation", "Compilation", "Encryption", "Paging only"],
             "answer": "Starvation", "explanation": "Low-priority processes may wait indefinitely."},
            {"question": "Which key encrypts a message for a recipient in public-key encryption?",
             "options": ["Recipient's public key", "Recipient's private key", "Sender's private key only", "No key"],
             "answer": "Recipient's public key", "explanation": "The recipient uses their private key to decrypt it."},
            {"question": "Which algorithm finds shortest paths with nonnegative edge weights?",
             "options": ["Dijkstra's algorithm", "Bubble sort", "Binary search", "KMP"],
             "answer": "Dijkstra's algorithm", "explanation": "Dijkstra's algorithm finds shortest paths from a source."}
        ]
    }
}

QUESTION_COUNTS = {"Easy": 3, "Medium": 4, "Hard": 5}


# -------------------- SESSION STATE --------------------

defaults = {
    "started": False,
    "finished": False,
    "question_index": 0,
    "answers": [],
    "category": "Python",
    "difficulty": "Easy",
    "questions": []
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def start_quiz():
    st.session_state.category = st.session_state.category_choice
    st.session_state.difficulty = st.session_state.difficulty_choice
    st.session_state.questions = QUIZZES[
        st.session_state.category
    ][st.session_state.difficulty][:QUESTION_COUNTS[
        st.session_state.difficulty
    ]]
    st.session_state.answers = [None] * len(st.session_state.questions)
    st.session_state.question_index = 0
    st.session_state.started = True
    st.session_state.finished = False


def go_previous():
    st.session_state.question_index -= 1


def go_next():
    i = st.session_state.question_index
    key = f"answer_{i}"
    st.session_state.answers[i] = st.session_state.get(key)
    if i < len(st.session_state.questions) - 1:
        st.session_state.question_index += 1
    else:
        st.session_state.finished = True


def quit_quiz():
    st.session_state.started = False
    st.session_state.finished = False
    st.session_state.question_index = 0
    st.session_state.answers = []
    st.session_state.questions = []


def play_again():
    quit_quiz()


# -------------------- HEADER --------------------

st.markdown(
    "<h1 style='text-align:center'>🧠 QuizMaster</h1>"
    "<p style='text-align:center'>Challenge your knowledge!</p>",
    unsafe_allow_html=True
)

st.divider()


# -------------------- HOME PAGE --------------------

if not st.session_state.started:

    st.markdown("<div class='quiz-card'>", unsafe_allow_html=True)
    st.subheader("🎯 Set Up Your Quiz")
    st.write("Choose a category and difficulty to begin.")

    st.selectbox(
        "Select Category",
        list(QUIZZES.keys()),
        key="category_choice"
    )

    st.selectbox(
        "Select Difficulty",
        ["Easy", "Medium", "Hard"],
        key="difficulty_choice"
    )

    st.caption("Easy: 3 questions | Medium: 4 questions | Hard: 5 questions")
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.button("🚀 Start Quiz", on_click=start_quiz)


# -------------------- QUIZ PAGE --------------------

elif st.session_state.started and not st.session_state.finished:

    questions = st.session_state.questions
    index = st.session_state.question_index
    question = questions[index]

    st.progress((index + 1) / len(questions))

    st.caption(
        f"{st.session_state.category} • "
        f"{st.session_state.difficulty} • "
        f"Question {index + 1} of {len(questions)}"
    )

    st.markdown("<div class='quiz-card'>", unsafe_allow_html=True)
    st.subheader(question["question"])

    answer_key = f"answer_{index}"

    # Restore the saved answer when returning to a previous question.
    if answer_key not in st.session_state:
        st.session_state[answer_key] = st.session_state.answers[index]

    selected_answer = st.radio(
        "Choose your answer:",
        question["options"],
        index=(
            question["options"].index(st.session_state[answer_key])
            if st.session_state[answer_key] in question["options"]
            else None
        ),
        key=answer_key
    )

    st.markdown("</div>", unsafe_allow_html=True)
    st.write("")

    left, middle, right = st.columns(3)

    with left:
        if index > 0:
            st.button(
                "⬅️ Previous",
                on_click=go_previous,
                use_container_width=True
            )

    with middle:
        st.button(
            "➡️ Next" if index < len(questions) - 1 else "🏁 Finish Quiz",
            on_click=go_next,
            use_container_width=True
        )

    with right:
        st.button(
            "✖ Quit Quiz",
            on_click=quit_quiz,
            use_container_width=True
        )


# -------------------- RESULTS PAGE --------------------

elif st.session_state.finished:

    questions = st.session_state.questions
    answers = st.session_state.answers
    total = len(questions)

    score = sum(
        1 for question, answer in zip(questions, answers)
        if answer == question["answer"]
    )

    percentage = round((score / total) * 100) if total else 0

    st.balloons()

    st.markdown(
        f"""
        <div class="result-card">
            <h1>🏆 Quiz Completed!</h1>
            <h2>{score} / {total}</h2>
            <h3>{percentage}%</h3>
            <p>You have completed the {st.session_state.difficulty} quiz!</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    if percentage == 100:
        st.success("Perfect score! Excellent work! 🎉")
    elif percentage >= 60:
        st.success("Great job! Keep practising! 👏")
    else:
        st.info("Keep learning. Practice makes progress! 💪")

    st.subheader("📝 Answer Review")

    for number, (question, answer) in enumerate(
        zip(questions, answers), start=1
    ):
        st.markdown(f"**Q{number}. {question['question']}**")

        if answer == question["answer"]:
            st.success(f"Your answer: {answer} — Correct!")
        else:
            st.error(f"Your answer: {answer if answer else 'Not answered'}")
            st.write(f"Correct answer: **{question['answer']}**")

        st.caption(f"💡 {question['explanation']}")
        st.divider()

    st.button("🔄 Play Again", on_click=play_again)


# -------------------- FOOTER --------------------

st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:#aaaaaa'>"
    "Made with ❤️ using Python and Streamlit"
    "</p>",
    unsafe_allow_html=True
)
