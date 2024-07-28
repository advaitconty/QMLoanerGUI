from pymongo import MongoClient
import secret
import certifi

def reset_available_values(client, db_name):
    db = client[db_name]
    collections = db.list_collection_names()

    for collection_name in collections:
        collection = db[collection_name]
        update_result = collection.update_many(
            {},
            {"$set": {"available": True}}
        )
        print(f"Updated {update_result.modified_count} documents in collection '{collection_name}'")

def main():
    client = MongoClient(secret.mongo_host_connection("soote", "big", default=True), tlsCAFile=certifi.where())
    db_name = "inventory"  # replace with your database name
    reset_available_values(client, db_name)

if __name__ == '__main__':
    main()
