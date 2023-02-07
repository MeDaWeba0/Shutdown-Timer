import os, sys, subprocess,platform,time
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPixmap


class clase1(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("gui.ui", self)
        self.pushButton.clicked.connect(self.startfn)
        self.canc.clicked.connect(self.cancelarfn)
    
    def startfn(self):
        command = "shutdown "
        if self.ti.currentText() == "h":
            arr = 3600
        elif self.ti.currentText() == "m":
            arr = 60
        elif self.ti.currentText() == "s":
            arr = 1
        if platform.system() == "Windows":
            if self.mode.currentText() == "Shutdown":
                command += "/s"
            elif self.mode.currentText() == "Reboot":
                command += "/r"
            elif self.mode.currentText() == "Log out":
                command += "/l"
            command += " /t "+str(self.numero.value()*arr)
        elif platform.system() == "Linux":
            if self.mode.currentText() == "Shutdown":
                command += "-h"
            elif self.mode.currentText() == "Reboot":
                command += "-r"
            command += " +"+str(self.numero.value()*(arr/60))
        output = subprocess.run(command, shell=True)
        print(output)

    def cancelarfn(self):
        exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = clase1()
    GUI.show()
    GUI.setWindowTitle("Shutdown timer")
    GUI.setWindowIcon(QtGui.QIcon('icon.png'))
    sys.exit(app.exec_())