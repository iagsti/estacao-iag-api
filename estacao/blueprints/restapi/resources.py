from flask import jsonify
from estacao.exceptions.nocontent import abort, NoContentException
from flask_restful import Resource
from flask_httpauth import HTTPBasicAuth

from werkzeug.security import check_password_hash

from estacao.models import Consolidado, Pressao, Users
from estacao.mixins.authentication_mixin import AuthMixin


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user = Users.query.filter_by(login=username).first()
    if not user:
        return jsonify({
            "error": 204,
            "status": "User not found"
        })
    hash_password = user.password
    validated = check_password_hash(hash_password, password)
    return validated


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


class UserResource(Resource, AuthMixin):
    @auth.login_required
    def get(self, login):
        try:
            user = Users.query.filter_by(login=login).first() or abort(204)
            response = jsonify(
                {"user": {"id": user.id, "login": user.login}}
            )
        except NoContentException:
            response = jsonify({
                "user": {},
                "status": 204,
                "message": "User not found"
            })
        return response
