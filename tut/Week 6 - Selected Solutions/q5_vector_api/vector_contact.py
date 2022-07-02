import urllib.request
import json

data = json.dumps({'v': [1, 2, 3], 'u' : [1, 5, 5]})

req = urllib.request.Request('http://localhost:9001/crossproduct',data=bytes(data, 'utf-8'), headers={'content-type':'application/json'})

res = urllib.request.urlopen(req)

s = res.read()

print(s)
