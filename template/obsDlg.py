# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'obsDlg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogObs(object):
    def setupUi(self, DialogObs):
        if not DialogObs.objectName():
            DialogObs.setObjectName(u"DialogObs")
        DialogObs.resize(906, 450)
        self.horizontalLayout = QHBoxLayout(DialogObs)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plainTextEdit = QPlainTextEdit(DialogObs)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout.addWidget(self.plainTextEdit)


        self.retranslateUi(DialogObs)

        QMetaObject.connectSlotsByName(DialogObs)
    # setupUi

    def retranslateUi(self, DialogObs):
        DialogObs.setWindowTitle(QCoreApplication.translate("DialogObs", u"Dialog", None))
        self.plainTextEdit.setPlainText("")
    # retranslateUi

