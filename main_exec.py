from GUI.mainWindow import MainWindow
from PyQt5 import QtWidgets
from utils.reminder import reminder

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    app.exec_()
