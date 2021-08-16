from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

# Database instances
db = SQLAlchemy()
DB_NAME = 'database.db'

# Create flask application 
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'gonzo'
    app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from .views import views
    from .auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
# Import models.py
    from .models import User

# Call create_database
    create_database(app)
    
# Log in manager
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
# Access user model when loggin in 
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app

# Create database
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created database!')
        