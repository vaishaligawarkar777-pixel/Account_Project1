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
