# DROP TABLES

songplay_table_drop = "drop table f_songplays"
user_table_drop = "drop table d_users"
song_table_drop = "drop table d_songs"
artist_table_drop = "drop table artist"
time_table_drop = "drop table time"

# CREATE TABLES

songplay_table_create = ("""create table if not exists f_songplays (songplay_id int, start_time timestamp, user_id int, level varchar, song_id int, artist_id int , session_id int , location varchar, user_agent varchar)
""")

user_table_create =     ("""create table if not exists d_users (user_id int, first_name varchar, last_name varchar, gender char(1),level varchar)
""")

song_table_create =     ("""create table if not exists d_songs (song_id varchar, title varchar, artist_id int, year int, duration numeric)
""")

artist_table_create =   ("""create table if not existsd_artist (artist_id varchar, name varchar, location varchar, latitude numeric, longitude numeric)
""") 

time_table_create =     ("""create table if not exists d_time ()
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]