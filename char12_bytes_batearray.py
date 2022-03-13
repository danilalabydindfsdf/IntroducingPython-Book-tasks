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

    # but a bytearray is mutable
    blist = [1, 2, 4, 255]
    the_byte_array = bytearray(blist)
    print(the_byte_array)
    the_byte_array[1] = 127
    print(the_byte_array)

    # each of this variables can contain a value(0-255) and max len = 256
    the_bytes = bytes(range(0, 256))
    the_byte_array = bytearray(range(0, 256))
    print(the_bytes)

if __name__ == '__main__':
    main()
