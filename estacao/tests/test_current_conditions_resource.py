from estacao.blueprints.restapi.resources import CurrentConditionsResource
from flask_restful import Resource
from estacao.mixins.authentication_mixin import AuthMixin


class TestCurrentConditionsResource:
    def test_is_resource_instance(self):
        assert isinstance(CurrentConditionsResource(), Resource)

    def test_has_authmixin(self):
        assert isinstance(CurrentConditionsResource(), AuthMixin)

