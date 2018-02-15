from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
import time

import sys

import UI_view_saraa
import DB_manager

#To incorporate UI_view_SARAA inherit QDialog, and UI_view
class MainDialog(QDialog, UI_view_saraa.Ui_Dialog):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        #self.insertPilotBtn.clicked.connect(self.insertPilot)
#TODO:QMessageBox.information(self,"done")

    # def initializeModel(model):
    #     model.setTable("pilots1")
    #     model.setEd
    #
    #
    # def insertPilot(self):
    #     print("WORKS")
    #
    # def createDB(self):
    #     db = QSqlDatabase.addDatabase('QSQLITE')
    #     db.setDatabaseName('saraa1.db')
    #     model = QSqlTableModel()
    #     delrow = -1
    #
    #
    #
    #     if not db.open():
    #         QMessageBox.critical(p_str="cannot open db")
    #         return False
    #     query = QSqlQuery()
    #     query.exec_("""CREATE TABLE IF NOT EXISTS sarra1(id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
    #           pilot CHAR(20) NOT NULL , aircraft CHAR(20) NOT NULL, date1 DATE NOT NULL, time1 TIME NOT NULL)""")
    #
    #     query.exec_("insert into saraa1 values(1, 'Roger Federer','tagazou', '10-10-2008','11:20')")
    #     return True
    #
    # def addRow(self):
    #     pass





if __name__ == '__main__':
    try:
        app = QApplication(sys.argv)
        #create and display splash screen

        splash_pix = QPixmap('Logo_armee.png')

        splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
        splash.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        splash.setEnabled(False)
        #add progress bar
        progressBar = QProgressBar(splash)
        progressBar.setMaximum(10)
        progressBar.setGeometry(0, splash_pix.height() - 50, splash_pix.width(), 20)

        splash.show()
        splash.showMessage("<h1><font color='black'>Bienvenue dans Moise!</font></h1>", Qt.AlignTop | Qt.AlignCenter, Qt.black)

        for i in range(1, 11):
            progressBar.setValue(i)
            t = time.time()
            while time.time() < t + 0.1:
                app.processEvents()
        #simulating
        time.sleep(2)





        form = MainDialog()
        form.show()
        splash.finish(form)
        app.exec_()
        sys.exit(0)
    except NameError:
        print("Name Error: ", sys.exc_info()[1])
    except SystemExit:
        print("Closing Window....")
    except Exception:
        print(sys.exc_info()[1])
