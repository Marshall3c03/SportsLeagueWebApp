DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS teams;

CREATE TABLE teams (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    position INT,
    gamesplayed INT,
    wins INT,
    draws INT,
    loses INT,
    points INT
);

CREATE TABLE matches (
    id SERIAL PRIMARY KEY,
    team_1 VARCHAR(255),
    team_2 VARCHAR(255),
    result VARCHAR(255)
);

INSERT INTO teams (name,position,gamesplayed,wins,draws,loses,points) 
VALUES ('Chelsea',1,11,8,2,1,26);

INSERT INTO teams (name,position,gamesplayed,wins,draws,loses,points) 
VALUES ('Man City',2,11,7,2,2,23);

INSERT INTO teams (name,position,gamesplayed,wins,draws,loses,points) 
VALUES ('West Ham',3,11,7,2,2,23);

INSERT INTO teams (name,position,gamesplayed,wins,draws,loses,points) 
VALUES ('Liverpool',4,11,6,4,1,22);

INSERT INTO teams (name,position,gamesplayed,wins,draws,loses,points) 
VALUES ('Arsenal',5,11,6,2,3,20);