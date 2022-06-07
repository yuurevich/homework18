from dao.directors import DirectorsDAO
from dao.genres import GenresDAO
from dao.movies import MoviesDAO
from service.directors import DirectorsService
from service.genres import GenresService
from setup_db import db
from service.movies import MoviesService

movies_dao = MoviesDAO(db.session)
movies_service = MoviesService(movies_dao=movies_dao)


directors_dao = DirectorsDAO(db.session)
directors_service = DirectorsService(directors_dao=directors_dao)


genres_dao = GenresDAO(db.session)
genres_service = GenresService(genres_dao=genres_dao)