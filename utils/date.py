from PyQt5.QtCore import QDate

def normalizeDateTime(date):
    # converts data format.
    # "금 7 3 22:00:00 2020" -> "2020/7/3/22:00
    date = date.split(' ')
    time = date[3].split(':')
    return f"{date[4].zfill(4)}/{date[1].zfill(2)}/{date[2].zfill(2)}/{time[0].zfill(2)}:{time[1].zfill(2)}"

def normalizeTime(time):
    # converts time format.
    # "15:00:00" -> "15h 00m"
    time = time.split(':')
    return f"{time[0]}h {time[1]}m"


if __name__ == '__main__':
    print("A Module to convert date/time format")
