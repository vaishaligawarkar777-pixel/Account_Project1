from PyQt5.QtWidgets import QMainWindow
from MainWindow.MainWindow import Ui_MainWindow
class clsMainWindow(QMainWindow):
    def __init__(self):
        super(clsMainWindow,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionChange_Password.triggered.connect(self.Change_PasswordClick)

        self.ui.menuStudent.aboutToShow.connect(self.Open_Form1)
        self.ui.menuFees.aboutToShow.connect(self.Open_Form2)
        self.ui.menuReport.aboutToShow.connect(self.Open_Form3)
        self.ui.menuMonthlyReport.aboutToShow.connect(self.Open_Form4)
        self.ui.menuYearly_Report.aboutToShow.connect(self.Open_Form5)



    def Change_PasswordClick(self):
        self.c1 = clsChange_Password()
        self.ui.mdiArea.addSubWindow(self.c1)
        self.c1.show()



      