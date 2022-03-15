import time
from datetime import date
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


if __name__ == '__main__':
    main()
