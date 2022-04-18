import secrets, os
from PIL import Image
from flask import render_template, flash, redirect, url_for, request
from makememe import app, db, bcrypt
from makememe.forms import RegistrationForm, LoginForm, UpdateAccountForm
from makememe.models import Users, Post, Meme, Feedback
from makememe.make import make
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if current_user.is_authenticated:
        user = Users.query.filter_by(id=current_user.id).first()
        authenticated = True
        is_beta = user.is_beta
        if request.method == "POST":
            description = request.form["description"]
            meme = make(description, current_user.id)
        else:
            meme = {
                "meme": "default.png",
            }
    else:
        is_beta = False
        authenticated = False
        meme = {
            "meme": "default.png",
        }
    image_file = url_for("static", filename=meme["meme"])

    return render_template(
        "home.html", image_file=image_file, authenticated=authenticated
    )


@app.route("/tutorial")
def tutorial():
    return render_template(
        "tutorial.html", title="tutorial", authenticated=current_user.is_authenticated
    )


@app.route("/about")
def about():
    return render_template("about.html", title="about")


@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        feedback = Feedback(
            description=request.form["description"], user_id=current_user.id
        )
        db.session.add(feedback)
        db.session.commit()
    return render_template("feedback.html", title="feedback")


@app.route("/blog")
def blog():
    return render_template("blog.html", title="blog")


@app.route("/technology")
def technology():
    return render_template("technology.html", title="technology")


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode(
            "utf-8"
        )
        user = Users(
            username=form.username.data, email=form.email.data, password=hashed_password
        )
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get("next")

            return redirect(next_page) if next_page else redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check email and password", "danger")
    return render_template("login.html", title="Login", form=form)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    logout_user()
    return redirect(url_for("home"))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, "static/profile_pics", picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


@app.route("/account", methods=["GET", "POST"])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your account has been updated!", "success")
        return redirect(url_for("account"))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for("static", filename="profile_pics/" + current_user.image_file)
    return render_template(
        "account.html", title="Account", image_file=image_file, form=form
    )
