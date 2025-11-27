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
        self.id =0
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

        Current_Date = QDate.currentDate()
        self.ui.dateEdit.setDate(Current_Date)
        #self.loadDataInTable()
        self.ui.cmbSelectgroup.currentTextChanged.connect(self.groupSelect)


        self.ui.Receivedtable.setColumnCount(4)
        self.ui.Receivedtable.setHorizontalHeaderLabels(["Sr", "Date", "Amount","Note"])
        self.ui.Receivedtable.setColumnWidth(3,350)
        self.ui.Paymenttable.setColumnCount(4)
        self.ui.Paymenttable.setHorizontalHeaderLabels(["Sr", "Date", "Amount", "Note"])
        self.ui.Paymenttable.setColumnWidth(3, 350)

        self.ui.cmbSelectgroup.addItem("Select Group")
        sql = "select * from Group_Data"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            self.ui.cmbSelectgroup.addItem(str(row[1]))

        self.ui.cmbSelectAccount.currentTextChanged.connect(self.loadTableData)
        self.ui.cmbSelectAccount.currentTextChanged.connect(self.loadTableDataPayment)
        self.ui.Receivedtable.clicked.connect(self.tableClick1)
        self.ui.Paymenttable.clicked.connect(self.tableClick2)

    def loadTableData(self):
        self.cursor.execute(f"select * from Transaction_Data where Account_Name='{self.ui.cmbSelectAccount.currentText()}' AND Transaction_Type='Received'")
        self.ui.Receivedtable.setRowCount(0)
        i = 0
        for row in self.cursor:
            i = int(i) + 1
            self.ui.Receivedtable.setRowCount(self.ui.Receivedtable.rowCount() + 1)
            rw = self.ui.Receivedtable.rowCount()
            self.ui.Receivedtable.setItem(rw - 1, 0, QTableWidgetItem(str(i)))
            self.ui.Receivedtable.setItem(rw - 1, 1, QTableWidgetItem(str(row[4])))
            self.ui.Receivedtable.setItem(rw - 1, 2, QTableWidgetItem(str(row[5])))
            self.ui.Receivedtable.setItem(rw - 1, 3, QTableWidgetItem(str(row[6])))

    def tableClick1(self):
        cr = self.ui.Receivedtable.currentRow().__index__()
        print(cr)
        self.id = self.ui.Receivedtable.item(cr, 0).text()
        print("Selected Id=",self.id)
        sdate = self.ui.Receivedtable.item(cr, 1).text()
        sdate = sdate.split("/")
        fdate = QDate(int(sdate[0]), int(sdate[1]), int(sdate[2]))
        self.ui.dateEdit.setDate(fdate)

        self.ui.txtAmount.setText(self.ui.Receivedtable.item(cr, 2).text())
        self.ui.textNote.setPlainText(self.ui.Receivedtable.item(cr, 3).text())


    def loadTableDataPayment(self):
        self.cursor.execute(f"select * from Transaction_Data where Account_Name='{self.ui.cmbSelectAccount.currentText()}' AND Transaction_Type='Payment'")
        self.ui.Paymenttable.setRowCount(0)
        i = 0
        for row in self.cursor:
            i = int(i) + 1
            self.ui.Paymenttable.setRowCount(self.ui.Paymenttable.rowCount() + 1)
            rw = self.ui.Paymenttable.rowCount()
            self.ui.Paymenttable.setItem(rw - 1, 0, QTableWidgetItem(str(i)))
            self.ui.Paymenttable.setItem(rw - 1, 1, QTableWidgetItem(str(row[4])))
            self.ui.Paymenttable.setItem(rw - 1, 2, QTableWidgetItem(str(row[5])))
            self.ui.Paymenttable.setItem(rw - 1, 3, QTableWidgetItem(str(row[6])))

    def tableClick2(self):
        cr = self.ui.Paymenttable.currentRow().__index__()
        print(cr)
        self.Id = self.ui.Paymenttable.item(cr, 0).text()
        sdate = self.ui.Paymenttable.item(cr, 1).text()
        sdate = sdate.split("/")
        fdate = QDate(int(sdate[0]), int(sdate[1]), int(sdate[2]))
        self.ui.dateEdit.setDate(fdate)
        self.ui.txtAmount.setText(self.ui.Paymenttable.item(cr, 2).text())
        self.ui.textNote.setPlainText(self.ui.Paymenttable.item(cr, 3).text())

    def groupSelect(self):
        self.ui.cmbSelectAccount.clear()
        self.ui.cmbSelectAccount.addItem("Select Account")
        sql = f"select * from Account_Data where Group_Name='{self.ui.cmbSelectgroup.currentText()}'"
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        for row in result:
            self.ui.cmbSelectAccount.addItem(str(row[2]))


    def NewBtnClick(self):
        self.ui.cmbSelectgroup.currentText("")
        self.ui.cmbSelectAccount.setText("")
        self.ui.txtAmount.setText("")
        self.ui.textNote.setPlainText("")

    def SaveBtnClick(self):
        Selectgroup = self.ui.cmbSelectgroup.currentText()
        SelectAccount = self.ui.cmbSelectAccount.currentText()
        Transaction_Type = ""
        if self.ui.radReceived.isChecked():
            Transaction_Type = "Received"
        elif self.ui.radPayment.isChecked():
            Transaction_Type = "Payment"
        else:
            QMessageBox.warning(self,"Warning","Please select Transaction Type!")
        Date = self.ui.dateEdit.date().toString("yyyy/MM/dd")

        sql = f"insert into Transaction_Data values(null,'{Selectgroup}','{SelectAccount}','{Transaction_Type}','{Date}','{self.ui.txtAmount.text()}','{self.ui.textNote.toPlainText()}')"
        self.cursor.execute(sql)
        self.conn.commit()
        #self.loadDataInTable()
        #self.loadTableDataPayment()

    def UpdateBtnClick(self):
        Selectgroup = self.ui.cmbSelectgroup.currentText()
        SelectAccount = self.ui.cmbSelectAccount.currentText()
        Transaction_Type = ""
        if self.ui.radReceived.isChecked():
            Transaction_Type = "Received"
        elif self.ui.radPayment.isChecked():
            Transaction_Type = "Payment"
        else:
            QMessageBox.warning(self, "Warning", "Please select Transaction Type!")
        Date = self.ui.dateEdit.date().toString("yyyy/MM/dd")

        sql = f"update Transaction_Data set Group_Name='{Selectgroup}',Account_Name='{SelectAccount}',Transaction_Type='{Transaction_Type}',Date='{Date}',Amount='{self.ui.txtAmount.text()}',Note='{self.ui.textNote.toPlainText()}' where Id='{self.id}'"
        self.cursor.execute(sql)
        self.conn.commit()

    def DeleteBtnClick(self):
       self.cursor.execute(f"delete from Transaction_Data where Id={self.id}")
       self.conn.commit()
        #self.loadDataInTable()