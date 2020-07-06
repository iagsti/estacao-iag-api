from estacao.blueprints.restapi.resources import TemperaturaMinResource
from flask_restful import Resource
from estacao.mixins.authentication_mixin import AuthMixin


TEMPERATURA_MIN_URI = '/api/v0/temperatura-min/2017-01-01/2019-12-01'


class TestTemperaturaMin:
    def test_instance(self):
        assert isinstance(TemperaturaMinResource(), Resource)

    def test_is_instance_of_auth_mixin(self):
        assert isinstance(TemperaturaMinResource(), AuthMixin)

    def test_has_get_attribute(self):
        assert hasattr(TemperaturaMinResource(), 'get')


class TestTemperaturaMinGet:
    def test_status_code(self, client, consolidado, auth_header):
        response = client.get(TEMPERATURA_MIN_URI, headers=auth_header)
        assert response.status_code == 200

    def test_response_body(self, client, auth_header):
        response = client.get(TEMPERATURA_MIN_URI, headers=auth_header)
        expected = {
            'temp_min': [
                {'data': '2018-01-01 13:48:10', 'temp': 12.0}
            ]
        }
        assert response.json == expected

    def test_temperatura_min_require_authentication(self, client, auth_header):
        response = client.get(TEMPERATURA_MIN_URI)
        assert response.status_code == 401
