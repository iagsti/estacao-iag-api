from flask import Blueprint
from flask_restful import Api


from .resources import ConsolidadoResource, PressaoResource


bp = Blueprint('restapi', __name__, url_prefix='/api/v0')
api = Api(bp)


def init_app(app):
    api.add_resource(ConsolidadoResource, '/consolidado/<string:date_from>/<string:date_to>/')
    api.add_resource(PressaoResource, '/pressao/<string:date_from>/<string:date_to>/')
    app.register_blueprint(bp)
