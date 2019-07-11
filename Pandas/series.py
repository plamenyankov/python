import pandas as pd
def convert_currency(val):
    """
    Convert the string number value to a float
     - Remove $
     - Remove commas
     - Convert to float type
    """
    new_val = val.replace(',','').replace('$', '')
    return float(new_val)
csv = pd.read_csv('test.csv')
csv['2016'] = csv['2016'].apply(convert_currency).astype('float')
csv['2017'] = csv['2017'].apply(convert_currency).astype('float')
# print(csv[['2016','2017']])
csv['Sum 16-17'] = csv['2016'] > csv['2017']
csv2016 = csv['2016'].sort_values(ascending = False)
print(csv2016)
# print(csv[['2016','2017','Sum 16-17']])
# df = csv['2016'].apply(lambda x: x.replace('$','').replace(',','')).astype('float')
# df2 = csv['2017'].apply(lambda x: x.replace('$','').replace(',','')).astype('float')
# print(df)
# print(df2)
# print(df + df2)
