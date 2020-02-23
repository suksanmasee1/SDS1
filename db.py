#
# from  pymongo import  MongoClient
# #uri= "mongodb://admin:admin1234@ds263048.mlab.com:63048/faceverification"
# # client = pymongo.MongoClient(uri)
# # database = client['faceverification']
# # collection = database['faces']
# #
# # #faces = collection.find({})
# # collection.insert_one({"name" : "sukaaaa","last": "saaaa"})
# con  = MongoClient("ds263048.mlab.com",
# 63048)
#
# db =con.get_database("faceverification")
#
# face = db.faceUser
#
# face.insert({"name":"sssssss","lname":"ssss"})
import pymongo
conn = pymongo.MongoClient('mongodb://admin:admin1234@ds263048.mlab.com:63048/')
print(conn)
db = conn['faceverification']
print(db)
coll = db.get_collection(db)

print(coll)
