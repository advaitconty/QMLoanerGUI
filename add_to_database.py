import pandas as pd
from pymongo import MongoClient
import secret
import certifi
import csv


def load_inventory_as_dict(file_path):
    inventory_list = []

    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            guitar = {
                '_id': row['Code'].replace(' ', ''),
                'brand': row['Brand'].strip(),
                'allocation': row['Allocation'],
                'region': row['Code'].split('/')[0],
                'serial': int(row['Code'].split('/')[1]),
                'remarks': row['REMARKS']
            }
            inventory_list.append(guitar)

    return inventory_list
def insert_document(document):
    client = MongoClient(secret.mongo_host_connection("spsgeloans", "SooteFlap"), tlsCAFile=certifi.where())
    possible_collections = ["Alhambra", "Synchronium", "Valencia", "Y. Chai"]
    db = client["inventory"]
    for item in document:
        if item['brand'] in possible_collections:
            collection = db[item['brand']]
        else:
            collection = db["Other"]

        collection.insert_one(item)

    client.close()

insert_document(load_inventory_as_dict("inventory.csv"))
