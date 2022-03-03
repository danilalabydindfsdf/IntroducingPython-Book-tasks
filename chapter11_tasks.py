from collections import OrderedDict
from collections import defaultdict


def main():
    plain = {'a': 1, 'b': 2, 'c': 3}
    fancy = OrderedDict(plain)
    print(plain)
    print(fancy)
    dict_of_list = defaultdict(list)
    dict_of_list['a'] = 'something for a'
    print(dict_of_list['a'])


if __name__ == '__main__':
    main()
