# fname = input("Enter file name: ")
fh = open('mbox-short.txt')
count = 0
avg = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    numstr = line.find(' ')
    # print(float(line[numstr:].lstrip()))
    num = float(line[numstr:].lstrip())
    total+=num
    count +=1
    avg = total/count


print("Average spam confidence:",avg)
