from PyQt5 import QtGui, QtWidgets
from PyQt5 import uic
import os
from utils import pyTask
from .dial import Dialog


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.tasks = pyTask.TaskSeries()
        self.loadData()

        self.loadUi()
        self.setEventListener()

    def loadUi(self):
        uic.loadUi("UI/main.ui", self)
        self.updateTable()

        # init menubar
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')

        actionSave = QtWidgets.QAction(QtGui.QIcon("data/images/save.png"), "Save", self)
        actionSave.setShortcut('Ctrl+S')
        actionSave.setStatusTip('Save File')
        actionSave.triggered.connect(self.ASave)
        filemenu.addAction(actionSave)

    def updateTable(self):
        self.taskTable.clear()
        elem = ['label', 'deadline', 'require', 'type']
        for row, task in enumerate(self.tasks):
            task.__dict__().values()
            for col in range(4):
                self.taskTable.setItem(row, col, QtWidgets.QTableWidgetItem(task.__dict__()[elem[col]]))

    def setEventListener(self):
        self.addButton.clicked.connect(self.AAdd)
        self.delButton.clicked.connect(self.ADelete)
        self.taskTable.doubleClicked.connect(self.AEdit)

    def loadData(self):
        if os.path.isfile('data/tasks.json'):
            self.tasks.load_file('data/tasks.json')
        else:
            with open('data/tasks.json', 'w') as f:
                self.ASave()

    def AAdd(self):
        dial = Dialog()
        dial.exec_()

        task = dial.getTask()

        # Fixme: It adds when we cancels either.
        if task is not None:
            self.tasks.append(task)
            self.updateTable()

    def ADelete(self):
        selected = self.taskTable.selectedItems()

        selected = [selected[l*4].row() for l in range(0, int(len(selected)/4))]
        for line in selected:
            del self.tasks[line]
        self.updateTable()

    def ASave(self):
        self.tasks.save_file('data/tasks.json', overwrite=True)

    def AEdit(self):
        row = self.taskTable.selectedItems()[0].row()
        sub = Dialog(self.tasks[row])
        sub.exec_()

        task = sub.getTask()
        self.tasks[row] = task
        self.updateTable()

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox()
        close.setText("저장하시겠습니까?")
        close.setWindowTitle("종료하기")
        close.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No | QtWidgets.QMessageBox.Cancel)
        close = close.exec()

        if close == QtWidgets.QMessageBox.Yes:
            self.ASave()
            event.accept()
        elif close == QtWidgets.QMessageBox.No:
            event.accept()
        else:
            event.ignore()