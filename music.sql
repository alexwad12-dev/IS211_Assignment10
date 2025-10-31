CREATE TABLE artist (
    id INTEGER PRIMARY KEY,
    artist_name TEXT
);

CREATE TABLE album (
    id INTEGER PRIMARY KEY,
    album_name TEXT,
    artist_id INTEGER,
    FOREIGN KEY (artist_id) REFERENCES artist(id)
 );

 CREATE TABLE song (
    id INTEGER PRIMARY KEY,
    song_name TEXT,
    album_id INTEGER,
    track_number INTEGER,
    song_duration INTEGER
    FOREIGN KEY (album_id) REFERENCE album(id)
);
