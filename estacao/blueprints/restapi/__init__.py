from flask import Blueprint
from flask_restful import Api


from .resources import (ConsolidadoResource, PressaoResource,
                        UserResource, UmidadeResource, TemperaturaMinResource)


bp = Blueprint('restapi', __name__, url_prefix='/api/v0')
api = Api(bp)


def init_app(app):
    api.add_resource(UserResource, '/user/<string:login>/')
    api.add_resource(ConsolidadoResource, '/consolidado/<string:date_from>/<string:date_to>/')
    api.add_resource(PressaoResource, '/pressao/<string:date_from>/<string:date_to>/')
    api.add_resource(UmidadeResource, '/umidade/<string:date_from>/<string:date_to>/')
    api.add_resource(TemperaturaMinResource, '/temperatura-min/<string:start_date>/<string:end_date>')
    app.register_blueprint(bp)
