import sqlite3 

conn = sqlite3.connect('wallet.db')
print ("Opened database successfully")

conn.execute('''CREATE TABLE COMPANY
         (ID INT PRIMARY KEY     NOT NULL,
         balance         TEXT    NOT NULL,
         code          TEXT    NOT NULL,
         pid          TEXT    NOT NULL,
         ppr         TEXT    NOT NULL,
         ct         TEXT    NOT NULL,
         sub         TEXT    NOT NULL,
         tref         TEXT    NOT NULL,
         uname     TEXT    NOT NULL,
         address     TEXT    NOT NULL,
         number     TEXT    NOT NULL,
         post     TEXT    NOT NULL,
         province     TEXT    NOT NULL,
         street     TEXT    NOT NULL,
         note     TEXT    NOT NULL,
         refby        TEXT    NOT NULL,
         payment         TEXT    NOT NULL,
         amount         TEXT    NOT NULL,
         name         TEXT    NOT NULL,
         tome         TEXT    NOT NULL,
         allow         TEXT    NOT NULL,
         link           TEXT    NOT NULL

);''')#uname,address,number,post,province,street,note
print ("Table created successfully")

conn.close()
