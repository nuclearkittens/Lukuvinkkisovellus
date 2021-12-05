CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username TEXT NOT NULL UNIQUE,
  password TEXT NOT NULL
  );

CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  author TEXT,
  title TEXT,
  description TEXT,
  type TEXT,
  isbn TEXT,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  marked_read TIMESTAMP
);

CREATE TABLE podcasts (
  id SERIAL PRIMARY KEY,
  title TEXT,
  episode TEXT,
  description TEXT,
  type TEXT,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  marked_read TIMESTAMP
);

CREATE TABLE blogs (
  id SERIAL PRIMARY KEY,
  author TEXT,
  title TEXT,
  url TEXT,
  description TEXT,
  type TEXT,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  marked_read TIMESTAMP
);

CREATE TABLE videos (
  id SERIAL PRIMARY KEY,
  title TEXT,
  url TEXT,
  description TEXT,
  type TEXT,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
  marked_read TIMESTAMP
);
