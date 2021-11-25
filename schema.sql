--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3
-- Dumped by pg_dump version 13.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: books; Type: TABLE; Schema: public; Owner: levantsi
--

CREATE TABLE public.books (
    id integer NOT NULL,
    author text,
    title text,
    type text,
    isbn text,
    user_id integer
);


ALTER TABLE public.books OWNER TO levantsi;

--
-- Name: books_courses; Type: TABLE; Schema: public; Owner: levantsi
--

CREATE TABLE public.books_courses (
    id integer NOT NULL,
    course_id integer,
    book_id integer
);


ALTER TABLE public.books_courses OWNER TO levantsi;

--
-- Name: books_courses_id_seq; Type: SEQUENCE; Schema: public; Owner: levantsi
--

CREATE SEQUENCE public.books_courses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.books_courses_id_seq OWNER TO levantsi;

--
-- Name: books_courses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: levantsi
--

ALTER SEQUENCE public.books_courses_id_seq OWNED BY public.books_courses.id;


--
-- Name: books_id_seq; Type: SEQUENCE; Schema: public; Owner: levantsi
--

CREATE SEQUENCE public.books_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.books_id_seq OWNER TO levantsi;

--
-- Name: books_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: levantsi
--

ALTER SEQUENCE public.books_id_seq OWNED BY public.books.id;


--
-- Name: courses; Type: TABLE; Schema: public; Owner: levantsi
--

CREATE TABLE public.courses (
    id integer NOT NULL,
    name text
);


ALTER TABLE public.courses OWNER TO levantsi;

--
-- Name: courses_id_seq; Type: SEQUENCE; Schema: public; Owner: levantsi
--

CREATE SEQUENCE public.courses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.courses_id_seq OWNER TO levantsi;

--
-- Name: courses_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: levantsi
--

ALTER SEQUENCE public.courses_id_seq OWNED BY public.courses.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: levantsi
--

CREATE TABLE public.users (
    id integer NOT NULL,
    username text NOT NULL,
    password text NOT NULL
);


ALTER TABLE public.users OWNER TO levantsi;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: levantsi
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO levantsi;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: levantsi
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: books id; Type: DEFAULT; Schema: public; Owner: levantsi
--

ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public.books_id_seq'::regclass);


--
-- Name: books_courses id; Type: DEFAULT; Schema: public; Owner: levantsi
--

ALTER TABLE ONLY public.books_courses ALTER COLUMN id SET DEFAULT nextval('public.books_courses_id_seq'::regclass);


--
-- Name: courses id; Type: DEFAULT; Schema: public; Owner: levantsi
--

ALTER TABLE ONLY public.courses ALTER COLUMN id SET DEFAULT nextval('public.courses_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: levantsi
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: levantsi
--

COPY public.books (id, author, title, type, isbn, user_id) FROM stdin;
\.


--
-- Data for Name: books_courses; Type: TABLE DATA; Schema: public; Owner: levantsi
--

COPY public.books_courses (id, course_id, book_id) FROM stdin;
\.


--
-- Data for Name: courses; Type: TABLE DATA; Schema: public; Owner: levantsi
--

COPY public.courses (id, name) FROM stdin;
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: levantsi
--

COPY public.users (id, username, password) FROM stdin;
\.


--
-- Name: books_courses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: levantsi
--

SELECT pg_catalog.setval('public.books_courses_id_seq', 1, false);


--
-- Name: books_id_seq; Type: SEQUENCE SET; Schema: public; Owner: levantsi
--

SELECT pg_catalog.setval('public.books_id_seq', 1, false);


--
-- Name: courses_id_seq; Type: SEQUENCE SET; Schema: public; Owner: levantsi
--

SELECT pg_catalog.setval('public.courses_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: levantsi
--

SELECT pg_catalog.setval('public.users_id_seq', 1, false);


--
-- Name: books_courses books_courses_pkey; Type: CONSTRAINT; Schema: public; Owner: levantsi
--

ALTER TABLE ONLY public.books_courses
    ADD CONSTRAINT books_courses_pkey PRIMARY KEY (id);


--
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: levantsi
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);


--
-- Name: courses courses_pkey; Type: CONSTRAINT; Schema: public; Owner: levantsi
--

ALTER TABLE ONLY public.courses
    ADD CONSTRAINT courses_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: levantsi
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: users users_username_key; Type: CONSTRAINT; Schema: public; Owner: levantsi
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_username_key UNIQUE (username);


--
-- Name: books_courses books_courses_book_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: levantsi
--

ALTER TABLE ONLY public.books_courses
    ADD CONSTRAINT books_courses_book_id_fkey FOREIGN KEY (book_id) REFERENCES public.books(id);


--
-- Name: books_courses books_courses_course_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: levantsi
--

ALTER TABLE ONLY public.books_courses
    ADD CONSTRAINT books_courses_course_id_fkey FOREIGN KEY (course_id) REFERENCES public.courses(id);


--
-- Name: books books_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: levantsi
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id);


--
-- PostgreSQL database dump complete
--

