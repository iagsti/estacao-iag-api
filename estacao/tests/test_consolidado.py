import json


class TestConsolidado:
    def test_status_code(self, client):
        """Status code should be 200"""
        response = client.get('/api/v0/consolidado')
        assert response.status_code == 200

    def test_response_data(self, client, consolidado):
        response = client.get('/api/v0/consolidado')
        data = json.loads(response.data)
        print(data.get('consolidado'))
        assert data['consolidado'][0]['vis'] == 34
