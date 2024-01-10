from telegram.error import TelegramError
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
import datetime
import sqlite3
import random
import telegram.ext
from datetime import date
from datetime import datetime, timedelta
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler,CallbackQueryHandler
from datetime import datetime as er
import xlwt
from openpyxl import load_workbook
import sqlite3 as sql
import os
from sqlite3 import Error
from telegram import KeyboardButton
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import re
heelp=['admin wil update']
import logging

wallo=['bc1qnjh086d833wkdfs5z36x72fxuwjysgtyks0fqr']

man=[]
AB,PPR,CATEX,DESCRIP,IMGE,BUTTON,PTYPE,DELETE,MCAT,DELCAT,WALL,ABD,JE,LOG,KAKAK,FFAQ,KUNG,PDM,PDB=range(19)
from telegram import LabeledPrice, ShippingOption
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    PreCheckoutQueryHandler,
    ShippingQueryHandler,
)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
wc=['www']
import ast
import requests
from telegram import ParseMode
def start(update, context):
    print(update.effective_user.id)
    user = update.message.from_user
    usa=str(update.effective_user.id)
    userg = update.message.from_user
    xg=er.today().strftime("%m/%d/%Y, %H:%M:%S")
    try:
        usaf=userg.username
    except:
        usaf=userg.first_name#1394902938
  

    connection = sqlite3.connect("wallet.db")  
    cursor = connection.cursor()  
    cursor.execute("SELECT id FROM COMPANY where id= {}".format(int(update.effective_user.id))) 
    jobs = cursor.fetchall()
    if len(jobs) ==0: 
                cursor.execute("INSERT INTO COMPANY (ID,balance ,link,code,pid,ppr,ct,amount,payment,tref,refby,sub,name,allow,uname,address,number,post,province,street,note,tome) \
                    VALUES ({}, '{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(int(update.effective_user.id),"0","0","0","0","0","0","0","0","0","0","0",usaf,"0","0","0","0","0","0","0","0",xg))
                connection.commit()
                connection.close() 
                conn = sqlite3.connect('cart.db') 
                conn.execute("INSERT INTO COMPANY (ID,name,productID,price) \
                        VALUES ('{}', '{}','{}', '{}')".format(str(update.effective_user.id),'0','0','0'))
                conn.commit()
    if usa=='1394902938' or usa=='114524870':
            keyboard =[[InlineKeyboardButton("➕ Book", callback_data="1"),InlineKeyboardButton("❌ Book", callback_data="2")],
                    [InlineKeyboardButton("Add category", callback_data="32"),InlineKeyboardButton("Delete Category", callback_data="90")],
                    [InlineKeyboardButton("🛒 Orders", callback_data="99v"),InlineKeyboardButton("🛒 Users Log", callback_data="llo")],
                    [InlineKeyboardButton("➕ FAQ", callback_data="1f"),InlineKeyboardButton("❌ FAQ", callback_data="2f")],
                    [InlineKeyboardButton("🔊 Announcement", callback_data="916"),InlineKeyboardButton("Shop logo", callback_data="8ab")],
                    [InlineKeyboardButton("User Side", callback_data="200"),InlineKeyboardButton("Add balance", callback_data="abda")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
            return BUTTON
    else:
        loc_keyboard1 = KeyboardButton(text="📕 Books")
        loc_keyboard2 = KeyboardButton(text="💵 Wallet")
        loc_keyboard3 = KeyboardButton(text="🗓 Orders")
        loc_keyboard4 = KeyboardButton(text="☎️ Support")
        keyboard = [[loc_keyboard1,loc_keyboard3],[loc_keyboard2,loc_keyboard4]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
        return BUTTON 
def button(update,context):
    h=update.effective_user.id
    query = update.callback_query
    a=query.data
    if a== '1':
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_message(chat_id=update.effective_user.id,text='Send name of Book',reply_markup=reply_markup)
        return AB
    elif a=='100':
            keyboard =[[InlineKeyboardButton("➕ Book", callback_data="1"),InlineKeyboardButton("❌ Book", callback_data="2")],
                    [InlineKeyboardButton("Add category", callback_data="32"),InlineKeyboardButton("Delete Category", callback_data="90")],
                    [InlineKeyboardButton("🛒 Orders", callback_data="99v"),InlineKeyboardButton("🛒 Users Log", callback_data="llo")],
                    [InlineKeyboardButton("➕ FAQ", callback_data="1f"),InlineKeyboardButton("❌ FAQ", callback_data="2f")],
                    [InlineKeyboardButton("🔊 Announcement", callback_data="916"),InlineKeyboardButton("Shop logo", callback_data="8ab")],
                    [InlineKeyboardButton("User Side", callback_data="100"),InlineKeyboardButton("Add balance", callback_data="abda")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Welcome to admin Dashboard" ,reply_markup=reply_markup)
            return BUTTON
    elif a=='2':
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_message(chat_id=update.effective_user.id,text='Send ProductID to delete',reply_markup=reply_markup)
        return DELETE
    elif a=='200':
        loc_keyboard1 = KeyboardButton(text="📕 Books")
        loc_keyboard2 = KeyboardButton(text="💵 Wallet")
        loc_keyboard3 = KeyboardButton(text="🗓 Orders")
        loc_keyboard4 = KeyboardButton(text="☎️ Support")
        keyboard = [[loc_keyboard1,loc_keyboard3],[loc_keyboard2,loc_keyboard4]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
        return BUTTON 
    elif a=='32':   
            keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Send name of category',reply_markup=reply_markup)
            return MCAT
    elif a=='90':
        keyf=[]
        conn = sqlite3.connect('cat.db')
        cursor = conn.execute("SELECT cat from COMPANY")
        conn.commit()
        keyf=[]
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[0])]
            keyf.append(c)
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True ) 

        context.bot.send_message(chat_id=update.effective_user.id,text="Select the category to delete",reply_markup=reply_markup)  
        return DELCAT
    elif a== '1f':
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Send question of FAQs",reply_markup=reply_markup)
        return ABD
    elif a== '916':
            keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Send announcement message',reply_markup=reply_markup)
            return JE
    elif a=='8ab':   
            keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Send shop logo',reply_markup=reply_markup)
            return LOG
    elif a=='abda':   
            keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='Send User ID to add balance',reply_markup=reply_markup)
            return KAKAK
    elif a=='99v':
            style = xlwt.easyxf('font: bold 1, color black;')
            conn = sqlite3.connect('orders.db') 
            cursor = conn.execute("SELECT ID,price,oid,pname,username,date,productID,status,address from COMPANY ")
            conn.commit() 
            jobs = cursor.fetchall()
            if len(jobs) !=0:
                f = open("orders.txt", "w",encoding="utf-8")
                conn = sqlite3.connect('orders.db') 
                cursor = conn.execute("SELECT ID,price,oid,pname,username,date,productID,status,address from COMPANY  ")
                conn.commit()
                xa="Orders\n"
                i=0
                j=0
                workbook = xlwt.Workbook()
                sheet = workbook.add_sheet("Order History")
                sheet.write(i, 1, "order_id", style)
                sheet.write(i, 2, "user_id", style)
                sheet.write(i, 3, "date",  style)
                sheet.write(i, 4, "Product Name",  style)
                sheet.write(i, 5, "Price",  style)
                sheet.write(i, 6, "Users_name",  style)

                for row in cursor:
                        i=i+1
                        j=j+1
                        inv=row[0]
                        vgy=row[1]
                        xdrt=row[2]
                        sheet.write(i, 1, row[2], style)
                        sheet.write(i, 2, row[0], style)
                        sheet.write(i, 3, row[5],  style)
                        sheet.write(i, 4, row[3],  style)
                        sheet.write(i, 5, row[1],  style)
                        sheet.write(i, 6, row[4],  style)
                workbook.save("orders.xls")
                keyboard =[[InlineKeyboardButton("Main Menu", callback_data="100")]]
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                context.bot.send_document(chat_id=update.effective_user.id,document=open('orders.xls', 'rb'),reply_markup=reply_markup)
            else:
                    keyboard =[[InlineKeyboardButton("❌", callback_data="100")]]
                    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text="You have no orders",reply_markup=reply_markup)
                    return BUTTON
    elif a=="ff":    
        conn = sqlite3.connect('faq.db')
        cursor = conn.execute("SELECT question,code from COMPANY ")
        conn.commit()
        keyf=[]
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[1])]
            keyf.append(c) 
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True ) 
        context.bot.send_message(chat_id=update.effective_user.id,text="Select Question to read out",reply_markup=reply_markup)
        return FFAQ
    elif a=='buy':
        cc=update.callback_query.message.caption
        fg=cc
        cc=cc.replace("$","")
        cf=update.callback_query.message.message_id
        dd=cc.split("𝐁𝐨𝐨𝐤 𝐍𝐚𝐦𝐞:")
        dd=dd[1]
        dd=dd.split("𝐏𝐫𝐨𝐝𝐮𝐜𝐭𝐈𝐃:: ")
        dd=dd[0]
        dd=dd.strip()

        ccv=cc.split("𝐏𝐫𝐨𝐝𝐮𝐜𝐭𝐈𝐃: ")
        ccv=ccv[1]
        ccv=ccv.split("𝐏𝐫𝐢𝐜𝐞: ")
        ccv=ccv[0]
        ccv=ccv.strip() 

        rr=cc.split("𝐏𝐫𝐢𝐜𝐞: ")
        rr=rr[1]
        rr=rr.split("𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧: ")
        rr=rr[0]
        rr=rr.strip()        
        print(rr)     
        conn = sqlite3.connect('cart.db')
        cursor=conn.execute("UPDATE COMPANY set name='{}',productID='{}',price='{}' where ID = {}".format(dd,ccv,rr,int(update.effective_user.id)))
        conn.commit()
        conn = sqlite3.connect('cart.db')
        cursor = conn.execute("SELECT price from COMPANY where id= '{}' ".format(update.effective_user.id))
        conn.commit()
        for row in cursor:
            ffa=float(row[0])
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("SELECT link from COMPANY where productID= '{}' ".format(ccv))
        conn.commit()
        for row in cursor:
            poda=row[0]

        conn = sqlite3.connect('wallet.db')
        cursor = conn.execute("SELECT balance,name from COMPANY where id= '{}' ".format(update.effective_user.id))
        conn.commit()
        for row in cursor:
            ff=float(row[0])
            tep=row[1]
            tola=float(ff)-float(ffa)
            if ff>=ffa:   
                    yu= random.randint (0,999999)
                    xg=er.today().strftime("%m/%d/%Y, %H:%M:%S")
                    conn = sqlite3.connect('orders.db')
                    conn.execute("INSERT INTO COMPANY (ID,price,oid,pname,username,date,productID,status,address) \
                                        VALUES ('{}', '{}','{}','{}','{}','{}','{}','{}','{}')".format(str(update.effective_user.id),ffa,yu,dd,tep,xg,ccv,'Pending','N/A'))
                    conn.commit()
                    context.bot.send_message(chat_id=1394902938,text='You have a new order ')
                    keyboard =[[InlineKeyboardButton("Click Here", url='{}'.format(poda))]]
                    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
                    context.bot.send_message(chat_id=update.effective_user.id,text='Cick the button Below to download the book. Thanks',reply_markup=reply_markup)
                    return BUTTON
            else:             
                keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="200")]]
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
                context.bot.send_message(chat_id=update.effective_user.id,text="Your balance is not enough".format(update.effective_user.id),reply_markup=reply_markup)
                return BUTTON 
