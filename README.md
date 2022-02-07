# Premier League Sports League Application

![](https://seeklogo.com/images/P/premier-league-new-logo-D22A0CE87E-seeklogo.com.png) 

## About

<table>
  <tr>
    A web application built using Python, communicating with a PostgreSQL database using Psycopg2 as an adapter. The front-end is displayed using Flask.
  </tr>
  <tr>
    The app allows the user to add teams within the preimer league, then add match results reflecting the current league results. This updates the table that is located on the homepage.
    Each team has an individual team page that breaks down their current league form.
  </tr>
</table>

## Site

### Homepage

![](https://i.imgur.com/ZbXA3hD.png)

### Teams
![](https://i.imgur.com/vTQbI43.png)

### Individual Team
![](https://i.imgur.com/qaFScK1.png)

### Fixtures
![](https://i.imgur.com/7uEWgO9.png)

### Individual Fixture
![](https://i.imgur.com/Ron40Uf.png)

### About
![](https://i.imgur.com/ppTMzqx.jpg)

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

What I'm pleased With
---------------------

 - As this was my first project, I was happy to have learned the fundamentals of Python and pair that with a framework of Flask to create my first ever web application.
 - I feel the css is to a good standard given this was my first experience in CSS styling.
 - Getting a table to display with the relative information was a great feeling, then adding the logic to update league points via matches played was another amazing achievement.

Possible improvements
---------------------

 - Ability to change leagues (SPFL, Seria A, La Liga, Bundesliga)
 - Add goal difference functionality.
 - Allow user to upload a club crest in the create team page.
 - Research into API's to pull all match data
 - Add a calendar on the fixtures page
 - UserExperience:
    -   Implement good sizing conventions around the whole web-application.
    -   Re-vamp the fixtures pages to reflect more like official premier league fixture page.
    -   Style more elements (Buttons, Text fields)
    -   Create responsive CSS designs to accomodate all screen-sizes.