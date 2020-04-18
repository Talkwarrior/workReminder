from PyQt5.QtCore import QDate


def normalizeDate(date):
    # converts data format.
    # "토 4 18 2020" -> "2020/4/18"
    date = date.split(' ')
    # TODO: fill 0 among the numbers
    return f"{date[3]}/{date[1]}/{date[2]}"


def normalizeTime(time):
    # converts time format.
    # "15:00:00" -> "15h 00m"
    time = time.split(':')
    return f"{time[0]}h {time[1]}m"


if __name__ == '__main__':
    print("A Module to convert date/time format")
