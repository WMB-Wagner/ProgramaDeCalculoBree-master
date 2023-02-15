# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DiagHarm.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from template import bree_rc

class Ui_DialogHarm(object):
    def setupUi(self, DialogHarm):
        if not DialogHarm.objectName():
            DialogHarm.setObjectName(u"DialogHarm")
        DialogHarm.resize(400, 358)
        icon = QIcon()
        icon.addFile(u":/bree/table.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogHarm.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(DialogHarm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setContentsMargins(4, 4, 4, 4)
        self.label = QLabel(DialogHarm)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.inputF1 = QLineEdit(DialogHarm)
        self.inputF1.setObjectName(u"inputF1")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inputF1)

        self.label_2 = QLabel(DialogHarm)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.inputPasso = QLineEdit(DialogHarm)
        self.inputPasso.setObjectName(u"inputPasso")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputPasso)

        self.label_3 = QLabel(DialogHarm)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.inputNharm = QLineEdit(DialogHarm)
        self.inputNharm.setObjectName(u"inputNharm")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.inputNharm)


        self.verticalLayout.addLayout(self.formLayout)

        self.tableViewHarm = QTableView(DialogHarm)
        self.tableViewHarm.setObjectName(u"tableViewHarm")

        self.verticalLayout.addWidget(self.tableViewHarm)

        self.frame = QFrame(DialogHarm)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.bt_refresh = QPushButton(self.frame)
        self.bt_refresh.setObjectName(u"bt_refresh")

        self.horizontalLayout.addWidget(self.bt_refresh)

        self.bt_Fill = QPushButton(self.frame)
        self.bt_Fill.setObjectName(u"bt_Fill")
        self.bt_Fill.setIcon(icon)

        self.horizontalLayout.addWidget(self.bt_Fill)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DialogHarm)

        QMetaObject.connectSlotsByName(DialogHarm)
    # setupUi

    def retranslateUi(self, DialogHarm):
        DialogHarm.setWindowTitle(QCoreApplication.translate("DialogHarm", u"Harm\u00f4nicas", None))
        self.label.setText(QCoreApplication.translate("DialogHarm", u"F1 (Hz)", None))
        self.inputF1.setText(QCoreApplication.translate("DialogHarm", u"60", None))
        self.label_2.setText(QCoreApplication.translate("DialogHarm", u"Passo (Hz)", None))
        self.inputPasso.setText(QCoreApplication.translate("DialogHarm", u"60", None))
        self.label_3.setText(QCoreApplication.translate("DialogHarm", u"# Harmonicas", None))
        self.inputNharm.setText(QCoreApplication.translate("DialogHarm", u"1", None))
        self.bt_refresh.setText(QCoreApplication.translate("DialogHarm", u"Atualizar", None))
        self.bt_Fill.setText(QCoreApplication.translate("DialogHarm", u"Preencher", None))
    # retranslateUi

