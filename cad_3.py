import os
import sys

from PySide2 import QtCore, QtGui
from PySide2.QtWidgets import QMainWindow, QAction, QApplication

#from coin import SoInput, SoDB
from quarter import QuarterWidget
import FreeCADGui
import FreeCAD


class MdiQuarterWidget(QuarterWidget):
    def __init__(self, parent, sharewidget):
        QuarterWidget.__init__(self, parent=parent, sharewidget=sharewidget)

    def minimumSizeHint(self):
        return QtCore.QSize(640, 480)


class MdiMainWindow(QMainWindow):
    def __init__(self, qApp):
        QMainWindow.__init__(self)
        self._firstwidget = None
        self._workspace = QtGui.QWorkspace()
        self.setCentralWidget(self._workspace)
        self.setAcceptDrops(True)
        self.setWindowTitle("Pivy Quarter MDI example")

        filemenu = self.menuBar().addMenu("&File")
        windowmenu = self.menuBar().addMenu("&Windows")

        fileopenaction = QAction("&Create Box", self)
        fileexitaction = QAction("E&xit", self)
        tileaction = QAction("Tile", self)
        cascadeaction = QAction("Cascade", self)

        filemenu.addAction(fileopenaction)
        filemenu.addAction(fileexitaction)
        windowmenu.addAction(tileaction)
        windowmenu.addAction(cascadeaction)

        self.connect(fileopenaction, QtCore.SIGNAL(
            "triggered()"), self.createBoxInFreeCAD)
        self.connect(fileexitaction, QtCore.SIGNAL(
            "triggered()"), QtGui.qApp.closeAllWindows)
        self.connect(tileaction, QtCore.SIGNAL(
            "triggered()"), self._workspace.tile)
        self.connect(cascadeaction, QtCore.SIGNAL(
            "triggered()"), self._workspace.cascade)

        windowmapper = QtCore.QSignalMapper(self)
        self.connect(windowmapper, QtCore.SIGNAL(
            "mapped(QWidget *)"), self._workspace.setActiveWindow)

        self.dirname = os.curdir

    def closeEvent(self, event):
        self._workspace.closeAllWindows()

    def createBoxInFreeCAD(self):
        d = FreeCAD.newDocument()
        o = d.addObject("Part::Box")
        d.recompute()
        s = FreeCADGui.subgraphFromObject(o)
        child = self.createMdiChild()
        child.show()
        child.setSceneGraph(s)

    def createMdiChild(self):
        widget = MdiQuarterWidget(None, self._firstwidget)
        self._workspace.addWindow(widget)
        if not self._firstwidget:
            self._firstwidget = widget
        return widget


def main():
    app = QApplication(sys.argv)
    FreeCADGui.setupWithoutGUI()
    mdi = MdiMainWindow(app)
    mdi.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
