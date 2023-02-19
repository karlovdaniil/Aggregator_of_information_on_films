from typing import Optional

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        if movie := self.dao.get_by_id(pk):
            return movie
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None, status: Optional[str] = None) -> list[Movie]:
        return self.dao.get_all(page=page, status=status)



# from dao.movie import MovieDAO
#
#
# class MovieService:
#     def __init__(self, dao: MovieDAO):
#         self.dao = dao
#
#     def get_one(self, bid):
#         return self.dao.get_one(bid)
#
#     def get_all(self, filters):
#         if filters.get("director_id") is not None:
#             movies = self.dao.get_by_director_id(filters.get("director_id"))
#         elif filters.get("genre_id") is not None:
#             movies = self.dao.get_by_genre_id(filters.get("genre_id"))
#         elif filters.get("year") is not None:
#             movies = self.dao.get_by_year(filters.get("year"))
#         else:
#             movies = self.dao.get_all()
#         return movies
#
#     def create(self, movie_d):
#         return self.dao.create(movie_d)
#
#     def update(self, movie_d):
#         self.dao.update(movie_d)
#         return self.dao
#
#     def delete(self, rid):
#         self.dao.delete(rid)
