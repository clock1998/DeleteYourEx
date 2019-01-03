import sys
import os
import ntpath
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QApplication, QListWidgetItem
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
path = os.path.dirname(__file__) #uic paths from itself, not the active dir, so path needed
qtCreatorFile = "/DeleteYourExGui.ui" #Ui file name, from QtDesigner, assumes in same folder as this .py

Ui_MainWindow, QtBaseClass = uic.loadUiType(path + qtCreatorFile) #process through pyuic


class MyApp(QMainWindow, Ui_MainWindow): #gui class
    target_image = ""
    unknown_images = []

    def __init__(self):
        #The following sets up the gui via Qt
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionOpen_Folder.triggered.connect(self.openFolderDialog)
        self.ui.actionOpen_Files.triggered.connect(self.openFileNamesDialog)
        self.ui.actionLoad_Target.triggered.connect(self.openFileNameDialog)

        #set up callbacks

    def openFileNamesDialog(self):
        global unknown_images
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "Select File", "",
                                                "Images Files (*.png *.xpm *.jpg)", options=options)

        if files:
            unknown_images = files
            self.ui.pendingList.setIconSize(QSize(100, 100))
            self.ui.pendingList.clear()

            for i in files:
                item = QListWidgetItem(ntpath.basename(i))
                item.setIcon(QIcon(i))
                item.setSizeHint(QSize(100, 100))
                self.ui.pendingList.addItem(item)
            print(unknown_images)

    def openFileNameDialog(self):
        global target_image
        options = QFileDialog.Options()

        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getOpenFileName(self, "Select File", "",
                                              "Images Files (*.png *.xpm *.jpg)", options=options)
        if file:
            target_image = file
            pixmap = QtGui.QPixmap(file).scaled(300, 400, aspectRatioMode=QtCore.Qt.KeepAspectRatio,
                                                transformMode=QtCore.Qt.SmoothTransformation)
            self.ui.targetFace.setPixmap(pixmap)

    def openFolderDialog(self):
        folder_path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(folder_path)
        return folder_path


if __name__ == "__main__":
    app = QApplication(sys.argv) #instantiate a QtGui (holder for the app)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
