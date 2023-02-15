# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SysDataDlg_SpinBox.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from template import bree_rc

class Ui_DialogSys(object):
    def setupUi(self, DialogSys):
        if not DialogSys.objectName():
            DialogSys.setObjectName(u"DialogSys")
        DialogSys.resize(564, 739)
        icon = QIcon()
        icon.addFile(u":/bree/configuracoes.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogSys.setWindowIcon(icon)
        DialogSys.setSizeGripEnabled(False)
        DialogSys.setModal(True)
        self.verticalLayout = QVBoxLayout(DialogSys)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.frequNciaHzLabel = QLabel(DialogSys)
        self.frequNciaHzLabel.setObjectName(u"frequNciaHzLabel")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.frequNciaHzLabel)

        self.inputFreq = QDoubleSpinBox(DialogSys)
        self.inputFreq.setObjectName(u"inputFreq")
        self.inputFreq.setDecimals(1)
        self.inputFreq.setMaximum(10000.000000000000000)
        self.inputFreq.setSingleStep(60.000000000000000)
        self.inputFreq.setValue(60.000000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.inputFreq)

        self.tensONominalVLabel = QLabel(DialogSys)
        self.tensONominalVLabel.setObjectName(u"tensONominalVLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.tensONominalVLabel)

        self.inputVn = QDoubleSpinBox(DialogSys)
        self.inputVn.setObjectName(u"inputVn")
        self.inputVn.setDecimals(3)
        self.inputVn.setMaximum(2000.000000000000000)
        self.inputVn.setValue(13.800000000000001)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.inputVn)

        self.normaLabel = QLabel(DialogSys)
        self.normaLabel.setObjectName(u"normaLabel")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.normaLabel)

        self.normaComboBox = QComboBox(DialogSys)
        self.normaComboBox.addItem("")
        self.normaComboBox.addItem("")
        self.normaComboBox.addItem("")
        self.normaComboBox.addItem("")
        self.normaComboBox.addItem("")
        self.normaComboBox.addItem("")
        self.normaComboBox.addItem("")
        self.normaComboBox.setObjectName(u"normaComboBox")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.normaComboBox)

        self.altitudeMLabel = QLabel(DialogSys)
        self.altitudeMLabel.setObjectName(u"altitudeMLabel")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.altitudeMLabel)

        self.inputAlt = QDoubleSpinBox(DialogSys)
        self.inputAlt.setObjectName(u"inputAlt")
        self.inputAlt.setDecimals(1)
        self.inputAlt.setMaximum(10000.000000000000000)
        self.inputAlt.setValue(1000.000000000000000)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.inputAlt)

        self.imputVento = QLabel(DialogSys)
        self.imputVento.setObjectName(u"imputVento")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.imputVento)

        self.inputVvento = QDoubleSpinBox(DialogSys)
        self.inputVvento.setObjectName(u"inputVvento")
        self.inputVvento.setDecimals(1)
        self.inputVvento.setMaximum(400.000000000000000)
        self.inputVvento.setValue(120.000000000000000)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.inputVvento)

        self.temperaturaAmbienteCLabel = QLabel(DialogSys)
        self.temperaturaAmbienteCLabel.setObjectName(u"temperaturaAmbienteCLabel")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.temperaturaAmbienteCLabel)

        self.inputTamb = QDoubleSpinBox(DialogSys)
        self.inputTamb.setObjectName(u"inputTamb")
        self.inputTamb.setDecimals(1)
        self.inputTamb.setValue(40.000000000000000)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.inputTamb)

        self.temperaturaDeReferNciaCLabel = QLabel(DialogSys)
        self.temperaturaDeReferNciaCLabel.setObjectName(u"temperaturaDeReferNciaCLabel")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.temperaturaDeReferNciaCLabel)

        self.inputTref = QDoubleSpinBox(DialogSys)
        self.inputTref.setObjectName(u"inputTref")
        self.inputTref.setDecimals(1)
        self.inputTref.setMaximum(200.000000000000000)
        self.inputTref.setValue(75.000000000000000)

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.inputTref)

        self.nBIKVLabel = QLabel(DialogSys)
        self.nBIKVLabel.setObjectName(u"nBIKVLabel")

        self.formLayout.setWidget(13, QFormLayout.LabelRole, self.nBIKVLabel)

        self.inputNBI = QDoubleSpinBox(DialogSys)
        self.inputNBI.setObjectName(u"inputNBI")
        self.inputNBI.setDecimals(1)
        self.inputNBI.setMaximum(2000.000000000000000)
        self.inputNBI.setValue(110.000000000000000)

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.inputNBI)

        self.label_4 = QLabel(DialogSys)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(14, QFormLayout.LabelRole, self.label_4)

        self.inputNBI_sea_level = QDoubleSpinBox(DialogSys)
        self.inputNBI_sea_level.setObjectName(u"inputNBI_sea_level")
        self.inputNBI_sea_level.setDecimals(1)
        self.inputNBI_sea_level.setMaximum(2000.000000000000000)
        self.inputNBI_sea_level.setValue(110.000000000000000)

        self.formLayout.setWidget(14, QFormLayout.FieldRole, self.inputNBI_sea_level)

        self.indutNciaNominalMHLabel = QLabel(DialogSys)
        self.indutNciaNominalMHLabel.setObjectName(u"indutNciaNominalMHLabel")

        self.formLayout.setWidget(16, QFormLayout.LabelRole, self.indutNciaNominalMHLabel)

        self.inputLn = QDoubleSpinBox(DialogSys)
        self.inputLn.setObjectName(u"inputLn")
        self.inputLn.setDecimals(4)
        self.inputLn.setMaximum(10000.000000000000000)
        self.inputLn.setValue(1.000000000000000)

        self.formLayout.setWidget(16, QFormLayout.FieldRole, self.inputLn)

        self.indutNciaAlvoMHLabel = QLabel(DialogSys)
        self.indutNciaAlvoMHLabel.setObjectName(u"indutNciaAlvoMHLabel")

        self.formLayout.setWidget(17, QFormLayout.LabelRole, self.indutNciaAlvoMHLabel)

        self.inputLtarget = QDoubleSpinBox(DialogSys)
        self.inputLtarget.setObjectName(u"inputLtarget")
        self.inputLtarget.setDecimals(4)
        self.inputLtarget.setMaximum(10000.000000000000000)
        self.inputLtarget.setValue(1.000000000000000)

        self.formLayout.setWidget(17, QFormLayout.FieldRole, self.inputLtarget)

        self.labelICCSys = QLabel(DialogSys)
        self.labelICCSys.setObjectName(u"labelICCSys")

        self.formLayout.setWidget(18, QFormLayout.LabelRole, self.labelICCSys)

        self.inputICCSys = QDoubleSpinBox(DialogSys)
        self.inputICCSys.setObjectName(u"inputICCSys")
        self.inputICCSys.setDecimals(1)
        self.inputICCSys.setMaximum(200.000000000000000)

        self.formLayout.setWidget(18, QFormLayout.FieldRole, self.inputICCSys)

        self.label_3 = QLabel(DialogSys)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(19, QFormLayout.LabelRole, self.label_3)

        self.inputICC = QDoubleSpinBox(DialogSys)
        self.inputICC.setObjectName(u"inputICC")
        self.inputICC.setDecimals(1)
        self.inputICC.setMaximum(200.000000000000000)

        self.formLayout.setWidget(19, QFormLayout.FieldRole, self.inputICC)

        self.duraOSLabel = QLabel(DialogSys)
        self.duraOSLabel.setObjectName(u"duraOSLabel")

        self.formLayout.setWidget(20, QFormLayout.LabelRole, self.duraOSLabel)

        self.inputTempo = QDoubleSpinBox(DialogSys)
        self.inputTempo.setObjectName(u"inputTempo")
        self.inputTempo.setDecimals(1)
        self.inputTempo.setValue(1.000000000000000)

        self.formLayout.setWidget(20, QFormLayout.FieldRole, self.inputTempo)

        self.correnteNominalALabel = QLabel(DialogSys)
        self.correnteNominalALabel.setObjectName(u"correnteNominalALabel")

        self.formLayout.setWidget(21, QFormLayout.LabelRole, self.correnteNominalALabel)

        self.inputInominal = QDoubleSpinBox(DialogSys)
        self.inputInominal.setObjectName(u"inputInominal")
        self.inputInominal.setMaximum(10000.000000000000000)

        self.formLayout.setWidget(21, QFormLayout.FieldRole, self.inputInominal)

        self.iccPicoKALabel = QLabel(DialogSys)
        self.iccPicoKALabel.setObjectName(u"iccPicoKALabel")

        self.formLayout.setWidget(23, QFormLayout.LabelRole, self.iccPicoKALabel)

        self.inputPico = QDoubleSpinBox(DialogSys)
        self.inputPico.setObjectName(u"inputPico")
        self.inputPico.setMaximum(200.000000000000000)

        self.formLayout.setWidget(23, QFormLayout.FieldRole, self.inputPico)

        self.correnteTotalALabel = QLabel(DialogSys)
        self.correnteTotalALabel.setObjectName(u"correnteTotalALabel")

        self.formLayout.setWidget(24, QFormLayout.LabelRole, self.correnteTotalALabel)

        self.inputITotal = QDoubleSpinBox(DialogSys)
        self.inputITotal.setObjectName(u"inputITotal")
        self.inputITotal.setMaximum(10000.000000000000000)
        self.inputITotal.setValue(500.000000000000000)

        self.formLayout.setWidget(24, QFormLayout.FieldRole, self.inputITotal)

        self.label = QLabel(DialogSys)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(25, QFormLayout.LabelRole, self.label)

        self.InputFatorCorrente = QDoubleSpinBox(DialogSys)
        self.InputFatorCorrente.setObjectName(u"InputFatorCorrente")
        self.InputFatorCorrente.setReadOnly(True)
        self.InputFatorCorrente.setDecimals(3)
        self.InputFatorCorrente.setValue(1.000000000000000)

        self.formLayout.setWidget(25, QFormLayout.FieldRole, self.InputFatorCorrente)

        self.label_2 = QLabel(DialogSys)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(26, QFormLayout.LabelRole, self.label_2)

        self.inputFatorNBI = QDoubleSpinBox(DialogSys)
        self.inputFatorNBI.setObjectName(u"inputFatorNBI")
        self.inputFatorNBI.setReadOnly(True)
        self.inputFatorNBI.setDecimals(3)
        self.inputFatorNBI.setValue(1.000000000000000)

        self.formLayout.setWidget(26, QFormLayout.FieldRole, self.inputFatorNBI)

        self.label_5 = QLabel(DialogSys)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(15, QFormLayout.LabelRole, self.label_5)

        self.comboBoxAplicacao = QComboBox(DialogSys)
        self.comboBoxAplicacao.addItem("")
        self.comboBoxAplicacao.addItem("")
        self.comboBoxAplicacao.addItem("")
        self.comboBoxAplicacao.addItem("")
        self.comboBoxAplicacao.addItem("")
        self.comboBoxAplicacao.addItem("")
        self.comboBoxAplicacao.addItem("")
        self.comboBoxAplicacao.setObjectName(u"comboBoxAplicacao")

        self.formLayout.setWidget(15, QFormLayout.FieldRole, self.comboBoxAplicacao)

        self.label_6 = QLabel(DialogSys)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.inputCliente = QLineEdit(DialogSys)
        self.inputCliente.setObjectName(u"inputCliente")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.inputCliente)

        self.label_7 = QLabel(DialogSys)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.inputQuant = QSpinBox(DialogSys)
        self.inputQuant.setObjectName(u"inputQuant")
        self.inputQuant.setMinimum(1)
        self.inputQuant.setMaximum(10000)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.inputQuant)

        self.label_8 = QLabel(DialogSys)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_8)

        self.inputRef = QLineEdit(DialogSys)
        self.inputRef.setObjectName(u"inputRef")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.inputRef)

        self.label_9 = QLabel(DialogSys)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_9)

        self.cbInstall = QComboBox(DialogSys)
        self.cbInstall.addItem("")
        self.cbInstall.addItem("")
        self.cbInstall.addItem("")
        self.cbInstall.setObjectName(u"cbInstall")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.cbInstall)

        self.label_10 = QLabel(DialogSys)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(22, QFormLayout.LabelRole, self.label_10)

        self.inputTipo = QLineEdit(DialogSys)
        self.inputTipo.setObjectName(u"inputTipo")

        self.formLayout.setWidget(22, QFormLayout.FieldRole, self.inputTipo)

        self.label_11 = QLabel(DialogSys)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_11)

        self.inputItem = QSpinBox(DialogSys)
        self.inputItem.setObjectName(u"inputItem")
        self.inputItem.setMinimum(1)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.inputItem)

        self.finalidadeLabel = QLabel(DialogSys)
        self.finalidadeLabel.setObjectName(u"finalidadeLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.finalidadeLabel)

        self.finalidadeComboBox = QComboBox(DialogSys)
        self.finalidadeComboBox.addItem("")
        self.finalidadeComboBox.addItem("")
        self.finalidadeComboBox.addItem("")
        self.finalidadeComboBox.addItem("")
        self.finalidadeComboBox.setObjectName(u"finalidadeComboBox")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.finalidadeComboBox)


        self.verticalLayout.addLayout(self.formLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_Ok = QPushButton(DialogSys)
        self.btn_Ok.setObjectName(u"btn_Ok")

        self.horizontalLayout.addWidget(self.btn_Ok)

        self.btn_cancel = QPushButton(DialogSys)
        self.btn_cancel.setObjectName(u"btn_cancel")

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.finalidadeComboBox, self.inputCliente)
        QWidget.setTabOrder(self.inputCliente, self.inputQuant)
        QWidget.setTabOrder(self.inputQuant, self.inputRef)
        QWidget.setTabOrder(self.inputRef, self.inputItem)
        QWidget.setTabOrder(self.inputItem, self.cbInstall)
        QWidget.setTabOrder(self.cbInstall, self.inputFreq)
        QWidget.setTabOrder(self.inputFreq, self.inputVn)
        QWidget.setTabOrder(self.inputVn, self.normaComboBox)
        QWidget.setTabOrder(self.normaComboBox, self.inputAlt)
        QWidget.setTabOrder(self.inputAlt, self.inputVvento)
        QWidget.setTabOrder(self.inputVvento, self.inputTamb)
        QWidget.setTabOrder(self.inputTamb, self.inputTref)
        QWidget.setTabOrder(self.inputTref, self.inputNBI)
        QWidget.setTabOrder(self.inputNBI, self.inputNBI_sea_level)
        QWidget.setTabOrder(self.inputNBI_sea_level, self.comboBoxAplicacao)
        QWidget.setTabOrder(self.comboBoxAplicacao, self.inputLn)
        QWidget.setTabOrder(self.inputLn, self.inputLtarget)
        QWidget.setTabOrder(self.inputLtarget, self.inputICCSys)
        QWidget.setTabOrder(self.inputICCSys, self.inputICC)
        QWidget.setTabOrder(self.inputICC, self.inputTempo)
        QWidget.setTabOrder(self.inputTempo, self.inputInominal)
        QWidget.setTabOrder(self.inputInominal, self.inputTipo)
        QWidget.setTabOrder(self.inputTipo, self.inputPico)
        QWidget.setTabOrder(self.inputPico, self.inputITotal)
        QWidget.setTabOrder(self.inputITotal, self.InputFatorCorrente)
        QWidget.setTabOrder(self.InputFatorCorrente, self.inputFatorNBI)
        QWidget.setTabOrder(self.inputFatorNBI, self.btn_Ok)
        QWidget.setTabOrder(self.btn_Ok, self.btn_cancel)

        self.retranslateUi(DialogSys)

        QMetaObject.connectSlotsByName(DialogSys)
    # setupUi

    def retranslateUi(self, DialogSys):
        DialogSys.setWindowTitle(QCoreApplication.translate("DialogSys", u"Dados do sistema", None))
        self.frequNciaHzLabel.setText(QCoreApplication.translate("DialogSys", u"Frequ\u00eancia (Hz)", None))
        self.inputFreq.setProperty("text", QCoreApplication.translate("DialogSys", u"60.0", None))
        self.inputFreq.setProperty("inputMask", "")
        self.inputFreq.setProperty("placeholderText", QCoreApplication.translate("DialogSys", u"Entre com a frequ\u00eancia industrial", None))
        self.tensONominalVLabel.setText(QCoreApplication.translate("DialogSys", u"Tens\u00e3o nominal (kV)", None))
        self.inputVn.setProperty("text", QCoreApplication.translate("DialogSys", u"13.800", None))
        self.normaLabel.setText(QCoreApplication.translate("DialogSys", u"Norma", None))
        self.normaComboBox.setItemText(0, QCoreApplication.translate("DialogSys", u"NBR 5119 - Reator", None))
        self.normaComboBox.setItemText(1, QCoreApplication.translate("DialogSys", u"NBR 8119 - Bobina", None))
        self.normaComboBox.setItemText(2, QCoreApplication.translate("DialogSys", u"IEC 60076-6 - Reator", None))
        self.normaComboBox.setItemText(3, QCoreApplication.translate("DialogSys", u"IEC 60353 - Bobina", None))
        self.normaComboBox.setItemText(4, QCoreApplication.translate("DialogSys", u"ANSI C57.21 - Reator Shunt", None))
        self.normaComboBox.setItemText(5, QCoreApplication.translate("DialogSys", u"ANSI C93.3 - Bobina", None))
        self.normaComboBox.setItemText(6, QCoreApplication.translate("DialogSys", u"ANSI C57.21 - Reator Serie", None))

        self.altitudeMLabel.setText(QCoreApplication.translate("DialogSys", u"Altitude (m)", None))
        self.inputAlt.setProperty("text", QCoreApplication.translate("DialogSys", u"1000.0", None))
        self.imputVento.setText(QCoreApplication.translate("DialogSys", u"Velocidade do vento (km/h)", None))
        self.inputVvento.setProperty("text", QCoreApplication.translate("DialogSys", u"120.0", None))
        self.temperaturaAmbienteCLabel.setText(QCoreApplication.translate("DialogSys", u"Temperatura ambiente (\u00b0C)", None))
        self.inputTamb.setProperty("text", QCoreApplication.translate("DialogSys", u"40.0", None))
        self.temperaturaDeReferNciaCLabel.setText(QCoreApplication.translate("DialogSys", u"Temperatura de refer\u00eancia (\u00b0C)", None))
        self.inputTref.setProperty("text", QCoreApplication.translate("DialogSys", u"75.0", None))
        self.nBIKVLabel.setText(QCoreApplication.translate("DialogSys", u"NBI (kV)", None))
        self.inputNBI.setProperty("text", QCoreApplication.translate("DialogSys", u"110.0", None))
        self.label_4.setText(QCoreApplication.translate("DialogSys", u"NBI ao n\u00edvel do mar (kV)", None))
        self.indutNciaNominalMHLabel.setText(QCoreApplication.translate("DialogSys", u"Indut\u00e2ncia nominal (mH)", None))
        self.indutNciaAlvoMHLabel.setText(QCoreApplication.translate("DialogSys", u"Indut\u00e2ncia alvo (mH)", None))
        self.labelICCSys.setText(QCoreApplication.translate("DialogSys", u"Corrente de curto-circuito sistema (kA)", None))
        self.label_3.setText(QCoreApplication.translate("DialogSys", u"Corrente de curto circuito no reator (kA)", None))
        self.duraOSLabel.setText(QCoreApplication.translate("DialogSys", u"Dura\u00e7\u00e3o (s)", None))
        self.inputTempo.setProperty("text", QCoreApplication.translate("DialogSys", u"1.0", None))
        self.correnteNominalALabel.setText(QCoreApplication.translate("DialogSys", u"Corrente nominal (A)", None))
        self.iccPicoKALabel.setText(QCoreApplication.translate("DialogSys", u"Icc Pico (kA)", None))
        self.correnteTotalALabel.setText(QCoreApplication.translate("DialogSys", u"Corrente total (A)", None))
        self.label.setText(QCoreApplication.translate("DialogSys", u"Fator de corre\u00e7\u00e3o da corrente pela altitude", None))
        self.InputFatorCorrente.setProperty("text", QCoreApplication.translate("DialogSys", u"1.000", None))
        self.label_2.setText(QCoreApplication.translate("DialogSys", u"Fator de corre\u00e7\u00e3o do NBI pela altitude", None))
        self.inputFatorNBI.setProperty("text", QCoreApplication.translate("DialogSys", u"1.000", None))
        self.label_5.setText(QCoreApplication.translate("DialogSys", u"Aplica\u00e7\u00e3o", None))
        self.comboBoxAplicacao.setItemText(0, QCoreApplication.translate("DialogSys", u"Filtro de harm\u00f4nico", None))
        self.comboBoxAplicacao.setItemText(1, QCoreApplication.translate("DialogSys", u"Limitador de corrente", None))
        self.comboBoxAplicacao.setItemText(2, QCoreApplication.translate("DialogSys", u"SHUNT", None))
        self.comboBoxAplicacao.setItemText(3, QCoreApplication.translate("DialogSys", u"SVC", None))
        self.comboBoxAplicacao.setItemText(4, QCoreApplication.translate("DialogSys", u"TCR", None))
        self.comboBoxAplicacao.setItemText(5, QCoreApplication.translate("DialogSys", u"Alisamento", None))
        self.comboBoxAplicacao.setItemText(6, QCoreApplication.translate("DialogSys", u"Inrush", None))

        self.label_6.setText(QCoreApplication.translate("DialogSys", u"Cliente", None))
        self.label_7.setText(QCoreApplication.translate("DialogSys", u"Quantidade", None))
        self.label_8.setText(QCoreApplication.translate("DialogSys", u"Refer\u00eancia", None))
        self.label_9.setText(QCoreApplication.translate("DialogSys", u"Instala\u00e7\u00e3o", None))
        self.cbInstall.setItemText(0, QCoreApplication.translate("DialogSys", u"Externa", None))
        self.cbInstall.setItemText(1, QCoreApplication.translate("DialogSys", u"Interna", None))
        self.cbInstall.setItemText(2, QCoreApplication.translate("DialogSys", u"Interna em c\u00fabiculo met\u00e1lico", None))

        self.label_10.setText(QCoreApplication.translate("DialogSys", u"Tipo", None))
        self.label_11.setText(QCoreApplication.translate("DialogSys", u"Item", None))
        self.finalidadeLabel.setText(QCoreApplication.translate("DialogSys", u"Finalidade", None))
        self.finalidadeComboBox.setItemText(0, QCoreApplication.translate("DialogSys", u"Estudo", None))
        self.finalidadeComboBox.setItemText(1, QCoreApplication.translate("DialogSys", u"Proposta", None))
        self.finalidadeComboBox.setItemText(2, QCoreApplication.translate("DialogSys", u"Fabrica\u00e7ao", None))
        self.finalidadeComboBox.setItemText(3, QCoreApplication.translate("DialogSys", u"Engenharia reversa", None))

        self.btn_Ok.setText(QCoreApplication.translate("DialogSys", u"Ok", None))
        self.btn_cancel.setText(QCoreApplication.translate("DialogSys", u"Cancelar", None))
    # retranslateUi

