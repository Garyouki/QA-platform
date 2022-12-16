from flask import Flask, session, g
import config
from extensions import db, mail
from blueprints.auth import bp as auth_bp
from blueprints.qa import bp as qa_bp
from models import UserModel
from flask_migrate import Migrate
app = Flask(__name__)

# bundle the config file
app.config.from_object(config)

# initialize databse
db.init_app(app)

# initialize mail (Flask-Mail)
mail.init_app(app)

migrate = Migrate(app, db)
# register the blueprint
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)


@app.before_request
def my_before_request():
    # store the user_id
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g, "user", user)
    else:
        setattr(g, "user", None)


@app.context_processor
def my_context_processor():
    # after the user sign in, this user name should be seen in the nav bar
    return {"user": g.user}


if __name__ == '__main__':
    app.run(debug=False)
