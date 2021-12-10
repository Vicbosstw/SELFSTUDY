# from pymongo import MongoClient, collection
# import json
# from jieba import cut_words
from elasticsearch import Elasticsearch
import json
es = Elasticsearch(
    cloud_id="TFB103:dXMtZWFzdC0xLmF3cy5mb3VuZC5pbyRjM2I1NDU5OWEwZmQ0MWEyODg4MThjYWY0ODI2YjBiMiRkNzllZjg5MWFhMzk0NTc3ODE4MjI4NTE4ZWJjNjg3NA==",
    http_auth=("elastic", "P1czxewpainpIigjt4hvFl9E"),
)

def create_index(es):
    body = dict()
    body['settings'] = get_setting()
    body['mappings'] = get_mappings()
    print(json.dumps(body)) #可以用json.dumps輸出來看格式有沒又包錯
    es.indices.create(index='school_members', body=body)


def get_setting():
    settings = {
        "index": {
            "number_of_shards": 3,
            "number_of_replicas": 2
        }
    }

    return settings


def get_mappings():
    mappings = {
        "properties": {
            "sid": {
                "type": "integer"
            },
            "name": {
                "type": "text"
            },
            "age": {
                "type": "integer"
            },
            "class": {
                "type": "keyword"
            }
        }
    }

    return mappings


if __name__ == "__main__":
    es = Elasticsearch(
    cloud_id="TFB103:dXMtZWFzdC0xLmF3cy5mb3VuZC5pbyRjM2I1NDU5OWEwZmQ0MWEyODg4MThjYWY0ODI2YjBiMiRkNzllZjg5MWFhMzk0NTc3ODE4MjI4NTE4ZWJjNjg3NA==",
    http_auth=("elastic", "P1czxewpainpIigjt4hvFl9E"),
)
    create_index(es)



# connection = MongoClient(host="localhost", port=27017)
# db = connection.kingstone
# collections = db['cleanbook']
# cursor = collection.find()
# # print(cursor.alive)

# for i in cursor:
#     db.collections.find({"書籍簡介":{'$exists': True}})