from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QMessageBox
from PyQt5.uic.properties import QtWidgets
from Transaction.Transaction import Ui_MainWindow
import sqlite3

class clsTransaction(QMainWindow):
    def __init__(self):
        super(clsTransaction, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedHeight(730)
        self.setFixedWidth(1020)
        self.ui.cmbSelectgroup.setFocus()
        self.conn = sqlite3.connect('DataBase.db')
        self.cursor = self.conn.cursor()
        self.ui.btnnew.clicked.connect(self.NewBtnClick)
        self.ui.btnsave.clicked.connect(self.SaveBtnClick)
        self.ui.btnupdate.clicked.connect(self.UpdateBtnClick)
        self.ui.btndelete.clicked.connect(self.DeleteBtnClick)
        self.ui.radReceived.setChecked(True)
        self.ui.cmbSelectgroup.addItem("Select Group")
        sql = "select * from Group_Data"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            self.ui.cmbSelectgroup.addItem(str(row[1]))

            self.ui.tableWidget.setColumnCount(3)
            self.ui.tableWidget.setHorizontalHeaderLabels(["Sr", "Date", "Amount"])
            self.ui.tableWidget.setColumnWidth(0, 50)
            self.ui.tableWidget.setColumnWidth(1, 150)
            self.ui.tableWidget.setColumnWidth(2, 150)

            self.ui.tableWidget_2.setColumnCount(3)
            self.ui.tableWidget_2.setHorizontalHeaderLabels(["Sr", "Date", "Amount"])
            self.ui.tableWidget_2.setColumnWidth(0, 50)
            self.ui.tableWidget_2.setColumnWidth(1, 150)
            self.ui.tableWidget_2.setColumnWidth(2, 150)

            Current_Date = QDate.currentDate()
            self.ui.dateEdit.setDate(Current_Date)

            self.ui.tableWidget.clicked.connect(self.tableClick)
            self.ui.tableWidget_2.clicked.connect(self.tableClick_2)
            self.loadDataInTable()
            self.ui.cmbSelectgroup.currentTextChanged.connect(self.groupSelect)

    def groupSelect(self):
        self.ui.cmbSelectAccount.clear()
        self.ui.cmbSelectAccount.addItem("Select Account")
        sql = f"select * from Account_Data where Group_Name='{self.ui.cmbSelectgroup.currentText()}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            self.ui.cmbSelectAccount.addItem(str(row[2]))

    def loadDataInTable(self):
        self.cursor.execute(f"select * from Transaction_Data")
        result = self.cursor.fetchall()
        self.ui.tableWidget.setRowCount(0)
        rw = 0
        for row in result:
            rw = rw + 1
            self.ui.tableWidget.setColumnCount(rw)
            self.ui.tableWidget.setItem(rw - 1, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(rw - 1, 1, QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(rw - 1, 2, QTableWidgetItem(str(row[2])))

        self.ui.tableWidget_2.setRowCount(0)
        rw = 0
        for row in result:
            rw = rw + 1
            self.ui.tableWidget_2.setColumnCount(rw)
            self.ui.tableWidget_2.setItem(rw - 1, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget_2.setItem(rw - 1, 1, QTableWidgetItem(str(row[1])))
            self.ui.tableWidget_2.setItem(rw - 1, 2, QTableWidgetItem(str(row[2])))

    def tableClick(self):
        cr = self.ui.tableWidget.currentRow().__index__()
        print(cr)
        self.id = self.ui.tableWidget.item(cr, 0).text()
        self.ui.cmbSelectgroup.setCurrentText(self.ui.tableWidget.item(cr, 1).text())
        self.ui.cmbSelectAccount.setCurrentText(self.ui.tableWidget.item(cr, 2).text())
        S_Date = self.ui.tableWidget.item(cr, 3).text()
        S_Date = S_Date.split("/")
        F_Date = (int(S_Date[0]), int(S_Date[1]), int(S_Date[2]))
        self.ui.radReceived.setDate(F_Date)
        Transaction_Type = self.ui.tableWidget.item(cr, 4).text()
        if Transaction_Type == "Received":
            self.ui.radReceived.setChecked(True)
        if Transaction_Type == "Payment":
            self.ui.radPayment.setChecked(True)
        self.ui.txtAmount.setText(self.ui.tableWidget.item(cr, 5).text())
        self.ui.textNote.setText(self.ui.tableWidget.item(cr, 6).text())

    def NewBtnClick(self):
        self.ui.cmbSelectgroup.currentText("")
        self.ui.cmbSelectAccount.setText("")
        self.ui.txtAmount.setText("")
        self.ui.textNote.setPlainText("")

    def SaveBtnClick(self):
        Selectgroup = self.ui.cmbSelectgroup.currentText()
        SelectAccount = self.ui.cmbSelectAccount.currentText()
        Date = self.ui.dateEdit.date().toString("yyyy/MM/dd")
        Transaction_Type = ""
        if self.ui.radReceived.isChecked():
            Transaction_Type = "Received"
        if self.ui.radPayment.isChecked():
            Transaction_Type = "Payment"

        sql = f"insert into Transaction_Data values(null,'{Selectgroup}','{SelectAccount}','{Date}','{Transaction_Type}','{self.ui.txtAmount.text()}','{self.ui.textNote.toPlainText()}')"
        self.cursor.execute(sql)
        self.conn.commit()
        self.loadDataInTable()

    def UpdateBtnClick(self):
        Selectgroup = self.ui.cmbSelectgroup.currentText()
        SelectAccount = self.ui.cmbSelectAccount.currentText()
        Date = (self.ui.dateEdit.date().toString("yyyy/MM/dd"))
        Transaction_Type = ""
        if self.ui.radReceived.isChecked():
            Transaction_Type = "Received"
        if self.ui.radPayment.isChecked():
            Transaction_Type = "Payment"
        sql = f"Update Transaction_Data set Group_Name='{Selectgroup}',Account_Name='{SelectAccount}',Date='{Date}',Transaction_Type'{Transaction_Type},'Amount='{self.ui.txtAmount.text()}',Note='{self.ui.textNote.toPlainText()}'"
        self.cursor.execute(sql)
        self.conn.commit()
        self.loadDataInTable()

    def DeleteBtnClick(self):
        self.cursor.execute(f"delete from Transaction_Data where Id={self.id}")
        self.conn.commit()
        self.loadDataInTable()