import os
import glob
from numpy import promote_types
from pandas._libs.tslibs.timestamps import Timestamp
from pandas.core.indexing import convert_to_index_sliceable
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):

    '''
    process_song_file(cur, filepath)::
    
    Paramters:
    cur      :cursor
    filepath :file path of song file

    Reading from source file  'data/song_data'

    Whit  using defined sql queries and insert data to song and artist dim tables.

    '''

    # open song file
    df = pd.read_json(filepath, lines=True)

    # insert song record
    song_data = list(df[['song_id', 'title', 'artist_id', 'year', 'duration']].values[0])
    cur.execute(song_table_insert, song_data)
    
    # insert artist record
    artist_data = list(df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values[0])
    cur.execute(artist_table_insert, artist_data)
  

def process_log_file(cur, filepath):

    '''
    process_log_file(cur, filepath)::
    
    Paramters:
    cur      :cursor
    filepath :file path of log file


    Reading  from source file 'data/log_data'

    Filtering  page with 'NextSong'
    
    Converting timestamp  to datetime  with using pandas

    inserting rows to time and user table with iterating list of rows.

    finally insterting data to tables.

    '''

    # open log file
    df = pd.read_json(filepath, lines=True)

    # filter by NextSong action
    df = df[df['page']=='NextSong']

    # convert timestamp column to datetime
    t = pd.to_datetime(df['ts'], unit='ms')
    
    # insert time data records
    t = pd.to_datetime(df['ts'], unit='ms')
    time_data = (df['ts'], t.dt.hour, t.dt.day, t.dt.weekofyear, t.dt.month, t.dt.year, t.dt.weekday)
    column_labels = ['timestamp', 'hour', 'day', 'week of year', 'month', 'year', 'weekday']
    time_df = pd.DataFrame(dict(zip(column_labels, time_data)))
    print(time_df.head())

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

    # load user table
    user_df = pd.DataFrame(df[['userId', 'firstName', 'lastName', 'gender', 'level']].values)

    # insert user records
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    # insert songplay records
    for index, row in df.iterrows():
        
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record                 
        songplay_data = (row.ts, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent)
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''
    process_data(cur,conn,filepath,func)  starting data proccessing  of song and log files

    Parameters:
        cur      :cursor
        con      :connection
        filepath :source file path
        func     :accepting function 

    '''

    # get all files matching extension from directory
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))

    # get total number of files found
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))

    # iterate over files and process
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():

    '''
    Connecting sparkifydb database  and  starting file operations , ingesting operations

    Data  source are  inside project file  'data/song_data' and 'data/log_data'

    process_data(cur,conn,filepath,func)  starting data proccessing  of song and log files

    Parameters:
        cur      :cursor
        con      :connection
        filepath :source file path
        process_song_file() : processing song files
        process_log_file()  : processing log  files

    '''
    conn = psycopg2.connect(user="student",password="student",host="127.0.0.1",port="5433",database="sparkifydb")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()
