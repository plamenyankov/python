import re
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
mydict = dict()
for line in fh:
    if line.startswith('From '):
    # if re.search('From ',line):
        # print(line)
        ln = line.split()
        tmp = ln[-2].split(':')[0]
        mydict[tmp] = mydict.get(tmp,0)+1

tmp2 = sorted([(k,v) for k,v in mydict.items()])
for k,v in tmp2:
    print(k,v)
# print(sorted([(k,v) for k,v in mydict.items()]))
