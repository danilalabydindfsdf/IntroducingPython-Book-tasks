# create a class that represents a real-world object (a cat for example)
class Cat():
    # if you want to assign attributes to an object, you need to use a special method called '__init__'
    def __init__(self):
        ...


def main():
    # to create an object of any Class, use the following construction
    my_cat = Cat()
    another_cat = Cat()
    print(my_cat)
    print(another_cat)

    # attribute is a variable that locates inside a class or object
    my_cat.age = 10
    my_cat.name = 'Philya'
    print(my_cat.age, my_cat.name)

    # attribute can reference to other object
    my_cat.nemesis = another_cat
    print(my_cat.nemesis)

    # if you want to get access to different objects attributes, make sure the object has any attributes
    try:
        print(my_cat.nemesis.name)
    except AttributeError as err:
        print(err)
    my_cat.nemesis.name = 'Marysya'
    print(my_cat.nemesis.name)


if __name__ == '__main__':
    main()
