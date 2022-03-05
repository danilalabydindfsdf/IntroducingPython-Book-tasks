import html


def main():
    # html mnemonic can be a handy method to encode and decode symbols
    symbol = html.unescape('&egrave;')
    print(symbol)


if __name__ == '__main__':
    main()
