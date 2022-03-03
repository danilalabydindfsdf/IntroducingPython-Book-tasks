from collections import deque
import sys
import cProfile


def infinity_palindrome():
    num = 0
    while True:
        if is_palindrome_digit(num):
            i = (yield num)
            if i is not None:
                num = i
        num += 1


def is_palindrome_digit(num):
    # skip single-digit inputs
    if num // 10 == 0:
        return False
    temp = num
    reversed_num = 0

    while temp != 0:
        reversed_num = (reversed_num * 10) + (temp % 10)
        temp = temp // 10

    if num == reversed_num:
        return True
    return False


def multi_yield():
    yield_str = 'This will print the first string'
    yield yield_str
    yield_str = 'This will print the second string'
    yield yield_str


def is_palindrome(word):
    dq = deque(str(word))
    if len(dq) == 1:
        return False
    while len(dq) > 1:
        if dq.pop() != dq.popleft():
            return False
    return True


def csv_reader(file_name):
    for row in open(file_name, 'r'):
        yield row


def infinity_sequence():
    num = 0
    while True:
        yield num
        num += 1


def main():
    # use generator when you want to work with large datasets
    csv_gen = csv_reader('/home/lsbyd/generator_practice.csv')
    row_count = 0

    for _ in csv_gen:
        row_count += 1

    print(f'Row count is {row_count}')

    # generator comprehension
    csv_gen = (row for row in open('/home/lsbyd/generator_practice.csv'))
    print(csv_gen)

    # use generator to create an infinity sequence
    gen_seq = infinity_sequence()
    for _ in range(10):
        print(next(gen_seq))

    print(is_palindrome('0'))

    # use infinity sequence generator to get a running list of all numeric palindromes
    # for nb in infinity_sequence():
    #    if is_palindrome(nb):
    #       print(nb)

    # building generators with generator expressions
    nums_squared_lc = [num ** 2 for num in range(10000)]
    nums_squared_gc = (num ** 2 for num in range(10000))

    print(sys.getsizeof(nums_squared_lc), '- list')
    print(sys.getsizeof(nums_squared_gc), '- generator')

    cProfile.run('sum([i * 2 for i in range(10000)])')

    # understanding the python Yield statement
    multi_obj = multi_yield()
    print(next(multi_obj))
    print(next(multi_obj))

    # advanced Generator Methods(send, throw, close)
    pal_gen = infinity_palindrome()
    for i in pal_gen:
        digits = len(str(i))
        pal_gen.send(10 ** digits)


if __name__ == '__main__':
    main()
