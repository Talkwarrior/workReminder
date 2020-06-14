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
        year = 0
        month = 0
        day = 0
        remain = 0
        while(self.flags[0]):
            self.timer = self.parent.taskTabs.currentWidget()
            idx = self.parent.tasks.find(self.timer.lbl_Label.text())

            # task의 데드라인 읽어오기 -> 남은 초로 변환
            year, month, day = map(int, self.parent.tasks[idx].deadline.split('/'))
            timeleft = (datetime.datetime(year, month, day)-datetime.datetime.now()).total_seconds()

            # reuse variables
            # day, hour, minute
            day, remain = divmod(timeleft, 86400)
            month, remain = divmod(remain, 3600)
            year, remain = divmod(remain, 60)
            self.timer.lcd_Day.display(day)
            self.timer.lcd_Hour.display(month)
            self.timer.lcd_Min.display(year)

            time.sleep(1)

    def killTasks(self):
        for idx, flag in enumerate(self.flags):
            self.flags[idx] = False