name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fh = open(name)
mydict = dict()
for line in fh:
    if line.startswith('From '):
        ln = line.split()
        mydict[ln[1]] = mydict.get(ln[1],0)+1
email = None
count = None
for key,val in mydict.items():
    if email is None or val > count:
        email = key
        count = val

print(email,count)
