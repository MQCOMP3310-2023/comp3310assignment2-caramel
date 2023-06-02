from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import secrets
# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = secrets.token_hex(32)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurantmenu.db'
    db.init_app(app)

    login_manager = LoginManager() #initialises login_manager
    login_manager.login_view = 'auth.login' #redirect when login is required
    login_manager.init_app(app)
    
    from .models import User
    @login_manager.user_loader
    def load_user(user_id): #reload user object from the user ID 
                            #stored in the session
        # since the user_id is just the primary key of our user 
        # table, use it in the query for the user
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for auth routes in our app
    from .json import json as json_blueprint
    app.register_blueprint(json_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
