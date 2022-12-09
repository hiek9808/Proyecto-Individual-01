create database movies_tv_shows_db;
use movies_tv_shows_db;

CREATE TABLE genre(
    genre_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE actor(
    actor_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE director(
    director_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NULL
);

CREATE TABLE platform(
    platform_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100)
);

CREATE TABLE catalog(
    catalog_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    type ENUM('movie', 'tv show') NOT NULL,
    country VARCHAR(25) NULL,
    release_year CHAR(4) NOT NULL,
    duration INTEGER NULL,
    measure_duration ENUM('min', 'season') NULL,
    rating VARCHAR(10) NULL,
    description TEXT NULL
);

CREATE TABLE catalog_genre(
    catalog_id INTEGER NOT NULL ,
    genre_id INTEGER NOT NULL ,
    PRIMARY KEY (catalog_id, genre_id),
    FOREIGN KEY (catalog_id) REFERENCES catalog(catalog_id),
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
);

CREATE TABLE catalog_actor(
    catalog_id INTEGER NOT NULL,
    actor_id INTEGER NOT NULL,
    PRIMARY KEY (catalog_id, actor_id),
    FOREIGN KEY (catalog_id) REFERENCES catalog(catalog_id),
    FOREIGN KEY (actor_id) REFERENCES actor(actor_id)
);

CREATE TABLE catalog_director(
    catalog_id INTEGER NOT NULL,
    director_id INTEGER NOT NULL,
    PRIMARY KEY (catalog_id, director_id),
    FOREIGN KEY (catalog_id) REFERENCES catalog(catalog_id),
    FOREIGN KEY (director_id) REFERENCES director(director_id)
);

CREATE TABLE catalog_platform(
    catalog_id INTEGER NOT NULL,
    platform_id INTEGER NOT NULL,
    date_added DATE NULL,
    PRIMARY KEY (catalog_id, platform_id),
    FOREIGN KEY (catalog_id) REFERENCES catalog(catalog_id),
    FOREIGN KEY (platform_id) REFERENCES platform(platform_id)
);