import json
from urllib.request import urlopen

url1 = "https://my-json-server.typicode.com/typicode/demo/posts"
response = urlopen(url1)
data_json1 = json.loads(response.read())


url2 = "https://my-json-server.typicode.com/typicode/demo/comments"
response = urlopen(url2)
data_json2 = json.loads(response.read())


from collections import defaultdict
d = defaultdict(dict)
for l in (data_json1, data_json2):
    for elem in l:
        d[elem['id']].update(elem)
l3 = d.values()

from operator import itemgetter
l3 = sorted(d.values(), key=itemgetter("id"))

jsonStr = json.dumps(l3)
print(jsonStr)