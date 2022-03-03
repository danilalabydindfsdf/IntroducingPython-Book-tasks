class OopsException(Exception):
    pass


def test(func):
    def add_info(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print(result)
        print('End')
    return add_info


@test
def good():
    return ['Harry', 'Ron', 'Hermione']


def get_odds():
    for nb in range(10):
        if nb % 2 != 0:
            yield nb


print(good())
a = get_odds()
for i in a:
    print(i)

try:
    raise OopsException()
except OopsException as err:
    print('Caught an oops')

