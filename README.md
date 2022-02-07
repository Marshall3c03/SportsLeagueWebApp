# Premier League Sports League Application

![](https://seeklogo.com/images/P/premier-league-new-logo-D22A0CE87E-seeklogo.com.png) 

## About

<table>
  <tr>
    A web application built using Python, communicating with a PostgreSQL database using Psycopg2 as an adapter. The front-end is displayed using Flask.
  </tr>
  <tr>
    The app allows the user to add teams within the preimer league, then add match results reflecting the current league results. This updates the table that is located on the homepage.
  </tr>
</table>

## Site

### Homepage

![](Insert Table Page)

### Teams
![](Insert Teams Page)

### Matches
![](Insert Matches Page)

### About
![](Insert About Page)

## How to Run
----------

### Client:

Start the application in development mode. running this command will open ( http://localhost:5000 ) in a browser to view the application:

    flask run

### Creating the DB:

To get the application running you must install all the dependencies:

    createdb -d premier_league

Then creating the tables within the db:

    psql -d premier_league -f db/premier_league.sql

### If Postgres is not working try:

If you are getting a Postgres related issue try the following:

    brew uninstall postgresql

    brew install postgresql@13

    brew services start postgresql@13

    brew link postgresql@13 --force

## Built with 

- [Python]
- [Flask]
- [PostgreSQL]