def main():
    # create a bytes object
    blist = [1, 2, 3, 4, 5]
    the_bytes = bytes(blist)
    print(the_bytes)

    # bytes is an unmutable object
    try:
        blist = [1, 2, 3, 4, 255]
        the_bytes = bytes(blist)
        the_bytes[0] = 124
    except TypeError as err:
        print(err)


if __name__ == '__main__':
    main()
