from pandasql import sqldf
import sys
import os
#from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from template.main_reactor_window import Ui_BreeReactorMainWindow
from template.SysDataDlg import Ui_DialogSys

#sys.path.append('OneDrive/Documentos/Bree')
sys.path.append('OneDrive/Documentos/GitHub/bree_reactor')
sys.path.append('Documents/GitHub')

#from pathlib import Path
path_name = os.getcwd()
path_name = path_name = path_name.replace("\\","/")
path_name = path_name = path_name.replace("C:","")
path_name

pysqldf = lambda q: sqldf(q, globals())

# import bree_reactor_core_1 as bree
# class MainWindow(QDialog):
class MainWindow(QMainWindow,Ui_BreeReactorMainWindow): 
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.actionDados_do_sistema.triggered.connect(self.system_data)  
    def system_data(self):
        data_system = SysData()
        data_system.exec()                

class SysData(QDialog,Ui_DialogSys):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Create an instance of the GUI
        self.ui = Ui_DialogSys()
        # Run the .setupUi() method to show the GUI
        self.ui.setupUi(self)


# main
if __name__ == "__main__":
    # Create the application
    app = QApplication(sys.argv)
    # Create and show the application's main window
    win = MainWindow()
    win.show()
    # Run the application's main loop
    sys.exit(app.exec())
'''app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()'''