from flask import Flask
import config
from extensions import db
from blueprints.auth import bp as auth_bp
from blueprints.q_and_a import bp as qa_bp
from models import UserModel
from flask_migrate import Migrate
app = Flask(__name__)

# bundle the config file
app.config.from_object(config)

db.init_app(app)

migrate = Migrate(app, db)
# register the blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(qa_bp)


# @app.route('/')
# def hello_world():
#     return "Hello"


if __name__ == '__main__':
    app.run(debug=False)
