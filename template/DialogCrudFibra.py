# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DialogCrudFibra.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from template import bree_rc

class Ui_DialogCrudFibra(object):
    def setupUi(self, DialogCrudFibra):
        if not DialogCrudFibra.objectName():
            DialogCrudFibra.setObjectName(u"DialogCrudFibra")
        DialogCrudFibra.setWindowModality(Qt.WindowModal)
        DialogCrudFibra.resize(400, 383)
        icon = QIcon()
        icon.addFile(u":/bree/glass_characteristics_higher_resistance_than_steel_yarns.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogCrudFibra.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(DialogCrudFibra)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DialogCrudFibra)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.inputPadrao = QLineEdit(DialogCrudFibra)
        self.inputPadrao.setObjectName(u"inputPadrao")
        self.inputPadrao.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.inputPadrao)

        self.label_2 = QLabel(DialogCrudFibra)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.inputFi1 = QLineEdit(DialogCrudFibra)
        self.inputFi1.setObjectName(u"inputFi1")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputFi1)

        self.label_3 = QLabel(DialogCrudFibra)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.inputFiN = QLineEdit(DialogCrudFibra)
        self.inputFiN.setObjectName(u"inputFiN")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.inputFiN)

        self.label_4 = QLabel(DialogCrudFibra)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.inputFeN = QLineEdit(DialogCrudFibra)
        self.inputFeN.setObjectName(u"inputFeN")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.inputFeN)

        self.label_5 = QLabel(DialogCrudFibra)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.inputFeU = QLineEdit(DialogCrudFibra)
        self.inputFeU.setObjectName(u"inputFeU")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.inputFeU)


        self.verticalLayout.addLayout(self.formLayout)

        self.tableView = QTableView(DialogCrudFibra)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout.addWidget(self.tableView)

        self.frame = QFrame(DialogCrudFibra)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btCreate = QPushButton(self.frame)
        self.btCreate.setObjectName(u"btCreate")
        icon1 = QIcon()
        icon1.addFile(u":/bree/blue-document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btCreate.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btCreate)

        self.btRead = QPushButton(self.frame)
        self.btRead.setObjectName(u"btRead")

        self.horizontalLayout.addWidget(self.btRead)

        self.btUpdate = QPushButton(self.frame)
        self.btUpdate.setObjectName(u"btUpdate")
        icon2 = QIcon()
        icon2.addFile(u":/bree/verificar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btUpdate.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btUpdate)

        self.btDelete = QPushButton(self.frame)
        self.btDelete.setObjectName(u"btDelete")
        icon3 = QIcon()
        icon3.addFile(u":/bree/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btDelete.setIcon(icon3)

        self.horizontalLayout.addWidget(self.btDelete)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DialogCrudFibra)

        QMetaObject.connectSlotsByName(DialogCrudFibra)
    # setupUi

    def retranslateUi(self, DialogCrudFibra):
        DialogCrudFibra.setWindowTitle(QCoreApplication.translate("DialogCrudFibra", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogCrudFibra", u"Padr\u00e3o", None))
        self.label_2.setText(QCoreApplication.translate("DialogCrudFibra", u"Fibra interna Cilindro 1 (mm)", None))
        self.inputFi1.setText(QCoreApplication.translate("DialogCrudFibra", u"3.0", None))
        self.label_3.setText(QCoreApplication.translate("DialogCrudFibra", u"Fibra interna demais cilindros (mm)", None))
        self.inputFiN.setText(QCoreApplication.translate("DialogCrudFibra", u"1", None))
        self.label_4.setText(QCoreApplication.translate("DialogCrudFibra", u"Fibra externa demais cilindros (mm)", None))
        self.label_5.setText(QCoreApplication.translate("DialogCrudFibra", u"Fibra externa \u00faltimo cilindro (mm)", None))
        self.btCreate.setText(QCoreApplication.translate("DialogCrudFibra", u"Novo", None))
        self.btRead.setText(QCoreApplication.translate("DialogCrudFibra", u"Ler", None))
        self.btUpdate.setText(QCoreApplication.translate("DialogCrudFibra", u"Update", None))
        self.btDelete.setText(QCoreApplication.translate("DialogCrudFibra", u"Delete", None))
    # retranslateUi

