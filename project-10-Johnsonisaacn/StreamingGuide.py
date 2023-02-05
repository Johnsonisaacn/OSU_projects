# Author: Isaac Johnson
# GitHub UserID: Johnsonisaacn
# Date: 12/1/2022
# Description: Three classes that create objects related to movies and streaming services

class Movie:
    """Creates movie objects with title, genre, director, and year as data members"""
    def __init__(self, title, genre, director, year):
        """initializes data members"""
        self._title = str(title)
        self._genre = str(genre)
        self._director = str(director)
        self._year = int(year)

    def get_title(self):
        """returns title of the film"""
        return self._title
    def get_genre(self):
        """returns genre of the film"""
        return self._genre
    def get_director(self):
        """:return director of the film"""
        return self._director
    def get_year(self):
        """returns year that the film premiered"""
        return self._year
class StreamingService:
    """Creates dictionaries of catalogs of films"""
    def __init__(self, name):
        """initializes data members with name as an argument and catalog as an empty library"""
        self._name = name
        self._catalog = {}
    def get_name(self):
        """returns name of film"""
        return self._name
    def get_catalog(self):
        """returns catalog"""
        return self._catalog
    def add_movie(self, movie):
        """adds movie object to catalog"""
        self._catalog[movie.get_title()] = movie
    def delete_movie(self, movie):
        """deletes a movie from the catalog"""
        del self._catalog[movie]
class StreamingGuide:
    """creates list of streaming services that can be searched for films"""
    def __init__(self):
        """initializes data object of list of streaming services"""
        self._streaming_guide = []
    def add_streaming_service(self, streaming_service):
        """adds a streaming service object to the guide list"""
        self._streaming_guide.append(streaming_service)
    def delete_streaming_service(self, streaming_service):
        """deletes streaming services from streaming guide list"""
        if streaming_service in self._streaming_guide:
            self._streaming_guide.remove(streaming_service)
    def where_to_watch_movie(self, movie_title):
        """takes a movie title as an argument and returns streaming services on which
        it can be watched"""
        streaming_services = []
        for service in self._streaming_guide:
            if movie_title in service.get_catalog():
                service_name = service.get_name()
                if len(streaming_services) == 0:
                    found_film = service.get_catalog()[movie_title]
                    year = found_film.get_year()
                    movie_info = movie_title+" ("+str(year)+")"
                    streaming_services.append(movie_info)
                streaming_services.append(service_name)
        if len(streaming_services) > 0:
            return streaming_services
        else:
            return None

