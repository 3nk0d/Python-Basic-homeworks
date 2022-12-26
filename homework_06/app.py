from flask import Flask, render_template
from fill_db import main
#from sql import read, read_user, read_record
from functions import view_records_users

main()
#read()
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_records/")
def create_records():
    return render_template("create_records.html")


@app.route("/view_records/")
def view_records():
    return render_template("view_records.html", record=view_records_users())
    #record=["record_1", "record_2"])
