# user_id
# user_name
# user_account
# user_address
# user_ifsc
# user_balance

# from ../config import db    
import os
import sys
import importlib
from config import db

def get_ifsc_code():
    db.dbop.execute("SELECT `bank_name`,`bank_address`,`bank_ifsc` FROM `branch`")
    res = db.dbop.fetchall()
    i = 1
    for r in res:
        print('Select',i,'for',r[0],r[1],r[2])
        i += 1
    branch = int(input('Select branch : '))
    if branch >=1 and branch <= len(res):
        return res[branch-1][2]

def create_account():
    ifsc    =   get_ifsc_code()
    name    =   input('Enter user name : ') # 'Teja'
    accno   =   input('Enter user account no : ') # '098876876876'
    address =   input('Enter user address : ') # 'Vizag'
    balance =   input('Enter user balance : ') # 100000

    db.dbop.execute("INSERT INTO `accounts` (user_name, user_account, user_address, user_ifsc, user_balance) VALUES (%s,%s,%s,%s,%s)",(name,accno,address,ifsc,balance))
    db.mydb.commit()


def update_account():
    pass
