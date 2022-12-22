from flask import Flask, render_template
from fill_db import main, Session

main()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_records/")
def create_records():
    return render_template("create_records.html")


@app.route("/view_records/")
def view_records():
    return render_template("view_records.html", record = "record_1")
