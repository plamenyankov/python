import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT,count INTEGER)')

fname = input('Enter filename: ')

if (len(fname) < 1): fname ='mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    email = line.split()[1].split('@')[1]
    row = cur.execute('SELECT * FROM Counts WHERE org=?',(email,))
    if (row.fetchone() is None):
        cur.execute('INSERT INTO Counts (org, count) VALUES (?,1)',(email,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org=?',(email,))
    conn.commit()
sql = 'SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sql):
    print(str(row[0]),row[1])
cur.close()
