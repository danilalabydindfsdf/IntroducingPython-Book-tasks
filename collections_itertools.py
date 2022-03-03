import itertools


from collections import defaultdict
from collections import Counter
from collections import deque


def summ_nested_items(nb_seq):
    for item in itertools.accumulate(nb_seq):
        if type(item) == list:
            item = itertools.accumulate(item)
            # ?


def no_idea():
    return 'Huh?'


def palindrome(word):
    dq = deque(word)
    while len(dq) > 1:
        if dq.pop() != dq.popleft():
            return False
    return True


def main():
    periodic_table = {'Hydrogen': 1, 'Helium': 2}
    print(periodic_table)
    carbon = periodic_table.setdefault('Carbon', 12)
    print(carbon)
    print(periodic_table)

    periodic_table = defaultdict(int)
    print(periodic_table)
    periodic_table['Hydrogen'] = 1
    print(periodic_table)
    periodic_table['Lead']
    print(periodic_table)

    bestiary = defaultdict(no_idea)
    bestiary['A'] = 'Abominable Snowman'
    bestiary['B'] = 'Basilisk'
    print(bestiary['A'])
    print(bestiary['B'])
    print(bestiary['C'])

    breakfast = ['spam', 'spam', 'eggs', 'spam']
    breakfast_counter = Counter(breakfast)
    print(breakfast_counter)
    print()
    print(breakfast_counter.most_common(2))

    lunch = ['eggs', 'eggs', 'bacon']
    lunch_counter = Counter(lunch)
    print(lunch_counter)

    print(breakfast_counter + lunch_counter)
    print(lunch_counter - breakfast_counter)
    print(breakfast_counter - lunch_counter)
    print(breakfast_counter & lunch_counter)
    print(breakfast_counter | lunch_counter)

    # stack + line == deque
    print(palindrome('abba'))
    print(palindrome('aaavvfdfg'))

    for item in itertools.chain([1, 2, [9, 8]], ['a', 'b']):
        print(item)

    #for item in itertools.cycle([1, 2]):
        #print(item)

    print()
    for item in itertools.accumulate([1, 2, 3, 4, 5, [1, 2]]):
        print(item)

    print('my_func')
    nbs = [1, 2, 3, 4, 5]



if __name__ == '__main__':
    main()
