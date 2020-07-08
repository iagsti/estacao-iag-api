from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
tablename = 'consolidado'


def get_consolidado_tablename(app):
    return app.config.CONSOLIDADO_TABLENAME


def set_sqlalchemy_binds(app):
    if app.config.SQLALCHEMY_DATABASE_USERS_URI:
        app.config['SQLALCHEMY_BINDS'] = {
            'users': app.config.SQLALCHEMY_DATABASE_USERS_URI
        }


def init_app(app):
    global tablename
    if get_consolidado_tablename(app):
        tablename = get_consolidado_tablename(app)
    set_sqlalchemy_binds(app)
    db.init_app(app)