def ffaq(update,context):#PDB,PDVM,PDV,SAL
    query = update.callback_query
    msg=query.data
    conn = sqlite3.connect('faq.db')
    cursor = conn.execute("SELECT question,answer from COMPANY where code= '{}' ".format(msg))
    conn.commit()
    for row in cursor:
        ff=row[0]
        rr=row[1]
        keyboard =[[InlineKeyboardButton("Back to FAQs", callback_data="ff")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Question: {}\n\nAnswer: {}".format(ff,rr),reply_markup=reply_markup)
        return BUTTON 
def jos(update,context):
    msg=update.message.text
    print(msg)
    if msg=='📕 Books':
        conn = sqlite3.connect('cat.db')
        cursor = conn.execute("SELECT cat from COMPANY")
        conn.commit()
        keyf=[] 
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[0])]
            keyf.append(c) 
        b=[InlineKeyboardButton("Back", callback_data='🌎Main Menu')]
        keyf.append(b) 
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True ) 
        context.bot.send_message(chat_id=update.effective_user.id,text="Select category to view the Books.",reply_markup=reply_markup)
        return PDM
    elif msg=='💵 Wallet':#t0J60jhxFVBjTywgbu7kCMLJZNdqhfSzVFBQAhjRzrQ
        conn = sqlite3.connect('wallet.db')
        cursor = conn.execute("SELECT balance,tref from COMPANY where ID= {} ".format(int(update.effective_user.id)))
        conn.commit()
        for row in cursor:
            hj=float(row[0])
            hj=round(hj, 2)
            keyboard =[[InlineKeyboardButton("Add Balance", callback_data="1bal"),InlineKeyboardButton("🔙 Back", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text='WalletID: {}\nBalance: {}$'.format(str(update.effective_user.id),row[0]),reply_markup=reply_markup)
            return BUTTON 
    elif msg=="🗓 Orders":
        conn = sqlite3.connect('orders.db')
        cursor = conn.execute("SELECT ID,price,oid,pname,username,date,productID,date,address,status from COMPANY where ID ='{}'".format(update.effective_user.id))
        conn.commit()
        for row in cursor: 
            g="\nUserID:  "+row[0]+"\nOrderID: "+row[2]+"\nProduct Name: "+row[3]+"\nPrice: "+row[1]+'$'+"\nUser name:  "+row[4]+"\nDate: "+row[7]+"\n\n"
            keyboard =[[InlineKeyboardButton("🔙 Cancel", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text=g,reply_markup=reply_markup)
        return BUTTON  
    elif msg=='☎️ Support':
            keyboard =[[InlineKeyboardButton("📜 FAQs", callback_data="ff"),InlineKeyboardButton("Contact us", url='https://t.me/bonco1')]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
            context.bot.send_message(chat_id=update.effective_user.id,text="Please Read through FAQ’S before sending message to admin.\n\n",reply_markup=reply_markup)
            return BUTTON
def pdm(update,context):#PDB,PDVM,PDV,SAL
    query = update.callback_query
    msg=query.data
    print(msg)    
    c=update.callback_query.message.message_id
    context.bot.delete_message(chat_id=update.effective_user.id,
                        message_id=c)
    if msg=="🌎Main Menu":
        loc_keyboard1 = KeyboardButton(text="📕 Books")
        loc_keyboard2 = KeyboardButton(text="💵 Wallet")
        loc_keyboard3 = KeyboardButton(text="🗓 Orders")
        loc_keyboard4 = KeyboardButton(text="☎️ Support")
        keyboard = [[loc_keyboard1,loc_keyboard3],[loc_keyboard2,loc_keyboard4]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
        return BUTTON 
    elif msg=="200":
        loc_keyboard1 = KeyboardButton(text="📕 Books")
        loc_keyboard2 = KeyboardButton(text="💵 Wallet")
        loc_keyboard3 = KeyboardButton(text="🗓 Orders")
        loc_keyboard4 = KeyboardButton(text="☎️ Support")
        keyboard = [[loc_keyboard1,loc_keyboard3],[loc_keyboard2,loc_keyboard4]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
        return BUTTON 
    else:
        conn = sqlite3.connect('wallet.db')
        cursor=conn.execute("UPDATE COMPANY set ct = '{}' where ID = {}".format(msg,int(update.effective_user.id)))
        conn.commit()
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("SELECT name from COMPANY where category= '{}' ".format(msg))  
        conn.commit()                             
        keyf=[]
        jobs = cursor.fetchall()
        if len(jobs) !=0:
            conn = sqlite3.connect('shop.db')
            cursor = conn.execute("SELECT name from COMPANY where category= '{}' ".format(msg))
            conn.commit()
            for row in cursor:
                c=[InlineKeyboardButton(row[0], callback_data=row[0])]
                keyf.append(c)
            b=[InlineKeyboardButton("Back", callback_data='🌎Main Menu')]
            keyf.append(b)
            reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True )
            context.bot.send_message(chat_id=update.effective_user.id,text="📕 Books\n\nSelect Name of Book to View ",reply_markup=reply_markup)            
            return PDB
        else: 
            keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
            reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
            context.bot.send_message(chat_id=update.effective_user.id,text='This Category has no 📕 Books',reply_markup=reply_markup)
            return BUTTON
def pdb(update,context):#PDB,PDVM,PDV,SAL
    query = update.callback_query
    msg=query.data
    print(msg)    
    c=update.callback_query.message.message_id
    context.bot.delete_message(chat_id=update.effective_user.id,
                        message_id=c)
    if msg=="🌎Main Menu":
        conn = sqlite3.connect('cat.db')
        cursor = conn.execute("SELECT cat from COMPANY")
        conn.commit()
        keyf=[] 
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[0])]
            keyf.append(c) 
        b=[InlineKeyboardButton("Back", callback_data='🌎Main Menu')]
        keyf.append(b) 
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True ) 
        context.bot.send_message(chat_id=update.effective_user.id,text="Select category to view the products.",reply_markup=reply_markup)
        return PDM
    elif msg=="200":
        loc_keyboard1 = KeyboardButton(text="🛒 Store")
        loc_keyboard2 = KeyboardButton(text="💵 Wallet")
        loc_keyboard3 = KeyboardButton(text="🗓 Orders")
        loc_keyboard4 = KeyboardButton(text="☎️ Support")
        keyboard = [[loc_keyboard1,loc_keyboard3],[loc_keyboard2,loc_keyboard4]]
        reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_photo(chat_id=update.effective_user.id,photo=open('logo.jpg','rb'),caption=wc[0],reply_markup=reply_markup)
        return BUTTON 
    else:
            conn = sqlite3.connect('wallet.db')
            cursor = conn.execute("SELECT ct from COMPANY where ID={} ".format(str(update.effective_user.id)))
            conn.commit()
            for names in cursor:
                hjj=names[0] 
            conn = sqlite3.connect('shop.db')
            cursor = conn.execute("SELECT name from COMPANY where name='{}' AND category= '{}'".format(msg,hjj))                              
            keyf=[]
            jobs = cursor.fetchall()
            if len(jobs) !=0:
                conn = sqlite3.connect('shop.db')
                cursor = conn.execute("SELECT name,price,productID,image,description from COMPANY where name='{}' AND category= '{}'".format(msg,hjj))  
                for row in cursor:                               
                    m="𝐁𝐨𝐨𝐤 𝐍𝐚𝐦𝐞: {}\n𝐏𝐫𝐨𝐝𝐮𝐜𝐭𝐈𝐃: {}\n𝐏𝐫𝐢𝐜𝐞: {}$\n𝐃𝐞𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧: {}".format(row[0],row[2],row[1],row[4])

                    keyboard =[[InlineKeyboardButton("Buy Now", callback_data="buy")],[InlineKeyboardButton("🔙 Back", callback_data="200d")]]
                    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
                    context.bot.send_photo(chat_id=update.effective_user.id,photo=row[3],caption=m,reply_markup=reply_markup)
                    return BUTTON
            else:
                keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="200")]]
                reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
                context.bot.send_message(chat_id=update.effective_user.id,text='This Category has no Items',reply_markup=reply_markup)
                return BUTTON 
