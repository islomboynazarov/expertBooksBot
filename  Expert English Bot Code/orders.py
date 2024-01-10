import sqlite3

conn = sqlite3.connect('orders.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         ( 
         ID     TEXT    NOT NULL,
         price         TEXT    NOT NULL,
         oid     TEXT    NOT NULL,
         pname     TEXT    NOT NULL,
         username     TEXT    NOT NULL,
         date     TEXT    NOT NULL,
         address     TEXT    NOT NULL,
         productID     TEXT    NOT NULL,
         status     TEXT    NOT NULL
        
);''')
print ("Table created successfully")
conn.close()#ID,price,oid,pname,username,date,productID,status,number,address