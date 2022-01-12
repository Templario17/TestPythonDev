from core.db import DBQuery
from core.helpers import show, show_json
from settings import ARG

class Artist(object):
    
    def __init__(self):
        self.artist_id = 0
        self.name = ''
        self.url = ''

    def select(self):
        sql = """SELECT name, url
                 FROM artist
                 WHERE artist_id={}""".format(self.artist_id)
        
        resultados = DBQuery().execute(sql)[0] 
        self.name = resultados[0]
        self.url = resultados[1]
        

class ArtistView(object):
    pass


class ArtistController(object):
    
    def __init__(self, api):
        self.model = Artist()
        self.view = ArtistView()
        self.api = api
    
    def ver(self):
        self.model.artist_id = ARG
        self.model.select()
        show(vars(self.model))
            
        
