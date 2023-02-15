# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Force_Side_by_Side.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_DialogForceIcc(object):
    def setupUi(self, DialogForceIcc):
        if not DialogForceIcc.objectName():
            DialogForceIcc.setObjectName(u"DialogForceIcc")
        DialogForceIcc.resize(430, 440)
        self.verticalLayout = QVBoxLayout(DialogForceIcc)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DialogForceIcc)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.cbMontagem = QComboBox(DialogForceIcc)
        self.cbMontagem.addItem("")
        self.cbMontagem.addItem("")
        self.cbMontagem.addItem("")
        self.cbMontagem.addItem("")
        self.cbMontagem.setObjectName(u"cbMontagem")
        self.cbMontagem.setEditable(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.cbMontagem)

        self.label_6 = QLabel(DialogForceIcc)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_6)

        self.cbEmpilhar = QComboBox(DialogForceIcc)
        self.cbEmpilhar.addItem("")
        self.cbEmpilhar.addItem("")
        self.cbEmpilhar.setObjectName(u"cbEmpilhar")
        self.cbEmpilhar.setEditable(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.cbEmpilhar)

        self.label_2 = QLabel(DialogForceIcc)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.cbIsolador = QComboBox(DialogForceIcc)
        self.cbIsolador.setObjectName(u"cbIsolador")
        self.cbIsolador.setEditable(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.cbIsolador)

        self.label_4 = QLabel(DialogForceIcc)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_4)

        self.dbH_isol = QDoubleSpinBox(DialogForceIcc)
        self.dbH_isol.setObjectName(u"dbH_isol")
        self.dbH_isol.setDecimals(1)
        self.dbH_isol.setMaximum(50000.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.dbH_isol)

        self.label_3 = QLabel(DialogForceIcc)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_3)

        self.intQutIsol = QSpinBox(DialogForceIcc)
        self.intQutIsol.setObjectName(u"intQutIsol")
        self.intQutIsol.setMinimum(1)
        self.intQutIsol.setMaximum(16)

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.intQutIsol)

        self.label_5 = QLabel(DialogForceIcc)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_5)

        self.dbH_Pedestal = QDoubleSpinBox(DialogForceIcc)
        self.dbH_Pedestal.setObjectName(u"dbH_Pedestal")
        self.dbH_Pedestal.setDecimals(1)
        self.dbH_Pedestal.setMaximum(5000.000000000000000)

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.dbH_Pedestal)

        self.label_7 = QLabel(DialogForceIcc)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_7)

        self.dbEixos = QDoubleSpinBox(DialogForceIcc)
        self.dbEixos.setObjectName(u"dbEixos")
        self.dbEixos.setDecimals(1)
        self.dbEixos.setMaximum(10000.000000000000000)

        self.formLayout.setWidget(7, QFormLayout.FieldRole, self.dbEixos)

        self.label_8 = QLabel(DialogForceIcc)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_8)

        self.dbCentro = QDoubleSpinBox(DialogForceIcc)
        self.dbCentro.setObjectName(u"dbCentro")
        self.dbCentro.setDecimals(1)
        self.dbCentro.setMaximum(10000.000000000000000)

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.dbCentro)

        self.label_9 = QLabel(DialogForceIcc)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_9)

        self.dbRadialForce = QDoubleSpinBox(DialogForceIcc)
        self.dbRadialForce.setObjectName(u"dbRadialForce")
        self.dbRadialForce.setDecimals(1)
        self.dbRadialForce.setMaximum(100000.000000000000000)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.dbRadialForce)

        self.label_10 = QLabel(DialogForceIcc)
        self.label_10.setObjectName(u"label_10")

        self.formLayout.setWidget(10, QFormLayout.LabelRole, self.label_10)

        self.dbAxialForce = QDoubleSpinBox(DialogForceIcc)
        self.dbAxialForce.setObjectName(u"dbAxialForce")
        self.dbAxialForce.setDecimals(1)
        self.dbAxialForce.setMaximum(10000.000000000000000)

        self.formLayout.setWidget(10, QFormLayout.FieldRole, self.dbAxialForce)

        self.label_11 = QLabel(DialogForceIcc)
        self.label_11.setObjectName(u"label_11")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_11)

        self.dbFlexao = QDoubleSpinBox(DialogForceIcc)
        self.dbFlexao.setObjectName(u"dbFlexao")
        self.dbFlexao.setDecimals(1)
        self.dbFlexao.setMaximum(10000.000000000000000)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.dbFlexao)

        self.pbCalcular = QPushButton(DialogForceIcc)
        self.pbCalcular.setObjectName(u"pbCalcular")

        self.formLayout.setWidget(13, QFormLayout.FieldRole, self.pbCalcular)

        self.label_12 = QLabel(DialogForceIcc)
        self.label_12.setObjectName(u"label_12")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_12)

        self.dbDiamCirc = QDoubleSpinBox(DialogForceIcc)
        self.dbDiamCirc.setObjectName(u"dbDiamCirc")
        self.dbDiamCirc.setDecimals(1)
        self.dbDiamCirc.setMaximum(9999.899999999999636)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.dbDiamCirc)

        self.doubleSpinBox = QDoubleSpinBox(DialogForceIcc)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")

        self.formLayout.setWidget(12, QFormLayout.FieldRole, self.doubleSpinBox)

        self.label_13 = QLabel(DialogForceIcc)
        self.label_13.setObjectName(u"label_13")

        self.formLayout.setWidget(12, QFormLayout.LabelRole, self.label_13)


        self.verticalLayout.addLayout(self.formLayout)

        QWidget.setTabOrder(self.cbMontagem, self.cbEmpilhar)
        QWidget.setTabOrder(self.cbEmpilhar, self.cbIsolador)
        QWidget.setTabOrder(self.cbIsolador, self.dbDiamCirc)
        QWidget.setTabOrder(self.dbDiamCirc, self.dbH_isol)
        QWidget.setTabOrder(self.dbH_isol, self.intQutIsol)
        QWidget.setTabOrder(self.intQutIsol, self.dbH_Pedestal)
        QWidget.setTabOrder(self.dbH_Pedestal, self.dbEixos)
        QWidget.setTabOrder(self.dbEixos, self.dbCentro)
        QWidget.setTabOrder(self.dbCentro, self.dbRadialForce)
        QWidget.setTabOrder(self.dbRadialForce, self.dbAxialForce)
        QWidget.setTabOrder(self.dbAxialForce, self.dbFlexao)
        QWidget.setTabOrder(self.dbFlexao, self.pbCalcular)

        self.retranslateUi(DialogForceIcc)

        QMetaObject.connectSlotsByName(DialogForceIcc)
    # setupUi

    def retranslateUi(self, DialogForceIcc):
        DialogForceIcc.setWindowTitle(QCoreApplication.translate("DialogForceIcc", u"For\u00e7a de curto-circuito lado a lad e vento", None))
        self.label.setText(QCoreApplication.translate("DialogForceIcc", u"Montagem", None))
        self.cbMontagem.setItemText(0, QCoreApplication.translate("DialogForceIcc", u"Tr\u00edf\u00e1sico lado a lado ", None))
        self.cbMontagem.setItemText(1, QCoreApplication.translate("DialogForceIcc", u"Trif\u00e1sico tr\u00e2ngular", None))
        self.cbMontagem.setItemText(2, QCoreApplication.translate("DialogForceIcc", u"Bif\u00e1sico", None))
        self.cbMontagem.setItemText(3, QCoreApplication.translate("DialogForceIcc", u"S\u00e9rie/Paralelo", None))

        self.label_6.setText(QCoreApplication.translate("DialogForceIcc", u"Empilhamento", None))
        self.cbEmpilhar.setItemText(0, QCoreApplication.translate("DialogForceIcc", u"Reator - Sapata - Isolador - Pedestal", None))
        self.cbEmpilhar.setItemText(1, QCoreApplication.translate("DialogForceIcc", u"Reator - Sapata - Pedestal -Isolador", None))

        self.label_2.setText(QCoreApplication.translate("DialogForceIcc", u"Isolador", None))
        self.label_4.setText(QCoreApplication.translate("DialogForceIcc", u"Altura Isolador (mm)", None))
        self.label_3.setText(QCoreApplication.translate("DialogForceIcc", u"Quantidade", None))
        self.label_5.setText(QCoreApplication.translate("DialogForceIcc", u"Altura do pedestal (mm)", None))
        self.label_7.setText(QCoreApplication.translate("DialogForceIcc", u"Dist\u00e2ncia entre eixos (mm)", None))
        self.label_8.setText(QCoreApplication.translate("DialogForceIcc", u"Dist\u00e2ncia entre centros (mm)", None))
        self.label_9.setText(QCoreApplication.translate("DialogForceIcc", u"For\u00e7a radial entre reatrores (kN) ", None))
        self.label_10.setText(QCoreApplication.translate("DialogForceIcc", u"For\u00e7a axial entre reatroes (kN)", None))
        self.label_11.setText(QCoreApplication.translate("DialogForceIcc", u"Rea\u00e7\u00e3o Flex\u00e3o na cabe\u00e7a do isolador (kN)", None))
        self.pbCalcular.setText(QCoreApplication.translate("DialogForceIcc", u"Calcular", None))
        self.label_12.setText(QCoreApplication.translate("DialogForceIcc", u"Di\u00e2mentro do circulo dos isoladores", None))
        self.label_13.setText(QCoreApplication.translate("DialogForceIcc", u"Rea\u00e7\u00e3o na funda\u00e7\u00e3o (kN)", None))
    # retranslateUi

