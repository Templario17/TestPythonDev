from json import loads, dumps
from cgi import FieldStorage
from string import Template

from modules.artist import Artist
from modules.genresong import GenreSong, GenreSongHelper
from core.api import APIRESTFul
from core.db import DBQuery
from core.helpers import show, show_json
from settings import ARG


class Song(object):
    
    def __init__(self):
        self.song_id = 0
        self.name = ''
        self.kind = ''
        self.release_date  = ''
        self.content_advisory_rating = ''
        self.url = ''
        self.artist = Artist()
        self.genre_collection = [] #propiedad colectora independiente
    
    def add_genre(self, genre):
        self.genre_collection.append(genre)
        
    def insert(self):
        sql = """ INSERT INTO song
                               (song_id, name, kind, release_date, 
                                content_advisory_rating, url, artist)
                   VALUES ({}, '{}', '{}', '{}', '{}', '{}', {})
        """.format(
            self.song_id,
            self.name,
            self.kind,
            self.release_date,
            self.content_advisory_rating,
            self.url,
            self.artist.artist_id
        )
        DBQuery().execute(sql)
        
    def select(self):
        sql = """SELECT name, kind, release_date, content_advisory_rating, url, artist
                 FROM song
                 WHERE song_id={}""".format(self.song_id)
        resultados = DBQuery().execute(sql)[0]
        
        self.name = resultados[0]
        self.kind = resultados[1]
        self.release_date = str(resultados[2])
        self.content_advisory_rating = resultados[3]
        self.url = resultados[4]
        self.artist = resultados[5]
        
        obj = Artist()
        obj.artist_id = self.artist
        obj.select()
        self.artist = obj
       
        cl = GenreSong(self) # intancia del conector logico relacional 
        cl.select()
        
            
    def update(self):
        pass

    def delete(self):
        sql = """DELETE FROM song WHERE song_id={}""".format(self.song_id)
        
        DBQuery().execute(sql)
        


class SongView(object):
    pass
    


class SongController(object):
    
    def __init__(self, api):
        self.model = Song()
        self.view = SongView()
        self.api = api
    
    def ver(self):        
        self.model.song_id = ARG
        try:
            self.model.select()
        except IndexError:
            show("Registo no encontrado")
            exit()
            
        if self.api is True:
            obj_dicc = vars(self.model.artist)
            self.model.artist = obj_dicc
            
            show_json(vars(self.model))
        else:
            show("llamado a la API")
    
    def search_lookup(self):
        """ An endpoint to provide a search lookup within the tracks
             (at least by name, but is open to any suggestions) """
        form = FieldStorage()
        json = form['data'].value
        dato = loads(json)
        kword = data['name']
        
        if self.api is True:
            try:
                resultado = SongHelper().get_name(kword)
                show_json(dumps(resultado))
            except IndexError:
                show("No existe registro")
                exit()
        else:
            show("Consuma la API ->http://host/api/modulo/recurso")
    
    def get_top(self):
        """ An endpoint that would allow to get the top 50 popularity tracks """
        if not ARG == 0:
            params = ARG
        else:
            params = 50
        query = SongHelper().get_top(params) 
        show_json(dumps(query, indent=4))
    
    def eliminar(self):
        """ An endpoint to remove a track, using a given identifier (defined by you) """
        if self.api is True:        
            self.model.song_id = ARG
            self.model.delete()                                           
        else:
            show("Consuma la API ->http://hostname/api/modulo/recurso/<id>")
            
    def get_by_genre(self):
        """ Create an endpoint to return the tracks grouped by genres """
        query = GenreSongHelper().group_by_genre()
        show(query)
    
    def add_track(self):
        """ An endpoint to add new tracks using ORM """
        try:
            form = FieldStorage()
            json = form['data'].value
            track_data = loads(json)
            
            artist = track_data['artistId']
            self.model.artist.artist_id = artist
            self.model.artist.select() 
        
            self.model.song_id = track_data['id']
            self.model.name = track_data['name']
            self.model.kind = track_data['kind']
            self.model.release_date = track_data['releaseDate'] 
            self.model.content_advisory_rating = track_data['content_advisory_rating']
            self.model.url = track_data['url']
            self.model.select()
            
            show_json(vars(self.model))
        except:
            show("error en parametros !")
            exit()
        

class SongHelper(object):
    
    @staticmethod
    def get_name(kword=''):
        sql = """SELECT song_id, name, kind, release_date, content_advisory_rating, url, artist
                 FROM song
                 WHERE name='{}' """.format(kword)
        resultado = DBQuery().execute(sql)[0]
        
        serializer = dict(song_id=resultado[0],
                    name=resultado[1],
                    kind=resultado[2],
                    release_date=str(resultado[3]),
                    content_advisory_rating=resultado[4],
                    url=str(resultado[5])
                    
                    )
        return serializer
    
    @staticmethod
    def get_top(n):
        sql = """SELECT song_id, name, kind, release_date, content_advisory_rating, url, artist
                 FROM song
                 ASCENT LIMIT {}""".format(n)
        resultado = DBQuery().execute(sql)
        json = """{
                "song_id":$song_id,
                "name":"$name",
                "kind":"$kind",
                "release_date":"$release_date",
                "content_advisory_rating":"$content_advisory_rating",
                "url":"$url",
                "artist":"$artist"      
        }"""
        lista = []
        for i in range(len(resultado)):
            dicc = dict(song_id=resultado[i][0],
                    name=resultado[i][1],
                    kind=resultado[i][2],
                    release_date=str(resultado[i][3]),
                    content_advisory_rating=resultado[i][4],
                    url=str(resultado[i][5]),
                    artist=resultado[i][6]
                    )
            data = Template(json).safe_substitute(dicc)
            lista.append(data)
        return lista
    
