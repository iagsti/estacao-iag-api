from flask import jsonify
from flask_restful import Resource

from estacao.models import Consolidado


class ConsolidadoResource(Resource):
    def get(self):
        data = Consolidado.query.all()
        return jsonify(
            {"consolidado": [consolidado.to_dict() for consolidado in data]}
        )
