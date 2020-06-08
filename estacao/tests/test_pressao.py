import json

PRESSAO_URN = '/api/v0/pressao/2020-02-01/2020-03-01/'


class TestPressao:
    def test_uri_status_code(self, client):
        response = client.get(PRESSAO_URN)
        assert response.status_code == 200

    def test_uri_data_response(self, client, pressao):
        response = client.get(PRESSAO_URN)
        data = json.loads(response.data)
        print(data.get('pressao'))
        assert len(data.get('pressao')) == 1

    def test_uri_data_response_value(self, client):
        response = client.get(PRESSAO_URN)
        data = json.loads(response.data)
        assert data.get('pressao')[0].get('pressao') == 192.5

    def test_uri_data_response_empty(self, client):
        response = client.get('/api/v0/pressao/2020-01-01/2020-01-02/')
        data = json.loads(response.data)
        assert len(data.get('pressao')) == 0
