from PyQt5.QtWidgets import QMainWindow

from MainWindow.MainWindow import Ui_MainWindow
from Add_Username.clsAddUsername import clsAdd_Username
from Change_Password.clsChange_Password import clsChange_Password
from Group.clsGroup import clsGroup
from Account.clsAccount import clsAccount
from Transaction.clsTransaction import clsTransaction

class clsMainWindow(QMainWindow):
    def __init__(self):
        super(clsMainWindow,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionAdd_Username.triggered.connect(self.Add_UsernameClick)
        self.ui.actionChange_Password_2.triggered.connect(self.Change_PasswordClick)
        self.ui.menuGroup.aboutToShow.connect(self.Group_NameClick)
        self.ui.menuAccount.aboutToShow.connect(self.Account_NameClick)
        self.ui.menuTransaction.aboutToShow.connect(self.Transaction_Click)

    def Add_UsernameClick(self):
        self.a1=clsAdd_Username()
        self.ui.mdiArea.addSubWindow(self.a1)
        self.a1.show()

    def Change_PasswordClick(self):
        self.c1=clsChange_Password()
        self.ui.mdiArea.addSubWindow(self.c1)
        self.c1.show()

    def Group_NameClick(self):
        self.g1=clsGroup()
        self.ui.mdiArea.addSubWindow(self.g1)
        self.g1.show()

    def Account_NameClick(self):
        self.n1=clsAccount()
        self.ui.mdiArea.addSubWindow(self.n1)
        self.n1.show()

    def Transaction_Click(self):
        self.t1=clsTransaction()
        self.ui.mdiArea.addSubWindow(self.t1)
        self.t1.show()




