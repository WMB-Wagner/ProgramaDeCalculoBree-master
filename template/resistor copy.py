# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'resistor.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Win_Resistor(object):
    def setupUi(self, Win_Resistor):
        if not Win_Resistor.objectName():
            Win_Resistor.setObjectName(u"Win_Resistor")
        Win_Resistor.resize(530, 440)
        font = QFont()
        font.setPointSize(9)
        Win_Resistor.setFont(font)
        self.verticalLayout_3 = QVBoxLayout(Win_Resistor)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_19 = QLabel(Win_Resistor)
        self.label_19.setObjectName(u"label_19")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"background-color: rgb(255, 255, 0);")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)

        self.tabWidget = QTabWidget(Win_Resistor)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabShape(QTabWidget.Triangular)
        self.tabInput = QWidget()
        self.tabInput.setObjectName(u"tabInput")
        self.verticalLayout_5 = QVBoxLayout(self.tabInput)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.tabInput)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fr_labels = QFrame(self.frame_2)
        self.fr_labels.setObjectName(u"fr_labels")
        self.fr_labels.setFrameShape(QFrame.NoFrame)
        self.fr_labels.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_labels)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_20 = QLabel(self.fr_labels)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_20)

        self.label_4 = QLabel(self.fr_labels)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.fr_labels)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.fr_labels)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.label_11 = QLabel(self.fr_labels)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.label_7 = QLabel(self.fr_labels)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label = QLabel(self.fr_labels)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.fr_labels)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.fr_labels)

        self.fr_edit = QFrame(self.frame_2)
        self.fr_edit.setObjectName(u"fr_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fr_edit.sizePolicy().hasHeightForWidth())
        self.fr_edit.setSizePolicy(sizePolicy)
        self.fr_edit.setFrameShape(QFrame.NoFrame)
        self.fr_edit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_edit)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cb_Conex = QComboBox(self.fr_edit)
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.setObjectName(u"cb_Conex")
        self.cb_Conex.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.cb_Conex.sizePolicy().hasHeightForWidth())
        self.cb_Conex.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.cb_Conex)

        self.ed_Vn = QLineEdit(self.fr_edit)
        self.ed_Vn.setObjectName(u"ed_Vn")
        sizePolicy1.setHeightForWidth(self.ed_Vn.sizePolicy().hasHeightForWidth())
        self.ed_Vn.setSizePolicy(sizePolicy1)
        self.ed_Vn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_Vn)

        self.ed_Fr = QLineEdit(self.fr_edit)
        self.ed_Fr.setObjectName(u"ed_Fr")
        sizePolicy1.setHeightForWidth(self.ed_Fr.sizePolicy().hasHeightForWidth())
        self.ed_Fr.setSizePolicy(sizePolicy1)
        self.ed_Fr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_Fr)

        self.ed_KVAR = QLineEdit(self.fr_edit)
        self.ed_KVAR.setObjectName(u"ed_KVAR")
        sizePolicy1.setHeightForWidth(self.ed_KVAR.sizePolicy().hasHeightForWidth())
        self.ed_KVAR.setSizePolicy(sizePolicy1)
        self.ed_KVAR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_KVAR)

        self.ed_max_W_R = QLineEdit(self.fr_edit)
        self.ed_max_W_R.setObjectName(u"ed_max_W_R")
        sizePolicy1.setHeightForWidth(self.ed_max_W_R.sizePolicy().hasHeightForWidth())
        self.ed_max_W_R.setSizePolicy(sizePolicy1)
        self.ed_max_W_R.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_max_W_R)

        self.ed_tempo = QLineEdit(self.fr_edit)
        self.ed_tempo.setObjectName(u"ed_tempo")
        sizePolicy1.setHeightForWidth(self.ed_tempo.sizePolicy().hasHeightForWidth())
        self.ed_tempo.setSizePolicy(sizePolicy1)
        self.ed_tempo.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_tempo)

        self.ed_Vend = QLineEdit(self.fr_edit)
        self.ed_Vend.setObjectName(u"ed_Vend")
        sizePolicy1.setHeightForWidth(self.ed_Vend.sizePolicy().hasHeightForWidth())
        self.ed_Vend.setSizePolicy(sizePolicy1)
        self.ed_Vend.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_Vend)

        self.ed_file_name = QLineEdit(self.fr_edit)
        self.ed_file_name.setObjectName(u"ed_file_name")
        sizePolicy1.setHeightForWidth(self.ed_file_name.sizePolicy().hasHeightForWidth())
        self.ed_file_name.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.ed_file_name)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.fr_edit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.tabWidget.addTab(self.tabInput, "")
        self.tabDF = QWidget()
        self.tabDF.setObjectName(u"tabDF")
        self.verticalLayout_4 = QVBoxLayout(self.tabDF)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_DF = QFrame(self.tabDF)
        self.frame_DF.setObjectName(u"frame_DF")
        self.frame_DF.setFrameShape(QFrame.StyledPanel)
        self.frame_DF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_DF)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tableView_1 = QTableView(self.frame_DF)
        self.tableView_1.setObjectName(u"tableView_1")

        self.verticalLayout_6.addWidget(self.tableView_1)


        self.verticalLayout_4.addWidget(self.frame_DF)

        self.tabWidget.addTab(self.tabDF, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.frame_14 = QFrame(Win_Resistor)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_calc = QPushButton(self.frame_14)
        self.bt_calc.setObjectName(u"bt_calc")
        font2 = QFont()
        font2.setPointSize(12)
        self.bt_calc.setFont(font2)
        self.bt_calc.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.horizontalLayout_3.addWidget(self.bt_calc)

        self.bt_close = QPushButton(self.frame_14)
        self.bt_close.setObjectName(u"bt_close")
        self.bt_close.setFont(font2)
        self.bt_close.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout_3.addWidget(self.bt_close)


        self.verticalLayout_3.addWidget(self.frame_14)

        QWidget.setTabOrder(self.tabWidget, self.cb_Conex)
        QWidget.setTabOrder(self.cb_Conex, self.ed_Vn)
        QWidget.setTabOrder(self.ed_Vn, self.ed_Fr)
        QWidget.setTabOrder(self.ed_Fr, self.ed_KVAR)
        QWidget.setTabOrder(self.ed_KVAR, self.ed_max_W_R)
        QWidget.setTabOrder(self.ed_max_W_R, self.ed_tempo)
        QWidget.setTabOrder(self.ed_tempo, self.bt_calc)
        QWidget.setTabOrder(self.bt_calc, self.bt_close)
        QWidget.setTabOrder(self.bt_close, self.tableView_1)

        self.retranslateUi(Win_Resistor)
        self.bt_close.clicked.connect(Win_Resistor.close)

        self.tabWidget.setCurrentIndex(0)
        self.cb_Conex.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Win_Resistor)
    # setupUi

    def retranslateUi(self, Win_Resistor):
        Win_Resistor.setWindowTitle(QCoreApplication.translate("Win_Resistor", u"Resistor de descarga", None))
        self.label_19.setText(QCoreApplication.translate("Win_Resistor", u"Resistor de Descarga", None))
        self.label_20.setText(QCoreApplication.translate("Win_Resistor", u"Conex\u00e3o dos Resistores", None))
        self.label_4.setText(QCoreApplication.translate("Win_Resistor", u"Tens\u00e3o (V)", None))
        self.label_5.setText(QCoreApplication.translate("Win_Resistor", u"Frequ\u00eancia (Hz)", None))
        self.label_6.setText(QCoreApplication.translate("Win_Resistor", u"Pot\u00eancia Reativa (KVAr)/Se\u00e7\u00e3o", None))
        self.label_11.setText(QCoreApplication.translate("Win_Resistor", u"Maximo Watss por Resistor", None))
        self.label_7.setText(QCoreApplication.translate("Win_Resistor", u"Tempo de descarga", None))
        self.label.setText(QCoreApplication.translate("Win_Resistor", u"Tens\u00e3o Final", None))
        self.label_2.setText(QCoreApplication.translate("Win_Resistor", u"Nome do arquivo de resultado", None))
        self.cb_Conex.setItemText(0, QCoreApplication.translate("Win_Resistor", u"S\u00e9rie", None))
        self.cb_Conex.setItemText(1, QCoreApplication.translate("Win_Resistor", u"S\u00e9rie/Paralelo", None))

        self.cb_Conex.setPlaceholderText("")
        self.ed_Vn.setText(QCoreApplication.translate("Win_Resistor", u"7200", None))
        self.ed_Vn.setPlaceholderText(QCoreApplication.translate("Win_Resistor", u"Tens\u00e3o (V)", None))
        self.ed_Fr.setText(QCoreApplication.translate("Win_Resistor", u"60", None))
        self.ed_Fr.setPlaceholderText(QCoreApplication.translate("Win_Resistor", u"Frequ\u00eancia (HZ)", None))
        self.ed_KVAR.setText(QCoreApplication.translate("Win_Resistor", u"200", None))
        self.ed_KVAR.setPlaceholderText(QCoreApplication.translate("Win_Resistor", u"Pot\u00eancia Reativa (kVAr)", None))
        self.ed_max_W_R.setText(QCoreApplication.translate("Win_Resistor", u"3", None))
        self.ed_tempo.setText(QCoreApplication.translate("Win_Resistor", u"300", None))
        self.ed_Vend.setText(QCoreApplication.translate("Win_Resistor", u"50", None))
        self.ed_file_name.setText(QCoreApplication.translate("Win_Resistor", u"Resustudas Resistor de descarga", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabInput), QCoreApplication.translate("Win_Resistor", u"Entrada geral", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabDF), QCoreApplication.translate("Win_Resistor", u"Data Frame", None))
        self.bt_calc.setText(QCoreApplication.translate("Win_Resistor", u"Calcular...", None))
        self.bt_close.setText(QCoreApplication.translate("Win_Resistor", u"Voltar...", None))
    # retranslateUi

