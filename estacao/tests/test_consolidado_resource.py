import json


CONSOLIDADO_URN = '/api/v0/consolidado/2020-01-01/2020-02-20/'


class TestConsolidado:
    def test_uri_status_code(self, client, consolidado, users, auth_header):
        response = client.get(CONSOLIDADO_URN, headers=auth_header)
        assert response.status_code == 200

    def test_uri_response_exists(self, client, consolidado, users, auth_header):
        response = client.get(CONSOLIDADO_URN, headers=auth_header)
        data = json.loads(response.data)
        assert len(data) == 1

    def test_uri_response_empty(self, client, users,  consolidado, auth_header):
        urn = '/api/v0/consolidado/2020-10-01/2020-12-20/'
        response = client.get(urn, headers=auth_header)
        data = json.loads(response.data)
        assert len(data.get('consolidado')) == 0

    def test_uri_reponse_data_value(self, client, users, consolidado, auth_header):
        response = client.get(CONSOLIDADO_URN, headers=auth_header)
        data = json.loads(response.data)
        assert data['consolidado'][0]['vis'] == 34
