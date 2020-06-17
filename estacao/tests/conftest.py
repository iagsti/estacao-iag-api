import pytest
import base64
from estacao.app import create_app, minimal_app
from estacao.blueprints.restapi.resources import UserResource, UmidadeResource
from estacao.ext.database import db
from estacao.ext.commands import populate_db, populate_pressao, populate_users
from estacao.ext.commands import populate_umidade


@pytest.fixture(scope="session")
def min_app():
    app = minimal_app(FORCE_ENV_FOR_DYNACONF="testing")
    return app


@pytest.fixture(scope="session")
def app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():
        db.create_all(app=app)
        yield app
        db.drop_all(app=app)


@pytest.fixture(scope="session")
def auth_header(app):
    with app.app_context():
        credentials = base64.b64encode(b'login_test:12345').decode('utf-8')
        auth_header = {'Authorization': 'Basic {}'.format(credentials)}
        return auth_header


@pytest.fixture(scope="session")
def consolidado(app):
    with app.app_context():
        return populate_db()


@pytest.fixture(scope="session")
def pressao(app):
    with app.app_context():
        return populate_pressao()


@pytest.fixture(scope='session')
def users(app):
    with app.app_context():
        return populate_users()


@pytest.fixture(scope='session')
def user_resource(app):
    with app.app_context():
        return UserResource()


@pytest.fixture(scope='session')
def umidade(app):
    with app.app_context():
        return populate_umidade()


@pytest.fixture(scope='session')
def umidade_resource(app):
    with app.app_context():
        return UmidadeResource()
