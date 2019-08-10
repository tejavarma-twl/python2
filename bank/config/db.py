import mysql.connector as mysql

mydb = mysql.connect(host='localhost',user='root',password='',database='bank',port=3307)
dbop = mydb.cursor()