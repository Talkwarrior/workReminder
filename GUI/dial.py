from PyQt5 import QtWidgets, QtCore
from PyQt5 import uic
from pyTask import PyTask


class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.loadui()
        self.task = None

    def loadui(self):
        uic.loadUi("UI/taskQuery.ui", self)
        self.buttonBox.accepted.connect(self.btnAccepted)

    def btnAccepted(self):
        lbl = self.LblEdit.text()
        dline = self.DateEdit.date()  # PyQt5.QtCore.QDate(2020, 1, 1)
        description = self.DescriptionEdit.toPlainText()
        ttype = self.TypeBox.currentText()
        require = self.TimeEdit.time()  # PyQt5.QtCore.QTime(12, 0)
        co_work = self.Co_Work.isChecked()

        self.task = PyTask(_label=lbl,
                           _deadline=dline.toString(),
                           _description=description,
                           _co_work=co_work,
                           _type=ttype,
                           _require=require.toString()
                           )

        self.close()

    def getTask(self):
        return self.task
