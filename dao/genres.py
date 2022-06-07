from dao.model.genres import Genre, GenreSchema


class GenresDAO:
    def __init__(self, session):
        self.session = session

    def get_all_genres(self):
        genres = Genre.query.all()
        return GenreSchema(many=True).dump(genres)

    def get_genre(self, gid):
        genre = Genre.query.filter(Genre.id == gid).first()
        return GenreSchema().dump(genre)
