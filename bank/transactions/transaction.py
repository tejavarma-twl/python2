# trans_id trans_sender trans_receiver trans_amount trans_mode trans_date trans_time

# CREATE TABLE `bank`.`transactions` ( `trans_id` INT NOT NULL AUTO_INCREMENT , 
# `trans_sender` INT NOT NULL , `trans_receiver` INT NOT NULL , 
# `trans_amount` FLOAT NOT NULL , `trans_mode` VARCHAR(5) NOT NULL , 
# `trans_createdon` DATETIME NOT NULL , `trans_status` VARCHAR(10) NOT NULL , 
# PRIMARY KEY (`trans_id`)) ENGINE = InnoDB;

from config import db

INSERT `transactions`

db.dbop.execute("UPDATE `account` SET `user_balance` = %s WHERE `user_id` = %s",(balance,id))
db.dbop.execute("UPDATE `account` SET `user_balance` = %s WHERE `user_id` = %s",(balance,id))

transactions = [
    {'trans_id':'123','trans_sender':'teja','trans_receiver':'avi',
'trans_amount':'2200000','trans_mode':'rtgs','trans_date':'6/19','trans_time':'9:00 am'},
{'trans_id':'123','trans_sender':'varma','trans_receiver':'avi',
'trans_amount':'2200000','trans_mode':'rtgs','trans_date':'6/19','trans_time':'9:00 am'},
{'trans_id':'123','trans_sender':'avi','trans_receiver':'teja',
'trans_amount':'2200000','trans_mode':'rtgs','trans_date':'6/19','trans_time':'9:00 am'},
{'trans_id':'123','trans_sender':'hari','trans_receiver':'teja',
'trans_amount':'2200000','trans_mode':'rtgs','trans_date':'6/19','trans_time':'9:00 am'},
]

mytransaction = []
mytransaction_debit = []
mytransaction_credit = []


def transfer():  #Transaction creation
    pass

def debited():    #Debit details of account
    for trans in transactions:
        if trans['trans_sender']=='teja':
            mytransaction_debit.append(trans)
    print(mytransaction_debit)

def credited():   #Credit details
    for trans in transactions:
        if trans['trans_receiver']=='teja':
            mytransaction_credit.append(trans)
    print(mytransaction_credit)

def allTransactions():   #Credit details
    for trans in transactions:
        if trans['trans_sender']=='teja' or trans['trans_receiver']=='teja':
            mytransaction.append(trans)
    print(mytransaction)

# print("Debit Transactions")
# debited()
# print("Credit Transactions")
# credited()
# print("All Transactions")
# allTransactions()