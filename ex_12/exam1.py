import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

inp = input('Enter url:')
if len(inp) < 1:
    inp = "http://py4e-data.dr-chuck.net/comments_241804.html"

data = urllib.request.urlopen(inp).read()

soup = BeautifulSoup(data,'html.parser')
tags = soup('span')
sum = 0
cnt = 0
for t in tags:
    cnt+=1
    sum += int(t.text)
print('Count:',cnt)
print('Sum:',sum)
