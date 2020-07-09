from flask import jsonify
from estacao.exceptions.nocontent import abort, NoContentException
from flask_restful import Resource


from estacao.models import Consolidado, Pressao, Users, Umidade
from estacao.mixins.authentication_mixin import AuthMixin, auth
from estacao.repositories import TemperaturaRepository


class ConsolidadoResource(Resource, AuthMixin):
    @auth.login_required
    def get(self, date_from, date_to):
        date_interval = Consolidado.data.between(date_from, date_to)
        query = Consolidado.query.filter(date_interval)
        data = query.all()
        return jsonify(
            {"consolidado": [consolidado.to_dict() for consolidado in data]}
        )


class PressaoResource(Resource, AuthMixin):
    @auth.login_required
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


class UmidadeResource(Resource, AuthMixin):
    @auth.login_required
    def get(self, date_from, date_to):
        date_interval = Umidade.data.between(date_from, date_to)
        query = Umidade.query.filter(date_interval)
        data = query.all()
        return jsonify({"umidade": [umidade.to_dict() for umidade in data]})


class TemperaturaMinResource(Resource, AuthMixin):
    @auth.login_required
    def get(self, start_date, end_date):
        repository = TemperaturaRepository()
        data = repository.get_temperatura_min(start_date, end_date)
        return jsonify({'temp_min': [{'data': str(tempmin[0]), 'temp': tempmin[1]} for tempmin in data]})


class TemperaturaMaxResource(Resource, AuthMixin):
    @auth.login_required
    def get(self, start_date, end_date):
        repository = TemperaturaRepository()
        data = repository.get_temperatura_max(start_date, end_date)
        return jsonify({'temp_max': [{'data': str(tempmax[0]), 'temp': tempmax[1]} for tempmax in data]})
