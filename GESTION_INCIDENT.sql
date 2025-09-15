-- Database: GESTION_INCIDENT

-- DROP DATABASE IF EXISTS "GESTION_INCIDENT";

CREATE DATABASE "GESTION_INCIDENT"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'French_Cameroon.1252'
    LC_CTYPE = 'French_Cameroon.1252'
    LOCALE_PROVIDER = 'libc'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;


	 -- création de la table incident--

     CREATE TABLE Incident (
    ID_Incident SERIAL PRIMARY KEY,
    Titre VARCHAR(255) NOT NULL,
    Description TEXT NOT NULL,
    Date_Signalement DATE,
    Statut VARCHAR(60) NOT NULL,
    Priorité VARCHAR(60) NOT NULL   
);


SELECT * FROM Incident

