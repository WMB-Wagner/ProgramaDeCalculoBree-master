
import sys
# sys.path.append('C:/Program Files/FreeCAD 0.20/bin/')
# sys.path.append('C:/Program Files/FreeCAD 0.20/Mod/Part/BasicShapes/')
# sys.path.append('C:/Program Files/FreeCAD 0.20/Mod/Draft')
# sys.path.append('C:/Program Files/FreeCAD 0.20/bin/lib/')
# sys.path.append('C:/Program Files/FreeCAD 0.20/lib/')
# sys.path.append('C:/Program Files/FreeCAD 0.20/Mod/')
# sys.path.append('C:/Program Files/FreeCAD 0.20/Ex/')

import userpaths
freecad_path = userpaths.get_my_documents() 
FREECAD_CAD = freecad_path + "\\FreeCAD 0.20"
FREECAD_BIN = freecad_path+"\\FreeCAD 0.20\\bin"
FREECAD_BIN_LIB = freecad_path+"\\FreeCAD 0.20\\bin\\Lib"
FREECAD_LIB = freecad_path+"\\FreeCAD 0.20\\lib"
FREECAD_MOD = freecad_path+"\\FreeCAD 0.20\\Mod"
FREECAD_EXT = freecad_path+"\\FreeCAD 0.20\\Ext"
FREECAD_SHAPES = freecad_path+"\\FreeCAD 0.20\\Mod\\Part\\BasicShapes"

sys.path.append(FREECAD_CAD)
sys.path.append(FREECAD_BIN)
sys.path.append(FREECAD_BIN_LIB)
sys.path.append(FREECAD_LIB)
sys.path.append(FREECAD_MOD)
sys.path.append(FREECAD_EXT)
sys.path.append(FREECAD_SHAPES)

import Shapes
import Part
import FreeCADGui as Gui
import FreeCAD as App
import Draft
#from Mod.Draft.draftobjects.rectangle import Rectangle
import duckdb
from modulos import bree_reactor_core_1 as reactor
import pandas as pd
from PySide2 import QtGui, QtCore
from PySide2.QtWidgets import QApplication, QMainWindow
import math
#from FreeCADGui import Workbench
#import PartGui
con = duckdb.connect()
#from BasicShapes import Shapes


# class ScriptWorkbench (Workbench):
#     MenuText = "Scripts"

#     def Initialize(self):
#         import Scripts  # assuming Scripts.py is your module
#         # That list must contain command names, that can be defined in Scripts.py
#         list = ["Script_Cmd"]
#         self.appendToolbar("My Scripts", list)


