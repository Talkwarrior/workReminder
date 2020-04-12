from PyQt5 import QtWidgets, QtCore
from PyQt5 import uic
from pyTask import PyTask

class dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.loadui()

    def loadui(self):
        uic.loadUi("UI/taskQuery.ui", self)

    def mainloop(self):
        super().exec()

    def getTask(self, wind):
        self.mainloop()
        lbl = self.LblEdit.text()
        dline = self.DateEdit.date()    # PyQt5.QtCore.QDate(2020, 1, 1)
        description = self.DescriptionEdit.toPlainText()
        ttype = self.TypeBox.currentText()
        require = self.TimeEdit.time()     # PyQt5.QtCore.QTime(12, 0)
        co_work = self.Co_Work.isChecked()

        return (PyTask(_label=lbl,
                       _deadline=dline.toString(),
                       _description=description,
                       _co_work=co_work,
                       _type=ttype,
                       _require=require.toString()
                       ),
                True) # FIXME: I want to get if this dialog is accepted
