from flask_restx import Namespace, Resource

from project.container import director_service
from project.setup.api.models import director
from project.decorators import auth_required

api = Namespace('directors')


@api.route('/')
class DirectorsView(Resource):
    @auth_required
    @api.marshal_with(director, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all directors.
        """
        return director_service.get_all()


@api.route('/<int:director_id>/')
class DirectorView(Resource):
    @api.response(404, 'Not Found')
    @auth_required
    @api.marshal_with(director, code=200, description='OK')
    def get(self, director_id: int):
        """
        Get director by id.
        """
        return director_service.get_item(director_id)
