from .forms import RegisterFrom, LoginForm
from random import random
from flask import Blueprint, render_template, session
from extensions import mail, db
from flask_mail import Message
from flask import request, jsonify, redirect, url_for
import string
import random
from werkzeug.security import generate_password_hash, check_password_hash
from models import EmailCaptchaModel, UserModel

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                return redirect(url_for("auth.login"))
            if check_password_hash(user.password, password):
                # The data in the session is stored on the cookies
                # and signed by the server cryptographically.
                session['user_id'] = user.id
                return redirect("/")
            else:
                return redirect(url_for("auth.login"))
        else:
            return redirect(url_for("auth.login"))


@bp.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template("register.html")
    else:
        # verifiy the verification code matched with the input
        form = RegisterFrom(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            # encrypt user's password for data privacy
            user = UserModel(email=email, username=username,
                             password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            # after sign up successfully, redirect the the login page
            return redirect(url_for("auth.login"))
        else:
            return redirect(url_for("auth.register"))


@bp.route("/logout")
# logout, clear the info in cookie
def logout():
    session.clear()
    return redirect("/")


# This method is letting clients to receive captcha
@bp.route("/captcha/email")
def get_email_captcha():
    email = request.args.get("email")
    # randomly get four digits from library string.digits
    # use string.digits * 4 in order to create 4 0123456789 together
    # if we don't times 4 then the next digit will be selected
    # from 9 digit instead of 10
    source = string.digits * 4
    # choose 4 unique digit from the source
    captcha = random.sample(source, 4)
    captcha = "".join(captcha)
    message = Message(subject="QA platform signup verification code", recipients=[
                      email], body=f"The verification code is:{captcha}")
    mail.send(message)

    # store the information into the database
    email_verification_code = EmailCaptchaModel(email=email, captcha=captcha)
    db.session.add(email_verification_code)
    db.session.commit()
    return jsonify({"code": 200, "message": "", "data": None})
