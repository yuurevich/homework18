from flask_restx import Resource, Namespace
from implemented import movies_service
from flask import request

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesView(Resource):
    def get(self):
        args = request.args

        if 'director_id' in args:
            return movies_service.get_by_director_id(args['director_id'])

        if 'genre_id' in args:
            return movies_service.get_by_genre_id(args['genre_id'])

        if 'year' in args:
            return movies_service.get_by_year(args['year'])

        movies = movies_service.get_movies()
        return movies, 200

    def post(self):
        data = request.get_json()
        movies_service.create(data)
        return "Фильм добавлен", 201


@movies_ns.route('/<id>')
class MovieView(Resource):
    def get(self, id):
        movie = movies_service.get_movie(id)
        return movie, 200

    def put(self, id):
        data = request.json
        movies_service.update(id, data)
        return 'Поля фильма изменены', 200

    def delete(self, id):
        movies_service.delete(id)
        return 'Фильм удален', 200
