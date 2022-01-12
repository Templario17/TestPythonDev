from core.db import DBQuery
from modules.genre import Genre


#TODO conector logico Relacional genre - song 
class GenreSong(object):
    
    def __init__(self, song):
        self.genresong_id = 0
        self.song = song # Objeto compuesto
        self.genres = self.song.genre_collection #Objetos compositores

    def insert(self):
        self.delete()
        for genre in self.genres:
            sql = """INSERT INTO genresong (song, genre)
                     VALUES ({}, {})""".format(self.song.song_id, self.genre.genre_id)
            self.genresong_id = DBQuery().execute(sql)
                
    def delete(self):
        sql = """DELETE FROM genresong WHERE song={}""".format(self.song.song_id)
        DBQuery().execute(sql)
    
    def select(self):
        sql = """SELECT genre 
                 FROM   genresong 
                 WHERE song={}""".format(self.song.song_id)
        resultado = DBQuery().execute(sql)
        
        for obj in resultado:
            genero = Genre()
            genero.genre_id = obj[0]
            genero.select()
            self.song.add_genre(vars(genero))


class GenreSongHelper(object):
    
    @staticmethod
    def group_by_genre():
        sql = """SELECT song, genre FROM genresong ORDER BY genre"""
        resultado = DBQuery().execute(sql)
        return resultado
