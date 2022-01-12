-- ORM mapeo relacional de objetos 

CREATE TABLE IF NOT EXISTS artist(
    artist_id  INT(11) NOT NULL PRIMARY KEY,
    name VARCHAR(100),
    url BLOB
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS song(
    song_id INT(11) NOT NULL PRIMARY KEY,
    name VARCHAR(50),
    kind VARCHAR(25),
    release_date DATE,
    content_advisory_rating VARCHAR(25),
    url BLOB,
    artist INT(11),
    FOREIGN KEY(artist)
        REFERENCES artist(artist_id)
        ON DELETE SET NULL
)ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS genre(
    genre_id INT(11) NOT NULL PRIMARY KEY,
    name VARCHAR(25),
    url BLOB
)ENGINE=InnoDB;

--conector logico relacional
CREATE TABLE IF NOT EXISTS genresong(
    genresong_id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    song INT(11),
    INDEX (song),
    FOREIGN KEY(song)
        REFERENCES song(song_id)
        ON DELETE CASCADE,
    genre INT(11),
    FOREIGN KEY(genre)
        REFERENCES genre(genre_id)
        ON DELETE CASCADE
)ENGINE=InnoDB;