def kakak(update,context):
    msg=update.message.text
    global xtar
    xtar=msg
    conn = sqlite3.connect('wallet.db')
    cursor = conn.execute("SELECT ID from COMPANY  where ID = '{}'".format(msg))
    conn.commit()
    jobs = cursor.fetchall()
    if len(jobs) !=0:

        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_message(chat_id=update.effective_user.id,text="Send Balance in digit only",reply_markup=reply_markup)
        return KUNG
    else:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_message(chat_id=update.effective_user.id,text="Invalid ID",reply_markup=reply_markup)
        return KAKAK
def kung(update,context):
    msg=update.message.text
    try:
        msg=float(msg)
        connection = sqlite3.connect("wallet.db")  
        cursor = connection.cursor()  
        cursor.execute("SELECT balance FROM COMPANY where id= {}".format(int(xtar)) )
        for names in cursor:
            inv=float(names[0])
        bn=inv+msg
        bn=str(bn)
        conn = sqlite3.connect("wallet.db")  
        conn.execute("UPDATE COMPANY set balance = '{}' where ID = {}".format(bn,int(xtar)))
        conn.commit()
        conn.close()
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_message(chat_id=update.effective_user.id,text="Balance added",reply_markup=reply_markup)
        return BUTTON
    except:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_message(chat_id=update.effective_user.id,text="Send balance in digits only",reply_markup=reply_markup)
        return KUNG
