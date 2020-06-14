from PyQt5 import QtWidgets, QtCore
from PyQt5 import uic
from utils.pyTask import PyTask
from utils.date import *

types = {'수행평가': 0, '사이드 프로젝트': 1, '대회': 2}


class Dialog(QtWidgets.QDialog):
    def __init__(self, _task=None):
        super().__init__()
        self.task = _task
        self.loadUI()

    def loadUI(self):
        # TODO: enable selecting time longer than 24h
        # uic.loadUi("UI/taskQuery.ui", self)

        self.setObjectName("taskQuery")
        self.resize(330, 321)
        self.setMinimumSize(QtCore.QSize(330, 321))
        self.setMaximumSize(QtCore.QSize(330, 321))
        self.buttonBox = QtWidgets.QDialogButtonBox(self)
        self.buttonBox.setGeometry(QtCore.QRect(30, 270, 281, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(self)
        self.formLayoutWidget.setGeometry(QtCore.QRect(20, 39, 291, 224))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.LblEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.LblEdit.setObjectName("LblEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.LblEdit)
        self.deadline = QtWidgets.QLabel(self.formLayoutWidget)
        self.deadline.setObjectName("deadline")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.deadline)
        self.DateEdit = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.DateEdit.setCalendarPopup(True)
        self.DateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.DateEdit.setDate(QtCore.QDate(2020, 1, 1))
        self.DateEdit.setObjectName("DateEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.DateEdit)
        self.require = QtWidgets.QLabel(self.formLayoutWidget)
        self.require.setObjectName("require")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.require)
        self.type = QtWidgets.QLabel(self.formLayoutWidget)
        self.type.setObjectName("type")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.type)
        self.TypeBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.TypeBox.setEditable(True)
        self.TypeBox.setObjectName("TypeBox")
        self.TypeBox.addItem("")
        self.TypeBox.addItem("")
        self.TypeBox.addItem("")
        self.TypeBox.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.TypeBox)
        self.co_work = QtWidgets.QLabel(self.formLayoutWidget)
        self.co_work.setObjectName("co_work")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.co_work)
        self.Co_Work = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.Co_Work.setObjectName("Co_Work")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.Co_Work)
        self.description = QtWidgets.QLabel(self.formLayoutWidget)
        self.description.setObjectName("description")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.description)
        self.DescriptionEdit = QtWidgets.QPlainTextEdit(self.formLayoutWidget)
        self.DescriptionEdit.setDocumentTitle("")
        self.DescriptionEdit.setPlainText("")
        self.DescriptionEdit.setOverwriteMode(False)
        self.DescriptionEdit.setObjectName("DescriptionEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.DescriptionEdit)
        self.TimeEdit = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.TimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.TimeEdit.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(23, 59, 59)))
        self.TimeEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.TimeEdit.setMinimumTime(QtCore.QTime(0, 0, 0))
        self.TimeEdit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.TimeEdit.setCalendarPopup(True)
        self.TimeEdit.setObjectName("TimeEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.TimeEdit)
        self.info_lbl = QtWidgets.QLabel(self)
        self.info_lbl.setGeometry(QtCore.QRect(20, 10, 281, 21))
        self.info_lbl.setTextFormat(QtCore.Qt.AutoText)
        self.info_lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.info_lbl.setObjectName("info_lbl")

        self.retranslateUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        QtCore.QMetaObject.connectSlotsByName(self)

        if self.task is None:
            self.DateEdit.setDate(QtCore.QDate.currentDate())
        else:
            self.setupUiWithTask()


    def retranslateUi(self, taskQuery):
        _translate = QtCore.QCoreApplication.translate
        taskQuery.setWindowTitle(_translate("taskQuery", "과제편집기"))
        self.label.setText(_translate("taskQuery", "제목"))
        self.deadline.setText(_translate("taskQuery", "제출기한"))
        self.require.setText(_translate("taskQuery", "필요 시간"))
        self.type.setText(_translate("taskQuery", "분류"))
        self.TypeBox.setItemText(0, _translate("taskQuery", "수행평가"))
        self.TypeBox.setItemText(1, _translate("taskQuery", "사이드 프로젝트"))
        self.TypeBox.setItemText(2, _translate("taskQuery", "대회"))
        self.TypeBox.setItemText(3, _translate("taskQuery", "기타: "))
        self.co_work.setText(_translate("taskQuery", "팀과제"))
        self.description.setText(_translate("taskQuery", "설명"))
        self.DescriptionEdit.setPlaceholderText(_translate("taskQuery", "문제수/중요도/연계성 등"))
        self.TimeEdit.setDisplayFormat(_translate("taskQuery", "h:mm"))
        self.info_lbl.setText(_translate("taskQuery", "과제 정보를 입력하세요"))

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

    def accept(self):
        dic = {}
        dic['label'] = self.LblEdit.text()
        dic['deadline'] = normalizeDate(self.DateEdit.date().toString())  # PyQt5.QtCore.QDate(2020, 1, 1)
        dic['description'] = self.DescriptionEdit.toPlainText()
        dic['type'] = self.TypeBox.currentText()
        dic['require'] = normalizeTime(self.TimeEdit.time().toString())  # PyQt5.QtCore.QTime(12, 0)
        dic['co_work'] = self.Co_Work.isChecked()

        for key, value in dic.items():
            # print(key, value)
            if value is '':
                self.info_lbl.setText(f"{key} is none. try again.")
                return False

        self.task = PyTask().load_dict(dic)
        super().accept()

    def reject(self):
        self.task = None
        super().reject()

    def getTask(self):
        return self.task
