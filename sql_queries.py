# DROP TABLES

song_plays_table_drop = "DROP TABLE IF EXISTS song_plays CASCADE;"
users_table_drop = "DROP TABLE IF EXISTS users CASCADE;"
songs_table_drop = "DROP TABLE IF EXISTS songs CASCADE;"
artists_table_drop = "DROP TABLE IF EXISTS artists CASCADE;"
time_table_drop = "DROP TABLE IF EXISTS time CASCADE;"

# CREATE TABLES

song_plays_table_create = ("""

CREATE TABLE IF NOT EXISTS song_plays (
    song_play_id SERIAL PRIMARY KEY,
    start_time bigint NOT NULL,
    user_id int NOT NULL,
    level varchar,
    song_id varchar,
    artist_id varchar,
    session_id int,
    location varchar,
    user_agent varchar,

    CONSTRAINT FK_song_plays_users FOREIGN KEY (user_id)
        REFERENCES users (user_id)
        ON DELETE CASCADE,

    CONSTRAINT FK_song_plays_songs FOREIGN KEY (song_id)
        REFERENCES songs (song_id)
        ON DELETE CASCADE,

    CONSTRAINT FK_song_plays_artists FOREIGN KEY (artist_id)
        REFERENCES artists (artist_id)
        ON DELETE CASCADE
        
    );
""")

users_table_create = ("""

CREATE TABLE IF NOT EXISTS users (
    user_id int NOT NULL PRIMARY KEY,
    first_name varchar,
    last_name varchar,
    gender varchar,
    level varchar
    );
""")

songs_table_create = ("""

CREATE TABLE IF NOT EXISTS songs (
    song_id varchar PRIMARY KEY,
    title varchar,
    artist_id varchar,
    year int,
    duration float,

    CONSTRAINT FK_songs_artists FOREIGN KEY (artist_id)
        REFERENCES artists (artist_id)
        ON DELETE CASCADE
        
    );    
""")

artists_table_create = ("""

CREATE TABLE IF NOT EXISTS artists (
    artist_id varchar PRIMARY KEY,
    name varchar NOT NULL ,
    location varchar,
    latitude float,
    longitude float
    );
""")

time_table_create = ("""

CREATE TABLE IF NOT EXISTS time (
    start_time timestamp NOT NULL PRIMARY KEY,
    hour int,
    day int,
    week int,
    month int,
    year int,
    weekday varchar
    );
""")

# INSERT RECORDS

song_plays_table_insert = ("""

INSERT INTO song_plays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (song_play_id) DO NOTHING;
""")

users_table_insert = ("""

INSERT INTO users (user_id, first_name, last_name, gender, level)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;
""")

songs_table_insert = ("""

INSERT INTO songs (
    song_id, title, artist_id, year, duration)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
""")

artists_table_insert = ("""

INSERT INTO artists (
    artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""

INSERT INTO time (start_time, year, month, week, weekday, day, hour)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
 
""")

# FIND SONGS

song_select = ("""
SELECT songs.song_id, artists.artist_id
FROM songs JOIN artists
ON songs.artist_id = artists.artist_id
WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s;

""")

# QUERY LISTS

create_table_queries = [users_table_create, artists_table_create, songs_table_create, time_table_create, song_plays_table_create]
drop_table_queries = [users_table_drop, artists_table_drop, songs_table_drop, time_table_drop, song_plays_table_drop]
