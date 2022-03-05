import unicodedata


def unicode_test(value):
    """The function takes Unicode symbol, finds its name and then
     finds symbol that references to its name(must be the same with the original value"""
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print(f'value - {value} name - {name} value2 - {value2}')


def main():
    try:
        unicode_test('E')
    except TypeError as err:
        print(err)

    # encode a Unicode string with UTF-8 format
    snowman = '\u2603'
    print(len(snowman))  # should be 1
    print(snowman)
    ds = snowman.encode('utf-8')
    print(len(ds))  # should be 3
    print(ds)

    # you can use different encodings, but make sure your encoding can process your Unicode value
    # (otherwise get exceptions)
    try:
        ds = snowman.encode('ascii')
        print(ds)
    except UnicodeError as err:
        print(err)

    # to avoid this, use a second argument like ignore, replace
    ds = snowman.encode('ascii', 'ignore')
    print(ds)
    ds = snowman.encode('ascii', 'replace')
    print(ds)

    # use 'backslashreplace' to create a string that contains only Python Unicode symbols like unicode-escape
    ds = snowman.encode('ascii', 'backslashreplace')
    print(ds)

    # use 'xmlcharrefreplace' to create HTML safety strings
    ds = snowman.encode('ascii', 'xmlcharrefreplace')
    print(ds)

    # decoding
    place = 'caf\u00e9'
    print(place)
    print(type(place))

    place_bytes = place.encode('utf-8')
    print(place_bytes)
    print(len(place_bytes))
    print(type(place_bytes))

    place2 = place_bytes.decode('utf-8')
    print(place2)
    print(type(place2))

    place3 = place_bytes.decode('ascii', 'replace')
    print(place3)

    place4 = place_bytes.decode('latin-1')
    print(place4)

    place4 = place_bytes.decode('windows-1252')
    print(place4)


if __name__ == '__main__':
    main()
