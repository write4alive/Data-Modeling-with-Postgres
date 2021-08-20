# DROP TABLES


user_table_drop = "drop table if exists  d_users"
song_table_drop = "drop table  if exists d_songs"
artist_table_drop = "drop table  if exists d_artists"
time_table_drop = "drop table  if exists d_time"
songplay_table_drop = "drop table if exists f_songplays"

# CREATE TABLES

songplay_table_create = ("""create table if not exists f_songplays 
(songplay_id serial primary key, start_time bigint, user_id int, level varchar, song_id varchar, artist_id varchar , session_id int not null , location varchar, user_agent varchar)
""")

user_table_create =     ("""create table if not exists d_users 
(user_id int primary key, first_name varchar, last_name varchar, gender char(1),level varchar)
""")

song_table_create =     ("""create table if not exists d_songs 
(song_id varchar primary key, title varchar, artist_id varchar, year int, duration float)
""")

artist_table_create =   ("""create table if not exists d_artists 
(artist_id varchar primary key, name varchar, location varchar, latitude float, longitude float)
""") 

time_table_create =     ("""create table if not exists d_time 
(start_time bigint primary key , hour int , day int ,week int ,month int , year int , weekday int )
""")

# INSERT RECORDS

songplay_table_insert = ("""insert into f_songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
values(%s,%s,%s,%s,%s,%s,%s,%s)
""")

user_table_insert = ("""insert into d_users(user_id, first_name, last_name, gender, level)
values(%s,%s,%s,%s,%s) ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level;
""")

song_table_insert = ("""insert into d_songs(song_id, title, artist_id, year, duration)
values(%s,%s,%s,%s,%s) ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""insert into d_artists(artist_id, name, location, latitude, longitude)
values(%s,%s,%s,%s,%s) ON CONFLICT (artist_id) DO NOTHING
""")

time_table_insert = ("""insert into d_time(start_time, hour, day, week, month, year, weekday)
values(%s,%s,%s,%s,%s,%s,%s) ON CONFLICT (start_time) DO NOTHING;
""")


# FIND SONGS

song_select = ("""select s.song_id , s.artist_id 
from d_songs s ,d_artists a
where s.artist_id=a.artist_id and s.title=(%s) AND a.name=(%s) AND s.duration=(%s)
""")

# ON songs.artist_id = artists.artist_id

# WHERE songs.title=(%s) AND artists.name=(%s) AND songs.duration=(%s)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [user_table_drop, song_table_drop, artist_table_drop, time_table_drop,songplay_table_drop]


# Simple Data Analysis Queries

# Top_3_song=(""" """)



