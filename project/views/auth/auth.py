from flask import request, abort, jsonify
from flask_restx import Namespace, Resource

from project.container import user_service, auth_service
from project.setup.api.models import user


api = Namespace('auth')


@api.route('/register/')
class RegisterView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def post(self):
        """
        Get all directors.
        """
        req_json = request.json
        user_new = user_service.create(req_json)

        return f'{user_new}', 201


@api.route('/login/')
class AuthView(Resource):
    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def post(self):
        """
        Get all directors.
        """
        req_json = request.json

        email = req_json.get('email')
        password = req_json.get('password')

        try:
            tokens = auth_service.generate_token(email, password)
            print(tokens)

            return tokens, 201

        except Exception as e:
            abort(401)

    @api.marshal_with(user, as_list=True, code=200, description='OK')
    def put(self):
        """
        Get all directors.
        """
        req_json = request.json

        access_token = req_json.get('access_token')
        refresh_token = req_json.get('refresh_token')

        try:
            tokens = auth_service.refresh_token(access_token, refresh_token)
            return tokens, 201

        except Exception as e:
            abort(401)
