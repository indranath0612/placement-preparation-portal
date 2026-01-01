from flask import Flask, render_template, request, redirect, session
import sqlite3
from flask import session

app = Flask(__name__)
app.secret_key = "placement_secret"
app.secret_key = "supersecretkey123"

def init_db():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS mock_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        option1 TEXT NOT NULL,
        option2 TEXT NOT NULL,
        option3 TEXT NOT NULL,
        option4 TEXT NOT NULL,
        answer TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

def seed_mock_questions():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM mock_questions")
    count = cur.fetchone()[0]

    if count == 0:
        questions = [

        # ---------------- PYTHON (1–25) ----------------
        ("Which keyword is used to define a function in Python?", "func", "define", "def", "function", "def"),
        ("Which data type is immutable?", "List", "Set", "Tuple", "Dictionary", "Tuple"),
        ("What is the output of len([1,2,3])?", "2", "3", "4", "Error", "3"),
        ("Which symbol is used for comments in Python?", "//", "#", "/* */", "--", "#"),
        ("Which operator is used for exponentiation?", "^", "**", "//", "%", "**"),
        ("Which keyword is used to handle exceptions?", "try", "catch", "error", "exception", "try"),
        ("Which loop executes at least once?", "for", "while", "do-while", "foreach", "do-while"),
        ("What does PEP stand for?", "Python Extension Proposal", "Python Enhancement Proposal", "Program Execution Plan", "None", "Python Enhancement Proposal"),
        ("Which method is a constructor in Python?", "__init__", "__new__", "__create__", "__build__", "__init__"),
        ("Which method is a destructor?", "__delete__", "__free__", "__del__", "__remove__", "__del__"),
        ("Which keyword creates a class?", "class", "struct", "define", "object", "class"),
        ("Which keyword exits a loop?", "stop", "break", "exit", "end", "break"),
        ("Which function converts string to int?", "str()", "float()", "int()", "chr()", "int()"),
        ("Which collection allows duplicates?", "Set", "Dictionary", "List", "Tuple", "List"),
        ("Which keyword is used to inherit a class?", "extends", "inherits", "super", "class", "class"),
        ("What is the output of bool(0)?", "True", "False", "None", "Error", "False"),
        ("Which module supports regular expressions?", "math", "regex", "re", "pyregex", "re"),
        ("Which keyword is used for anonymous functions?", "lambda", "def", "anon", "func", "lambda"),
        ("Which function reads input from user?", "read()", "input()", "scan()", "get()", "input()"),
        ("Which type stores key-value pairs?", "List", "Tuple", "Dictionary", "Set", "Dictionary"),
        ("Which function returns ASCII value?", "ord()", "chr()", "ascii()", "val()", "ord()"),
        ("Which function converts ASCII to char?", "ord()", "chr()", "char()", "ascii()", "chr()"),
        ("Which keyword checks membership?", "in", "has", "exists", "contains", "in"),
        ("Which function sorts a list?", "sort()", "order()", "arrange()", "sorted()", "sort()"),
        ("Which exception occurs when index is invalid?", "KeyError", "IndexError", "ValueError", "TypeError", "IndexError"),

        # ---------------- DSA (26–50) ----------------
        ("Which data structure follows FIFO?", "Stack", "Queue", "Tree", "Graph", "Queue"),
        ("Which data structure follows LIFO?", "Queue", "Stack", "Array", "Tree", "Stack"),
        ("Which DS is used for recursion?", "Queue", "Array", "Stack", "Linked List", "Stack"),
        ("Which is a linear data structure?", "Tree", "Graph", "Array", "Heap", "Array"),
        ("Which sorting is fastest on average?", "Bubble", "Selection", "Merge", "Insertion", "Merge"),
        ("Which sorting is in-place?", "Merge", "Quick", "Heap", "Bubble", "Bubble"),
        ("Which traversal is DFS?", "Queue based", "Stack based", "Level order", "Breadth", "Stack based"),
        ("Binary Search works on?", "Any array", "Sorted array", "Unsorted array", "List", "Sorted array"),
        ("Worst case of binary search?", "O(1)", "O(n)", "O(log n)", "O(n log n)", "O(log n)"),
        ("Worst case of linear search?", "O(log n)", "O(1)", "O(n)", "O(n log n)", "O(n)"),
        ("Which DS uses nodes?", "Array", "Stack", "Linked List", "Queue", "Linked List"),
        ("Which DS is non-linear?", "Array", "Stack", "Queue", "Tree", "Tree"),
        ("Which traversal prints root first?", "Inorder", "Postorder", "Preorder", "Level", "Preorder"),
        ("Which traversal prints root last?", "Preorder", "Inorder", "Postorder", "Level", "Postorder"),
        ("Which DS uses priority?", "Queue", "Stack", "Priority Queue", "Array", "Priority Queue"),
        ("Hashing improves?", "Memory", "Speed", "Accuracy", "Security", "Speed"),
        ("Collision occurs in?", "Array", "Queue", "Hash Table", "Tree", "Hash Table"),
        ("Balanced BST height?", "O(n)", "O(log n)", "O(1)", "O(n log n)", "O(log n)"),
        ("Which DS is used in BFS?", "Stack", "Queue", "Tree", "Heap", "Queue"),
        ("Which DS is used in DFS?", "Queue", "Stack", "Graph", "Array", "Stack"),
        ("Which sorting is stable?", "Quick", "Heap", "Merge", "Selection", "Merge"),
        ("Time complexity of merge sort?", "O(n)", "O(log n)", "O(n log n)", "O(n²)", "O(n log n)"),
        ("Time complexity of bubble sort?", "O(n)", "O(n log n)", "O(n²)", "O(log n)", "O(n²)"),
        ("Which DS supports recursion?", "Queue", "Stack", "Array", "Tree", "Stack"),
        ("Which DS uses key-value?", "Array", "Hash Table", "Stack", "Queue", "Hash Table"),

        # ---------------- OS / DB / CN (51–100) ----------------
        ("Which OS is open source?", "Windows", "Linux", "macOS", "DOS", "Linux"),
        ("Which OS supports multitasking?", "DOS", "Linux", "CP/M", "None", "Linux"),
        ("What is a process?", "Program in execution", "Compiled code", "Thread", "File", "Program in execution"),
        ("What is a thread?", "Lightweight process", "Heavy process", "Kernel", "Program", "Lightweight process"),
        ("Which memory is volatile?", "ROM", "RAM", "HDD", "SSD", "RAM"),
        ("Which DB key is unique?", "Foreign key", "Primary key", "Composite key", "Candidate key", "Primary key"),
        ("Which SQL command retrieves data?", "INSERT", "UPDATE", "SELECT", "DELETE", "SELECT"),
        ("Which SQL removes table?", "DROP", "DELETE", "REMOVE", "TRUNCATE", "DROP"),
        ("Which normal form removes redundancy?", "1NF", "2NF", "3NF", "BCNF", "3NF"),
        ("Which join returns matching rows?", "Left", "Right", "Full", "Inner", "Inner"),
        ("Which protocol is used for web?", "FTP", "SMTP", "HTTP", "SNMP", "HTTP"),
        ("Which protocol sends emails?", "FTP", "SMTP", "HTTP", "POP", "SMTP"),
        ("Which layer is transport layer?", "Layer 1", "Layer 2", "Layer 4", "Layer 7", "Layer 4"),
        ("Which protocol is secure?", "HTTP", "HTTPS", "FTP", "SMTP", "HTTPS"),
        ("Which port does HTTP use?", "21", "22", "80", "443", "80"),
        ("Which port does HTTPS use?", "21", "80", "443", "22", "443"),
        ("Which address identifies device?", "IP", "MAC", "Port", "Socket", "IP"),
        ("Which device routes packets?", "Hub", "Switch", "Router", "Repeater", "Router"),
        ("Which layer handles encryption?", "Application", "Transport", "Session", "Presentation", "Presentation"),
        ("Which protocol is connection-oriented?", "UDP", "TCP", "IP", "ICMP", "TCP"),
        ("Which protocol is faster?", "TCP", "UDP", "FTP", "HTTP", "UDP"),
        ("Which SQL constraint avoids null?", "UNIQUE", "NOT NULL", "PRIMARY", "CHECK", "NOT NULL"),
        ("Which DB stores rows?", "NoSQL", "Relational", "Graph", "Key-value", "Relational"),
        ("Which DB stores documents?", "SQL", "MongoDB", "MySQL", "Postgres", "MongoDB"),
        ("Which OS manages hardware?", "Compiler", "Kernel", "Shell", "BIOS", "Kernel"),
        ]

        cur.executemany("""
        INSERT INTO mock_questions
        (question, option1, option2, option3, option4, answer)
        VALUES (?, ?, ?, ?, ?, ?)
        """, questions)

        conn.commit()

    conn.close()

