from flask_restx import Resource, Namespace
from implemented import directors_service

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        directors = directors_service.get_all_directors()
        return directors, 200


@directors_ns.route('/<id>')
class DirectorsView(Resource):
    def get(self, id):
        return directors_service.get_director(id), 200
