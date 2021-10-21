import pymongo as pym
import csv

def select():
    with open("abc.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile, delimiter =";")
        selected_dict = []
        for row in reader:
            selected_dict.append({"id": row["id"], "title": row["title"],"url": row["url"]})
        return selected_dict

print(select())

def insert_document(documentToInsert):
    client = pym.MongoClient("mongodb://localhost:27017")
    db = client["client_data"]
    coll = db["collection_1"]
    coll.insert_many(documentToInsert)

insert_document(select())