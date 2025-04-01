from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user
from flask_migrate import Migrate
from os import path

app = Flask(__name__)
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app.config['SECRET_KEY'] = 'mW_CFB.!r3jHWVnQEKnU' #TODO: Change this to import from 1password
    app.config['SQLALCHEMY_DATABASE_URI'] = F'sqlite:///{DB_NAME}'
    app.config["UPLOAD_FOLDER"] = r"C:\Users\Lucca Augusto\Downloads\imagens_copa_bagres"
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Usuario, Time, Jogador
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Usuario.query.get(int(id))

    return app

def create_database(app):
    # if not path.exists(f"website/{DB_NAME}"):
        with app.app_context():
            db.drop_all()
            db.create_all()
            print("Banco de dados criado!")
