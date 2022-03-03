class Word():
    def __init__(self, text):
        self.text = text

    def __eq__(self, other):
        return self.text.lower() == other.text.lower()

    def __str__(self):
        return self.text


def main():
    first = Word('ha')
    second = Word('Ha')
    third = Word('eh')

    print(first == second)
    print(second == third)
    print(first)


if __name__ == '__main__':
    main()
