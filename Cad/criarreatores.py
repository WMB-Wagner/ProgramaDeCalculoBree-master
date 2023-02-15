import FreeCAD as App
import FreeCADGui
import Part
import sys
#import PartGui
import math
import Shapes
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtGui, QtCore
#from BasicShapes import Shapes

doc = App.activeDocument()
n = list()
raiomiolo = 51


class Ui_BreeCad(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(508, 436)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mdiArea = QtGui.QMdiArea(self.centralwidget)
        self.mdiArea.setViewMode(QtGui.QMdiArea.TabbedView)
        self.mdiArea.setTabPosition(QtGui.QTabWidget.South)
        self.mdiArea.setObjectName("mdiArea")
        self.gridLayout.addWidget(self.mdiArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 27))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate(
            "MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))


def clearAll():
    doc = App.ActiveDocument
    for obj in doc.Objects:
        doc.removeObject(obj.Label)


def criarcilindros(diamint, espessuracil, diamesp, numcil, altura):
    for x in range(numcil):
        tube = Shapes.addTube(App.ActiveDocument, "Cilindro")
        tube.Height = altura
        tube.InnerRadius = diamint + espessuracil*x + x*diamesp
        tube.OuterRadius = diamint + espessuracil*(x+1) + x*diamesp
        tube.Placement = App.Placement(
            App.Vector(0, 0, 0), App.Rotation(0, 0, 0))
        doc.recompute()


def criarcruzeta(alturacruzpol, espessurabraco, compbraco, numbracos, alturart):
    # cruzeta inferior
    tube = Shapes.addTube(App.ActiveDocument, "CruzInfMiolo")
    tube.Height = alturacruzpol*25.4
    tube.InnerRadius = 22
    tube.OuterRadius = 81
    tube.Placement = App.Placement(App.Vector(
        0, 0, (-alturacruzpol*25.4)), App.Rotation(0, 0, 0))
    doc.recompute()
    for x in range(numbracos):
        box = doc.addObject("Part::Box", "CruzInfBraco")
        box.Length = compbraco
        box.Width = espessurabraco
        box.Height = alturacruzpol*25.4
        anguloentrebracos = math.radians(360/numbracos)
        xrel = math.cos(anguloentrebracos*x -
                        math.atan(espessurabraco/(2*raiomiolo)))*raiomiolo
        yrel = math.sin(anguloentrebracos*x -
                        math.atan(espessurabraco/(2*raiomiolo)))*raiomiolo
        box.Placement = App.Placement(App.Vector(
            xrel, yrel, (-alturacruzpol*25.4)), App.Rotation((360/numbracos)*x, 0, 0))
        doc.recompute()
    # cruzeta superior
    tube = Shapes.addTube(App.ActiveDocument, "CruzSupMiolo")
    tube.Height = alturacruzpol*25.4
    tube.InnerRadius = 22
    tube.OuterRadius = 81
    tube.Placement = App.Placement(App.Vector(
        0, 0, alturart), App.Rotation(0, 0, 0))
    doc.recompute()
    for x in range(numbracos):
        box = doc.addObject("Part::Box", "CruzSupBraco")
        box.Length = compbraco
        box.Width = espessurabraco
        box.Height = alturacruzpol*25.4
        anguloentrebracos = math.radians(360/numbracos)
        xrel = math.cos(anguloentrebracos*x -
                        math.atan(espessurabraco/(2*raiomiolo)))*raiomiolo
        yrel = math.sin(anguloentrebracos*x -
                        math.atan(espessurabraco/(2*raiomiolo)))*raiomiolo
        box.Placement = App.Placement(App.Vector(
            xrel, yrel, alturart), App.Rotation((360/numbracos)*x, 0, 0))
        doc.recompute()


def criarterminal(compbraco, espessurabraco, alturacruzpol, numbracos, postermsup, posterminf, compterminal, altura, espessuracil, diamint, diamesp, numcil):
    anguloentrebracos = math.radians(360/numbracos)
    # terminal superior
    box = doc.addObject("Part::Box", "CruzSupTerminal")
    box.Length = compterminal
    box.Width = espessurabraco
    box.Height = alturacruzpol*25.4
    anguloentrebracos = math.radians(360/numbracos)
    raiobraco = raiomiolo + diamint + \
        espessuracil*(numcil-1)+(numcil-1)*diamesp
    xrel = math.cos(anguloentrebracos*postermsup -
                    math.atan(espessurabraco/(2*raiobraco)))*raiobraco
    yrel = math.sin(anguloentrebracos*postermsup -
                    math.atan(espessurabraco/(2*raiobraco)))*raiobraco
    box.Placement = App.Placement(App.Vector(
        xrel, yrel, altura), App.Rotation((360/numbracos)*postermsup, 0, 0))
    doc.recompute()
    # terminal inferior
    box = doc.addObject("Part::Box", "CruzSupTerminal")
    box.Length = compterminal
    box.Width = espessurabraco
    box.Height = alturacruzpol*25.4
    anguloentrebracos = math.radians(360/numbracos)
    raiobraco = raiomiolo + diamint + \
        espessuracil*(numcil-1)+(numcil-1)*diamesp
    xrel = math.cos(anguloentrebracos*posterminf -
                    math.atan(espessurabraco/(2*raiobraco)))*raiobraco
    yrel = math.sin(anguloentrebracos*posterminf -
                    math.atan(espessurabraco/(2*raiobraco)))*raiobraco
    box.Placement = App.Placement(App.Vector(
        xrel, yrel, (-alturacruzpol*25.4)), App.Rotation((360/numbracos)*posterminf, 0, 0))
    doc.recompute()


def criarsapata(diamfundacao, alturasapata, ladosapata, numbracos, alturacruzpol, numsapatas, altura, sapatasup):
    # sapata inferior
    for x in range(numsapatas):
        box = doc.addObject("Part::Box", "SapataInf")
        box.Length = ladosapata
        box.Width = ladosapata
        box.Height = alturasapata
        anguloentrebracos = math.radians(360/numbracos)
        raiobraco = diamfundacao/2
        xrel = math.cos(anguloentrebracos*x -
                        math.atan(ladosapata/(2*raiobraco)))*raiobraco
        yrel = math.sin(anguloentrebracos*x -
                        math.atan(ladosapata/(2*raiobraco)))*raiobraco
        box.Placement = App.Placement(App.Vector(
            xrel, yrel, (-alturacruzpol*25.4-alturasapata)), App.Rotation((360/numbracos)*x, 0, 0))
        doc.recompute()
    # sapata superior
    if (sapatasup == 1):
        for x in range(numsapatas):
            box = doc.addObject("Part::Box", "SapataSup")
            box.Length = ladosapata
            box.Width = ladosapata
            box.Height = alturasapata
            anguloentrebracos = math.radians(360/numbracos)
            raiobraco = diamfundacao/2
            xrel = math.cos(anguloentrebracos*x -
                            math.atan(ladosapata/(2*raiobraco)))*raiobraco
            yrel = math.sin(anguloentrebracos*x -
                            math.atan(ladosapata/(2*raiobraco)))*raiobraco
            box.Placement = App.Placement(App.Vector(
                xrel, yrel, (altura+alturacruzpol*25.4)), App.Rotation((360/numbracos)*x, 0, 0))
            doc.recompute()


def criarpedestal(pedestal, diamfundacao, alturasapata, ladosapata, numbracos, alturacruzpol, numsapatas, altura, sapatasup, espessurabraco, alturapedestal, numsaias):
    if (pedestal == 1):
        alturaisolador = -2*alturasapata-10+80+40*numsaias
        zpedestal = alturacruzpol*25.4+2*alturasapata+alturapedestal+alturaisolador
        # pedestal inferior
        for x in range(numsapatas):
            # parte superior
            box = doc.addObject("Part::Box", "PedestalInf-superior")
            box.Length = ladosapata
            box.Width = ladosapata
            box.Height = alturasapata
            anguloentrebracos = math.radians(360/numbracos)
            raiobraco = diamfundacao/2
            xrel = math.cos(anguloentrebracos*x -
                            math.atan(ladosapata/(2*raiobraco)))*raiobraco
            yrel = math.sin(anguloentrebracos*x -
                            math.atan(ladosapata/(2*raiobraco)))*raiobraco
            box.Placement = App.Placement(App.Vector(
                xrel, yrel, -zpedestal+alturapedestal), App.Rotation((360/numbracos)*x, 0, 0))
            doc.recompute()
            # parte central
            box = doc.addObject("Part::Box", "PedestalInf-central")
            box.Length = espessurabraco
            box.Width = ladosapata-espessurabraco/2
            box.Height = alturapedestal-2*alturasapata
            anguloentrebracos = math.radians(360/numbracos)
            raiobraco = (diamfundacao+ladosapata-espessurabraco)/2
            xrel = math.cos(
                anguloentrebracos*x-math.atan((ladosapata-espessurabraco/2)/(2*raiobraco)))*raiobraco
            yrel = math.sin(
                anguloentrebracos*x-math.atan((ladosapata-espessurabraco/2)/(2*raiobraco)))*raiobraco
            box.Placement = App.Placement(App.Vector(
                xrel, yrel, -zpedestal+2*alturasapata), App.Rotation((360/numbracos)*x, 0, 0))
            doc.recompute()
            # parte lateral direita
            box = doc.addObject("Part::Box", "PedestalInf-esquerda")
            box.Length = ladosapata
            box.Width = espessurabraco
            box.Height = alturapedestal-2*alturasapata
            anguloentrebracos = math.radians(360/numbracos)
            raiobraco = diamfundacao/2
            xrel = math.cos(anguloentrebracos*x -
                            math.atan((ladosapata)/(2*raiobraco)))*raiobraco
            yrel = math.sin(anguloentrebracos*x -
                            math.atan((ladosapata)/(2*raiobraco)))*raiobraco
            box.Placement = App.Placement(App.Vector(
                xrel, yrel, -zpedestal+2*alturasapata), App.Rotation((360/numbracos)*x, 0, 0))
            doc.recompute()
            # parte lateral esquerda
            box = doc.addObject("Part::Box", "PedestalInf-direita")
            box.Length = ladosapata
            box.Width = espessurabraco+1.28
            box.Height = alturapedestal-2*alturasapata
            anguloentrebracos = math.radians(360/numbracos)
            raiobraco = (diamfundacao-3.8)/2
            xrel = math.cos(
                anguloentrebracos*x-math.atan((-ladosapata+2*espessurabraco)/(2*raiobraco)))*raiobraco
            yrel = math.sin(
                anguloentrebracos*x-math.atan((-ladosapata+2*espessurabraco)/(2*raiobraco)))*raiobraco
            box.Placement = App.Placement(App.Vector(
                xrel, yrel, -zpedestal+2*alturasapata), App.Rotation((360/numbracos)*x, 0, 0))
            doc.recompute()
            # parte inferior
            box = doc.addObject("Part::Box", "PedestalInf-inferior")
            box.Length = ladosapata
            box.Width = ladosapata
            box.Height = alturasapata
            anguloentrebracos = math.radians(360/numbracos)
            raiobraco = diamfundacao/2
            xrel = math.cos(anguloentrebracos*x -
                            math.atan(ladosapata/(2*raiobraco)))*raiobraco
            yrel = math.sin(anguloentrebracos*x -
                            math.atan(ladosapata/(2*raiobraco)))*raiobraco
            box.Placement = App.Placement(App.Vector(
                xrel, yrel, -zpedestal+alturasapata), App.Rotation((360/numbracos)*x, 0, 0))
            doc.recompute()
        # pedestal superior
        if (sapatasup == 1):
            for x in range(numsapatas):
                zpedestal = alturacruzpol*25.4+alturasapata
                # parte inferior
                box = doc.addObject("Part::Box", "PedestalSup-inferior")
                box.Length = ladosapata
                box.Width = ladosapata
                box.Height = alturasapata
                anguloentrebracos = math.radians(360/numbracos)
                raiobraco = diamfundacao/2
                xrel = math.cos(anguloentrebracos*x -
                                math.atan(ladosapata/(2*raiobraco)))*raiobraco
                yrel = math.sin(anguloentrebracos*x -
                                math.atan(ladosapata/(2*raiobraco)))*raiobraco
                box.Placement = App.Placement(App.Vector(
                    xrel, yrel, altura+zpedestal), App.Rotation((360/numbracos)*x, 0, 0))
                doc.recompute()
                # parte central
                box = doc.addObject("Part::Box", "PedestalSup-central")
                box.Length = espessurabraco
                box.Width = ladosapata-espessurabraco/2
                box.Height = alturapedestal-2*alturasapata
                anguloentrebracos = math.radians(360/numbracos)
                raiobraco = (diamfundacao+ladosapata-espessurabraco)/2
                xrel = math.cos(
                    anguloentrebracos*x-math.atan((ladosapata-espessurabraco/2)/(2*raiobraco)))*raiobraco
                yrel = math.sin(
                    anguloentrebracos*x-math.atan((ladosapata-espessurabraco/2)/(2*raiobraco)))*raiobraco
                box.Placement = App.Placement(App.Vector(
                    xrel, yrel, altura+zpedestal), App.Rotation((360/numbracos)*x, 0, 0))
                doc.recompute()
                # parte lateral direita
                box = doc.addObject("Part::Box", "PedestalSup-esquerda")
                box.Length = ladosapata
                box.Width = espessurabraco
                box.Height = alturapedestal-2*alturasapata
                anguloentrebracos = math.radians(360/numbracos)
                raiobraco = diamfundacao/2
                xrel = math.cos(anguloentrebracos*x -
                                math.atan((ladosapata)/(2*raiobraco)))*raiobraco
                yrel = math.sin(anguloentrebracos*x -
                                math.atan((ladosapata)/(2*raiobraco)))*raiobraco
                box.Placement = App.Placement(App.Vector(
                    xrel, yrel, altura+zpedestal), App.Rotation((360/numbracos)*x, 0, 0))
                doc.recompute()
                # parte lateral esquerda
                box = doc.addObject("Part::Box", "PedestalSup-direita")
                box.Length = ladosapata
                box.Width = espessurabraco+1.28
                box.Height = alturapedestal-2*alturasapata
                anguloentrebracos = math.radians(360/numbracos)
                raiobraco = (diamfundacao-3.8)/2
                xrel = math.cos(
                    anguloentrebracos*x-math.atan((-ladosapata+2*espessurabraco)/(2*raiobraco)))*raiobraco
                yrel = math.sin(
                    anguloentrebracos*x-math.atan((-ladosapata+2*espessurabraco)/(2*raiobraco)))*raiobraco
                box.Placement = App.Placement(App.Vector(
                    xrel, yrel, altura+zpedestal), App.Rotation((360/numbracos)*x, 0, 0))
                doc.recompute()
                # parte superior
                box = doc.addObject("Part::Box", "PedestalSup-superior")
                box.Length = ladosapata
                box.Width = ladosapata
                box.Height = alturasapata
                anguloentrebracos = math.radians(360/numbracos)
                raiobraco = diamfundacao/2
                xrel = math.cos(anguloentrebracos*x -
                                math.atan(ladosapata/(2*raiobraco)))*raiobraco
                yrel = math.sin(anguloentrebracos*x -
                                math.atan(ladosapata/(2*raiobraco)))*raiobraco
                box.Placement = App.Placement(App.Vector(
                    xrel, yrel, altura+zpedestal+alturapedestal-2*alturasapata), App.Rotation((360/numbracos)*x, 0, 0))
                doc.recompute()


def criarespacadores(diamesp, altura, numbracos, espessurabraco, numcil, diamint, espessuracil):
    numespacadores = numbracos*int((360/numbracos)/10)
    for y in range(numcil-1):
        for x in range(numespacadores):
            cylinder = doc.addObject("Part::Cylinder", "Espacador")
            cylinder.Radius = diamesp/2
            cylinder.Height = altura
            anguloentrebracos = math.radians(360/numbracos)
            anguloentreespacadores = math.radians(360/numespacadores)
            xrel = math.cos(anguloentreespacadores*x-math.atan(espessurabraco/(2*raiomiolo)))*(
                diamint+diamesp*(y+1)-(0.55*diamesp)+espessuracil*(y+1))
            yrel = math.sin(anguloentreespacadores*x-math.atan(espessurabraco/(2*raiomiolo)))*(
                diamint+diamesp*(y+1)-(0.55*diamesp)+espessuracil*(y+1))
            cylinder.Placement = App.Placement(App.Vector(
                xrel, yrel, 0), App.Rotation((360/numespacadores)*x, 0, 0))
            doc.recompute()


def criaranelanticorona(altura, diamint, espessuracil, numcil, diamesp, anel, posterminf, postermsup, numbracos):
    if (anel == 1):
        # anel superior
        torus = doc.addObject("Part::Torus", "myTorus")
        torus.Radius1 = (diamint)+espessuracil*(numcil+1)+(numcil+1)*diamesp
        torus.Radius2 = 76.2/2
        torus.Angle1 = -180
        torus.Angle2 = 180
        torus.Angle3 = 330
        torus.Placement = App.Placement(App.Vector(
            0, 0, altura+30), App.Rotation(15+(360/numbracos)*postermsup, 0, 0))
        doc.recompute()
        # anel inferior
        torus = doc.addObject("Part::Torus", "myTorus")
        torus.Radius1 = (diamint)+espessuracil*(numcil+1)+(numcil+1)*diamesp
        torus.Radius2 = 76.2/2
        torus.Angle1 = -180
        torus.Angle2 = 180
        torus.Angle3 = 330
        torus.Placement = App.Placement(App.Vector(
            0, 0, 0), App.Rotation(15+(360/numbracos)*posterminf, 0, 0))
        doc.recompute()


def criarisolador(numbracos, espessurabraco, raiomiolo, diamfundacao, altura, diamsaia, numsaias, espessuracil, alturasapata, alturacruzpol, ladosapata):
    for y in range(numbracos):
        for x in range(numsaias):
            # Saia isolador
            cylinder = doc.addObject("Part::Cylinder", "SaiaIsolador")
            cylinder.Radius = diamsaia
            cylinder.Height = 20
            anguloentrebracos = math.radians(360/numbracos)
            xrel = math.cos(anguloentrebracos*y)*(diamfundacao/2+ladosapata/2)
            yrel = math.sin(anguloentrebracos*y)*(diamfundacao/2+ladosapata/2)
            cylinder.Placement = App.Placement(App.Vector(
                xrel, yrel, -(alturacruzpol*25.4+3*alturasapata+40)-40*x), App.Rotation((360/numbracos)*y, 0, 0))
            doc.recompute()
            # Tubo interno
            if (x < numsaias-1):
                cylinder = doc.addObject("Part::Cylinder", "TuboIsolador")
                cylinder.Radius = diamsaia/2
                cylinder.Height = 20
                anguloentrebracos = math.radians(360/numbracos)
                cylinder.Placement = App.Placement(App.Vector(
                    xrel, yrel, -(alturacruzpol*25.4+3*alturasapata+40)-40*x-20), App.Rotation((360/numbracos)*y, 0, 0))
                doc.recompute()
            # contorno lateral da saia
            torus = doc.addObject("Part::Torus", "ArestaSaia")
            torus.Radius1 = diamsaia
            torus.Radius2 = 10
            torus.Angle1 = -180
            torus.Angle2 = 180
            torus.Angle3 = 360
            torus.Placement = App.Placement(App.Vector(
                xrel, yrel, -(alturacruzpol*25.4+3*alturasapata-10+40)-40*x), App.Rotation((360/numbracos)*y, 0, 0))
            doc.recompute()
        # Apoio superior
        cylinder = doc.addObject("Part::Cylinder", "ApoioSuperior")
        cylinder.Radius = diamsaia*0.6
        cylinder.Height = 40
        anguloentrebracos = math.radians(360/numbracos)
        cylinder.Placement = App.Placement(App.Vector(
            xrel, yrel, -(alturacruzpol*25.4+3*alturasapata)-20), App.Rotation((360/numbracos)*y, 0, 0))
        doc.recompute()
        # Apoio inferior
        cylinder = doc.addObject("Part::Cylinder", "ApoioInferior")
        cylinder.Radius = diamsaia*0.6
        cylinder.Height = 40
        anguloentrebracos = math.radians(360/numbracos)
        cylinder.Placement = App.Placement(App.Vector(
            xrel, yrel, -(alturacruzpol*25.4+3*alturasapata-10+80)-40*x), App.Rotation((360/numbracos)*y, 0, 0))
        doc.recompute()


def criarsemiesferas(altura, alturacruzpol, espessurabraco, diamint, espessuracil, numcil, diamesp, numbracos, posterminf, postermsup, semiesfera, diamsemiesferapol):
    if (semiesfera == 1):
        # Semi esfera inferior
        for x in range(numbracos):
            if (x != posterminf):
                sphere = doc.addObject("Part::Sphere", "SemiEsferaInf")
                sphere.Radius = diamsemiesferapol*25.4/2
                sphere.Angle1 = -90
                sphere.Angle2 = 90
                sphere.Angle3 = 180
                anguloentrebracos = math.radians(360/numbracos)
                raio = (diamint)+espessuracil*(numcil-1) + \
                    (numcil-1)*diamesp+raiomiolo
                xrel = math.cos(anguloentrebracos*x -
                                math.atan(espessurabraco*0.25/(2*raio)))*raio
                yrel = math.sin(anguloentrebracos*x -
                                math.atan(espessurabraco*0.25/(2*raio)))*raio
                sphere.Placement = App.Placement(App.Vector(
                    xrel, yrel, -alturacruzpol*25.4/2), App.Rotation(-90+((360/numbracos)*(x)), 0, 0))
                doc.recompute()
        # Semi esfera superior
        for x in range(numbracos):
            if (x != postermsup):
                sphere = doc.addObject("Part::Sphere", "SemiEsferaSup")
                sphere.Radius = diamsemiesferapol*25.4/2
                sphere.Angle1 = -90
                sphere.Angle2 = 90
                sphere.Angle3 = 180
                anguloentrebracos = math.radians(360/numbracos)
                raio = (diamint)+espessuracil*(numcil-1) + \
                    (numcil-1)*diamesp+raiomiolo
                xrel = math.cos(anguloentrebracos*x -
                                math.atan(espessurabraco*0.25/(2*raio)))*raio
                yrel = math.sin(anguloentrebracos*x -
                                math.atan(espessurabraco*0.25/(2*raio)))*raio
                sphere.Placement = App.Placement(App.Vector(
                    xrel, yrel, altura + alturacruzpol*25.4/2), App.Rotation(-90+((360/numbracos)*(x)), 0, 0))
                doc.recompute()


def criarreator(diamint, espessuracil, diamesp, numcil, altura, alturacruzpol, espessurabraco, numbracos, postermsup, posterminf, compterminal, diamfundacao, alturasapata, ladosapata, numsapatas, sapatasup, alturapedestal, pedestal, anel, diamsaia, numsaias, semiesfera, diamsemiesferapol):
    criarcilindros(diamint, espessuracil, diamesp, numcil, altura)
    criarcruzeta(alturacruzpol, espessurabraco, (diamint) +
                 espessuracil*(numcil-1)+(numcil-1)*diamesp, numbracos, altura)
    criarterminal((diamint)+espessuracil*(numcil-1)+(numcil-1)*diamesp, espessurabraco, alturacruzpol,
                  numbracos, postermsup, posterminf, compterminal, altura, espessuracil, diamint, diamesp, numcil)
    criarsapata(diamfundacao, alturasapata, ladosapata, numbracos,
                alturacruzpol, numsapatas, altura, sapatasup)
    criarpedestal(pedestal, diamfundacao, alturasapata, ladosapata, numbracos, alturacruzpol,
                  numsapatas, altura, sapatasup, espessurabraco, alturapedestal, numsaias)
    criarespacadores(diamesp, altura, numbracos,
                     espessurabraco, numcil, diamint, espessuracil)
    criaranelanticorona(altura, diamint, espessuracil, numcil,
                        diamesp, anel, posterminf, postermsup, numbracos)
    criarisolador(numbracos, espessurabraco, raiomiolo, diamfundacao, altura,
                  diamsaia, numsaias, espessuracil, alturasapata, alturacruzpol, ladosapata)
    criarsemiesferas(altura, alturacruzpol, espessurabraco, diamint, espessuracil,
                     numcil, diamesp, numbracos, posterminf, postermsup, semiesfera, diamsemiesferapol)


if __name__ == "__main__":
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    FreeCADGui.showMainWindow()
    doc = App.newDocument()
    # box = Part.makeBox(100, 100, 100)
    # Part.show(box)
    clearAll()
    criarreator(500, 30, 19, 5, 1500, 2, 13, 10, 5, 0, 100,
                1000, 10, 120, 10, 0, 500, 1, 0, 80, 10, 1, 5)
    sys.exit(app.exec_())
# def desenharReator():
#     if __name__ == "Cad.criarreatores":
#         app = QApplication.instance()
#         if app is None:
#             app = QApplication(sys.argv)
#         FreeCADGui.showMainWindow()
#         doc = App.newDocument()
#         # box = Part.makeBox(100, 100, 100)
#         # Part.show(box)
#         clearAll()
#         criarreator(500, 30, 19, 5, 1500, 2, 13, 10, 5, 0, 100,
#                     1000, 10, 120, 10, 0, 500, 1, 0, 80, 10, 1, 5)
#         sys.exit(app.exec_())
