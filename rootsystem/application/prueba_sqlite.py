import sqlite3

con = sqlite3.connect('ejemplo.db')

cursor = con.cursor()

#cursor.execute("""CREATE TABLE song(
	#song_id INT(11) NOT NULL PRIMARY KEY,
    	#name VARCHAR(50),
    	#kind VARCHAR(25),
    	#release_date DATE,
    	#content_advisory_rating VARCHAR(25),
    	#url BLOB)
#"""
#)
song_sql = """ INSERT INTO song
                               (song_id, name, kind, release_date, 
                                content_advisory_rating, url)
                   VALUES ({}, '{}', '{}', '{}', '{}', '{}')
    """.format(
            1222, 
            'test', 
            'music', 
            '2022-01-11', 
            'explicit', 
            'http://'
    )
sql = """SELECT * FROM song"""

print(cursor.execute(sql))

con.commit()
con.close()
