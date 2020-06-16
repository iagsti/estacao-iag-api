import json
from estacao.blueprints.restapi.resources import UserResource
from flask_restful import Resource


USER_URI = '/api/v0/user/login_test/'


class TestUserResource:
    def test_is_instance(self, user_resource):
        assert isinstance(user_resource, UserResource)
        assert isinstance(user_resource, Resource)

    def test_has_get_attribute(self):
        assert hasattr(UserResource, 'get')


class TestUserEndPoint:
    def test_status_code(self, client, auth_header):
        response = client.get(USER_URI, headers=auth_header)
        assert response.status_code == 200

    def test_response_data(self, client, users, auth_header):
        response = client.get(USER_URI, headers=auth_header)
        data = json.loads(response.data)
        assert data.get('user').get('login') == 'login_test'

    def test_user_not_exists(self, client, auth_header):
        uri = '/api/v0/user/login_not_exists/'
        response = client.get(uri, headers=auth_header)
        data = json.loads(response.data)
        assert data.get('message') == 'User not found'
        assert data.get('status') == 204

    def test_not_show_password(self, client, auth_header):
        response = client.get('/api/v0/user/login_test/', headers=auth_header)
        data = json.loads(response.data)
        assert data.get('user').get('password') is None




































