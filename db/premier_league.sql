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

INSERT INTO teams (name,position,gamesplayed,wins,draws,loses,points) 
VALUES ('Chelsea',1,10,8,1,1,25);