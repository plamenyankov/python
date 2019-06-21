import urllib.request, urllib.parse, urllib.error
import json

inp = input('Enter location:')

if(len(inp) < 1):
    inp = "http://py4e-data.dr-chuck.net/comments_241807.json"

req = urllib.request.urlopen(inp).read().decode()
print('Retrieved:',len(req), 'characters')
parse = json.loads(req)
sum = 0
count = 0
for com in parse['comments']:
    sum+= int(com['count'])
    count+=1
print('Count:',count)
print('Sum:',sum)
