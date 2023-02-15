# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_system_bree.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(428, 299)
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.bt_CpEn = QPushButton(self.centralwidget)
        self.bt_CpEn.setObjectName(u"bt_CpEn")
        self.bt_CpEn.setFont(font)
        self.bt_CpEn.setStyleSheet(u"background-color: rgb(0, 170, 255);\n"
"alternate-background-color: rgb(170, 170, 255);")
        self.bt_CpEn.setFlat(False)

        self.verticalLayout.addWidget(self.bt_CpEn)

        self.bt_CpBr = QPushButton(self.centralwidget)
        self.bt_CpBr.setObjectName(u"bt_CpBr")
        self.bt_CpBr.setFont(font)
        self.bt_CpBr.setStyleSheet(u"background-color: rgb(170, 170, 0);")

        self.verticalLayout.addWidget(self.bt_CpBr)

        self.bt_CHF = QPushButton(self.centralwidget)
        self.bt_CHF.setObjectName(u"bt_CHF")
        self.bt_CHF.setFont(font)
        self.bt_CHF.setStyleSheet(u"background-color: rgb(170, 85, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.bt_CHF)

        self.bt_FI = QPushButton(self.centralwidget)
        self.bt_FI.setObjectName(u"bt_FI")
        self.bt_FI.setFont(font)
        self.bt_FI.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.verticalLayout.addWidget(self.bt_FI)

        self.bt_RS = QPushButton(self.centralwidget)
        self.bt_RS.setObjectName(u"bt_RS")
        self.bt_RS.setFont(font)
        self.bt_RS.setStyleSheet(u"background-color: rgb(255, 255, 0);")

        self.verticalLayout.addWidget(self.bt_RS)

        self.bt_RSP = QPushButton(self.centralwidget)
        self.bt_RSP.setObjectName(u"bt_RSP")
        self.bt_RSP.setFont(font)
        self.bt_RSP.setStyleSheet(u"background-color: rgb(170, 170, 255);")

        self.verticalLayout.addWidget(self.bt_RSP)

        self.bt_reactor = QPushButton(self.centralwidget)
        self.bt_reactor.setObjectName(u"bt_reactor")
        self.bt_reactor.setFont(font)
        self.bt_reactor.setStyleSheet(u"background-color: rgb(85, 85, 255);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.bt_reactor)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistemas de c\u00e1culos bree", None))
        self.bt_CpEn.setText(QCoreApplication.translate("MainWindow", u"Capacitor de Pot\u00eancia Eixos Americanos", None))
        self.bt_CpBr.setText(QCoreApplication.translate("MainWindow", u"Capacitor de Pot\u00eancia Eixos Brasileiros", None))
        self.bt_CHF.setText(QCoreApplication.translate("MainWindow", u"Capacitor de Alta Frequ\u00eancia", None))
        self.bt_FI.setText(QCoreApplication.translate("MainWindow", u"Fus\u00edvel Interno", None))
        self.bt_RS.setText(QCoreApplication.translate("MainWindow", u"Resistor de descarga S\u00e9rie", None))
        self.bt_RSP.setText(QCoreApplication.translate("MainWindow", u"Resistor S\u00e9rie/Paralelo", None))
        self.bt_reactor.setText(QCoreApplication.translate("MainWindow", u"Reator de N\u00facleo de Ar", None))
    # retranslateUi

