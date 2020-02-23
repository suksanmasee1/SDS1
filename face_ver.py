import face_recognition
from os import path

import pymongo

from pymongo import MongoClient

myclient = pymongo.MongoClient("mongodb://admin:admin1234@ds263048.mlab.com:63048/faceverification")
mydatabase = myclient['faceverification']
mycol = mydatabase['faces']


class Face:
    def __init__(self, app):
        self.storage_img = app.config["storage_img"]
        self.known_face_encodings = []
        self.known_face_names = []
        self.face_user_keys = {}
        self.load_all()
        self.db = app.db

    def load_user_by_index_key(self, index_key=0):
        key_str = str(index_key)
        if key_str in self.face_user_keys:
            return self.face_user_keys[key_str]
        return None

    def load_train_file_by_name(self, name):
        trained_storage = path.join(self.storage_img, 'trained')
        return path.join(trained_storage, name)

    def load_unknown_file_by_name(self, name):
        unknown_storage = path.join(self.storage, 'unknown')
        return path.join(unknown_storage, name)
    def load_all(self):
        results = self.db.find()





