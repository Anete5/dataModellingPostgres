# Project: Data Modeling with Postgres

## About the project

This project is created for a startup called *Sparkify*. It has released a new music streaming app that collects data on songs and user activity. The analytics team wants to analyze the data (e.g., what songs users are listening to), however, they do not have an easy way to do so since all the data resides in directories of JSON logs for user activity and JSON metadata for songs.  

To help *Sparkify's* analytics team, I was brought to the project. The main project activities included:

1. Creating a database schema

2. Building an ETL pipeline

To complete the project, I used a Postgres database, PyCharm, and JupyterLab for writing SQL, Python.

## Datasets

*Sparkify's* analytics team provided me with two datasets - Songs and Logs.

Songs dataset includes all the metadata about a song and an artist. Below is an example of one of the JSON files:

**TRAAABD128F429CF47.json**

`{"num_songs": 1, "artist_id": "ARMJAGH1187FB546F3", "artist_latitude": 35.14968, "artist_longitude": -90.04892, "artist_location": "Memphis, TN", "artist_name": "The Box Tops", "song_id": "SOCIWDW12A8C13D406", "title": "Soul Deep", "duration": 148.03546, "year": 1969}`

Logs dataset includes all the data about user activity on the app. Below is an example of one of the JSON files:

**2018-11-01-events.json**

`{"artist":null,"auth":"Logged In","firstName":"Walter","gender":"M","itemInSession":0,"lastName":"Frye","length":null,"level":"free","location":"San Francisco-Oakland-Hayward, CA","method":"GET","page":"Home","registration":1540919166796.0,"sessionId":38,"song":null,"status":200,"ts":1541105830796,"userAgent":"\"Mozilla\/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit\/537.36 (KHTML, like Gecko) Chrome\/36.0.1985.143 Safari\/537.36\"","userId":"39"}`

Both datasets can be found in a folder called *data*. Below are examples of the filepaths:

**data/song_data/A/A/A/TRAAABD128F429CF47.json**
**data/log_data/2018/11/2018-11-01-events.json**

## Database schema

The database schema that I needed to create consists of **one fact table** and **four dimension tables**.

The fact table called *song_plays* includes the following columns:

**song_plays table**

- songplay_id
- start_time
- user_id
- level
- song_id
- artist_id
- session_id
- location
- user_agent

The dimension tables called *artists*, *songs*, *users*, *time* include the following columns:

**artists table**

- artist_id
- name
- location
- latitude
- longitude

**songs table**

- song_id
- title
- artist_id
- year
- duration

**users table**

- user_id
- first_name
- last_name
- gender
- level

**time table**

- start_time
- hour
- day
- week
- month
- year
- weekday

Here you can see how this schema looks like in the Postgres database:

![ER diagram](https://i.postimg.cc/J7gLY4XJ/Screenshot-31.png)

# Project's template files

To implement specific project activities as well as assist me while working, I needed additional files. These files are the following:

1. **test.ipynb, test (2).ipynb**  - for testing purposes such as running files or displaying query results.

2. **create_tables.py** - for performing table drops and creates.

3. **etl.ipynb** - for reading and processing a single file from Songs and Logs datasets and loading the data into my tables.

4. **etl.py** - for reading and processing all the files from Songs and Logs datasets and loading them into my tables.

5. **sql_queries.py**  - for writing SQL queries that are imported into the last three files above.

6. **README.md**  - for providing discussion on this project.

# Project's steps

The project consists of several steps that are listed below.

**Writing CREATE and DROP statements in *sql_queries.py*.**

In this step, I worked on the queries that are later imported into other files. First, I completed CREATE statements for each and every table. This includes stating all the needed columns, their data types and constraints. Then, I completed the DROP statements using the tables names I gave while doing CREATE statements.

**Creating the database and tables**

For creating the database, I used psql CREATE DATABASE command where I named the database *sparkifydb*. 

After creating a specific user that was needed for the project, I connected to it as such and used pgAdmin as an additional tool to interact and overlook the database while working on this project. I ran the *create_tables.py* file to connect to the database and create/drop tables. 

Then, I could check if the SQL queries from earlier have been implemented in the database. Occasionally, I used *test (2).ipynb* to run python scripts but for most of my testing I used pgAdmin.

**Building ETL processes**

This step focused on processing Songs and Logs data as well as inserting single files in the created database tables. Here I used JupyterLab, which I ran from PyCharm terminal, to work in a notebook dedicated to ETL processes.

ETL activity started with getting JSON files from **data/song_data/** to be later inserted into *songs* and *artists* tables. This is where I went back to *sql_queries.py* where I created INSERT statements for those two tables; then ran the inserts from *etl.ipynb*.

After that, it was time to do the same with Logs data from **data/log_data/**. Once done with a few transformations like getting proper time, user values, I went back to *sql_queries.py* and completed the INSERT statements for *users* and *time* tables; then ran the inserts from *etl.ipynb*.

Finally, I had to work on the *song_plays* table. It required additional query that joined *songs* and *artists* tables to get the full picture of artists and songs so that I could use the data from Songs (name, title, duration) and match them with Logs (artist name, title, length) to get *artist_id* and *song_id* in that table. Then, I completed the INSERT statement and ran the insert from *etl.ipynb*.

**Building ETL pipeline**

This was the final step in implementing the requested project, in which all the data files from Songs and Logs were processed, meaning that the data was extracted, transformed and loaded into the tables accordingly. For the ETL pipeline, I worked in *etl.py* file. I used certain parts from *etl.ipynb* to complete/run the script.

**Song play analysis examples**

Here I share a few examples of song play analysis.

*Example 1: Where do our listeners come from?*

![Example 1](https://i.postimg.cc/8PntxNpT/Screenshot-33.png)

*Example 2: On average, how many songs a user plays during a session?*

![Example 2](https://i.postimg.cc/L6N8pQw9/Screenshot-34.png)

*Example 3: Which gender is our app attracting most?*

![Example 3](https://i.postimg.cc/rwRGR4Sr/Screenshot-35.png)