from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    @classmethod
    def get(cls, name: str):
        store = StoreModel.find_store_by_name(name)
        if store:
            return store.json()

    @classmethod
    def post(cls, name: str):
        if StoreModel.find_store_by_name(name):
            return {"message": "Store alrady exists."}, 400

        store = StoreModel(name)

        try:
            store.save_to_database()
        except:
            return {"message": "An error occured while creating the store."}, 500

        return store.json(), 201

    @classmethod
    def delete(cls, name: str):
        store = StoreModel.find_store_by_name(name)
        if store:
            store.delete_from_database()
            return {"message": "store deleted."}

        return {"message": "store don't exist"}


class StoreList(Resource):

    @classmethod
    def get(cls):
        # return {"item": list(map(lambda x: x.json(), ItemModel.query.all()))}
        return {"stores": [store.json() for store in StoreModel.find_all()]}