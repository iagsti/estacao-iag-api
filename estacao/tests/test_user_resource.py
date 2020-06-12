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

    def test_post_return_users(self, user_resource, users):
        response = user_resource.get('login_test')
        users = json.loads(response.data)
        assert users.get('user').get('login') == 'login_test'


class TestUserEndPoint:
    def test_status_code(self, client):
        response = client.get(USER_URI)
        assert response.status_code == 200

    def test_response_data(self, client, users):
        response = client.get(USER_URI)
        data = json.loads(response.data)
        assert data.get('user').get('login') == 'login_test'

    def test_user_not_exists(self, client):
        response = client.get('/api/v0/user/login_not_exists/')
        data = json.loads(response.data)
        assert data.get('message') == 'User not found'
        assert data.get('status') == 204

    def test_not_show_password(self, client):
        response = client.get('/api/v0/user/login_test/')
        data = json.loads(response.data)
        assert data.get('user').get('password') is None




































