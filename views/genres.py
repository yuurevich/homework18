from flask_restx import Resource, Namespace
from implemented import genres_service

genres_ns = Namespace('genres')


@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genres_service.get_all_genres()
        return genres, 200


@genres_ns.route('/<id>')
class GenreView(Resource):
    def get(self, id):
        return genres_service.get_genre(id), 200

