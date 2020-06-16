import json

PRESSAO_URN = '/api/v0/pressao/2020-02-01/2020-03-01/'


def make_request(uri, client, headers):
    response = client.get(uri, headers=headers)
    data = json.loads(response.data)
    return data


class TestPressao:
    def test_uri_status_code(self, client, pressao, auth_header):
        response = client.get(PRESSAO_URN, headers=auth_header)
        assert response.status_code == 200

    def test_uri_data_response(self, client, pressao, auth_header):
        data = make_request(PRESSAO_URN, client=client, headers=auth_header)
        assert len(data.get('pressao')) == 1

    def test_uri_data_response_value(self, client, pressao, auth_header):
        data = make_request(PRESSAO_URN, client=client, headers=auth_header)
        assert data.get('pressao')[0].get('pressao') == 192.5

    def test_uri_data_response_empty(self, client, pressao, auth_header):
        uri = '/api/v0/pressao/2020-01-01/2020-01-01/'
        data = make_request(uri, client=client, headers=auth_header)
        assert len(data.get('pressao')) == 0
