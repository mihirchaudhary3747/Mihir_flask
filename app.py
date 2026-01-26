import sqlite3
from flask import Flask, render_template,request, redirect, url_for


app = Flask(__name__)


def db_database():
  conn = sqlite3.connect("data.db")
  conn.row_factory=sqlite3.Row
  return conn

def create_table():
  conn = db_database()
  conn.execute("""
      CREATE TABLE IF NOT EXISTS thoughts (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT NOT NULL,
          interest TEXT NOT NULL,
          motivation TEXT NOT NULL
      );
  """)
  conn.commit()
  conn.close()

create_table()


@app.route("/")
def hello_world():
  return render_template('about.html')


@app.route('/motivation', methods=["GET", "POST"])
def mtv():
    if request.method == "POST":
        name = request.form["name"]
        interest = request.form["interest"]
        motivation = request.form["motivation"]

        conn = db_database()
        conn.execute(
            "INSERT INTO thoughts (name, interest, motivation) VALUES (?, ?, ?)",
            (name, interest, motivation)
        )
        conn.commit()
        conn.close()

        return redirect(url_for("hello_world"))
    return render_template("motivation.html")





        
  
  
@app.route("/resume")
def resumepd():
  return render_template('resume.html')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
