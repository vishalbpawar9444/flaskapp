from flask import Flask, request, jsonify, render_template_string
import pymysql

app = Flask(__name__)

# MySQL (Docker on same EC2)
DB_HOST = "mysql"
DB_USER = "root"
DB_PASSWORD = "root123"
DB_NAME = "mydb"
DB_PORT = 3306  # MUST be int

def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=False
    )

# HTML FORM TEMPLATE
form_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Add Employee</title>
</head>
<body>
    <h2>Add Employee</h2>

    <form action="/addform" method="post">
        <label>Name:</label><br>
        <input type="text" name="name" required><br><br>

        <label>Email:</label><br>
        <input type="email" name="email" required><br><br>

        <label>Salary:</label><br>
        <input type="number" name="salary" required><br><br>

        <button type="submit">Add Employee</button>
    </form>

    <br><br>
    <a href="/employees">View All Employees</a>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(form_html)

@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()
    return jsonify(rows)

@app.route('/addform', methods=['POST'])
def addform():
    name = request.form.get("name")
    email = request.form.get("email")
    salary = request.form.get("salary")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, email, salary) VALUES (%s, %s, %s)",
        (name, email, salary)
    )
    conn.commit()
    conn.close()

    return f"""
    <h3>Employee {name} added successfully!</h3>
    <br>
    <a href="/">Back to Form</a>
    """

@app.route('/add', methods=['POST'])
def add_employee():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    name = data.get("name")
    email = data.get("email")
    salary = data.get("salary")

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, email, salary) VALUES (%s, %s, %s)",
        (name, email, salary)
    )
    conn.commit()
    conn.close()

    return jsonify({"message": "Employee added successfully"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

