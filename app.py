from flask import Flask, render_template, request, redirect, session
import sqlite3, os

app = Flask(__name__)
app.secret_key = "supersecretkey123"

# ---------------- DATABASE SETUP ----------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "database.db")

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS mock_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        option1 TEXT,
        option2 TEXT,
        option3 TEXT,
        option4 TEXT,
        answer TEXT
    )
    """)

    conn.commit()
    conn.close()

init_db()

# ---------------- AUTH ----------------

@app.route("/")
def home():
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO users VALUES (?, ?)",
            (request.form["username"], request.form["password"])
        )
        conn.commit()
        conn.close()
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        conn = get_db()
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (request.form["username"], request.form["password"])
        )
        user = cur.fetchone()
        conn.close()

        if user:
            session["user"] = user["username"]
            return redirect("/dashboard")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# ---------------- MOCK TEST ----------------

@app.route("/mocktest", methods=["GET", "POST"])
def mocktest():
    conn = get_db()
    cur = conn.cursor()

    # ---------- PICK RANDOM QUESTIONS ONCE ----------
    if request.method == "GET":
        cur.execute("""
            SELECT id FROM mock_questions
            ORDER BY RANDOM()
            LIMIT 10
        """)
        session["mock_q_ids"] = [row["id"] for row in cur.fetchall()]

    q_ids = session.get("mock_q_ids", [])

    if not q_ids:
        conn.close()
        return render_template(
            "mocktest.html",
            questions=[],
            score=None,
            submitted=False
        )

    placeholders = ",".join("?" * len(q_ids))
    cur.execute(
        f"SELECT * FROM mock_questions WHERE id IN ({placeholders})",
        q_ids
    )
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

    # ---------- EVALUATE ----------
    if request.method == "POST":
        submitted = True
        score = 0

        for q in questions:
            selected = request.form.get(f"q{q['id']}")
            q["selected"] = selected

            if selected and selected.strip() == q["answer"].strip():
                score += 1

        # Reset for next attempt
        session.pop("mock_q_ids", None)

    return render_template(
        "mocktest.html",
        questions=questions,
        score=score,
        submitted=submitted
    )

# ---------------- OTHER PAGES ----------------

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/coding")
def coding():
    return render_template("coding.html")

# ---------------- RUN ----------------

if __name__ == "__main__":
    app.run(debug=True)
