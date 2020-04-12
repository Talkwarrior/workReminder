from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
import os
import pyTask
from .dial import dialog

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

    # TODO: complete updateTable, set size
    def updateTable(self):
        elem = ['label', 'deadline', 'require', 'type']
        for row, task in enumerate(self.tasks):
            task.__dict__().values()
            for col in range(4):
                self.taskTable.setItem(row, col, QtWidgets.QTableWidgetItem(task.__dict__()[elem[col]]))
        pass

    def setEventListener(self):
        self.addButton.clicked.connect(self.AAdd)
        self.delButton.clicked.connect(self.ADelete)

    def loadData(self):
        if os.path.isfile('data/tasks.json'):
            print('file found')
            self.tasks.load_file('data/tasks.json')
        else:
            open('data/tasks.json').close()

    def AAdd(self):
        dial = dialog()
        task, ok = dial.getTask(self)
        if ok:
            self.tasks.append(task)
            self.updateTable()

    def ADelete(self):
        print('delete')
        pass
