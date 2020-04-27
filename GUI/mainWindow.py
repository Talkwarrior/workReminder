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
        menubar = self.menuBar
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        viewmenu = menubar.addMenu('&View')

        actionSave = QtWidgets.QAction(QtGui.QIcon("data/images/save.png"), "Save", self)
        actionSave.setShortcut('Ctrl+S')
        actionSave.setStatusTip('Save File')
        actionSave.triggered.connect(self.ASave)
        filemenu.addAction(actionSave)

        viewCoWork = QtWidgets.QAction("CoWork only", self)
        viewCoWork.setCheckable(True)
        viewCoWork.toggled.connect(self.updateTable)
        viewmenu.addAction(viewCoWork)

    def updateTable(self, co_work_Only=False):
        self.taskTable.clear()
        elem = ['label', 'deadline', 'require', 'type']

        row = 0
        if co_work_Only:
            for task in self.tasks:
                if co_work_Only and task.co_work:
                    for col in range(4):
                        self.taskTable.setItem(row, col, QtWidgets.QTableWidgetItem(task.__dict__()[elem[col]]))
                    row += 1
        else:
            for task in self.tasks:
                for col in range(4):
                    self.taskTable.setItem(row, col, QtWidgets.QTableWidgetItem(task.__dict__()[elem[col]]))
                row += 1


    def setEventListener(self):
        self.addButton.clicked.connect(self.AAdd)
        self.delButton.clicked.connect(self.ADelete)
        self.taskTable.doubleClicked.connect(self.tableDblClicked)

    def loadData(self):
        if os.path.isfile('data/tasks.json'):
            self.tasks.load_file('data/tasks.json')
        else:
            with open('data/tasks.json', 'w') as f:
                self.ASave()

    def tableDblClicked(self):
        selected = self.taskTable.selectedItems()
        if len(selected) == 0 or selected[0].row() >= len(self.tasks):
            self.AAdd()
        else:
            self.AEdit(selected[0].row())

    def AAdd(self):
        dial = Dialog()
        dial.exec_()

        task = dial.getTask()

        if task is not None:
            self.tasks.append(task)
            self.updateTable()

    def ADelete(self):
        selected = self.taskTable.selectedItems()
        # FIXME: do not delete empty items
        selected = [selected[l*4].text() for l in range(0, int(len(selected)/4))]
        self.tasks.delete(labels=selected) # list of work label
        self.updateTable()

    def ASave(self):
        self.tasks.save_file('data/tasks.json', overwrite=True)

    def AEdit(self, row):
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