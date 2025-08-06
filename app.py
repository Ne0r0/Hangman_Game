import secrets
from flask import Flask
from models import db
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from routes import routes


app = Flask(__name__)
app.config["SECRET_KEY"] = secrets.token_urlsafe(16)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Mail config
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True

db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)

login_manager.login_view = 'routes.login' # type: ignore
app.register_blueprint(routes)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)