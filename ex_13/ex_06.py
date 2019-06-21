import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    url = "http://py4e-data.dr-chuck.net/comments_241806.xml"
parms = dict()
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx).read()
print('Retrieved', len(uh), 'characters')
tree = ET.fromstring(uh)
lst = tree.findall('.//comment')
sum = 0
charl = 0
count = 0;
for l in lst:
    charl+=int(len(l.find('name').text))
    sum+=int(l.find('count').text)
    count+=1
print('Count:',count)
print('Sum:',sum)
