from sqlalchemy import Column, String, Integer, Float, ForeignKey
from marshmallow import Schema, fields

from project.setup.db import models


class Genre(models.Base):
    __tablename__ = 'genres'

    name = Column(String(100), unique=True, nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class Director(models.Base):
    __tablename__ = 'directors'

    name = Column(String(100), unique=True, nullable=False)


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()


class Movie(models.Base):
    __tablename__ = 'movies'

    title = Column(String(100), unique=True, nullable=False)
    description = Column(String, nullable=False)
    trailer = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    rating = Column(Float, nullable=False)
    genre_id = Column(Integer, ForeignKey('genres.id'), nullable=False)
    director_id = Column(Integer, ForeignKey('directors.id'), nullable=False)


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre_id = fields.Int()
    director_id = fields.Int()


class User(models.Base):
    __tablename__ = 'users'

    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    name = Column(String)
    surname = Column(Integer)
    favorite_genre = Column(String)


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    password = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()
