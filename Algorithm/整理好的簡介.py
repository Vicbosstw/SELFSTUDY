import pymongo
import pandas as pd
from pymongo import MongoClient
MONGO_HOST = '10.2.14.10'
MONGO_DB = 'kingstone'
MONGO_COLLETION = 'clean_data'

def connect_mongo():  #連線資料庫
    global collection
    client = MongoClient(MONGO_HOST, 27017)
    db = client[MONGO_DB]
    collection = db[MONGO_COLLETION]

connect_mongo()  #呼叫連線資料庫函式
cursor = collection.find()  #依query查詢資料
df=  pd.DataFrame(list(cursor))  #轉換成DataFrame
del df['_id']
df['ISBN'] = df['ISBN'].astype('str')  # 確認 ISBN 為字串
df.head()
