DROP TABLE IF EXISTS sights;
DROP TABLE IF EXISTS cities;
DROP TABLE IF EXISTS countries;


CREATE TABLE countries (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  description TEXT,
  visit Boolean
);

CREATE TABLE cities (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  visit Boolean,
  country_id INT NOT NULL REFERENCES countries(id) ON DELETE CASCADE
);

CREATE TABLE sights (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  visit Boolean,
  city_id INT NOT NULL REFERENCES cities(id) ON DELETE CASCADE
);









