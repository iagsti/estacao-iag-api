from estacao.blueprints.restapi.resources import CurrentConditionsResource
from flask_restful import Resource


class TestCurrentConditionsResource:
    def test_is_resource_instance(self):
        assert isinstance(CurrentConditionsResource(), Resource)
