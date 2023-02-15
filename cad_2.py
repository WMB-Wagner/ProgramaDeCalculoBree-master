# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sun Dec 27 11:18:56 2009
#      by: PySide UI code generator 4.6
#
# Modify for PySide 11/02/2015
#      Python version: 2.7.8
#      Qt version: 4.8.6
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2.QtGui import QWo
from PySide2.QtWidgets import QApplication, QDialog, QMainWindow, QFileDialog, QTableView, QMessageBox, QWidget, QGridLayout, QMdiArea, QTabWidget, QMenuBar, QStatusBar
from PySide2.QtCore import Qt, Signal, QObject, QModelIndex, QAbstractTableModel, QWo
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(508, 436)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setViewMode(QMdiArea.TabbedView)
        self.mdiArea.setTabPosition(QTabWidget.South)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate(
            "MainWindow", "MainWindow", None))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui_MainWindow()
    my_mw = QMainWindow()
    ui.setupUi(my_mw)
    # ui.mdiArea.addSubWindow(v)
    my_mw.show()

    sys.exit(app.exec_())
