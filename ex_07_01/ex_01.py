fh = open('mbox-short.txt')
# print(fh.read())
emails = []
uemails = []
for line in fh:
    if not line.startswith('From'):
        continue
    pos = line.find('@')
    epos = line.find(' ',pos)
    spos = line.rfind(' ',0,pos)
    # line = line.rstrip()
    # print(pos,epos)
    uemails.append(line[spos+1:epos])
    if line[spos+1:epos] in emails:
        continue
    else:
        emails.append(line[spos+1:epos])
# for em in emails:
    # print(em)

import pandas as pd

ue = pd.Series(uemails)
print(len(emails))
print(len(uemails))
print(ue.unique())
print('The lenght of array',len(ue.unique()))
