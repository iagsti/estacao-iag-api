from estacao.mixins.authentication_mixin import AuthMixin
from estacao.models import Users


class TestAuthentication:
    def test_get_user_by_login(self, users):
        auth = AuthMixin()
        user = auth.get_user_by_login('login_test')
        assert user.login == 'login_test'

    def test_get_user_by_login_not_found(self):
        auth = AuthMixin()
        assert not auth.get_user_by_login('not_exists')

    def test_check_password(self, users):
        auth = AuthMixin()
        user = Users.query.filter_by(login='login_test').first()
        assert auth.check_password(user.password, '12345')

    def test_check_password_invalid(self):
        auth = AuthMixin()
        user = Users.query.filter_by(login='login_test').first()
        assert not auth.check_password(user.password, 'wrong_password')
