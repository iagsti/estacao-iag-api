from flask import Blueprint
from flask_restful import Api


from .resources import ConsolidadoResource


bp = Blueprint('restapi', __name__, url_prefix='/api/v0')
api = Api(bp)


def init_app(app):
    urn = '/consolidado/<string:date_from>/<string:date_to>/'
    api.add_resource(ConsolidadoResource, urn)
    app.register_blueprint(bp)
