# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reator_aberto_modulo_hibrido4.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogHibrido(object):
    def setupUi(self, DialogHibrido):
        if not DialogHibrido.objectName():
            DialogHibrido.setObjectName(u"DialogHibrido")
        DialogHibrido.resize(1089, 860)
        self.verticalLayout = QVBoxLayout(DialogHibrido)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogHibrido)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout_7 = QFormLayout()
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setSizeConstraint(QLayout.SetMaximumSize)
        self.formLayout_7.setContentsMargins(5, 5, 5, 5)
        self.label_52 = QLabel(self.frame)
        self.label_52.setObjectName(u"label_52")

        self.formLayout_7.setWidget(0, QFormLayout.LabelRole, self.label_52)

        self.cbMaterialTap = QComboBox(self.frame)
        self.cbMaterialTap.addItem("")
        self.cbMaterialTap.addItem("")
        self.cbMaterialTap.addItem("")
        self.cbMaterialTap.addItem("")
        self.cbMaterialTap.addItem("")
        self.cbMaterialTap.setObjectName(u"cbMaterialTap")
        self.cbMaterialTap.setEditable(True)

        self.formLayout_7.setWidget(0, QFormLayout.FieldRole, self.cbMaterialTap)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_7.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.inputLn = QDoubleSpinBox(self.frame)
        self.inputLn.setObjectName(u"inputLn")
        self.inputLn.setEnabled(False)
        self.inputLn.setDecimals(3)
        self.inputLn.setMaximum(10000.000000000000000)

        self.formLayout_7.setWidget(1, QFormLayout.FieldRole, self.inputLn)

        self.label_53 = QLabel(self.frame)
        self.label_53.setObjectName(u"label_53")

        self.formLayout_7.setWidget(2, QFormLayout.LabelRole, self.label_53)

        self.inputL1 = QDoubleSpinBox(self.frame)
        self.inputL1.setObjectName(u"inputL1")
        self.inputL1.setEnabled(False)
        self.inputL1.setDecimals(3)

        self.formLayout_7.setWidget(2, QFormLayout.FieldRole, self.inputL1)

        self.label_54 = QLabel(self.frame)
        self.label_54.setObjectName(u"label_54")

        self.formLayout_7.setWidget(3, QFormLayout.LabelRole, self.label_54)

        self.inputSinal = QSpinBox(self.frame)
        self.inputSinal.setObjectName(u"inputSinal")
        self.inputSinal.setMinimum(-1)
        self.inputSinal.setMaximum(1)
        self.inputSinal.setSingleStep(2)
        self.inputSinal.setValue(1)

        self.formLayout_7.setWidget(3, QFormLayout.FieldRole, self.inputSinal)

        self.label_56 = QLabel(self.frame)
        self.label_56.setObjectName(u"label_56")

        self.formLayout_7.setWidget(4, QFormLayout.LabelRole, self.label_56)

        self.inputDi = QDoubleSpinBox(self.frame)
        self.inputDi.setObjectName(u"inputDi")
        self.inputDi.setDecimals(1)
        self.inputDi.setMaximum(3000.000000000000000)
        self.inputDi.setValue(0.000000000000000)

        self.formLayout_7.setWidget(4, QFormLayout.FieldRole, self.inputDi)

        self.label_57 = QLabel(self.frame)
        self.label_57.setObjectName(u"label_57")

        self.formLayout_7.setWidget(5, QFormLayout.LabelRole, self.label_57)

        self.inputEspPerfil = QDoubleSpinBox(self.frame)
        self.inputEspPerfil.setObjectName(u"inputEspPerfil")
        self.inputEspPerfil.setDecimals(1)
        self.inputEspPerfil.setValue(13.000000000000000)

        self.formLayout_7.setWidget(5, QFormLayout.FieldRole, self.inputEspPerfil)

        self.label_58 = QLabel(self.frame)
        self.label_58.setObjectName(u"label_58")

        self.formLayout_7.setWidget(6, QFormLayout.LabelRole, self.label_58)

        self.inputLargPerf = QDoubleSpinBox(self.frame)
        self.inputLargPerf.setObjectName(u"inputLargPerf")
        self.inputLargPerf.setDecimals(1)
        self.inputLargPerf.setValue(23.000000000000000)

        self.formLayout_7.setWidget(6, QFormLayout.FieldRole, self.inputLargPerf)

        self.label_59 = QLabel(self.frame)
        self.label_59.setObjectName(u"label_59")

        self.formLayout_7.setWidget(7, QFormLayout.LabelRole, self.label_59)

        self.inputNumPerf = QSpinBox(self.frame)
        self.inputNumPerf.setObjectName(u"inputNumPerf")
        self.inputNumPerf.setValue(1)

        self.formLayout_7.setWidget(7, QFormLayout.FieldRole, self.inputNumPerf)

        self.label_61 = QLabel(self.frame)
        self.label_61.setObjectName(u"label_61")

        self.formLayout_7.setWidget(8, QFormLayout.LabelRole, self.label_61)

        self.cbPosicao = QComboBox(self.frame)
        self.cbPosicao.addItem("")
        self.cbPosicao.addItem("")
        self.cbPosicao.addItem("")
        self.cbPosicao.addItem("")
        self.cbPosicao.setObjectName(u"cbPosicao")
        self.cbPosicao.setEditable(False)

        self.formLayout_7.setWidget(8, QFormLayout.FieldRole, self.cbPosicao)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_7.setWidget(9, QFormLayout.LabelRole, self.label_5)

        self.inputCalco = QDoubleSpinBox(self.frame)
        self.inputCalco.setObjectName(u"inputCalco")
        self.inputCalco.setDecimals(3)
        self.inputCalco.setValue(5.500000000000000)

        self.formLayout_7.setWidget(9, QFormLayout.FieldRole, self.inputCalco)

        self.label_62 = QLabel(self.frame)
        self.label_62.setObjectName(u"label_62")

        self.formLayout_7.setWidget(10, QFormLayout.LabelRole, self.label_62)

        self.inputDBSb = QDoubleSpinBox(self.frame)
        self.inputDBSb.setObjectName(u"inputDBSb")
        self.inputDBSb.setDecimals(1)
        self.inputDBSb.setMaximum(1000.000000000000000)
        self.inputDBSb.setValue(10.000000000000000)

        self.formLayout_7.setWidget(10, QFormLayout.FieldRole, self.inputDBSb)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_7.setWidget(11, QFormLayout.LabelRole, self.label_3)

        self.inputTap = QDoubleSpinBox(self.frame)
        self.inputTap.setObjectName(u"inputTap")
        self.inputTap.setDecimals(1)
        self.inputTap.setMinimum(-100.000000000000000)
        self.inputTap.setMaximum(100.000000000000000)
        self.inputTap.setValue(5.000000000000000)

        self.formLayout_7.setWidget(11, QFormLayout.FieldRole, self.inputTap)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        self.bt_DelTap = QPushButton(self.frame)
        self.bt_DelTap.setObjectName(u"bt_DelTap")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_DelTap.sizePolicy().hasHeightForWidth())
        self.bt_DelTap.setSizePolicy(sizePolicy)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.bt_DelTap)

        self.bt_AddTap = QPushButton(self.frame)
        self.bt_AddTap.setObjectName(u"bt_AddTap")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.bt_AddTap.sizePolicy().hasHeightForWidth())
        self.bt_AddTap.setSizePolicy(sizePolicy1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.bt_AddTap)


        self.formLayout_7.setLayout(12, QFormLayout.FieldRole, self.formLayout)


        self.horizontalLayout.addLayout(self.formLayout_7)

        self.formLayout_8 = QFormLayout()
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setSizeConstraint(QLayout.SetMaximumSize)
        self.label_67 = QLabel(self.frame)
        self.label_67.setObjectName(u"label_67")

        self.formLayout_8.setWidget(7, QFormLayout.LabelRole, self.label_67)

        self.inputForca = QDoubleSpinBox(self.frame)
        self.inputForca.setObjectName(u"inputForca")
        self.inputForca.setReadOnly(True)
        self.inputForca.setDecimals(1)
        self.inputForca.setMaximum(10000.000000000000000)

        self.formLayout_8.setWidget(7, QFormLayout.FieldRole, self.inputForca)

        self.label_66 = QLabel(self.frame)
        self.label_66.setObjectName(u"label_66")

        self.formLayout_8.setWidget(4, QFormLayout.LabelRole, self.label_66)

        self.inputLcalc = QDoubleSpinBox(self.frame)
        self.inputLcalc.setObjectName(u"inputLcalc")
        self.inputLcalc.setReadOnly(True)
        self.inputLcalc.setDecimals(3)
        self.inputLcalc.setMaximum(1000.000000000000000)

        self.formLayout_8.setWidget(4, QFormLayout.FieldRole, self.inputLcalc)

        self.label_68 = QLabel(self.frame)
        self.label_68.setObjectName(u"label_68")

        self.formLayout_8.setWidget(3, QFormLayout.LabelRole, self.label_68)

        self.inputLtap = QDoubleSpinBox(self.frame)
        self.inputLtap.setObjectName(u"inputLtap")

        self.formLayout_8.setWidget(3, QFormLayout.FieldRole, self.inputLtap)

        self.label_65 = QLabel(self.frame)
        self.label_65.setObjectName(u"label_65")

        self.formLayout_8.setWidget(2, QFormLayout.LabelRole, self.label_65)

        self.inputMutua = QDoubleSpinBox(self.frame)
        self.inputMutua.setObjectName(u"inputMutua")
        self.inputMutua.setReadOnly(True)
        self.inputMutua.setDecimals(3)

        self.formLayout_8.setWidget(2, QFormLayout.FieldRole, self.inputMutua)

        self.label_64 = QLabel(self.frame)
        self.label_64.setObjectName(u"label_64")

        self.formLayout_8.setWidget(1, QFormLayout.LabelRole, self.label_64)

        self.inputHe = QDoubleSpinBox(self.frame)
        self.inputHe.setObjectName(u"inputHe")
        self.inputHe.setReadOnly(True)
        self.inputHe.setDecimals(1)
        self.inputHe.setMaximum(10000.000000000000000)

        self.formLayout_8.setWidget(1, QFormLayout.FieldRole, self.inputHe)

        self.label_63 = QLabel(self.frame)
        self.label_63.setObjectName(u"label_63")

        self.formLayout_8.setWidget(0, QFormLayout.LabelRole, self.label_63)

        self.inputNesp = QDoubleSpinBox(self.frame)
        self.inputNesp.setObjectName(u"inputNesp")
        self.inputNesp.setDecimals(4)
        self.inputNesp.setMaximum(1000.000000000000000)
        self.inputNesp.setValue(10.000000000000000)

        self.formLayout_8.setWidget(0, QFormLayout.FieldRole, self.inputNesp)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout_8.setWidget(5, QFormLayout.LabelRole, self.label)

        self.InputTmed = QDoubleSpinBox(self.frame)
        self.InputTmed.setObjectName(u"InputTmed")

        self.formLayout_8.setWidget(5, QFormLayout.FieldRole, self.InputTmed)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_8.setWidget(6, QFormLayout.LabelRole, self.label_2)

        self.inputHotSpot = QDoubleSpinBox(self.frame)
        self.inputHotSpot.setObjectName(u"inputHotSpot")

        self.formLayout_8.setWidget(6, QFormLayout.FieldRole, self.inputHotSpot)

        self.ck_Tap = QCheckBox(self.frame)
        self.ck_Tap.setObjectName(u"ck_Tap")
        self.ck_Tap.setEnabled(True)
        self.ck_Tap.setCheckable(False)
        self.ck_Tap.setChecked(False)

        self.formLayout_8.setWidget(8, QFormLayout.LabelRole, self.ck_Tap)


        self.horizontalLayout.addLayout(self.formLayout_8)


        self.verticalLayout.addWidget(self.frame)

        self.tv_Taps = QTableView(DialogHibrido)
        self.tv_Taps.setObjectName(u"tv_Taps")

        self.verticalLayout.addWidget(self.tv_Taps)

        self.tv_Cil = QTableView(DialogHibrido)
        self.tv_Cil.setObjectName(u"tv_Cil")

        self.verticalLayout.addWidget(self.tv_Cil)

        self.tv_Camadas = QTableView(DialogHibrido)
        self.tv_Camadas.setObjectName(u"tv_Camadas")

        self.verticalLayout.addWidget(self.tv_Camadas)

        self.frame_2 = QFrame(DialogHibrido)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.checkBoxAutoTurn = QCheckBox(self.frame_2)
        self.checkBoxAutoTurn.setObjectName(u"checkBoxAutoTurn")
        self.checkBoxAutoTurn.setChecked(True)

        self.horizontalLayout_3.addWidget(self.checkBoxAutoTurn)

        self.pbCalc = QPushButton(self.frame_2)
        self.pbCalc.setObjectName(u"pbCalc")
        self.pbCalc.setStyleSheet(u"background-color: rgb(255, 85, 0);")

        self.horizontalLayout_3.addWidget(self.pbCalc)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_3.addWidget(self.pushButton)

        self.bt_CAD = QPushButton(self.frame_2)
        self.bt_CAD.setObjectName(u"bt_CAD")

        self.horizontalLayout_3.addWidget(self.bt_CAD)


        self.verticalLayout.addWidget(self.frame_2)

        QWidget.setTabOrder(self.cbMaterialTap, self.inputLn)
        QWidget.setTabOrder(self.inputLn, self.inputL1)
        QWidget.setTabOrder(self.inputL1, self.inputSinal)
        QWidget.setTabOrder(self.inputSinal, self.inputDi)
        QWidget.setTabOrder(self.inputDi, self.inputEspPerfil)
        QWidget.setTabOrder(self.inputEspPerfil, self.inputLargPerf)
        QWidget.setTabOrder(self.inputLargPerf, self.inputNumPerf)
        QWidget.setTabOrder(self.inputNumPerf, self.cbPosicao)
        QWidget.setTabOrder(self.cbPosicao, self.inputCalco)
        QWidget.setTabOrder(self.inputCalco, self.inputDBSb)
        QWidget.setTabOrder(self.inputDBSb, self.inputTap)
        QWidget.setTabOrder(self.inputTap, self.bt_DelTap)
        QWidget.setTabOrder(self.bt_DelTap, self.inputNesp)
        QWidget.setTabOrder(self.inputNesp, self.inputHe)
        QWidget.setTabOrder(self.inputHe, self.inputMutua)
        QWidget.setTabOrder(self.inputMutua, self.inputLtap)
        QWidget.setTabOrder(self.inputLtap, self.inputLcalc)
        QWidget.setTabOrder(self.inputLcalc, self.InputTmed)
        QWidget.setTabOrder(self.InputTmed, self.inputHotSpot)
        QWidget.setTabOrder(self.inputHotSpot, self.inputForca)
        QWidget.setTabOrder(self.inputForca, self.pbCalc)
        QWidget.setTabOrder(self.pbCalc, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.bt_AddTap)
        QWidget.setTabOrder(self.bt_AddTap, self.bt_CAD)
        QWidget.setTabOrder(self.bt_CAD, self.tv_Cil)
        QWidget.setTabOrder(self.tv_Cil, self.tv_Camadas)
        QWidget.setTabOrder(self.tv_Camadas, self.ck_Tap)
        QWidget.setTabOrder(self.ck_Tap, self.tv_Taps)

        self.retranslateUi(DialogHibrido)

        self.cbMaterialTap.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(DialogHibrido)
    # setupUi

    def retranslateUi(self, DialogHibrido):
        DialogHibrido.setWindowTitle(QCoreApplication.translate("DialogHibrido", u"M\u00f3dulo aberto simples ou como parte h\u00edbrido se\u00e7\u00e3o de taps", None))
        self.label_52.setText(QCoreApplication.translate("DialogHibrido", u"Material condutor", None))
        self.cbMaterialTap.setItemText(0, QCoreApplication.translate("DialogHibrido", u"Al", None))
        self.cbMaterialTap.setItemText(1, QCoreApplication.translate("DialogHibrido", u"Cu", None))
        self.cbMaterialTap.setItemText(2, QCoreApplication.translate("DialogHibrido", u"Inox AISI 304", None))
        self.cbMaterialTap.setItemText(3, QCoreApplication.translate("DialogHibrido", u"Inox AISI 310", None))
        self.cbMaterialTap.setItemText(4, QCoreApplication.translate("DialogHibrido", u"Liga de Al", None))

        self.label_4.setText(QCoreApplication.translate("DialogHibrido", u"Indut\u00e2ncia nominal (mH)", None))
        self.label_53.setText(QCoreApplication.translate("DialogHibrido", u"Indut\u00e2ncia indutor principal (mH)", None))
        self.label_54.setText(QCoreApplication.translate("DialogHibrido", u"Acoplamento sinal", None))
        self.label_56.setText(QCoreApplication.translate("DialogHibrido", u"Di\u00e2metro interno (mm)", None))
        self.label_57.setText(QCoreApplication.translate("DialogHibrido", u"Espessura do perfil (mm)", None))
        self.label_58.setText(QCoreApplication.translate("DialogHibrido", u"Largura do perfil mm)", None))
        self.label_59.setText(QCoreApplication.translate("DialogHibrido", u"# Perfiis em paralelo", None))
        self.label_61.setText(QCoreApplication.translate("DialogHibrido", u"Instala\u00e7\u00e3o", None))
        self.cbPosicao.setItemText(0, QCoreApplication.translate("DialogHibrido", u"Acima da cruzeta superior", None))
        self.cbPosicao.setItemText(1, QCoreApplication.translate("DialogHibrido", u"Satetlite por baixo da crizeta superior", None))
        self.cbPosicao.setItemText(2, QCoreApplication.translate("DialogHibrido", u"Sat\u00e9tile acima da cruzeta inferior", None))
        self.cbPosicao.setItemText(3, QCoreApplication.translate("DialogHibrido", u"Abaixo da cruzeta inferior", None))

        self.label_5.setText(QCoreApplication.translate("DialogHibrido", u"Altura do cal\u00e7o", None))
        self.label_62.setText(QCoreApplication.translate("DialogHibrido", u"Dist\u00e2ncia para cruzeta (mm)", None))
        self.label_3.setText(QCoreApplication.translate("DialogHibrido", u"Tap (%)", None))
        self.bt_DelTap.setText(QCoreApplication.translate("DialogHibrido", u"Deletar tap", None))
        self.bt_AddTap.setText(QCoreApplication.translate("DialogHibrido", u"Adicionar Tap", None))
        self.label_67.setText(QCoreApplication.translate("DialogHibrido", u"For\u00e7a axial (kN)", None))
        self.label_66.setText(QCoreApplication.translate("DialogHibrido", u"Indut\u00e2ncia Total calculada (mH)", None))
        self.label_68.setText(QCoreApplication.translate("DialogHibrido", u"Indut\u00e2ncia pr\u00f3pria Tap (mH)", None))
        self.label_65.setText(QCoreApplication.translate("DialogHibrido", u"Mutua Indut\u00e2ncia (mH)", None))
        self.label_64.setText(QCoreApplication.translate("DialogHibrido", u"Altura do enrolamento (mm)", None))
        self.label_63.setText(QCoreApplication.translate("DialogHibrido", u"N\u00famero de espiras", None))
        self.label.setText(QCoreApplication.translate("DialogHibrido", u"Tmed (\u00b0C)", None))
        self.label_2.setText(QCoreApplication.translate("DialogHibrido", u"Hot Spot (\u00b0C)", None))
        self.ck_Tap.setText(QCoreApplication.translate("DialogHibrido", u"Tap Calculado", None))
        self.checkBoxAutoTurn.setText(QCoreApplication.translate("DialogHibrido", u"Auto espira", None))
        self.pbCalc.setText(QCoreApplication.translate("DialogHibrido", u"Calcular Taps", None))
        self.pushButton.setText(QCoreApplication.translate("DialogHibrido", u"For\u00e7a no maior tap", None))
        self.bt_CAD.setText(QCoreApplication.translate("DialogHibrido", u"CAD", None))
    # retranslateUi

