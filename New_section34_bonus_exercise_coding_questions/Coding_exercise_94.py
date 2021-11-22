# what day is it on a particular date
import datetime


def goo(date):
    date_from_string = datetime.datetime.strptime(date, '%Y-%m-%d')
    day_of_date = date_from_string.strftime('%A')
    print(day_of_date)
    return day_of_date


goo('2000-2-22')
