import pandas as pd
fhandle = open('lorem.txt')
# for index,l in enumerate(fhandle):
    # print(index,l)
text = fhandle.read().find('\n')
print(text)
# lspos = text.find('\n')
# print(lspos)

# print(fhandle.read())
# print(len(pd.Series(fhandle)))
# print(pd.Series(fhandle)[2])
