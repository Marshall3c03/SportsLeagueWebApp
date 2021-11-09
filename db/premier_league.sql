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
    home_team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    away_team_id INT REFERENCES teams(id) ON DELETE CASCADE,
    home_score INT,
    away_score INT,
    result VARCHAR(255)
);