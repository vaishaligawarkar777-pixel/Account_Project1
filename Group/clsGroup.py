from PyQt5.QtWidgets import QMainWindow,QTableWidget,QTableWidgetItem,QMessageBox
from Group.Group import Ui_MainWindow
import sqlite3
class clsGroup(QMainWindow):
    def __init__(self):
        super(clsGroup,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedHeight(600)
        self.setFixedWidth(600)
        self.ui.txtGroupname.setFocus()
        self.conn = sqlite3.connect('DataBase.db')
        self.cursor = self.conn.cursor()
        self.ui.btnnew.clicked.connect(self.NewBtnClick)
        self.ui.btnsave.clicked.connect(self.SaveBtnClick)
        self.ui.btnupdate.clicked.connect(self.UpdateBtnClick)
        self.ui.btndelete.clicked.connect(self.DeleteBtnClick)

        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setHorizontalHeaderLabels(["Sr.No","Group Name"])
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


    def tableClick(self):
        cr=self.ui.tableWidget.currentRow().__index__()
        print(cr)
        self.Sr_No = self.ui.tableWidget.item(cr,0).text()
        self.ui.txtGroupname.setText(self.ui.tableWidget.item(cr,1).text())

    def NewBtnClick(self):
        self.ui.txtGroupname.setText("")

    def SaveBtnClick(self):
        sql = f"insert into Group_Data values(null,'{self.ui.txtGroupname.text()}')"
        self.cursor.execute(sql)
        self.conn.commit()
        self.loadDataInTable()

    def UpdateBtnClick(self):
        sql = f"Update Group_Data set Groupname='{self.ui.txtGroupname.text()}' where Sr_No='{self.Sr_No}'"
        self.cursor.execute(sql)
        self.conn.commit()
        self.loadDataInTable()

    def DeleteBtnClick(self):
        self.cursor.execute(f"delete from Group_Data where Sr_No={self.Sr_No}")
        self.conn.commit()
        self.loadDataInTable()
