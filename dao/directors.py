from dao.model.directors import Director, DirectorSchema

class DirectorsDAO():
    def __init__(self, session):
        self.session = session

    def get_all_directors(self):
        directors = Director.query.all()
        return DirectorSchema(many=True).dump(directors)

    def get_director(self, did):
        director = Director.query.filter(Director.id == did).first()
        return DirectorSchema().dump(director)
