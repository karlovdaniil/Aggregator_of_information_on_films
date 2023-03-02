import jwt
import datetime
import calendar

from flask import abort

from project.config import BaseConfig
from project.services.users_service import UsersService


class AuthService:

    def __init__(self, user_service: UsersService):
        self.user_service = user_service

    def generate_token(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)

        if user is None:
            abort(400)
        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            'email': user.email,
        }

        min_token = datetime.datetime.utcnow() + datetime.timedelta(minutes=BaseConfig.TOKEN_EXPIRE_MINUTES)
        data['exp'] = calendar.timegm(min_token.timetuple())
        access_token = jwt.encode(data, BaseConfig.SECRET_KEY, algorithm=BaseConfig.ALGO)

        days_token = datetime.datetime.utcnow() + datetime.timedelta(days=BaseConfig.TOKEN_EXPIRE_DAYS)
        data['exp'] = calendar.timegm(days_token.timetuple())
        refresh_token = jwt.encode(data, BaseConfig.SECRET_KEY, algorithm=BaseConfig.ALGO)

        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def refresh_tokens(self, token):
        data = jwt.decode(jwt=token, key=BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGO])
        email = data.get('email')

        tokens = self.generate_token(email, None, is_refresh=True)

        return tokens

    def validate_token(self, access_token, refresh_token):
        for token in (access_token, refresh_token):
            try:
                jwt.decode(jwt=token, key=BaseConfig.SECRET_KEY, algorithms=[BaseConfig.ALGO])
            except Exception as e:
                return False

        return True
