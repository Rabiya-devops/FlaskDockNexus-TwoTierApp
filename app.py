from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        message = "Database Connected Successfully ✔"
    except:
        message = "Database Connection Failed ❌"

    return render_template("index.html", msg=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