def log(update,context):
    msg=update.message.photo[-1].file_id
    newFile = context.bot.getFile(msg)
    newFile.download('logo.jpg')
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='Logo edited successfully',reply_markup=reply_markup)
    return BUTTON
def je(update,context):
        msg=update.message.text
        conn = sqlite3.connect('wallet.db')
        cursor = conn.execute("SELECT ID from COMPANY")
        conn.commit()
        for row in cursor:
            aa=row[0]
            try:
                context.bot.send_message(chat_id=aa,text=msg)
            except:
                pass
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
        context.bot.send_message(chat_id=update.effective_user.id,text="Message Sent",reply_markup=reply_markup)
        return BUTTON
def abd(update,context):
    msg=update.message.text
    global papa
    papa=msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="Send answer of FAQs",reply_markup=reply_markup)
    return WALL
def wall(update,context):
    msg=update.message.text
    yu= random.randint (0,999999)
    conn = sqlite3.connect('faq.db')
    conn.execute("INSERT INTO COMPANY (question,answer,code) \
                        VALUES ('{}','{}','{}')".format(papa,msg,yu))
    conn.commit()  
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="FAQ added",reply_markup=reply_markup)
    return BUTTON
def delcat(update,context):
    c=update.callback_query.message.message_id
    query = update.callback_query
    msg=query.data
    conn = sqlite3.connect('cat.db')
    cursor = conn.execute("DELETE from COMPANY where cat='{}'".format(msg))
    conn.commit()
    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
    context.bot.send_message(chat_id=update.effective_user.id,text="Category Deleted",reply_markup=reply_markup)
    return BUTTON