class BreeCadReactor(object):
    # doc = App.activeDocument()
    # raiomiolo = 51

    def __init__(self, raiomiolo=51):
        self.raiomiolo = raiomiolo
        self.doc = App.activeDocument()        
        self.setupUi(self)
        


    def setupUi(self, MainWindow):        
        Gui.showMainWindow()
        

        app = App.newDocument()        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate(
            "MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))

    def clearAll(self):
        self.activ_doc = App.ActiveDocument
        for obj in self.activ_doc.Objects:
            self.doc.removeObject(obj.Label)
        self.group = App.ActiveDocument.addObject("App::DocumentObjectGroup", "Reator")      

    def criarcamada(self,raio,altura,diametrofioisol,numeroespiras):
        helix = self.activ_doc.addObject("Part::Helix", "HelicoideFio")
        helix.Pitch = diametrofioisol
        helix.Height = numeroespiras*diametrofioisol
        helix.Radius = raio
        helix.SegmentLength = 10
        helix.Angle = 0
        helix.Placement = App.Placement(App.Vector(0, 0,altura), App.Rotation(0, 0, 0))
        circle = self.activ_doc.addObject("Part::Circle", "Fio")
        circle.Radius = diametrofioisol/2
        circle.Angle1 = 0
        circle.Angle2 = 360
        circle.Placement = App.Placement(App.Vector(raio, 0, altura), App.Rotation(-90, 90, 0))
        sweep = self.activ_doc.addObject('Part::Sweep','SweepFio')
        sweep.Sections = circle
        sweep.Spine = helix
        sweep.Solid = True
        sweep.Frenet = True
    def criarperfil(self,raio=750.0,h1=1000.0,dbs1=1000,alturaperfil=13.0,larguraperfil=23,alturacalco=7.5,numerovoltas=10.0,
                    numentradas=1,DBST=10.0,posicao='Acima da cruzeta superior'):
        helix = self.activ_doc.addObject("Part::Helix", "myHelix")
        helix.Pitch = (alturaperfil + alturacalco)*numentradas
        helix.Height = numerovoltas*(alturaperfil + alturacalco)*numentradas
        helix.Radius = raio
        helix.SegmentLength = 0
        helix.Angle = 0
        if posicao == 'Acima da cruzeta superior':
            zc = h1+DBST
        elif posicao == 'Satetlite por baixo da cruzeta superior':
            zc = dbs1-DBST
        elif posicao == 'Satétile acima da cruzeta inferior':
            zc = DBST
        elif posicao == 'Abaixo da cruzeta inferior':
            zc = -DBST-h1-helix.Height
        helix.Placement = App.Placement(App.Vector(0, 0,zc), App.Rotation(0, 0, 0))   
        helix.Visibility = False     
        self.activ_doc.recompute()
        rectangle = Draft.make_rectangle(alturaperfil, larguraperfil, placement=App.Placement(App.Vector(raio, 0, 0), App.Rotation(-90, 90, 0)), face=True, support=None)
        rectangle.Visibility = False
        sweep = App.ActiveDocument.addObject('Part::Sweep','Sweep')
        sweep.Sections = rectangle
        sweep.Spine = helix
        sweep.Solid = True
        sweep.Frenet = True
        sweep.Placement = App.Placement(App.Vector(0, 0,zc), App.Rotation(0, 0, 0))
        self.group.addObjects([helix,rectangle,sweep])
        self.activ_doc.recompute()

    def criarcilindros(self, diamint, espessuracil, diamesp, numcil, altura):
        for x in range(numcil):
            tube = Shapes.addTube(App.ActiveDocument, "Cilindro")
            tube.Height = altura
            tube.InnerRadius = diamint + espessuracil*x + x*diamesp
            tube.OuterRadius = diamint + espessuracil*(x+1) + x*diamesp
            tube.Placement = App.Placement(
                App.Vector(0, 0, 0), App.Rotation(0, 0, 0))
            self.activ_doc.recompute()

    def criarcruzeta(self, alturacruzpol, espessurabraco, compbraco, numbracos, alturart):
        # cruzeta inferior
        tube = Shapes.addTube(App.ActiveDocument, "CruzInfMiolo")
        tube.Height = alturacruzpol*25.4
        tube.InnerRadius = 22
        tube.OuterRadius = 81
        tube.Placement = App.Placement(App.Vector(
            0, 0, (-alturacruzpol*25.4)), App.Rotation(0, 0, 0))
        self.activ_doc.recompute()
        for x in range(numbracos):
            box = self.activ_doc.addObject("Part::Box", "CruzInfBraco")
            box.Length = compbraco
            box.Width = espessurabraco
            box.Height = alturacruzpol*25.4
            anguloentrebracos = math.radians(360/numbracos)
            xrel = math.cos(anguloentrebracos*x -
                            math.atan(espessurabraco/(2*self.raiomiolo)))*self.raiomiolo
            yrel = math.sin(anguloentrebracos*x -
                            math.atan(espessurabraco/(2*self.raiomiolo)))*self.raiomiolo
            box.Placement = App.Placement(App.Vector(
                xrel, yrel, (-alturacruzpol*25.4)), App.Rotation((360/numbracos)*x, 0, 0))
            self.activ_doc.recompute()
        # cruzeta superior
        tube = Shapes.addTube(App.ActiveDocument, "CruzSupMiolo")
        tube.Height = alturacruzpol*25.4
        tube.InnerRadius = 22
        tube.OuterRadius = 81
        tube.Placement = App.Placement(App.Vector(
            0, 0, alturart), App.Rotation(0, 0, 0))
        self.activ_doc.recompute()
        for x in range(numbracos):
            box = self.activ_doc.addObject("Part::Box", "CruzSupBraco")
            box.Length = compbraco
            box.Width = espessurabraco
            box.Height = alturacruzpol*25.4
            anguloentrebracos = math.radians(360/numbracos)
            xrel = math.cos(anguloentrebracos*x -
                            math.atan(espessurabraco/(2*self.raiomiolo)))*self.raiomiolo
            yrel = math.sin(anguloentrebracos*x -
                            math.atan(espessurabraco/(2*self.raiomiolo)))*self.raiomiolo
            box.Placement = App.Placement(App.Vector(
                xrel, yrel, alturart), App.Rotation((360/numbracos)*x, 0, 0))
            self.activ_doc.recompute()

    def criarterminal(self, compbraco, espessurabraco, alturacruzpol, numbracos, postermsup, posterminf, compterminal, altura, espessuracil, diamint, diamesp, numcil):
        anguloentrebracos = math.radians(360/numbracos)
        # terminal superior
        box = self.activ_doc.addObject("Part::Box", "CruzSupTerminal")
        box.Length = compterminal
        box.Width = espessurabraco
        box.Height = alturacruzpol*25.4
        anguloentrebracos = math.radians(360/numbracos)
        raiobraco = self.raiomiolo + diamint + \
            espessuracil*(numcil-1)+(numcil-1)*diamesp
        xrel = math.cos(anguloentrebracos*postermsup -
                        math.atan(espessurabraco/(2*raiobraco)))*raiobraco
        yrel = math.sin(anguloentrebracos*postermsup -
                        math.atan(espessurabraco/(2*raiobraco)))*raiobraco
        box.Placement = App.Placement(App.Vector(
            xrel, yrel, altura), App.Rotation((360/numbracos)*postermsup, 0, 0))
        self.activ_doc.recompute()
        # terminal inferior
        box = self.activ_doc.addObject("Part::Box", "CruzSupTerminal")
        box.Length = compterminal
        box.Width = espessurabraco
        box.Height = alturacruzpol*25.4
        anguloentrebracos = math.radians(360/numbracos)
        raiobraco = self.raiomiolo + diamint + \
            espessuracil*(numcil-1)+(numcil-1)*diamesp
        xrel = math.cos(anguloentrebracos*posterminf -
                        math.atan(espessurabraco/(2*raiobraco)))*raiobraco
        yrel = math.sin(anguloentrebracos*posterminf -
                        math.atan(espessurabraco/(2*raiobraco)))*raiobraco
        box.Placement = App.Placement(App.Vector(
            xrel, yrel, (-alturacruzpol*25.4)), App.Rotation((360/numbracos)*posterminf, 0, 0))
        self.activ_doc.recompute()

    def criarsapata(self, diamfundacao, alturasapata, ladosapata, numbracos, alturacruzpol, numsapatas, altura, sapatasup):
        # sapata inferior
        for x in range(numsapatas):
            box = self.activ_doc.addObject("Part::Box", "SapataInf")
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
            self.activ_doc.recompute()
        # sapata superior
        if (sapatasup == 1):
            for x in range(numsapatas):
                box = self.activ_doc.addObject("Part::Box", "SapataSup")
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
                self.activ_doc.recompute()

    def criarpedestal(self, pedestal, diamfundacao, alturasapata, ladosapata, numbracos, alturacruzpol, numsapatas, altura, sapatasup, espessurabraco, alturapedestal, numsaias):
        if (pedestal == 1):
            alturaisolador = -2*alturasapata-10+80+40*numsaias
            zpedestal = alturacruzpol*25.4+2*alturasapata+alturapedestal+alturaisolador
            # pedestal inferior
            for x in range(numsapatas):
                # parte superior
                box = self.activ_doc.addObject(
                    "Part::Box", "PedestalInf-superior")
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
                self.activ_doc.recompute()
                # parte central
                box = self.activ_doc.addObject(
                    "Part::Box", "PedestalInf-central")
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
                self.activ_doc.recompute()
                # parte lateral direita
                box = self.activ_doc.addObject(
                    "Part::Box", "PedestalInf-esquerda")
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
                self.activ_doc.recompute()
                # parte lateral esquerda
                box = self.activ_doc.addObject(
                    "Part::Box", "PedestalInf-direita")
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
                self.activ_doc.recompute()
                # parte inferior
                box = self.activ_doc.addObject(
                    "Part::Box", "PedestalInf-inferior")
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
                self.activ_doc.recompute()
            # pedestal superior
            if (sapatasup == 1):
                for x in range(numsapatas):
                    zpedestal = alturacruzpol*25.4+alturasapata
                    # parte inferior
                    box = self.activ_doc.addObject(
                        "Part::Box", "PedestalSup-inferior")
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
                    self.activ_doc.recompute()
                    # parte central
                    box = self.activ_doc.addObject(
                        "Part::Box", "PedestalSup-central")
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
                    self.activ_doc.recompute()
                    # parte lateral direita
                    box = self.activ_doc.addObject(
                        "Part::Box", "PedestalSup-esquerda")
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
                    self.activ_doc.recompute()
                    # parte lateral esquerda
                    box = self.activ_doc.addObject(
                        "Part::Box", "PedestalSup-direita")
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
                    self.activ_doc.recompute()
                    # parte superior
                    box = self.activ_doc.addObject(
                        "Part::Box", "PedestalSup-superior")
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
                    self.activ_doc.recompute()

    def criarespacadores(self, diamesp, altura, numbracos, espessurabraco, numcil, diamint, espessuracil):
        numespacadores = numbracos*int((360/numbracos)/10)
        for y in range(numcil-1):
            for x in range(numespacadores):
                cylinder = self.activ_doc.addObject(
                    "Part::Cylinder", "Espacador")
                cylinder.Radius = diamesp/2
                cylinder.Height = altura
                anguloentrebracos = math.radians(360/numbracos)
                anguloentreespacadores = math.radians(360/numespacadores)
                xrel = math.cos(anguloentreespacadores*x-math.atan(espessurabraco/(2*self.raiomiolo)))*(
                    diamint+diamesp*(y+1)-(0.55*diamesp)+espessuracil*(y+1))
                yrel = math.sin(anguloentreespacadores*x-math.atan(espessurabraco/(2*self.raiomiolo)))*(
                    diamint+diamesp*(y+1)-(0.55*diamesp)+espessuracil*(y+1))
                cylinder.Placement = App.Placement(App.Vector(
                    xrel, yrel, 0), App.Rotation((360/numespacadores)*x, 0, 0))
                self.activ_doc.recompute()

    def criaranelanticorona(self, altura, diamint, espessuracil, numcil, diamesp, anel, posterminf, postermsup, numbracos):
        if (anel == 1):
            # anel superior
            torus = self.activ_doc.addObject("Part::Torus", "myTorus")
            torus.Radius1 = (diamint)+espessuracil * \
                (numcil+1)+(numcil+1)*diamesp
            torus.Radius2 = 76.2/2
            torus.Angle1 = -180
            torus.Angle2 = 180
            torus.Angle3 = 330
            torus.Placement = App.Placement(App.Vector(
                0, 0, altura+30), App.Rotation(15+(360/numbracos)*postermsup, 0, 0))
            self.activ_doc.recompute()
            # anel inferior
            torus = self.activ_doc.addObject("Part::Torus", "myTorus")
            torus.Radius1 = (diamint)+espessuracil * \
                (numcil+1)+(numcil+1)*diamesp
            torus.Radius2 = 76.2/2
            torus.Angle1 = -180
            torus.Angle2 = 180
            torus.Angle3 = 330
            torus.Placement = App.Placement(App.Vector(
                0, 0, 0), App.Rotation(15+(360/numbracos)*posterminf, 0, 0))
            self.activ_doc.recompute()

    def criarisolador(self, numbracos, espessurabraco, raiomiolo, diamfundacao, altura, diamsaia, numsaias, espessuracil, alturasapata, alturacruzpol, ladosapata):
        for y in range(numbracos):
            for x in range(numsaias):
                # Saia isolador
                cylinder = self.activ_doc.addObject(
                    "Part::Cylinder", "SaiaIsolador")
                cylinder.Radius = diamsaia
                cylinder.Height = 20
                anguloentrebracos = math.radians(360/numbracos)
                xrel = math.cos(anguloentrebracos*y) * \
                    (diamfundacao/2+ladosapata/2)
                yrel = math.sin(anguloentrebracos*y) * \
                    (diamfundacao/2+ladosapata/2)
                cylinder.Placement = App.Placement(App.Vector(
                    xrel, yrel, -(alturacruzpol*25.4+3*alturasapata+40)-40*x), App.Rotation((360/numbracos)*y, 0, 0))
                self.activ_doc.recompute()
                # Tubo interno
                if (x < numsaias-1):
                    cylinder = self.activ_doc.addObject(
                        "Part::Cylinder", "TuboIsolador")
                    cylinder.Radius = diamsaia/2
                    cylinder.Height = 20
                    anguloentrebracos = math.radians(360/numbracos)
                    cylinder.Placement = App.Placement(App.Vector(
                        xrel, yrel, -(alturacruzpol*25.4+3*alturasapata+40)-40*x-20), App.Rotation((360/numbracos)*y, 0, 0))
                    self.activ_doc.recompute()
                # contorno lateral da saia
                torus = self.activ_doc.addObject("Part::Torus", "ArestaSaia")
                torus.Radius1 = diamsaia
                torus.Radius2 = 10
                torus.Angle1 = -180
                torus.Angle2 = 180
                torus.Angle3 = 360
                torus.Placement = App.Placement(App.Vector(
                    xrel, yrel, -(alturacruzpol*25.4+3*alturasapata-10+40)-40*x), App.Rotation((360/numbracos)*y, 0, 0))
                self.activ_doc.recompute()
            # Apoio superior
            cylinder = self.activ_doc.addObject(
                "Part::Cylinder", "ApoioSuperior")
            cylinder.Radius = diamsaia*0.6
            cylinder.Height = 40
            anguloentrebracos = math.radians(360/numbracos)
            cylinder.Placement = App.Placement(App.Vector(
                xrel, yrel, -(alturacruzpol*25.4+3*alturasapata)-20), App.Rotation((360/numbracos)*y, 0, 0))
            self.activ_doc.recompute()
            # Apoio inferior
            cylinder = self.activ_doc.addObject(
                "Part::Cylinder", "ApoioInferior")
            cylinder.Radius = diamsaia*0.6
            cylinder.Height = 40
            anguloentrebracos = math.radians(360/numbracos)
            cylinder.Placement = App.Placement(App.Vector(
                xrel, yrel, -(alturacruzpol*25.4+3*alturasapata-10+80)-40*x), App.Rotation((360/numbracos)*y, 0, 0))
            self.activ_doc.recompute()

    def criarsemiesferas(self, altura, alturacruzpol, espessurabraco, diamint, espessuracil, numcil, diamesp, numbracos, posterminf, postermsup, semiesfera, diamsemiesferapol):
        if (semiesfera == 1):
            # Semi esfera inferior
            for x in range(numbracos):
                if (x != posterminf):
                    sphere = self.activ_doc.addObject(
                        "Part::Sphere", "SemiEsferaInf")
                    sphere.Radius = diamsemiesferapol*25.4/2
                    sphere.Angle1 = -90
                    sphere.Angle2 = 90
                    sphere.Angle3 = 180
                    anguloentrebracos = math.radians(360/numbracos)
                    raio = (diamint)+espessuracil*(numcil-1) + \
                        (numcil-1)*diamesp+self.raiomiolo
                    xrel = math.cos(anguloentrebracos*x -
                                    math.atan(espessurabraco*0.25/(2*raio)))*raio
                    yrel = math.sin(anguloentrebracos*x -
                                    math.atan(espessurabraco*0.25/(2*raio)))*raio
                    sphere.Placement = App.Placement(App.Vector(
                        xrel, yrel, -alturacruzpol*25.4/2), App.Rotation(-90+((360/numbracos)*(x)), 0, 0))
                    self.activ_doc.recompute()
            # Semi esfera superior
            for x in range(numbracos):
                if (x != postermsup):
                    sphere = self.activ_doc.addObject(
                        "Part::Sphere", "SemiEsferaSup")
                    sphere.Radius = diamsemiesferapol*25.4/2
                    sphere.Angle1 = -90
                    sphere.Angle2 = 90
                    sphere.Angle3 = 180
                    anguloentrebracos = math.radians(360/numbracos)
                    raio = (diamint)+espessuracil*(numcil-1) + \
                        (numcil-1)*diamesp+self.raiomiolo
                    xrel = math.cos(anguloentrebracos*x -
                                    math.atan(espessurabraco*0.25/(2*raio)))*raio
                    yrel = math.sin(anguloentrebracos*x -
                                    math.atan(espessurabraco*0.25/(2*raio)))*raio
                    sphere.Placement = App.Placement(App.Vector(
                        xrel, yrel, altura + alturacruzpol*25.4/2), App.Rotation(-90+((360/numbracos)*(x)), 0, 0))
                    self.activ_doc.recompute()

    def criarreator(self, diamint, espessuracil, diamesp, numcil, altura, alturacruzpol, espessurabraco, numbracos, postermsup, posterminf, compterminal, diamfundacao, alturasapata, ladosapata, numsapatas, sapatasup, alturapedestal, pedestal, anel, diamsaia, numsaias, semiesfera, diamsemiesferapol):
        self.criarcilindros(diamint, espessuracil, diamesp, numcil, altura)
        self.criarcruzeta(alturacruzpol, espessurabraco, (diamint) +
                          espessuracil*(numcil-1)+(numcil-1)*diamesp, numbracos, altura)
        self.criarterminal((diamint)+espessuracil*(numcil-1)+(numcil-1)*diamesp, espessurabraco, alturacruzpol,
                           numbracos, postermsup, posterminf, compterminal, altura, espessuracil, diamint, diamesp, numcil)
        self.criarsapata(diamfundacao, alturasapata, ladosapata, numbracos,
                         alturacruzpol, numsapatas, altura, sapatasup)
        self.criarpedestal(pedestal, diamfundacao, alturasapata, ladosapata, numbracos, alturacruzpol,
                           numsapatas, altura, sapatasup, espessurabraco, alturapedestal, numsaias)
        self.criarespacadores(diamesp, altura, numbracos,
                              espessurabraco, numcil, diamint, espessuracil)
        self.criaranelanticorona(altura, diamint, espessuracil, numcil,
                                 diamesp, anel, posterminf, postermsup, numbracos)
        self.criarisolador(numbracos, espessurabraco, self.raiomiolo, diamfundacao, altura,
                           diamsaia, numsaias, espessuracil, alturasapata, alturacruzpol, ladosapata)
        self.criarsemiesferas(altura, alturacruzpol, espessurabraco, diamint, espessuracil,
                              numcil, diamesp, numbracos, posterminf, postermsup, semiesfera, diamsemiesferapol)

    def terminal(self, cruzinf=pd.DataFrame, cruzsup=pd.DataFrame, dbs=0.0, raiobraco=0.0, compterminal=0.0, postermsup=0, posterminf=0):
        numbracos = cruzsup['Braços'][0]
        alturacruz = cruzsup['Largura (mm)'][0]
        espessurabraco = cruzsup['Espessura (mm)'][0]
        anguloentrebracos = math.radians(360/numbracos)
        # terminal superior
        box = self.activ_doc.addObject("Part::Box", "Terminal superior")
        box.Length = compterminal
        box.Width = espessurabraco
        box.Height = alturacruz
        anguloentrebracos = math.radians(360/numbracos)
        # raiobraco = self.raiomiolo + diamint + \
        #     espessuracil*(numcil-1)+(numcil-1)*diamesp
        xrel = math.cos(anguloentrebracos*postermsup -
                        math.atan(espessurabraco/(2*raiobraco)))*raiobraco
        yrel = math.sin(anguloentrebracos*postermsup -
                        math.atan(espessurabraco/(2*raiobraco)))*raiobraco
        box.Placement = App.Placement(App.Vector(
            xrel, yrel, dbs), App.Rotation((360/numbracos)*postermsup, 0, 0))
        self.group.addObjects([box])    
        self.activ_doc.recompute()
        # terminal inferior
        numbracos = cruzinf['Braços'][0]
        alturacruz = cruzinf['Largura (mm)'][0]
        espessurabraco = cruzinf['Espessura (mm)'][0]
        box = self.activ_doc.addObject("Part::Box", "Terminal inferior")
        box.Length = compterminal
        box.Width = espessurabraco
        box.Height = alturacruz
        anguloentrebracos = math.radians(360/numbracos)
        # raiobraco = self.raiomiolo + diamint + \
        #     espessuracil*(numcil-1)+(numcil-1)*diamesp
        xrel = math.cos(anguloentrebracos*posterminf -
                        math.atan(espessurabraco/(2*raiobraco)))*raiobraco
        yrel = math.sin(anguloentrebracos*posterminf -
                        math.atan(espessurabraco/(2*raiobraco)))*raiobraco
        box.Placement = App.Placement(App.Vector(
            xrel, yrel, (-alturacruz)), App.Rotation((360/numbracos)*posterminf, 0, 0))
        self.group.addObjects([box])    
        self.activ_doc.recompute()

    def cruzetas(self, cruzinf=pd.DataFrame, cruzsup=pd.DataFrame, dbs=0.0, compbraco=0.0):
        # cruzeta inferior
        tube = Shapes.addTube(App.ActiveDocument, "Botton Hub")
        alturacruz = cruzinf['Largura (mm)'][0]
        tube.Height = alturacruz
        tube.InnerRadius = 22
        tube.OuterRadius = 81

        tube.Placement = App.Placement(App.Vector(
            0, 0, -alturacruz), App.Rotation(0, 0, 0))
        self.activ_doc.recompute()
        espessurabraco = cruzinf['Espessura (mm)'][0]
        numbracos = cruzinf['Braços'][0]
        self.group.addObjects([tube]) 
        for x in range(numbracos):
            box = self.activ_doc.addObject(
                "Part::Box", "botton arm "+str(x))
            box.Length = compbraco
            box.Width = espessurabraco
            box.Height = alturacruz
            anguloentrebracos = math.radians(360/numbracos)
            xrel = math.cos(anguloentrebracos*x -
                            math.atan(espessurabraco/(2*self.raiomiolo)))*self.raiomiolo
            yrel = math.sin(anguloentrebracos*x -
                            math.atan(espessurabraco/(2*self.raiomiolo)))*self.raiomiolo
            box.Placement = App.Placement(App.Vector(
                xrel, yrel, -alturacruz), App.Rotation((360/numbracos)*x, 0, 0))
            self.group.addObjects([box]) 
            self.activ_doc.recompute()
        # cruzeta superior
        tube = Shapes.addTube(App.ActiveDocument, "Top Hub")         
        alturacruz = cruzsup['Largura (mm)'][0]
        tube.Height = alturacruz
        tube.InnerRadius = 22
        tube.OuterRadius = 81
        tube.Placement = App.Placement(App.Vector(
            0, 0, dbs), App.Rotation(0, 0, 0))
        self.group.addObjects([tube])    
        self.activ_doc.recompute()
        espessurabraco = cruzsup['Espessura (mm)'][0]
        numbracos = cruzsup['Braços'][0]
        for x in range(numbracos):
            box = self.activ_doc.addObject(
                "Part::Box", "Top arm "+str(x))
            box.Length = compbraco
            box.Width = espessurabraco
            box.Height = alturacruz
            anguloentrebracos = math.radians(360/numbracos)
            xrel = math.cos(anguloentrebracos*x -
                            math.atan(espessurabraco/(2*self.raiomiolo)))*self.raiomiolo
            yrel = math.sin(anguloentrebracos*x -
                            math.atan(espessurabraco/(2*self.raiomiolo)))*self.raiomiolo
            box.Placement = App.Placement(App.Vector(
                xrel, yrel, dbs), App.Rotation((360/numbracos)*x, 0, 0))
            self.group.addObjects([box])
            self.activ_doc.recompute()
        pass

    def cilindros(self, cils=pd.DataFrame, camadas=pd.DataFrame, dbs=0.0, espessurabraco=12.7,cruz = 76.2,numbracos=6, enrol=False):
        id_cam = 0
        id_esp = 0
        id_fio = 0
        for index, cil in cils.iterrows():            
            frd = int(cil['Fios radiais'])
            fax = int(cil['Fios axiais'])
            tube = Shapes.addTube(App.ActiveDocument,
                                  "Fibra interna "+str(index+1))
            tube.Height = dbs
            tube.InnerRadius = (camadas['Diâmetro médio'][id_cam] -
                                cil['dfio isol avg (mm)']-2*cil['Fibra interna (mm)'])/2
            tube.OuterRadius = (camadas['Diâmetro médio'][id_cam] -
                                cil['dfio isol avg (mm)'])/2
            tube.ViewObject.DiffuseColor=(1.0,1.0,1.0)
            tube.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 0))
            self.group.addObjects([tube])
            #self.activ_doc.recompute()
            raio = cil['dfio isol avg (mm)']/2
            grade = min(numbracos,fax)            
            for layer in range(frd):
                anel = (dbs-camadas['Altura do enrolamento'][id_cam])/2
                r_cam = camadas['Diâmetro médio'][id_cam]/2
                h_cam = camadas['Altura do enrolamento'][id_cam]
                if layer==0:
                    hmin = h_cam
                    hmax = h_cam
                    rmin = r_cam
                    rmax = r_cam
                else:
                    hmin = min(h_cam,hmin)
                    hmax = max(h_cam,hmax)
                    rmin = min(r_cam,rmin)
                    rmax = max(r_cam,rmax)      
                anel = (dbs-hmin)/2
                if enrol:
                    for fio in range(fax):
                        circle = self.activ_doc.addObject("Part::Circle", "Fio" + str(id_fio+1))
                        place = App.Placement(App.Vector(r_cam*math.cos(math.radians((360/grade)*fio)), r_cam*math.sin(math.radians((360/grade)*fio)), anel), App.Rotation(90, 90, (360-(360/grade))*fio))
                        circle.Radius = raio
                        circle.Angle1 = 0
                        circle.Angle2 = 0
                        circle.Placement = place
                        helix = self.activ_doc.addObject("Part::Helix", "camada " + str(id_fio+1))
                        helix.Pitch = fax**raio*2                   
                        helix.Height = h_cam                    
                        helix.Radius = r_cam
                        helix.SegmentLength = 0
                        helix.Angle = 0
                        helix.Placement = App.Placement(App.Vector(0, 0, anel), App.Rotation(((360/grade)*(fio)), 0, 0))
                        sweep = self.activ_doc.addObject('Part::Sweep','Enrolamento' + str(id_fio+1))
                        sweep.Sections = circle
                        sweep.Spine = helix
                        sweep.Solid = True
                        sweep.Frenet = True
                        sweep.Placement = App.Placement(App.Vector(0,0,0), App.Rotation(0 ,0, 0))
                        sweep.ViewObject.DiffuseColor=(1.0,0.0,0.0)
                        id_fio += 1
                        self.group.addObjects([sweep])
                else:
                    lay = Shapes.addTube(App.ActiveDocument,"camada "+str(id_cam+1))
                    lay.Height = h_cam
                    lay.InnerRadius = r_cam-raio*reactor.np.cos(reactor.np.pi/6)
                    lay.OuterRadius = r_cam+raio*reactor.np.cos(reactor.np.pi/6)
                    lay.Placement = App.Placement(App.Vector(0, 0, anel), App.Rotation(0, 0, 0)) 
                    lay.ViewObject.DiffuseColor=(1.0,0.0,0.0)
                    self.group.addObjects([lay])                   
                id_cam += 1
            tube = Shapes.addTube(App.ActiveDocument,
                                  "Fibra externa "+str(index+1))
            tube.Height = dbs
            tube.InnerRadius = (camadas['Diâmetro médio'][id_cam-1] + cil['dfio isol avg (mm)'])/2
            tube.OuterRadius = (camadas['Diâmetro médio'][id_cam-1] + cil['dfio isol avg (mm)']+2 * cil['Fibra externa (mm)'])/2
            tube.ViewObject.DiffuseColor=(1.0,1.0,1.0)
            tube.Placement = App.Placement(App.Vector(0, 0, 0), App.Rotation(0, 0, 0))            
            self.group.addObjects([tube]) 
            ds_cil = (camadas['Diâmetro médio'][id_cam-1] +
                                cil['dfio isol avg (mm)']+2 * cil['Fibra externa (mm)'])/2
            self.group.addObjects([tube])            
            larg_espc = cil['Espaçadores (mm)']
            numespacadores = int(cil['# Espaçadores'])

            if numespacadores>0:
                box = self.activ_doc.addObject("Part::Box", "separador "+str(index))
                box.Length = larg_espc
                box.Width = 6.35
                box.Height = dbs+cruz 
                box.Placement = App.Placement(App.Vector(ds_cil, 0, -cruz/2), App.Rotation(0, 0, 0))                
                esp_array = Draft.make_polar_array(box,number=numespacadores, angle=360, center=App.Vector(0, 0, 0),
                                            use_link=True)
                self.group.addObjects([box,esp_array])
        self.activ_doc.recompute()
        pass

    def modelo(self, cilindros=pd.DataFrame, camadas=pd.DataFrame, constr=pd.DataFrame, enrol=False):        
        cruzetas = reactor.cruzetas()
        q = reactor.string_cruz(constr['Cruzeta superior'][0])
        cruz_sup = con.execute(q).df()
        q = reactor.string_cruz(constr['Cruzeta inferior'][0])
        cruz_inf = con.execute(q).df()
        espessurabraco = cruz_inf['Espessura (mm)'][0]
        numbracos = cruz_inf['Braços'][0]
        cruz = cruz_inf['Largura (mm)'][0]
        self.cilindros(cilindros, camadas, constr['DBS (mm)'][0],cruz=cruz,espessurabraco=espessurabraco,numbracos=numbracos,enrol=enrol)        
        arm_len = (constr['Diâmetro externo (mm)'][0]+20)/2-self.raiomiolo
        self.cruzetas(cruz_inf, cruz_sup, constr['DBS (mm)'][0], arm_len)
        self.terminal(cruzinf=cruz_inf, cruzsup=cruz_sup,
                      dbs=constr['DBS (mm)'][0], compterminal=200, raiobraco=arm_len, posterminf=0, postermsup=cruz_sup['Braços'][0]//2)
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().viewIsometric()
        #Gui.activeDocument().activeView().setCameraType("Perspective")
        pass

    def desenha(self, cils=pd.DataFrame):
        # FreeCADGui.showMainWindow()
        # app = App.newDocument()
        self.clearAll()
        self.criarreator(500, 30, 19, 5, 1500, 2, 13, 10, 5, 0, 100,
                         1000, 10, 120, 10, 0, 500, 1, 0, 80, 10, 1, 5)
        Gui.SendMsgToActiveView("ViewFit")
        Gui.activeDocument().activeView().setCameraType("Perspective")
        Gui.activeDocument().activeView().viewIsometric()
        # FreeCADGui.show()
        # End command ViewPerspectiveCmd
        # FreeCADGui.runCommand('Std_OrthographicCamera', 0)
        # FreeCADGui.runCommand('Std_PerspectiveCamera', 1)


# if __name__ == "__main__":
#     app = QApplication.instance()
#     if app is None:
#         app = QApplication(sys.argv)
#     FreeCADGui.showMainWindow()
#     doc = App.newDocument()
#     # box = Part.makeBox(100, 100, 100)
#     # Part.show(box)
#     reator = BreeCadReactor(51, list(), doc)
#     reator.clearAll()
#     reator.criarreator(500, 30, 19, 5, 1500, 2, 13, 10, 5, 0, 100,
#                        1000, 10, 120, 10, 0, 500, 1, 0, 80, 10, 1, 5)
#     sys.exit(app.exec_())
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