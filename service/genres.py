from dao.genres import GenresDAO

class GenresService:

    def __init__(self, genres_dao: GenresDAO):
        self.genres_dao = genres_dao

    def get_all_genres(self):
        return self.genres_dao.get_all_genres()

    def get_genre(self, gid):
        return self.genres_dao.get_genre(gid)