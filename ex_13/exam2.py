import urllib.request, urllib.parse, urllib.error
import json
inp = dict({'key':42})
inp['address'] = input('Enter location:')
url = "http://py4e-data.dr-chuck.net/json?"
furl =url+ urllib.parse.urlencode(inp)
print('Retrieving:',furl)
req = urllib.request.urlopen(furl).read().decode()
print('Retrieved:',len(req), 'characters')
parse = json.loads(req)
print(parse['results'][0]['place_id'])
