from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash


from estacao.models import Users


auth = HTTPBasicAuth()


class AuthMixin(object):
    @auth.verify_password
    def verify_password(self, username, password):
        user = self.get_user_by_login(username)
        if not user:
            return False
        return self.check_password(user.password, password)

    def get_user_by_login(self, username):
        user = Users.query.filter_by(login=username).first()
        if not user:
            return False
        return user

    def check_password(self, hashed_password, plain_password):
        return check_password_hash(hashed_password, plain_password)
