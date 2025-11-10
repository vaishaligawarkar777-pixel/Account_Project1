from PyQt5.QtWidgets import QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox
from Account.Account import Ui_MainWindow
import sqlite3
class clsAccount(QMainWindow):
    def __init__(self):
        super(clsAccount,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedHeight(650)
        self.setFixedWidth(600)
        self.ui.cmbSelectgroup.setFocus()
        self.conn = sqlite3.connect('DataBase.db')
        self.cursor = self.conn.cursor()
        self.ui.btnnew.clicked.connect(self.NewBtnClick)
        self.ui.btnsave.clicked.connect(self.SaveBtnClick)
        self.ui.btnupdate.clicked.connect(self.UpdateBtnClick)
        self.ui.btndelete.clicked.connect(self.DeleteBtnClick)
        sql = "select * from Group_Data"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            self.ui.cmbSelectgroup.addItem(str(row[1]))

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Sr_No","Group","Account Name"])
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 150)
        self.ui.tableWidget.clicked.connect(self.tableClick)
        self.loadDataInTable()

    def loadDataInTable(self):
        self.cursor.execute(f"select * from Account_Data")
        result = self.cursor.fetchall()
        self.ui.tableWidget.setRowCount(0)
        rw = 0
        for row in result:
            rw = int(rw) + 1
            self.ui.tableWidget.setRowCount(rw)
            self.ui.tableWidget.setItem(rw - 1, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(rw - 1, 1, QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(rw - 1, 2, QTableWidgetItem(str(row[2])))

    def tableClick(self):
        cr=self.ui.tableWidget.currentRow().__index__()
        print(cr)
        self.Sr_No= self.ui.tableWidget.item(cr,0).text()
        #self.ui.cmbSelectgroup.currentText(self.ui.tableWidget.item(cr,1).text())
        self.ui.txtAccountname.setText(self.ui.tableWidget.item(cr,1).text())

    def NewBtnClick(self):
        self.ui.cmbSelectgroup.currentText("")
        self.ui.txtAccountname.setText("")

    def SaveBtnClick(self):
        Selectgroup = self.ui.cmbSelectgroup.currentText()
        sql = f"insert into Account_Data values(null,'{Selectgroup}','{self.ui.txtAccountname.text()}')"
        self.cursor.execute(sql)
        self.conn.commit()
        self.loadDataInTable()

    def UpdateBtnClick(self):
        Selectgroup = self.ui.cmbSelectgroup.currentText()
        sql = f"Update Account_Data set Group='{Selectgroup}',Accountname='{self.ui.txtAccountname.text()}' where Sr_No='{self.Sr_No}'"
        self.cursor.execute(sql)
        self.conn.commit()
        self.loadDataInTable()

    def DeleteBtnClick(self):
        self.cursor.execute(f"delete from Account_Data where Sr_No={self.Sr_No}")
        self.conn.commit()
        self.loadDataInTable()


