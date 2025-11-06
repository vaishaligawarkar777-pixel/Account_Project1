from PyQt5.QtWidgets import QMainWindow

from MainWindow.MainWindow import Ui_MainWindow
from Add_Username.clsAddUsername import clsAdd_Username
from Change_Password.clsChange_Password import clsChange_Password

class clsMainWindow(QMainWindow):
    def __init__(self):
        super(clsMainWindow,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionAdd_Username.triggered.connect(self.Add_UsernameClick)
        self.ui.actionChange_Password_2.triggered.connect(self.Change_PasswordClick)

    def Add_UsernameClick(self):
        self.a1=clsAdd_Username()
        self.ui.mdiArea.addSubWindow(self.a1)
        self.a1.show()

    def Change_PasswordClick(self):
        self.c1=clsChange_Password()
        self.ui.mdiArea.addSubWindow(self.c1)
        self.c1.show()



