import json
from estacao.blueprints.restapi.resources import UmidadeResource
from flask_restful import Resource


UMIDADE_URN = '/api/v0/umidade/2020-01-01/2020-03-01/'


class TestResource:
    def test_resource_instance(self, umidade_resource):
        assert isinstance(umidade_resource, UmidadeResource)
        assert isinstance(umidade_resource, Resource)

    def test_has_attribute_get(self, umidade_resource):
        assert hasattr(umidade_resource, 'get')

    def test_status_code(self, client, auth_header):
        response = client.get(UMIDADE_URN, headers=auth_header)
        assert response.status_code == 200

    def test_response_has_data(self, umidade, client, auth_header):
        response = client.get(UMIDADE_URN, headers=auth_header)
        data = json.loads(response.data)
        assert len(data.get('umidade')) == 1

    def test_response_value(self, umidade, client, auth_header):
        response = client.get(UMIDADE_URN, headers=auth_header)
        data = json.loads(response.data)
        assert data.get('umidade')[0].get('ur') == 80.4

    def test_status_code_unauthorized(self, client):
        response = client.get(UMIDADE_URN)
        assert response.status_code == 401
