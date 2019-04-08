import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

##new_doc = {'first': 'douglas','last': 'adams', 'dob': '11/03/1952','hair_color': 'grey','occupation': 'writer', 'nationality':'english'}
##coll.insert(new_doc)

##new_docs =[{'first': 'terry','last': 'pratchett', 'dob': '28/04/1948','hair_color': 'grey','occupation': 'writer', 'nationality':'english'}, {'first': 'george','last': 'rr martin', 'dob': '02/09/1948','hair_color': 'grey','occupation': 'writer', 'nationality':'english'}]
##coll.insert_many(new_docs)

##documents = coll.find()

##coll.remove({'first':'douglas'})

coll.update_many({'nationality': 'american'}, {'$set': {'hair_color':'multi-coloured'}})

documents = coll.find({'nationality':'american'})

for doc in documents:
    print(doc)