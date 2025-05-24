from flask_login import UserMixin
from . import mongo

class User(UserMixin):
    def __init__(self, user_doc):
        self.id = str(user_doc["_id"])
        self.username = user_doc["username"]
        self.password = user_doc["password"]

    @staticmethod
    def get_by_username(username):
        user_doc = mongo.db.users.find_one({"username": username})
        return User(user_doc) if user_doc else None

    @staticmethod
    def get_by_id(user_id):
        from bson import ObjectId
        user_doc = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        return User(user_doc) if user_doc else None