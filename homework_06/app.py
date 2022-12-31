from flask import Flask, render_template, request
#from fill_db import main
#from sql import read, read_user, read_record
#from functions import view_records_users
from .models import db, PG_CONN_URI, Post, User
from flask_migrate import Migrate

#main()
#read()
app = Flask(__name__)

app.config.update(SQLALCHEMY_DATABASE_URI=PG_CONN_URI, SQLALCHEMY_ECHO=True)

db.init_app(app)

migrate = Migrate(app, db)

#@app.cli("db_create_all")
#def db_create_all():
    #db.create_all()

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_records/", methods=["GET", "POST"])
def create_records():
    from .data import users, posts
    #for item in posts:
    #    post = Post(id=item.get("id"), user_id=item.get("userId"), title=item.get("title"), body=item.get("body"))
    #    db.session.add(post)
    #    db.session.commit()
    #for item in users:
    #    user = User(id=item.get("id"), name=item.get("name"), username=item.get("username"), email=item.get("email"))
    #    print(user)
    #    db.session.add(user)
    #    db.session.commit()
    if request.method == "GET":
        return render_template("create_records.html", form=form)

    Post(id=item.get("id"), user_id=item.get("userId"), title=item.get("title"), body=item.get("body"))
    db.session.add(post)
    db.session.commit()


@app.route("/view_records/")
def view_records():
    posts = Post.query.all()
    return render_template("view_records.html", record=posts)


@app.route("/view_records/<int:record_id>")
def view_record(record_id):
    post = Post.query.get_or_404(record_id, description=f"Record #{record_id} not found.")
    return render_template("view_record.html", record=post)
