from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def set_sqlalchemy_binds(app):
    if app.config.SQLALCHEMY_DATABASE_USERS_URI:
        app.config['SQLALCHEMY_BINDS'] = {
            'users': app.config.SQLALCHEMY_DATABASE_USERS_URI
        }


def init_app(app):
    set_sqlalchemy_binds(app)
    db.init_app(app)
