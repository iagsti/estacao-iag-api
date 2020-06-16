from estacao.models import Users
from estacao.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class TestConsolidado:
    def test_consolidado_length(self, consolidado):
        assert len(consolidado) == 1

    def test_has_save_attribute(self, consolidado):
        assert hasattr(consolidado[0], 'save')


class TestPressao:
    def test_pressao_length(self, pressao):
        assert len(pressao) == 1

    def test_has_save_attribute(self, pressao):
        assert hasattr(pressao[0], 'save')


class TestUsers:
    def test_user_instances(self, users):
        assert isinstance(users, Users)
        assert isinstance(users, db.Model)
        assert isinstance(users, SerializerMixin)

    def test_users_has_attributes(self, users):
        assert hasattr(Users, 'login')
        assert hasattr(Users, 'password')

    def test_has_save_attribute(self, users):
        assert hasattr(Users, 'save')

    def test_users_populated(self, users):
        users_list = Users.query.all()
        assert len(users_list) == 1

    
    # def test_get_user_by_login(self, users):
    #     auth = AuthMixin()
    #     user = auth.get_user_by_login('login_test')
    #     assert user.login == 'login_test'

    # def test_get_user_by_login_not_found(self):
    #     auth = AuthMixin()
    #     assert not auth.get_user_by_login('not_exists')

    # def test_check_password(self, users):
    #     auth = AuthMixin()
    #     user = Users.query.filter_by(login='login_test').first()
    #     assert auth.check_password(user.password, '12345')

    # def test_check_password_invalid(self):
    #     auth = AuthMixin()
    #     user = Users.query.filter_by(login='login_test').first()
    #     assert not auth.check_password(user.password, 'wrong_password')
