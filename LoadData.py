import pandas as pd
from app_fast_api.database.MysqlDB import MysqlDB

data = pd.read_csv("./datasets/all_data_cleaned.csv")

db = MysqlDB()

db.insert_all_data(data[1:])

