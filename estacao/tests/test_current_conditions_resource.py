import json
from estacao.blueprints.restapi.resources import CurrentConditionsResource
from flask_restful import Resource
from estacao.mixins.authentication_mixin import AuthMixin

CURRENT_CONDITIONS_API = '/api/v0/current-conditions'


class TestCurrentConditionsResource:
    def test_is_resource_instance(self):
        assert isinstance(CurrentConditionsResource(), Resource)

    def test_has_authmixin(self):
        assert isinstance(CurrentConditionsResource(), AuthMixin)

    def test_has_get_attribute(self):
        assert hasattr(CurrentConditionsResource, 'get')

    def test_get_status_code(self, client, users, auth_header):
        response = client.get(CURRENT_CONDITIONS_API, headers=auth_header)
        assert response.status_code == 200

