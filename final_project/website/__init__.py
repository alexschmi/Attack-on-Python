from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='AttackOnPython'

    from .views import views
    from .auth import auth
#    from .database import Database

    app.register_blueprint(views, url_prefix = '/')
    app.register_blueprint(auth, url_prefix = '/')

    return app
