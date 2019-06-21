import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
# ctx = ssl._create_unverified_context()
html = urllib.request.urlopen('https://free-proxy-list.net/',context=ctx).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('a')
# print(len(tags))
dict = dict()
for tag in tags:
    t = tag.get('class',None)
    if t is not None:
        for tt in t:
            dict[tt] = dict.get(tt,0)+1
lst2 = list()
for (k,v) in dict.items():
    lst2.append((v,k))
for (k,v) in sorted(lst2,reverse = True):
    print(v,k)
# print(fh.read())
# lst =list()
# for line in fh:
#     result = re.findall('href="(.+)"',line.decode().rstrip())
#     if len(result) > 0:
#         for r in result:
#             lst.append(r)
# for l in lst:
#     print(l)
