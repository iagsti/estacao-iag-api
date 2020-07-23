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
    def test_has_get_conditions_attribute(self, current_conditions):
        assert hasattr(current_conditions, 'get_conditions')

    def test_has_model_attribute(self, current_conditions):
        assert hasattr(current_conditions, 'model')

    def test_model_instance(self, current_conditions, consolidado):
        assert isinstance(current_conditions.model(), Consolidado)

    def test_load_data(self, current_conditions):
        self.make_consolidado()
        current_values = ('tipob', 12, 'tipom', 'tipoa')
        current_conditions.load_data()
        response = current_conditions.data
        for expected in current_values:
            assert expected in response

    def test_get_conditions_data_type(self, current_conditions):
        self.make_consolidado()
        resp = current_conditions.get_conditions()
        assert isinstance(resp, dict)

    def test_to_dict(self, current_conditions):
        self.make_consolidado()
        current_conditions.load_data()
        current_conditions.to_dict()
        assert isinstance(current_conditions.data, dict)

    def test_get_conditions(self, current_conditions):
        self.make_consolidado()
        expected = dict(tipob='tipob', vis=34, tipom='tipom',
                        tipoa='tipoa')
        resp = current_conditions.get_conditions()
        for item in expected.keys():
            assert expected.get(item) == resp.get(item)

    def make_consolidado(self):
        date = datetime.now()
        consolidado = factories.consolidado_factory(1, date, date)
        consolidado[0].save()
