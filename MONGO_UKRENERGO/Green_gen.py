import pymongo
import pandas as pd

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["GB_analytics_alternative"]
mycol = mydb["PSO_tariffs"]
new_coll = mydb["Monthly_report"]

def monthly_report(file):
    monthly_report = pd.read_excel(file, header=0)
    monthly_report = monthly_report.melt(id_vars=["IPS/BEI", "EIC-W", "ЄДРПОУ", "X", "Назва", "Alias W", "Параметр", "Обсяг"])
    row_data = monthly_report.to_dict(orient="records")
    mydb.Monthly_report.insert_many(row_data)

monthly_report("1.xlsx")