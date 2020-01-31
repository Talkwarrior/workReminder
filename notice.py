import sys
import random
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import *
import winsound

form_class=uic.loadUiType("data/Warn.ui")[0]


# 화면을 띄우는데 사용되는 Class 선언
class WindowClass1(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.setWindowFlags(flags)
        self.initCloseBtn()

        self.Message.setText('미해결 과제가 있습니다: \n' + sys.argv[1])

        # winsound.PlaySound('data/Windows XP Critial Stop.wav', winsound.SND_FILENAME|winsound.SND_NODEFAULT)
        winsound.PlaySound('SystemHand', winsound.SND_ALIAS)

    def initCloseBtn(self):
        num = random.randint(0, 7)
        btns = [self.Close_1, self.Close_2, self.Close_3, self.Close_4, \
                self.Close_5, self.Close_6, self.Close_7, self.Close_8]

        btns[num].clicked.connect(self.close)


if __name__ == "__main__" :
    # QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    # WindowClass의 인스턴스 생성
    myWindow = WindowClass1()

    # 프로그램 화면을 보여주는 코드
    myWindow.show()

    # 프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()