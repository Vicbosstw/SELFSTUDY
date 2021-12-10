from elasticsearch import Elasticsearch
from datetime import datetime
es = Elasticsearch(hosts='10.2.18.6', port=9200)
res = es.search(index="kingstone", body={"query":{"match_all":{}}})
print(res)
for hit in res['書名']['ISBN']:
    print(hit["_source"])


