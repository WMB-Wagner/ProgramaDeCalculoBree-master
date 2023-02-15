# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ConstrDlg_SpinBox.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from template import bree_rc

class Ui_DialogConstr(object):
    def setupUi(self, DialogConstr):
        if not DialogConstr.objectName():
            DialogConstr.setObjectName(u"DialogConstr")
        DialogConstr.resize(1358, 843)
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
        self.formLayout.setFormAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(4)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.normaLabel = QLabel(self.frame)
        self.normaLabel.setObjectName(u"normaLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.normaLabel)

        self.condutorComboBox = QComboBox(self.frame)
        self.condutorComboBox.addItem("")
        self.condutorComboBox.addItem("")
        self.condutorComboBox.addItem("")
        self.condutorComboBox.addItem("")
        self.condutorComboBox.addItem("")
        self.condutorComboBox.setObjectName(u"condutorComboBox")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.condutorComboBox)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.comboBoxClasse = QComboBox(self.frame)
        self.comboBoxClasse.addItem("")
        self.comboBoxClasse.addItem("")
        self.comboBoxClasse.addItem("")
        self.comboBoxClasse.setObjectName(u"comboBoxClasse")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.comboBoxClasse)

        self.frequNciaHzLabel = QLabel(self.frame)
        self.frequNciaHzLabel.setObjectName(u"frequNciaHzLabel")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.frequNciaHzLabel)

        self.inputAnelInf = QDoubleSpinBox(self.frame)
        self.inputAnelInf.setObjectName(u"inputAnelInf")
        self.inputAnelInf.setDecimals(1)
        self.inputAnelInf.setMaximum(500.000000000000000)
        self.inputAnelInf.setSingleStep(10.000000000000000)
        self.inputAnelInf.setValue(50.000000000000000)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.inputAnelInf)

        self.tensONominalVLabel = QLabel(self.frame)
        self.tensONominalVLabel.setObjectName(u"tensONominalVLabel")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.tensONominalVLabel)

        self.inputAnelSup = QDoubleSpinBox(self.frame)
        self.inputAnelSup.setObjectName(u"inputAnelSup")
        self.inputAnelSup.setDecimals(1)
        self.inputAnelSup.setMaximum(500.000000000000000)
        self.inputAnelSup.setValue(50.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.inputAnelSup)

        self.nBIKVLabel = QLabel(self.frame)
        self.nBIKVLabel.setObjectName(u"nBIKVLabel")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.nBIKVLabel)

        self.inputDi = QDoubleSpinBox(self.frame)
        self.inputDi.setObjectName(u"inputDi")
        self.inputDi.setDecimals(1)
        self.inputDi.setMinimum(200.000000000000000)
        self.inputDi.setMaximum(4000.000000000000000)
        self.inputDi.setSingleStep(50.000000000000000)
        self.inputDi.setValue(1000.000000000000000)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.inputDi)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_3)

        self.inputDs = QDoubleSpinBox(self.frame)
        self.inputDs.setObjectName(u"inputDs")
        self.inputDs.setReadOnly(True)
        self.inputDs.setDecimals(1)
        self.inputDs.setMaximum(5000.000000000000000)
        self.inputDs.setValue(1000.000000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.inputDs)

        self.altitudeMLabel = QLabel(self.frame)
        self.altitudeMLabel.setObjectName(u"altitudeMLabel")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.altitudeMLabel)

        self.inputLargEsp = QDoubleSpinBox(self.frame)
        self.inputLargEsp.setObjectName(u"inputLargEsp")
        self.inputLargEsp.setDecimals(2)
        self.inputLargEsp.setMinimum(0.000000000000000)
        self.inputLargEsp.setMaximum(101.599999999999994)
        self.inputLargEsp.setSingleStep(6.350000000000000)
        self.inputLargEsp.setValue(19.050000000000001)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.inputLargEsp)

        self.imputVento = QLabel(self.frame)
        self.imputVento.setObjectName(u"imputVento")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.imputVento)

        self.comboBoxCruzInf = QComboBox(self.frame)
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.addItem("")
        self.comboBoxCruzInf.setObjectName(u"comboBoxCruzInf")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.comboBoxCruzInf)

        self.labelICC = QLabel(self.frame)
        self.labelICC.setObjectName(u"labelICC")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.labelICC)

        self.comboBoxCruzSup = QComboBox(self.frame)
        self.comboBoxCruzSup.setObjectName(u"comboBoxCruzSup")

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.comboBoxCruzSup)

        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_17)

        self.inputHs = QDoubleSpinBox(self.frame)
        self.inputHs.setObjectName(u"inputHs")
        self.inputHs.setEnabled(False)
        self.inputHs.setDecimals(1)
        self.inputHs.setMaximum(5000.000000000000000)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.inputHs)

        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_21)

        self.comboBoxMontagem = QComboBox(self.frame)
        self.comboBoxMontagem.addItem("")
        self.comboBoxMontagem.addItem("")
        self.comboBoxMontagem.addItem("")
        self.comboBoxMontagem.addItem("")
        self.comboBoxMontagem.setObjectName(u"comboBoxMontagem")
        self.comboBoxMontagem.setEditable(False)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.comboBoxMontagem)


        self.horizontalLayout_2.addLayout(self.formLayout)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.formLayout_4.setVerticalSpacing(4)
        self.formLayout_4.setContentsMargins(10, 10, 10, 10)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.comboBoxFibra = QComboBox(self.frame)
        self.comboBoxFibra.setObjectName(u"comboBoxFibra")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.comboBoxFibra)

        self.duraOSLabel = QLabel(self.frame)
        self.duraOSLabel.setObjectName(u"duraOSLabel")

        self.formLayout_4.setWidget(3, QFormLayout.LabelRole, self.duraOSLabel)

        self.inputAxial = QDoubleSpinBox(self.frame)
        self.inputAxial.setObjectName(u"inputAxial")
        self.inputAxial.setDecimals(0)
        self.inputAxial.setMinimum(1.000000000000000)
        self.inputAxial.setMaximum(16.000000000000000)
        self.inputAxial.setValue(1.000000000000000)

        self.formLayout_4.setWidget(3, QFormLayout.FieldRole, self.inputAxial)

        self.iccPicoKALabel = QLabel(self.frame)
        self.iccPicoKALabel.setObjectName(u"iccPicoKALabel")

        self.formLayout_4.setWidget(4, QFormLayout.LabelRole, self.iccPicoKALabel)

        self.inputRadial = QDoubleSpinBox(self.frame)
        self.inputRadial.setObjectName(u"inputRadial")
        self.inputRadial.setDecimals(0)
        self.inputRadial.setMinimum(1.000000000000000)
        self.inputRadial.setMaximum(8.000000000000000)
        self.inputRadial.setValue(4.000000000000000)

        self.formLayout_4.setWidget(4, QFormLayout.FieldRole, self.inputRadial)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_4.setWidget(5, QFormLayout.LabelRole, self.label_5)

        self.comboBoxAWG = QComboBox(self.frame)
        self.comboBoxAWG.setObjectName(u"comboBoxAWG")

        self.formLayout_4.setWidget(5, QFormLayout.FieldRole, self.comboBoxAWG)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_4.setWidget(6, QFormLayout.LabelRole, self.label_8)

        self.input_Folga = QDoubleSpinBox(self.frame)
        self.input_Folga.setObjectName(u"input_Folga")
        self.input_Folga.setDecimals(3)
        self.input_Folga.setMinimum(1.000000000000000)
        self.input_Folga.setMaximum(1.200000000000000)
        self.input_Folga.setSingleStep(0.001000000000000)
        self.input_Folga.setValue(1.000000000000000)

        self.formLayout_4.setWidget(6, QFormLayout.FieldRole, self.input_Folga)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(7, QFormLayout.LabelRole, self.label_9)

        self.comboBox_metodo_temp = QComboBox(self.frame)
        self.comboBox_metodo_temp.addItem("")
        self.comboBox_metodo_temp.addItem("")
        self.comboBox_metodo_temp.setObjectName(u"comboBox_metodo_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_metodo_temp.sizePolicy().hasHeightForWidth())
        self.comboBox_metodo_temp.setSizePolicy(sizePolicy)
        self.comboBox_metodo_temp.setBaseSize(QSize(19, 0))

        self.formLayout_4.setWidget(7, QFormLayout.FieldRole, self.comboBox_metodo_temp)

        self.label_Tmed = QLabel(self.frame)
        self.label_Tmed.setObjectName(u"label_Tmed")

        self.formLayout_4.setWidget(8, QFormLayout.LabelRole, self.label_Tmed)

        self.InputTmed = QDoubleSpinBox(self.frame)
        self.InputTmed.setObjectName(u"InputTmed")
        self.InputTmed.setEnabled(False)
        self.InputTmed.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.InputTmed.setReadOnly(True)
        self.InputTmed.setDecimals(1)
        self.InputTmed.setMaximum(10000.000000000000000)

        self.formLayout_4.setWidget(8, QFormLayout.FieldRole, self.InputTmed)

        self.label_Hot_Spot = QLabel(self.frame)
        self.label_Hot_Spot.setObjectName(u"label_Hot_Spot")

        self.formLayout_4.setWidget(9, QFormLayout.LabelRole, self.label_Hot_Spot)

        self.inputHotSpot = QDoubleSpinBox(self.frame)
        self.inputHotSpot.setObjectName(u"inputHotSpot")
        self.inputHotSpot.setEnabled(False)
        self.inputHotSpot.setStyleSheet(u"color: rgb(0, 0, 255);\n"
"")
        self.inputHotSpot.setReadOnly(True)
        self.inputHotSpot.setDecimals(1)
        self.inputHotSpot.setMaximum(1000.000000000000000)

        self.formLayout_4.setWidget(9, QFormLayout.FieldRole, self.inputHotSpot)

        self.correnteNominalALabel = QLabel(self.frame)
        self.correnteNominalALabel.setObjectName(u"correnteNominalALabel")

        self.formLayout_4.setWidget(10, QFormLayout.LabelRole, self.correnteNominalALabel)

        self.inputPerdas = QDoubleSpinBox(self.frame)
        self.inputPerdas.setObjectName(u"inputPerdas")
        self.inputPerdas.setEnabled(False)
        self.inputPerdas.setReadOnly(True)
        self.inputPerdas.setDecimals(3)
        self.inputPerdas.setMaximum(300.000000000000000)

        self.formLayout_4.setWidget(10, QFormLayout.FieldRole, self.inputPerdas)

        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_20)

        self.inputDBS = QDoubleSpinBox(self.frame)
        self.inputDBS.setObjectName(u"inputDBS")
        self.inputDBS.setEnabled(False)
        self.inputDBS.setDecimals(1)
        self.inputDBS.setMaximum(5000.000000000000000)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.inputDBS)


        self.horizontalLayout_2.addLayout(self.formLayout_4)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setVerticalSpacing(4)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.temperaturaAmbienteCLabel = QLabel(self.frame)
        self.temperaturaAmbienteCLabel.setObjectName(u"temperaturaAmbienteCLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.temperaturaAmbienteCLabel)

        self.inputSecao = QDoubleSpinBox(self.frame)
        self.inputSecao.setObjectName(u"inputSecao")
        self.inputSecao.setEnabled(False)
        self.inputSecao.setReadOnly(True)
        self.inputSecao.setDecimals(1)
        self.inputSecao.setMaximum(10000.000000000000000)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.inputSecao)

        self.temperaturaDeReferNciaCLabel = QLabel(self.frame)
        self.temperaturaDeReferNciaCLabel.setObjectName(u"temperaturaDeReferNciaCLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.temperaturaDeReferNciaCLabel)

        self.inputJdc = QDoubleSpinBox(self.frame)
        self.inputJdc.setObjectName(u"inputJdc")
        self.inputJdc.setEnabled(False)
        self.inputJdc.setReadOnly(True)
        self.inputJdc.setDecimals(3)
        self.inputJdc.setMaximum(10.000000000000000)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.inputJdc)

        self.indutNciaNominalMHLabel = QLabel(self.frame)
        self.indutNciaNominalMHLabel.setObjectName(u"indutNciaNominalMHLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.indutNciaNominalMHLabel)

        self.inputLcalc = QDoubleSpinBox(self.frame)
        self.inputLcalc.setObjectName(u"inputLcalc")
        self.inputLcalc.setEnabled(False)
        self.inputLcalc.setReadOnly(True)
        self.inputLcalc.setDecimals(3)
        self.inputLcalc.setMaximum(100.000000000000000)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.inputLcalc)

        self.indutNciaAlvoMHLabel = QLabel(self.frame)
        self.indutNciaAlvoMHLabel.setObjectName(u"indutNciaAlvoMHLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.indutNciaAlvoMHLabel)

        self.inputErro = QDoubleSpinBox(self.frame)
        self.inputErro.setObjectName(u"inputErro")
        self.inputErro.setEnabled(False)
        self.inputErro.setReadOnly(True)
        self.inputErro.setDecimals(3)
        self.inputErro.setMaximum(20.000000000000000)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.inputErro)

        self.correnteTotalALabel = QLabel(self.frame)
        self.correnteTotalALabel.setObjectName(u"correnteTotalALabel")

        self.formLayout_2.setWidget(5, QFormLayout.LabelRole, self.correnteTotalALabel)

        self.inputQ = QDoubleSpinBox(self.frame)
        self.inputQ.setObjectName(u"inputQ")
        self.inputQ.setEnabled(False)
        self.inputQ.setReadOnly(True)
        self.inputQ.setDecimals(1)
        self.inputQ.setMaximum(1000.000000000000000)

        self.formLayout_2.setWidget(5, QFormLayout.FieldRole, self.inputQ)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_2.setWidget(6, QFormLayout.LabelRole, self.label_10)

        self.inputNBI_Esp = QDoubleSpinBox(self.frame)
        self.inputNBI_Esp.setObjectName(u"inputNBI_Esp")
        self.inputNBI_Esp.setEnabled(False)
        self.inputNBI_Esp.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.inputNBI_Esp.setReadOnly(True)

        self.formLayout_2.setWidget(6, QFormLayout.FieldRole, self.inputNBI_Esp)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")

        self.formLayout_2.setWidget(7, QFormLayout.LabelRole, self.label_11)

        self.inputNBI_He = QDoubleSpinBox(self.frame)
        self.inputNBI_He.setObjectName(u"inputNBI_He")
        self.inputNBI_He.setEnabled(False)
        self.inputNBI_He.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.inputNBI_He.setReadOnly(True)

        self.formLayout_2.setWidget(7, QFormLayout.FieldRole, self.inputNBI_He)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")

        self.formLayout_2.setWidget(8, QFormLayout.LabelRole, self.label_12)

        self.inputNBI_Cam = QDoubleSpinBox(self.frame)
        self.inputNBI_Cam.setObjectName(u"inputNBI_Cam")
        self.inputNBI_Cam.setEnabled(False)
        self.inputNBI_Cam.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.inputNBI_Cam.setReadOnly(True)

        self.formLayout_2.setWidget(8, QFormLayout.FieldRole, self.inputNBI_Cam)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(9, QFormLayout.LabelRole, self.label)

        self.inputNBI_Cil = QDoubleSpinBox(self.frame)
        self.inputNBI_Cil.setObjectName(u"inputNBI_Cil")
        self.inputNBI_Cil.setEnabled(False)
        self.inputNBI_Cil.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.inputNBI_Cil.setReadOnly(True)

        self.formLayout_2.setWidget(9, QFormLayout.FieldRole, self.inputNBI_Cil)

        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.label_7)

        self.inputPac = QDoubleSpinBox(self.frame)
        self.inputPac.setObjectName(u"inputPac")
        self.inputPac.setEnabled(False)
        self.inputPac.setReadOnly(True)
        self.inputPac.setDecimals(3)
        self.inputPac.setMaximum(300.000000000000000)

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.inputPac)


        self.horizontalLayout_2.addLayout(self.formLayout_2)

        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setVerticalSpacing(4)
        self.formLayout_3.setContentsMargins(10, 10, 10, 10)
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_18)

        self.inputHoop = QDoubleSpinBox(self.frame)
        self.inputHoop.setObjectName(u"inputHoop")
        self.inputHoop.setEnabled(False)
        self.inputHoop.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.inputHoop.setReadOnly(True)
        self.inputHoop.setDecimals(1)
        self.inputHoop.setMaximum(1000.000000000000000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.inputHoop)

        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_19)

        self.inputCompress = QDoubleSpinBox(self.frame)
        self.inputCompress.setObjectName(u"inputCompress")
        self.inputCompress.setEnabled(False)
        self.inputCompress.setStyleSheet(u"color: rgb(0, 0, 255);")
        self.inputCompress.setReadOnly(True)
        self.inputCompress.setDecimals(1)
        self.inputCompress.setMaximum(1000.000000000000000)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.inputCompress)

        self.comboBox_TempIcc = QComboBox(self.frame)
        self.comboBox_TempIcc.setObjectName(u"comboBox_TempIcc")
        self.comboBox_TempIcc.setEnabled(True)
        self.comboBox_TempIcc.setEditable(False)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.comboBox_TempIcc)

        self.labelInccNorma = QLabel(self.frame)
        self.labelInccNorma.setObjectName(u"labelInccNorma")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.labelInccNorma)

        self.comboBox_IccMax = QComboBox(self.frame)
        self.comboBox_IccMax.setObjectName(u"comboBox_IccMax")
        self.comboBox_IccMax.setEnabled(True)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.comboBox_IccMax)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.inputCs = QDoubleSpinBox(self.frame)
        self.inputCs.setObjectName(u"inputCs")
        self.inputCs.setEnabled(False)
        self.inputCs.setReadOnly(True)
        self.inputCs.setDecimals(3)
        self.inputCs.setMaximum(999.990000000000009)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.inputCs)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.label_13)

        self.inputCp = QDoubleSpinBox(self.frame)
        self.inputCp.setObjectName(u"inputCp")
        self.inputCp.setEnabled(False)
        self.inputCp.setReadOnly(True)
        self.inputCp.setDecimals(3)
        self.inputCp.setMaximum(999.990000000000009)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.inputCp)

        self.Cg9pF = QLabel(self.frame)
        self.Cg9pF.setObjectName(u"Cg9pF")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.Cg9pF)

        self.inputCg = QDoubleSpinBox(self.frame)
        self.inputCg.setObjectName(u"inputCg")
        self.inputCg.setEnabled(False)
        self.inputCg.setReadOnly(True)
        self.inputCg.setDecimals(3)
        self.inputCg.setMaximum(999.990000000000009)

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.inputCg)

        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")

        self.formLayout_3.setWidget(7, QFormLayout.LabelRole, self.label_14)

        self.inputCinf = QDoubleSpinBox(self.frame)
        self.inputCinf.setObjectName(u"inputCinf")
        self.inputCinf.setEnabled(False)
        self.inputCinf.setReadOnly(True)
        self.inputCinf.setDecimals(3)

        self.formLayout_3.setWidget(7, QFormLayout.FieldRole, self.inputCinf)

        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")

        self.formLayout_3.setWidget(8, QFormLayout.LabelRole, self.label_15)

        self.doubleSpinBox = QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setEnabled(False)
        self.doubleSpinBox.setReadOnly(True)
        self.doubleSpinBox.setDecimals(3)

        self.formLayout_3.setWidget(8, QFormLayout.FieldRole, self.doubleSpinBox)

        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")

        self.formLayout_3.setWidget(9, QFormLayout.LabelRole, self.label_16)

        self.doubleSpinBox_3 = QDoubleSpinBox(self.frame)
        self.doubleSpinBox_3.setObjectName(u"doubleSpinBox_3")
        self.doubleSpinBox_3.setEnabled(False)
        self.doubleSpinBox_3.setReadOnly(True)
        self.doubleSpinBox_3.setDecimals(3)

        self.formLayout_3.setWidget(9, QFormLayout.FieldRole, self.doubleSpinBox_3)

        self.label_temp_norma = QLabel(self.frame)
        self.label_temp_norma.setObjectName(u"label_temp_norma")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_temp_norma)


        self.horizontalLayout_2.addLayout(self.formLayout_3)

        self.formLayout_6 = QFormLayout()
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.pesoTotalKgLabel = QLabel(self.frame)
        self.pesoTotalKgLabel.setObjectName(u"pesoTotalKgLabel")

        self.formLayout_6.setWidget(0, QFormLayout.LabelRole, self.pesoTotalKgLabel)

        self.pesoTotalKgDoubleSpinBox = QDoubleSpinBox(self.frame)
        self.pesoTotalKgDoubleSpinBox.setObjectName(u"pesoTotalKgDoubleSpinBox")
        self.pesoTotalKgDoubleSpinBox.setDecimals(1)
        self.pesoTotalKgDoubleSpinBox.setMaximum(10000.000000000000000)

        self.formLayout_6.setWidget(0, QFormLayout.FieldRole, self.pesoTotalKgDoubleSpinBox)

        self.custoTotalRLabel = QLabel(self.frame)
        self.custoTotalRLabel.setObjectName(u"custoTotalRLabel")

        self.formLayout_6.setWidget(1, QFormLayout.LabelRole, self.custoTotalRLabel)

        self.custoTotalRLineEdit = QLineEdit(self.frame)
        self.custoTotalRLineEdit.setObjectName(u"custoTotalRLineEdit")

        self.formLayout_6.setWidget(1, QFormLayout.FieldRole, self.custoTotalRLineEdit)

        self.pesoTotalDoCondutorKgLabel = QLabel(self.frame)
        self.pesoTotalDoCondutorKgLabel.setObjectName(u"pesoTotalDoCondutorKgLabel")

        self.formLayout_6.setWidget(2, QFormLayout.LabelRole, self.pesoTotalDoCondutorKgLabel)

        self.pesoTotalDoCondutorKgDoubleSpinBox = QDoubleSpinBox(self.frame)
        self.pesoTotalDoCondutorKgDoubleSpinBox.setObjectName(u"pesoTotalDoCondutorKgDoubleSpinBox")
        self.pesoTotalDoCondutorKgDoubleSpinBox.setDecimals(1)
        self.pesoTotalDoCondutorKgDoubleSpinBox.setMaximum(10000.000000000000000)

        self.formLayout_6.setWidget(2, QFormLayout.FieldRole, self.pesoTotalDoCondutorKgDoubleSpinBox)

        self.pesoDaFibraKgLabel = QLabel(self.frame)
        self.pesoDaFibraKgLabel.setObjectName(u"pesoDaFibraKgLabel")

        self.formLayout_6.setWidget(3, QFormLayout.LabelRole, self.pesoDaFibraKgLabel)

        self.pesoDaFibraKgDoubleSpinBox = QDoubleSpinBox(self.frame)
        self.pesoDaFibraKgDoubleSpinBox.setObjectName(u"pesoDaFibraKgDoubleSpinBox")
        self.pesoDaFibraKgDoubleSpinBox.setDecimals(1)
        self.pesoDaFibraKgDoubleSpinBox.setMaximum(10000.000000000000000)

        self.formLayout_6.setWidget(3, QFormLayout.FieldRole, self.pesoDaFibraKgDoubleSpinBox)

        self.pesoDasCruzetasKgLabel = QLabel(self.frame)
        self.pesoDasCruzetasKgLabel.setObjectName(u"pesoDasCruzetasKgLabel")

        self.formLayout_6.setWidget(4, QFormLayout.LabelRole, self.pesoDasCruzetasKgLabel)

        self.pesoDasCruzetasKgDoubleSpinBox = QDoubleSpinBox(self.frame)
        self.pesoDasCruzetasKgDoubleSpinBox.setObjectName(u"pesoDasCruzetasKgDoubleSpinBox")
        self.pesoDasCruzetasKgDoubleSpinBox.setDecimals(1)
        self.pesoDasCruzetasKgDoubleSpinBox.setMaximum(10000.000000000000000)

        self.formLayout_6.setWidget(4, QFormLayout.FieldRole, self.pesoDasCruzetasKgDoubleSpinBox)


        self.horizontalLayout_2.addLayout(self.formLayout_6)


        self.verticalLayout.addWidget(self.frame)

        self.tableViewCil = QTableView(DialogConstr)
        self.tableViewCil.setObjectName(u"tableViewCil")

        self.verticalLayout.addWidget(self.tableViewCil)

        self.tableViewCam = QTableView(DialogConstr)
        self.tableViewCam.setObjectName(u"tableViewCam")

        self.verticalLayout.addWidget(self.tableViewCam)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBoxAutoTurn = QCheckBox(DialogConstr)
        self.checkBoxAutoTurn.setObjectName(u"checkBoxAutoTurn")
        icon1 = QIcon()
        icon1.addFile(u":/bree/verificar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.checkBoxAutoTurn.setIcon(icon1)
        self.checkBoxAutoTurn.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxAutoTurn)

        self.checkBoxHe = QCheckBox(DialogConstr)
        self.checkBoxHe.setObjectName(u"checkBoxHe")
        self.checkBoxHe.setIcon(icon1)
        self.checkBoxHe.setChecked(True)

        self.horizontalLayout.addWidget(self.checkBoxHe)

        self.bt_Del_Cil = QPushButton(DialogConstr)
        self.bt_Del_Cil.setObjectName(u"bt_Del_Cil")
        icon2 = QIcon()
        icon2.addFile(u":/bree/cross.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_Del_Cil.setIcon(icon2)

        self.horizontalLayout.addWidget(self.bt_Del_Cil)

        self.bt_ins_cil = QPushButton(DialogConstr)
        self.bt_ins_cil.setObjectName(u"bt_ins_cil")
        icon3 = QIcon()
        icon3.addFile(u":/bree/folder-open-document.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_ins_cil.setIcon(icon3)

        self.horizontalLayout.addWidget(self.bt_ins_cil)

        self.horizontalSpacer = QSpacerItem(30, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.bt_inicial = QPushButton(DialogConstr)
        self.bt_inicial.setObjectName(u"bt_inicial")
        self.bt_inicial.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout.addWidget(self.bt_inicial)

        self.btn_Ok = QPushButton(DialogConstr)
        self.btn_Ok.setObjectName(u"btn_Ok")

        self.horizontalLayout.addWidget(self.btn_Ok)

        self.btnFreeCad = QPushButton(DialogConstr)
        self.btnFreeCad.setObjectName(u"btnFreeCad")
        self.btnFreeCad.setEnabled(False)
        self.btnFreeCad.setIcon(icon)

        self.horizontalLayout.addWidget(self.btnFreeCad)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.cB_FC_model = QCheckBox(DialogConstr)
        self.cB_FC_model.setObjectName(u"cB_FC_model")

        self.horizontalLayout_4.addWidget(self.cB_FC_model)

        self.pbObs = QPushButton(DialogConstr)
        self.pbObs.setObjectName(u"pbObs")
        self.pbObs.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.horizontalLayout_4.addWidget(self.pbObs)

        self.pushButtonCalc = QPushButton(DialogConstr)
        self.pushButtonCalc.setObjectName(u"pushButtonCalc")
        self.pushButtonCalc.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout_4.addWidget(self.pushButtonCalc)

        self.pushButtonAsBuilt = QPushButton(DialogConstr)
        self.pushButtonAsBuilt.setObjectName(u"pushButtonAsBuilt")
        self.pushButtonAsBuilt.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout_4.addWidget(self.pushButtonAsBuilt)

        self.btEmpilhado = QPushButton(DialogConstr)
        self.btEmpilhado.setObjectName(u"btEmpilhado")
        self.btEmpilhado.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.btEmpilhado)

        self.btn_calc = QPushButton(DialogConstr)
        self.btn_calc.setObjectName(u"btn_calc")
        self.btn_calc.setEnabled(False)
        self.btn_calc.setStyleSheet(u"background-color: rgb(255, 0, 0);")

        self.horizontalLayout_4.addWidget(self.btn_calc)

        self.btForce = QPushButton(DialogConstr)
        self.btForce.setObjectName(u"btForce")
        self.btForce.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.btForce)

        self.pbCriar = QPushButton(DialogConstr)
        self.pbCriar.setObjectName(u"pbCriar")
        self.pbCriar.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.pbCriar)

        self.pbHibrido = QPushButton(DialogConstr)
        self.pbHibrido.setObjectName(u"pbHibrido")
        self.pbHibrido.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.pbHibrido)

        self.pbQRing = QPushButton(DialogConstr)
        self.pbQRing.setObjectName(u"pbQRing")
        self.pbQRing.setEnabled(False)

        self.horizontalLayout_4.addWidget(self.pbQRing)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        QWidget.setTabOrder(self.condutorComboBox, self.comboBoxClasse)
        QWidget.setTabOrder(self.comboBoxClasse, self.inputAnelInf)
        QWidget.setTabOrder(self.inputAnelInf, self.inputAnelSup)
        QWidget.setTabOrder(self.inputAnelSup, self.inputDi)
        QWidget.setTabOrder(self.inputDi, self.inputLargEsp)
        QWidget.setTabOrder(self.inputLargEsp, self.comboBoxCruzInf)
        QWidget.setTabOrder(self.comboBoxCruzInf, self.comboBoxCruzSup)
        QWidget.setTabOrder(self.comboBoxCruzSup, self.comboBoxFibra)
        QWidget.setTabOrder(self.comboBoxFibra, self.inputAxial)
        QWidget.setTabOrder(self.inputAxial, self.inputRadial)
        QWidget.setTabOrder(self.inputRadial, self.comboBoxAWG)
        QWidget.setTabOrder(self.comboBoxAWG, self.input_Folga)
        QWidget.setTabOrder(self.input_Folga, self.comboBox_metodo_temp)
        QWidget.setTabOrder(self.comboBox_metodo_temp, self.checkBoxAutoTurn)
        QWidget.setTabOrder(self.checkBoxAutoTurn, self.checkBoxHe)
        QWidget.setTabOrder(self.checkBoxHe, self.bt_Del_Cil)
        QWidget.setTabOrder(self.bt_Del_Cil, self.bt_ins_cil)
        QWidget.setTabOrder(self.bt_ins_cil, self.inputPerdas)
        QWidget.setTabOrder(self.inputPerdas, self.inputSecao)
        QWidget.setTabOrder(self.inputSecao, self.inputJdc)
        QWidget.setTabOrder(self.inputJdc, self.inputLcalc)
        QWidget.setTabOrder(self.inputLcalc, self.inputErro)
        QWidget.setTabOrder(self.inputErro, self.inputQ)
        QWidget.setTabOrder(self.inputQ, self.inputNBI_Esp)
        QWidget.setTabOrder(self.inputNBI_Esp, self.inputNBI_He)
        QWidget.setTabOrder(self.inputNBI_He, self.inputNBI_Cam)
        QWidget.setTabOrder(self.inputNBI_Cam, self.inputNBI_Cil)
        QWidget.setTabOrder(self.inputNBI_Cil, self.inputHoop)
        QWidget.setTabOrder(self.inputHoop, self.inputCompress)
        QWidget.setTabOrder(self.inputCompress, self.inputCs)
        QWidget.setTabOrder(self.inputCs, self.inputCp)
        QWidget.setTabOrder(self.inputCp, self.inputCg)
        QWidget.setTabOrder(self.inputCg, self.inputCinf)
        QWidget.setTabOrder(self.inputCinf, self.doubleSpinBox)
        QWidget.setTabOrder(self.doubleSpinBox, self.doubleSpinBox_3)
        QWidget.setTabOrder(self.doubleSpinBox_3, self.inputDs)
        QWidget.setTabOrder(self.inputDs, self.comboBox_TempIcc)
        QWidget.setTabOrder(self.comboBox_TempIcc, self.comboBox_IccMax)
        QWidget.setTabOrder(self.comboBox_IccMax, self.bt_inicial)
        QWidget.setTabOrder(self.bt_inicial, self.btn_Ok)
        QWidget.setTabOrder(self.btn_Ok, self.inputHs)
        QWidget.setTabOrder(self.inputHs, self.tableViewCam)
        QWidget.setTabOrder(self.tableViewCam, self.InputTmed)
        QWidget.setTabOrder(self.InputTmed, self.tableViewCil)
        QWidget.setTabOrder(self.tableViewCil, self.inputHotSpot)

        self.retranslateUi(DialogConstr)

        self.comboBoxCruzInf.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(DialogConstr)
    # setupUi

    def retranslateUi(self, DialogConstr):
        DialogConstr.setWindowTitle(QCoreApplication.translate("DialogConstr", u"Dados construtivos", None))
        self.normaLabel.setText(QCoreApplication.translate("DialogConstr", u"Material condutor", None))
        self.condutorComboBox.setItemText(0, QCoreApplication.translate("DialogConstr", u"Al", None))
        self.condutorComboBox.setItemText(1, QCoreApplication.translate("DialogConstr", u"Cu", None))
        self.condutorComboBox.setItemText(2, QCoreApplication.translate("DialogConstr", u"Inox AISI 304", None))
        self.condutorComboBox.setItemText(3, QCoreApplication.translate("DialogConstr", u"Inox AISI 310", None))
        self.condutorComboBox.setItemText(4, QCoreApplication.translate("DialogConstr", u"Liga de Al", None))

        self.label_4.setText(QCoreApplication.translate("DialogConstr", u"Classe de temperatura(\u00b0C)", None))
        self.comboBoxClasse.setItemText(0, QCoreApplication.translate("DialogConstr", u"130", None))
        self.comboBoxClasse.setItemText(1, QCoreApplication.translate("DialogConstr", u"155", None))
        self.comboBoxClasse.setItemText(2, QCoreApplication.translate("DialogConstr", u"180", None))

        self.frequNciaHzLabel.setText(QCoreApplication.translate("DialogConstr", u"Anel de fibra inferior (mm)", None))
        self.inputAnelInf.setProperty("text", QCoreApplication.translate("DialogConstr", u"50.0", None))
        self.inputAnelInf.setProperty("inputMask", "")
        self.inputAnelInf.setProperty("placeholderText", QCoreApplication.translate("DialogConstr", u"Entre com a frequ\u00eancia industrial", None))
        self.tensONominalVLabel.setText(QCoreApplication.translate("DialogConstr", u"Anel de firbra superior (mm) ", None))
        self.inputAnelSup.setProperty("text", QCoreApplication.translate("DialogConstr", u"50.0", None))
        self.nBIKVLabel.setText(QCoreApplication.translate("DialogConstr", u"Di\u00e2metro interno (mm)", None))
        self.inputDi.setProperty("text", QCoreApplication.translate("DialogConstr", u"1000.0", None))
        self.label_3.setText(QCoreApplication.translate("DialogConstr", u"Di\u00e2metro externo (mm)", None))
        self.altitudeMLabel.setText(QCoreApplication.translate("DialogConstr", u"Largura do espa\u00e7ador (mm)", None))
        self.inputLargEsp.setProperty("text", QCoreApplication.translate("DialogConstr", u"19.05", None))
        self.imputVento.setText(QCoreApplication.translate("DialogConstr", u"Cruzeta inferior", None))
        self.comboBoxCruzInf.setItemText(0, QCoreApplication.translate("DialogConstr", u"6 bra\u00e7os 5\"x1/2\"", None))
        self.comboBoxCruzInf.setItemText(1, QCoreApplication.translate("DialogConstr", u"6 bra\u00e7os 4\"x1/2\"", None))
        self.comboBoxCruzInf.setItemText(2, QCoreApplication.translate("DialogConstr", u"8 bra\u00e7os 3\"x1/2\"", None))
        self.comboBoxCruzInf.setItemText(3, QCoreApplication.translate("DialogConstr", u"6 bra\u00e7os 3\"x1/2\"", None))
        self.comboBoxCruzInf.setItemText(4, QCoreApplication.translate("DialogConstr", u"6 bra\u00e7os 3\"x1/2\"", None))
        self.comboBoxCruzInf.setItemText(5, QCoreApplication.translate("DialogConstr", u"4 bra\u00e7os 3\"x1/2\"", None))
        self.comboBoxCruzInf.setItemText(6, QCoreApplication.translate("DialogConstr", u"3 bra\u00e7os 3\"x1/2\"", None))

        self.labelICC.setText(QCoreApplication.translate("DialogConstr", u"Cruzeta superior", None))
        self.label_17.setText(QCoreApplication.translate("DialogConstr", u"Altura do reator (mm)", None))
        self.label_21.setText(QCoreApplication.translate("DialogConstr", u"Montagem", None))
        self.comboBoxMontagem.setItemText(0, QCoreApplication.translate("DialogConstr", u"Lado a lado", None))
        self.comboBoxMontagem.setItemText(1, QCoreApplication.translate("DialogConstr", u"Lado a lado com coroa de taps", None))
        self.comboBoxMontagem.setItemText(2, QCoreApplication.translate("DialogConstr", u"Empilhado duplo", None))
        self.comboBoxMontagem.setItemText(3, QCoreApplication.translate("DialogConstr", u"Empilhado trif\u00e1sico", None))

        self.label_6.setText(QCoreApplication.translate("DialogConstr", u"Espessura das fibra(mm)", None))
        self.duraOSLabel.setText(QCoreApplication.translate("DialogConstr", u"# Fios Axiais", None))
        self.inputAxial.setProperty("text", QCoreApplication.translate("DialogConstr", u"1", None))
        self.iccPicoKALabel.setText(QCoreApplication.translate("DialogConstr", u"# Fios Radiais", None))
        self.inputRadial.setProperty("text", QCoreApplication.translate("DialogConstr", u"4", None))
        self.label_5.setText(QCoreApplication.translate("DialogConstr", u"AWG do primeiro cilindro", None))
        self.label_8.setText(QCoreApplication.translate("DialogConstr", u"Fator de folga", None))
        self.input_Folga.setProperty("text", QCoreApplication.translate("DialogConstr", u"1.000", None))
        self.label_9.setText(QCoreApplication.translate("DialogConstr", u"M\u00e9todo de c\u00e1lculo da temperatura", None))
        self.comboBox_metodo_temp.setItemText(0, QCoreApplication.translate("DialogConstr", u"Heat constant", None))
        self.comboBox_metodo_temp.setItemText(1, QCoreApplication.translate("DialogConstr", u"Dubell", None))

        self.label_Tmed.setText(QCoreApplication.translate("DialogConstr", u"Tmed (\u00b0C)", None))
        self.InputTmed.setProperty("text", QCoreApplication.translate("DialogConstr", u"0.0", None))
        self.label_Hot_Spot.setText(QCoreApplication.translate("DialogConstr", u"Hot Spot (\u00b0C)", None))
        self.inputHotSpot.setProperty("text", QCoreApplication.translate("DialogConstr", u"0.0", None))
        self.correnteNominalALabel.setText(QCoreApplication.translate("DialogConstr", u"Perdas DC (kW) @ 75 \u00b0C", None))
        self.label_20.setText(QCoreApplication.translate("DialogConstr", u"Dist\u00e2ncia entre cruzetas (mm)", None))
        self.temperaturaAmbienteCLabel.setText(QCoreApplication.translate("DialogConstr", u"Se\u00e7\u00e3o condutora mm\u00b2", None))
        self.inputSecao.setProperty("text", QCoreApplication.translate("DialogConstr", u"0.0", None))
        self.temperaturaDeReferNciaCLabel.setText(QCoreApplication.translate("DialogConstr", u"Densidade de corrente em DC (A/mm\u00b2)", None))
        self.inputJdc.setProperty("text", QCoreApplication.translate("DialogConstr", u"0.000", None))
        self.indutNciaNominalMHLabel.setText(QCoreApplication.translate("DialogConstr", u"Indut\u00e2ncia calculada (mH)", None))
        self.indutNciaAlvoMHLabel.setText(QCoreApplication.translate("DialogConstr", u"(Lcalc/Ln-1)*100 (%)", None))
        self.correnteTotalALabel.setText(QCoreApplication.translate("DialogConstr", u"Fator Q", None))
        self.label_10.setText(QCoreApplication.translate("DialogConstr", u"NBI/Esp (kV/esp) < 10 kV/esp", None))
        self.label_11.setText(QCoreApplication.translate("DialogConstr", u"NBI/He (kV/mm) < 0.5 kV/mm", None))
        self.label_12.setText(QCoreApplication.translate("DialogConstr", u"NBI Cam (kV/mm) < 10 kV/mm", None))
        self.label.setText(QCoreApplication.translate("DialogConstr", u"NBI Cil (kV/mm) < 50 kV/mm", None))
        self.label_7.setText(QCoreApplication.translate("DialogConstr", u"Perdas AC (kW) @ 75 \u00b0C", None))
        self.label_18.setText(QCoreApplication.translate("DialogConstr", u"Hoop (Mpa) < 350 Mpa", None))
        self.label_19.setText(QCoreApplication.translate("DialogConstr", u"Comp (Mpa) < 135 Mpa", None))
        self.labelInccNorma.setText(QCoreApplication.translate("DialogConstr", u"Incc M\u00e1xximo pela IEC (kA)", None))
        self.label_2.setText(QCoreApplication.translate("DialogConstr", u"Cs (pF)", None))
        self.label_13.setText(QCoreApplication.translate("DialogConstr", u"Cp (pF)", None))
        self.Cg9pF.setText(QCoreApplication.translate("DialogConstr", u"Cg (pF)", None))
        self.label_14.setText(QCoreApplication.translate("DialogConstr", u"C\u221e (pF)", None))
        self.label_15.setText(QCoreApplication.translate("DialogConstr", u"CeffG (pF)", None))
        self.label_16.setText(QCoreApplication.translate("DialogConstr", u"Ceff_Ug (pF)", None))
        self.label_temp_norma.setText(QCoreApplication.translate("DialogConstr", u"Temp. Icc pela norma IEC", None))
        self.pesoTotalKgLabel.setText(QCoreApplication.translate("DialogConstr", u"Peso total (kg)", None))
        self.custoTotalRLabel.setText(QCoreApplication.translate("DialogConstr", u"Custo total (R$)", None))
        self.pesoTotalDoCondutorKgLabel.setText(QCoreApplication.translate("DialogConstr", u"Peso condutor (kg)", None))
        self.pesoDaFibraKgLabel.setText(QCoreApplication.translate("DialogConstr", u"Peso da fibra (kg)", None))
        self.pesoDasCruzetasKgLabel.setText(QCoreApplication.translate("DialogConstr", u"Peso das cruzetas (kg)", None))
        self.checkBoxAutoTurn.setText(QCoreApplication.translate("DialogConstr", u"Auto Espira", None))
        self.checkBoxHe.setText(QCoreApplication.translate("DialogConstr", u"Auto Altura", None))
        self.bt_Del_Cil.setText(QCoreApplication.translate("DialogConstr", u"Delete cilindros", None))
        self.bt_ins_cil.setText(QCoreApplication.translate("DialogConstr", u"Insert Cilindro", None))
        self.bt_inicial.setText(QCoreApplication.translate("DialogConstr", u"Inicial", None))
        self.btn_Ok.setText(QCoreApplication.translate("DialogConstr", u"Ok", None))
        self.btnFreeCad.setText(QCoreApplication.translate("DialogConstr", u"FreeCad", None))
        self.cB_FC_model.setText(QCoreApplication.translate("DialogConstr", u"Freecad com enrolamentos", None))
        self.pbObs.setText(QCoreApplication.translate("DialogConstr", u"Observa\u00e7\u00f5es", None))
        self.pushButtonCalc.setText(QCoreApplication.translate("DialogConstr", u"Gravar calculado", None))
        self.pushButtonAsBuilt.setText(QCoreApplication.translate("DialogConstr", u"Ler construido", None))
        self.btEmpilhado.setText(QCoreApplication.translate("DialogConstr", u"Indut\u00e2ncia e For\u00e7a empilhado", None))
        self.btn_calc.setText(QCoreApplication.translate("DialogConstr", u"Calcular", None))
        self.btForce.setText(QCoreApplication.translate("DialogConstr", u"For\u00e7a Lado a Lado", None))
        self.pbCriar.setText(QCoreApplication.translate("DialogConstr", u"Criar documentos", None))
        self.pbHibrido.setText(QCoreApplication.translate("DialogConstr", u"Hibrido Indut\u00e2ncia & For\u00e7a", None))
        self.pbQRing.setText(QCoreApplication.translate("DialogConstr", u"QRings For\u00e7as", None))
    # retranslateUi

