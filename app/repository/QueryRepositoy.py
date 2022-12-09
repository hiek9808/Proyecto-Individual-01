from app.database.MysqlDB import MysqlDB


class QueryRepository:

    def __init__(self):
        self.db = MysqlDB()

    def load_data(self, values):
        self.db.insert_all_data(values)

    def get_max_duration(self, year, platform, measure):
        return self.db.get_max_duration(year, platform, measure)

    def get_count_platform(self, platform):
        return self.db.get_count_platform(platform)

    def get_listedin(self, genre):
        return self.db.get_listedin(genre)

    def get_actor(self, platform, year):
        return self.db.get_actor(platform, year)