def mcat(update,context):
    msg=update.message.text
    conn = sqlite3.connect('cat.db')
    conn.execute("INSERT INTO COMPANY (cat) \
                        VALUES ('{}')".format(msg))
    conn.commit()

    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text="category added successfully" ,reply_markup=reply_markup)
    return BUTTON
def delete(update,context):
    msg=update.message.text
    conn = sqlite3.connect('shop.db')
    cursor = conn.execute("SELECT productID from COMPANY  where productID = '{}'".format(str(msg)))
    conn.commit()
    jobs = cursor.fetchall()
    if len(jobs) !=0:
        conn = sqlite3.connect('shop.db')
        cursor = conn.execute("DELETE  from COMPANY where productID='{}'".format(msg))
        conn.commit()

        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_message(chat_id=update.effective_user.id,text="Product Deleted",reply_markup=reply_markup)
        return BUTTON
    else:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_message(chat_id=update.effective_user.id,text="Invalid ProductID",reply_markup=reply_markup)
        return DELETE
def ab(update,context):
    msg=update.message.text 
    global nm
    nm =msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Price of Book.',reply_markup=reply_markup)
    return PPR
def ppr(update,context):
    msg=update.message.text 
    global pri
    pri =msg
    try:
        msg=float(msg)
        keyf=[]
        conn = sqlite3.connect('cat.db')
        cursor = conn.execute("SELECT cat from COMPANY")
        conn.commit()
        keyf=[]
        for row in cursor:
            c=[InlineKeyboardButton(row[0], callback_data=row[0])]
            keyf.append(c)
        reply_markup = InlineKeyboardMarkup(keyf,resize_keyboard=True ) 
        context.bot.send_message(chat_id=update.effective_user.id,text="Select the Category for product",reply_markup=reply_markup)  
        return CATEX
    except:
        keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
        reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
        context.bot.send_message(chat_id=update.effective_user.id,text='Send Product Price in digits only.',reply_markup=reply_markup)
        return PPR
