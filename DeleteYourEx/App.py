import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
path = os.path.dirname(__file__) #uic paths from itself, not the active dir, so path needed
qtCreatorFile = "/DeleteYourExGui.ui" #Ui file name, from QtDesigner, assumes in same folder as this .py

Ui_MainWindow, QtBaseClass = uic.loadUiType(path + qtCreatorFile) #process through pyuic


class MyApp(QMainWindow, Ui_MainWindow): #gui class
    def __init__(self):
        #The following sets up the gui via Qt
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen_Folder.triggered.connect(self.openFolderDialog)
        self.ui.actionOpen_Files.triggered.connect(self.openFileNamesDialog)
        #set up callbacks

    def openFileNamesDialog(self):
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Select File", "",
                                                "Images Files (*.png *.xpm *.jpg)", options=options)
        if files:
            print(files)
            return files
        return

    def openFileNameDialog(self):
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(self, "Select File", "",
                                              "Images Files (*.png *.xpm *.jpg)", options=options)
        if file:
            print(file)
            return file
        return

    def openFolderDialog(self):
        folder_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(folder_path)
        return folder_path


if __name__ == "__main__":
    app = QApplication(sys.argv) #instantiate a QtGui (holder for the app)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
