from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        user=os.getenv("DB_USER", "eventuser"),
        password=os.getenv("DB_PASSWORD", "event123"),
        database=os.getenv("DB_NAME", "events")
    )

@app.route("/")
def home():
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM events ORDER BY date")
    events = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("index.html", events=events)

@app.route("/add", methods=["POST"])
def add_event():
    name = request.form["name"].strip()
    event_date = request.form["date"]
    venue = request.form["venue"].strip()

    if name and event_date and venue:
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO events (name, date, venue) VALUES (%s, %s, %s)",
            (name, event_date, venue)
        )
        db.commit()
        cursor.close()
        db.close()

    return redirect(url_for("home"))

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