def catex(update,context):
    query = update.callback_query
    msg=query.data
    global categ
    categ =msg
    print(msg)
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Description of Product.',reply_markup=reply_markup)
    return DESCRIP
def descrip(update,context):
    msg=update.message.text 
    global desa
    desa =msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Link of book for user to download.',reply_markup=reply_markup)
    return PTYPE
def ptype(update,context):
    msg=msg=update.message.text
    global ptop
    ptop =msg
    keyboard =[[InlineKeyboardButton("🔙 Back", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True )
    context.bot.send_message(chat_id=update.effective_user.id,text='Send Image of Product.',reply_markup=reply_markup)
    return IMGE
def imge(update,context):
    msg=update.message.photo[-1].file_id
    yu= random.randint (0,999999)
    conn = sqlite3.connect('shop.db')
    conn.execute("INSERT INTO COMPANY (name,price,image,productID,category,description,link) \
                        VALUES ('{}', '{}','{}','{}','{}','{}','{}')".format(nm,pri,msg,yu,categ,desa,ptop))
    conn.commit()

    keyboard =[[InlineKeyboardButton("🌎Main Menu", callback_data="100")]]
    reply_markup = InlineKeyboardMarkup(keyboard,resize_keyboard=True,one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,text='Product added successfully',reply_markup=reply_markup)
    return BUTTON

  
def main():#AB,PPR,CATE,DESCRIP,IMGE
  updater = Updater("6281798688:AAGDEgt110g2ElXZkYtgf1BByiPvkzjDVrg", use_context=True)
  dp = updater.dispatcher
  conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start),MessageHandler(Filters.regex('^(📕 Books|👤 Seller|🛒 Store|💵 Wallet|🗓 Orders|☎️ Support|🔈 Channel|💬 Channel)$'), jos)],

        states={        
        BUTTON: [CallbackQueryHandler(button)],
        CATEX: [CallbackQueryHandler(catex)],
        PTYPE: [MessageHandler(Filters.text, ptype),CallbackQueryHandler(button)],
        AB: [MessageHandler(Filters.text, ab),CallbackQueryHandler(button)],
        PPR: [MessageHandler(Filters.text, ppr),CallbackQueryHandler(button)],
        DESCRIP: [MessageHandler(Filters.text, descrip),CallbackQueryHandler(button)],
        IMGE: [MessageHandler(Filters.photo, imge),CallbackQueryHandler(button)],
        DELETE: [MessageHandler(Filters.text, delete),CallbackQueryHandler(button)],
        MCAT: [MessageHandler(Filters.text, mcat),CallbackQueryHandler(button)],
        DELCAT: [CallbackQueryHandler(delcat)],
        WALL: [MessageHandler(Filters.text, wall),CallbackQueryHandler(button)],
        ABD: [MessageHandler(Filters.text, abd),CallbackQueryHandler(button)],
        JE: [MessageHandler(Filters.text, je),CallbackQueryHandler(button)],
        LOG: [MessageHandler(Filters.photo, log),CallbackQueryHandler(button)],
        KAKAK: [MessageHandler(Filters.text, kakak),CallbackQueryHandler(button)],
        FFAQ: [MessageHandler(Filters.text, ffaq),CallbackQueryHandler(button)],
        KUNG: [MessageHandler(Filters.text, kung),CallbackQueryHandler(button)],
        PDM: [CallbackQueryHandler(pdm)],
        PDB: [CallbackQueryHandler(pdb)],

        },  
        fallbacks=[CommandHandler('start', start)],#KUNG,KAKAK
        allow_reentry=True
     )
  dp.add_handler(conv_handler)
  updater.start_polling()
  updater.idle()
    
if __name__ == '__main__':
    main()
