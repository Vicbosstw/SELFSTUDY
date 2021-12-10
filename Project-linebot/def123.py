# import flask related
from flask import Flask, request, abort
# import linebot related
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent,TextSendMessage,CarouselTemplate,CarouselColumn,PostbackEvent,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,URITemplateAction,PostbackTemplateAction, events
from linebot.models.messages import ImageMessage,TextMessage
import time
import json
from elasticsearch import Elasticsearch
from linebot.models.responses import Content
from linebot.models.template import ConfirmTemplate
import numpy as np
from pymongo import MongoClient, collection
from pymongo.errors import DuplicateKeyError
import random

secretFile=json.load(open("secretFile.json",'r'))
channelAccessToken=secretFile['channelAccessToken']
channelSecret=secretFile["channelSecret"]
ip = secretFile["IP"]
line_bot_api =LineBotApi(channelAccessToken)
handler=WebhookHandler(channelSecret)

def mongo_user_stored(self):
    connection = MongoClient(host=ip,port=27017)
    db = connection.kingstone
    collection = db['customers']
    try:
        collection.insert([self])
        print('已新增',self['_id'])
        print("----------")
    except DuplicateKeyError:
        collection.update({ '_id' : self['_id'] },{ '$addToSet': { 'tag': self['tag'][0] }})
        print("----------")
    except:
        print('已存在_id',self['_id'],'(因此不寫入)')
        print("----------")

def findbook_ISBN(ISBN):
    es = Elasticsearch(hosts=ip, port=9200)
    res = es.search(index="cleanbook_test", query={"match":{"ISBN":ISBN}})
    # print(res['hits']['hits'])
    # book = res['hits']['hits'][0]["_source"]
    for hit in res['hits']['hits']:
        global book_all
        book_all = hit["_source"]
        book_all.pop('書籍簡介')
        # print(book_all)
    return book_all

def random_choosebookISBN():  #按鈕樣版
    connection = MongoClient(host=ip,port=27017)
    db = connection.kingstone
    collection = db['inter']
    # allbooks = list(collection.find())
    chooseisbn = list(collection.aggregate([{'$project':{'_id':0,'ISBN':1}},{'$sample':{'size':3}}]))
    # chooseisbn[0] = chooseisbn[0]['ISBN']
    return [chooseisbn[0]['ISBN'],chooseisbn[1]['ISBN'],chooseisbn[2]['ISBN']]

def findyoumaybelike_ISBN(isbn):  #轉盤樣板
    connection = MongoClient(host=ip,port=27017)
    db = connection.kingstone
    collection = db['comment_all.json']
    data = collection.find({'ISBN':isbn})
    datas = list(data)[0]['list']
    return datas