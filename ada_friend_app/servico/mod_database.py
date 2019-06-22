from pymongo import MongoClient

from ada_friend_app.config import MONGO_USER, MONGO_PWD, MONGO_IP, MONGO_PORT


class ModDatabase:
    def __init__(self, db, user=None, password=None,
                 host='localhost', port=27017):
        if user:
            self.__client = MongoClient(
                f'mongodb://{user}:{password}@{host}:{port}/{db}')
        else:
            self.__client = MongoClient(f'mongodb://{host}:{port}/{db}')

        self.__db = self.__client.get_database()

    def get_names_collections(self):
        return self.__db.collection_names()

    def get_columns(self, collection):
        columns = set()

        for data in self.get_document(collection):
            for column in data.keys():
                columns.add(column)
        return columns

    def get_document(self, collection, filter=None,
                     visible=None, max=0, sort=[('_id', 1)]):
        # ASCENDING = 1
        # DESCENDING = -1

        return [r for r in self.__db[collection].find(
            filter, visible).sort(sort).limit(max)]

    def get_distinct(self, collection, column):
        unq = self.__db[collection].distinct(column)
        count = [self.__db[collection].find({column: r}).count() for r in unq]

        return unq, count

    def __next_id(self, collection):
        try:
            _id = self.__db.seqs.find_and_modify(
                {'_id': collection}, {'$inc': {'id': 1}}, upsert=True)['id']
        except TypeError:
            _id = self.__db.seqs.find_and_modify(
                {'_id': collection}, {'$inc': {'id': 1}}, upsert=True)['id']

        return _id

    def set_document(self, collection, value, auto=False):
        if auto:
            value['_id'] = self.__next_id(collection)

        return self.__db[collection].insert_one(value).inserted_id

    def update_document(self, collection, filter, value):
        if '$push' not in value:
            value = {'$set': value}

        result = self.__db[collection].update_many(filter, value)

        return result.modified_count

    def delete_document(self, collection, filter):
        self.__db[collection].delete_one(filter)

    def len_collection(self, collection, filter=None):
        return self.__db[collection].find(filter).count()

    def drop_collection(self, collection):
        self.__db[collection].drop()
        self.__db.seqs.delete_one({'_id': collection})

    def __del__(self):
        self.__client.close()


class Database(ModDatabase):
    def __init__(self):
        super().__init__('ada-friend', MONGO_USER, MONGO_PWD, MONGO_IP, MONGO_PORT)
