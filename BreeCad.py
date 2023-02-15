from PySide2 import QtGui, QtWidgets
from PySide2 import QtCore


def getMainWindow():
    toplevel = QtWidgets.QApplication.topLevelWidgets()
    for i in toplevel:
        if i.metaObject().className() == "Gui::MainWindow":
            return i
    raise Exception("No main window found")


mw = getMainWindow()
