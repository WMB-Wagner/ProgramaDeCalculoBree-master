# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'capacitor_Potencia.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_win_CpEn(object):
    def setupUi(self, win_CpEn):
        if not win_CpEn.objectName():
            win_CpEn.setObjectName(u"win_CpEn")
        win_CpEn.resize(646, 876)
        win_CpEn.setMinimumSize(QSize(609, 650))
        font = QFont()
        font.setPointSize(9)
        win_CpEn.setFont(font)
        win_CpEn.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(win_CpEn)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_19 = QLabel(win_CpEn)
        self.label_19.setObjectName(u"label_19")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_19.setFont(font1)
        self.label_19.setStyleSheet(u"background-color: rgb(0, 170, 255);")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_19)

        self.tabWidgetCP = QTabWidget(win_CpEn)
        self.tabWidgetCP.setObjectName(u"tabWidgetCP")
        self.tabWidgetCP.setEnabled(True)
        self.tabWidgetCP.setTabPosition(QTabWidget.North)
        self.tabWidgetCP.setTabShape(QTabWidget.Triangular)
        self.tabInput = QWidget()
        self.tabInput.setObjectName(u"tabInput")
        self.verticalLayout_5 = QVBoxLayout(self.tabInput)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.scrollArea = QScrollArea(self.tabInput)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 583, 854))
        self.verticalLayout_16 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_input = QFrame(self.scrollAreaWidgetContents)
        self.frame_input.setObjectName(u"frame_input")
        self.frame_input.setFrameShape(QFrame.NoFrame)
        self.frame_input.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_input)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.fr_labels = QFrame(self.frame_input)
        self.fr_labels.setObjectName(u"fr_labels")
        self.fr_labels.setFrameShape(QFrame.NoFrame)
        self.fr_labels.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_labels)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_41 = QLabel(self.fr_labels)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_41)

        self.label_35 = QLabel(self.fr_labels)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_35)

        self.label_51 = QLabel(self.fr_labels)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_51)

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

        self.label_7 = QLabel(self.fr_labels)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.label_vCoil = QLabel(self.fr_labels)
        self.label_vCoil.setObjectName(u"label_vCoil")
        self.label_vCoil.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_vCoil)

        self.label_paper = QLabel(self.fr_labels)
        self.label_paper.setObjectName(u"label_paper")
        self.label_paper.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_paper)

        self.label_49 = QLabel(self.fr_labels)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_49)

        self.label_52 = QLabel(self.fr_labels)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_52)

        self.label_filme2 = QLabel(self.fr_labels)
        self.label_filme2.setObjectName(u"label_filme2")
        self.label_filme2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_filme2)

        self.label_filme3 = QLabel(self.fr_labels)
        self.label_filme3.setObjectName(u"label_filme3")
        self.label_filme3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_filme3)

        self.label_10 = QLabel(self.fr_labels)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label_11 = QLabel(self.fr_labels)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.label_34 = QLabel(self.fr_labels)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_34)

        self.label_12 = QLabel(self.fr_labels)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_12)

        self.label_38 = QLabel(self.fr_labels)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_38)

        self.label_13 = QLabel(self.fr_labels)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.label_14 = QLabel(self.fr_labels)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_14)

        self.label_15 = QLabel(self.fr_labels)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_15)

        self.label_16 = QLabel(self.fr_labels)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_16)

        self.label_17 = QLabel(self.fr_labels)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_17)

        self.label_18 = QLabel(self.fr_labels)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_18)

        self.label_43 = QLabel(self.fr_labels)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_43)

        self.label_44 = QLabel(self.fr_labels)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_44)

        self.label_45 = QLabel(self.fr_labels)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_45)

        self.label_46 = QLabel(self.fr_labels)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_46)

        self.label_32 = QLabel(self.fr_labels)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout.addWidget(self.label_32)

        self.verticalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)


        self.horizontalLayout.addWidget(self.fr_labels)

        self.fr_edit = QFrame(self.frame_input)
        self.fr_edit.setObjectName(u"fr_edit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fr_edit.sizePolicy().hasHeightForWidth())
        self.fr_edit.setSizePolicy(sizePolicy1)
        self.fr_edit.setFrameShape(QFrame.NoFrame)
        self.fr_edit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.fr_edit)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cb_modelo = QComboBox(self.fr_edit)
        self.cb_modelo.addItem("")
        self.cb_modelo.addItem("")
        self.cb_modelo.addItem("")
        self.cb_modelo.addItem("")
        self.cb_modelo.addItem("")
        self.cb_modelo.addItem("")
        self.cb_modelo.addItem("")
        self.cb_modelo.addItem("")
        self.cb_modelo.addItem("")
        self.cb_modelo.addItem("")
        self.cb_modelo.setObjectName(u"cb_modelo")

        self.verticalLayout_2.addWidget(self.cb_modelo)

        self.spN_Buchas = QSpinBox(self.fr_edit)
        self.spN_Buchas.setObjectName(u"spN_Buchas")
        self.spN_Buchas.setMinimum(1)
        self.spN_Buchas.setMaximum(2)
        self.spN_Buchas.setValue(2)

        self.verticalLayout_2.addWidget(self.spN_Buchas)

        self.cb_NBI = QComboBox(self.fr_edit)
        self.cb_NBI.addItem("")
        self.cb_NBI.addItem("")
        self.cb_NBI.addItem("")
        self.cb_NBI.addItem("")
        self.cb_NBI.addItem("")
        self.cb_NBI.addItem("")
        self.cb_NBI.setObjectName(u"cb_NBI")
        self.cb_NBI.setEditable(True)

        self.verticalLayout_2.addWidget(self.cb_NBI)

        self.cb_Eixos = QComboBox(self.fr_edit)
        self.cb_Eixos.addItem("")
        self.cb_Eixos.addItem("")
        self.cb_Eixos.setObjectName(u"cb_Eixos")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cb_Eixos.sizePolicy().hasHeightForWidth())
        self.cb_Eixos.setSizePolicy(sizePolicy2)

        self.verticalLayout_2.addWidget(self.cb_Eixos)

        self.ed_Vn = QLineEdit(self.fr_edit)
        self.ed_Vn.setObjectName(u"ed_Vn")
        sizePolicy2.setHeightForWidth(self.ed_Vn.sizePolicy().hasHeightForWidth())
        self.ed_Vn.setSizePolicy(sizePolicy2)
        self.ed_Vn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_Vn)

        self.ed_Fr = QLineEdit(self.fr_edit)
        self.ed_Fr.setObjectName(u"ed_Fr")
        sizePolicy2.setHeightForWidth(self.ed_Fr.sizePolicy().hasHeightForWidth())
        self.ed_Fr.setSizePolicy(sizePolicy2)
        self.ed_Fr.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_Fr)

        self.ed_KVAR = QLineEdit(self.fr_edit)
        self.ed_KVAR.setObjectName(u"ed_KVAR")
        sizePolicy2.setHeightForWidth(self.ed_KVAR.sizePolicy().hasHeightForWidth())
        self.ed_KVAR.setSizePolicy(sizePolicy2)
        self.ed_KVAR.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_KVAR)

        self.Ed_Ncoil = QLineEdit(self.fr_edit)
        self.Ed_Ncoil.setObjectName(u"Ed_Ncoil")
        sizePolicy2.setHeightForWidth(self.Ed_Ncoil.sizePolicy().hasHeightForWidth())
        self.Ed_Ncoil.setSizePolicy(sizePolicy2)
        self.Ed_Ncoil.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.Ed_Ncoil)

        self.ed_Vcoil = QDoubleSpinBox(self.fr_edit)
        self.ed_Vcoil.setObjectName(u"ed_Vcoil")
        self.ed_Vcoil.setMaximum(10000.000000000000000)
        self.ed_Vcoil.setValue(1990.000000000000000)

        self.verticalLayout_2.addWidget(self.ed_Vcoil)

        self.Ed_MilsPaper = QLineEdit(self.fr_edit)
        self.Ed_MilsPaper.setObjectName(u"Ed_MilsPaper")
        sizePolicy2.setHeightForWidth(self.Ed_MilsPaper.sizePolicy().hasHeightForWidth())
        self.Ed_MilsPaper.setSizePolicy(sizePolicy2)
        self.Ed_MilsPaper.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.Ed_MilsPaper)

        self.spinBoxNumFilmes = QSpinBox(self.fr_edit)
        self.spinBoxNumFilmes.setObjectName(u"spinBoxNumFilmes")
        self.spinBoxNumFilmes.setMinimum(2)
        self.spinBoxNumFilmes.setMaximum(3)
        self.spinBoxNumFilmes.setValue(2)

        self.verticalLayout_2.addWidget(self.spinBoxNumFilmes)

        self.cb_filme1 = QComboBox(self.fr_edit)
        self.cb_filme1.setObjectName(u"cb_filme1")
        self.cb_filme1.setEditable(True)

        self.verticalLayout_2.addWidget(self.cb_filme1)

        self.cb_filme2 = QComboBox(self.fr_edit)
        self.cb_filme2.setObjectName(u"cb_filme2")
        self.cb_filme2.setEditable(True)

        self.verticalLayout_2.addWidget(self.cb_filme2)

        self.cb_filme3 = QComboBox(self.fr_edit)
        self.cb_filme3.setObjectName(u"cb_filme3")
        self.cb_filme3.setEditable(True)

        self.verticalLayout_2.addWidget(self.cb_filme3)

        self.ed_milsFilm = QLineEdit(self.fr_edit)
        self.ed_milsFilm.setObjectName(u"ed_milsFilm")
        self.ed_milsFilm.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.ed_milsFilm.sizePolicy().hasHeightForWidth())
        self.ed_milsFilm.setSizePolicy(sizePolicy2)
        self.ed_milsFilm.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_milsFilm)

        self.ed_gauge_Al = QLineEdit(self.fr_edit)
        self.ed_gauge_Al.setObjectName(u"ed_gauge_Al")
        sizePolicy2.setHeightForWidth(self.ed_gauge_Al.sizePolicy().hasHeightForWidth())
        self.ed_gauge_Al.setSizePolicy(sizePolicy2)
        self.ed_gauge_Al.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_gauge_Al)

        self.dSPCalco = QDoubleSpinBox(self.fr_edit)
        self.dSPCalco.setObjectName(u"dSPCalco")
        self.dSPCalco.setMinimum(1.000000000000000)
        self.dSPCalco.setMaximum(5.000000000000000)
        self.dSPCalco.setValue(3.000000000000000)

        self.verticalLayout_2.addWidget(self.dSPCalco)

        self.ed_Hcoil = QLineEdit(self.fr_edit)
        self.ed_Hcoil.setObjectName(u"ed_Hcoil")
        sizePolicy2.setHeightForWidth(self.ed_Hcoil.sizePolicy().hasHeightForWidth())
        self.ed_Hcoil.setSizePolicy(sizePolicy2)
        self.ed_Hcoil.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.ed_Hcoil.setReadOnly(False)

        self.verticalLayout_2.addWidget(self.ed_Hcoil)

        self.dSpinFolga = QDoubleSpinBox(self.fr_edit)
        self.dSpinFolga.setObjectName(u"dSpinFolga")
        self.dSpinFolga.setDecimals(1)
        self.dSpinFolga.setValue(60.000000000000000)

        self.verticalLayout_2.addWidget(self.dSpinFolga)

        self.ed_lamelas_foil = QLineEdit(self.fr_edit)
        self.ed_lamelas_foil.setObjectName(u"ed_lamelas_foil")
        sizePolicy2.setHeightForWidth(self.ed_lamelas_foil.sizePolicy().hasHeightForWidth())
        self.ed_lamelas_foil.setSizePolicy(sizePolicy2)
        self.ed_lamelas_foil.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_lamelas_foil)

        self.ed_larg_foil = QLineEdit(self.fr_edit)
        self.ed_larg_foil.setObjectName(u"ed_larg_foil")
        sizePolicy2.setHeightForWidth(self.ed_larg_foil.sizePolicy().hasHeightForWidth())
        self.ed_larg_foil.setSizePolicy(sizePolicy2)
        self.ed_larg_foil.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_larg_foil)

        self.ed_tol = QLineEdit(self.fr_edit)
        self.ed_tol.setObjectName(u"ed_tol")
        sizePolicy2.setHeightForWidth(self.ed_tol.sizePolicy().hasHeightForWidth())
        self.ed_tol.setSizePolicy(sizePolicy2)
        self.ed_tol.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_tol)

        self.ed_FatorEsp = QLineEdit(self.fr_edit)
        self.ed_FatorEsp.setObjectName(u"ed_FatorEsp")
        sizePolicy2.setHeightForWidth(self.ed_FatorEsp.sizePolicy().hasHeightForWidth())
        self.ed_FatorEsp.setSizePolicy(sizePolicy2)
        self.ed_FatorEsp.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_FatorEsp)

        self.ed_sobre_voltas = QLineEdit(self.fr_edit)
        self.ed_sobre_voltas.setObjectName(u"ed_sobre_voltas")
        sizePolicy2.setHeightForWidth(self.ed_sobre_voltas.sizePolicy().hasHeightForWidth())
        self.ed_sobre_voltas.setSizePolicy(sizePolicy2)
        self.ed_sobre_voltas.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_sobre_voltas)

        self.ed_fator_coil = QLineEdit(self.fr_edit)
        self.ed_fator_coil.setObjectName(u"ed_fator_coil")
        sizePolicy2.setHeightForWidth(self.ed_fator_coil.sizePolicy().hasHeightForWidth())
        self.ed_fator_coil.setSizePolicy(sizePolicy2)
        self.ed_fator_coil.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.ed_fator_coil)

        self.cb_Conexao = QComboBox(self.fr_edit)
        self.cb_Conexao.addItem("")
        self.cb_Conexao.addItem("")
        self.cb_Conexao.setObjectName(u"cb_Conexao")
        self.cb_Conexao.setEditable(True)

        self.verticalLayout_2.addWidget(self.cb_Conexao)

        self.ed_Watts = QLineEdit(self.fr_edit)
        self.ed_Watts.setObjectName(u"ed_Watts")

        self.verticalLayout_2.addWidget(self.ed_Watts)

        self.ed_Tempo = QLineEdit(self.fr_edit)
        self.ed_Tempo.setObjectName(u"ed_Tempo")

        self.verticalLayout_2.addWidget(self.ed_Tempo)

        self.ed_Vend = QLineEdit(self.fr_edit)
        self.ed_Vend.setObjectName(u"ed_Vend")

        self.verticalLayout_2.addWidget(self.ed_Vend)

        self.ed_file_name = QLineEdit(self.fr_edit)
        self.ed_file_name.setObjectName(u"ed_file_name")

        self.verticalLayout_2.addWidget(self.ed_file_name)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)


        self.horizontalLayout.addWidget(self.fr_edit)

        self.frame_15 = QFrame(self.frame_input)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy3)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.ck_eixo = QCheckBox(self.frame_15)
        self.ck_eixo.setObjectName(u"ck_eixo")
        self.ck_eixo.setGeometry(QRect(10, 335, 16, 18))
        sizePolicy4 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.ck_eixo.sizePolicy().hasHeightForWidth())
        self.ck_eixo.setSizePolicy(sizePolicy4)
        self.ck_eixo.setChecked(False)
        self.cb_mandris = QComboBox(self.frame_15)
        self.cb_mandris.setObjectName(u"cb_mandris")
        self.cb_mandris.setGeometry(QRect(78, 334, 69, 20))
        self.cb_mandris.setEditable(True)
        self.label_37 = QLabel(self.frame_15)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setGeometry(QRect(0, 10, 151, 16))
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_37.sizePolicy().hasHeightForWidth())
        self.label_37.setSizePolicy(sizePolicy5)
        self.label_37.setAlignment(Qt.AlignCenter)
        self.inputCodLateral = QLineEdit(self.frame_15)
        self.inputCodLateral.setObjectName(u"inputCodLateral")
        self.inputCodLateral.setGeometry(QRect(10, 30, 113, 20))
        self.inputCodLateral.setReadOnly(True)
        self.labelDescr = QLabel(self.frame_15)
        self.labelDescr.setObjectName(u"labelDescr")
        self.labelDescr.setGeometry(QRect(40, 60, 61, 16))
        self.label_40 = QLabel(self.frame_15)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setGeometry(QRect(30, 140, 91, 16))
        self.ed_codFilm1 = QLineEdit(self.frame_15)
        self.ed_codFilm1.setObjectName(u"ed_codFilm1")
        self.ed_codFilm1.setGeometry(QRect(20, 160, 113, 20))
        self.label_42 = QLabel(self.frame_15)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(30, 190, 81, 16))
        self.ed_codFilm2 = QLineEdit(self.frame_15)
        self.ed_codFilm2.setObjectName(u"ed_codFilm2")
        self.ed_codFilm2.setGeometry(QRect(20, 210, 113, 20))
        self.ed_codFilm2.setReadOnly(True)
        self.label_CodFilm3 = QLabel(self.frame_15)
        self.label_CodFilm3.setObjectName(u"label_CodFilm3")
        self.label_CodFilm3.setGeometry(QRect(30, 240, 81, 20))
        self.ed_codFilm3 = QLineEdit(self.frame_15)
        self.ed_codFilm3.setObjectName(u"ed_codFilm3")
        self.ed_codFilm3.setGeometry(QRect(20, 260, 113, 20))
        self.ed_codFilm3.setReadOnly(True)
        self.inputDescr = QPlainTextEdit(self.frame_15)
        self.inputDescr.setObjectName(u"inputDescr")
        self.inputDescr.setGeometry(QRect(10, 80, 141, 61))
        self.checkBoxAutoNCoils = QCheckBox(self.frame_15)
        self.checkBoxAutoNCoils.setObjectName(u"checkBoxAutoNCoils")
        self.checkBoxAutoNCoils.setGeometry(QRect(10, 380, 141, 17))
        self.checkBoxAutoNCoils.setChecked(True)

        self.horizontalLayout.addWidget(self.frame_15)


        self.verticalLayout_16.addWidget(self.frame_input)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_5.addWidget(self.scrollArea)

        self.tabWidgetCP.addTab(self.tabInput, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_17 = QVBoxLayout(self.tab_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(10)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.label_9 = QLabel(self.tab_4)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.label_53 = QLabel(self.tab_4)
        self.label_53.setObjectName(u"label_53")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_53)

        self.label_54 = QLabel(self.tab_4)
        self.label_54.setObjectName(u"label_54")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_54)

        self.label_55 = QLabel(self.tab_4)
        self.label_55.setObjectName(u"label_55")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_55)

        self.label_56 = QLabel(self.tab_4)
        self.label_56.setObjectName(u"label_56")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_56)

        self.label_58 = QLabel(self.tab_4)
        self.label_58.setObjectName(u"label_58")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_58)

        self.label_59 = QLabel(self.tab_4)
        self.label_59.setObjectName(u"label_59")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_59)

        self.label_60 = QLabel(self.tab_4)
        self.label_60.setObjectName(u"label_60")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_60)

        self.label_61 = QLabel(self.tab_4)
        self.label_61.setObjectName(u"label_61")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_61)

        self.label_62 = QLabel(self.tab_4)
        self.label_62.setObjectName(u"label_62")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_62)

        self.ed_PapelBK = QLineEdit(self.tab_4)
        self.ed_PapelBK.setObjectName(u"ed_PapelBK")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.ed_PapelBK)

        self.ed_FilmeDK = QLineEdit(self.tab_4)
        self.ed_FilmeDK.setObjectName(u"ed_FilmeDK")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.ed_FilmeDK)

        self.ed_OleoDK = QLineEdit(self.tab_4)
        self.ed_OleoDK.setObjectName(u"ed_OleoDK")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.ed_OleoDK)

        self.ed_rhoPaper = QLineEdit(self.tab_4)
        self.ed_rhoPaper.setObjectName(u"ed_rhoPaper")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ed_rhoPaper)

        self.ed_custoPaper = QLineEdit(self.tab_4)
        self.ed_custoPaper.setObjectName(u"ed_custoPaper")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.ed_custoPaper)

        self.ed_custoFilm = QLineEdit(self.tab_4)
        self.ed_custoFilm.setObjectName(u"ed_custoFilm")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.ed_custoFilm)

        self.ed_custoFoil = QLineEdit(self.tab_4)
        self.ed_custoFoil.setObjectName(u"ed_custoFoil")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.ed_custoFoil)

        self.ed_largFoil = QLineEdit(self.tab_4)
        self.ed_largFoil.setObjectName(u"ed_largFoil")

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.ed_largFoil)

        self.ed_largDie = QLineEdit(self.tab_4)
        self.ed_largDie.setObjectName(u"ed_largDie")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.ed_largDie)

        self.ed_Refugo = QLineEdit(self.tab_4)
        self.ed_Refugo.setObjectName(u"ed_Refugo")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.ed_Refugo)


        self.verticalLayout_17.addLayout(self.formLayout)

        self.tabWidgetCP.addTab(self.tab_4, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.lb_fatorEsp = QDoubleSpinBox(self.tab)
        self.lb_fatorEsp.setObjectName(u"lb_fatorEsp")
        self.lb_fatorEsp.setReadOnly(True)
        self.lb_fatorEsp.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.lb_fatorEsp)

        self.label_2 = QLabel(self.tab)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lb_compFoil = QDoubleSpinBox(self.tab)
        self.lb_compFoil.setObjectName(u"lb_compFoil")
        self.lb_compFoil.setReadOnly(True)
        self.lb_compFoil.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lb_compFoil)

        self.label_3 = QLabel(self.tab)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.lb_fat_Bob = QDoubleSpinBox(self.tab)
        self.lb_fat_Bob.setObjectName(u"lb_fat_Bob")
        self.lb_fat_Bob.setReadOnly(True)
        self.lb_fat_Bob.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.lb_fat_Bob)

        self.label_21 = QLabel(self.tab)
        self.label_21.setObjectName(u"label_21")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_21)

        self.lb_voltasFoil = QDoubleSpinBox(self.tab)
        self.lb_voltasFoil.setObjectName(u"lb_voltasFoil")
        self.lb_voltasFoil.setReadOnly(True)
        self.lb_voltasFoil.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.lb_voltasFoil)

        self.label_22 = QLabel(self.tab)
        self.label_22.setObjectName(u"label_22")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_22)

        self.lb_sobreVoltas = QDoubleSpinBox(self.tab)
        self.lb_sobreVoltas.setObjectName(u"lb_sobreVoltas")
        self.lb_sobreVoltas.setReadOnly(True)
        self.lb_sobreVoltas.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.lb_sobreVoltas)

        self.label_23 = QLabel(self.tab)
        self.label_23.setObjectName(u"label_23")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.label_23)

        self.lb_tCoils = QDoubleSpinBox(self.tab)
        self.lb_tCoils.setObjectName(u"lb_tCoils")
        self.lb_tCoils.setReadOnly(True)
        self.lb_tCoils.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.lb_tCoils)

        self.label_24 = QLabel(self.tab)
        self.label_24.setObjectName(u"label_24")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_24)

        self.lb_epBob = QDoubleSpinBox(self.tab)
        self.lb_epBob.setObjectName(u"lb_epBob")
        self.lb_epBob.setReadOnly(True)
        self.lb_epBob.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.lb_epBob)

        self.label_25 = QLabel(self.tab)
        self.label_25.setObjectName(u"label_25")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_25)

        self.lb_cUn = QDoubleSpinBox(self.tab)
        self.lb_cUn.setObjectName(u"lb_cUn")
        self.lb_cUn.setReadOnly(True)
        self.lb_cUn.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.lb_cUn)

        self.label_26 = QLabel(self.tab)
        self.label_26.setObjectName(u"label_26")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_26)

        self.lb_cCoil = QDoubleSpinBox(self.tab)
        self.lb_cCoil.setObjectName(u"lb_cCoil")
        self.lb_cCoil.setReadOnly(True)
        self.lb_cCoil.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.lb_cCoil)

        self.label_27 = QLabel(self.tab)
        self.label_27.setObjectName(u"label_27")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label_27)

        self.lb_larg = QDoubleSpinBox(self.tab)
        self.lb_larg.setObjectName(u"lb_larg")
        self.lb_larg.setReadOnly(True)
        self.lb_larg.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.lb_larg)

        self.label_64 = QLabel(self.tab)
        self.label_64.setObjectName(u"label_64")

        self.formLayout_2.setWidget(10, QFormLayout.LabelRole, self.label_64)

        self.lbdsMan = QDoubleSpinBox(self.tab)
        self.lbdsMan.setObjectName(u"lbdsMan")
        self.lbdsMan.setReadOnly(True)
        self.lbdsMan.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(10, QFormLayout.FieldRole, self.lbdsMan)

        self.label_65 = QLabel(self.tab)
        self.label_65.setObjectName(u"label_65")

        self.formLayout_2.setWidget(11, QFormLayout.LabelRole, self.label_65)

        self.lb_vCoil = QDoubleSpinBox(self.tab)
        self.lb_vCoil.setObjectName(u"lb_vCoil")
        self.lb_vCoil.setReadOnly(True)
        self.lb_vCoil.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(11, QFormLayout.FieldRole, self.lb_vCoil)

        self.label_30 = QLabel(self.tab)
        self.label_30.setObjectName(u"label_30")

        self.formLayout_2.setWidget(12, QFormLayout.LabelRole, self.label_30)

        self.spin_stressVPM = QDoubleSpinBox(self.tab)
        self.spin_stressVPM.setObjectName(u"spin_stressVPM")
        self.spin_stressVPM.setReadOnly(True)
        self.spin_stressVPM.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(12, QFormLayout.FieldRole, self.spin_stressVPM)

        self.label_66 = QLabel(self.tab)
        self.label_66.setObjectName(u"label_66")

        self.formLayout_2.setWidget(13, QFormLayout.LabelRole, self.label_66)

        self.spin_Stress = QDoubleSpinBox(self.tab)
        self.spin_Stress.setObjectName(u"spin_Stress")
        self.spin_Stress.setReadOnly(True)
        self.spin_Stress.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(13, QFormLayout.FieldRole, self.spin_Stress)

        self.label_67 = QLabel(self.tab)
        self.label_67.setObjectName(u"label_67")

        self.formLayout_2.setWidget(14, QFormLayout.LabelRole, self.label_67)

        self.lb_pfPrin = QDoubleSpinBox(self.tab)
        self.lb_pfPrin.setObjectName(u"lb_pfPrin")
        self.lb_pfPrin.setReadOnly(True)
        self.lb_pfPrin.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(14, QFormLayout.FieldRole, self.lb_pfPrin)

        self.label_69 = QLabel(self.tab)
        self.label_69.setObjectName(u"label_69")

        self.formLayout_2.setWidget(15, QFormLayout.LabelRole, self.label_69)

        self.lb_95PF = QDoubleSpinBox(self.tab)
        self.lb_95PF.setObjectName(u"lb_95PF")
        self.lb_95PF.setReadOnly(True)
        self.lb_95PF.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(15, QFormLayout.FieldRole, self.lb_95PF)

        self.label_70 = QLabel(self.tab)
        self.label_70.setObjectName(u"label_70")

        self.formLayout_2.setWidget(16, QFormLayout.LabelRole, self.label_70)

        self.lb_pFoil = QDoubleSpinBox(self.tab)
        self.lb_pFoil.setObjectName(u"lb_pFoil")
        self.lb_pFoil.setReadOnly(True)
        self.lb_pFoil.setMaximum(9999.989999999999782)

        self.formLayout_2.setWidget(16, QFormLayout.FieldRole, self.lb_pFoil)

        self.label_8 = QLabel(self.tab)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(17, QFormLayout.LabelRole, self.label_8)

        self.spinBoxGS = QSpinBox(self.tab)
        self.spinBoxGS.setObjectName(u"spinBoxGS")
        self.spinBoxGS.setReadOnly(True)

        self.formLayout_2.setWidget(17, QFormLayout.FieldRole, self.spinBoxGS)

        self.label_31 = QLabel(self.tab)
        self.label_31.setObjectName(u"label_31")

        self.formLayout_2.setWidget(18, QFormLayout.LabelRole, self.label_31)

        self.spinBoxGP = QSpinBox(self.tab)
        self.spinBoxGP.setObjectName(u"spinBoxGP")
        self.spinBoxGP.setReadOnly(True)

        self.formLayout_2.setWidget(18, QFormLayout.FieldRole, self.spinBoxGP)

        self.label_33 = QLabel(self.tab)
        self.label_33.setObjectName(u"label_33")

        self.formLayout_2.setWidget(19, QFormLayout.LabelRole, self.label_33)

        self.spinBoxGSGP = QSpinBox(self.tab)
        self.spinBoxGSGP.setObjectName(u"spinBoxGSGP")
        self.spinBoxGSGP.setReadOnly(True)

        self.formLayout_2.setWidget(19, QFormLayout.FieldRole, self.spinBoxGSGP)

        self.line = QFrame(self.tab)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Sunken)
        self.line.setLineWidth(8)
        self.line.setMidLineWidth(8)
        self.line.setFrameShape(QFrame.HLine)

        self.formLayout_2.setWidget(20, QFormLayout.FieldRole, self.line)

        self.codSecCapacitivaLineEdit = QLineEdit(self.tab)
        self.codSecCapacitivaLineEdit.setObjectName(u"codSecCapacitivaLineEdit")

        self.formLayout_2.setWidget(21, QFormLayout.FieldRole, self.codSecCapacitivaLineEdit)

        self.label_73 = QLabel(self.tab)
        self.label_73.setObjectName(u"label_73")

        self.formLayout_2.setWidget(23, QFormLayout.LabelRole, self.label_73)

        self.comboBoxCaixas = QComboBox(self.tab)
        self.comboBoxCaixas.setObjectName(u"comboBoxCaixas")

        self.formLayout_2.setWidget(23, QFormLayout.FieldRole, self.comboBoxCaixas)

        self.label_74 = QLabel(self.tab)
        self.label_74.setObjectName(u"label_74")

        self.formLayout_2.setWidget(24, QFormLayout.LabelRole, self.label_74)

        self.dSpinHBox = QSpinBox(self.tab)
        self.dSpinHBox.setObjectName(u"dSpinHBox")
        self.dSpinHBox.setReadOnly(True)
        self.dSpinHBox.setMaximum(10000)

        self.formLayout_2.setWidget(24, QFormLayout.FieldRole, self.dSpinHBox)

        self.label_75 = QLabel(self.tab)
        self.label_75.setObjectName(u"label_75")

        self.formLayout_2.setWidget(25, QFormLayout.LabelRole, self.label_75)

        self.dSpinPBox = QSpinBox(self.tab)
        self.dSpinPBox.setObjectName(u"dSpinPBox")
        self.dSpinPBox.setReadOnly(True)
        self.dSpinPBox.setMaximum(10000)

        self.formLayout_2.setWidget(25, QFormLayout.FieldRole, self.dSpinPBox)

        self.resitoresAprovadosLabel = QLabel(self.tab)
        self.resitoresAprovadosLabel.setObjectName(u"resitoresAprovadosLabel")

        self.formLayout_2.setWidget(26, QFormLayout.LabelRole, self.resitoresAprovadosLabel)

        self.resitoresAprovadosComboBox = QComboBox(self.tab)
        self.resitoresAprovadosComboBox.setObjectName(u"resitoresAprovadosComboBox")

        self.formLayout_2.setWidget(26, QFormLayout.FieldRole, self.resitoresAprovadosComboBox)

        self.fusVeisAprovadosLabel = QLabel(self.tab)
        self.fusVeisAprovadosLabel.setObjectName(u"fusVeisAprovadosLabel")

        self.formLayout_2.setWidget(27, QFormLayout.LabelRole, self.fusVeisAprovadosLabel)

        self.fusVeisAprovadosComboBox = QComboBox(self.tab)
        self.fusVeisAprovadosComboBox.setObjectName(u"fusVeisAprovadosComboBox")

        self.formLayout_2.setWidget(27, QFormLayout.FieldRole, self.fusVeisAprovadosComboBox)

        self.listaTecnicapushButton = QPushButton(self.tab)
        self.listaTecnicapushButton.setObjectName(u"listaTecnicapushButton")
        font2 = QFont()
        font2.setPointSize(12)
        self.listaTecnicapushButton.setFont(font2)
        self.listaTecnicapushButton.setStyleSheet(u"background-color: rgb(255, 170, 0);")

        self.formLayout_2.setWidget(28, QFormLayout.FieldRole, self.listaTecnicapushButton)

        self.label_39 = QLabel(self.tab)
        self.label_39.setObjectName(u"label_39")

        self.formLayout_2.setWidget(21, QFormLayout.LabelRole, self.label_39)

        self.label_71 = QLabel(self.tab)
        self.label_71.setObjectName(u"label_71")

        self.formLayout_2.setWidget(22, QFormLayout.LabelRole, self.label_71)

        self.cb_PlacaLateral = QComboBox(self.tab)
        self.cb_PlacaLateral.setObjectName(u"cb_PlacaLateral")
        self.cb_PlacaLateral.setEditable(False)

        self.formLayout_2.setWidget(22, QFormLayout.FieldRole, self.cb_PlacaLateral)


        self.verticalLayout_6.addLayout(self.formLayout_2)

        self.tabWidgetCP.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_9 = QVBoxLayout(self.tab_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_custos = QFrame(self.tab_2)
        self.frame_custos.setObjectName(u"frame_custos")
        self.frame_custos.setFrameShape(QFrame.NoFrame)
        self.frame_custos.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_custos)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_8 = QFrame(self.frame_custos)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_8)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_28 = QLabel(self.frame_8)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_10.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_8)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_10.addWidget(self.label_29)

        self.label_36 = QLabel(self.frame_8)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_10.addWidget(self.label_36)

        self.label_47 = QLabel(self.frame_8)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_10.addWidget(self.label_47)

        self.label_48 = QLabel(self.frame_8)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_10.addWidget(self.label_48)


        self.horizontalLayout_6.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_custos)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_9)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_50 = QLabel(self.frame_9)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_50)

        self.lb_pTSec = QLabel(self.frame_9)
        self.lb_pTSec.setObjectName(u"lb_pTSec")
        self.lb_pTSec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.lb_pTSec)

        self.lb_pTlUn = QLabel(self.frame_9)
        self.lb_pTlUn.setObjectName(u"lb_pTlUn")
        self.lb_pTlUn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.lb_pTlUn)

        self.lb_ctSec = QLabel(self.frame_9)
        self.lb_ctSec.setObjectName(u"lb_ctSec")
        self.lb_ctSec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.lb_ctSec)

        self.lb_ctUn = QLabel(self.frame_9)
        self.lb_ctUn.setObjectName(u"lb_ctUn")
        self.lb_ctUn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.lb_ctUn)


        self.horizontalLayout_6.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_custos)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_10)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_57 = QLabel(self.frame_10)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_57)

        self.lb_pPapSec = QLabel(self.frame_10)
        self.lb_pPapSec.setObjectName(u"lb_pPapSec")
        self.lb_pPapSec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.lb_pPapSec)

        self.lb_pPapUn = QLabel(self.frame_10)
        self.lb_pPapUn.setObjectName(u"lb_pPapUn")
        self.lb_pPapUn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.lb_pPapUn)

        self.lb_cPapSec = QLabel(self.frame_10)
        self.lb_cPapSec.setObjectName(u"lb_cPapSec")
        self.lb_cPapSec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.lb_cPapSec)

        self.lb_cPapUn = QLabel(self.frame_10)
        self.lb_cPapUn.setObjectName(u"lb_cPapUn")
        self.lb_cPapUn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_12.addWidget(self.lb_cPapUn)


        self.horizontalLayout_6.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame_custos)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_63 = QLabel(self.frame_11)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_63)

        self.lb_pFilSec = QLabel(self.frame_11)
        self.lb_pFilSec.setObjectName(u"lb_pFilSec")
        self.lb_pFilSec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.lb_pFilSec)

        self.lb_pFilUn = QLabel(self.frame_11)
        self.lb_pFilUn.setObjectName(u"lb_pFilUn")
        self.lb_pFilUn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.lb_pFilUn)

        self.lb_cFilSec = QLabel(self.frame_11)
        self.lb_cFilSec.setObjectName(u"lb_cFilSec")
        self.lb_cFilSec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.lb_cFilSec)

        self.lb_cFilUn = QLabel(self.frame_11)
        self.lb_cFilUn.setObjectName(u"lb_cFilUn")
        self.lb_cFilUn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_13.addWidget(self.lb_cFilUn)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.frame_12 = QFrame(self.frame_custos)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_68 = QLabel(self.frame_12)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_68)

        self.lb_pFoSec = QLabel(self.frame_12)
        self.lb_pFoSec.setObjectName(u"lb_pFoSec")
        self.lb_pFoSec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.lb_pFoSec)

        self.lb_pFoUn = QLabel(self.frame_12)
        self.lb_pFoUn.setObjectName(u"lb_pFoUn")
        self.lb_pFoUn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.lb_pFoUn)

        self.lb_cFoSec = QLabel(self.frame_12)
        self.lb_cFoSec.setObjectName(u"lb_cFoSec")
        self.lb_cFoSec.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.lb_cFoSec)

        self.lb_cFoUn = QLabel(self.frame_12)
        self.lb_cFoUn.setObjectName(u"lb_cFoUn")
        self.lb_cFoUn.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_14.addWidget(self.lb_cFoUn)


        self.horizontalLayout_6.addWidget(self.frame_12)


        self.verticalLayout_9.addWidget(self.frame_custos)

        self.tabWidgetCP.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.horizontalLayout_7 = QHBoxLayout(self.tab_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_14 = QFrame(self.tab_3)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.tableView = QTableView(self.frame_14)
        self.tableView.setObjectName(u"tableView")

        self.horizontalLayout_8.addWidget(self.tableView)


        self.horizontalLayout_7.addWidget(self.frame_14)

        self.tabWidgetCP.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_2 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableView_Resistor = QTableView(self.tab_5)
        self.tableView_Resistor.setObjectName(u"tableView_Resistor")

        self.horizontalLayout_2.addWidget(self.tableView_Resistor)

        self.tabWidgetCP.addTab(self.tab_5, "")
        self.tab_fusein = QWidget()
        self.tab_fusein.setObjectName(u"tab_fusein")
        self.tab_fusein.setEnabled(True)
        self.horizontalLayout_4 = QHBoxLayout(self.tab_fusein)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tableView_fusein = QTableView(self.tab_fusein)
        self.tableView_fusein.setObjectName(u"tableView_fusein")

        self.horizontalLayout_4.addWidget(self.tableView_fusein)

        self.tabWidgetCP.addTab(self.tab_fusein, "")
        self.tab_lt = QWidget()
        self.tab_lt.setObjectName(u"tab_lt")
        self.horizontalLayout_5 = QHBoxLayout(self.tab_lt)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.tableView_bom = QTableView(self.tab_lt)
        self.tableView_bom.setObjectName(u"tableView_bom")

        self.horizontalLayout_5.addWidget(self.tableView_bom)

        self.tabWidgetCP.addTab(self.tab_lt, "")

        self.verticalLayout_3.addWidget(self.tabWidgetCP)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.frame_btn = QFrame(win_CpEn)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setFrameShape(QFrame.NoFrame)
        self.frame_btn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.bt_calc = QPushButton(self.frame_btn)
        self.bt_calc.setObjectName(u"bt_calc")
        self.bt_calc.setFont(font2)
        self.bt_calc.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.horizontalLayout_3.addWidget(self.bt_calc)

        self.bt_close = QPushButton(self.frame_btn)
        self.bt_close.setObjectName(u"bt_close")
        self.bt_close.setFont(font2)
        self.bt_close.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout_3.addWidget(self.bt_close)


        self.verticalLayout_4.addWidget(self.frame_btn)

        QWidget.setTabOrder(self.cb_modelo, self.spN_Buchas)
        QWidget.setTabOrder(self.spN_Buchas, self.cb_NBI)
        QWidget.setTabOrder(self.cb_NBI, self.cb_Eixos)
        QWidget.setTabOrder(self.cb_Eixos, self.ed_Vn)
        QWidget.setTabOrder(self.ed_Vn, self.ed_Fr)
        QWidget.setTabOrder(self.ed_Fr, self.ed_KVAR)
        QWidget.setTabOrder(self.ed_KVAR, self.Ed_Ncoil)
        QWidget.setTabOrder(self.Ed_Ncoil, self.ed_Vcoil)
        QWidget.setTabOrder(self.ed_Vcoil, self.Ed_MilsPaper)
        QWidget.setTabOrder(self.Ed_MilsPaper, self.spinBoxNumFilmes)
        QWidget.setTabOrder(self.spinBoxNumFilmes, self.cb_filme1)
        QWidget.setTabOrder(self.cb_filme1, self.cb_filme2)
        QWidget.setTabOrder(self.cb_filme2, self.cb_filme3)
        QWidget.setTabOrder(self.cb_filme3, self.ed_milsFilm)
        QWidget.setTabOrder(self.ed_milsFilm, self.ed_gauge_Al)
        QWidget.setTabOrder(self.ed_gauge_Al, self.dSPCalco)
        QWidget.setTabOrder(self.dSPCalco, self.ed_Hcoil)
        QWidget.setTabOrder(self.ed_Hcoil, self.dSpinFolga)
        QWidget.setTabOrder(self.dSpinFolga, self.ed_lamelas_foil)
        QWidget.setTabOrder(self.ed_lamelas_foil, self.ed_larg_foil)
        QWidget.setTabOrder(self.ed_larg_foil, self.ed_tol)
        QWidget.setTabOrder(self.ed_tol, self.ed_FatorEsp)
        QWidget.setTabOrder(self.ed_FatorEsp, self.ed_sobre_voltas)
        QWidget.setTabOrder(self.ed_sobre_voltas, self.ed_fator_coil)
        QWidget.setTabOrder(self.ed_fator_coil, self.cb_Conexao)
        QWidget.setTabOrder(self.cb_Conexao, self.ed_Watts)
        QWidget.setTabOrder(self.ed_Watts, self.ed_Tempo)
        QWidget.setTabOrder(self.ed_Tempo, self.ed_Vend)
        QWidget.setTabOrder(self.ed_Vend, self.ed_file_name)
        QWidget.setTabOrder(self.ed_file_name, self.bt_close)
        QWidget.setTabOrder(self.bt_close, self.ed_largFoil)
        QWidget.setTabOrder(self.ed_largFoil, self.ed_largDie)
        QWidget.setTabOrder(self.ed_largDie, self.ed_Refugo)
        QWidget.setTabOrder(self.ed_Refugo, self.lb_fatorEsp)
        QWidget.setTabOrder(self.lb_fatorEsp, self.lb_compFoil)
        QWidget.setTabOrder(self.lb_compFoil, self.lb_fat_Bob)
        QWidget.setTabOrder(self.lb_fat_Bob, self.lb_voltasFoil)
        QWidget.setTabOrder(self.lb_voltasFoil, self.lb_sobreVoltas)
        QWidget.setTabOrder(self.lb_sobreVoltas, self.ck_eixo)
        QWidget.setTabOrder(self.ck_eixo, self.lb_epBob)
        QWidget.setTabOrder(self.lb_epBob, self.lb_cUn)
        QWidget.setTabOrder(self.lb_cUn, self.lb_cCoil)
        QWidget.setTabOrder(self.lb_cCoil, self.lb_larg)
        QWidget.setTabOrder(self.lb_larg, self.lbdsMan)
        QWidget.setTabOrder(self.lbdsMan, self.lb_vCoil)
        QWidget.setTabOrder(self.lb_vCoil, self.spin_Stress)
        QWidget.setTabOrder(self.spin_Stress, self.lb_pfPrin)
        QWidget.setTabOrder(self.lb_pfPrin, self.lb_95PF)
        QWidget.setTabOrder(self.lb_95PF, self.lb_pFoil)
        QWidget.setTabOrder(self.lb_pFoil, self.spin_stressVPM)
        QWidget.setTabOrder(self.spin_stressVPM, self.spinBoxGS)
        QWidget.setTabOrder(self.spinBoxGS, self.spinBoxGP)
        QWidget.setTabOrder(self.spinBoxGP, self.spinBoxGSGP)
        QWidget.setTabOrder(self.spinBoxGSGP, self.inputCodLateral)
        QWidget.setTabOrder(self.inputCodLateral, self.lb_tCoils)
        QWidget.setTabOrder(self.lb_tCoils, self.ed_custoFilm)
        QWidget.setTabOrder(self.ed_custoFilm, self.scrollArea)
        QWidget.setTabOrder(self.scrollArea, self.cb_mandris)
        QWidget.setTabOrder(self.cb_mandris, self.tableView)
        QWidget.setTabOrder(self.tableView, self.ed_custoFoil)
        QWidget.setTabOrder(self.ed_custoFoil, self.ed_PapelBK)
        QWidget.setTabOrder(self.ed_PapelBK, self.ed_FilmeDK)
        QWidget.setTabOrder(self.ed_FilmeDK, self.ed_OleoDK)
        QWidget.setTabOrder(self.ed_OleoDK, self.ed_custoPaper)
        QWidget.setTabOrder(self.ed_custoPaper, self.ed_codFilm1)
        QWidget.setTabOrder(self.ed_codFilm1, self.ed_codFilm2)
        QWidget.setTabOrder(self.ed_codFilm2, self.ed_codFilm3)
        QWidget.setTabOrder(self.ed_codFilm3, self.resitoresAprovadosComboBox)
        QWidget.setTabOrder(self.resitoresAprovadosComboBox, self.fusVeisAprovadosComboBox)
        QWidget.setTabOrder(self.fusVeisAprovadosComboBox, self.listaTecnicapushButton)
        QWidget.setTabOrder(self.listaTecnicapushButton, self.tableView_Resistor)
        QWidget.setTabOrder(self.tableView_Resistor, self.tableView_fusein)
        QWidget.setTabOrder(self.tableView_fusein, self.inputDescr)
        QWidget.setTabOrder(self.inputDescr, self.tabWidgetCP)
        QWidget.setTabOrder(self.tabWidgetCP, self.ed_rhoPaper)
        QWidget.setTabOrder(self.ed_rhoPaper, self.checkBoxAutoNCoils)
        QWidget.setTabOrder(self.checkBoxAutoNCoils, self.codSecCapacitivaLineEdit)
        QWidget.setTabOrder(self.codSecCapacitivaLineEdit, self.comboBoxCaixas)
        QWidget.setTabOrder(self.comboBoxCaixas, self.dSpinHBox)
        QWidget.setTabOrder(self.dSpinHBox, self.dSpinPBox)
        QWidget.setTabOrder(self.dSpinPBox, self.cb_PlacaLateral)
        QWidget.setTabOrder(self.cb_PlacaLateral, self.tableView_bom)
        QWidget.setTabOrder(self.tableView_bom, self.bt_calc)

        self.retranslateUi(win_CpEn)
        self.bt_close.clicked.connect(win_CpEn.close)

        self.tabWidgetCP.setCurrentIndex(0)
        self.cb_modelo.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(win_CpEn)
    # setupUi

    def retranslateUi(self, win_CpEn):
        win_CpEn.setWindowTitle(QCoreApplication.translate("win_CpEn", u"Capacitor de Pot\u00eancia", None))
        self.label_19.setText(QCoreApplication.translate("win_CpEn", u"Capacitor de Pot\u00eancia", None))
        self.label_41.setText(QCoreApplication.translate("win_CpEn", u"Modelo", None))
        self.label_35.setText(QCoreApplication.translate("win_CpEn", u"N\u00famero de buchas", None))
        self.label_51.setText(QCoreApplication.translate("win_CpEn", u"NBI (kV)", None))
        self.label_20.setText(QCoreApplication.translate("win_CpEn", u"Eixos", None))
        self.label_4.setText(QCoreApplication.translate("win_CpEn", u"Tens\u00e3o (V)", None))
        self.label_5.setText(QCoreApplication.translate("win_CpEn", u"Frequ\u00eancia (Hz)", None))
        self.label_6.setText(QCoreApplication.translate("win_CpEn", u"Pot\u00eancia Reativa (KVAr)", None))
        self.label_7.setText(QCoreApplication.translate("win_CpEn", u"N\u00famero de bobinas", None))
        self.label_vCoil.setText(QCoreApplication.translate("win_CpEn", u"Volts/Bobina", None))
        self.label_paper.setText(QCoreApplication.translate("win_CpEn", u"MILS Paper", None))
        self.label_49.setText(QCoreApplication.translate("win_CpEn", u"# Filmes", None))
        self.label_52.setText(QCoreApplication.translate("win_CpEn", u"Espessura filme 1", None))
        self.label_filme2.setText(QCoreApplication.translate("win_CpEn", u"Espessura filme 2", None))
        self.label_filme3.setText(QCoreApplication.translate("win_CpEn", u"Espessura filme 3", None))
        self.label_10.setText(QCoreApplication.translate("win_CpEn", u"MILS Filme", None))
        self.label_11.setText(QCoreApplication.translate("win_CpEn", u"Gauge Alum\u00ednio", None))
        self.label_34.setText(QCoreApplication.translate("win_CpEn", u"Altura dos cal\u00e7os (mm) 2 x ", None))
        self.label_12.setText(QCoreApplication.translate("win_CpEn", u"Altura total bobinas (in)", None))
        self.label_38.setText(QCoreApplication.translate("win_CpEn", u"Folga da caixa (mm)", None))
        self.label_13.setText(QCoreApplication.translate("win_CpEn", u"Lamelas / Foil", None))
        self.label_14.setText(QCoreApplication.translate("win_CpEn", u"Largura Ativa do Foil", None))
        self.label_15.setText(QCoreApplication.translate("win_CpEn", u"Toler\u00e2ncia do Capacitor", None))
        self.label_16.setText(QCoreApplication.translate("win_CpEn", u"Fator de espa\u00e7o", None))
        self.label_17.setText(QCoreApplication.translate("win_CpEn", u"Sobre Voltas", None))
        self.label_18.setText(QCoreApplication.translate("win_CpEn", u"Fator de espa\u00e7o Bobinas", None))
        self.label_43.setText(QCoreApplication.translate("win_CpEn", u"Conex\u00e3o dos resitores", None))
        self.label_44.setText(QCoreApplication.translate("win_CpEn", u"M\u00e1ximo Watts por resitor", None))
        self.label_45.setText(QCoreApplication.translate("win_CpEn", u"Tempo de descarga", None))
        self.label_46.setText(QCoreApplication.translate("win_CpEn", u"Tens\u00e3o final", None))
        self.label_32.setText(QCoreApplication.translate("win_CpEn", u"Nome do arquivo de resultado", None))
        self.cb_modelo.setItemText(0, QCoreApplication.translate("win_CpEn", u"FI - 1 elo", None))
        self.cb_modelo.setItemText(1, QCoreApplication.translate("win_CpEn", u"FI - 2 elos", None))
        self.cb_modelo.setItemText(2, QCoreApplication.translate("win_CpEn", u"MI", None))
        self.cb_modelo.setItemText(3, QCoreApplication.translate("win_CpEn", u"MH", None))
        self.cb_modelo.setItemText(4, QCoreApplication.translate("win_CpEn", u"MF", None))
        self.cb_modelo.setItemText(5, QCoreApplication.translate("win_CpEn", u"ME", None))
        self.cb_modelo.setItemText(6, QCoreApplication.translate("win_CpEn", u"MG", None))
        self.cb_modelo.setItemText(7, QCoreApplication.translate("win_CpEn", u"ST", None))
        self.cb_modelo.setItemText(8, QCoreApplication.translate("win_CpEn", u"TR", None))
        self.cb_modelo.setItemText(9, QCoreApplication.translate("win_CpEn", u"VDC", None))

        self.cb_NBI.setItemText(0, QCoreApplication.translate("win_CpEn", u"60", None))
        self.cb_NBI.setItemText(1, QCoreApplication.translate("win_CpEn", u"110", None))
        self.cb_NBI.setItemText(2, QCoreApplication.translate("win_CpEn", u"125", None))
        self.cb_NBI.setItemText(3, QCoreApplication.translate("win_CpEn", u"150", None))
        self.cb_NBI.setItemText(4, QCoreApplication.translate("win_CpEn", u"170", None))
        self.cb_NBI.setItemText(5, QCoreApplication.translate("win_CpEn", u"200", None))

        self.cb_Eixos.setItemText(0, QCoreApplication.translate("win_CpEn", u"Americanos", None))
        self.cb_Eixos.setItemText(1, QCoreApplication.translate("win_CpEn", u"Brasileiros", None))

        self.cb_Eixos.setPlaceholderText("")
        self.ed_Vn.setText(QCoreApplication.translate("win_CpEn", u"7960.00", None))
        self.ed_Vn.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"Tens\u00e3o (V)", None))
        self.ed_Fr.setText(QCoreApplication.translate("win_CpEn", u"60.0", None))
        self.ed_Fr.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"Frequ\u00eancia (HZ)", None))
        self.ed_KVAR.setText(QCoreApplication.translate("win_CpEn", u"200.0", None))
        self.ed_KVAR.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"Pot\u00eancia Reativa (kVAr)", None))
        self.Ed_Ncoil.setText(QCoreApplication.translate("win_CpEn", u"1", None))
        self.Ed_Ncoil.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"N\u00famero de bobinas", None))
        self.Ed_MilsPaper.setText(QCoreApplication.translate("win_CpEn", u"0.00", None))
        self.Ed_MilsPaper.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"MILS Paper", None))
        self.ed_milsFilm.setText(QCoreApplication.translate("win_CpEn", u"1.15", None))
        self.ed_milsFilm.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"MILS Filme", None))
        self.ed_gauge_Al.setText(QCoreApplication.translate("win_CpEn", u"0.00020", None))
        self.ed_gauge_Al.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"Gauge Alum\u00ednio", None))
        self.ed_Hcoil.setText(QCoreApplication.translate("win_CpEn", u"12.75", None))
        self.ed_Hcoil.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"Altura da bobina (mm)", None))
        self.ed_lamelas_foil.setText(QCoreApplication.translate("win_CpEn", u"0", None))
        self.ed_lamelas_foil.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"Lamelas / Foil", None))
        self.ed_larg_foil.setText(QCoreApplication.translate("win_CpEn", u"11.5748", None))
        self.ed_larg_foil.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"Largura Ativa do Foil", None))
        self.ed_tol.setText(QCoreApplication.translate("win_CpEn", u"1.00", None))
        self.ed_tol.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"Toler\u00e2cia do Capacitor", None))
        self.ed_FatorEsp.setText(QCoreApplication.translate("win_CpEn", u"1.29", None))
        self.ed_FatorEsp.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"Sobre Voltas", None))
        self.ed_sobre_voltas.setText(QCoreApplication.translate("win_CpEn", u"1.25", None))
        self.ed_sobre_voltas.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"Fator de espa\u00e7o", None))
        self.ed_fator_coil.setText(QCoreApplication.translate("win_CpEn", u"1.22", None))
        self.ed_fator_coil.setPlaceholderText(QCoreApplication.translate("win_CpEn", u"Fator de espa\u00e7p Bobinas", None))
        self.cb_Conexao.setItemText(0, QCoreApplication.translate("win_CpEn", u"S\u00e9rie", None))
        self.cb_Conexao.setItemText(1, QCoreApplication.translate("win_CpEn", u"S\u00e9rie/Paralelo", None))

        self.ed_Watts.setText(QCoreApplication.translate("win_CpEn", u"3", None))
        self.ed_Tempo.setText(QCoreApplication.translate("win_CpEn", u"300", None))
        self.ed_Vend.setText(QCoreApplication.translate("win_CpEn", u"50", None))
        self.ed_file_name.setText(QCoreApplication.translate("win_CpEn", u"Resultados CP", None))
        self.ck_eixo.setText(QCoreApplication.translate("win_CpEn", u"Eixos", None))
        self.label_37.setText(QCoreApplication.translate("win_CpEn", u"C\u00f3digo da placa lateral", None))
        self.labelDescr.setText(QCoreApplication.translate("win_CpEn", u"Descri\u00e7\u00e3o", None))
        self.label_40.setText(QCoreApplication.translate("win_CpEn", u"Codigo filme 1", None))
        self.label_42.setText(QCoreApplication.translate("win_CpEn", u"Codigo filme 2", None))
        self.label_CodFilm3.setText(QCoreApplication.translate("win_CpEn", u"Codigo filme 3", None))
        self.checkBoxAutoNCoils.setText(QCoreApplication.translate("win_CpEn", u"Auto  # Bobinas", None))
        self.tabWidgetCP.setTabText(self.tabWidgetCP.indexOf(self.tabInput), QCoreApplication.translate("win_CpEn", u"Entrada geral", None))
        self.label_9.setText(QCoreApplication.translate("win_CpEn", u"Papel DK", None))
        self.label_53.setText(QCoreApplication.translate("win_CpEn", u"Filme DK", None))
        self.label_54.setText(QCoreApplication.translate("win_CpEn", u"\u00d3leo DK", None))
        self.label_55.setText(QCoreApplication.translate("win_CpEn", u"'Densidade do papel", None))
        self.label_56.setText(QCoreApplication.translate("win_CpEn", u"Papel (US$/kg)", None))
        self.label_58.setText(QCoreApplication.translate("win_CpEn", u"Filme (US$/kg)", None))
        self.label_59.setText(QCoreApplication.translate("win_CpEn", u"Foil (US$/kg)", None))
        self.label_60.setText(QCoreApplication.translate("win_CpEn", u"Largura do Foil Padr\u00e3o", None))
        self.label_61.setText(QCoreApplication.translate("win_CpEn", u"Largura do diel\u00e9trico", None))
        self.label_62.setText(QCoreApplication.translate("win_CpEn", u"Refugo (%)", None))
        self.ed_PapelBK.setText(QCoreApplication.translate("win_CpEn", u"4.3", None))
        self.ed_FilmeDK.setText(QCoreApplication.translate("win_CpEn", u"2.34", None))
        self.ed_OleoDK.setText(QCoreApplication.translate("win_CpEn", u"2.55", None))
        self.ed_rhoPaper.setText(QCoreApplication.translate("win_CpEn", u"1", None))
        self.ed_custoPaper.setText(QCoreApplication.translate("win_CpEn", u"1", None))
        self.ed_custoFilm.setText(QCoreApplication.translate("win_CpEn", u"4.7", None))
        self.ed_custoFoil.setText(QCoreApplication.translate("win_CpEn", u"6.1", None))
        self.ed_largFoil.setText(QCoreApplication.translate("win_CpEn", u"12.52", None))
        self.ed_largDie.setText(QCoreApplication.translate("win_CpEn", u"12.68", None))
        self.ed_Refugo.setText(QCoreApplication.translate("win_CpEn", u"3", None))
        self.tabWidgetCP.setTabText(self.tabWidgetCP.indexOf(self.tab_4), QCoreApplication.translate("win_CpEn", u"Materiais", None))
        self.label.setText(QCoreApplication.translate("win_CpEn", u"Fator de espa\u00e7o", None))
        self.label_2.setText(QCoreApplication.translate("win_CpEn", u"Comprimento Foil (m)", None))
        self.label_3.setText(QCoreApplication.translate("win_CpEn", u"Fator de espa\u00e7amento bobinagem", None))
        self.label_21.setText(QCoreApplication.translate("win_CpEn", u"Voltas Foil", None))
        self.label_22.setText(QCoreApplication.translate("win_CpEn", u"Sobre voltas", None))
        self.label_23.setText(QCoreApplication.translate("win_CpEn", u"Total de bobinas", None))
        self.label_24.setText(QCoreApplication.translate("win_CpEn", u"Espessura bobina (mm)", None))
        self.label_25.setText(QCoreApplication.translate("win_CpEn", u"Capacit\u00e2ncia / unidade (\u03bcF)", None))
        self.label_26.setText(QCoreApplication.translate("win_CpEn", u"Capacit\u00e2ncia / bobina (\u03bcF)", None))
        self.label_27.setText(QCoreApplication.translate("win_CpEn", u"Largura (mm)", None))
        self.label_64.setText(QCoreApplication.translate("win_CpEn", u"Di\u00e2mentro externo do mandril (in)", None))
        self.label_65.setText(QCoreApplication.translate("win_CpEn", u"Volts/Bobina (V)", None))
        self.label_30.setText(QCoreApplication.translate("win_CpEn", u"Stress (VPM)", None))
        self.label_66.setText(QCoreApplication.translate("win_CpEn", u"Stress (kV/mm)", None))
        self.label_67.setText(QCoreApplication.translate("win_CpEn", u"P. F. Principal", None))
        self.label_69.setText(QCoreApplication.translate("win_CpEn", u"95% P. F.", None))
        self.label_70.setText(QCoreApplication.translate("win_CpEn", u"Perdas Foil", None))
        self.label_8.setText(QCoreApplication.translate("win_CpEn", u"Grupos s\u00e9rie", None))
        self.label_31.setText(QCoreApplication.translate("win_CpEn", u"Grupos paralelo", None))
        self.label_33.setText(QCoreApplication.translate("win_CpEn", u"Numero de bobinas GS*GP", None))
        self.label_73.setText(QCoreApplication.translate("win_CpEn", u"Caixas cadastradas Largura x Altura", None))
        self.label_74.setText(QCoreApplication.translate("win_CpEn", u"Altura da caixa (mm)", None))
        self.label_75.setText(QCoreApplication.translate("win_CpEn", u"Largura da caixa (mm)", None))
        self.resitoresAprovadosLabel.setText(QCoreApplication.translate("win_CpEn", u"Resistores aprovados", None))
        self.fusVeisAprovadosLabel.setText(QCoreApplication.translate("win_CpEn", u"Fus\u00edveis aprovados", None))
        self.listaTecnicapushButton.setText(QCoreApplication.translate("win_CpEn", u"Gerar lista t\u00e9cnica", None))
        self.label_39.setText(QCoreApplication.translate("win_CpEn", u"C\u00f3digo da se\u00e7\u00e3o capacitiva", None))
        self.label_71.setText(QCoreApplication.translate("win_CpEn", u"Placa lateral Largura x Altura", None))
        self.tabWidgetCP.setTabText(self.tabWidgetCP.indexOf(self.tab), QCoreApplication.translate("win_CpEn", u"Resultados", None))
        self.label_28.setText("")
        self.label_29.setText(QCoreApplication.translate("win_CpEn", u"Peso/Se\u00e7\u00e3o", None))
        self.label_36.setText(QCoreApplication.translate("win_CpEn", u"Peso/Unidade", None))
        self.label_47.setText(QCoreApplication.translate("win_CpEn", u"Custo/Se\u00e7\u00e3o", None))
        self.label_48.setText(QCoreApplication.translate("win_CpEn", u"Custo/Unidade", None))
        self.label_50.setText(QCoreApplication.translate("win_CpEn", u"Total", None))
        self.lb_pTSec.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.lb_pTlUn.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.lb_ctSec.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.lb_ctUn.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.label_57.setText(QCoreApplication.translate("win_CpEn", u"Papel", None))
        self.lb_pPapSec.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.lb_pPapUn.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.lb_cPapSec.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.lb_cPapUn.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.label_63.setText(QCoreApplication.translate("win_CpEn", u"Filme", None))
        self.lb_pFilSec.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.lb_pFilUn.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.lb_cFilSec.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.lb_cFilUn.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.label_68.setText(QCoreApplication.translate("win_CpEn", u"Foil", None))
        self.lb_pFoSec.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.lb_pFoUn.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.lb_cFoSec.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.lb_cFoUn.setText(QCoreApplication.translate("win_CpEn", u"TextLabel", None))
        self.tabWidgetCP.setTabText(self.tabWidgetCP.indexOf(self.tab_2), QCoreApplication.translate("win_CpEn", u"Material/Custos", None))
#if QT_CONFIG(accessibility)
        self.tab_3.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.tabWidgetCP.setTabText(self.tabWidgetCP.indexOf(self.tab_3), QCoreApplication.translate("win_CpEn", u"Capacitor", None))
        self.tabWidgetCP.setTabText(self.tabWidgetCP.indexOf(self.tab_5), QCoreApplication.translate("win_CpEn", u"Resistor", None))
        self.tabWidgetCP.setTabText(self.tabWidgetCP.indexOf(self.tab_fusein), QCoreApplication.translate("win_CpEn", u"Fus\u00edvel interno", None))
        self.tabWidgetCP.setTabText(self.tabWidgetCP.indexOf(self.tab_lt), QCoreApplication.translate("win_CpEn", u"Lista t\u00e9cnica", None))
        self.bt_calc.setText(QCoreApplication.translate("win_CpEn", u"Calcular...", None))
        self.bt_close.setText(QCoreApplication.translate("win_CpEn", u"Voltar...", None))
    # retranslateUi

