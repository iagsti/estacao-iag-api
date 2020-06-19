from flask_httpauth import HTTPBasicAuth
from werkzeug.security import check_password_hash


from models import Users


auth = HTTPBasicAuth()


def get_user_by_login(username):
    user = Users.query.filter_by(login=username).first()
    if not user:
        return False
    return user


def check_password(hashed_password, plain_password):
    return check_password_hash(hashed_password, plain_password)


class AuthMixin(object):
    @auth.verify_password
    def verify_password(username, password):
        user = get_user_by_login(username)
        if not user:
            return False
        return check_password(user.password, password)
