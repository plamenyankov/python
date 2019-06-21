import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (email TEXT,count INTEGER)')

fname = input('Enter filename: ')

if (len(fname) < 1): fname ='../ex_10/mbox-short.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    email = line.split()[1]
    row = cur.execute('SELECT * FROM Counts WHERE email=?',(email,))
    if (row.fetchone() is None):
        cur.execute('INSERT INTO Counts (email, count) VALUES (?,1)',(email,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE email=?',(email,))
    conn.commit()
sql = 'SELECT email,count FROM Counts ORDER BY count DESC LIMIT 100'

for row in cur.execute(sql):
    print(row[0],row[1])
