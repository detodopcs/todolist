
CREATE DATABASE tolist_db

-- Table: public.list_tasks

-- DROP TABLE IF EXISTS public.list_tasks;

CREATE TABLE IF NOT EXISTS public.list_tasks
(
    id integer NOT NULL DEFAULT nextval('list_tasks_id_seq'::regclass),
    tasks character varying(255) COLLATE pg_catalog."default" NOT NULL,
    iscompleted integer,
    CONSTRAINT list_tasks_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.list_tasks
    OWNER to postgres;