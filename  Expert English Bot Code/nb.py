import sqlite3 

conn = sqlite3.connect('shop.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (name          TEXT     NOT NULL,
         price         TEXT    NOT NULL,
         productID          TEXT    NOT NULL,
         image         TEXT    NOT NULL,
         link        TEXT    NOT NULL,
         description        TEXT    NOT NULL,
         category         TEXT    NOT NULL

);''')#name,price,image,productID,category
print ("Table created successfully")

conn.close()