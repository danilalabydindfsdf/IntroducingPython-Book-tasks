# there are 3 types of methods: object method, class method and static method
class A():
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(self):
        print('I am an A')

    @classmethod
    def kids(cls):
        print(f'A has {cls.count} little objects.')


def main():
    easy_a = A()
    breezy_b = A()
    wheezy_a = A()
    A.kids()


if __name__ == '__main__':
    main()
