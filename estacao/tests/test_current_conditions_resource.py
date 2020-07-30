import json
from estacao.blueprints.restapi.resources import CurrentConditionsResource
from flask_restful import Resource
from estacao.mixins.authentication_mixin import AuthMixin
from estacao.normalize import Normalize

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

    def test_get_not_authorized(self, client):
        response = client.get(CURRENT_CONDITIONS_API)
        assert response.status_code == 401

    def test_get(self, client, users, consolidado, auth_header):
        response = consolidado.query.order_by(consolidado.data.desc()).first()
        data = response.to_dict()
        expected = self.make_current_conditions(data)
        response = client.get(CURRENT_CONDITIONS_API, headers=auth_header)
        data = json.loads(response.data)
        expected_keys = data.get('current').keys()
        for item in expected_keys:
            assert data.get('current').get(item) == expected.get(item)

    def make_current_conditions(self, data):
        normalize = Normalize()
        float_round = 2
        pressao_hpa = normalize.trans_p(data.get('pressao'), data.get('temp_bar'))
        temp_orvalho = normalize.td(data.get('tseco'), data.get('tumido'), pressao_hpa)
        umidade_relativa = normalize.rh_tw(data.get('tseco'), data.get('tumido'), pressao_hpa)
        current_conditions = {
            'data': data.get('data'),
            'temperatura_ar': round(data.get('tseco'), float_round),
            'temperatura_ponto_orvalho': round(temp_orvalho, float_round),
            'umidade_relativa': round(umidade_relativa, float_round),
            'temperatura_min': round(data.get('tmin'), float_round),
            'temperatura_min_date': data.get('data'),
            'temperatura_max': round(data.get('tmax'), float_round),
            'temperatura_max_date': data.get('data'),
            'visibilidade': 'maior que 50km',
            'vento': round(data.get('vento'), float_round),
            'dir': data.get('dir'),
            'pressao': round(pressao_hpa, float_round),
            'nuvens_baixas': data.get('tipob'),
            'quant_nuvens_baixas': data.get('qtdb'),
            'nuvens_medias': data.get('tipom'),
            'quant_nuvens_medias': data.get('qtdm'),
            'nuvens_altas': data.get('tipoa'),
            'quant_nuvens_altas': data.get('qtda'),
        }
        return current_conditions
