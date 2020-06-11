from flask import jsonify
from flask_restful import Resource


from estacao.models import Consolidado, Pressao, Users


class ConsolidadoResource(Resource):
    def get(self, date_from, date_to):
        date_interval = Consolidado.data.between(date_from, date_to)
        query = Consolidado.query.filter(date_interval)
        data = query.all()
        return jsonify(
            {"consolidado": [consolidado.to_dict() for consolidado in data]}
        )


class PressaoResource(Resource):
    def get(self, date_from, date_to):
        date_interval = Pressao.data.between(date_from, date_to)
        query = Pressao.query.filter(date_interval)
        data = query.all()
        return jsonify(
            {"pressao": [pressao.to_dict() for pressao in data]}
        )


class UserResource(Resource):
    def get(self, login):
        user = Users.query.filter_by(login=login).first()
        return jsonify(
            {"user": user.to_dict()}
        )
