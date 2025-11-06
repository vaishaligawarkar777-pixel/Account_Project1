import sqlite3
from PyQt5.QtWidgets import QApplication
from MainWindow.clsMainWindow import clsMainWindow
from Login.clsLogin import clsLogin
import sys

app=QApplication([])
conn=sqlite3.connect('DataBase.db')
cursor=conn.cursor()
sql=f"select * from User_table"
cursor.execute(sql)
result=cursor.fetchall()
i=0
for row in result:
    i+=1
m=clsMainWindow()
f=clsLogin()

if i==0:
    m.show()
else:
    f.show()
sys.exit(app.exec_())