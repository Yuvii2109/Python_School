import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="yuvraj")
cur = mydb.cursor()
cur.execute('CREATE DATABASE bank_management_system')
