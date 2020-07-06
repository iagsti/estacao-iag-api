from flask_restful import Resource
from estacao.blueprints.restapi.resources import TemperaturaMaxResource
from estacao.mixins.authentication_mixin import AuthMixin


TEMPERATURA_MAX_URI = '/api/v0/temperatura-max/2017-01-01/2019-12-01'


class TestTemperaturaMax:
    def test_instance(self):
        assert isinstance(TemperaturaMaxResource(), Resource)

    def test_is_instance_of_auth_mixin(self):
        assert isinstance(TemperaturaMaxResource(), AuthMixin)

    def test_has_get_attribute(self):
        assert hasattr(TemperaturaMaxResource(), 'get')


class TestTemperaturaMaxGet:
    def test_status_code(self, client, auth_header):
        response = client.get(TEMPERATURA_MAX_URI, headers=auth_header)
        assert response.status_code == 200

    def test_access_not_authorized(self, client):
        response = client.get(TEMPERATURA_MAX_URI)
        assert response.status_code == 401

    def test_temperatura_max_response(self, consolidado, client, auth_header):
        response = client.get(TEMPERATURA_MAX_URI, headers=auth_header)
        expected = {
            'temp_max': [
                {'data': '2018-01-01 13:48:10', 'temp': 50}
            ]
        }
        assert response.json == expected
