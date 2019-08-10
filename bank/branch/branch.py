# bank_id
# bank_name
# bank_branch
# bank_ifsc
# bank_branchcode
# bank_address

# CREATE TABLE `bank`.`branch` ( `bank_id` INT NOT NULL AUTO_INCREMENT , 
# `bank_name` VARCHAR(30) NOT NULL , `bank_branch` VARCHAR(20) NOT NULL , 
# `bank_ifsc` VARCHAR(15) NOT NULL , `bank_branchcode` VARCHAR(10) NOT NULL , 
# `bank_address` TEXT NOT NULL , PRIMARY KEY (`bank_id`)) ENGINE = InnoDB;

import mysql.connector as mysql

mydb = mysql.connect(host='localhost',user='root',password='',database='bank',port=3307)
# mydb2 = mysql.connect(host='localhost',user='root',password='admin',database='bank',port=3306)
dbop = mydb.cursor()
# dbop2 = mydb2.cursor()

def creation():
    bank_name = input("Bank Name")
    bank_branch = input("Bank Branch")
    bank_ifsc = input("Bank IFSC")
    bank_branchcode = input("Bank Branch Code")
    bank_address = input("Bank Address")

    try:
        res = dbop.execute("INSERT INTO `branch` (`bank_id`, `bank_name`, `bank_branch`, `bank_ifsc`, `bank_branchcode`, `bank_address`) VALUES (NULL, %s, %s, %s, %s, %s)",(bank_name,bank_branch,bank_ifsc,bank_branchcode,bank_address))
        # 'ICICI', 'Vizag', 'ICIC0000365', '0365', 'Dwarakanagar'
        mydb.commit()
    except mysql.Error as err:
        print("Failed inserting in database: {}".format(err))
        exit(1)

def getBanks():
    try:
        dbop.execute("SELECT * FROM `branch` WHERE `bank_name`='ICICI'")
        res = dbop.fetchall()
        for i in res:
            print(i)
        # for (bank_name, bank_branch, bank_ifsc) in dbop:
        #     print(bank_name, bank_branch, bank_ifsc)
    except mysql.Error as err:
        print("Failed retreiving in database: {}".format(err))
        exit(1)


def updation():
    try:
        res = dbop.execute("UPDATE `branch` SET `bank_ifsc` = 'ICIC0000365' WHERE `branch`.`bank_id` = 3")
        mydb.commit()
    except mysql.Error as err:
        print("Failed updating database: {}".format(err))
        exit(1)

    

