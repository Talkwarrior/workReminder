from PyQt5 import QtWidgets, QtCore
from PyQt5 import uic
from utils.pyTask import PyTask
from utils.date import *

types = {'수행평가': 0, '사이드 프로젝트': 1, '대회': 2}


class Dialog(QtWidgets.QDialog):
    def __init__(self, _task=None):
        super().__init__()
        self.task = _task
        self.loadui()

    def loadui(self):
        uic.loadUi("UI/taskQuery.ui", self)
        self.buttonBox.accepted.connect(self.btnAccepted)
        self.buttonBox.rejected.connect(self.btnRejected)

        if self.task is None:
            self.DateEdit.setDate(QtCore.QDate.currentDate())
        else:
            self.setupUiWithTask()

    def setupUiWithTask(self):
        self.LblEdit.setText(self.task.label)

        self.DateEdit.setDate(QtCore.QDate.fromString(self.task.deadline, "yyyy/MM/dd"))
        self.DescriptionEdit.setPlainText(self.task.description)

        if self.task.type in types.keys():
            self.TypeBox.setCurrentIndex(types[self.task.type])
        else:
            self.TypeBox.setCurrentIndex(3)
        self.TimeEdit.setTime(QtCore.QTime.fromString(self.task.require, "TTh MMm"))
        self.Co_Work.setChecked(self.task.co_work)

    def btnAccepted(self):
        lbl = self.LblEdit.text()
        dline = normalizeDate(self.DateEdit.date().toString())  # PyQt5.QtCore.QDate(2020, 1, 1)
        description = self.DescriptionEdit.toPlainText()
        ttype = self.TypeBox.currentText()
        require = normalizeTime(self.TimeEdit.time().toString())  # PyQt5.QtCore.QTime(12, 0)
        co_work = self.Co_Work.isChecked()

        self.task = PyTask(_label=lbl,
                           _deadline=dline,
                           _description=description,
                           _co_work=co_work,
                           _type=ttype,
                           _require=require
                           )

        self.close()

    def btnRejected(self):
        self.task = None
        self.close()

    def getTask(self):
        return self.task
