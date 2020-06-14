from GUI.mainWindow import MainWindow
from PyQt5 import QtWidgets
from GUI.main_ui import Ui_MainWindow

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())