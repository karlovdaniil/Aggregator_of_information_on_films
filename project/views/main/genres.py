from flask_restx import Namespace, Resource

from project.container import genre_service
from project.setup.api.models import genre
from project.decorators import auth_required

api = Namespace('genres')


@api.route('/')
class GenresView(Resource):
    @auth_required
    @api.marshal_with(genre, as_list=True, code=200, description='OK')
    def get(self):
        """
        Get all genres.
        """
        return genre_service.get_all()


@api.route('/<int:genre_id>/')
class GenreView(Resource):
    @api.response(404, 'Not Found')
    @auth_required
    @api.marshal_with(genre, code=200, description='OK')
    def get(self, genre_id: int):
        """
        Get genre by id.
        """
        return genre_service.get_item(genre_id)
