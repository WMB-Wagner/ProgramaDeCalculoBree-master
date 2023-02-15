# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'fuseIn.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from template import bree_rc


class Ui_Win_FuseIn(object):
    def setupUi(self, Win_FuseIn):
        if not Win_FuseIn.objectName():
            Win_FuseIn.setObjectName(u"Win_FuseIn")
        Win_FuseIn.resize(530, 713)
        self.verticalLayout_3 = QVBoxLayout(Win_FuseIn)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_19 = QLabel(Win_FuseIn)
        self.label_19.setObjectName(u"label_19")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)

        self.tabWidget = QTabWidget(Win_FuseIn)
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
        self.label_20.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_20)

        self.label_2 = QLabel(self.fr_labels)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_4 = QLabel(self.fr_labels)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.fr_labels)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.fr_labels)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.label_11 = QLabel(self.fr_labels)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.label_7 = QLabel(self.fr_labels)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label_9 = QLabel(self.fr_labels)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.label_10 = QLabel(self.fr_labels)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label_S = QLabel(self.fr_labels)
        self.label_S.setObjectName(u"label_S")
        self.label_S.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_S)

        self.label_P0 = QLabel(self.fr_labels)
        self.label_P0.setObjectName(u"label_P0")
        self.label_P0.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_P0)

        self.label_S1 = QLabel(self.fr_labels)
        self.label_S1.setObjectName(u"label_S1")
        self.label_S1.setEnabled(True)
        self.label_S1.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_S1)

        self.label_S2 = QLabel(self.fr_labels)
        self.label_S2.setObjectName(u"label_S2")
        self.label_S2.setEnabled(True)
        self.label_S2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_S2)

        self.label_P1 = QLabel(self.fr_labels)
        self.label_P1.setObjectName(u"label_P1")
        self.label_P1.setEnabled(True)
        self.label_P1.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_P1)

        self.label_P2 = QLabel(self.fr_labels)
        self.label_P2.setObjectName(u"label_P2")
        self.label_P2.setEnabled(True)
        self.label_P2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_P2)

        self.label_23 = QLabel(self.fr_labels)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_23)

        self.label_27 = QLabel(self.fr_labels)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_27)

        self.label = QLabel(self.fr_labels)
        self.label.setObjectName(u"label")
        self.label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_12 = QLabel(self.fr_labels)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout.addWidget(self.label_12)

        self.verticalSpacer_3 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout.addWidget(self.fr_labels)

        self.fr_edit = QFrame(self.frame_2)
        self.fr_edit.setObjectName(u"fr_edit")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.fr_edit.sizePolicy().hasHeightForWidth())
        self.fr_edit.setSizePolicy(sizePolicy)
        self.fr_edit.setFrameShape(QFrame.NoFrame)
        self.fr_edit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_edit)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cb_Conex = QComboBox(self.fr_edit)
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.addItem("")
        self.cb_Conex.setObjectName(u"cb_Conex")
        self.cb_Conex.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.cb_Conex.sizePolicy().hasHeightForWidth())
        self.cb_Conex.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.cb_Conex)

        self.spinBoxNumElos = QSpinBox(self.fr_edit)
        self.spinBoxNumElos.setObjectName(u"spinBoxNumElos")
        self.spinBoxNumElos.setMinimum(1)
        self.spinBoxNumElos.setMaximum(2)

        self.verticalLayout_2.addWidget(self.spinBoxNumElos)

        self.ed_Vn = QLineEdit(self.fr_edit)
        self.ed_Vn.setObjectName(u"ed_Vn")
        sizePolicy1.setHeightForWidth(
            self.ed_Vn.sizePolicy().hasHeightForWidth())
        self.ed_Vn.setSizePolicy(sizePolicy1)
        self.ed_Vn.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_Vn)

        self.ed_Fr = QLineEdit(self.fr_edit)
        self.ed_Fr.setObjectName(u"ed_Fr")
        sizePolicy1.setHeightForWidth(
            self.ed_Fr.sizePolicy().hasHeightForWidth())
        self.ed_Fr.setSizePolicy(sizePolicy1)
        self.ed_Fr.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_Fr)

        self.ed_KVAR = QLineEdit(self.fr_edit)
        self.ed_KVAR.setObjectName(u"ed_KVAR")
        sizePolicy1.setHeightForWidth(
            self.ed_KVAR.sizePolicy().hasHeightForWidth())
        self.ed_KVAR.setSizePolicy(sizePolicy1)
        self.ed_KVAR.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_KVAR)

        self.ed_Cap = QLineEdit(self.fr_edit)
        self.ed_Cap.setObjectName(u"ed_Cap")
        sizePolicy1.setHeightForWidth(
            self.ed_Cap.sizePolicy().hasHeightForWidth())
        self.ed_Cap.setSizePolicy(sizePolicy1)
        self.ed_Cap.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_Cap)

        self.ed_size_un = QLineEdit(self.fr_edit)
        self.ed_size_un.setObjectName(u"ed_size_un")
        self.ed_size_un.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_size_un)

        self.ed_G_SI = QLineEdit(self.fr_edit)
        self.ed_G_SI.setObjectName(u"ed_G_SI")
        sizePolicy1.setHeightForWidth(
            self.ed_G_SI.sizePolicy().hasHeightForWidth())
        self.ed_G_SI.setSizePolicy(sizePolicy1)
        self.ed_G_SI.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_G_SI)

        self.ed_GPI = QLineEdit(self.fr_edit)
        self.ed_GPI.setObjectName(u"ed_GPI")
        sizePolicy1.setHeightForWidth(
            self.ed_GPI.sizePolicy().hasHeightForWidth())
        self.ed_GPI.setSizePolicy(sizePolicy1)
        self.ed_GPI.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_GPI)

        self.ed_serie = QLineEdit(self.fr_edit)
        self.ed_serie.setObjectName(u"ed_serie")
        sizePolicy1.setHeightForWidth(
            self.ed_serie.sizePolicy().hasHeightForWidth())
        self.ed_serie.setSizePolicy(sizePolicy1)
        self.ed_serie.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_serie)

        self.ed_P0 = QLineEdit(self.fr_edit)
        self.ed_P0.setObjectName(u"ed_P0")
        sizePolicy1.setHeightForWidth(
            self.ed_P0.sizePolicy().hasHeightForWidth())
        self.ed_P0.setSizePolicy(sizePolicy1)
        self.ed_P0.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_P0)

        self.ed_S1 = QLineEdit(self.fr_edit)
        self.ed_S1.setObjectName(u"ed_S1")
        self.ed_S1.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.ed_S1.sizePolicy().hasHeightForWidth())
        self.ed_S1.setSizePolicy(sizePolicy1)
        self.ed_S1.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_S1)

        self.ed_S2 = QLineEdit(self.fr_edit)
        self.ed_S2.setObjectName(u"ed_S2")
        self.ed_S2.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.ed_S2.sizePolicy().hasHeightForWidth())
        self.ed_S2.setSizePolicy(sizePolicy1)
        self.ed_S2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_S2)

        self.ed_P1 = QLineEdit(self.fr_edit)
        self.ed_P1.setObjectName(u"ed_P1")
        self.ed_P1.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.ed_P1.sizePolicy().hasHeightForWidth())
        self.ed_P1.setSizePolicy(sizePolicy1)
        self.ed_P1.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_P1)

        self.ed_P2 = QLineEdit(self.fr_edit)
        self.ed_P2.setObjectName(u"ed_P2")
        self.ed_P2.setEnabled(True)
        sizePolicy1.setHeightForWidth(
            self.ed_P2.sizePolicy().hasHeightForWidth())
        self.ed_P2.setSizePolicy(sizePolicy1)
        self.ed_P2.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_P2)

        self.ed_PST = QLineEdit(self.fr_edit)
        self.ed_PST.setObjectName(u"ed_PST")
        sizePolicy1.setHeightForWidth(
            self.ed_PST.sizePolicy().hasHeightForWidth())
        self.ed_PST.setSizePolicy(sizePolicy1)
        self.ed_PST.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_PST)

        self.ed_KURL = QLineEdit(self.fr_edit)
        self.ed_KURL.setObjectName(u"ed_KURL")
        sizePolicy1.setHeightForWidth(
            self.ed_KURL.sizePolicy().hasHeightForWidth())
        self.ed_KURL.setSizePolicy(sizePolicy1)
        self.ed_KURL.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_KURL)

        self.ed_KMIN = QLineEdit(self.fr_edit)
        self.ed_KMIN.setObjectName(u"ed_KMIN")
        sizePolicy1.setHeightForWidth(
            self.ed_KMIN.sizePolicy().hasHeightForWidth())
        self.ed_KMIN.setSizePolicy(sizePolicy1)
        self.ed_KMIN.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_KMIN)

        self.ed_file_name = QLineEdit(self.fr_edit)
        self.ed_file_name.setObjectName(u"ed_file_name")
        sizePolicy1.setHeightForWidth(
            self.ed_file_name.sizePolicy().hasHeightForWidth())
        self.ed_file_name.setSizePolicy(sizePolicy1)

        self.verticalLayout_2.addWidget(self.ed_file_name)

        self.verticalSpacer_4 = QSpacerItem(
            20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.horizontalLayout.addWidget(self.fr_edit)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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

        self.tableView_2 = QTableView(self.frame_DF)
        self.tableView_2.setObjectName(u"tableView_2")

        self.verticalLayout_6.addWidget(self.tableView_2)

        self.tableView_3 = QTableView(self.frame_DF)
        self.tableView_3.setObjectName(u"tableView_3")

        self.verticalLayout_6.addWidget(self.tableView_3)

        self.verticalLayout_4.addWidget(self.frame_DF)

        self.tabWidget.addTab(self.tabDF, "")

        self.verticalLayout_3.addWidget(self.tabWidget)

        self.frame_14 = QFrame(Win_FuseIn)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_calc = QPushButton(self.frame_14)
        self.bt_calc.setObjectName(u"bt_calc")
        font1 = QFont()
        font1.setPointSize(12)
        self.bt_calc.setFont(font1)
        self.bt_calc.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        icon = QIcon()
        icon.addFile(u":/bree/calculadora.png",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.bt_calc.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.bt_calc)

        self.bt_read_file = QPushButton(self.frame_14)
        self.bt_read_file.setObjectName(u"bt_read_file")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.bt_read_file.setFont(font2)
        self.bt_read_file.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/bree/document-sticky-note.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.bt_read_file.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.bt_read_file)

        self.bt_save_file = QPushButton(self.frame_14)
        self.bt_save_file.setObjectName(u"bt_save_file")
        self.bt_save_file.setFont(font1)
        self.bt_save_file.setStyleSheet(
            u"background-color: rgb(85, 170, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/bree/folder-open-document.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.bt_save_file.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.bt_save_file)

        self.bt_close = QPushButton(self.frame_14)
        self.bt_close.setObjectName(u"bt_close")
        self.bt_close.setFont(font1)
        self.bt_close.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        icon3 = QIcon()
        icon3.addFile(u":/bree/verificar.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.bt_close.setIcon(icon3)

        self.horizontalLayout_3.addWidget(self.bt_close)

        self.verticalLayout_3.addWidget(self.frame_14)

        QWidget.setTabOrder(self.cb_Conex, self.spinBoxNumElos)
        QWidget.setTabOrder(self.spinBoxNumElos, self.ed_Vn)
        QWidget.setTabOrder(self.ed_Vn, self.ed_Fr)
        QWidget.setTabOrder(self.ed_Fr, self.ed_KVAR)
        QWidget.setTabOrder(self.ed_KVAR, self.ed_Cap)
        QWidget.setTabOrder(self.ed_Cap, self.ed_size_un)
        QWidget.setTabOrder(self.ed_size_un, self.ed_G_SI)
        QWidget.setTabOrder(self.ed_G_SI, self.ed_GPI)
        QWidget.setTabOrder(self.ed_GPI, self.ed_serie)
        QWidget.setTabOrder(self.ed_serie, self.ed_P0)
        QWidget.setTabOrder(self.ed_P0, self.ed_S1)
        QWidget.setTabOrder(self.ed_S1, self.ed_S2)
        QWidget.setTabOrder(self.ed_S2, self.ed_P1)
        QWidget.setTabOrder(self.ed_P1, self.ed_P2)
        QWidget.setTabOrder(self.ed_P2, self.ed_PST)
        QWidget.setTabOrder(self.ed_PST, self.ed_KURL)
        QWidget.setTabOrder(self.ed_KURL, self.ed_KMIN)
        QWidget.setTabOrder(self.ed_KMIN, self.ed_file_name)
        QWidget.setTabOrder(self.ed_file_name, self.bt_calc)
        QWidget.setTabOrder(self.bt_calc, self.bt_read_file)
        QWidget.setTabOrder(self.bt_read_file, self.bt_save_file)
        QWidget.setTabOrder(self.bt_save_file, self.bt_close)
        QWidget.setTabOrder(self.bt_close, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.tableView_2)
        QWidget.setTabOrder(self.tableView_2, self.tableView_3)
        QWidget.setTabOrder(self.tableView_3, self.tableView_1)

        self.retranslateUi(Win_FuseIn)
        self.bt_close.clicked.connect(Win_FuseIn.close)

        self.tabWidget.setCurrentIndex(0)
        self.cb_Conex.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(Win_FuseIn)
    # setupUi

    def retranslateUi(self, Win_FuseIn):
        Win_FuseIn.setWindowTitle(QCoreApplication.translate(
            "Win_FuseIn", u"Fus\u00edvel Interno", None))
        self.label_19.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Fus\u00edvel Interno", None))
        self.label_20.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Conex\u00e3o do Banco", None))
        self.label_2.setText(QCoreApplication.translate(
            "Win_FuseIn", u"# elos fus\u00edveis", None))
        self.label_4.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Tens\u00e3o (V)", None))
        self.label_5.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Frequ\u00eancia (Hz)", None))
        self.label_6.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Pot\u00eancia Reativa (KVAr)/Se\u00e7\u00e3o", None))
        self.label_11.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Capacit\u00e2ncia (uF)", None))
        self.label_7.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Tamanho da Unidade (3-11)", None))
        self.label_9.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Grupos S\u00e9rie (GS)", None))
        self.label_10.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Grupos Paralelo (GP)", None))
        self.label_S.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Capacitores S\u00e9rie (S)", None))
        self.label_P0.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Capacitores paralelo (P)", None))
        self.label_S1.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Capacitores S\u00e9rie (S1)", None))
        self.label_S2.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Capacitores S\u00e9rie (S2)", None))
        self.label_P1.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Capacitores Paralelo (P1)", None))
        self.label_P2.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Capacitores Papralelo (P2)", None))
        self.label_23.setText(
            QCoreApplication.translate("Win_FuseIn", u"PST", None))
        self.label_27.setText(QCoreApplication.translate(
            "Win_FuseIn", u"KURL", None))
        self.label.setText(QCoreApplication.translate(
            "Win_FuseIn", u"KMIN", None))
        self.label_12.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Nome do arquivo de resultado", None))
        self.cb_Conex.setItemText(
            0, QCoreApplication.translate("Win_FuseIn", u"Y", None))
        self.cb_Conex.setItemText(
            1, QCoreApplication.translate("Win_FuseIn", u"Y0", None))
        self.cb_Conex.setItemText(
            2, QCoreApplication.translate("Win_FuseIn", u"I", None))
        self.cb_Conex.setItemText(
            3, QCoreApplication.translate("Win_FuseIn", u"D", None))
        self.cb_Conex.setItemText(
            4, QCoreApplication.translate("Win_FuseIn", u"YY", None))
        self.cb_Conex.setItemText(
            5, QCoreApplication.translate("Win_FuseIn", u"Y0HI", None))
        self.cb_Conex.setItemText(
            6, QCoreApplication.translate("Win_FuseIn", u"YH", None))
        self.cb_Conex.setItemText(
            7, QCoreApplication.translate("Win_FuseIn", u"H", None))
        self.cb_Conex.setItemText(
            8, QCoreApplication.translate("Win_FuseIn", u"Y0H", None))
        self.cb_Conex.setItemText(
            9, QCoreApplication.translate("Win_FuseIn", u"HI", None))
        self.cb_Conex.setItemText(
            10, QCoreApplication.translate("Win_FuseIn", u"YHI", None))
        self.cb_Conex.setItemText(
            11, QCoreApplication.translate("Win_FuseIn", u"DHI", None))
        self.cb_Conex.setItemText(
            12, QCoreApplication.translate("Win_FuseIn", u"DH", None))

        self.cb_Conex.setPlaceholderText("")
        self.ed_Vn.setText(QCoreApplication.translate(
            "Win_FuseIn", u"7960", None))
        self.ed_Vn.setPlaceholderText(QCoreApplication.translate(
            "Win_FuseIn", u"Tens\u00e3o (V)", None))
        self.ed_Fr.setText(QCoreApplication.translate(
            "Win_FuseIn", u"60", None))
        self.ed_Fr.setPlaceholderText(QCoreApplication.translate(
            "Win_FuseIn", u"Frequ\u00eancia (HZ)", None))
        self.ed_KVAR.setText(QCoreApplication.translate(
            "Win_FuseIn", u"300", None))
        self.ed_KVAR.setPlaceholderText(QCoreApplication.translate(
            "Win_FuseIn", u"Pot\u00eancia Reativa (kVAr)", None))
        self.ed_Cap.setText(
            QCoreApplication.translate("Win_FuseIn", u"0", None))
        self.ed_size_un.setText(
            QCoreApplication.translate("Win_FuseIn", u"10", None))
        self.ed_G_SI.setText(
            QCoreApplication.translate("Win_FuseIn", u"5", None))
        self.ed_G_SI.setPlaceholderText(
            QCoreApplication.translate("Win_FuseIn", u"MILS Paper", None))
        self.ed_GPI.setText(QCoreApplication.translate(
            "Win_FuseIn", u"10", None))
        self.ed_GPI.setPlaceholderText(
            QCoreApplication.translate("Win_FuseIn", u"MILS Filme", None))
        self.ed_serie.setText(
            QCoreApplication.translate("Win_FuseIn", u"1", None))
        self.ed_serie.setPlaceholderText(
            QCoreApplication.translate("Win_FuseIn", u"Sobre Voltas", None))
        self.ed_P0.setText(QCoreApplication.translate(
            "Win_FuseIn", u"1", None))
        self.ed_S1.setText(QCoreApplication.translate(
            "Win_FuseIn", u"1", None))
        self.ed_S2.setText(QCoreApplication.translate(
            "Win_FuseIn", u"1", None))
        self.ed_P1.setText(QCoreApplication.translate(
            "Win_FuseIn", u"7", None))
        self.ed_P2.setText(QCoreApplication.translate(
            "Win_FuseIn", u"7", None))
        self.ed_PST.setText(
            QCoreApplication.translate("Win_FuseIn", u"1", None))
        self.ed_KURL.setText(QCoreApplication.translate(
            "Win_FuseIn", u"2.5", None))
        self.ed_KMIN.setText(QCoreApplication.translate(
            "Win_FuseIn", u"0.9", None))
        self.ed_file_name.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Resultado FuseIn", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabInput), QCoreApplication.translate("Win_FuseIn", u"Entrada geral", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(
            self.tabDF), QCoreApplication.translate("Win_FuseIn", u"Data Frame", None))
        self.bt_calc.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Calcular...", None))
        self.bt_read_file.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Ler Arquivo...", None))
        self.bt_save_file.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Salvar Arquivo...", None))
        self.bt_close.setText(QCoreApplication.translate(
            "Win_FuseIn", u"Voltar...", None))
    # retranslateUi
