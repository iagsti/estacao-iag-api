from estacao.repositories import TemperaturaRepository
from datetime import datetime
from estacao.ext import factories
from estacao.models import Consolidado


class TestTemperaturaMinRepository:
    def test_instance(self):
        assert isinstance(TemperaturaRepository(), TemperaturaRepository)

    def test_has_get_temperatura_min_attribute(self):
        assert hasattr(TemperaturaRepository(), 'get_temperatura_min')

    def test_temperatura_min(self, consolidado):
        repository = TemperaturaRepository()
        temperatura_min = repository.get_temperatura_min('2017-12-31', '2018-02-01')
        expected = [(datetime(2018, 1, 1, 13, 48, 10), 12.0, 12.0)]
        assert expected == temperatura_min


class TestTemperaturaMaxRepository:
    def test_has_get_temperatura_max_attribute(self):
        assert hasattr(TemperaturaRepository(), 'get_temperatura_max')

    def test_temperatura_min(self, consolidado):
        repository = TemperaturaRepository()
        temepratura_max = repository.get_temperatura_max('2017-12-31', '2018-02-01')
        expected = [(datetime(2018, 1, 1, 13, 48, 10), 50.0, 50.0)]
        assert expected == temepratura_max


class TestCurrentConditionsRepository:
    def test_has_model_attribute(self, current_conditions):
        assert hasattr(current_conditions, 'model')

    def test_model_instance(self, current_conditions, consolidado):
        assert isinstance(current_conditions.model(), Consolidado)
