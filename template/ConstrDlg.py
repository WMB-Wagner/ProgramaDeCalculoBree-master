# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'ConstrDlg.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from template import bree_rc


class Ui_DialogConstr(object):
    def setupUi(self, DialogConstr):
        if not DialogConstr.objectName():
            DialogConstr.setObjectName(u"DialogConstr")
        DialogConstr.resize(733, 620)
        icon = QIcon()
        icon.addFile(u":/bree/ruler.png", QSize(), QIcon.Normal, QIcon.Off)
        DialogConstr.setWindowIcon(icon)
        DialogConstr.setSizeGripEnabled(False)
        DialogConstr.setModal(True)
        self.verticalLayout = QVBoxLayout(DialogConstr)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(DialogConstr)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setFormAlignment(
            Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(4)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.normaLabel = QLabel(self.frame)
        self.normaLabel.setObjectName(u"normaLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.normaLabel)

        self.condutorComboBox = QComboBox(self.frame)
        self.condutorComboBox.addItem("")
        self.condutorComboBox.addItem("")
        self.condutorComboBox.addItem("")
        self.condutorComboBox.addItem("")
        self.condutorComboBox.addItem("")
        self.condutorComboBox.addItem("")
        self.condutorComboBox.setObjectName(u"condutorComboBox")

        self.formLayout.setWidget(
            0, QFormLayout.FieldRole, self.condutorComboBox)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.comboBoxClasse = QComboBox(self.frame)
        self.comboBoxClasse.addItem("")
        self.comboBoxClasse.addItem("")
        self.comboBoxClasse.addItem("")
        self.comboBoxClasse.setObjectName(u"comboBoxClasse")

        self.formLayout.setWidget(
            1, QFormLayout.FieldRole, self.comboBoxClasse)

        self.frequNciaHzLabel = QLabel(self.frame)
        self.frequNciaHzLabel.setObjectName(u"frequNciaHzLabel")

        self.formLayout.setWidget(
            2, QFormLayout.LabelRole, self.frequNciaHzLabel)

        self.inputAnelInf = QLineEdit(self.frame)
        self.inputAnelInf.setObjectName(u"inputAnelInf")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.inputAnelInf)

        self.tensONominalVLabel = QLabel(self.frame)
        self.tensONominalVLabel.setObjectName(u"tensONominalVLabel")

        self.formLayout.setWidget(
            3, QFormLayout.LabelRole, self.tensONominalVLabel)

        self.inputAnelSup = QLineEdit(self.frame)
        self.inputAnelSup.setObjectName(u"inputAnelSup")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.inputAnelSup)

        self.nBIKVLabel = QLabel(self.frame)
        self.nBIKVLabel.setObjectName(u"nBIKVLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.nBIKVLabel)

        self.inputDi = QLineEdit(self.frame)
        self.inputDi.setObjectName(u"inputDi")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.inputDi)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.inputDs = QLineEdit(self.frame)
        self.inputDs.setObjectName(u"inputDs")
        self.inputDs.setReadOnly(True)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.inputDs)

        self.altitudeMLabel = QLabel(self.frame)
        self.altitudeMLabel.setObjectName(u"altitudeMLabel")

        self.formLayout.setWidget(
            6, QFormLayout.LabelRole, self.altitudeMLabel)

        self.inputLargEsp = QLineEdit(self.frame)
        self.inputLargEsp.setObjectName(u"inputLargEsp")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.inputLargEsp)

        self.imputVento = QLabel(self.frame)
        self.imputVento.setObjectName(u"imputVento")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.imputVento)

        self.comboBoxCruzInf = QComboBox(self.frame)
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.setObjectName(u"comboBoxCruzInf")

        self.formLayout.setWidget(
            7, QFormLayout.FieldRole, self.comboBoxCruzInf)

        self.labelICC = QLabel(self.frame)
        self.labelICC.setObjectName(u"labelICC")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.labelICC)

        self.comboBoxCruzSup = QComboBox(self.frame)
        self.comboBoxCruzSup.setObjectName(u"comboBoxCruzSup")

        self.formLayout.setWidget(
            8, QFormLayout.FieldRole, self.comboBoxCruzSup)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_6)

        self.comboBoxFibra = QComboBox(self.frame)
        self.comboBoxFibra.setObjectName(u"comboBoxFibra")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.comboBoxFibra)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_5)

        self.comboBoxAWG = QComboBox(self.frame)
        self.comboBoxAWG.setObjectName(u"comboBoxAWG")

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.comboBoxAWG)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_8)

        self.input_Folga = QLineEdit(self.frame)
        self.input_Folga.setObjectName(u"input_Folga")

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.input_Folga)

        self.horizontalLayout_2.addLayout(self.formLayout)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setVerticalSpacing(4)
        self.formLayout_4.setContentsMargins(10, 10, 10, 10)
        self.duraOSLabel = QLabel(self.frame)
        self.duraOSLabel.setObjectName(u"duraOSLabel")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.duraOSLabel)

        self.inputAxial = QLineEdit(self.frame)
        self.inputAxial.setObjectName(u"inputAxial")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.inputAxial)

        self.iccPicoKALabel = QLabel(self.frame)
        self.iccPicoKALabel.setObjectName(u"iccPicoKALabel")

        self.formLayout_4.setWidget(
            1, QFormLayout.LabelRole, self.iccPicoKALabel)

        self.inputRadial = QLineEdit(self.frame)
        self.inputRadial.setObjectName(u"inputRadial")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.inputRadial)

        self.temperaturaAmbienteCLabel = QLabel(self.frame)
        self.temperaturaAmbienteCLabel.setObjectName(
            u"temperaturaAmbienteCLabel")

        self.formLayout_4.setWidget(
            2, QFormLayout.LabelRole, self.temperaturaAmbienteCLabel)

        self.inputSecao = QLineEdit(self.frame)
        self.inputSecao.setObjectName(u"inputSecao")
        self.inputSecao.setReadOnly(True)

        self.formLayout_4.setWidget(2, QFormLayout.FieldRole, self.inputSecao)

        self.temperaturaDeReferNciaCLabel = QLabel(self.frame)
        self.temperaturaDeReferNciaCLabel.setObjectName(
            u"temperaturaDeReferNciaCLabel")

        self.formLayout_4.setWidget(
            3, QFormLayout.LabelRole, self.temperaturaDeReferNciaCLabel)

        self.inputJdc = QLineEdit(self.frame)
        self.inputJdc.setObjectName(u"inputJdc")
        self.inputJdc.setReadOnly(True)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.inputJdc)

        self.indutNciaNominalMHLabel = QLabel(self.frame)
        self.indutNciaNominalMHLabel.setObjectName(u"indutNciaNominalMHLabel")

        self.formLayout_4.setWidget(
            4, QFormLayout.LabelRole, self.indutNciaNominalMHLabel)

        self.inputLcalc = QLineEdit(self.frame)
        self.inputLcalc.setObjectName(u"inputLcalc")
        self.inputLcalc.setReadOnly(True)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.inputLcalc)

        self.indutNciaAlvoMHLabel = QLabel(self.frame)
        self.indutNciaAlvoMHLabel.setObjectName(u"indutNciaAlvoMHLabel")

        self.formLayout_4.setWidget(
            5, QFormLayout.LabelRole, self.indutNciaAlvoMHLabel)

        self.inputErro = QLineEdit(self.frame)
        self.inputErro.setObjectName(u"inputErro")
        self.inputErro.setReadOnly(True)

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.inputErro)

        self.correnteNominalALabel = QLabel(self.frame)
        self.correnteNominalALabel.setObjectName(u"correnteNominalALabel")

        self.formLayout_4.setWidget(
            6, QFormLayout.LabelRole, self.correnteNominalALabel)

        self.inputPerdas = QLineEdit(self.frame)
        self.inputPerdas.setObjectName(u"inputPerdas")
        self.inputPerdas.setReadOnly(True)

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.inputPerdas)

        self.correnteTotalALabel = QLabel(self.frame)
        self.correnteTotalALabel.setObjectName(u"correnteTotalALabel")

        self.formLayout_4.setWidget(
            8, QFormLayout.LabelRole, self.correnteTotalALabel)

        self.inputQ = QLineEdit(self.frame)
        self.inputQ.setObjectName(u"inputQ")
        self.inputQ.setReadOnly(True)

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.inputQ)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout_4.setWidget(10, QFormLayout.LabelRole, self.label)

        self.InputTmed = QLineEdit(self.frame)
        self.InputTmed.setObjectName(u"InputTmed")
        self.InputTmed.setReadOnly(True)

        self.formLayout_4.setWidget(10, QFormLayout.FieldRole, self.InputTmed)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_4.setWidget(11, QFormLayout.LabelRole, self.label_2)

        self.inputHotSpot = QLineEdit(self.frame)
        self.inputHotSpot.setObjectName(u"inputHotSpot")
        self.inputHotSpot.setReadOnly(True)

        self.formLayout_4.setWidget(
            11, QFormLayout.FieldRole, self.inputHotSpot)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.label_7)

        self.inputPac = QLineEdit(self.frame)
        self.inputPac.setObjectName(u"inputPac")

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.inputPac)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(9, QFormLayout.LabelRole, self.label_9)

        self.comboBox_metodo_temp = QComboBox(self.frame)
        self.comboBox_metodo_temp.addItem("")
        self.comboBox_metodo_temp.addItem("")
        self.comboBox_metodo_temp.setObjectName(u"comboBox_metodo_temp")

        self.formLayout_4.setWidget(
            9, QFormLayout.FieldRole, self.comboBox_metodo_temp)

        self.horizontalLayout_2.addLayout(self.formLayout_4)

        self.verticalLayout.addWidget(self.frame)

        self.tableViewCil = QTableView(DialogConstr)
        self.tableViewCil.setObjectName(u"tableViewCil")

        self.verticalLayout.addWidget(self.tableViewCil)

        self.tableViewCam = QTableView(DialogConstr)
        self.tableViewCam.setObjectName(u"tableViewCam")

        self.verticalLayout.addWidget(self.tableViewCam)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBoxAuto = QCheckBox(DialogConstr)
        self.checkBoxAuto.setObjectName(u"checkBoxAuto")
        icon1 = QIcon()
        icon1.addFile(u":/bree/verificar.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.checkBoxAuto.setIcon(icon1)
        self.checkBoxAuto.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxAuto)

        self.bt_Del_Cil = QPushButton(DialogConstr)
        self.bt_Del_Cil.setObjectName(u"bt_Del_Cil")
        icon2 = QIcon()
        icon2.addFile(u":/bree/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Del_Cil.setIcon(icon2)

        self.horizontalLayout.addWidget(self.bt_Del_Cil)

        self.bt_ins_cil = QPushButton(DialogConstr)
        self.bt_ins_cil.setObjectName(u"bt_ins_cil")
        icon3 = QIcon()
        icon3.addFile(u":/bree/folder-open-document.png",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.bt_ins_cil.setIcon(icon3)

        self.horizontalLayout.addWidget(self.bt_ins_cil)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bt_inicial = QPushButton(DialogConstr)
        self.bt_inicial.setObjectName(u"bt_inicial")

        self.horizontalLayout.addWidget(self.bt_inicial)

        self.btn_Ok = QPushButton(DialogConstr)
        self.btn_Ok.setObjectName(u"btn_Ok")

        self.horizontalLayout.addWidget(self.btn_Ok)

        self.btn_calc = QPushButton(DialogConstr)
        self.btn_calc.setObjectName(u"btn_calc")
        self.btn_calc.setEnabled(False)

        self.horizontalLayout.addWidget(self.btn_calc)

        self.verticalLayout.addLayout(self.horizontalLayout)

        QWidget.setTabOrder(self.condutorComboBox, self.comboBoxClasse)
        QWidget.setTabOrder(self.comboBoxClasse, self.inputAnelInf)
        QWidget.setTabOrder(self.inputAnelInf, self.inputAnelSup)
        QWidget.setTabOrder(self.inputAnelSup, self.inputDi)
        QWidget.setTabOrder(self.inputDi, self.inputDs)
        QWidget.setTabOrder(self.inputDs, self.inputLargEsp)
        QWidget.setTabOrder(self.inputLargEsp, self.comboBoxCruzInf)
        QWidget.setTabOrder(self.comboBoxCruzInf, self.comboBoxCruzSup)
        QWidget.setTabOrder(self.comboBoxCruzSup, self.comboBoxFibra)
        QWidget.setTabOrder(self.comboBoxFibra, self.comboBoxAWG)
        QWidget.setTabOrder(self.comboBoxAWG, self.input_Folga)
        QWidget.setTabOrder(self.input_Folga, self.inputAxial)
        QWidget.setTabOrder(self.inputAxial, self.inputRadial)
        QWidget.setTabOrder(self.inputRadial, self.inputSecao)
        QWidget.setTabOrder(self.inputSecao, self.inputJdc)
        QWidget.setTabOrder(self.inputJdc, self.inputLcalc)
        QWidget.setTabOrder(self.inputLcalc, self.inputErro)
        QWidget.setTabOrder(self.inputErro, self.inputPerdas)
        QWidget.setTabOrder(self.inputPerdas, self.inputPac)
        QWidget.setTabOrder(self.inputPac, self.inputQ)
        QWidget.setTabOrder(self.inputQ, self.comboBox_metodo_temp)
        QWidget.setTabOrder(self.comboBox_metodo_temp, self.InputTmed)
        QWidget.setTabOrder(self.InputTmed, self.inputHotSpot)
        QWidget.setTabOrder(self.inputHotSpot, self.tableViewCil)
        QWidget.setTabOrder(self.tableViewCil, self.tableViewCam)
        QWidget.setTabOrder(self.tableViewCam, self.btn_calc)
        QWidget.setTabOrder(self.btn_calc, self.bt_ins_cil)
        QWidget.setTabOrder(self.bt_ins_cil, self.bt_Del_Cil)
        QWidget.setTabOrder(self.bt_Del_Cil, self.checkBoxAuto)

        self.retranslateUi(DialogConstr)

        self.comboBoxCruzInf.setCurrentIndex(4)

        QMetaObject.connectSlotsByName(DialogConstr)
    # setupUi

    def retranslateUi(self, DialogConstr):
        DialogConstr.setWindowTitle(QCoreApplication.translate(
            "DialogConstr", u"Dados construtivos", None))
        self.normaLabel.setText(QCoreApplication.translate(
            "DialogConstr", u"Material condutor", None))
        self.condutorComboBox.setItemText(
            0, QCoreApplication.translate("DialogConstr", u"Al", None))
        self.condutorComboBox.setItemText(
            1, QCoreApplication.translate("DialogConstr", u"Cu", None))
        self.condutorComboBox.setItemText(
            2, QCoreApplication.translate("DialogConstr", u"Inox AISI 304", None))
        self.condutorComboBox.setItemText(
            3, QCoreApplication.translate("DialogConstr", u"Inox AISI 310", None))
        self.condutorComboBox.setItemText(4, QCoreApplication.translate(
            "DialogConstr", u"ANSI C57.21 - Reator Shunt", None))
        self.condutorComboBox.setItemText(
            5, QCoreApplication.translate("DialogConstr", u"Liga de Al", None))

        self.label_4.setText(QCoreApplication.translate(
            "DialogConstr", u"Classe de temperatura do isolamento (\u00b0C)", None))
        self.comboBoxClasse.setItemText(
            0, QCoreApplication.translate("DialogConstr", u"130", None))
        self.comboBoxClasse.setItemText(
            1, QCoreApplication.translate("DialogConstr", u"155", None))
        self.comboBoxClasse.setItemText(
            2, QCoreApplication.translate("DialogConstr", u"180", None))

        self.frequNciaHzLabel.setText(QCoreApplication.translate(
            "DialogConstr", u"Anel de fibra inferior (mm)", None))
        self.inputAnelInf.setInputMask("")
        self.inputAnelInf.setText(
            QCoreApplication.translate("DialogConstr", u"50", None))
        self.inputAnelInf.setPlaceholderText(QCoreApplication.translate(
            "DialogConstr", u"Entre com a frequ\u00eancia industrial", None))
        self.tensONominalVLabel.setText(QCoreApplication.translate(
            "DialogConstr", u"Anel de firbra superior (mm) ", None))
        self.inputAnelSup.setText(
            QCoreApplication.translate("DialogConstr", u"50", None))
        self.nBIKVLabel.setText(QCoreApplication.translate(
            "DialogConstr", u"Di\u00e2metro interno (mm)", None))
        self.inputDi.setText(QCoreApplication.translate(
            "DialogConstr", u"1000", None))
        self.label_3.setText(QCoreApplication.translate(
            "DialogConstr", u"Di\u00e2metro externo (mm)", None))
        self.altitudeMLabel.setText(QCoreApplication.translate(
            "DialogConstr", u"Largura do espa\u00e7ador (mm)", None))
        self.inputLargEsp.setText(
            QCoreApplication.translate("DialogConstr", u"19.05", None))
        self.imputVento.setText(QCoreApplication.translate(
            "DialogConstr", u"Cruzeta inferior", None))
        self.comboBoxCruzInf.setItemText(0, QCoreApplication.translate(
            "DialogConstr", u"6 bra\u00e7os 5\"x1/2\"", None))
        self.comboBoxCruzInf.setItemText(1, QCoreApplication.translate(
            "DialogConstr", u"6 bra\u00e7os 4\"x1/2\"", None))
        self.comboBoxCruzInf.setItemText(2, QCoreApplication.translate(
            "DialogConstr", u"8 bra\u00e7os 3\"x1/2\"", None))
        self.comboBoxCruzInf.setItemText(3, QCoreApplication.translate(
            "DialogConstr", u"6 bra\u00e7os 3\"x1/2\"", None))
        self.comboBoxCruzInf.setItemText(4, QCoreApplication.translate(
            "DialogConstr", u"6 bra\u00e7os 3\"x1/2\"", None))
        self.comboBoxCruzInf.setItemText(5, QCoreApplication.translate(
            "DialogConstr", u"4 bra\u00e7os 3\"x1/2\"", None))
        self.comboBoxCruzInf.setItemText(6, QCoreApplication.translate(
            "DialogConstr", u"3 bra\u00e7os 3\"x1/2\"", None))

        self.labelICC.setText(QCoreApplication.translate(
            "DialogConstr", u"Cruzeta superior", None))
        self.label_6.setText(QCoreApplication.translate(
            "DialogConstr", u"Espessura das fibras de vidro (mm)", None))
        self.label_5.setText(QCoreApplication.translate(
            "DialogConstr", u"AWG do primeiro cilindro", None))
        self.label_8.setText(QCoreApplication.translate(
            "DialogConstr", u"Fator de folga", None))
        self.input_Folga.setText(
            QCoreApplication.translate("DialogConstr", u"1.0", None))
        self.duraOSLabel.setText(QCoreApplication.translate(
            "DialogConstr", u"# Fios Axiais", None))
        self.inputAxial.setText(
            QCoreApplication.translate("DialogConstr", u"1", None))
        self.iccPicoKALabel.setText(QCoreApplication.translate(
            "DialogConstr", u"# Fios Radiais", None))
        self.inputRadial.setText(
            QCoreApplication.translate("DialogConstr", u"4", None))
        self.temperaturaAmbienteCLabel.setText(QCoreApplication.translate(
            "DialogConstr", u"Se\u00e7\u00e3o condutora mm\u00b2", None))
        self.inputSecao.setText("")
        self.temperaturaDeReferNciaCLabel.setText(QCoreApplication.translate(
            "DialogConstr", u"Densidade de corrente em DC (A/mm\u00b2)", None))
        self.inputJdc.setText("")
        self.indutNciaNominalMHLabel.setText(QCoreApplication.translate(
            "DialogConstr", u"Indut\u00e2ncia calculada (mH)", None))
        self.indutNciaAlvoMHLabel.setText(QCoreApplication.translate(
            "DialogConstr", u"(Lcalc/Ln-1)*100 (%)", None))
        self.correnteNominalALabel.setText(
            QCoreApplication.translate("DialogConstr", u"Perdas DC (kW)", None))
        self.correnteTotalALabel.setText(
            QCoreApplication.translate("DialogConstr", u"Fator Q", None))
        self.label.setText(QCoreApplication.translate(
            "DialogConstr", u"Tmed (\u00b0C)", None))
        self.InputTmed.setText("")
        self.label_2.setText(QCoreApplication.translate(
            "DialogConstr", u"Hot Spot (\u00b0C)", None))
        self.inputHotSpot.setText("")
        self.label_7.setText(QCoreApplication.translate(
            "DialogConstr", u"Perdas AC (kW)", None))
        self.label_9.setText(QCoreApplication.translate(
            "DialogConstr", u"M\u00e9todo de c\u00e1lculo da temperatura", None))
        self.comboBox_metodo_temp.setItemText(0, QCoreApplication.translate(
            "DialogConstr", u"Heat constant com perdas @ 75 \u00b0C", None))
        self.comboBox_metodo_temp.setItemText(1, QCoreApplication.translate(
            "DialogConstr", u"Dubell com perdas @75 \u00b0C", None))

        self.checkBoxAuto.setText(
            QCoreApplication.translate("DialogConstr", u"Auto", None))
        self.bt_Del_Cil.setText(QCoreApplication.translate(
            "DialogConstr", u"Delete cilindros", None))
        self.bt_ins_cil.setText(QCoreApplication.translate(
            "DialogConstr", u"Insert Cilindro", None))
        self.bt_inicial.setText(QCoreApplication.translate(
            "DialogConstr", u"Inicial", None))
        self.btn_Ok.setText(QCoreApplication.translate(
            "DialogConstr", u"Ok", None))
        self.btn_calc.setText(QCoreApplication.translate(
            "DialogConstr", u"Calcular", None))
    # retranslateUi
