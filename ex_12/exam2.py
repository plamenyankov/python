import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL:')
count = int(input('Enter count:'))
pos = int(input('Enter position:'))



# # Retrieve all of the anchor tags

while count >= 0:

    if len(url) < 1:
        url = "http://py4e-data.dr-chuck.net/known_by_Miles.html"
    print('Retriving:', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    cnt = 1

    for tag in tags:
        # print(cnt,pos)
        if cnt == pos:
            cnt = 0
            url = tag.get('href', None)
            # r = re.findall('by_(.*).html+',url)
            # print(r[0])
            # url = tag.get('href', None)
            break
        cnt+=1
    # print('Count:',count)
    count-=1
