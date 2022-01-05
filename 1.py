import json
import requests
response = requests.get("https://s3.amazonaws.com/open-to-cors/assignment.json")
d=json.loads(response.text)
print('data structure is ' + str(type(d)))
data=d['products']
valu=data.values()
valu=list(valu)
l=[]
for i in range(len(valu)):
    l.append(int(valu[i]['popularity']))

l.sort()
for i in range(len(valu)):
    print(valu[i])
