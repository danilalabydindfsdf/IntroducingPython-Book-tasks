class Duck:
    def __init__(self, input_name):
        self.__name = input_name

    def get_name(self):
        print('inside the getter')
        return self.__name

    def set_name(self, input_name):
        print('inside the setter')
        self.__name = input_name
    name = property(get_name, set_name)


if __name__ == '__main__':
    don = Duck('Donald')
    print(don.get_name())
    print(don.set_name('Donna'))
    print(don.get_name())
    print(don.name)
