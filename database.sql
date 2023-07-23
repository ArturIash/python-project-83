DROP TABLE IF EXISTS urls;

CREATE TABLE urls (
  id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  name varchar(255) UNIQUE NOT NULL,
  created_at timestamp NOT NULL
);

DROP TABLE IF EXISTS url_checks;

CREATE TABLE url_checks (
  id bigint PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  url_id bigint REFERENCES urls (id),
  status_code int,
  h1 text,
  title text,
  description text,
  created_at timestamp NOT NULL
);