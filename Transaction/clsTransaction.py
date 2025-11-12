from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox
from Transaction.Transaction import Ui_MainWindow
import sqlite3
class clsTransaction(QMainWindow):
    def __init__(self):
        super(clsTransaction,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedHeight(670)
        self.setFixedWidth(970)
        self.ui.cmbSelectgroup.setFocus()
        self.conn = sqlite3.connect('DataBase.db')
        self.ui.btnnew.clicked.connect(self.NewBtnClick)
        self.ui.btnsave.clicked.connect(self.SaveBtnClick)
        self.ui.btnupdate.clicked.connect(self.UpdateBtnClick)
        self.ui.btndelete.clicked.connect(self.DeleteBtnClick)
        self.ui.radReceived.setChecked(True)

        self.ui.tableWidget.setColumnCount(7)
        self.ui.tableWidget.setHorizontalHeaderLabels(["ID", "Group_Name", "Account_Name", "Transaction_Type", "Date", "Amount", "Note"])
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 150)


        Current_Date = QDate.currentDate()
        self.ui.dateEdit.setDate(Current_Date)

        self.ui.tableWidget.clicked.connect(self.tableClick)
        self.loadDataInTable()

    def loadDataInTable(self):
        self.cursor.execute(f"select * from Transaction_Data")
        result = self.cursor.fetchall()
        self.ui.tableWidget.setRowCount(0)
        rw = 0
        for row in result:
            rw = int(row) + 1
            self.ui.tableWidget.setColumnCount(rw)
            self.ui.tableWidget.setItem(rw - 1, 0, QTableWidgetItem(str(row[0])))
            self.ui.tableWidget.setItem(rw - 1, 1, QTableWidgetItem(str(row[1])))
            self.ui.tableWidget.setItem(rw - 1, 2, QTableWidgetItem(str(row[2])))
            self.ui.tableWidget.setItem(rw - 1, 3, QTableWidgetItem(str(row[3])))
            self.ui.tableWidget.setItem(rw - 1, 4, QTableWidgetItem(str(row[4])))
            self.ui.tableWidget.setItem(rw - 1, 5, QTableWidgetItem(str(row[5])))
            self.ui.tableWidget.setItem(rw - 1, 6, QTableWidgetItem(str(row[6])))

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
        self.ui.txtNote.setText(self.ui.tableWidget.item(cr, 6).text())

    def NewBtnClick(self):
        self.ui.cmbSelectgroup.currentText("")
        self.ui.cmbSelectAccount.setText("")
        self.ui.txtAmount.setText("")
        self.ui.txtNote.setText("")

    def SaveBtnClick(self):
        Selectgroup = self.ui.cmbSelectgroup.currentText()
        SelectAccount = self.ui.cmbSelectAccount.currentText()
        Date = self.ui.dateEdit.date().toString("yyyy/MM/dd")
        sql = f"insert into Transaction_Data values(null,'{Selectgroup}','{SelectAccount}','{Date}','{self.ui.txtAmount.text()}','{self.ui.txtNote.text()}')"
        self.cursor.execute(sql)
        self.conn.commit()
        self.loadDataInTable()
    def UpdateBtnClick(self):
        Selectgroup = self.ui.cmbSelectgroup.currentText()
        SelectAccount = self.ui.cmbSelectAccount.currentText()
        Date = (self.ui.dateEdit.date().toString("yyyy/MM/dd"))
        sql = f"Update Transaction_Data set Group_Name='{Selectgroup}',Account_Name='{SelectAccount}',Date='{Date}',Amount='{self.ui.txtAmount.text()}',Note='{self.ui.txtNote.text()}'"
        self.cursor.execute(sql)
        self.conn.commit()
        self.loadDataInTable()
    def DeleteBtnClick(self):
        self.cursor.execute(f"delete from Transaction_Data where Id={self.id}")
        self.conn.commit()
        self.loadDataInTable()





