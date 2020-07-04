from PyQt5 import QtGui, QtWidgets, QtCore
import os
from utils import pyTask
from .dial import Dialog
from .taskWidget import taskWidget
from .timer import callBackTasks


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.tasks = pyTask.TaskSeries()
        self.tableRow = len(self.tasks)

        self.timer = callBackTasks(self)
        self.loadData()
        self.setupUi()

        self.updateUI()
        self.setEventListener()
        self.timer.runTasks()

    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(670, 587)
        self.setMinimumSize(QtCore.QSize(670, 587))
        self.setMaximumSize(QtCore.QSize(670, 587))
        self.setDocumentMode(False)
        self.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.setDockNestingEnabled(False)
        self.setDockOptions(QtWidgets.QMainWindow.AnimatedDocks)
        self.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 30, 671, 511))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame = QtWidgets.QFrame(self.page)
        self.frame.setGeometry(QtCore.QRect(0, 10, 661, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.taskTable = QtWidgets.QTableWidget(self.frame)
        self.taskTable.setGeometry(QtCore.QRect(10, 10, 531, 476))
        self.taskTable.setMinimumSize(QtCore.QSize(0, 0))
        self.taskTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.taskTable.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.taskTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.taskTable.setShowGrid(True)
        self.taskTable.setWordWrap(False)
        self.taskTable.setCornerButtonEnabled(True)
        self.taskTable.setRowCount(23)
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
        self.delButton = QtWidgets.QPushButton(self.frame)
        self.delButton.setGeometry(QtCore.QRect(550, 60, 93, 28))
        self.delButton.setObjectName("delButton")
        self.addButton = QtWidgets.QPushButton(self.frame)
        self.addButton.setGeometry(QtCore.QRect(550, 20, 93, 28))
        self.addButton.setObjectName("addButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.taskTabs = QtWidgets.QTabWidget(self.page_2)
        self.taskTabs.setGeometry(QtCore.QRect(10, 10, 651, 501))
        self.taskTabs.setMinimumSize(QtCore.QSize(651, 501))
        self.taskTabs.setMaximumSize(QtCore.QSize(651, 501))
        self.taskTabs.setTabPosition(QtWidgets.QTabWidget.West)
        self.taskTabs.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.taskTabs.setElideMode(QtCore.Qt.ElideNone)
        self.taskTabs.setDocumentMode(False)
        self.taskTabs.setTabsClosable(False)
        self.taskTabs.setMovable(True)
        self.taskTabs.setTabBarAutoHide(False)
        self.taskTabs.setObjectName("taskTabs")

        self.stackedWidget.addWidget(self.page_2)
        self.btn_nextPage = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nextPage.setGeometry(QtCore.QRect(560, 0, 81, 28))
        self.btn_nextPage.setObjectName("btn_nextPage")
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
        # always on top
        self.viewOnTop = QtWidgets.QAction(self)
        self.viewOnTop.setCheckable(True)
        self.viewOnTop.setObjectName("viewOnTop")

        self.filemenu.addAction(self.actionSave)
        self.viewmenu.addAction(self.viewCoWork)
        self.viewmenu.addAction(self.viewOnTop)
        self.menubar.addAction(self.filemenu.menuAction())
        self.menubar.addAction(self.viewmenu.menuAction())

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(0)
        self.taskTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "과제독촉기"))
        self.taskTable.setSortingEnabled(False)
        item = self.taskTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "이름"))
        item = self.taskTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "제출기한"))
        item = self.taskTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "필요시간"))
        item = self.taskTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "분류"))
        self.delButton.setText(_translate("MainWindow", "삭제"))
        self.addButton.setText(_translate("MainWindow", "추가"))

        self.btn_nextPage.setText(_translate("MainWindow", "NEXT>>"))
        self.filemenu.setTitle(_translate("MainWindow", "File"))
        self.viewmenu.setTitle(_translate("MainWindow", "View"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.viewCoWork.setText(_translate("MainWindow", "CoWork Only"))
        self.viewOnTop.setText(_translate("MainWindow", "창 위에 고정"))

    def setEventListener(self):
        self.addButton.clicked.connect(self.AAdd)
        self.delButton.clicked.connect(self.ADelete)
        self.taskTable.doubleClicked.connect(self.tableDblClicked)
        self.actionSave.triggered.connect(self.ASave)
        self.viewCoWork.toggled.connect(self.updateUI)
        self.viewOnTop.toggled.connect(self.toggleViewOnTop)
        self.btn_nextPage.clicked.connect(self.AChangeStack)

    def toggleViewOnTop(self):
        if self.viewOnTop.isChecked():
            self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
            self.show()
        else:
            self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowStaysOnTopHint)
            self.show()

    def updateUI(self):
        self.updateTabs()
        self.updateTable()

    def updateTable(self):
        self.taskTable.clearContents()
        elem = ['label', 'deadline', 'require', 'type']

        row = 0
        co_work_Only = self.viewCoWork.isChecked()
        for task in self.tasks:
            if task.co_work and co_work_Only or not co_work_Only:
                for col in range(4):
                    self.taskTable.setItem(row, col, QtWidgets.QTableWidgetItem(task.__dict__()[elem[col]]))
                row += 1

        self.taskTable.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.taskTable.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.taskTable.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.taskTable.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)


        self.tableRow = row

    def updateTabs(self):
        self.taskTabs.clear()
        self.taskTabs.currentWidget()

        co_work_Only = self.viewCoWork.isChecked()
        for idx, task in enumerate(self.tasks):
            if task.co_work and co_work_Only or not co_work_Only:
                w = taskWidget(task)
                self.taskTabs.addTab(w, task.label)
                w.btn_edit.clicked.connect(lambda : self.AEdit(eventTriggered="tabs"))

    def loadData(self):
        if os.path.isfile('data/tasks.json'):
            self.tasks.load_file('data/tasks.json')
        else:
            with open('data/tasks.json', 'w') as f:
                self.ASave()

    def tableDblClicked(self):
        selected = self.taskTable.selectedItems()
        if len(selected) == 0 or selected[0].row() >= self.tableRow:
            self.AAdd()
        else:
            self.AEdit(eventTriggered="table", select=selected[0].text())

    def AAdd(self):
        dial = Dialog()
        if self.viewOnTop.isChecked():
            dial.setWindowFlags( dial.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        dial.exec_()

        task = dial.getTask()

        if task is not None:
            self.tasks.append(task)
            self.updateUI()

    def ADelete(self):
        selected = self.taskTable.selectedItems()
        selected = [item.text() for item in selected if item is not None and item.column() == 0]
        self.tasks.delete(labels=selected)  # list of work labels
        self.updateUI()

    def ASave(self):
        self.tasks.save_file('data/tasks.json', overwrite=True)

        # create empty flag file
        # this will notify the autoReminder.py
        with open("./data/modified.flag", "w") as f:
            pass

    def AEdit(self, eventTriggered, select=None):
        cursor = -1
        if eventTriggered == "tabs":
            cursor = self.tasks.find(self.taskTabs.currentWidget().lbl_Label.text())

        elif eventTriggered == "table":
            cursor = self.tasks.find(select)
        else:
            return

        sub = Dialog(self.tasks[cursor])
        if self.viewOnTop.isChecked():
            sub.setWindowFlags(sub.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        sub.exec_()

        task = sub.getTask()

        try:
            if task is not None:
                self.tasks[cursor] = task
                self.updateUI()
        except IndexError:
            print("AEdit: IndexError")
            exit(1)

    def AChangeStack(self):
        self.stackedWidget.setCurrentIndex(1 - self.stackedWidget.currentIndex())

    def closeEvent(self, event):
        close = QtWidgets.QMessageBox()
        if self.viewOnTop.isChecked():
            close.setWindowFlags(close.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

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

        self.timer.killTasks()
