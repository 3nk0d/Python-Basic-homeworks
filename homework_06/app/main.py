from flask import Flask, render_template, request
from models import db, PG_CONN_URI, Post, User
from flask_migrate import Migrate

app = Flask(__name__)

app.config.update(SQLALCHEMY_DATABASE_URI=PG_CONN_URI, SQLALCHEMY_ECHO=True)

db.init_app(app)

migrate = Migrate(app, db)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/create_record/", methods=["GET", "POST"])
def create_record():
    #from data import users, posts
    # for item in users:
    #    user = User(id=item.get("id"), name=item.get("name"), username=item.get("username"), email=item.get("email"))
    #    print(user)
    #    db.session.add(user)
    #    db.session.commit()
    # for item in posts:
    #    post = Post(id=item.get("id"), user_id=item.get("userId"), title=item.get("title"), body=item.get("body"))
    #    db.session.add(post)
    #    db.session.commit()
    if request.method == "GET":
        print("get")
        return render_template("create_record.html")

    input_id = request.form.get('input_id')
    user_id = request.form.get('user_id')
    title = request.form.get('title')
    body = request.form.get('body')
    post = Post(id=input_id, user_id=user_id, title=title, body=body)

    db.session.add(post)
    db.session.commit()

    return render_template("create_record.html")


@app.route("/create_user/", methods=["GET", "POST"])
def create_user():
    if request.method == "GET":
        return render_template("create_user.html")

    input_id = request.form.get('input_id')
    name = request.form.get('name')
    username = request.form.get('username')
    email = request.form.get('email')
    user = User(id=input_id, name=name, username=username, email=email)

    db.session.add(user)
    db.session.commit()

    return render_template("create_user.html")


@app.route("/view_records/")
def view_records():
    posts = Post.query.all()
    return render_template("view_records.html", record=posts)


@app.route("/view_users/")
def view_users():
    posts = User.query.all()
    return render_template("view_users.html", record=posts)


@app.route("/view_record/", methods=["GET", "POST"])
def view_record():
    post = Post()
    if request.method == "POST":
        record_id = request.form.get('requested_id')
        print(record_id)
        post = Post.query.get_or_404(record_id, description=f"Record #{record_id} not found.")
    return render_template("view_record.html", record=post)
