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

CREATE TABLE tags (
  id SERIAL PRIMARY KEY,
  tag TEXT,
  user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE book_tags (
  id SERIAL PRIMARY KEY, 
  tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE, 
  book_id INTEGER REFERENCES books(id) ON DELETE CASCADE
);

CREATE TABLE blog_tags (
  id SERIAL PRIMARY KEY, 
  tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE, 
  book_id INTEGER REFERENCES blogs(id) ON DELETE CASCADE
);

CREATE TABLE podcast_tags (
  id SERIAL PRIMARY KEY, 
  tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE, 
  book_id INTEGER REFERENCES podcasts(id) ON DELETE CASCADE
);

CREATE TABLE video_tags (
  id SERIAL PRIMARY KEY, 
  tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE, 
  book_id INTEGER REFERENCES videos(id) ON DELETE CASCADE
);
