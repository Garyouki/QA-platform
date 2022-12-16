from flask import Blueprint, request, render_template, g, redirect, url_for
from extensions import db
from models import QuestionModel
from .forms import QuestionForm
from decorators import login_required

bp = Blueprint("qa", __name__, url_prefix="/")


@bp.route("/")
def index():
    # sort the questions in descending time order
    questions = QuestionModel.query.order_by(
        QuestionModel.create_time.desc()).all()
    return render_template("index.html", questions=questions)


@bp.route("/qa/public", methods=['GET', 'POST'])
@login_required
def public_question():

    if request.method == 'GET':
        return render_template("public_question.html")
    else:
        form = QuestionForm(request.form)
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(
                title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect("/")
        else:
            return redirect(url_for("qa.public_question"))