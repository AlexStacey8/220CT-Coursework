import sqlite3 as sql

con = sql.connect('Question1.db')
cur = con.cursor()

#Creating my Tables

#ISS_Missions table


cur.execute('''CREATE TABLE ISS_Mission
(Mission_No CHAR(8) NOT NULL,
Agcy_No INT NOT NULL,
Mission_Date DATE,
Total_Weight INT);''')

#creating Agency Table

cur.execute('''CREATE TABLE Agency
(
Agcy_No INT NOT NULL,
Lead_Agency VARCHAR(255),
Country VARCHAR(255)
);''')

#Creating Equipment list table

cur.execute('''CREATE TABLE Equipment_List
(	
Mission_No CHAR(8) NOT NULL,
Equipment VARCHAR(255),
Quantity INT,
Item_Weight INT
);''') 


                
con.close()


