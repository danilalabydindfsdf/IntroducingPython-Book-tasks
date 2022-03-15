import time
from datetime import date, datetime, timedelta
from datetime import time as tm


def main():
    # this amount of seconds means how many seconds have gone since the creation of the UNIX system
    now = time.time()
    print(now)

    # you can convert it in more normal view
    print(time.ctime(now))

    print(time.localtime())
    print(time.gmtime())

    # specifiers to convert a date format to string format
    fmt = "It is a %A, %B, %d, %Y, local time %I:%M:%S%p"
    t = time.localtime()
    print(time.strftime(fmt, t))

    # with date object the function works only with date specifiers
    some_day = date(2019, 7, 14)
    print(some_day.strftime(fmt))

    # with time object the function works with time specifiers
    some_time = tm(10, 35)
    print(some_time.strftime(fmt))

    # to convert a string format to date format
    fmt = "%Y-%m-%d"
    time.strptime("2019-01-21", fmt)

    # make sure you enter a string with correct format
    try:
        print(time.strptime("2019 01 21"))
    except ValueError as err:
        print(err)

    now = date.today()
    now_str = now.isoformat()
    # with open('time.txt', 'wt') as file:
    #     print(now_str, file=file)

    with open('time.txt', 'r') as file:
        today_string = file.read()
        print(today_string)
        print(type(today_string))
        fmt = "%Y-%m-%d\n"
        print(time.strptime(today_string, fmt))

    day = date(2000, 4, 12)
    print(day)
    print(day.weekday())
    years = timedelta(days=10000)
    print(day + years)


if __name__ == '__main__':
    main()
