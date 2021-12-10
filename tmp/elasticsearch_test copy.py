from elasticsearch import Elasticsearch
from datetime import datetime
es = Elasticsearch(hosts='localhost', port=9200)
index_mapping = { "mappings":
                     { "properties": 
                        { "id": { "type": "long" }, 
                          "age": { "type": "integer" }, 
                          "time": { "type": "date" }, 
                          "name": { "type": "keyword" }, 
                          "desc": { 
                            "type": "text", 
                            "analyzer": "whitespace", 
                            "search_analyzer": "whitespace"
                             }, 
                          "user": { "type": "object" } } 
                     } 
                }


