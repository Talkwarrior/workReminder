from PyQt5 import QtGui, QtWidgets, QtCore
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
        self.setupUi()
        self.updateTable()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(670, 547)
        self.setMinimumSize(QtCore.QSize(670, 600))
        self.setMaximumSize(QtCore.QSize(670, 600))
        self.setDocumentMode(False)
        self.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.setDockNestingEnabled(False)
        self.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        self.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.taskTable = QtWidgets.QTableWidget(self.centralwidget)
        self.taskTable.setGeometry(QtCore.QRect(20, 20, 531, 500))
        self.taskTable.setMinimumSize(QtCore.QSize(0, 0))
        self.taskTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.taskTable.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.taskTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.taskTable.setShowGrid(True)
        self.taskTable.setWordWrap(False)
        self.taskTable.setCornerButtonEnabled(True)
        self.taskTable.setRowCount(20)
        self.taskTable.setColumnCount(4)
        self.taskTable.setObjectName("taskTable")

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.taskTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.taskTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.taskTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.taskTable.setHorizontalHeaderItem(3, item)
        self.taskTable.horizontalHeader().setCascadingSectionResizes(True)
        self.taskTable.horizontalHeader().setDefaultSectionSize(120)
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(560, 20, 93, 28))
        self.addButton.setObjectName("addButton")
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(560, 60, 93, 28))
        self.delButton.setObjectName("delButton")

        self.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(self)
        self.statusBar.setObjectName("statusBar")
        self.setStatusBar(self.statusBar)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 670, 26))
        self.menubar.setObjectName("menubar")
        self.filemenu = QtWidgets.QMenu(self.menubar)
        self.filemenu.setObjectName("filemenu")
        self.viewmenu = QtWidgets.QMenu(self.menubar)
        self.viewmenu.setObjectName("viewmenu")
        self.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(self)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../data/images/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave.setIcon(icon)
        self.actionSave.setObjectName("actionSave")
        self.viewCoWork = QtWidgets.QAction(self)
        self.viewCoWork.setCheckable(True)
        self.viewCoWork.setObjectName("viewCoWork")
        self.filemenu.addAction(self.actionSave)
        self.viewmenu.addAction(self.viewCoWork)
        self.menubar.addAction(self.filemenu.menuAction())
        self.menubar.addAction(self.viewmenu.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "과제독촉기"))
        self.taskTable.setSortingEnabled(False)
        item = self.taskTable.horizontalHeaderItem(0)
        item.setText(_translate("self", "이름"))
        item = self.taskTable.horizontalHeaderItem(1)
        item.setText(_translate("self", "제출기한"))
        item = self.taskTable.horizontalHeaderItem(2)
        item.setText(_translate("self", "필요시간"))
        item = self.taskTable.horizontalHeaderItem(3)
        item.setText(_translate("self", "분류"))
        self.addButton.setText(_translate("self", "추가"))
        self.delButton.setText(_translate("self", "삭제"))
        self.filemenu.setTitle(_translate("self", "File"))
        self.viewmenu.setTitle(_translate("self", "View"))
        self.actionSave.setText(_translate("self", "Save"))
        self.actionSave.setShortcut(_translate("self", "Ctrl+S"))
        self.viewCoWork.setText(_translate("self", "CoWork Only"))

    # TODO: default value is wrong
    def updateTable(self):
        self.taskTable.clearContents()
        elem = ['label', 'deadline', 'require', 'type']

        row = 0
        # FIXME: need more simple code
        co_work_Only = self.viewCoWork.isChecked()
        if co_work_Only:
            for task in self.tasks:
                if task.co_work:
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
        self.viewCoWork.toggled.connect(self.updateTable)

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
        selected = [item.text() for item in selected if item is not None and item.column()==0]
        self.tasks.delete(labels=selected) # list of work labels
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