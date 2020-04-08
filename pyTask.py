import os
import json

"""
    task class for workReminder.
    Those are properties:
        "Label": "이름",
        "deadline": "2020-05-16",
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
    def __init__(self, _label="", _deadline="", _type="", _description="", _co_work=""):
        self.label = _label
        self.deadline = _deadline
        self.type = _type
        self.description = _description
        self.co_work = _co_work

    def __str__(self): return self.label

    def __repr__(self):
        return self.__dict__.__str__()

    def __cmp__(self, other):
        return self.label > other.label


"""
    TaskSeries class for workReminder.
    Those are properties(implements list):
        
    Also there are methods like:
        __init__()          initialize self
        __repr__()          introduces self tasks
        save_file(filename)     save to file(.json)
        load_file(filename)      load series from file(.json)
"""


class TaskSeries(list):
    def __init__(self, lst=[]):
        super().__init__(lst)

    def __str__(self):
        return ' '.join([task.__str__() for task in self])

    def save_file(self, filename, overwrite=False):
        if filename is None:
            return
        if os.path.isfile(filename) and not overwrite:
            print(f"Cannot Overwrite {filename}. The file already exists.")
            return
        with open(filename, 'w', encoding='UTF8') as f:
            data = dict()
            data["tasks"] = self  # represent error
            print(data)
            json.dump(data, f, indent="\t")

    def load_file(self, filename):
        if filename is None:
            return
        if not os.path.isfile(filename):
            print(f"Cannot Read {filename}. The file is not exist.")
            return
        with open(filename, encoding='UTF8') as f:
            data = json.load(f)
            print(data['tasks'])
        self = TaskSeries(data['tasks'])


if __name__ == '__main__':
    print("pyTask v0.0.1")