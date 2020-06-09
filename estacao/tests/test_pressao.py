import json

PRESSAO_URN = '/api/v0/pressao/2020-02-01/2020-03-01/'


def make_request(uri, client):
    response = client.get(uri)
    data = json.loads(response.data)
    return data


class TestPressao:
    def test_uri_status_code(self, client, pressao):
        response = client.get(PRESSAO_URN)
        assert response.status_code == 200

    def test_uri_data_response(self, client, pressao):
        data = make_request(PRESSAO_URN, client=client)
        assert len(data.get('pressao')) == 1

    def test_uri_data_response_value(self, client, pressao):
        data = make_request(PRESSAO_URN, client=client)
        assert data.get('pressao')[0].get('pressao') == 192.5

    def test_uri_data_response_empty(self, client, pressao):
        uri = '/api/v0/pressao/2020-01-01/2020-01-01/'
        data = make_request(uri, client=client)
        assert len(data.get('pressao')) == 0
