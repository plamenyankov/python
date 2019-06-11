fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    list = line.rstrip().split()
    for l in list:
        if l not in lst:
            lst.append(l)
lst.sort()
print(lst)
