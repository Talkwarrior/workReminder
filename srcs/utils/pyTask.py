import os
import datetime
import json

"""
    task class for workReminder.
    Those are properties:
        "Label": "이름",
        "deadline": "2020/05/16/23:00",
        "require": "None",
        "type": "과목이름/프로젝트/수행평가/...",
        "description": "문제수/중요도/연계성"
        "co_work": "True/False"

    Also there are methods like:
        __init__()      initialize self
        __repr__()      introduce self
        __cmp__()       to sort tasks with conditions


        # __add__()       append task into array => not needed
"""


class PyTask:
    def __init__(self, _label="", _deadline="", _type="", _require="", _description="", _co_work="", _dict=None):
        if _dict is not None:
            self.load_dict(_dict)
            return

        self.label = _label
        self.deadline = _deadline
        self.type = _type
        self.require = _require
        self.description = _description
        self.co_work = _co_work

    # TODO: improve __str__
    def __str__(self): return self.label

    def __repr__(self):
        return self.__dict__().__str__()

    # TODO: improve __cmp__
    def __cmp__(self, other):
        return self.label > other.label

    def __dict__(self):
        data = dict()
        data['label'] = self.label
        data['deadline'] = self.deadline
        data['type'] = self.type
        data['require'] = self.require
        data['description'] = self.description
        data['co_work'] = self.co_work
        return data

    def load_dict(self, dictionary):
        self.label = dictionary['label']
        self.deadline = dictionary['deadline']
        self.type = dictionary['type']
        self.require = dictionary['require']
        self.description = dictionary['description']
        self.co_work = dictionary['co_work']
        return self

    def getRemainTime(self, total_seconds=False):
        # task의 데드라인 읽어오기 -> 남은 초로 변환
        year, month, day, p = self.deadline.split('/')
        hour, minute = map(int, p.split(':'))
        timeleft = (datetime.datetime(int(year), int(month), int(day), hour, minute)
                    - datetime.datetime.now()).total_seconds()

        if (total_seconds):
            return timeleft

        # reuse variables
        # day, hour, minute
        day, remain = divmod(timeleft, 86400)
        hour, remain = divmod(remain, 3600)
        minute, remain = divmod(remain, 60)

        return (day, hour, minute)

"""
    TaskSeries class for workReminder.
    Those are properties(implements list):
        
    Also there are methods like:
        __init__()          initialize self
        __repr__()          introduces self tasks
        save_file(filename)     save to file(.json)
        load_file(filename)      load series from file(.json)
        delete(listofLabel, listofTask)     delete tasks in argument
"""


class TaskSeries(list):
    def __init__(self, lst=None):
        if lst is not None:
            super().__init__(lst)
        else:
            super().__init__()

    def __str__(self):
        return '/'.join([str(task) for task in self])

    def load_file(self, filename):
        if filename is None:
            return
        if not os.path.isfile(filename):
            return
        with open(filename, encoding='UTF8') as f:
            data = json.load(f)
        self.extend([PyTask(_dict=task) for task in data['tasks']])
        return self

    def save_file(self, filename, overwrite=False):
        if filename is None:
            return False
        if os.path.isfile(filename) and not overwrite:
            return False
        with open(filename, 'w', encoding='UTF8') as f:
            data = dict()
            data["tasks"] = [x.__dict__() for x in self]
            f.write(json.dumps(data, ensure_ascii=False, indent='\t'))
            return True

    def delete(self, labels=None, tasks=None):
        try:
            if labels is not None:
                for task in reversed(self):
                    if task.label in labels:
                        self.remove(task)
            elif tasks is not None:
                for task in reversed(self):
                    if task in tasks:
                        self.remove(task)
        except TypeError:
            return

    def find(self, label):
        for idx, task in enumerate(self):
            if task.label == label:
                return idx

if __name__ == '__main__':
    print("pyTask v0.0.3")
