from json import loads, dumps
from cgi import FieldStorage
from string import Template

from core.api import APIRESTFul
from core.db import DBQuery
from core.helpers import show, show_json
from settings import ARG


class Genre(object):
    
    def __init__(self):
        self.genre_id = 0
        self.name = ''
        self.url = ''
        
    def select(self):
        sql = """SELECT name, url
                 FROM genre
                 WHERE genre_id={}""".format(self.genre_id)
        resultado = DBQuery().execute(sql)[0]
        self.name = resultado[0]
        self.url = resultado[1]


class GenreView(object):
    pass
    
    
class GenreController(object):
    
    def __init__(self, api):
        self.model = Genre()
        self.view = GenreView()
        self.api = api
    
