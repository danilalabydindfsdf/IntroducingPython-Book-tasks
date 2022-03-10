class Quote():
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


class BabblinBrook():
    def who(self):
        return 'Brook'

    def says(self):
        return 'Bubble'


def who_says(obj):
    print(f'{obj.who()} says {obj.says()}')


def main():
    hunter = Quote('Elmer Fudd', 'I am hunting NOW')
    print(f'{hunter.who()} says {hunter.says()}')

    hunter1 = QuestionQuote('Bugs Bunny', 'wazap doc')
    print(f'{hunter1.who()} says {hunter1.says()}')

    hunter2 = ExclamationQuote('Daffy Duck', 'It is a rabbit season')
    print(f'{hunter2.who()} says {hunter2.says()}')

    brook = BabblinBrook()

    who_says(brook)
    who_says(hunter)
    who_says(hunter1)
    who_says(hunter2)


if __name__ == '__main__':
    main()
    