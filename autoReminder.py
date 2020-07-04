"""
autoReminder.py

this is background program.
No GUI but notifiers.

what this will do:
    1. read tasks.json file
    2. create notifiers on time
    3. show urgent alerts.
"""

import threading
import os
from utils.pyTask import TaskSeries
import time
import win10toast
import schedule

def notify(task):
    day, hour, minute = map(int, task.getRemainTime())
    title = f"{day}일 {hour}시간 {minute}분 후"
    msg = f"{task.label}의 마감입니다"
    win10toast.ToastNotifier().show_toast(title=title, msg=msg)

    return schedule.CancelJob

def updateNotifyPlan():
    global tasks
    global notifyPlan
    global timer
    global updateFlag

    notifyPlan = []
    notifyTerm = [604800, 302400, 259200, 172800, 86400, 43200, 3600]
    for idx, task in enumerate(tasks):
        t = task.getRemainTime(total_seconds=True)
        notifyPlan.append((25*idx, idx))
        for term in notifyTerm:
            if t > term:
                notifyPlan.append((t-term, idx))
    notifyPlan.sort()

    # update Thread
    updateFlag = True

def checkModified():
    global tasks

    while True:
        if os.path.isfile("./data/modified.flag"):
            os.remove("./data/modified.flag")
            tasks = TaskSeries().load_file(filename="./data/tasks.json")
            # print("modified")
            updateNotifyPlan()

        time.sleep(10)

def alert_timer():
    global tasks
    global notifyPlan
    global updateFlag
    while True:
        schedule.clear()

        for plan in notifyPlan:
            schedule.every(plan[0]).seconds.do(notify, task=tasks[plan[1]])

        while updateFlag is False:
            schedule.run_pending()
            time.sleep(1)
        updateFlag = False
        # print("updated plan")

if __name__ == '__main__':
    tasks = TaskSeries().load_file(filename="./data/tasks.json")
    notifyPlan = []
    updateFlag = False

    timer = threading.Thread(target=alert_timer)
    timer.start()

    # initial notify plan
    updateNotifyPlan()

    # checking modified
    checkModify = threading.Thread(target=checkModified)
    checkModify.start()