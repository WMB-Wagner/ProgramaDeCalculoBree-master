#from freecad import app
# import FreeCAD
# import FreeCADGui
# import Part
# import sys
# from PySide2.QtWidgets import QApplication
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     FreeCADGui.showMainWindow()
#     doc = FreeCAD.newDocument()
#     box = Part.makeBox(100, 100, 100)
#     Part.show(box)
#     sys.exit(app.exec_())
import sys
import os
import FreeCAD
import FreeCADGui as Gui
from PySide2 import QtCore, QtGui


class ScriptCmd:
    def Activated(self):
        # Here your write what your ScriptCmd does...
        FreeCAD.Console.PrintMessage('Hello, World!')

    def GetResources(self):
        return {'Pixmap': 'path_to_an_icon/myicon.png', 'MenuText': 'Short text', 'ToolTip': 'More detailed text'}


Gui.updateGui()
Gui.addCommand('Script_Cmd', ScriptCmd())

# class B:
#     def __init__(self):
#         ui_file = ":/Gui/capacitor_Frequencia.ui"
#         self.form = QtGui.QWidget()

#         uiFile = QtCore.QFile(ui_file)
#         b = FreeCADGui.UiLoader().load(uiFile)

#         layout = QtGui.QVBoxLayout(self.form)
#         layout.addWidget(b)
#         self.form.setWindowTitle("b")


# FreeCADGui.showB())
