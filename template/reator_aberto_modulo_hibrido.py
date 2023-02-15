# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reator_aberto_modulo_hibrido.ui'
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
        DialogHibrido.resize(554, 451)
        self.horizontalLayout = QHBoxLayout(DialogHibrido)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.label_12 = QLabel(DialogHibrido)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_12)

        self.cbMaterialTap = QComboBox(DialogHibrido)
        self.cbMaterialTap.addItem("")
        self.cbMaterialTap.addItem("")
        self.cbMaterialTap.addItem("")
        self.cbMaterialTap.addItem("")
        self.cbMaterialTap.addItem("")
        self.cbMaterialTap.setObjectName(u"cbMaterialTap")
        self.cbMaterialTap.setEditable(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cbMaterialTap)

        self.label_15 = QLabel(DialogHibrido)
        self.label_15.setObjectName(u"label_15")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_15)

        self.inputL1 = QDoubleSpinBox(DialogHibrido)
        self.inputL1.setObjectName(u"inputL1")
        self.inputL1.setEnabled(False)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputL1)

        self.label_16 = QLabel(DialogHibrido)
        self.label_16.setObjectName(u"label_16")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_16)

        self.inputSinal = QSpinBox(DialogHibrido)
        self.inputSinal.setObjectName(u"inputSinal")
        self.inputSinal.setMinimum(-1)
        self.inputSinal.setMaximum(1)
        self.inputSinal.setSingleStep(2)
        self.inputSinal.setValue(1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.inputSinal)

        self.label_13 = QLabel(DialogHibrido)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_13)

        self.inputL2 = QDoubleSpinBox(DialogHibrido)
        self.inputL2.setObjectName(u"inputL2")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.inputL2)

        self.label = QLabel(DialogHibrido)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label)

        self.inputDi = QDoubleSpinBox(DialogHibrido)
        self.inputDi.setObjectName(u"inputDi")
        self.inputDi.setDecimals(1)
        self.inputDi.setMaximum(3000.000000000000000)
        self.inputDi.setValue(1200.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.inputDi)

        self.label_2 = QLabel(DialogHibrido)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_2)

        self.inputEspPerfil = QDoubleSpinBox(DialogHibrido)
        self.inputEspPerfil.setObjectName(u"inputEspPerfil")
        self.inputEspPerfil.setDecimals(1)
        self.inputEspPerfil.setValue(13.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.inputEspPerfil)

        self.label_3 = QLabel(DialogHibrido)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_3)

        self.inputLargPerf = QDoubleSpinBox(DialogHibrido)
        self.inputLargPerf.setObjectName(u"inputLargPerf")
        self.inputLargPerf.setDecimals(1)
        self.inputLargPerf.setValue(23.000000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.inputLargPerf)

        self.label_4 = QLabel(DialogHibrido)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_4)

        self.inputNumPerf = QSpinBox(DialogHibrido)
        self.inputNumPerf.setObjectName(u"inputNumPerf")
        self.inputNumPerf.setValue(1)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.inputNumPerf)

        self.label_5 = QLabel(DialogHibrido)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_5)

        self.cbAltCalco = QComboBox(DialogHibrido)
        self.cbAltCalco.addItem("")
        self.cbAltCalco.addItem("")
        self.cbAltCalco.addItem("")
        self.cbAltCalco.setObjectName(u"cbAltCalco")
        self.cbAltCalco.setEditable(True)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.cbAltCalco)

        self.label_6 = QLabel(DialogHibrido)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_6)

        self.cbPosicao = QComboBox(DialogHibrido)
        self.cbPosicao.addItem("")
        self.cbPosicao.addItem("")
        self.cbPosicao.addItem("")
        self.cbPosicao.addItem("")
        self.cbPosicao.setObjectName(u"cbPosicao")
        self.cbPosicao.setEditable(False)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.cbPosicao)

        self.label_7 = QLabel(DialogHibrido)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_7)

        self.inputDBSb = QDoubleSpinBox(DialogHibrido)
        self.inputDBSb.setObjectName(u"inputDBSb")
        self.inputDBSb.setDecimals(1)
        self.inputDBSb.setMaximum(1000.000000000000000)
        self.inputDBSb.setValue(10.000000000000000)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.inputDBSb)

        self.label_9 = QLabel(DialogHibrido)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_9)

        self.inputNesp = QDoubleSpinBox(DialogHibrido)
        self.inputNesp.setObjectName(u"inputNesp")
        self.inputNesp.setDecimals(4)
        self.inputNesp.setMaximum(1000.000000000000000)
        self.inputNesp.setValue(10.000000000000000)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.inputNesp)

        self.label_10 = QLabel(DialogHibrido)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_10)

        self.inputHe = QDoubleSpinBox(DialogHibrido)
        self.inputHe.setObjectName(u"inputHe")
        self.inputHe.setReadOnly(True)
        self.inputHe.setDecimals(1)
        self.inputHe.setMaximum(10000.000000000000000)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.inputHe)

        self.label_14 = QLabel(DialogHibrido)
        self.label_14.setObjectName(u"label_14")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.label_14)

        self.inputMutua = QDoubleSpinBox(DialogHibrido)
        self.inputMutua.setObjectName(u"inputMutua")
        self.inputMutua.setReadOnly(True)
        self.inputMutua.setDecimals(3)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.inputMutua)

        self.label_8 = QLabel(DialogHibrido)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_8)

        self.inputLcalc = QDoubleSpinBox(DialogHibrido)
        self.inputLcalc.setObjectName(u"inputLcalc")
        self.inputLcalc.setReadOnly(True)
        self.inputLcalc.setDecimals(3)
        self.inputLcalc.setMaximum(1000.000000000000000)

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.inputLcalc)

        self.label_11 = QLabel(DialogHibrido)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.label_11)

        self.inputForca = QDoubleSpinBox(DialogHibrido)
        self.inputForca.setObjectName(u"inputForca")
        self.inputForca.setReadOnly(True)
        self.inputForca.setDecimals(1)
        self.inputForca.setMaximum(10000.000000000000000)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.inputForca)

        self.pbCalc = QPushButton(DialogHibrido)
        self.pbCalc.setObjectName(u"pbCalc")

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.pbCalc)

        self.label_17 = QLabel(DialogHibrido)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_17)

        self.inputLtap = QDoubleSpinBox(DialogHibrido)
        self.inputLtap.setObjectName(u"inputLtap")

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.inputLtap)


        self.horizontalLayout.addLayout(self.formLayout)


        self.retranslateUi(DialogHibrido)

        self.cbMaterialTap.setCurrentIndex(4)
        self.cbAltCalco.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(DialogHibrido)
    # setupUi

    def retranslateUi(self, DialogHibrido):
        DialogHibrido.setWindowTitle(QCoreApplication.translate("DialogHibrido", u"M\u00f3dulo aberto simples ou como parte h\u00edbrido se\u00e7\u00e3o de taps", None))
        self.label_12.setText(QCoreApplication.translate("DialogHibrido", u"Material condutor", None))
        self.cbMaterialTap.setItemText(0, QCoreApplication.translate("DialogHibrido", u"Al", None))
        self.cbMaterialTap.setItemText(1, QCoreApplication.translate("DialogHibrido", u"Cu", None))
        self.cbMaterialTap.setItemText(2, QCoreApplication.translate("DialogHibrido", u"Inox AISI 304", None))
        self.cbMaterialTap.setItemText(3, QCoreApplication.translate("DialogHibrido", u"Inox AISI 310", None))
        self.cbMaterialTap.setItemText(4, QCoreApplication.translate("DialogHibrido", u"Liga de Al", None))

        self.label_15.setText(QCoreApplication.translate("DialogHibrido", u"Indut\u00e2ncia indutor principal (mH)", None))
        self.label_16.setText(QCoreApplication.translate("DialogHibrido", u"Acoplamento sinal", None))
        self.label_13.setText(QCoreApplication.translate("DialogHibrido", u"Indut\u00e2ncia Total Alvo (mH)", None))
        self.label.setText(QCoreApplication.translate("DialogHibrido", u"Di\u00e2metro interno (mm)", None))
        self.label_2.setText(QCoreApplication.translate("DialogHibrido", u"Espessura do perfil (mm)", None))
        self.label_3.setText(QCoreApplication.translate("DialogHibrido", u"Largura do pergil (mm)", None))
        self.label_4.setText(QCoreApplication.translate("DialogHibrido", u"# Perfiis em paralelo", None))
        self.label_5.setText(QCoreApplication.translate("DialogHibrido", u"Altura do cal\u00e7o (mm)", None))
        self.cbAltCalco.setItemText(0, QCoreApplication.translate("DialogHibrido", u"4.5", None))
        self.cbAltCalco.setItemText(1, QCoreApplication.translate("DialogHibrido", u"5.5", None))
        self.cbAltCalco.setItemText(2, QCoreApplication.translate("DialogHibrido", u"7.5", None))

        self.label_6.setText(QCoreApplication.translate("DialogHibrido", u"Instala\u00e7\u00e3o", None))
        self.cbPosicao.setItemText(0, QCoreApplication.translate("DialogHibrido", u"Acima da cruzeta superior", None))
        self.cbPosicao.setItemText(1, QCoreApplication.translate("DialogHibrido", u"Satetlite por baixo da crizeta superior", None))
        self.cbPosicao.setItemText(2, QCoreApplication.translate("DialogHibrido", u"Sat\u00e9tile acima da cruzeta inferior", None))
        self.cbPosicao.setItemText(3, QCoreApplication.translate("DialogHibrido", u"Abaixo da cruzeta inferior", None))

        self.label_7.setText(QCoreApplication.translate("DialogHibrido", u"Dist\u00e2ncia para cruzeta (mm)", None))
        self.label_9.setText(QCoreApplication.translate("DialogHibrido", u"N\u00famero de espiras", None))
        self.label_10.setText(QCoreApplication.translate("DialogHibrido", u"Altura do enrolamento (mm)", None))
        self.label_14.setText(QCoreApplication.translate("DialogHibrido", u"Mutua Indut\u00e2ncia (mH)", None))
        self.label_8.setText(QCoreApplication.translate("DialogHibrido", u"Indut\u00e2ncia Total calculada (mH)", None))
        self.label_11.setText(QCoreApplication.translate("DialogHibrido", u"For\u00e7a axial (kN)", None))
        self.pbCalc.setText(QCoreApplication.translate("DialogHibrido", u"Calcular", None))
        self.label_17.setText(QCoreApplication.translate("DialogHibrido", u"Indut\u00e2ncia pr\u00f3pria Tap (mH)", None))
    # retranslateUi

