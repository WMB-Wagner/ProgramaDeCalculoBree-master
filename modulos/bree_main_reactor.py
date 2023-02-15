from pandasql import sqldf
import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog
import sqlite3

#sys.path.append('OneDrive/Documentos/Bree')
sys.path.append('OneDrive/Documentos/GitHub/bree_reactor')
sys.path.append('Documents/GitHub')

#from pathlib import Path
path_name = os.getcwd()
path_name = path_name = path_name.replace("\\","/")
path_name = path_name = path_name.replace("C:","")
path_name

pysqldf = lambda q: sqldf(q, globals())

import bree_reactor_core_1 as bree
# class MainWindow(QDialog):
class MainWindow(QMainWindow):    
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main_reactor_window.ui",self)
        self.show()
        '''self.tableWidget.setColumnWidth(0, 250)
        self.tableWidget.setColumnWidth(1, 100)
        self.tableWidget.setColumnWidth(2, 350)
        self.tableWidget.setHorizontalHeaderLabels(["City","Country","Subcountry"])
        self.loaddata()'''

    '''def loaddata(self):
        connection = sqlite3.connect('data.sqlite')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM worldcities LIMIT 40'

        tablerow=0
        results = cur.execute(sqlstr)
        self.tableWidget.setRowCount(40)
        for row in results:
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1'''
# main
app = QApplication(sys.argv)
UI = MainWindow()
app.exec_()
'''app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(850)
widget.setFixedWidth(1120)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")'''