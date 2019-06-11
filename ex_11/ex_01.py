import re
fh = open('regex_sum_241802.txt')
lst = list()
for line in fh:
    result = re.findall('[0-9]+',line.rstrip())
    if len(result) > 0:
        for r in result:
            lst.append(int(r))
print(sum(lst))
