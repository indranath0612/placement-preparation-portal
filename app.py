from flask import Flask, render_template, request, redirect, session
import sqlite3

app = Flask(__name__)
app.secret_key = "placement_secret"


def get_db():
    return sqlite3.connect("database.db")

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"
@app.route("/admin", methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        if request.form["username"] == ADMIN_USERNAME and request.form["password"] == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect("/add_question")
    return render_template("admin.html")
@app.route("/add_question", methods=["GET", "POST"])
def add_question():
    if not session.get("admin"):
        return redirect("/admin")

    if request.method == "POST":
        questions.append({
            "q": request.form["question"],
            "options": [
                request.form["opt1"],
                request.form["opt2"],
                request.form["opt3"],
                request.form["opt4"]
            ],
            "answer": request.form["answer"]
        })
    return render_template("add_question.html")


@app.route("/")
def home():
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO users VALUES (?,?)", (username, password))
        conn.commit()
        conn.close()

        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = username
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

import sqlite3, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

@app.route("/coding")
def coding():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("SELECT question FROM coding_questions")
    rows = cur.fetchall()

    conn.close()

    questions = [r[0] for r in rows]
    return render_template("coding.html", questions=questions)


@app.route("/resume")
def resume():
    return render_template("resume.html")



questions = [
    {
        "q": "What is Python?",
        "options": ["Snake", "Programming Language", "Game", "OS"],
        "answer": "Programming Language"
    },
    {
        "q": "Which is immutable?",
        "options": ["List", "Tuple", "Dictionary", "Set"],
        "answer": "Tuple"
    }
]

import sqlite3, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_random_mcqs(limit=10):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        SELECT question, option1, option2, option3, option4, answer
        FROM mcq
        ORDER BY RANDOM()
        LIMIT ?
    """, (limit,))

    rows = cur.fetchall()
    conn.close()

    return [
        {"q": r[0], "options": [r[1], r[2], r[3], r[4]], "answer": r[5]}
        for r in rows
    ]

@app.route("/mocktest", methods=["GET", "POST"])
def mocktest():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("""
        SELECT id, question, option1, option2, option3, option4, answer
        FROM mock_questions
        ORDER BY RANDOM()
        LIMIT 10
    """)
    rows = cur.fetchall()
    conn.close()

    questions = []
    for row in rows:
        questions.append({
            "id": row["id"],
            "q": row["question"],
            "options": [
                row["option1"],
                row["option2"],
                row["option3"],
                row["option4"]
            ],
            "answer": row["answer"],
            "selected": None
        })

    score = None
    submitted = False

    if request.method == "POST":
        submitted = True
        score = 0

        for i, q in enumerate(questions):
            selected = request.form.get(f"q{i}")
            q["selected"] = selected

            if selected and selected.strip() == q["answer"].strip():
                score += 1

    return render_template(
        "mocktest.html",
        questions=questions,
        score=score,
        submitted=submitted
    )



if __name__ == "__main__":
    app.run(debug=True)
