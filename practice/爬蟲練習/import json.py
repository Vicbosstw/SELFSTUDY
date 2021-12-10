import json
data = {'b': 10, 'a': 100}
output = json.dumps(data, sort_keys=True)
print(output)