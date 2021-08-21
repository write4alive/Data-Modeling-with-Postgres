#Data Engineering Nano Degree Programm of Udacity - Project 1 -
</h1>Project: Data Modeling with Postgres</h1>

<h3>Introduction</h3>

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

<h3>Project Description</h3>

In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.



<h3>Song Dataset</h3>

The first dataset is a subset of real data from the Million Song Dataset. Each file is in JSON format and contains metadata about a song and the artist of that song. The files are partitioned by the first three letters of each song's track ID. For example, here are filepaths to two files in this dataset.

song_data/A/B/C/TRABCEI128F424C983.json
song_data/A/A/B/TRAABJL12903CDCF1A.json
And below is an example of what a single song file, TRAABJL12903CDCF1A.json, looks like.

{"num_songs": 1, "artist_id": "ARJIE2Y1187B994AB7", "artist_latitude": null, "artist_longitude": null, "artist_location": "", "artist_name": "Line Renaud", "song_id": "SOUPIRU12A6D4FA1E1", "title": "Der Kleine Dompfaff", "duration": 152.92036, "year": 0}

<h3>Log Dataset</h3>

The second dataset consists of log files in JSON format generated by  event simulator based on the songs in the dataset above. These simulate activity logs from a music streaming app based on specified configurations. There you can check event Simulater https://github.com/Interana/eventsim

The log files in the dataset you'll be working with are partitioned by year and month. For example, here are filepaths to two files in this dataset.

log_data/2018/11/2018-11-12-events.json
log_data/2018/11/2018-11-13-events.json
And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.


If you would like to look at the JSON data within log_data files, you will need to create a pandas dataframe to read the data. Remember to first import JSON and pandas libraries.

df = pd.read_json(filepath, lines=True)

For example, df = pd.read_json('data/log_data/2018/11/2018-11-01-events.json', lines=True) would read the data file 2018-11-01-events.json.

In case you need a refresher on JSON file formats, here is a helpful video. https://www.youtube.com/watch?time_continue=1&v=hO2CayzZBoA


<h3>Schema for Song Play Analysis</h3>
Using the song and log datasets, you'll need to create a star schema optimized for queries on song play analysis. This includes the following tables.

<h3>Fact Table</h3>
songplays - records in log data associated with song plays i.e. records with page NextSong
songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

<h3>Dimension Tables</h3>
<li>users - users in the app <br>
user_id, first_name, last_name, gender, level<br><br>

<li>songs - songs in music database  <br>
song_id, title, artist_id, year, duration<br><br>

<li>artists - artists in music database<br>
artist_id, name, location, latitude, longitude<br><br>

<li>time - timestamps of records in songplays broken down into specific units<br>
start_time, hour, day, week, month, year, weekday<br>


<h3>Project Template</h3>

To get started with the project, go to the workspace on the next page, where you'll find the project template files. You can work on your project and submit your work through this workspace. Alternatively, you can download the project template files from the Resources folder if you'd like to develop your project locally.

In addition to the data files, the project workspace includes six files:

<li>test.ipynb displays the first few rows of each table to let you check your database.
<li>create_tables.py drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts.
<li>etl.ipynb reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.
<li>etl.py reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook.
<li>sql_queries.py contains all your sql queries, and is imported into the last three files above.
<li>README.md provides discussion on your project.


<h3>Project Steps</h3>
Below are steps you can follow to complete the project:

<h4>Create Tables</h4>
<li>Write CREATE statements in sql_queries.py to create each table.
<li>Write DROP statements in sql_queries.py to drop each table if it exists.
<li>Run create_tables.py to create your database and tables.


<h2>Queries that you can use on your tables:</h2>
<li>Select * from f_songplays LIMIT 10;
<li>Select * from d_artists   LIMIT 10



<h2>Table results in postgresql</h2>
Table List<br>
![p1_db_tables_attributes](https://user-images.githubusercontent.com/16669517/130276401-348602c1-e3d5-48f3-8861-1a4342628a3a.PNG)<br>
  
Fact songplays<br>
![fact songplays](https://user-images.githubusercontent.com/16669517/130276252-b47fa04f-b7e2-4998-8a1b-265d3c887727.PNG)<br>
  
Dim users<br>
![dim users](https://user-images.githubusercontent.com/16669517/130276375-7393a281-5975-46dd-b5f4-a6eb42339b11.PNG)<br>
  
Dim time<br>
![dim time](https://user-images.githubusercontent.com/16669517/130276382-71270b47-799d-4adf-91b7-d422051c0f08.PNG)<br>
  
Dim songs<br>
![dim songs](https://user-images.githubusercontent.com/16669517/130276389-24cfd679-f57c-4d33-bbe2-aa7a8e80fcb4.PNG)<br>
  
Dim artists<br>
![dim artist](https://user-images.githubusercontent.com/16669517/130276394-a66a8b26-fe40-4b00-8a9c-50d6e3bb0aa7.PNG)<br>








