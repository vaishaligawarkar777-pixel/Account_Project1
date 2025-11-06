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
        self.cursor = self.conn.cursor()
        #self.ui.btnnew.clicked.connect(self.NewBtnClick)
        #self.ui.btnsave.clicked.connect(self.SaveBtnClick)
        #self.ui.btnupdate.clicked.connect(self.UpdateBtnClick)
        #self.ui.btndelete.clicked.connect(self.DeleteBtnClick)

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Sr.No","Group","Account Name"])
        self.ui.tableWidget.setColumnWidth(0, 50)
        self.ui.tableWidget.setColumnWidth(1, 150)
        self.ui.tableWidget.setColumnWidth(2, 150)
        self.ui.tableWidget.clicked.connect(self.tableClick)
        self.loadDataInTable()

    def loadDataInTable(self):
        self.cursor.execute(f"select * from Group_Data")
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
      pass