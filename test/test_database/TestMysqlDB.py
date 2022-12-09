import unittest
from apifast.database.MysqlDB import MysqlDB


class MyTestCase(unittest.TestCase):

    def test_insert_full_data(self):
        db = MysqlDB()
        catalog = [("Movie",'The Grand Seduction',"Don McKellar","Brendan Gleeson, Taylor Kitsch, Gordon Pinsent","Canada","March 30, 2021","2014", None, 113, "min","Comedy, Drama","A small fishing village must procure a local doctor to secure a lucrative business contract. When unlikely candidate and big city doctor Paul Lewis lands in their lap for a trial residence, the townsfolk rally together to charm him into staying. As the doctor's time in the village winds to a close, acting mayor Murray French has no choice but to pull out all the stops.", "amazon prime"),
                   ("TV show","pelicula 4","Don McKellar","Brendan Gleeson","Canada","2021-02-02","2014", None, 113, "min","Comedy","A small fishing village must procure a local doctor to secure a lucrative business contract. When unlikely candidate and big city doctor Paul Lewis lands in their lap for a trial residence, the townsfolk rally together to charm him into staying. As the doctor's time in the village winds to a close, acting mayor Murray French has no choice but to pull out all the stops.", "netflix")]

        db.insert_all_data(catalog)



if __name__ == '__main__':
    unittest.main()
