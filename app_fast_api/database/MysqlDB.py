import mysql.connector


class MysqlDB:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="movies_tv_shows_db"
        )

    def insert_all_data(self, values):

        for value in values:
            type, title, directors, cast, country, date_added, release_year, rating, duration, measure_duration, \
                listed_in, description, platform = value
            mycursor = self.mydb.cursor()

            # buscamos si la pelicula o serie existe
            catalog_id_query = """SELECT catalog_id FROM catalog WHERE title = %s"""
            mycursor.execute(catalog_id_query, (title,))
            catalog_id = mycursor.fetchone()

            # si no existe ingresamos la pelicula o serie
            if catalog_id is None:

                # ingresamos la pelicula o serie en la tabla catalog
                insert_catalog_query = """INSERT INTO catalog (title, type, country, release_year, duration, 
                                                                measure_duration, rating, description)
                                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"""
                catalog = (title, type, country, release_year, duration, measure_duration, rating, description)
                mycursor.execute(insert_catalog_query, catalog)

                # obtenemos catalog_id de la pelicula o serie que acabamos de ingresamos
                mycursor.execute(catalog_id_query, (title,))
                catalog_id = mycursor.fetchone()

                # ingresamos los generos de la pelicula o serie
                for genre in listed_in.split(", "):

                    # obtenemos genre_id si existe
                    genre_id_query = """SELECT genre_id FROM genre WHERE name = %s LIMIT 1"""
                    mycursor.execute(genre_id_query, (genre,))
                    genre_id = mycursor.fetchone()

                    # si no existe el genero lo ingresamos
                    if genre_id is None:
                        # ingresamos el nuevo genero en la tabla genre
                        insert_genre_query = """INSERT INTO genre (name) VALUE (%s)"""
                        mycursor.execute(insert_genre_query, (genre,))

                        # obtenemos genre_id del genero que acabamos de ingresar
                        mycursor.execute(genre_id_query, (genre,))
                        genre_id = mycursor.fetchone()

                    # ingresamos la relacion de catalog con genre
                    insert_catalog_genre_query = """INSERT INTO catalog_genre(catalog_id, genre_id) VALUES (%s, %s)"""
                    mycursor.execute(insert_catalog_genre_query, (catalog_id[0], genre_id[0]))

                # ingresamos los actores de la pelicula o serie
                for actor in cast.split(", "):

                    # obtenemos actor_id si existe
                    actor_id_query = """SELECT actor_id FROM actor WHERE name = %s LIMIT 1"""
                    mycursor.execute(actor_id_query, (actor,))
                    actor_id = mycursor.fetchone()

                    # si no existe el actor los ingresamos
                    if actor_id is None:
                        # ingresamos el nuevo actor
                        insert_actor_query = """INSERT INTO actor (name) VALUE (%s)"""
                        mycursor.execute(insert_actor_query, (actor,))

                        # obtenemos actor_id que acabamos de ingresar
                        mycursor.execute(actor_id_query, (actor,))
                        actor_id = mycursor.fetchone()

                    # ingresamos la relacion de catalog con actor
                    insert_catalog_actor_query = """INSERT INTO catalog_actor (catalog_id, actor_id) VALUES (%s, %s)"""
                    mycursor.execute(insert_catalog_actor_query, (catalog_id[0], actor_id[0]))

                # ingresamos los directores de la pelicula o serie
                for director in directors.split(", "):

                    # obtenemos director_id si existe
                    director_id_query = """SELECT director_id FROM director WHERE name = %s LIMIT 1"""
                    mycursor.execute(director_id_query, (director,))
                    director_id = mycursor.fetchone()

                    # si no existe el director los ingresamos
                    if director_id is None:
                        # ingresamos el nuevo director
                        insert_director_query = """INSERT INTO director (name) VALUE (%s)"""
                        mycursor.execute(insert_director_query, (director,))

                        # obtenemos director_id que acabamos de ingresar
                        mycursor.execute(director_id_query, (director,))
                        director_id = mycursor.fetchone()

                    # ingresamos la relación de catalog con director
                    insert_catalog_director_query = """INSERT INTO catalog_director (catalog_id, director_id) 
                                                       VALUE (%s, %s) """
                    mycursor.execute(insert_catalog_director_query, (catalog_id[0], director_id[0]))

            # obtenemos platform_id si existe
            platform_id_query = """SELECT platform_id FROM platform WHERE name = %s LIMIT 1"""
            mycursor.execute(platform_id_query, (platform,))
            platform_id = mycursor.fetchone()

            # si no existe la plataforma la ingresamos
            if platform_id is None:
                # ingresamos la nueva plataforma en la tabla platform
                insert_platform_query = """INSERT INTO platform (name) VALUE (%s)"""
                mycursor.execute(insert_platform_query, (platform,))

                # obtenemos platform_id de la plataforma que acabamos de ingresar
                mycursor.execute(platform_id_query, (platform,))
                platform_id = mycursor.fetchone()

                # ingresamos la relación de catalog con plataforma
                insert_catalog_platform_query = """INSERT INTO catalog_platform (catalog_id, platform_id) 
                                                                   VALUE (%s, %s)"""
                mycursor.execute(insert_catalog_platform_query, (catalog_id[0], platform_id[0]))

            # obtenemos la si hay relacion entre catalog y platform
            catalog_platform_id_query = """SELECT catalog_id, platform_id FROM catalog_platform 
                                           WHERE catalog_id = %s AND platform_id = %s"""
            mycursor.execute(catalog_platform_id_query, (catalog_id[0], platform_id[0]))
            catalog_platform_id = mycursor.fetchone()

            # si no existe relacion ingresamos la relacion
            if catalog_platform_id is None:
                # ingresamos la relación de catalog con plataforma
                insert_catalog_platform_query = """INSERT INTO catalog_platform (catalog_id, platform_id, date_added) 
                                                                                   VALUES (%s, %s, %s)"""
                mycursor.execute(insert_catalog_platform_query, (catalog_id[0], platform_id[0], date_added))

            self.mydb.commit()

    def get_max_duration(self, year, platform, measure):
        query = """SELECT c.title FROM catalog c
                   INNER JOIN catalog_platform cp ON c.catalog_id = cp.catalog_id
                   INNER JOIN platform p on cp.platform_id = p.platform_id
                   WHERE release_year = %s AND p.name = %s AND measure_duration = %s
                   ORDER BY c.duration DESC LIMIT 1"""
        mycursor = self.mydb.cursor()
        mycursor.execute(query, (year, platform, measure))
        return mycursor.fetchone()

    def get_count_platform(self, platform):
        query = """ SELECT
                        p.name AS platform,
                        SUM(IF(type = 'movie', 1, 0)) AS movie,
                        SUM(IF(type = 'tv show', 1, 0)) AS tvshow
                    FROM catalog c
                    INNER JOIN catalog_platform cp ON c.catalog_id = cp.catalog_id
                    INNER JOIN platform p on cp.platform_id = p.platform_id
                    WHERE p.name = %s """
        mycursor = self.mydb.cursor()
        mycursor.execute(query, (platform,))
        return mycursor.fetchone()

    def get_listedin(self, genre):
        query = """ SELECT  p.name AS platform, COUNT(*) AS cantidad
                    FROM catalog c
                    INNER JOIN catalog_platform cp ON c.catalog_id = cp.catalog_id
                    INNER JOIN platform p ON cp.platform_id = p.platform_id
                    INNER JOIN catalog_genre cg ON c.catalog_id = cg.catalog_id
                    INNER JOIN genre g on cg.genre_id = g.genre_id
                    WHERE g.name = %s
                    GROUP BY p.name
                    ORDER BY cantidad DESC LIMIT 1;"""
        mycursor = self.mydb.cursor()
        mycursor.execute(query, (genre,))
        return mycursor.fetchone()

    def get_actor(self, platform, year):
        query = """ SELECT p.name AS platform, COUNT(*) AS cantidad, a.name AS actores
                    FROM catalog c
                    INNER JOIN catalog_actor ca on c.catalog_id = ca.catalog_id
                    INNER JOIN actor a on ca.actor_id = a.actor_id
                    INNER JOIN catalog_platform cp ON c.catalog_id = cp.catalog_id
                    INNER JOIN platform p on cp.platform_id = p.platform_id
                    WHERE p.name = %s AND c.release_year = %s
                    GROUP BY a.name
                    ORDER BY cantidad DESC LIMIT 1;"""
        mycursor = self.mydb.cursor()
        mycursor.execute(query, (platform, year))
        return mycursor.fetchone()
