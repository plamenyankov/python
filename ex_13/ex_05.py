import xml.etree.ElementTree as ET
data = '''<stuff>
<users>
<user x="3">
<id>001</id>
<name>Chuck</name>
</user>
<user x="7">
<id>005</id>
<name>Pancho</name>
</user>
</users>
</stuff>'''

tree = ET.fromstring(data)
lst = tree.findall('users/user')
for l in lst:
    print('Attr:',l.get('x'))
    print('Id:',l.find('id').text)
