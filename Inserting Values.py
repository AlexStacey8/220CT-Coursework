import sqlite3 as sql

con = sql.connect('Question1.db')
cur = con.cursor()

#Inserting values into my ISS_Mission Table

cur.execute('''INSERT INTO ISS_Mission  VALUES ('ISS-2237',178,'20141214',211)''')
cur.execute('''INSERT INTO ISS_Mission VALUES ('ISS-3664',526,'20140116',1.20)''')
cur.execute('''INSERT INTO ISS_Mission VALUES ('ISS-2356',167,'20140212',69)''')
cur.execute('''INSERT INTO ISS_Mission VALUES ('ISS-1234',032,'20140416',2.5)''')

#Inserting vaules into my Agency table

cur.execute('''INSERT INTO Agency VALUES (178,'JAXA','Japan')''')
cur.execute('''INSERT INTO Agency VALUES (526,'ESA','EU')''')
cur.execute('''INSERT INTO Agency VALUES (167,'NASA','USA')''')
cur.execute('''INSERT INTO Agency VALUES (032,'Roskosmos','Russia')''')

#Inserting values into my Equipment_List table

cur.execute('''INSERT INTO Equipment_List VALUES ('ISS-2237','Portable water dispenser',2,100)''')
cur.execute('''INSERT INTO Equipment_List VALUES ('ISS-2237','Felxible Airduct',6,0.5)''')
cur.execute('''INSERT INTO Equipment_List VALUES ('ISS-2237','Small storage rack',4,2)''')

cur.execute('''INSERT INTO Equipment_List VALUES ('ISS-3664','Biofilter',6,0.2)''')

cur.execute('''INSERT INTO Equipment_List VALUES ('ISS-2356','Small storage rack',3,2)''')
cur.execute('''INSERT INTO Equipment_List VALUES ('ISS-2356','Battery Pack',2,5)''')
cur.execute('''INSERT INTO Equipment_List VALUES ('ISS-2356','Urine transfer tubing',2,1.5)''')
cur.execute('''INSERT INTO Equipment_List VALUES ('ISS-2356','O2 scrubber',1,50)''')

cur.execute('''INSERT INTO Equipment_List VALUES ('ISS-1234','Small storage rack',1,2)''')
cur.execute('''INSERT INTO Equipment_List VALUES ('ISS-1234','Flexible Airduct',2,0.5)''')

con.close()
