import  pymongo

_author_ = 'suksan'

import pymongo
from  pymongo import  MongoClient
uri= "mongodb://admin:admin1234@ds263048.mlab.com:63048/faceverification"
client = pymongo.MongoClient(uri)
database = client['faceverification']
collection = database['faces']

faces = collection.find({})

for x in faces:
    print(x)

mydict = {"name" : "baruk","name": "suss"}
x  = collection.insert_one(mydict)
