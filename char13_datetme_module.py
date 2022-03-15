import calendar
from datetime import date, timedelta, time, datetime


def main():
    # check a leap year
    print(calendar.isleap(1900))
    print(calendar.isleap(2004))

    # you can create a day object with year, month, day
    halloween = date(2019, 10, 31)
    print(halloween.day)
    print(halloween.month)
    print(halloween.year)
    print(halloween.isoformat())

    now = date.today()
    print(now)

    # you can add a time interval
    one_day = timedelta(days=1)
    tomorrow = now + one_day
    print(tomorrow)

    # a time object represents a day time
    noon = time(12, 0, 0)
    print(noon)

    # you can create a date with day time
    some_day = datetime(2019, 1, 2, 3, 4, 6)
    print(some_day)
    print(some_day.isoformat())

    # to get a full current time and you can get access to all time components
    now = datetime.now()
    print(now)
    print(now.year)
    print(now.second)

    # you can combine date amd time objects using combine() method
    noon = time(12)
    this_day = date.today()
    noon_today = datetime.combine(this_day, noon)
    print(noon_today)
    print(noon_today.date())
    print(noon_today.time())


if __name__ == '__main__':
    main()
