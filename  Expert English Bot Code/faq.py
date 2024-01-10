import sqlite3 

conn = sqlite3.connect('faq.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (
         question          TEXT    NOT NULL,
         answer       TEXT    NOT NULL,
         code      TEXT    NOT NULL
);''') 
print ("Table created successfully")