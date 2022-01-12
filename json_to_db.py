#!/usr/bin/env python3

import json
from os import environ
from sys import path
path.append(environ['PWD'])
import pandas as pd

from rootsystem.application.core.db import DBQuery


url = "https://rss.applemarketingtools.com/api/v2/us/music/most-played/100/songs.json"

#datos = pd.read_json(url, orient='index')

    

with open("songs.json", "r") as f:
    data = json.loads(f.read())

for i in range(100):
    result =  data['feed']['results'][i]
    song_id = int(result['id'])
    #ARTIST
    artist_name = result['artistName']
    artist_id = int(result['artistId'])
    artist_url = result['artistUrl']
   
    artist_sql = """ INSERT INTO artist
                     (artist_id, name, url)
              VALUES ({}, '{}', '{}')
    """.format(
            artist_id, 
            artist_name, 
            artist_url)
    try:
        DBQuery().execute(artist_sql)
    except:
        pass
        
    #GENRE
    genre_collection = result['genres']
    for j in range(len(genre_collection)):
        g = genre_collection[j]
        genre_id = int(g['genreId'])
        name_genre = g['name']
        url_genre = g['url']
        genre_sql = """ INSERT INTO genre
                            (genre_id, name, url)
                        VALUES({}, '{}', '{}')    
        """.format(
            genre_id,
            name_genre,
            url_genre
        )
        #  RELACIONAL GENRE-SONG
        genresong_sql = """INSERT INTO  genresong 
                                        (song, genre)
                            VALUES       ({}, {})
        """.format(song_id, 
            genre_id
        )
        DBQuery().execute(genresong_sql)
        try:
            DBQuery().execute(genre_sql)
            
        except:
            pass
    #SONG
    name_song = result['name']
    kind = result['kind']
    d = result['releaseDate']
    try:
        content_adv = result['contentAdvisoryRating']
    except KeyError:
        content_adv = ""       
    url_song = result['url']
  
    song_sql = """ INSERT INTO song
                               (song_id, name, kind, release_date, 
                                content_advisory_rating, url, artist)
                   VALUES ({}, '{}', '{}', '{}', '{}', '{}', {})
    """.format(
            song_id, 
            name_song, 
            kind, 
            d, 
            content_adv, 
            url_song, 
            artist_id
    )
    try:
        DBQuery().execute(song_sql)
    except:
        pass
    
    
    print("{} ok".format(i))


