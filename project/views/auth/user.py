from flask import request
from flask_restx import Namespace, Resource

from project.container import user_service
from project.models import UserSchema

api = Namespace('user')


@api.route('/')
class UsersView(Resource):
    def get(self):
        """
        Show all users.
        """
        all_user = user_service.get_all()
        res = UserSchema(many=True).dump(all_user)
        return res, 200


@api.route('/<int:uid>/')
class UserView(Resource):
    def get(self, uid):
        """
        Show user by id.
        """
        user = user_service.get_one(uid)
        res = UserSchema().dump(user)
        return res, 200

    def patch(self, uid):
        """
        Update info about user.
        """
        req_json = request.json
        if 'id' not in req_json:
            req_json['id'] = uid

        user_service.update(req_json)
        return '', 204

    def delete(self, uid):
        """
        Delete user by id.
        """
        user_service.delete(uid)
        return '', 204


@api.route('/password/')
class UpdateUserPasswordView(Resource):
    def put(self):
        """
        Update password by user.
        """
        req_json = request.json
        email = req_json.get('email')
        old_password = req_json.get('old_password')
        new_password = req_json.get('new_password')

        user = user_service.get_by_email(email)

        if user_service.compare_passwords(user.password, old_password):
            user.password = user_service.get_hash(new_password)
            result = UserSchema().dump(user)
            user_service.update(result)

        return '', 201
