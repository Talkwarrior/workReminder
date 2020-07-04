import threading
import time
import datetime

class callBackTasks:
    def __init__(self, MainWindow):
        self.parent = MainWindow
        self.running = []
        self.flags = []
        self.initTasks()


    def initTasks(self):
        self.running.append(threading.Thread(target=self.timerTask))
        self.flags.append(True)

    def runTasks(self):
        for thread in self.running:
            thread.start()

    def timerTask(self):
        while(self.flags[0]):
            try:
                self.timer = self.parent.taskTabs.currentWidget()
                idx = self.parent.tasks.find(self.timer.lbl_Label.text())

                # task의 데드라인 읽어오기 -> 남은 초로 변환
                day, hour, minute = self.parent.tasks[idx].getRemainTime()

                self.timer.lcd_Day.display(day)
                self.timer.lcd_Hour.display(hour)
                self.timer.lcd_Min.display(minute)

            except AttributeError:
                pass
            time.sleep(1)

    def killTasks(self):
        for idx, flag in enumerate(self.flags):
            self.flags[idx] = False