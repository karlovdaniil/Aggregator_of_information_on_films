import base64
import hashlib
import hmac

from project.dao.user import UserDAO
from project.config import BaseConfig
from project.models import User


class UsersService:

    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid: int) -> User:
        return self.dao.get_user_by_id(uid)

    def get_all(self) -> list[User]:
        return self.dao.get_all()

    def get_by_email(self, email):
        return self.dao.get_user_by_email(email)

    def delete(self, uid):
        self.dao.delete(uid)

    def get_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            BaseConfig.PWD_HASH_SALT,
            BaseConfig.PWD_HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest)

    def compare_passwords(self, hash_password, password):
        decode_digest = base64.b64decode(hash_password)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            BaseConfig.PWD_HASH_SALT,
            BaseConfig.PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decode_digest, hash_digest)

    def create(self, user_d):
        user_d['password'] = self.get_hash(user_d['password'])

        return self.dao.create(user_d)

    def update(self, user_d):
        self.dao.update(user_d)
        return self.dao