init_db()
seed_mock_questions()



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

    # ---------- GET: pick random questions ONCE ----------
    if request.method == "GET":
        cur.execute("""
            SELECT id FROM mock_questions
            ORDER BY RANDOM()
            LIMIT 10
        """)
        q_ids = [row["id"] for row in cur.fetchall()]
        session["mock_q_ids"] = q_ids

    # ---------- FETCH SAME QUESTIONS ----------
    q_ids = session.get("mock_q_ids", [])

    if not q_ids:
        return render_template(
            "mocktest.html",
            questions=[],
            score=None,
            submitted=False
        )

    placeholders = ",".join("?" for _ in q_ids)
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

    # ---------- POST: evaluate SAME QUESTIONS ----------
    if request.method == "POST":
        submitted = True
        score = 0

        for q in questions:
            selected = request.form.get(f"q{q['id']}")
    q["selected"] = selected

    if selected and selected.strip() == q["answer"].strip():
        score += 1
        q["selected"] = selected

        if selected and selected.strip() == q["answer"].strip():
                score += 1

        # Clear session so next test gets new questions
        session.pop("mock_q_ids", None)

    return render_template(
        "mocktest.html",
        questions=questions,
        score=score,
        submitted=submitted
    )




if __name__ == "__main__":
    app.run(debug=True)
