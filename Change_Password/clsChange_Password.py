from PyQt5.QtWidgets import QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox
from Change_Password.Change_Password import Ui_MainWindow
import sqlite3
class clsChange_Password(QMainWindow):
    def __init__(self):
        super(clsChange_Password,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.id=0
        self.setFixedHeight(250)
        self.setFixedWidth(390)
        self.ui.txtOldpassword.setFocus()
        self.conn = sqlite3.connect('DataBase.db')
        self.cursor = self.conn.cursor()
        self.ui.btnChange.clicked.connect(self.changeBtnClick)
        sql = "select * from User_table"
        self.cursor.execute(sql)

    def changeBtnClick(self):
        sql = f"select * from User_table where Password='{self.ui.txtOldpassword.text()}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        #oldPass = ""
        for row in result:
            #oldPass = str(row[2])
            if self.ui.txtOldpassword.text()!="":
                if self.ui.txtNewpassword.text()!="":
                        sql = f"update User_table set Password='{self.ui.txtNewpassword.text()}' where Password='{self.ui.txtOldpassword.text()}'"
                        self.cursor.execute(sql)
                        self.conn.commit()
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Info")
                        msg.setText("Password Change Successfully ")
                        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                        msg.setDefaultButton(QMessageBox.Ok)
                        result = msg.exec_()
                        self.ui.txtOldpassword.setText("")
                        self.ui.txtNewpassword.setText("")
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle("Info")
                    msg.setText("Password can not be blank Or Old Password Not Match")
                    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                    msg.setDefaultButton(QMessageBox.Ok)

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Info")
                msg.setText("Old Password Not Match")
                msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                msg.setDefaultButton(QMessageBox.Ok)
                result = msg.exec_()


