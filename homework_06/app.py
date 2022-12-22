from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    render_template("index.html")

@app.route("/create_records/")
def create_records():
    return render_template("create_records.html")

